import cv2
import os


# Callback functions
def scaleImage(*args):
    global scaleFactor
    global scaleType

    # Get the scale factor from the trackbar
    scaleFactor = 1 + args[0]/100.0

    # Perform check if scaleFactor is zero
    if scaleFactor == 0:
        scaleFactor = 1

    # Resize the image
    scaledImage = cv2.resize(source, None, fx=scaleFactor,
                             fy=scaleFactor,
                             interpolation=cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)


# Callback functions
def scaleTypeImage(*args):
    global scaleType
    global scaleFactor
    scaleType = args[0]
    scaleFactor = 1 + scaleFactor/100.0
    if scaleFactor == 0:
        scaleFactor = 1
    scaledImage = cv2.resize(source, None, fx=scaleFactor,
                             fy=scaleFactor,
                             interpolation=cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)


# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Move up one directory level to the project directory
project_directory = os.path.join(current_directory, "")

# Create the path to the image
image_path = os.path.join(project_directory, "data/images", "truth.jpg")

source = cv2.imread(image_path, 1)

maxScaleUp = 100
scaleFactor = 1
scaleType = 0
maxType = 1

windowName = "Resize Image"
trackbarValue = "Scale"
trackbarType = "Type: \n 0: Scale Up \n 1: Scale Down"

# Create a window to display results
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp,
                   scaleImage)
cv2.createTrackbar(trackbarType, windowName, scaleType, maxType,
                   scaleTypeImage)

cv2.imshow(windowName, source)
c = cv2.waitKey(0)

cv2.destroyAllWindows()
