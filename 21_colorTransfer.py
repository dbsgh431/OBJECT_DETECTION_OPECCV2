import cv2
import numpy as np

src = cv2.imread('data/images/image1.jpg',1)
dst = cv2.imread('data/images/image2.jpg',1)

cv2.imshow("originalsrc",src)
cv2.imshow("originaldst",dst)

# 위 두 이미지의 컬러를 조합하여 결과로 만들 이미지 생성

output = dst.copy()

srcLab = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
dstLab = cv2.cvtColor(dst, cv2.COLOR_BGR2LAB)
outputLab = cv2.cvtColor(output, cv2.COLOR_BGR2LAB)

# 연산을 위해서 float32로 변환
srcLab = srcLab.astype('float32') # == np.float32(srcLab)
dstLab = dstLab.astype('float32')
outputLab = outputLab.astype('float32')


print(srcLab)

# 채널 분리!

srcL, srcA, srcB = cv2.split(srcLab)
dstL, dstA, dstB = cv2.split(dstLab)
outL, outA, outB = cv2.split(outputLab)

# dst의 값에서 dst의 평균을 각각에서 빼서 색감을 변화시킨다.

print(type(dstL))

outL = dstL - dstL.mean()
outA = dstA - dstA.mean()
outB = dstB - dstB.mean()

# std() : 표준편차
outL = outL * (srcL.std() / dstL.std())
outA = outA * (srcA.std() / dstA.std())
outB = outB * (srcB.std() / dstB.std())

outL = outL + srcL.mean()
outA = outA + srcA.mean()
outB = outB + srcB.mean()


# float32로 작업되는데, 이때 음수가 되거나 255보다 큰 값이 나올 수가 있는데, 이를 0~255까지로 만들기 위해 clip()을 사용하여 음수는 0, 최댓값은 255로 만들어줌
outL = np.clip(outL, 0, 255 )
outA = np.clip(outA, 0, 255 )
outB = np.clip(outB, 0, 255 )


# 분리된 채널을 다시 하나로 만든다.
# 합치는 파라미터 순서 -> L, A, B(LAB 컬러스페이스)

outputLab = cv2.merge( [outL, outA, outB])

# float32로 되있는데, 이미지는 uint8이므로 변경
outputLab = np.uint8(outputLab)

print(outputLab.dtype)


# 화면에 표시하는 cv2.imshow()는 BGR의 컬러스페이스를 화면에 표시하는 함수이므로
# 따라서 LAB로 되어있는 컬러스페이스를 BGR로 먼저 바꿔주어야 한다.


outputLab = cv2.cvtColor(outputLab, cv2.COLOR_LAB2BGR)

cv2.imshow("outputLab",outputLab)




cv2.waitKey(0)
cv2.destroyAllWindows()
