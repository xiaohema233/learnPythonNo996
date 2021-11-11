import cv2
import numpy as np
mask = cv2.imread("9-B.png ")
hsv = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
redLower = np.array([35, 43, 46])
redUpper = np.array([77, 255, 255])
mask = cv2.inRange(hsv, redLower, redUpper)
mask=cv2.erode(mask,None,iterations=5)
mask=cv2.dilate(mask,None,iterations=5)
mask = cv2.resize(mask,None,fx=0.6, fy=0.6, interpolation = cv2.INTER_CUBIC)
img = cv2.imread("9-A.png ")
res = cv2.resize(img,None,fx=0.6, fy=0.6, interpolation = cv2.INTER_CUBIC)
dst = cv2.inpaint(res, mask, 10, cv2.INPAINT_NS)
cv2.imwrite("9-C.png", dst)
