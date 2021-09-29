import cv2
import numpy as np

image = cv2.imread("data/images/mark.jpg")
cv2.imshow('img',image)

# 선 그리기
imageLine = image.copy()

cv2.line(imageLine, (322,179), (400,183), (0,0,255), thickness=2,lineType=cv2.LINE_AA )

cv2.imshow('image line',imageLine)



#원 그리기

imageCircle = image.copy()

cv2.circle(imageCircle, (350,200), radius=150, color=(255,0,0),thickness=3,lineType=cv2.LINE_AA)
cv2.imshow('imagecircle', imageCircle)


#타원 그리기

imageEllipse = image.copy()

cv2.ellipse(imageEllipse, (360,200), (100,170), 451, 0 , 360, (0,255,0),thickness=2)

cv2.imshow('ellipse',imageEllipse)



# 사각형 그리기


imageRectangel = image.copy()

cv2.rectangle(imageRectangel, (208,55) , (450,355),(255,0,0),thickness=3)
cv2.imshow('rectangle',imageRectangel)


# 글자 넣기

imageText = image.copy()
cv2.putText(imageText,"Mark",(205,50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), thickness=2)
cv2.imshow('imagetext',imageText)



# 실습 : 얼굴 위에 사각형 그리고 그위에 mark라고 글자를 넣으시오


image_my = image.copy()
cv2.putText(image_my,"Mark",(205,50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), thickness=2)
cv2.rectangle(image_my, (208,55) , (450,355),(255,0,0),thickness=3)
cv2.imshow('image_my',image_my)


cv2.waitKey(0)
cv2.destroyAllWindows()