import cv2
import numpy as np

img=cv2.imread("messi1.jpg")
y,x,_=img.shape
##img1=cv2.resize(img,(100,100),interpolation=cv2.INTER_LINEAR)
##img2=cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)

##M=np.float32(([1,0,50],[0,1,100]))
##img1=cv2.warpAffine(img,M,(200,200))

M=cv2.getRotationMatrix2D((x/2,y/2),45,1)
img1=cv2.warpAffine(img,M,(x,y))



cv2.imshow("res1",img1)
#cv2.imshow("res2",img2)
cv2.waitKey(0)
