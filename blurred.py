import cv2
from matplotlib import pyplot as plt

def img_blurred(immagine, valore):
    img = cv2.imread(immagine)
    
    blur = cv2.blur(img,(valore,valore)) #cambiare valori per aumentare o diminuire sfocatura
    
    #blur e img --> <class 'numpy.ndarray'>
    
    #il codice sotto serve come presentazione per mostrare il fallimento
    plt.figure(num='Fallimento BLURRED')
    plt.subplot(121),plt.imshow(img),plt.title('Originale')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('Sfocata')
    plt.xticks([]), plt.yticks([])
    plt.show()

#ok
