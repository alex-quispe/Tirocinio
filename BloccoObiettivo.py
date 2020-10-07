import os
from PIL import Image

name = "Fallimento_PARZIALE_APERTURA_OBIETTIVO"

def img_bloccoObiettivo(immagine,save,imgObiettivo):
   #per sovrapporre un'immagine con sfondo trasparente ad un'immagine esistente
   img = Image.open(immagine)
   imgO = Image.open(imgObiettivo).convert("RGBA")
   imgO=imgO.resize(img.size)
   img.paste(imgO,(0,0),imgO)
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
    
   
def folder_bloccoObiettivo(path, save, imgObiettivo):
    temp =os.listdir(path)
    for img in temp:
        if (img.endswith('png') or img.endswith('jpg') ):
            img_bloccoObiettivo(os.path.join(path, img), save, imgObiettivo) 