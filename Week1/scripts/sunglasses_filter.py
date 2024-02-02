from turtle import title
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Move up one directory level to the project directory
project_directory = os.path.join(current_directory, "..")

# Create the path to the image
image_path = os.path.join(project_directory, "data/images", "musk.jpg")

print(cv2.__version__)

# #### Read an image ####

faceImage = cv2.imread(image_path)
faceImage = np.float32(faceImage)/255

# Read the glasses images
glassImage = cv2.imread(os.path.join(project_directory, "data/images", "sunglass.png"), -1)
glassImage = np.float32(glassImage)/255

# resize the images
glassImage = cv2.resize(glassImage, None, fx=0.5, fy=0.5)
glassHeight, glassWidth, nChannels = glassImage.shape

# separate the color channel
glassBGR = glassImage[:,:,0:3]
glassAlpha = glassImage[:,:,3]

# Cordinate to place glass
topLeftRow = 130
topLeftCol = 130

bottomRightRow = topLeftRow + glassHeight
bottomRightCol = topLeftCol + glassWidth

# create face image with 3 channel
glassMask = cv2.merge((glassAlpha, glassAlpha, glassAlpha))

print(glassMask)

# make a copy of orginal image
faceImageCopy = faceImage.copy()

# get the eye region from face image
eyeROI = faceImageCopy[topLeftRow:bottomRightRow, topLeftCol:bottomRightCol]

# Use the mask to create the masked eye region
maskedEye = cv2.multiply(eyeROI, (1 - glassMask))

# Use the mask to create the masked sunglass region
maskedGlass = cv2.multiply(glassBGR, glassMask)

# combined the sunglass in the eye region to get the augmented image
eyeROIFinal = cv2.add(maskedEye, maskedGlass)

# add transparent into glass.
maskedEyeB = cv2.addWeighted(maskedEye, 0, glassMask, 0.5, 0.0)
maskedEye = cv2.multiply(eyeROI, (1 - maskedEyeB))

# replace eyeROI with main image.
faceImageCopy[topLeftRow:bottomRightRow,
              topLeftCol:bottomRightCol] = maskedEye

plt.figure(figsize=[20, 10])
plt.subplot(121);plt.imshow(eyeROIFinal[:,:,::-1]);plt.title("eyeROIFinal")
plt.subplot(122);plt.imshow(faceImageCopy[:,:,::-1]);plt.title("faceImageCopy")
plt.show()
