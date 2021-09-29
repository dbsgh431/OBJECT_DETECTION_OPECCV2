import cv2
import numpy as np

original = cv2.imread('data/images/girl.jpg',1)
cv2.imshow("original", original)

img = original.copy()

originalValue = np.array([0, 50, 100, 150 ,200,255])

rCurve = np.array([0, 40, 80, 120 ,180 ,255])

bCurve = np.array([0,80,120,160,230,255])

fullrange = np.arange(0, 255+1)

rLUT =  np.interp(fullrange, originalValue,rCurve)
bLUT =  np.interp(fullrange, originalValue,bCurve)

R = img[ : , : , 2 ]
R = cv2.LUT(R,rLUT)

B = img[ : , : , 0 ]
B = cv2.LUT(B,bLUT)

img[ : , :, 2] = R 
img[ : , :, 0] = B

combined = np.hstack( [original,img])
cv2.imshow("combined",combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
