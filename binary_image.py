import numpy as np
import cv2

bw = cv2.imread("gradient.png",0)
height,width = bw.shape[0:2]
cv2.imshow("orignal",bw)

binary = np.zeros([height,width,1],"uint8")
#slow threshold

threshold =85


for row in range(height):
    for col in range(width):
        if bw[row][col] > threshold:
            binary[row][col] = 255
cv2.imshow("slow_binary",binary)

#cv2 threshold  more faster way

ret,thre = cv2.threshold(bw,threshold,255,cv2.THRESH_BINARY)
cv2.imshow("cv threshold",thre)

cv2.waitKey(0)
cv2.destroyAllWindows()
