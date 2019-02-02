import cv2
img = cv2.imread('./Text Detection Train/100.jpg')
copyImg = img.copy()
annotationFile = open('./Text Detection Info/gt_100.txt','r')
annotationFileContent = annotationFile.read()
rows = annotationFileContent.split('\n')
del(rows[-1])
for row in rows:
	coOrdinates = []
	row = row.split(' ')
	for cell in row[:-1]:
		coOrdinates.append(int(cell))
	cv2.rectangle(copyImg, (coOrdinates[0],coOrdinates[1]), (coOrdinates[2],coOrdinates[3]), (0,0,255), 2)
	copyImg = copyImg.copy()
cv2.imshow('Rectangled',copyImg)
cv2.waitKey(0)