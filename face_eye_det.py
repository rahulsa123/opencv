import numpy as np 
import cv2

face= cv2.CascadeClassifier("face.xml")
eye= cv2.CascadeClassifier("eye.xml")
nose = cv2.CascadeClassifier("nose.xml")
cam= cv2.VideoCapture(0)

while True:
	ret ,img =cam.read()
	gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#finding face on picture
	faces = face.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		#finding eye inside picture, area diagonal mostly in y,x formate
		roi_gray=gray[y:y+h,x:x+w]
		roi_color=img[y:y+h,x:x+w]
		eyes=eye.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
		Nose = nose.detectMultiScale(roi_gray)
		for (x,y,w,h) in Nose:
				center = (x + w//2, y + h//2)
				cv2.ellipse(roi_color, center, (w//2, h//2), 0, 0, 360, (255, 0, 255),2)

	cv2.imshow("face_eye",img)
	k = cv2.waitKey(30) & 0xff
	if(k==27):
		break
cv2.destroyAllWindows()
cam.release()





