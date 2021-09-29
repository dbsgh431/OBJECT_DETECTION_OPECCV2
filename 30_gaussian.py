import cv2
import numpy as np

img = cv2.imread("data/images/gaussian-noise.png",1)

dst1 = cv2.GaussianBlur(img,(5,5),1)

dst2 = cv2.GaussianBlur(img,(25,25),10)

combined = np.hstack([img,dst1,dst2])

cv2.imshow("combined",combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
