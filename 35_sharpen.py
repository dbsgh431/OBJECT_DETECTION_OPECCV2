import cv2
import numpy as np

img = cv2.imread("data/images/mountain.jpeg",1)

cv2.imshow("original",img)

# 커널(필터) 정의
sharpen = np.array([0,-1,0,-1,5,-1,0,-1,0],dtype='int')

sharpen = sharpen.reshape(3,3)

print(sharpen)

# 컨볼루션 연산
result = cv2.filter2D(img, -1, sharpen)

cv2.imshow('sharp',result)

cv2.waitKey(0)
cv2.destroyAllWindows()