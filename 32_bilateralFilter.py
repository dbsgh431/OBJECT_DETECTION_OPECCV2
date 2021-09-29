import cv2
import numpy as np

img = cv2.imread("data/images/gaussian-noise.png",1)

#BilateralFilter : 이미지의 경계는 보존, 노이즈는 감소
result = cv2.bilateralFilter(img,15,80,80)

combined = np.hstack([img,result])

cv2.imshow("combined",combined)

cv2.waitKey(0)
cv2.destroyAllWindows()