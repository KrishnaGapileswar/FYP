import cv2
import numpy as np
image = cv2.imread('../FocusedSceneText/Text Detection Train/100.jpg')
grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(type(grayImage))
print(grayImage)
height, width = grayImage.shape[:2]
print(height)
print(width)
# print(grayImage[0][:2])
#sobel method signature ---> image array, CV_64F ensures same depth as original, x-derivative order, y-derivative order, kernel size
# edgeImage = cv2.Sobel(grayImage,cv2.CV_64F,1,0,ksize=3)

#Canny method signature ---> image array, min pixel val, max pixel value
edgeImage = cv2.Canny(grayImage[128:182,158:412],0,255)
edgeHeight, edgeWidth = edgeImage.shape[:2]
edgeImage.dtype = 'uint8'
for i in range(edgeHeight):
	for j in range(edgeWidth):
		if edgeImage[i,j] == 1:
			edgeImage[i,j] = 255

grayImage[128:182,158:412] = edgeImage

print(type(grayImage))
print(grayImage)
cv2.imshow('Edge Detected',grayImage)
cv2.waitKey(0)