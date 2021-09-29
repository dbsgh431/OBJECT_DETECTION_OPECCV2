import cv2

import numpy as np

source = cv2.imread('data/images/sample.jpg',cv2.IMREAD_COLOR)

cv2.imshow("original",source)

warpMat = np.array([1.2,0.2,2,-0.3,1.3,1])

print(warpMat.shape)

warpMat = warpMat.reshape(2,3)

result = cv2.warpAffine(source,warpMat,(int(source.shape[1]*1.5) ,int(source.shape[0]*1.5)))

cv2.imshow("result",result) 

warpMat2 = np.array([1.2,0.3,2,0.2,1.3,1])
warpMat2 = warpMat2.reshape(2,3)
result2 = cv2.warpAffine(source,warpMat2,(int(source.shape[1]*1.5) ,int(source.shape[0]*1.5)))


cv2.imshow("result2",result) 

cv2.waitKey(0)
cv2.destroyAllWindows()