from matplotlib import pyplot as plt
from PIL import Image, ImageEnhance

def img_flare(immagine,imgFlare):
   #per sovrapporre un'immagine con sfondo trasparente ad un'immagine esistente
   img = Image.open(immagine)
   imgf = Image.open(imgFlare).convert("RGBA")
   imgf=imgf.resize(img.size)
   img.paste(imgf,(0,0),imgf)

   '''##per effettuare blend, e sovrapporre immagini non trasparenti
   img = Image.open(immagine)
   imgf = Image.open(imgFlare)
   imgf=imgf.resize(img.size)
   immagineFinale=Image.blend(img,imgf, 0.25)
   enhancer=ImageEnhance.Brightness(immagineFinale)
   immagineFinale=enhancer.enhance(1.5)'''
    
    
   plt.figure(num='Fallimento Flare')
   plt.subplot(121),plt.imshow(img),plt.title('Originale')
   plt.xticks([]), plt.yticks([])
   plt.subplot(122),plt.imshow(imgf),plt.title('Flare')
   plt.xticks([]), plt.yticks([])
   plt.show()