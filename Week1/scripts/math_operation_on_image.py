# Brightness and contrast adjustments
# Two commonly used point processes are multiplication and addition with a constant:

# g(x)=αf(x)+β
# The parameters α>0 and β are often called the gain and bias parameters; sometimes these parameters are said to control contrast and brightness respectively.
# You can think of f(x) as the source image pixels and g(x) as the output image pixels. Then, more conveniently we can write the expression as:

# g(i,j)=α⋅f(i,j)+β
# where i and j indicates that the pixel is located in the i-th row and j-th column.



from turtle import title
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

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
# print("image dimension : ", image.shape)
# Scale the values so that they lie between [0,1]
image = image * scalingFactor

# print("image after conversion ", image)

# Convert back to unsigned int
image = image * (1.0/scalingFactor)

image = np.uint8(image)

# print("image convert to uint ", image)

# CONTRAST enhancement
# In this approach, a scale factor (  α ) is multiplied
# with intensity values of all the pixels. Given below is
# the code snippet to do the same. Intensity scaling is
# represented by the following equation
#          Io=αI
constrastValue = 30

constrastImage = image * (1+constrastValue/100)
# clipped the constrast image in between 0, 255
clippedConstrastImage = np.clip(constrastImage, 0, 255)
constrastImageCliipedUint8 = np.uint8(clippedConstrastImage)

plt.figure(figsize=[10,10])
plt.subplot(121);plt.imshow(image[...,::-1]);plt.title("orignal Image");
plt.subplot(122);plt.imshow(constrastImageCliipedUint8[...,::-1]);plt.title("constrast Image");
plt.show()

# Brightness enhancement
# If I is the input image, and  Io is the output image, brightness enhanced image is given by the equation
#                               Io=I+β

enhancementOffset = 40

# Add the offset for increasing brightness
image_int32 = np.int32(image)
ehancementImage = image_int32 + enhancementOffset
clippedIMage = np.clip(ehancementImage, 0, 255)

plt.figure(figsize=[10,10])
plt.subplot(121);plt.imshow(image[...,::-1]);plt.title("orignal Image");
plt.subplot(122);plt.imshow(clippedIMage[...,::-1]);plt.title("ehancement Image");
plt.show()
