import numpy as np
import cv2
from matplotlib import pyplot as plt

def img_noise(immagine):
    img = cv2.imread(immagine)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    '''
    #Gaussian Noise (altro tipo di rumore non utilizzato)
    gauss = np.random.normal(0,1,img.size)
    gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
    # Add the Gaussian noise to the image
    noise = cv2.add(img,gauss)
    '''
    
    #Speckle Noise
    gauss = np.random.normal(0,1,img.size)
    gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
    noise = img + img * gauss
    
    plt.figure(num='Fallimento NOISE')
    plt.subplot(121),plt.imshow(img),plt.title('Originale')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(noise),plt.title('Noise')
    plt.xticks([]), plt.yticks([])
    plt.show()

#ok
