import cv2
import numpy as np

img = cv2.imread("index.jpeg")

gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.jpg",gray)

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

rgba = cv2.merge([b,g,r,r])
cv2.imwrite("rgba.png",rgba)


