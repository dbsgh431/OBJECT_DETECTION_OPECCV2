import cv2

import numpy as np

# 첫번째 사진의 3점의 좌표
input_triangle = np.float32([50,50,100,100,200,150])


# 삼각형 세점의 좌표로 변환
input_triangle = input_triangle.reshape(3,2)
print(input_triangle)

# 변환된 사진의 세점의 좌표

output_triangle = np.float32([70,76,142,101,272,136])

# 삼각형 세점의 좌표로 변환

output_triangle = output_triangle.reshape(3,2)
print(output_triangle)



warpMat = cv2.getAffineTransform(input_triangle,output_triangle)

print(warpMat)


test = np.array([1,2,3,4,5,6], dtype='float32')
test = test.reshape(3,2)
print(test.dtype)