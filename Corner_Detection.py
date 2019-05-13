import numpy as np 
import cv2 
import matplotlib.pyplot as plt 

cam=cv2.VideoCapture(0)
while True:
	_,img = cam.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray =np.float32(gray)
	#The parameters here are the image, max corners to detect, quality, and minimum distance between corners
	corners =cv2.goodFeaturesToTrack(gray,5,0.1,10)
	corners =np.int0(corners)
	for corner in corners:
		x,y= corner.ravel()
		cv2.circle(img,(x,y),3,250,-1)

	cv2.imshow("image",img)
	k= cv2.waitKey(5)& 0xFF
	if k== 27:
		break
cv2.waitKey(0)