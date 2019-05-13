import cv2
import numpy as np 

nose = cv2.CascadeClassifier("nose.xml")
cam = cv2.VideoCapture(0)

while True:
	ret,image=cam.read()
	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	Nose = nose.detectMultiScale(gray)
	for (x,y,w,h) in Nose:
		center = (x + w//2, y + h//2)
		image = cv2.ellipse(image, center, (w//2, h//2), 0, 0, 360, (255, 0, 255),2)
	cv2.imshow("image",image)
	k = cv2.waitKey(30) & 0xff
	if(k==27):
		break
cv2.destroyAllWindows()
cam.release()