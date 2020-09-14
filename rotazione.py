import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w / 2, h / 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)   
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    print(cos,sin)

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

def img_rotazione(immagine, angolo):
    picture1 = Image.open(immagine)
    img=cv2.imread(immagine,1)
     
    picture = rotate_bound(img, angolo)
    #picture e picture1 --> <class 'PIL.JpegImagePlugin.JpegImageFile'>
 
    #il codice sotto serve come presentazione per mostrare il fallimento
    plt.figure(num='Fallimento ROTAZIONE')
    plt.subplot(121),plt.imshow(picture1),plt.title('Originale')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(picture),plt.title('Rotazione')
    plt.xticks([]), plt.yticks([])
    plt.show()

