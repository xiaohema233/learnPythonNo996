import cv2
vc=cv2.VideoCapture("FlatFreehand3D.mp4")
i=0
if vc.isOpened():
	rval,frame=vc.read()
else:
	rval=False
while rval:
	rval,frame=vc.read()
	if  i % 50 == 0:
		cv2.imwrite(str(i)+'.jpg',frame)
	i=i+1
	cv2.waitKey(1)
vc.release()
