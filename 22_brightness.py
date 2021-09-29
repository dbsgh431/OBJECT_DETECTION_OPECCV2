import cv2
import numpy as np

img = cv2.imread('data/images/candle.jpg',1)

cv2.imshow("original", img)

beta = 100

# 1. 컬러 스페이스 변경 -> YCrCb

ycbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# 2. 데이터 가공을 위해, uint8을 -> float32로 변경
ycbImage = ycbImage.astype('float32')

print(ycbImage.dtype)

# 3. 채널 분리
Y, Cr, Cb = cv2.split(ycbImage)

# 4. 밝기 조절 (밝기는 y값)

Y = Y + beta

# 5. 연산 후 np.clip으로 범위 조정

Y = np.clip(Y, 0, 255)

# 6. 채널을 하나로 합친다.
ycbImage = cv2.merge([Y,Cr,Cb])

# 7. uint8로 변경
ycbImage = np.uint8(ycbImage)

# 8. 화면 표시를 위해 컬러스페이스를 bgr로 변경

ycbImage = cv2.cvtColor(ycbImage, cv2.COLOR_YCrCb2BGR)

# 9. 출력
cv2.imshow("dst",ycbImage)

cv2.waitKey(0)
cv2.destroyAllWindows()