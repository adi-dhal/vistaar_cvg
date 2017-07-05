import cv2
import numpy as np
img=cv2.imread("messi1.jpg")
y,x,_=img.shape
img1=img[0:y/2,0:x/2]
img2=img[0:y/2,x/2:x]
img3=img[y/2:y,0:x/2]
img4=img[y/2:y,x/2:x]
channels_1=cv2.split(img1)
channels_2=cv2.split(img2)
channels_3=cv2.split(img3)
channels_4=np.dot(img4,[0.299,0.587,0.114])
img1=cv2.merge((channels_1[0],np.zeros_like(channels_1[0]),np.zeros_like(channels_1[0])))
img2=cv2.merge((np.zeros_like(channels_2[1]),channels_2[1],np.zeros_like(channels_2[1])))
img3=cv2.merge((np.zeros_like(channels_3[2]),np.zeros_like(channels_3[2]),channels_3[2]))
img4=cv2.merge((channels_4,channels_4,channels_4))
cv2.waitKey(0)
res=np.zeros_like(img)
res[0:y/2,0:x/2]=img1
res[0:y/2,x/2:x]=img2
res[y/2:y,0:x/2]=img3
res[y/2:y,x/2:x]=img4
cv2.imshow("res",res)
cv2.waitKey(0)
