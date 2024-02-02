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

# make a copy of orginal image
faceImageCopy = faceImage.copy()

# get the eye region from face image
eyeROI = faceImageCopy[topLeftRow:bottomRightRow, topLeftCol:bottomRightCol]

print(eyeROI)

# Use the mask to create the masked eye region
eye = cv2.bitwise_and(eyeROI, cv2.bitwise_not(glassMask))

print("eye ", eye)

# Use the mask to create the masked sunglass region
sunglass = cv2.bitwise_and(glassBGR, glassMask)

print("sunglass ", sunglass)

# Combine the Sunglass in the Eye Region to get the augmented image
eyeRoiFinal = np.clip(cv2.bitwise_xor(eye, sunglass), 0, 1)

# add transparent into glass.
maskedEyeB = cv2.addWeighted(eye, 0, glassMask, 0.5, 0.0)

maskedEye = cv2.multiply(eyeROI, 1-maskedEyeB)

# replace eyeROI with main image.
faceImageCopy[topLeftRow:bottomRightRow,
              topLeftCol:bottomRightCol] = maskedEye

# draw a line
cv2.line(faceImageCopy, (150, 80), (400, 80), (0, 0, 255), thickness=3,
         lineType=cv2.LINE_AA)

print("faceImageCopy", faceImageCopy)

# draw a circle  , set -1 thickness tof ill the circle.
cv2.circle(faceImageCopy, (280, 250), 200, (0, 255, 0), thickness=3,
           lineType=cv2.LINE_AA)

# draw a eclipse
# Function Syntax
# ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]) -> img
# The mandatory arguments are as follows.

# img: Image on which the ellipse is to be drawn.
# center: Center of the ellipse.
# axes: radius of the ellipse major and minor axes.
# angle: Ellipse rotation angle in degrees.
# startAngle: Starting angle of the elliptic arc in degrees.
# endAngle: Ending angle of the elliptic arc in degrees.
# color: Ellipse line color
cv2.ellipse(faceImageCopy, (280, 250), (100, 50), 0, 0, 360,
            (255, 0, 0), thickness=3, lineType=cv2.LINE_AA)

cv2.ellipse(faceImageCopy, (280, 250), (100, 50), 50, 0, 360,
            (0, 0, 255), thickness=-3, lineType=cv2.LINE_AA)

# draw rectangle
# Function Syntax
# rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
cv2.rectangle(faceImageCopy, (100, 50), (500, 200),
              (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)


# write a text
# Function Syntax¶
# putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) -> img
# The mandatory arguments that we need to focus on are:

# img: Image on which the text has to be written.
# text: Text string to be written.
# org: Bottom-left corner of the text string in the image.
# fontFace: Font type
# fontScale: Font scale factor that is multiplied by the font-specific base size.
# color: Font color
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontThickness = 2
message = "Hello"
fontScale = 1.5
fontColor = (250, 10, 10)

# solve font scale issue
# Function Syntax 
# fontScale   =   cv2.getFontScaleFromHeight( fontFace, pixelHeight[, thickness]  )
# Parameters

# fontFace - Font to use
# pixelHeight - Pixel height to compute the fontScale for
# thickness - Thickness of lines used to render the text. See putText for details
# fontScale (Output) - The fontsize to use in cv2.putText() function.
pixelHeight = 20
fontScale = cv2.getFontScaleFromHeight(fontFace, pixelHeight,
                                       fontThickness)

# get image width and height
imageGetTextSize = faceImageCopy.copy()
imageWidth, imageHeight = imageGetTextSize.shape[:2]

# Get height and width of text
fontGetTextSize, basline = cv2.getTextSize(message, fontFace, fontScale,
                                           fontThickness)

textWidth, textHeight = fontGetTextSize
print("imageWidth ", imageWidth)
print("textWidth ", textWidth)
# get cordinates
xcordinate = int((imageWidth-textWidth)/2)
ycordinate = int(imageHeight - basline - 10)
print("cxcordinate ", xcordinate)
print("ycordinate ", ycordinate)
# draw canvas (rectangle)
canvasColor = (255, 255, 255)
canvasBottomLeft = (xcordinate, ycordinate + basline)
canvasTopRight = (xcordinate+textWidth, ycordinate - textHeight)
print("canvas bottom left", canvasBottomLeft)
print("canvas top right ", canvasTopRight)
cv2.rectangle(imageGetTextSize, (canvasBottomLeft), canvasTopRight, canvasColor,
              thickness=1, lineType=cv2.LINE_AA)

# draw baseline
lineThickness = 2
lineLeft = (xcordinate, ycordinate) 
lineRight = (xcordinate + textWidth, ycordinate)
lineColor = (0, 255, 0)
cv2.line(imageGetTextSize, lineLeft, lineRight, lineColor, lineThickness)

# draw a text now
cv2.putText(imageGetTextSize, message, (50 , 50),
            fontFace, fontScale,
            fontColor, thickness=fontThickness, lineType=cv2.LINE_AA)


# plt.figure(figsize=[20, 10])
# plt.subplot(121);plt.imshow(eyeRoiFinal[:,:,::-1]);plt.title("eyeROIFinal")
# plt.subplot(122);plt.imshow(faceImageCopy[:,:,::-1]);plt.title("faceImageCopy")
# plt.show()

# cropping the aimage
cv2.imshow("crop image ", imageGetTextSize)
cv2.waitKey(0)
cv2.destroyAllWindows()