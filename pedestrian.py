
import imutils
from imutils.object_detection import non_max_suppression

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2


# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


goruntu = 'set01_V003_I00699.mat'
mat_contents = sio.loadmat(goruntu)

I = mat_contents["im"]


image = I[:,:,3]

image = imutils.resize(image, width=min(800, image.shape[1]))
orig = image.copy() 

# detect people in the image
(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
padding=(8, 8), scale=1.01)
# draw the original bounding boxes
for (x, y, w, h) in rects:
     cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)
     
    
# apply non-maxima suppression to the bounding boxes using a
# fairly large overlap threshold to try to maintain overlapping
# boxes that are still people
rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
pick = non_max_suppression(rects, probs=None, overlapThresh=0.1)
# draw the final bounding boxes
for (xA, yA, xB, yB) in pick:
    cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
# show the output images
plt.figure(0)
plt1=plt.imshow(orig)
plt.figure(1)
plt2=plt.imshow(image)