import os
from PIL import Image

name = "Fallimento_ROTAZIONE"

def img_rotazione(immagine, save, angolo):
    imgR = Image.open(immagine)
    white=(255,255,255)
    imgR=imgR.rotate(angolo, expand=1, fillcolor=white)
    i = 1
    while os.path.exists(os.path.join(save, name+str(i)+".png")):
        i+=1       
    imgR.save(os.path.join(save, name+str(i)+".png"),"PNG")
    
    
def folder_rotazione(path, save, angolo):
    temp =os.listdir(path)
    for img in temp:
        if (img.endswith('png') or img.endswith('jpg') ):
            img_rotazione(os.path.join(path, img), save, angolo) 
    