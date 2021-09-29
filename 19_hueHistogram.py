import cv2
import numpy as np

img = cv2.imread('data/images/sample.jpg',1)

cv2.imshow("color",img)

#gray scale image로 변환


gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray_img)

# HSV image

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",hsv_img)


# 밝기를 -100 한 이미지 표시

hsv_img[2] = hsv_img[2] - 100

# 밝기 조절 후 화면에 표시하기 위해서는 bgr로 다시 변환해야한다.
hsv_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
cv2.imshow("bright-100",hsv_img)



cv2.waitKey(0)
cv2.destroyAllWindows()

