import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
	ret,frame= cap.read()
	hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	#hsv hue sat value
	lower_red=np.array([255,106,34])
	upper_red=np.array([255,146,94])

	mask =cv2.inRange(hsv,lower_red,upper_red)
	res = cv2.bitwise_and(frame , frame , mask = mask)

	#not working properly
	kernal= np.ones((15,15),np.float32)/255
	smoothed = cv2.filter2D(res,-1,kernal)

	#GaussianBlur is ok
	blur=cv2.GaussianBlur(res,(15,15),0)
	
	#median BLur ok when object is near but when object is far it is not working 
	median = cv2.medianBlur(res,15)
	
	#bilateral Filter is better for me you choose your one
	bilateral = cv2.bilateralFilter(res,15,75,75)


	cv2.imshow("frame",frame)
	#cv2.imshow("mask",mask)
	# cv2.imshow("res",res)
	# cv2.imshow("smoothed",smoothed)
	# cv2.imshow("GaussianBlur",blur)
	# cv2.imshow("Median Blur",median)
	cv2.imshow("bilateral blur",bilateral)

	k= cv2.waitKey(5)& 0xFF
	if k== 27:
		break
cv2.destroyAllWindows()
cap.release()