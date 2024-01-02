
import cv2
import os
import numpy as np

# Data type conversion
# read an image means 8 bit per channel. intensity value 0-255 unsigned
# image gradiient cold be negative.

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Move up one directory level to the project directory
project_directory = os.path.join(current_directory, "..")

# Create the path to the image
image_path = os.path.join(project_directory, "data/images", "boy.jpg")

# Read image
image = cv2.imread(image_path)

scalingFactor = 1/255.0
# Convert unsigned int to float
image = np.float32(image)
print("image dimension : ", image.shape)
# Scale the values so that they lie between [0,1]
image = image * scalingFactor

print("image after conversion ", image.shape)

# Convert back to unsigned int
image = image * (1.0/scalingFactor)

image = np.uint8(image)

print("image convert to uint ", image.shape)

# contrast enhancement
