from PIL import Image
import os

name = "Fallimento_RIDIMENZIONAMENTO"

def img_scaling(immagine, save, value):
    img = Image.open(immagine)
    imgS = Image.open(immagine)
    imgS = imgS.resize((round(img.size[0]*value), round(img.size[1]*value)))
    i = 1
    while os.path.exists(os.path.join(save, name+str(i)+".png")):
        i+=1       
    imgS.save(os.path.join(save, name+str(i)+".png"),"PNG")


def folder_scaling(path, save, value):
    temp =os.listdir(path)
    for img in temp:
        if (img.endswith('png') or img.endswith('jpg') ):
            img_scaling(os.path.join(path, img), save, value) 
     