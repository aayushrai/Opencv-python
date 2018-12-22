
import numpy as np
import cv2 



video = cv2.VideoCapture(0)

while True:
    ret,frame = video.read()
    cv2.imshow("video feed",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
