# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:06:35 2020

@author: Administrator
"""

import cv2
import  numpy as np
img=cv2.imread('9-D.png')
(h,w)=img.shape[:2]
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_blue=np.array([90,70,70])
upper_blue=np.array([110,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
erode=cv2.erode(mask,None,iterations=1)
dilate=cv2.dilate(erode,None,iterations=1)
for i in range(h):
	for j in range(w):
		if dilate[i,j]==255:
			img[i,j]=(255,255,255)
cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
