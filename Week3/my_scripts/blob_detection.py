# blob detection

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
file_name = os.path.join(folder_path, "data/images", "blob_detection.jpg")

img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200
 
# Filter by Area.
params.filterByArea = True

params.minArea = 150
 
# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1
 
# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87
 
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01
 
# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(img)

img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# Mark blobs using image annotation concepts we have studied so far
for k in keypoints:
    x, y = k.pt
    x = int(round(x))
    y = int(round(y))
    # Mark center in BLACK
    cv2.circle(img, (x, y), 5, (0, 0, 0), -1)
    # Get radius of blob
    diameter = k.size
    radius = int(round(diameter/2))
    # Mark blob in RED
    cv2.circle(img, (x, y), radius, (130, 0, 255), 2)

# Let's see what image we are dealing with
plt.imshow(img[:,:,::-1])
plt.show()
