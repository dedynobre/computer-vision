import cv2
import numpy as np

 
img = cv2.imread("chessboard.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)


#Parameters of Harris
#blockSize - It is the size of neighbourhood considered for corner detection
#ksize - Aperture parameter of Sobel derivative used.
#k - Harris detector free parameter in the equation.

#dst = cv2.cornerHarris(gray,2,3,0.04)
#
#dst = cv2.dilate(dst,None)
#
#img[dst>dst.max()/100]=[0,0,255]
#
#cv2.imshow('dst',img)
#if cv2.waitKey(0) & 0xff == 27:
#    cv2.destroyAllWindows()
    
    
    
corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(0,0,255),3)


cv2.imshow('Shi-thomasi',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()