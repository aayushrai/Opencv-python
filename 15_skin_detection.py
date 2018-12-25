import numpy as np
import cv2


img = cv2.imread("faces1.jpg",1)
cv2.imshow("faces_orignal",img)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("faces_hsv",hsv)

h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

hsv_split = np.concatenate((h,s,v),axis=1)
cv2.imshow("hsv_split",hsv_split)

ret,sat_filter = cv2.threshold(s,40,255,cv2.THRESH_BINARY)
cv2.imshow("saturation_filter",sat_filter)

ret,hue_filter = cv2.threshold(h,15,255,cv2.THRESH_BINARY_INV)
cv2.imshow("hue_filter",hue_filter)

final = cv2.bitwise_and(sat_filter,hue_filter)
cv2.imshow("final",final)

cv2.waitKey(0)
cv2.destroyAllWindows()

