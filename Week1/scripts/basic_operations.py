import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Move up one directory level to the project directory
project_directory = os.path.join(current_directory, "..")

# Create the path to the image
image_path = os.path.join(project_directory, "data/images", "boyjpg")

print(cv2.__version__)

# #### Read an image ####

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.path.exists('../data/images/boy.jpg'))
img = cv2.imread("../data/images/boy.jpg")
print(img)

# display image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# create empty matrix
empty_matrix = np.zeros((100, 200, 3), dtype='uint8')
# convert bgr image to rgb(because cv2 read img as bgr instead of rgb)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

# Create a empty matrix of the same size as original image
emptyOrorigiinal = 100*np.ones_like(img)
plt.imshow(emptyOrorigiinal)
plt.show()

# cropping the aimage
cv2.imshow("crop image ", img[40:200, 170:320])
cv2.waitKey(0)
cv2.destroyAllWindows()

print("dimension ", img.shape)
# copy image
copyRoi = img[40:200, 180:320]
roiHeight, roiWidth = copyRoi.shape[:2]

# copy left to right face
copiedImg = img.copy()

# find height and width of roi image
roiheight, roiWidth = copyRoi.shape[:2]

# copy left to face
copiedImg[40:40+roiHeight, 10:10+roiWidth] = copyRoi

# copy right to face
copiedImg[40:40+roiHeight, 330:330+roiWidth] = copyRoi

# display the output
plt.figure(figsize=[15, 15], facecolor='black', edgecolor='blue', )
plt.subplot(131);plt.imshow(img[...,::-1]);plt.title("original img")
plt.subplot(132);plt.imshow(copiedImg[...,::-1]);plt.title("modified img")
plt.subplot(133);x = [10, 20, 50, 20];plt.pie(x, colors="r")
plt.show()
