import cv2

# 이미지 경로 설정
imageName = 'data/images/crayon.jpg'

#opencv로 이미지 열기
image = cv2.imread(imageName, cv2.IMREAD_COLOR)

#이미지가 정상인지 체크
if image is None:
    print("열수 없음")
# 이미지를 BGR에서 GRAY로 변경
grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#원본과 그레이스케일 출력
cv2.imshow("image",image)
cv2.imshow("gray",grayImage)

# 키가 입력되면 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()