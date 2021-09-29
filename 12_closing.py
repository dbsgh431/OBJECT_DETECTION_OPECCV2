import cv2

imageName = 'data/images/closing.png'

image = cv2.imread(imageName,0)

cv2.imshow('original',image)


closingSize =3 

element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*closingSize+1,2*closingSize+1))

imageClosing = cv2.morphologyEx(image, cv2.MORPH_CLOSE,element,iterations=3)

cv2.imshow('closing',imageClosing)



cv2.waitKey(0)
cv2.destroyAllWindows()