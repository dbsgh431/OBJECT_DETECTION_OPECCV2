import numpy as np
import argparse
import time
import cv2
import os
import matplotlib.pyplot as plt
import imutils


SET_WIDTH = int(600)

normalize_image = 1 / 255.0
resize_image_shape = (1024,512)

sample_img = cv2.imread('data4/images/example_04.png')


sample_img = imutils.resize(sample_img,width=SET_WIDTH)
# cv2.imshow("ori",sample_img)

# opencv의 pre-trained model을 통해 예측하기 위해서는 
# 입력 이미지를 blob으로 바꾸어주어야 한다.

blob_img = cv2.dnn.blobFromImage(sample_img,normalize_image,resize_image_shape,0,swapRB = False,crop = False)

# 시맨틱 세그먼테이션에 사용할 Enet 모델을 가져온다

cv_enet_model = cv2.dnn.readNet('data4/enet-cityscapes/enet-model.net')
print(cv_enet_model)

# 이미지 넣기
cv_enet_model.setInput(blob_img)

# 중요!1 포워드 함수를 실행해서, 예측해 줍니다.
cv_enet_model_output = cv_enet_model.forward()

print(cv_enet_model_output.shape)
# (1,20,512,1024) -> 1: 1개의 이미지를 넣었다. 20: 분류하는 클래스의 개수 512 : 행렬의 행 갯수 1024 : 행렬의 열 개수

# 분류하는 20개의 클래스 확인
label_values = open('data4/enet-cityscapes/enet-classes.txt').read().split('\n')
print(label_values)

#맨 마지막 원소가 공백이므로 제거
label_values = label_values[0:-2+1]


IMG_OUTPUT_SHAPE_START = 1
IMG_OUTPUT_SHAPE_END = 4
classes_num, h, w = cv_enet_model_output.shape[IMG_OUTPUT_SHAPE_START :IMG_OUTPUT_SHAPE_END ]

# 중요2! 모델의 아웃풀 20개 행렬을, 하나의 행렬로 만든다
class_map = np.argmax(cv_enet_model_output[0], axis=0)
print(class_map)

# 시맨틱 세그먼테이션에 사용될 색 정보도 가져온다
CV_ENET_SHAPE_IMG_COLORS = open('data4/enet-cityscapes/enet-colors.txt').read().split('\n')

# 문자로 된 색정보를 numpy로 사용하기 위해 숫자로 변환
color_list = []
for color in CV_ENET_SHAPE_IMG_COLORS[0 : -2+1]:
    array = np.array(color.split(',')).astype('int')
    color_list.append(array)

color_list = np.array(color_list)
print(color_list)


# 중요3! 하나의 행렬을 이미지로 만든다
# 각 픽셀별로 클래스에 해당하는 숫자가 적힌 class_map을
# 각 숫자에 매칭되는 색으로 세팅해준것이다
# 따라서 각 픽셀별 색 정보가 들어간다
# 2차원 행렬을, 3차원 채널이 있는 BGR행렬로 만든다.

mask_class_map = color_list[class_map]

# resize

mask_class_map = cv2.resize(mask_class_map,(sample_img.shape[1], sample_img.shape[0]),interpolation=cv2.INTER_NEAREST)

class_map = cv2.resize(class_map, (sample_img.shape[1],sample_img.shape[0]),interpolation=cv2.INTER_NEAREST)

# 이미지 합성
cv_enet_model_output = ((0.4*sample_img)+(0.6*mask_class_map)).astype('uint8')



# 화면에 색 정보를 표시하기 위한 레전드 생성
my_legend = np.zeros( ( len(label_values) * 25 ,  300 , 3  )   , dtype='uint8' )
for ( i, (class_name, img_color)) in enumerate( zip(label_values , color_list)) :
  color_info = [  int(color) for color in img_color  ] 
  cv2.putText(my_legend, class_name, (5, (i*25) + 17) , 
              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0) , 2 )
  cv2.rectangle(my_legend, (100, (i*25)), (300, (i*25) + 25) , tuple(color_info), -1)

cv2.imshow("legend",my_legend)

cv2.imshow("ori",sample_img)
cv2.imshow('output',cv_enet_model_output)

cv2.waitKey(0)
cv2.destroyAllWindows()