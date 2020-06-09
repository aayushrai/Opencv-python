import cv2
import numpy as np

img = np.zeros([200,200,1],"uint8") #intilize matrix of 200*200 with zero and channel 1 image
cv2.imshow("image",img)
print(img[0,0,:])

img = np.ones([200,200,3],"uint8")#intilize matrix of 200*200 with zero and channel 1 image
cv2.imshow("white",img)
print(img[0,0])

Max=255*img #uint8 is 8bit show max value of pixel is 2**8 = 256 index start from 0 so we take 255
cv2.imshow("255",Max)
print(Max[0,0,:])

img2 = img.copy()   #creat copy of img martix    
img2 =100*img2[:10,:100,0]  #taking first the row of image matrix and 100 coloumn
cv2.imshow("img2",img2)

color_image = img.copy() 
color_image[:,:]=(255,0,0) #(blue ,red ,green)
cv2.imshow("blue",color_image)
cv2.moveWindow("blue",0,1200)   # set where image display show on desktop screen
cv2.moveWindow("img2",500,500)
cv2.moveWindow("255",0,700)

cv2.waitKey(0)  #use for hang the image until we press any key
cv2.destroyAllWindows()  #after press any key it close all the tab
