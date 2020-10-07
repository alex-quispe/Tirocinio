import os
from PIL import Image

name = "Fallimento_WHITE"

def img_white(immagine,save):
    picture = Image.open(immagine)
    
    pixels = picture.load()
    width, height = picture.size
    
    for i in range(0,width):
        for j in range(0,height):
            pixels[i,j] = (255, 255, 255)
    i = 1
    while os.path.exists(os.path.join(save, name+str(i)+".png")):
        i+=1       
    picture.save(os.path.join(save, name+str(i)+".png"),"PNG")
    
def folder_white(path, save):
    temp =os.listdir(path)
    for img in temp:
        if (img.endswith('png') or img.endswith('jpg') ):
            img_white(os.path.join(path, img), save)