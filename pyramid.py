

import cv2
import numpy as np
from matplotlib import pyplot as plt
    
img = cv2.imread('foto.jpg',0)

lower = img
 
for i in range(4):
    lower = cv2.pyrDown(lower)
    cv2.imshow("lower",lower)
    
    k = cv2.waitKey(0)
    if k==27:    # Esc key to stop
        continue
 
  
upper = lower


for i in range(3):
    upper = cv2.pyrUp(upper)
    cv2.imshow("upper",upper)
    
    k = cv2.waitKey(0)
    if k==27:    # Esc key to stop
        continue
    
    
cv2.destroyAllWindows()
    







