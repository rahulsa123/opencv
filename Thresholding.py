import cv2
img =cv2.imread("book.jpg")

# thresholding means apply color on image while set some minimum or maximum  value of color 
grayScale= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(grayScale, 10, 255, cv2.THRESH_BINARY)
cv2.imshow("book",img)
cv2.imshow("gray",grayScale)
cv2.imshow("book_new",threshold)
cv2.waitKey(0)
cv2.distroyAllWindows()