import cv2
import numpy as np

img = cv2.imread('data/images/candle.jpg',1)

cv2.imshow("original",img)

gamma  = 1.5

# 이미지는 0부터 255까지 이므로, 이 이미지 범위에 해당하는 모든 숫자를 가져온다.
fullRange = np.arange(0, 255+1)

print(fullRange)

# 감마 보정을 통해, 원래의 0~255까지의 숫자를 보정한 숫자로 변경한다.
lookupTable = 255 * np.power((fullRange / 255.0) , gamma)

# 감마 보정하면 float이므로 uint8로 변경

lookupTable = np.uint8(lookupTable)

print(lookupTable)

output = cv2.LUT(img, lookupTable)

combined = np.hstack( [img,output] )

cv2.imshow("combined", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
