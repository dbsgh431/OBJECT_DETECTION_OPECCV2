import cv2
import numpy as np

img = cv2.imread("data/images/sample.jpg",0)


cv2.imshow("gray",img)

threshold_max = 150

threshold_min = 50

result = cv2.Canny(img, threshold_max, threshold_min)

cv2.imshow("Canny",result)

cv2.waitKey(0)
cv2.destroyAllWindows()