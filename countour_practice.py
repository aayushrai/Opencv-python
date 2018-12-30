import cv2
import numpy as np


img = cv2.imread("index.jpeg")
HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

H = HSV[:,:,0]
S = HSV[:,:,1]
V = HSV[:,:,2]

ret,sat = cv2.threshold(S,20,255,cv2.THRESH_BINARY)
ret,hue = cv2.threshold(H,25,255,cv2.THRESH_BINARY_INV)
ret,v = cv2.threshold(V,15,255,cv2.THRESH_BINARY_INV)

final = cv2.bitwise_and(sat,hue)
cv2.imshow("result",final)
cv2.imshow("v",v)
_,contour, herirechy = cv2.findContours(sat,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
cv2.drawContours(img2,contour,-1,(0,0,255),10)
cv2.imshow("hue",hue)

cv2.imshow("hue",hue)
cv2.imshow("countour",img2)
cv2.imshow("sar",sat)
cv2.waitKey(0)
cv2.destroyAllWindows()
