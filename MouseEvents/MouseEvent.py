import numpy as np
import cv2 as cv

#Print all events
#events = [i for i in dir(cv) if 'EVENT' in i]
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        font = cv.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv.imshow('image', img)
    if event == cv.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
        cv.imshow('image', img)

#img = np.zeros((512, 512, 3), np.uint8)
img = cv.imread('../lena.jpg')
cv.imshow('image', img)

cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()