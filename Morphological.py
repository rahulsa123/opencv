import cv2
import numpy as np 
cap = cv2.VideoCapture(0)

while True:
	ret,frame=cap.read()

	hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	upper_green=np.array([150,255,170])
	lower_green=np.array([80,164,71])

	mask = cv2.inRange(hsv,lower_green,upper_green)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	"""
	Erosion(expend) is where we will "erode" the edges. 
	The way these work is we work with a slider (kernel). 
	We give the slider a size, let's say 5 x 5 pixels. 
	What happens is we slide this slider around, 
	and if all of the pixels are white, then we get white, 
	otherwise black. This may help eliminate some white noise. 
	The other version of this is Dilation, 
	which basically does the opposite: Slides around, 
	if the entire area isn't black, then it is converted to 
	white
	"""
	keranl = np.ones((5,5),np.uint8)
	erosion = cv2.erode(mask,keranl,iterations=1)
	dilation = cv2.dilate(mask,keranl,iterations=1)
 	

	"""
	he goal with opening is to remove "false positives" so to speak. 
	ometimes, in the background, you get some pixels here and there 
	of "noise." The idea of "closing" is to remove false negatives. 
	Basically this is where you have your detected shape, like our hat,
	 and yet you still have some black pixels within the object.
	 Closing will attempt to clear that up.

	"""
	opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,keranl)
	closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,keranl)

	cv2.imshow("original",frame)
	# cv2.imshow("erosion",erosion)
	# cv2.imshow("dilation",dilation)

	cv2.imshow("opening",opening)
	cv2.imshow("closing",closing)



	k= cv2.waitKey(5) & 0xFF
	if k==27:
		break

cv2.destroyAllWindows()
cap.release()
