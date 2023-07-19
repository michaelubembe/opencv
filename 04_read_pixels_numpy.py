import numpy as np
import cv2 as cv
img = cv.imread('car.jpg', 1)
px = img.item(500,400,0)
print(px)
#use itemset to modify the value at that location
