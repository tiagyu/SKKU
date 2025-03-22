import cv2 as cv
import sys

img = cv.imread("starry_night.jpg")

if img is None:
    sys.exit("There is no image")
    
cv.imshow("Display window", img)

# How long should it wait for a user input (measured in millisecond)
# zero means to wait forever
k = cv.waitKey(0)

# python ord() function returns the Unicode code from a given character
if k == ord("s"):
    # the image is written to a file if the pressed key was the "s" key
    cv.imwrite("starry_night.png", img)