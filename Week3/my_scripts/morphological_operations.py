# in this script we will perform dilation and erosion operations.

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

current_dir = os.path.dirname(os.path.abspath(__file__))

project_dir = os.path.join(current_dir, "..")

image_path = os.path.join(project_dir, "data/images/", "dilation_example.jpg")

# read image and convert to binary image

img = cv2.imread(image_path)

k = (3, 3)
kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, k)

# perform dilation by using dilate function.
dst = cv2.dilate(img, kernel1, iterations=1)
dst = cv2.dilate(img, kernel1, iterations=2)

image_path = os.path.join(project_dir, "data/images/", "erosion_example.jpg")

# read image and convert to binary image

img = cv2.imread(image_path)

k = (3, 3)
kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, k)

# perform dilation by using dilate function.
dst = cv2.erode(img, kernel1, iterations=1)
dst = cv2.erode(img, kernel1, iterations=2)

plt.imshow(dst)
plt.show()
