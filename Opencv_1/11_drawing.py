import numpy as np
import cv2


canvas = np.ones([500,500,3],"uint8")*255
pressed = False
color =(0,255,0)
radius = 3
def brush(event,x,y,flags,pram):
    global canvas,pressed
    if event == cv2.EVENT_LBUTTONDOWN:
            pressed = True
            cv2.circle(canvas,(x,y),radius,color,-1)
    
    elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
            cv2.circle(canvas,(x,y),radius,color,-1)
  
    elif event == cv2.EVENT_LBUTTONUP:
            pressed = False



cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas",brush)



while True:
     
    cv2.imshow("canvas",canvas)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break 
cv2.destroyAllWindows()


