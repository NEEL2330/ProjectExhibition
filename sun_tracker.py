import cv2

# Load the image (replace 'sky_photo.jpg' with the path to your image)
image = cv2.imread('sky_photo.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to highlight the sun
_, threshold_image = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)

# Find contours of bright areas (sun)
contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    # Find the largest contour (which should be the sun)
    sun_contour = max(contours, key=cv2.contourArea)

    # Find the center of the sun
    M = cv2.moments(sun_contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])  # x-coordinate of the sun
        cy = int(M["m01"] / M["m00"])  # y-coordinate of the sun
        print(f"The sun is located at: ({cx}, {cy}) in the image")
    else:
        print("Sun not found")
else:
    print("No bright area found")

# Camera's field of view (in degrees)
fov_horizontal = 60  # Horizontal field of view (adjust based on your camera)
fov_vertical = 40    # Vertical field of view

# Image dimensions
image_width = image.shape[1]
image_height = image.shape[0]

# Calculate the image center
center_x = image_width // 2
center_y = image_height // 2

# Calculate azimuth and elevation
azimuth = (cx - center_x) / image_width * fov_horizontal
elevation = (center_y - cy) / image_height * fov_vertical

print(f"Sun's azimuth: {azimuth} degrees")
print(f"Sun's elevation: {elevation} degrees")

# Suggest optimal panel direction
optimal_tilt = elevation  # The tilt should match the sun's elevation
optimal_azimuth = azimuth  # The azimuth should match the sun's azimuth

print(f"Optimal panel tilt: {optimal_tilt} degrees")
print(f"Optimal panel azimuth: {optimal_azimuth} degrees")

# Display images
cv2.imshow('Original Image', image)
cv2.imshow('Threshold Image', threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
