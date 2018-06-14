import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def mostra_video():
    
    
    
    cap = cv.VideoCapture(0)
    while(True):
    # Capture frame-by-frame
        ret, frame = cap.read()
    # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
        cv.imshow('frame',gray)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
# When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
    
    return
    
    
def salva_video():
    

    cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv.flip(frame,0)
        # write the flipped frame
            out.write(frame)
            cv.imshow('frame',frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            else:
                break
# Release everything if job is finished
    cap.release()
    out.release()
    cv.destroyAllWindows()    
    
    return  
    
def video_back():
    
    cap = cv.VideoCapture(0)
    fgbg = cv.createBackgroundSubtractorMOG2()
    while True:
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)
        cv.imshow('frame',fgmask)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
        cap.release()
        cv.destroyAllWindows()
        
    return
        
def video_norm_gray():
    
    cap = cv.VideoCapture(0)
    
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    
    out = cv.VideoWriter('videos/output.avi', fourcc, 20.0, (640,480))
    
    while True:
        
        ret, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
        out.write(frame)
        
        cv.imshow('Normal', frame)
        cv.imshow('Cinza', gray)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    out.release()
    cv.destroyAllWindows()
    
    return