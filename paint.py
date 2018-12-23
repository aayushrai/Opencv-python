import numpy as np
import cv2

page = np.ones([800,1000,3],"uint8")*255
brush = False
eraser = False
pressed = False
color = (0,0,255)
page[20:40,20:40] =(0,0,0)
page[20:40,60:80] =(0,0,0)
def click(event,y,x,flags,para):
    global page,brush,eraser,pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        if x in range(20,40) and y in range(20,40):
            brush = np.invert(brush)
            eraser = False
            print("brush=",brush)
            print("eraser=",eraser)
    if event == cv2.EVENT_LBUTTONDOWN:
        if x in range(20,40) and y in range(60,80):
            eraser = np.invert(eraser)
            Brush = False
            print("eraser=",eraser)
            print("brush=", brush)
    if x in range(50,1000):       
        if brush == True:

             if event == cv2.EVENT_LBUTTONDOWN :
                page[x:x+5,y:y+5] =color
                pressed = True
             elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
                page[x:x+5,y:y+5] =color

             elif event == cv2.EVENT_LBUTTONUP:
                pressed = False
        if eraser == True:

             if event == cv2.EVENT_LBUTTONDOWN :
                page[x:x+20,y:y+20] =(255,255,255)
                pressed = True
             elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
                page[x:x+20,y:y+20] =(255,255,255)

             elif event == cv2.EVENT_LBUTTONUP:
                pressed = False
cv2.namedWindow("page")
cv2.setMouseCallback("page",click)

while True:
    cv2.imshow("page",page)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break 
   
cv2.destroyAllWindows()
