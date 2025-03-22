# Ex10 : adjust circle color using a trackbar in opencv
import numpy as np
import cv2 as cv

def nothing(x):
    pass

# Create a black image, a window
img = np.ones((512,512,3), np.uint8) * 255

# create window
cv.namedWindow('Trackbar Window')

# create trackbars for color change
cv.createTrackbar('R', 'Trackbar Window',0,255,nothing)
cv.createTrackbar('G', 'Trackbar Window',0,255,nothing)
cv.createTrackbar('B', 'Trackbar Window',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1: ON'
cv.createTrackbar(switch,'Trackbar Window',0,1,nothing)

while True:
    # get current positions of the three trackbar
    r = cv.getTrackbarPos('R', 'Trackbar Window')
    g = cv.getTrackbarPos('G', 'Trackbar Window')
    b = cv.getTrackbarPos('B', 'Trackbar Window')
    s = cv.getTrackbarPos(switch,'Trackbar Window')
    
    # switch
    if s == 0:
        b,g,r = 0,0,0
    else:
        pass
    
    # draw the circle with the current RGB value from the trackbar
    cv.circle(img, (256,256), 100, (b,g,r), -1)
    
    # display image
    cv.imshow('Trackbar Window', img)
    
    # Break point
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()