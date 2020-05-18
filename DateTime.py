import cv2 as cv
import datetime

cap = cv.VideoCapture(0);
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        font = cv.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + 'Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv.putText(frame, datet, (10, 50), font, 1,
                           (0, 255, 255), 2, cv.LINE_AA)
        cv.imshow('frame', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv.destroyAllWindows()