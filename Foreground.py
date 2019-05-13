import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('img.jpg')
cv2.imshow("hjg",img)
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
#set the diagonal of rectangle where foreground is in
rect = (264,187,159,175)

"""
First the input image, then the mask, then the rectangle for our main object, 
the background model, foreground model, the amount of iterations to run, and what mode you are using.
"""
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img),plt.colorbar(),plt.show()