import cv2

#grayscale
src = cv2.imread('data/images/threshold.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Original',src)

# 기준 값 thresh 설정
thresh = 100

# 위의 기준 값보다 큰 것을 전부 이 값으로 바꾸기 위해 사용
maxValue =255


# 두번째 리턴 값 dst가 threshold 적용된 이미지(numpy) 이다.
th, dst = cv2.threshold(src,thresh,maxValue,cv2.THRESH_BINARY)

# dst를 화면에 표시

cv2.imshow("Tresholded Image", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()