import cv2

imageName ='data/images/sample.jpg'

image = cv2.imread(imageName, cv2.IMREAD_COLOR)

if image is None:
    print("잘못된 이미지")

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

#이미지를 표시하는 창에 이름과 성질을 설정

cv2.namedWindow("gray image", cv2.WINDOW_AUTOSIZE)

# 위에서 설정한 내용을 반영하기 위해서는 cv2.imshow()를 사용해야 한다

cv2.imshow("gray image",grayImage)


#작업한 넘파이 이미지를 파일로 저장하는 코드

cv2.imwrite('data/images/gray_img.jpg', grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()