import os
from PIL import Image, ImageEnhance

name = "Fallimento_SHARPNESS"

'''
Sharpness: This class can be used to adjust the sharpness
of an image. An enhancement factor of 0.0 gives a
blurred image, a factor of 1.0 gives the original
image, and a factor of 2.0 gives a sharpened image.
'''
def img_sharpness(immagine,save, valore):
    img = Image.open(immagine) #se apri l'immagine con Image.open() non ci sono problemi
                                 # con i canali dei colori, se invece usi cv2.imread()
                                 # devi usare cv2.cvtColor(img, cv2.COLOR_BGR2RGB) per avere
                                 # colori corretti
    
    enhancer = ImageEnhance.Sharpness(img)
    
    '''
    
    esempi:
    
    factor = 1 --> img Originale
    factor = 3 --> img visibilmente più definita (non sempre un bene)
    factor = -3.5 --> img sfocata, non nitida (si avvicina molto al guasto Blurred)
    
    '''
    
    factor = valore
    img2 = enhancer.enhance(factor)
    i = 1
    while os.path.exists(os.path.join(save, name+str(i)+".png")):
        i+=1       
    img2.save(os.path.join(save, name+str(i)+".png"),"PNG")
    
def folder_sharpness(path, save, valore):
    temp =os.listdir(path)
    for img in temp:
        if (img.endswith('png') or img.endswith('jpg') ):
            img_sharpness(os.path.join(path, img), save, valore)