import numpy as np
import cv2 as cv

img1 = np.zeros((250,500,3), np.uint8)
img1 = cv.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
img2 = cv.imread('image_1.png')

#bitAnd = cv.bitwise_and(img2, img1) #Uses truth table for logical and to show outputs of one in white
#bitOr = cv.bitwise_or(img2, img1) #Uses truth table for logical or to show outputs of one in white
#bitXor = cv.bitwise_xor(img2, img1) #Uses truth table for logical Xor to show outputs of one in white
bitNot = cv.bitwise_not(img1) #Uses truth table for logical not to show opposite of source

cv.imshow('img1', img1)
cv.imshow('img2', img2)
#cv.imshow('bitAnd', bitAnd)
#cv.imshow('bitOr', bitOr)
#cv.imshow('bitXor', bitXor)
cv.imshow('bitNot', bitNot)


cv.waitKey(0)
cv.destroyAllWindows()