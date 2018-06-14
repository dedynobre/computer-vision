import cv2
import numpy as np

img = cv2.imread('shapes.jpg',0)
#img = cv2.imread('opencv-logo.png',0)
img = cv2.medianBlur(img,5)
color_img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)


#img = cv2.threshold(img, 50, 255,cv2.THRESH_BINARY)[1]


dp=1 # Inverse ratio of the accumulator resolution to the image resolution
minDist=10 # Minimum distance between the centers of the detected circles
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,dp,minDist,
                            param1=50,param2=30,minRadius=0,maxRadius=300)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(color_img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(color_img,(i[0],i[1]),2,(0,0,255),3)


#cv2.imshow('thresh',img)
cv2.imshow('detected circles',color_img)
cv2.waitKey(0)
cv2.destroyAllWindows()