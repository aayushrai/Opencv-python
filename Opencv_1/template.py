import cv2
import numpy as np

template = cv2.imread("ball2.jpeg")
frame = cv2.imread("football.jpg")

cv2.imshow("template",template)
cv2.imshow("frame",frame)


result = cv2.matchTemplate(frame,template,cv2.TM_CCOEFF_NORMED)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
print(max_val,max_loc)
cv2.circle(result,max_loc,50,255,2)

cv2.imshow("matching",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
