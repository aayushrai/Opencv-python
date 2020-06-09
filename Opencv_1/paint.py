import numpy as np
import cv2

page = np.ones([800,1000,3],"uint8")*255
plus = cv2.imread("plusminus20.jpg")
brus = cv2.imread("brush_r1.png")
eras = cv2.imread("eraser1.png")
brush = False
eraser = False
pressed = False
size = 5
color = (0,0,0) 
 # Tools select block 

page[:,:50] = (211,211,211)
page[0:50,:] = (211,211,211)
page[20:40,20:40] = brus[:,:]    # brush black block
page[20:40,60:80] =eras[:,:]     # eraser black block
page[80:100,20:40] =(0,0,255)   # color red block
page[110:130,20:40] =(0,255,0) #color green bolck
page[140:160,20:40] =(255,0,0) #color blue block 
page[180:200,20:40] = plus[0:20,0:20] #plus symbol block 
page[220:240,20:40] = plus[0:20,20:40] # minus symbol block
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
 # Red color brush
    if event == cv2.EVENT_LBUTTONDOWN:      
        if x in range(80,100) and y in range(20,40):
            color =(0,0,255)
 # Green color brush 
    if event == cv2.EVENT_LBUTTONDOWN:                   
        if x in range(110,130) and y in range(20,40):
            color =(0,255,0)
 # blue color brush   
    if event == cv2.EVENT_LBUTTONDOWN:
        if x in range(140,160) and y in range(20,40):
            color =(255,0,0)
 # Increase brush and eraser size           
    if event == cv2.EVENT_LBUTTONDOWN:
        if x in range(180,200) and y in range(20,40):
            size = size + 1
            print("size:",size)
 # Decrease brush and eraser size           
    if event == cv2.EVENT_LBUTTONDOWN:
        if x in range(220,240) and y in range(20,40):
            size = size - 1
            print("size:",size)
 # Drawing sheet
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
    page[:35,300:400]=(211,211,211)   
    cv2.putText(page,"Size:"+ str(size), (300,30), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255,255),lineType=cv2.LINE_AA) 


    cv2.imshow("page",page)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break 
   
cv2.destroyAllWindows()
