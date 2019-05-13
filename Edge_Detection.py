import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
	ret,frame= cap.read()
	
	"""
	the cv2.CV_64F is, that's the data type. 
	ksize is the kernel size.
	 We use 5, so 5x5 regions are consulted.
	"""
	laplacian =cv2.Laplacian(frame,cv2.CV_64F)
	#FOR x gradient
	sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
	#FOR Y gradient
	sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

	"""Canny edges Detection  First argument is our input image.
	Second 
	and third arguments are our minVal and maxVal respectively"""
	edge = cv2.Canny(frame,100,100)

	cv2.imshow("frame",frame)
	#cv2.imshow("laplacian",laplacian)
	# cv2.imshow("sobelx",sobelx)
	# cv2.imshow("sobely",sobely)
	cv2.imshow("Edge",edge)
	k= cv2.waitKey(5)& 0xFF
	if k== 27:
		break
cv2.destroyAllWindows()
cap.release()