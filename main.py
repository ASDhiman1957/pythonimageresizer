import cv2

# Corrected the source filename (removed the trailing space)
source = "amitojsingh.jpeg"

# The destination variable seems unused in your snippet, so I'll use it in cv2.imwrite
destination = 'newImage.jpeg'

# Read the image. Ensure the file exists in your working directory or provide the full path.
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# Check if image is loaded properly
if src is None:
    print(f"Error: Unable to load image '{source}'.")
    exit()

# Percent by which the image is resized
scale_percent = 50

# Calculate the 50 percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# Resize image
output = cv2.resize(src, (new_width, new_height))

# Write the resized image to a file
cv2.imwrite(destination, output)

# If you want to display the image, uncomment the lines below
# cv2.imshow("Resized Image", output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Note: cv2.waitkey(0) had a typo; it should be cv2.waitKey(0).
# Also, if displaying the image in a window, it's good practice to close windows with cv2.destroyAllWindows()
