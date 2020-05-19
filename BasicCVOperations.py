import numpy as np
import cv2 as cv

img = cv.imread('messi5.jpg')
img2 = cv.imread('opencv-logo.png')

print(img.shape)#Returns tuple of number of rows, columns, channels
print(img.size)#Returns total number of pixel that is accessed
print(img.dtype)#Returns image datatype that is obtained (useful for debugging)

b,g,r = cv.split(img)#Splits the image into its bgr channels

img = cv.merge((b,g,r))#If you have bgr channels and you want to combine them use merge to combine them

ball = img[280:340, 330:390] #Capture roi(region of interest) for ball on image
img[273:333, 100:160] = ball #Place ball onto different spot on image

#resizes both images to match size
img = cv.resize(img, (512, 512))
img2 = cv.resize(img2, (512, 512))

#dst = cv.add(img, img2) #Merges two complete images together

dst = cv.addWeighted(img, .2, img2, .8, 0) #Makes one image more dominant than another when adding them

cv.imshow('image', dst)
cv.waitKey(0)
cv.destroyAllWindows()