import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

color = (0,0,255)   #color of circle in this case red according to (b,g,r) we give maximum value to r
line_width = 3        #thickness of circumfrence of circle
radius = 40         #radius of circle
point =(170,114)  #coordinate of center of circle of window 

def click(event,x,y,flags,param):    #argument given by setMouseCallback funtion
    global point,pressed
    if event == cv2.EVENT_LBUTTONDOWN:     #event which button click on mouse 
        print('pressed',x,y)               #x,y is coordinate where we click on window
        point =(x,y)                           #change the coordinate of circle to mouse click coordinate
cv2.namedWindow('frame')
cv2.setMouseCallback("frame",click)    # this setMouseCallback function return some value event,x and y coordinate,flags,param to click funtion

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    cv2.circle(frame,point,radius,color,line_width)    #create circle
    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break 
    
cap.release()
cv2.destroyAllWindows()
