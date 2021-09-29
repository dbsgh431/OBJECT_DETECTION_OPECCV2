# 모션 디텍션 전체 완성 4/7

import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

for _ in range(10):
    _, frame = cap.read()
frame = cv2.resize(frame, (640, 480))
frame = cv2.flip(frame, 1)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (25,25), 0)

background = gray

# cv2.imshow("Background", background)

while True :
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (25, 25), 0)

    
    abs_diff = cv2.absdiff(gray, background)

    _, ad_mask = cv2.threshold(abs_diff, 63, 255, cv2.THRESH_BINARY)

    
    cv2.imshow("Abs diff mask", ad_mask)

    if cv2.waitKey(1) == ord('q'):
        break
