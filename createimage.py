import cv2
import numpy as np

img = np.zeros([200,200,1],"uint8") #intilize matrix of 200*200 with zero and channel 1 image
cv2.imshow("image",img)
print(img[0,0,:])

img = np.ones([200,200,1],"uint8")#intilize matrix of 200*200 with zero and channel 1 image
cv2.imshow("white",img)
print(img[0,0])

Max=255*img #uint8 is 8bit show max value of pixel is 2**8 = 256 index start from 0 so we take 255
cv2.imshow("255",Max)
print(Max[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()
