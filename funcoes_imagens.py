import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def soma(a, b):
    
    t = a + b
    
    return t

def carrega_imagem():

    imagem = "images/carro.jpg"


    #carrega imagem
    img = cv.imread(imagem)
    
    #carrega a imgagem em escala de cinza
    img = cv.imread("images/carro.jpg", cv.IMREAD_GRAYSCALE)
    
    #escreve imagem
    cv.imwrite("images/carro2.png", img)
    
    #mostra imagem
    cv.imshow("Carro", img)
    cv.waitKey(0)
    cv.destroyAllWindows()    

    return 

def carrega_plot():
    
    img = cv.imread("images/carro.jpg")
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()
    
    return

def carrega_cnz():
    
    img = cv.IMREAD_COLOR("images/carro.jpg")
    cv.imshow("Carro", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    return

def plots():
    
    filename = 'images/carro2.png'
    img = cv.imread(filename)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
    dst = cv.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.01*dst.max()]=[0,0,255]
    cv.imshow('dst',img)
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()
    