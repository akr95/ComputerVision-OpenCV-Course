# Connected Component Analysis

# Two pass algo:
# 1st pass we label the pixel and save the eqvivalent label info.
# 2nd pass we re-assign the same label of the equivalent label.


import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'


# directory path
current_dir = os.path.dirname(os.path.abspath(__file__))

project_dir = os.path.join(current_dir, "..")

image_path = os.path.join(project_dir, "data/images/", "truth.png")

# read image as grayscale
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
plt.imshow(img)

# apply thresholding: thresholding convert greyscale or RCG to binary image
th, imthresholding = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# find connected components
_, imgLabels = cv2.connectedComponents(imthresholding)
print("img labels ", imgLabels)

# display each labels
ncomponents = imgLabels.max()

displayRows = np.ceil(ncomponents / 3.0)
plt.figure(figsize=[20, 12])

for i in range(ncomponents + 1):
    print(int(displayRows))
    plt.subplot(int(displayRows), 3, i+1)
    plt.imshow(imgLabels == 1)
    if i == 0:
        plt.title("backgrouind {}".format(i))
    else:
        plt.title("component id {}".format(i))

    # the following line to find the min, max pixela nd location values.
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(imgLabels)

    # normalize the pixel value of the image, 0 to 255
    imgLabels = 255 * (imgLabels - minVal)/(maxVal - minVal)

    # convert image to uint 8-bits
    imgLabels = np.uint8(imgLabels)

    # apply color map to the labeled image
    imcolormap = cv2.applyColorMap(imgLabels, cv2.COLORMAP_JET)

    plt.imshow(imcolormap[:,:,::-1])
    plt.show()
