import cv2
import numpy as np

def mouse_hanlder(event, x, y,flags, data) :
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(data['image'], (x,y), radius=3, color =(0,0,255),thickness=5,lineType=cv2.LINE_AA)

        cv2.imshow("Image", data['image'])


        if len(data['points']) < 4:
            data['points'].append([x,y])

def get_four_points(image):
    data = {}

    data['image'] = image.copy()

    data['points'] = []

    cv2.imshow("Image",image)
    cv2.setMouseCallback("Image",mouse_hanlder,data)

    cv2.waitKey(0)

    # 유저가 마우스로 점을 다 찍고 다른 키를 누르면, 점의 좌표들을 float으로 바꿔줘야한다.
    points = np.array( data['points'], dtype=float)

    return points
