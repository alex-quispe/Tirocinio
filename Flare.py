import os
from PIL import Image

name = "Fallimento_FLARE"

def img_flare(immagine,save,imgFlare):
   #per sovrapporre un'immagine con sfondo trasparente ad un'immagine esistente
   img = Image.open(immagine)
   imgF = Image.open(imgFlare).convert("RGBA")
   imgF=imgF.resize(img.size)
   img.paste(imgF,(0,0),imgF)
   i = 1
   while os.path.exists(os.path.join(save, name+str(i)+".png")):
       i+=1       
   img.save(os.path.join(save, name+str(i)+".png"),"PNG")

   '''##per effettuare blend, e sovrapporre immagini non trasparenti
   img = Image.open(immagine)
   imgF = Image.open(imgFlare)
   imgF=imgF.resize(img.size)
   immagineFinale=Image.blend(img,imgF, 0.25)
   enhancer=ImageEnhance.Brightness(immagineFinale)
   immagineFinale=enhancer.enhance(1.5)'''
    
   
def folder_flare(path, save, imgFlare):
    print(path)
    temp = os.listdir(path)
    for img in temp:
        if (img.endswith('png') or img.endswith('jpg') ):
            print(path)
            print(img)
            img_flare(os.path.join(path,img), save, imgFlare) 
            