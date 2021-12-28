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
a,b,c,d= None,None,None,None    # ,  ,  x ,y
line = False
arr_line = False
rec = False
fill_rec =  False
cir = False
fill_cir = False
def func():
    pass
#Creating the TrackBar for the color
img = np.zeros((100,450,3), dtype = "uint8")
cv2.namedWindow("image")
#Creating the trackbar
cv2.createTrackbar('B',"image",0,255,func)    #For Blue color    
cv2.createTrackbar("G","image",0,255,func)    #For Green color
cv2.createTrackbar("R","image",0,255,func)    #For Red Color
 # Tools select block 

page[:,:50] = (211,211,211)
page[0:50,:] = (211,211,211)
page[20:40,20:40] = brus[:,:]    # brush black block
page[20:40,50:70] =eras[:,:]     # eraser black block
page[20:40,90:110] = 255                   #To create white block
cv2.line(page,(93,30),(107,30),color,1)  #To show the line  color = (0,0,0)
page[20:40,120:140] = 255
cv2.arrowedLine(page,(123,30),(137,30),1,tipLength=0.3)  #To show the Arrowed Line
page[20:40,150:170] = 255
cv2.rectangle(page ,(152,25),(167,35),color ,1)
page[20:40,180:200] = 255
cv2.circle(page,(190,30),8,color,1)
page[20:40,210:230] = 255
cv2.rectangle(page ,(212,25),(227,35),color ,-1)
page[20:40,240:260] = 255
cv2.circle(page,(250,30),8,color,-1)
page[180:200,20:40] = plus[0:20,0:20] #plus symbol block 
page[220:240,20:40] = plus[0:20,20:40] # minus symbol block
def click(event,y,x,flags,para):
    global page,brush,eraser,pressed,color,size,arr_line,line,rec,cir,fill_rec,fill_cir,a,b,c,d

    if event == cv2.EVENT_LBUTTONDOWN:   # Brush on or off
        if x in range(20,40) and y in range(20,40):
            brush = np.invert(brush)
            eraser = False
            print("brush=",brush)
            print("eraser=",eraser)  

    if event == cv2.EVENT_LBUTTONDOWN:
        if x in range(20,40) and y in range(50,70):   #eraser on or off
            eraser = np.invert(eraser)
            brush = False
            print("brush=", brush)
            print("eraser=",eraser)
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
 # To Draw a Line 
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if y in range(90,110) and x in range (20,40):
            brush  = False
            eraser = False
            line = True
 #To Draw Arrowed line
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if y in range(120,140) and x in range (20,40):
            brush  = False
            eraser = False
            line = False
            arr_line = True
    #To Draw Rectangle
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if y in range(150,170) and x in range (20,40):
            brush  = False
            eraser = False
            line = False
            arr_line = False
            rec = True
    #To Draw Circle
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if y in range(180,200) and x in range (20,40):
            brush  = False
            eraser = False
            line = False
            arr_line = False
            rec = False
            cir = True
    #To Draw Filled Rectangle
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if y in range(210,230) and x in range (20,40):
            brush  = False
            eraser = False
            line = False
            arr_line = False
            rec = False
            cir = False
            fill_rec = True
     #To Draw FIlled Circle
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if y in range(240,260) and x in range (20,40):
            brush  = False
            eraser = False
            line = False
            arr_line = False
            rec = False
            cir = False
            fill_rec = False
            fill_cir = True
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
        elif eraser == True:                                      #when left click is pressed then start erase when we select eraser

             if event == cv2.EVENT_LBUTTONDOWN :
                page[x:x+size,y:y+size] =(255,255,255)
                pressed = True
             elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
                page[x:x+size,y:y+size] =(255,255,255)

             elif event == cv2.EVENT_LBUTTONUP:
                pressed = False
        elif line == True:
            if event == cv2.EVENT_LBUTTONDOWN:
                pressed = True
                d,c=x,y

            elif event == cv2.EVENT_LBUTTONUP:
                b,a = x,y
                pressed = False
                cv2.line(page , (a,b),(c,d),color ,size)
        elif arr_line == True:
            if event == cv2.EVENT_LBUTTONDOWN:
                pressed = True
                d,c=x,y

            elif event == cv2.EVENT_LBUTTONUP:
                b,a = x,y
                pressed = False
                cv2.arrowedLine(page ,(c,d), (a,b),color ,size,tipLength=0.4)
        elif rec == True:
            if event == cv2.EVENT_LBUTTONDOWN:
                pressed = True
                d,c=x,y

            elif event == cv2.EVENT_LBUTTONUP:
                b,a = x,y
                pressed = False
                cv2.rectangle(page , (a,b),(c,d),color ,size)
        elif cir == True:
            if event == cv2.EVENT_LBUTTONDOWN:
                pressed = True
                d,c=x,y

            elif event == cv2.EVENT_LBUTTONUP:
                b,a = x,y
                pressed = False
                ctr = ((a+c)//2 , (b+d)//2)
                m = abs(b-d)
                n = abs(a-c)
                m = max(m,n)
                cv2.circle(page, ctr ,m//2,color,size)
        elif fill_rec == True:
            if event == cv2.EVENT_LBUTTONDOWN:
                pressed = True
                d,c=x,y

            elif event == cv2.EVENT_LBUTTONUP:
                b,a = x,y
                pressed = False
                cv2.rectangle(page , (a,b),(c,d),color ,-1)
        elif fill_cir == True:
            if event == cv2.EVENT_LBUTTONDOWN:
                pressed = True
                d,c=x,y

            elif event == cv2.EVENT_LBUTTONUP:
                b,a = x,y
                pressed = False
                ctr = ((a+c)//2 , (b+d)//2)
                m = abs(b-d)
                n = abs(a-c)
                m = max(m,n)
                cv2.circle(page, ctr ,m//2,color,-1)
        
                          
cv2.namedWindow("page")
cv2.setMouseCallback("page",click)

while True:
    page[:35,300:400]=(211,211,211)   
    cv2.putText(page,"Size:"+ str(size), (300,30), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255,255),lineType=cv2.LINE_AA) 

    cv2.imshow("image",img)
    cv2.imshow("page",page)
    #Taking values from trckbar
    b = cv2.getTrackbarPos("B","image")
    g = cv2.getTrackbarPos("G","image")
    r = cv2.getTrackbarPos("R","image")
    img[:] = [b,g,r]
    color = (b,g,r)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break 
   
cv2.destroyAllWindows()
