import cv2
import numpy as np 
main_img_rgb=cv2.imread("main.jpg")
 #objext in template which we want to find
template=cv2.imread("template.jpg",0)
# height and width return by shape
w,h =template.shape[::-1]
main_img_gray=cv2.cvtColor(main_img_rgb,cv2.COLOR_BGR2GRAY)
res = cv2.matchTemplate(main_img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold =0.9
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
	cv2.rectangle(main_img_rgb,pt,(pt[0]+w,pt[1]+h),(255,0,0),2)
	# print(pt)
cv2.imshow("Detected",main_img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()