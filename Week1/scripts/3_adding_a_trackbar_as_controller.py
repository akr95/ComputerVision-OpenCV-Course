import cv2
import os

maxScaleUp = 100
scaleValue = 1
scaleType = 0
maxType = 1
scaleFactor = 1.0

windowName = "Resize Image"
trackbarValue = "Scale"
trackbarType = "Type: \n 0: Scale Up \n 1: Scale Down"

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Move up one directory level to the project directory
project_directory = os.path.join(current_directory, "..")

# Create the path to the image
image_path = os.path.join(project_directory, "data/images", "truth.png")

# load an image
im = cv2.imread(image_path)

# Create a window to display results
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)


# Callback functions
def scaleTypeImage(*args):
    global scaleType
    global scaleValue
    global scaleFactor
    scaleType = args[0]
    if scaleType == 1:
        scaleFactor = 1 - scaleValue/100.0
    else:
        scaleFactor = 1 + scaleValue/100.0
    if scaleFactor == 0:
        scaleFactor = 1
    scaledImage = cv2.resize(im, None, fx=scaleFactor,
                             fy=scaleFactor,
                             interpolation=cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)


def scaleImage(*args):
    global scaleValue
    global scaleType
    global scaleFactor
    scaleValue = args[0]
    if scaleType == 1:
        scaleFactor = 1 - scaleValue/100.0
    else:
        scaleFactor = 1 + scaleValue/100.0
    if scaleFactor == 0:
        scaleFactor = 1
    scaledImage = cv2.resize(im, None, fx=scaleFactor,
                             fy=scaleFactor,
                             interpolation=cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)


cv2.createTrackbar(trackbarValue, windowName, scaleValue,
                   maxScaleUp, scaleImage)
cv2.createTrackbar(trackbarType, windowName,
                   scaleType, maxType, scaleTypeImage)

scaleImage(10)

while True:
    c = cv2.waitKey(10)
    if c == 27:
        break

cv2.destroyAllWindows()
