# 모션 디텍션 전체 완성 2/7

import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

for i in range(10):
    ret, frame = cap.read()

frame = cv2.resize(frame, (640,480))
frame = cv2.flip(frame, 1)
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

background = gray

cv2.imshow("background",background)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    frame = cv2.flip(frame,1)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    foreground = gray - background

    # 특정 값 기준으로 구분
    _, mask = cv2.threshold(foreground, 127, 255,cv2.THRESH_BINARY)

    cv2.imshow("Foreground",foreground)
    cv2.imshow("Mask", mask)
    if cv2.waitKey(1) == ord('q'):
        break
