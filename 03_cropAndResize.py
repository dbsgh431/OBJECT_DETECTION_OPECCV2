import cv2

# 1 은 칼라이미지, 0은 그레이스케일, -1은 알파채널을포함(투명도)한 이미지
source = cv2.imread('data/images/sample.jpg',1)

scaleX = 0.6 # x축은 60%
scaleY = 0.6

scaledDown = cv2.resize(source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Original",source)
cv2.imshow('Scaled Down',scaledDown)


scaleX = 2.1
scaleY = 1.5

scaledUP = cv2.resize(source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)

# cv2.imshow("Scale Up",scaledUP)


# CROP : 원하는 부분만 자르는 것
# numpy를 슬라이싱한 것 과 같다.
crop_img = source[10:200 , 100:400]

cv2.imshow("Crop",crop_img)



cv2.waitKey(0)
cv2.destroyAllWindows()