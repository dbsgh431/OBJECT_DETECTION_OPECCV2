import cv2

source = cv2.imread('data/images/book1.jpg',1) #1 -> color

print(source.shape)

cv2.imshow('original',source)

# 회전 중심을 구하기 위해 센터 좌표를 얻기 : 넘파이의 행렬인 행과 열의 정보로부터, 센터좌표를 만들때 주의점:
# 행렬을 좌표화 할때 행-> y좌표, 열-> x좌표가 된다.
centerY = source.shape[0] / 2

cenertX = source.shape[1] / 2

rotationAngle = 180
scaleFactor = 1

# 회전을 시킬 수 있는 행렬을 반환
rotationMatrix = cv2.getRotationMatrix2D(center=(cenertX,centerY), angle=rotationAngle, scale=scaleFactor)


print(rotationMatrix)

result = cv2.warpAffine(source,rotationMatrix,(source.shape[1], source.shape[0]))

cv2.imshow('rotiaon img',result)

cv2.waitKey(0)
cv2.destroyAllWindows()