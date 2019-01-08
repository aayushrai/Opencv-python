import cv2

img =cv2.imread(input("enter file name"))
img = cv2.resize(img,(int(input("height:")),int(input("width:"))))
cv2.imwrite(input("write image name"),img)
