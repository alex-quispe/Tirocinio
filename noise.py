import os
import numpy as np
import cv2

name = "Fallimento_NOISE"

def img_noise(immagine,save):
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
    i = 1
    while os.path.exists(os.path.join(save, name+str(i)+".png")):
        i+=1       
    cv2.imwrite(os.path.join(save, name+str(i)+".png"),noise)

def folder_noise(path, save):
    temp =os.listdir(path)
    for img in temp:
        if (img.endswith('png') or img.endswith('jpg') ):
            img_noise(os.path.join(path, img), save)