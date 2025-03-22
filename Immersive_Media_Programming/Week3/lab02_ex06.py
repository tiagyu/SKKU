import cv2 as cv
import numpy as np

img = np.ones((512,512,3), np.uint8) * 255

# 색깔 지정하기
red = (0,0,255)
blue = (255,0,0)
green = (0,255,0)
yellow = (0,255,255)
black = (0,0,0)

# Rectangle 그리기
# 첫 번째 빨간 상자
cv.rectangle(img,(100,250),(150,300),red, -1)

# 그린 상자
cv.rectangle(img, (160, 250),(210,300),green,-1)

# 파란 상자
cv.rectangle(img, (100,310),(150,360),blue,-1)

# 노란 상자
cv.rectangle(img,(160,310),(210,360), yellow,-1)

# 글자 쓰기
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "Microsoft", (215,320), font, 2, black, 3, cv.LINE_AA)

# display the image
cv.imshow('Microsfot logo', img)

# wait for a key press and close window
cv.waitKey(0)
cv.destroyAllWindows()