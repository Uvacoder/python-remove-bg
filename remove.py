import os
import rembg
import numpy as np
from PIL import Image

directory = "./output-2"
if not os.path.exists(directory):
    os.mkdir(directory)

# Set the path to the directory containing the images
input_directory = "dinosaur"

# Set the path to the directory to save the output images
output_directory = directory

# Set the desired output size for the images
new_size = (6000, 6000)

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

        # Create a new PIL Image object from the output
        bg_removed_image = Image.fromarray(output).convert("RGBA")

        # Create a new image with RGBA mode
        rgba_image = Image.new("RGBA", bg_removed_image.size)

        # Composite the background-removed image onto the RGBA image
        rgba_image.paste(bg_removed_image, (0, 0), bg_removed_image)

        # Save the resized and background-removed image to a new file with PNG format
        output_path = os.path.join(output_directory, "resized_" + os.path.splitext(filename)[0] + ".png")
        rgba_image.save(output_path, format="PNG")
        print("Image done:", filename)
