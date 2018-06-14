

import cv2
import numpy as np
from matplotlib import pyplot as plt
    
img = cv2.imread('images/foto.jpg',0)


hist,bins = np.histogram(img.flatten(),256,[0,256])
#plt.plot(hist, color = 'b')
#plt.hist(img.flatten(),256,[0,256], color = 'r')


cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

##
#equ = cv2.equalizeHist(img)
#cv2.imwrite('equ.jpg',equ)






