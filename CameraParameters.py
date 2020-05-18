import cv2 as cv

cap = cv.VideoCapture(0);
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))

cap.set(3, 1000)
cap.set(4, 1000)

print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv.destroyAllWindows()