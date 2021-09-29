import cv2
import numpy as np

img = cv2.imread("data/images/gaussian-noise.png",1)

cv2.imshow("img",img)


# 컨볼루션연산을 위한 kernel(filter)의 사이즈 설정

kernel_size = 5

kernel = np.ones( (kernel_size, kernel_size)) / kernel_size**2
print(kernel)

#opencv에서 컨볼루션 함수는 cv2.filter2D라는 함수를 이용한다

result = cv2.filter2D(img,-1,kernel)

combined = np.hstack([img,result])
cv2.imshow("combined",combined)

cv2.waitKey(0)
cv2.destroyAllWindows()






cv2.waitKey(0)
cv2.destroyAllWindows()