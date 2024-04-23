
# contours

import cv2
import numpy
import os
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

# director path
dir_name = os.path.dirname(os.path.abspath(__file__))

# folderpath
folder_path = os.path.join(dir_name, "..")

# file_name
file_name = os.path.join(folder_path, "data/images", "Contour.png")

img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

# convert to binary image
_, thres_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

contours, hierachy = cv2.findContours(thres_img, mode=cv2.RETR_TREE,
                                      method=cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))
print(hierachy)

# draw contours
img = cv2.drawContours(thres_img, contours, -1, (135, 255, 0), 6)

# properties of the contours
# 1. find the center of the mass or centeroid

for i in range(len(contours)):
    print("index ", i)
    moments = cv2.moments(contours[i])
    x = int(moments['m10']/moments['m00'])
    y = int(moments['m01']/moments['m00'])

    cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    cv2.circle(img, (x, y), 10, (200, 160, 255), -1)

cv2.imshow("img", img)
cv2.waitKey(0)