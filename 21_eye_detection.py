import cv2
import numpy as np

img = cv2.imread("faces1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

path = "haarcascade_eye.xml"   #file which detect eyes in image using machine learning

cascade = cv2.CascadeClassifier(path)    

coordinate_eyes = cascade.detectMultiScale(gray,scaleFactor=1.02,minNeighbors=20,minSize=(10,10))
print(len(coordinate_eyes))

for (x,y,w,h) in coordinate_eyes:     # classifier return coordinate of eyes in x,y,w,h
    cv2.circle(img,(int((x+x+w)/2),int((y+y+h)/2)),15,(0,0,255),1)   #draw circle on eyes

cv2.imshow("eyes",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
