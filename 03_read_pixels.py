import cv2 as cv
img = cv.imread('car.jpg', 1)
px = img[100,100]
px_blue = img[100,100,0]
px_green = img[100,100,1]
px_red = img[100,100,2]
print(px)
print('-Blue: ', px_blue)
print('-Green: ', px_green)
print('-Red: ', px_red)

