import cv2
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

image_color = cv2.imread('data2/image.jpg')

cv2.imshow("ori",image_color)

# 그레이 스케일

image_gray = cv2.cvtColor(image_color,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', image_gray)

image_copy = image_gray.copy()

print(image_copy.shape)

# 값이 195미만인 것들은 전부 0으로 세팅(흰색찾기)

print( image_copy[ : , : ] < 195)

image_copy[image_copy[ : , :] < 195] = 0

image = cv2.imread("data2/test_image.jpg")

cv2.imshow("img2",image)

print("height = ", image.shape[0],'pixels')
print("width = ", image.shape[1],'pixels')

gray_img= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray',gray_img)

hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('gray',hsv_img)

# Hue채널만 가져와서 출력
H, S, V = cv2.split(hsv_img)

H = hsv_img[ : , :, 0]
cv2.imshow("hue",H)

image = cv2.imread('data2/test_image2.jpg')
cv2.imshow("image",image)

M_rotation = cv2.getRotationMatrix2D( (image.shape[1]/2, image.shape[0]/2), 90, 0.5) # 90 도 회전 하고,0.5사이즈로세팅

rotated_img = cv2.warpAffine(image, M_rotation, (image.shape[1],image.shape[0]))

cv2.imshow("rotated",rotated_img)

image = cv2.imread("data2/test_image3.jpg")
cv2.imshow('image',image)

T_matrix = np.array([1, 0, 120,0, 1, -150],dtype='float32') #회전하지 말고 x축 y축으로 이동만
T_matrix = T_matrix.reshape(2,3) # warpaffine 하기위해 2행 3열로 변경
print(T_matrix)

translaion_img = cv2.warpAffine(image, T_matrix, (image.shape[1],image.shape[0]))
cv2.imshow("trans",translaion_img)


resized_image = cv2.resize(image,None,fx=0.5,fy=1.2,interpolation=cv2.INTER_LINEAR)
cv2.imshow('resize',resized_image)




cv2.waitKey(0)
cv2.destroyAllWindows()