import os
from PIL import Image, ImageEnhance

name = "Fallimento_BRIGHTNESS"

'''
Brightness: This class can be used to control the
brightness of an image. An enhancement
factor of 0.0 gives a black image.
A factor of 1.0 gives the original image.
'''
def img_brightness(immagine,save, valore):

    img = Image.open(immagine)
    
    enhancer = ImageEnhance.Brightness(img)

    
    factor = valore
    img2 = enhancer.enhance(factor)
    i = 1
    while os.path.exists(os.path.join(save, name+str(i)+".png")):
        i+=1       
    img2.save(os.path.join(save, name+str(i)+".png"),"PNG")
    
def folder_brightness(path, save, valore):
    temp =os.listdir(path)
    for img in temp:
        if (img.endswith('png') or img.endswith('jpg') ):
            img_brightness(os.path.join(path, img), save, valore)


