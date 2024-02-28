import cv2, time
import os
import numpy as np
import matplotlib.pyplot as plt


# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Move up one directory level to the project directory
project_directory = os.path.join(current_directory, "..")

# Create the path to the image
image_path = os.path.join(project_directory, "data/images", "IMG_5229.jpg")

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # read grey scale image

print(img.dtype)

# set the thresholding and maximum value
thresh = 150
maxValue = 255

# calculation of the calcualtion
t = time.time()
th, dst = cv2.threshold(img, thresh, maxValue, cv2.THRESH_TOZERO_INV)

adpt = cv2.adaptiveThreshold(img, maxValue, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY, 31, 1)
print("time taken = {} seconds ".format(time.time()-t))

blur = cv2.GaussianBlur(img, (5, 5), 0)
th, tsto = cv2.threshold(blur, 0, maxValue,
                         cv2.THRESH_BINARY+cv2.THRESH_OTSU)

plt.figure(figsize=[20, 5])
plt.subplot(121);plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB));plt.title("Original image")
plt.subplot(122);plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB));plt.title("Thresholding image")
# plt.subplot(133);plt.imshow(adpt);plt.title("Adpative image")
plt.show()

# img_sub = img[70:170, 420:550].copy()
# img_sub[img_sub == 200] = 1
# img_sub[img_sub == 0] = 1
# img_sub[img_sub != 1] = 0
# plt.imshow(img_sub)
# plt.show()
