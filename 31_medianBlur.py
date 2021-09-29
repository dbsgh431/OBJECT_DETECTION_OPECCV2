import cv2
import numpy as np

img = cv2.imread("data/images/gaussian-noise.png",1)

dst1 = cv2.medianBlur(img, 5)

dst2 = cv2.medianBlur(img, 7)

combined = np.hstack([img,dst1,dst2])

cv2.imshow("combined",combined)

cv2.waitKey(0)
cv2.destroyAllWindows()