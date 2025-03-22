import numpy as np
import cv2 as cv

# Drawing Line
# Create a black image
img = np.zeros((512,512,3), np.uint8)
 
# Draw a diagonal blue line with thickness of 5 px
# 좌표 (0,0) -> (511,511) 색상 (255,0,0) 굵기 5
cv.line(img,(0,0),(511,511),(255,0,0),5)

# Drawing Rectangle
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Drawing Circle
# 중심 (447,63) 반지름 63 채운 그림 -1
cv.circle(img,(447,63), 63, (0,0,255), -1)

# Drawing Ellipse
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Drawing Polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

# Adding Text to Images:
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

# Display the image in a window
cv.imshow('Drawing', img)

# Wait for the user to press any key to close the window
cv.waitKey(0)

# Close all OpenCV windows
cv.destroyAllWindows()