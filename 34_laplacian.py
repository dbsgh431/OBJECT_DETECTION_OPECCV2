import cv2
import numpy as np

img = cv2.imread("data/images/truth.png",1)

laplacian = cv2.Laplacian(img,cv2.CV_32F, ksize=3, scale=1)

cv2.imshow("original",img)
cv2.imshow("lapl",laplacian)










cv2.waitKey(0)
cv2.destroyAllWindows()