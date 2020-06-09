import cv2

img =cv2.imread("1")
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("display",img)

cv2.waitKey(0)
cv2.imwrite("write.jpg ",img)

