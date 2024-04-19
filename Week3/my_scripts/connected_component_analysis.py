
# Analysis of the numebr plate, using connected component analysis

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'


# dir path 
dirpath = os.path.dirname(os.path.abspath(__file__))

# join the os path
imagefolder = os.path.join(dirpath, "..")

# get image path
imgpath = os.path.join(imagefolder, "data/images/", "number-plate.jpg")

# read image
img = cv2.imread(imgpath)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply thresholding grey image to binary
_, img_thresh = cv2.threshold(img, 0, 255,
                              cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

cv2.imshow("thresholding ", img_thresh)
cv2.waitKey(0)

# perform connected component analysis
imgLabel = cv2.connectedComponentsWithStats(img_thresh, connectivity=8,
                                            ltype=cv2.CV_32S)

(numlabels, labels, stats, centeroids) = imgLabel

# initialize the zero numoy for masking the number palte

mask = np.zeros(img.shape, dtype="uint8")

for i in range(numlabels):

    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]
    area = stats[i, cv2.CC_STAT_AREA]
    (cx, cy) = centeroids[i]

    imgcopy = img.copy()
    cv2.rectangle(imgcopy, (x, y), ((x+w), (y+h)), (0, 255, 0), 2)
    cv2.circle(imgcopy, (int(cx), int(cy)), 7, (0, 0, 255), -1)

    # extract the number only from plate
    width = w > 10 and w < 60
    height = h > 50 and h < 90
    area = area > 2100 and area < 3200

    component = (labels == i).astype("uint8") * 255
    
    if all((width, height, area)):
        imgcopy = cv2.cvtColor(imgcopy, cv2.COLOR_BGR2RGBA)
        mask = cv2.bitwise_or(mask, component)

cv2.imshow("img ", imgcopy)
cv2.imshow("component ", mask)

cv2.waitKey(0)
