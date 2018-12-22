import cv2 
import numpy as np

img = cv2.imread("image_cv.png")


#scale 
img_half = cv2.resize(img,(0,0),fx=0.5,fy=0.5) # fx=.5 and fy=.5 means image resize to .5 of full image./fx=fy=.5 means half of full image
img_stretch =cv2.resize(img,(600,600))

cv2.imshow("Half",img_half)
cv2.imshow("strach",img_stretch)

cv2.waitKey(0)
cv2.destroyAllWindows()
