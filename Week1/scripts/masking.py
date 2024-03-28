import cv2
import os
import numpy as np

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Move up one directory level to the project directory
project_directory = os.path.join(current_directory, "...")

# Create the path to the image
videoPath = os.path.join(project_directory, "", "output.mp4")

# start the video
cap = cv2.VideoCapture(1)

print(os.path.exists(videoPath))

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while cap.isOpened():
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv values to detect the green color
    lowerValue = np.array([12, 100, 30])
    upperValue = np.array([30, 250, 250])

    mask = cv2.inRange(hsv, lowerValue, upperValue)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15, 15), np.float32)/225
    smoothed = cv2.filter2D(res, -1, kernel)

    blur = cv2.GaussianBlur(res, (15, 15), 0)
    median = cv2.medianBlur(res, 15)
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    # morological transformation
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    opening = cv2.morphologyEx

    cv2.imshow("frame ", frame)
    # cv2.imshow("mask frame ", mask)
    cv2.imshow("res frame ", res)
    # cv2.imshow("smoothed", smoothed)
    # cv2.imshow("blur", blur)
    # cv2.imshow("median", median)
    # cv2.imshow("bilateral", bilateral)
    cv2.imshow("erosion frame ", erosion)
    cv2.imshow("dilation frame ", dilation)

    c = cv2.waitKey(10)
    if c == 27:
        break


cv2.destroyAllWindows()
cap.release()