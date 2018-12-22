
import numpy as np
import cv2


image = cv2.imread("without_blur.jpeg",1)
cv2.imshow("orignal",image)

blur = cv2.GaussianBlur(image,(5,55),0)   #blur (x axis blur,y axis blur) && x and y has odd value
cv2.imshow("blur",blur)

cv2.moveWindow("blur",0,400)

cv2.waitKey(0)
cv2.destroyAllWindows()


