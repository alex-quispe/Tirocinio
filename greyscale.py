import os
from PIL import Image

name = "Fallimento_NOISE"

def img_greyscale(immagine,save):  
    gray = Image.open(immagine).convert('LA')
    i = 1
    while os.path.exists(os.path.join(save, name+str(i)+".png")):
        i+=1       
    gray.save(os.path.join(save, name+str(i)+".png"),"PNG")

def folder_greyscale(path, save):
    temp =os.listdir(path)
    for img in temp:
        if (img.endswith('png') or img.endswith('jpg') ):
            img_greyscale(os.path.join(path, img), save)
