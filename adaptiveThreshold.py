import cv2
image = cv2.imread('./images/car_wash.png')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#THRESHOLD signature ---> image array, threshold value, max value to be assigned when DN val > threshold (255 - white)
#threshold type
# ret, threshedImage = cv2.threshold(grayImage,230,255,cv2.THRESH_BINARY)

#adaptive thresholding signature
'''
image array
max DN value to be assigned
adaptive method
threshold type
block size ----> weighted average
C ----> constant to be subtracted
'''
threshedImage = cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,5)
cv2.imshow('Thresholded Image',threshedImage)
cv2.waitKey(0)