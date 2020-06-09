import cv2 
import numpy as np


img = cv2.imread("without_blur.jpeg",1)
cv2.imshow("orignal",img)

kernel = np.ones((5,5),"uint8")   #form filter of size 5*5 which iterate in whole image materix and erode or dilate the image matrix

dilate = cv2.dilate(img,kernel,iterations=1)   #https://docs.opencv.org/2.4/doc/tutorials/imgproc/erosion_dilatation/erosion_dilatation.html 
cv2.imshow("dilate",dilate)
cv2.moveWindow("dilate",500,0)

erode = cv2.erode(img,kernel,iterations=1)
cv2.imshow("erode",erode)
cv2.moveWindow("erode",1000,0)

print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
