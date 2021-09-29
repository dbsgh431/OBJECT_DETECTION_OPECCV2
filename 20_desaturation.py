import cv2
import numpy as np

img = cv2.imread('data/images/capsicum.jpg',1)

cv2.imshow("original",img)

saturationScale = 0.01 # 조절 수치

hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# unit로 되어있는 값을 , float32로 변경(행렬의 연산을 위해)
hsvImage = np.float32(hsvImage)

# 각각의 H, S, V 채널을 분리한다. 즉 3차원의 행렬을 2차원 행렬 3개 로 분리한다.
H, S, V = cv2.split(hsvImage)

# 유용한 함수 : np.clip 함수를 이용
# np.clip()을 통해 0보다 작은 값은 0으로, 255보다 큰값은 255로 스케일한다.

# 채도 조절
S = S * saturationScale

S = np.clip(S, 0 ,255)

# 각각 분리되있는 행렬을 하나로 원상복구하기

hsvImage = cv2.merge([H,S,V])

# 이미지는 정수형이여야 하므로 
hsvImage = np.uint8(hsvImage)

# cv2.imshow()는 컬러스페이스가 BGR로 되어있어야 정확히 표현가능하므로 변경
imgBgr = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)

cv2.imshow("cvt bgr", imgBgr)


cv2.waitKey(0)
cv2.destroyAllWindows()
