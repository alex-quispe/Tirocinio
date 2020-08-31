import cv2
from PIL import Image
from matplotlib import pyplot as plt

def img_rotazione(immagine, valore):
    img=cv2.imread(immagine,1)
    picture1 = Image.open(immagine)
    rows,cols,ht=img.shape
    
    rotazione = cv2.getRotationMatrix2D((rows/2,cols/2),valore,1)
    
    picture = cv2.warpAffine(img,rotazione,(rows,cols))
    #picture e picture1 --> <class 'PIL.JpegImagePlugin.JpegImageFile'>
    
    cv2.imshow('out', picture)
    
    #il codice sotto serve come presentazione per mostrare il fallimento
    plt.figure(num='Fallimento ROTAZIONE')
    plt.subplot(121),plt.imshow(picture1),plt.title('Originale')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(picture),plt.title('Rotazione')
    plt.xticks([]), plt.yticks([])
    plt.show()

