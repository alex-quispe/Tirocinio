from PIL import Image
import os
from matplotlib import pyplot as plt
name = "Fallimento_ROTAZIONE"
def img_rotazione(immagine, save, angolo):
    i = 1
    picture1 = Image.open(immagine)
    picture = Image.open(immagine)
    white=(255,255,255)
    picture=picture.rotate(angolo, expand=1, fillcolor=white)
    print (immagine)
    while os.path.exists(os.path.join(save, name+str(i)+".png")):
        i+=1       
    picture.save(os.path.join(save, name+str(i)+".png"),"PNG")
    
 
    #il codice sotto serve come presentazione per mostrare il fallimento
    plt.figure(num='Fallimento ROTAZIONE')
    plt.subplot(121),plt.imshow(picture1),plt.title('Originale')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(picture),plt.title('Rotazione')
    plt.xticks([]), plt.yticks([])
    plt.show()

def folder_rotazione(path, save, angolo):
    temp =os.listdir(path)
    for img in temp:
        if (img.endswith('png') or img.endswith('jpg') ):
            img_rotazione(os.path.join(path, img), save, angolo) 
    
        