import os
from PIL import Image
import rembg
import numpy as np


directory = "./output"
if not os.path.exists(directory):
    os.mkdir(directory)


# Set the path to the directory containing the images
input_directory = "input"

# Set the path to the directory to save the output images
output_directory = directory

# Set the desired output size for the images
new_size = (1000, 1000) # Optional

# Loop through all the files in the directory
for filename in os.listdir(input_directory):
    # Check if the file is a valid image file
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image file
        image_path = os.path.join(input_directory, filename)
        image = Image.open(image_path)

        # Resize the image to the new size
        resized_image = image.resize(new_size)

        # Convert the image to a NumPy array
        np_image = np.array(resized_image)

        # Remove the background from the image using rembg
        output = rembg.remove(np_image)

        # Convert the output to a PIL Image object
        bg_removed_image = Image.fromarray(output)

        # Save the resized and background-removed image to a new file
        output_path = os.path.join(output_directory, "resized_" + filename)
        bg_removed_image.save(output_path)
        print("image done")
