import cv2
import numpy as np

img = cv2.imread("data/images/truth.png",1)

cv2.imshow("original",img)

sobelX = cv2.Sobel(img, cv2.CV_32F, 1,0)

sobelY = cv2.Sobel(img, cv2.CV_32F, 0,1)

cv2.imshow("sobel x",sobelX)
cv2.imshow("sobel y",sobelY)



cv2.waitKey(0)
cv2.destroyAllWindows()