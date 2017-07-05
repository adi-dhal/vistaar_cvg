import cv2
import numpy as np
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if x < 225 and y < 120:
            cv2.circle(img,(x,y),10,(255,0,0),-1)
        if x > 255 and y < 120:
            cv2.circle(img,(x,y),10,(0,255,0),-1)
        if x < 255 and y > 120:
            cv2.circle(img,(x,y),10,(0,0,255),-1)
        if x > 255 and y > 120:
            cv2.circle(img,(x,y),10,(255,255,255),-1)

img=cv2.imread("messi1.jpg")
cv2.namedWindow("image")
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow("image",img)
    if cv2.waitKey(20) & 0xFF == 27 :
        break
cv2.destroyAllWindows()
