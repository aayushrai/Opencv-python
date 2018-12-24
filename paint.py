import numpy as np
import cv2

page = np.ones([800,1000,3],"uint8")*255
brush = False
eraser = False
pressed = False
size = 5
color = (0,0,0)
page[20:40,20:40] =(0,0,0)      # brush black block
page[20:40,60:80] =(0,0,0)     # eraser black block
page[80:100,20:40] =(0,0,255)   # color red block
page[110:130,20:40] =(0,255,0) #color green bolck
page[140:160,20:40] =(255,0,0) #color blue block 
def click(event,y,x,flags,para):
    global page,brush,eraser,pressed,color,size

    if event == cv2.EVENT_LBUTTONDOWN:   # Brush on or off
        if x in range(20,40) and y in range(20,40):
            brush = np.invert(brush)
            eraser = False
            print("brush=",brush)
            print("eraser=",eraser)  

    if event == cv2.EVENT_LBUTTONDOWN:
        if x in range(20,40) and y in range(60,80):   #eraser on or off
            eraser = np.invert(eraser)
            brush = False
            print("brush=", brush)
            print("eraser=",eraser)
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if x in range(80,100) and y in range(20,40):
            color =(0,0,255)
  
    if event == cv2.EVENT_LBUTTONDOWN:
        if x in range(110,130) and y in range(20,40):
            color =(0,255,0)
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if x in range(140,160) and y in range(20,40):
            color =(255,0,0)



    if x in range(50,1000) and y in range(50,1000):         # on x axis and y axis area of color is 50 t0 1000 mean paint only in area 50 to 1000
        
    #    if event == cv2.EVENT_MOUSEMOVE:
     #       cv2.circle(page,(y,x),size,color,-1)

        if brush == True:

             if event == cv2.EVENT_LBUTTONDOWN :            #when left click is pressed then start color when we select brush
                page[x:x+size,y:y+size] =color
                pressed = True
             elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
                page[x:x+size,y:y+size] =color

             elif event == cv2.EVENT_LBUTTONUP:
                pressed = False  
        if eraser == True:                                      #when left click is pressed then start erase when we select eraser

             if event == cv2.EVENT_LBUTTONDOWN :
                page[x:x+size,y:y+size] =(255,255,255)
                pressed = True
             elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
                page[x:x+size,y:y+size] =(255,255,255)

             elif event == cv2.EVENT_LBUTTONUP:
                pressed = False
cv2.namedWindow("page")
cv2.setMouseCallback("page",click)

while True:
    cv2.imshow("page",page)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break 
   
cv2.destroyAllWindows()
