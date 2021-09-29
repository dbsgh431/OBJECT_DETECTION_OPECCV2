import cv2
import numpy as np

img = cv2.imread('data/images/candle.jpg',1)

ycbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

Y, Cr, Cb = cv2.split(ycbImage)

# cv2.equalizeHist() : 히스토그램 균일화하는 함수\
# 이 함수 자체가 연산 후 결과를 준다. 따라서 함수 내부에서 알아서 float으로 바꾸고
# 알아서 0~255사이의 값으로 세팅해서 uint8로 반환해줌

Y = cv2.equalizeHist(Y)

print(Y)
print(Y.dtype)

ycbImage = cv2.merge( [Y,Cr,Cb])

ycbImage = cv2.cvtColor(ycbImage, cv2.COLOR_YCR_CB2BGR)

combined = np.hstack( [img, ycbImage])

cv2.imshow("combined",combined)

cv2.waitKey(0)
cv2.destroyAllWindows()