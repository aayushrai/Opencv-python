import cv2
import numpy as np

img = cv2.imread("gradient.png",1)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('contouir',thresh)
img2 = img.copy()

objects =np.zeros([img.shape[0],img.shape[1],3],"uint8")

for c in contours:
    cv2.drawContours(objects,[c],-1,(255,0,255),-1)

    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c,True)

    M =cv2.moments(c)
    cx = int(M["m10"]/M["m00"])
    cy = int(M["m01"]/M["m00"])
    cv2.circle(objects,(cx,cy),4,(0,0,255),-1)

    print("area:{},perimemter:{}".format(area,perimeter))

cv2.imshow('contour',objects)

cv2.waitKey(0)
cv2.destroyAllWindows()
