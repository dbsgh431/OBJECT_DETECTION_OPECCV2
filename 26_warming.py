import cv2
import numpy as np

original = cv2.imread('data/images/girl.jpg',1)
cv2.imshow("original", original)


img = original.copy()

# 행렬에 들어있는  원래의 기준값 6개 세팅
originalValue = np.array([0, 50, 100, 150 ,200,255])

# 위의 기준값에 매칭되는, 6개의 값 세팅
# 이 값은, 기준 값보다 높은 값들이다.
# 즉 기준값이 있으면, 그 값을 각각아래의 매칭된 값으로 적용
rCurve = np.array([0, 80, 150, 190 ,220 ,255])

# 위 기준값과 매칭되어 각각 아래의 매칭된 값으로 적용
bCurve = np.array([0,20,40,75,150,255])

# Lookup table 만들기 ->
# 현재, 6개의 기준점만 가지고 있다
# 그렇지만 256개의 모든 점으로 만들어 주어야한다
# 그래야, 0~255까지의 값들을 해당 룩업테이블에 매칭시켜 줄수 있기때문에, 6개의 기준점을 가지고
# 256개의 매칭점을 도출해내야 된다.

fullrange = np.arange(0, 255+1)

# 특정 개수의 점들로, 점들을 늘려 세팅
rLUT =  np.interp(fullrange, originalValue,rCurve)
print(fullrange)
print(rLUT)

bLUT =  np.interp(fullrange, originalValue,bCurve)

#원래의 원본 이미지에서, R채널만 가져와서, rLUT를 적용하면 따뜻한 느낌

# B,G,R = cv2.split(img)
R = img[ : , : , 2 ]
R = cv2.LUT(R,rLUT)

B = img[ : , : , 0 ]
B = cv2.LUT(B,bLUT)
# merge
img[ : , :, 2] = R 
img[ : , :, 0] = B

combined = np.hstack( [original,img])
cv2.imshow("combined",combined)

#원래의 원본 이미지에서, B채널만 가져와서, bLUT를 적용하면 차가운 느낌


cv2.waitKey(0)
cv2.destroyAllWindows()
