import cv2
import numpy as np

img = cv2.imread("faces1.jpg",1)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
path = "frontalFace10/haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(path)

faces = face_cascade.detectMultiScale(gray,scaleFactor=1.10,minNeighbors=5,minSize=(40,40))
print(len(faces))

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
