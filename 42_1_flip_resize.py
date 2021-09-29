# 모션 디텍션 전체 완성 1/7

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

    cv2.imshow("Foreground",foreground)

    if cv2.waitKey(1) == ord('q'):
        break
