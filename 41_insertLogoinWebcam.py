# 실습 : 웹캠에 로고 넣기 실습
import cv2
import numpy as np



# 1. logo.png 파일을 읽어오기
logo = cv2.imread("data3/logo.png",1)
# cv2.imshow("org",image)
# 2. 위 파일을 (100,100)으로 리사이징
print(logo.shape)

logo = cv2.resize(logo, (100,100))

# 3. 그레이스케일로 바꾸기
gray_img = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_img",gray_img)
# 4. threshold를 이용해서, 로고를 마스킹 하기


_,mask = cv2.threshold(gray_img, 1, 255 ,cv2.THRESH_BINARY)

cv2.imshow("result",mask)
# 5. 웹캠을 640, 480 사이즈로 설정해서 키고
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (640,480))
    frame = cv2.flip(frame,1)


    roi = frame[370:470, 530:630]
    roi[np.where(mask)] = 0

    roi = roi + logo

    cv2.imshow("Webcam",frame)

    if cv2.waitKey(1) == ord('q'):
        break
# 6. 웹캠 이미지에서 오른쪽 아래에 로고를 표시할 region of interest 세팅

# 7. 로고와 웹캠 이미지 합침







# cv2.waitKey(0)
# cv2.destroyAllWindows()