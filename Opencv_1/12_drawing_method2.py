import numpy as np
import cv2

canvas = np.ones([1000,1000,3],"uint8")

color = (0,0,255)
pressed = False
def click(event,x,y,flags,para):
    global canvas,pressed

    if event == cv2.EVENT_LBUTTONDOWN:
        pressed = True
        canvas[y:y+5,x:x+5] = color    # change pixel color where we click by add 5 we change color of more 5 pixel along with so brush get thick

    elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
         canvas[y:y+5,x:x+5] = color
     
    elif event == cv2.EVENT_LBUTTONUP:
            pressed = False

cv2.namedWindow('canvas')
cv2.setMouseCallback('canvas',click)
while True:

    cv2.imshow("canvas",canvas)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break 
    elif cv2.waitKey(1) & 0xFF == ord("r"):
        color = (0,0,255)

    elif cv2.waitKey(1) & 0xFF == ord("g"):
        color = (0,255,0)


    elif cv2.waitKey(1) & 0xFF == ord("b"):
        color = (255,0,0)

cv2.destroyAllWindows()

