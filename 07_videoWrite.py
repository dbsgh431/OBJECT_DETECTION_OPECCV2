import cv2
import numpy as np

# 캠으로부터 데이터 가져오기 
# 첫번째(0) 카메라로 부터
cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("unabel to read camera feed")

else:
    #프레임 정보 가져오기
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    out = cv2.VideoWriter('data/videos/output.avi', cv2.VideoWriter_fourcc('M','J','P','G'),(frame_width,frame_height))

    # 캠으로부터 사진을 계속 입력 받는다.

    while True:
        ret ,frame = cap.read()

        if ret == True:
            #동영상으로 저장
            out.write(frame)
            #화면에 표시
            cv2.imshow('frame',frame)

            if cv2.waitKey(25) & 0xFF == 27: # 키보드에서 esc(25)키를 누르면 exit 하여 실행 중간 종료가능
                break
        
        else:
            break    

    cap.release()
    out.release()
    cv2.destroyAllWindows()
