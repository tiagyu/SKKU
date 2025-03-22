import numpy as np
import cv2 as cv
 
cap = cv.VideoCapture('vtest.avi')
 
while cap.isOpened():
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 
    cv.imshow('frame', gray) # 어떻게 읽느냐에 따라 불러오는게 달라짐
    if cv.waitKey(1) == ord('q'):
        break
 
cap.release()
cv.destroyAllWindows()