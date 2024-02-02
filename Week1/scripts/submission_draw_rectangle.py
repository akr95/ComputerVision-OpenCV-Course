import cv2
import os


# start data
startValue = []
endValue = []


def drawRectangle(action, x, y, flags, userdata):
    # Referencing global variables
    global startValue, endValue

    # draw rectangle over face
    if action == cv2.EVENT_LBUTTONDOWN:
        startValue = [(x, y)]

    elif action == cv2.EVENT_LBUTTONUP:
        endValue = [(x, y)]
        cv2.rectangle(source, startValue[0], endValue[0], (255, 0, 0), 3)

        startValue.clear()
        endValue.clear()


# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Move up one directory level to the project directory
project_directory = os.path.join(current_directory, "..")

# Create the path to the image
image_path = os.path.join(project_directory, "data/images", "sample.jpg")

source = cv2.imread(image_path, 1)
# Make a dummy image, will be useful to clear the drawing
dummy = source.copy()
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawRectangle)

k = 0
# loop until escape character is pressed
while k != 27:
    cv2.imshow("Window", source)
    cv2.putText(source, '''Choose center, and drag, 
                        Press ESC to exit and c to clear''',
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                0.7, (255, 255, 255), 2)
    k = cv2.waitKey(20) & 0xFF
    # Another way of cloning
    if k == 99:
        source = dummy.copy()

cv2.destroyAllWindows()
