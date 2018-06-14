import numpy as np
import cv2

img = cv2.imread('shapes.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray,50,150,apertureSize = 3)



cv2.imshow('edges', edges)

rho = 1  # distance resolution in pixels of the Hough grid
theta = np.pi / 180  # angular resolution in radians of the Hough grid
threshold = 15  # minimum number of votes (intersections in Hough grid cell)
min_line_length = 50  # minimum number of pixels making up a line
max_line_gap = 10  # maximum gap in pixels between connectable line segments
lines = cv2.HoughLinesP(image=edges,rho=0.02,theta=np.pi/500, threshold=10,lines=np.array([]), minLineLength=min_line_length,maxLineGap=max_line_gap)


for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    
    


cv2.imshow('result', img)

cv2.waitKey(0)
cv2.destroyAllWindows()