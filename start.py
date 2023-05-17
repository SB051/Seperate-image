from PIL import Image
import os

# Set the input and output directories
input_dir = './images'
output_dir = './Cropped'

# Create the output directory if it doesn't already exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is a PNG or JPEG image
    if filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
        # Open the image file
        img = Image.open(os.path.join(input_dir, filename))

        # Get the width and height of the image
        width, height = img.size

        # Calculate the coordinates of the four quadrants
        top_left = (0, 0, width // 2, height // 2)
        top_right = (width // 2, 0, width, height // 2)
        bottom_left = (0, height // 2, width // 2, height)
        bottom_right = (width // 2, height // 2, width, height)

        # Crop the image to each quadrant and save it to the output directory with a suffix
        for i, quadrant in enumerate([top_left, top_right, bottom_left, bottom_right]):
            quadrant_img = img.crop(quadrant)
            output_filename = f"{os.path.splitext(filename)[0]}_{i}.png"
            output_path = os.path.join(output_dir, output_filename)
            quadrant_img.save(output_path)
