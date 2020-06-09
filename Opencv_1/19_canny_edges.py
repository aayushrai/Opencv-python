import cv2
import numpy as np

img = cv2.imread("tomato.jpg",1)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

edges = cv2.Canny(thresh,100,70)
cv2.imshow("canny",edges)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

