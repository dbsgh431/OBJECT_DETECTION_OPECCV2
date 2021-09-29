import cv2
import numpy as np

from utils import get_four_points

# 똑바른 이미지를, 찌그려 뜨린 이미지로 변환하고자 한다.
img_dst = cv2.imread('data/images/times-square.jpg',1)
img_src = cv2.imread('data/images/first-image.jpg',1)


cv2.imshow("img src", img_src)


print(img_src.shape)

# 똑바른 이미지의 4개의 점 좌표를 가져옴
points_src = np.array([0,0, img_src.shape[1],0, img_src.shape[1],img_src.shape[0], 0,img_src.shape[0]])
points_src = points_src.reshape(4,2)

print(points_src)


# 찌그러진 이미지의 4개의 점은, 바로 가져오지못하므로 마우스로 점의 좌표를 가져온다.
points_dst = get_four_points(img_dst)

print(points_dst)


H, status =cv2.findHomography(points_src, points_dst)

print(H)

img_tmp = cv2.warpPerspective(img_src,H,(img_dst.shape[1],img_dst.shape[0]))

cv2.imshow("Img tmp",img_tmp)

# 타임스 스퀘어(기존이미지)의 전광판 안쪽영역을 0으로 만들고, 두번째 이미지의 행렬과 더하게되면 하나의 이미지로 완성된다.

cv2.fillConvexPoly(img_dst,points_dst.astype(int),0)

cv2.imshow("img_dst",img_dst)

# 두이미지를 합

img_result = img_dst + img_tmp

cv2.imshow("result",img_result)


cv2.waitKey(0)
cv2.destroyAllWindows()