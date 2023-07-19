import cv2
img = cv2.imread('car.jpg', 0)
status = cv2.imwrite('new_car.jpg', img)
print('Saved Status: ', status)
