import cv2
import numpy as np


img = cv2.imread("index.jpeg")

rotate_info = cv2.getRotationMatrix2D((0,0),-30,1)  #(0,0) show rotate from coordinate 0,0 means left cornor of image,second aurgument angle of rotation and third is axis 
rotated = cv2.warpAffine(img,rotate_info,(img.shape[1],img.shape[0])) # this part rotate image and in last aurgument we pass height and width of image
cv2.imshow("rotated",rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()

