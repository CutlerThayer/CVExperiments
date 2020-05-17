import numpy as np
import cv2 as cv

#img = cv.imread('lena.jpg',1)
img = np.zeros([512,512,3], np.uint8)

#Draw a dark green line from top right to center
img = cv.line(img, (0,0), (255,255), (49, 105, 28), 10)
#Draw blue line from left to center
img = cv.arrowedLine(img, (0,255), (255,255), (255, 0, 0), 10)

#Draw rectangle
img = cv.rectangle(img, (384,0), (510,128), (0,0,255), 10)
#Draw circle
img = cv.circle(img, (447,63), 63, (0, 255, 0), -1)
#Add text
font = cv.FONT_HERSHEY_SIMPLEX
img = cv.putText(img, 'OpenCv', (10,500), font, 4, (0,255,255), 10, cv.LINE_AA)

cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()