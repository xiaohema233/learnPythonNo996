import cv2
img = cv2.imread('wordcloud.png',cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('wordcloud_1.png',img)
