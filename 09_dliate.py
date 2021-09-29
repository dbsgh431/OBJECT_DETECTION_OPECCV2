import cv2

imageName = 'data/images/truth.png'

image = cv2.imread(imageName, cv2.IMREAD_COLOR)

cv2.imshow("original",image)


# 이미지 확장 - dilation

dilatoinSize = 6

element = cv2.getStructuringElement(cv2.MORPH_RECT,(2*dilatoinSize + 1 ,2*dilatoinSize + 1  ))

imageDilate = cv2.dilate(image, element)

cv2.imshow("Dilation",imageDilate)






cv2.waitKey(0)
cv2.destroyAllWindows()