
# coding: utf-8

# # <font style = "color:rgb(50,120,229)">Implementation of Morphological Operations</font>
# We had discussed how to use dilation and erosion operations in the previous section. In this section, we will see what is going on under the hood. The most important concept that you need to understand is the Structuring element. We will discuss about the structuring element and how it is used for performing these morphological operations.

# ## <font style="color:rgb(50,120,229)">Implement Method 2</font>
# 1. Scan through the image and superimpose the kernel on the neighborhood of each pixel. 
# 1. Perform an AND operation of the neighborhood with the kernel.
# 1. Replace the pixel value with the `maximum` value in the neighborhood given by the kernel. 
# 
# This means that you check every pixel and its neighborhood with respect to the kernel and change the pixel to white if any of the pixel in this neighborhood is white. OpenCV implements an optimized version of this method. This will work even if the image is not a binary image.

# ## <font style="color:rgb(50,120,229)">Import Libraries </font>

# In[2]:

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


import matplotlib

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'


# # <font style="color:rgb(50,120,229)">Create a Demo Image</font>
# ## <font style="color:rgb(50,120,229)">Create an empty matrix </font>

# In[4]:


im = np.zeros((10,10),dtype='uint8')
print(im);
plt.imshow(im)


# ## <font style="color:rgb(50,120,229)">Lets add some white blobs</font>
# 
# We have added the blobs at different places so that all boundary cases are covered in this example.

# In[5]:


im[0,1] = 1
im[-1,0]= 1
im[-2,-1]=1
im[2,2] = 1
im[5:8,5:8] = 1

print(im)
plt.imshow(im)


# This becomes our demo Image for illustration purpose

# ## <font style="color:rgb(50,120,229)">Create an Ellipse Structuring Element </font>
# Let us create a 3x3 ellipse structuring element.

# In[6]:


element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
print(element)


# In[7]:


ksize = element.shape[0]


# In[8]:


height, width = im.shape[:2]


# ## <font style="color:rgb(50,120,229)">First check the correct output using cv2.dilate</font>

# In[9]:


dilatedEllipseKernel = cv2.dilate(im, element)
print(dilatedEllipseKernel)
plt.imshow(dilatedEllipseKernel)


# ## <font style="color:rgb(50,120,229)">Write Code for Dilation from scratch</font>
# 
# Create a VideoWriter object and write the result obtained at the end of each iteration to the object. Save the video to **`dilationScratch.avi`** and display it using markdown below:
# 
# **`dilationScratch.avi` will come here**
# 
# ```<video width="320" height="240" controls>
#   <source src="dilationScratch.avi" type="video/mp4">
# </video>```
# 
# **Note**
# 
# 1. Use FPS as 10 and frame size as 50x50
# 2. Before writing the frame, resize it to 50x50
# 3. Convert the resized frame to BGR
# 4. Release the object

# In[ ]:


border = ksize//2
paddedIm = np.zeros((height + border*2, width + border*2))
paddedIm = cv2.copyMakeBorder(im, border, border, border, border, cv2.BORDER_CONSTANT, value = 0)
paddedDilatedIm = paddedIm.copy()

# Create a VideoWriter object
# Use frame size as 50x50
out = cv2.VideoWriter('dilationScratch.avi',
                      cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (50, 50))

resizeWidth = 50
resizeheight = 50

for h_i in range(border, height+border):
    for w_i in range(border, width+border):
        
        dst = cv2.bitwise_and(dilatedEllipseKernel, paddedDilatedIm)

        # Resize output to 50x50 before writing it to the video
        resize = cv2.resize(dst, (resizeWidth, resizeheight),
                            interpolation=cv2.INTER_LINEAR)
       
        # # Convert resizedFrame to BGR before writing
        video = cv2.cvtColor(resize, cv2.COLOR_GRAY2BGR)
        
        if not resize.any():
            print("Empty frame detected")
        else:
            out.write(video)

# Release the VideoWriter object
out.release()

# Display final image (cropped)
plt.imshow(dst)
plt.show()


# # <font style="color:rgb(50,120,229)">Implement Erosion </font>

# ## <font style="color:rgb(50,120,229)">Check the correct output using cv2.erode </font>

# In[ ]:


ErodedEllipseKernel = cv2.erode(im, element)
print(ErodedEllipseKernel)
plt.imshow(ErodedEllipseKernel)


# ## <font style="color:rgb(50,120,229)">Write code for Erosion from scratch</font>
# 
# Create a VideoWriter object and write the result obtained at the end of each iteration to the object. Save the video to **`erosionScratch.avi`** and display it using markdown below:
# 
# **`erosionScratch.avi` will come here**
# 
# ```<video width="320" height="240" controls>
#   <source src="erosionScratch.avi" type="video/mp4">
# </video>```
# 
# **Note**
# 
# 1. Use FPS as 10 and frame size as 50x50
# 2. Before writing the frame, resize it to 50x50
# 3. Convert the resized frame to BGR
# 4. Release the object

# In[ ]:


border = ksize//2
paddedIm = np.zeros((height + border*2, width + border*2))
paddedIm = cv2.copyMakeBorder(im, border, border, border, border, cv2.BORDER_CONSTANT, value = 1)
paddedErodedIm = paddedIm.copy()

# Create a VideoWriter object
# Use frame size as 50x50
out = cv2.VideoWriter('erosionScratch.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10, (50,50))

resizeWidth = 50
resizeheight = 50

for h_i in range(border, height+border):
    for w_i in range(border,width+border):
        erode = cv2.erode(paddedErodedIm, ErodedEllipseKernel, iterations=1)
        
        # Resize output to 50x50 before writing it to the video
        size = cv2.resize(erode, (resizeWidth, resizeheight), interpolation=cv2.INTER_NEAREST)
        
        # print(resize)
        
        # Convert resizedFrame to BGR before writing
        video = cv2.cvtColor(size, cv2.COLOR_GRAY2BGR)
        
        # print("video ", video)
        
        out.write(video)
# Release the VideoWriter object
out.release()


# In[ ]:


# Display final image (cropped)
plt.imshow(erode)
plt.show()


# In[ ]:




