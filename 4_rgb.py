import cv2 
import numpy as np

img = cv2.imread("index.jpeg",1)
cv2.imshow("image",img)
cv2.moveWindow("image",0,0)
print(img.shape)
height,width,channels = img.shape

b,g,r = cv2.split(img)

rgb = np.empty([height,width*3,3],"uint8")
rgb[:,0:width] = cv2.merge([b,b,b])
rgb[:,width:2*width] = cv2.merge([g,g,g])
rgb[:,2*width:3*width] = cv2.merge([r,r,r])

cv2.imshow("channel",rgb)
cv2.moveWindow("channel",0,height)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_merge = np.concatenate((h,s,v),axis=1)

cv2.imshow("hsv",hsv_merge)

cv2.waitKey(0)
cv2.destroyAllWindows()
    

