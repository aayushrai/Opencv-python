import cv2
import numpy as np

img = np.zeros([200,200,1],"uint8")
cv2.imshow("image",img)
print(img[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()
