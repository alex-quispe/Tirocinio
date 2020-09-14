from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt

def img_traslata(immagine,x,y):
    picture1 = Image.open(immagine)
    img = cv2.imread(immagine)
    num_rows, num_cols = img.shape[:2]

    traslazione = np.float32([ [1,0,x], [0,1,y] ])
    img_traslata = cv2.warpAffine(img, traslazione, (num_cols, num_rows))
    
    plt.figure(num='Fallimento Traslazione')
    plt.subplot(121),plt.imshow(picture1),plt.title('Originale')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img_traslata),plt.title('Traslazione')
    plt.xticks([]), plt.yticks([])
    plt.show()


#ok
