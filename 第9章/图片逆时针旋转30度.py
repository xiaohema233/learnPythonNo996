import cv2
import numpy as np
img=cv2.imread('wordcloud.png')
(h,w)=img.shape[:2]
(x,y)=(w/2,h/2)
M=cv2.getRotationMatrix2D((x,y),30,1)
cos=np.abs(M[0,0])
sin=np.abs(M[0,1])
nW=int((h*sin)+(w*cos))
nH=int((h*cos)+(w*sin))
M[0,2]+=(nW/2)-x
M[1,2]+=(nH/2)-y
img=cv2.warpAffine(img,M,(nW,nH),borderValue=(255,255,255))
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('wordcloud_2.png',img)
