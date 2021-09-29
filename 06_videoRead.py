import cv2
import numpy as np

cap = cv2.VideoCapture('data/videos/chaplin.mp4')


if cap.isOpened() == False :
    print("error opening video stream of file")

else :
    # 비디오는 여러장의 사진으로 구성되있기에 반복문으로 한장 씩 처리
    while cap.isOpened() :
        
        ret, frame = cap.read()
        
        if ret == True : # ret에는 제대로 사진을 가져왔는지 정보가 true,false로 들어있다.
                         # 따라서 ret가 true이면 화면에 사진(frame)을 표시하면 된다.
            cv2.imshow('frame',frame)
            if cv2.waitKey(25) & 0xFF == 27: # 키보드에서 esc(25)키를 누르면 exit 하여 실행 중간 종료가능
                break

        else:
            #동영상 재생이 끝난 경우, 혹은 사진에 이상이 있는 경우   
            break
    cap.release()  # 자원을 반환

    cv2.destroyAllWindows()     