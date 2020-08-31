from matplotlib import pyplot as plt
from PIL import Image


img = Image.open("Town02_003780.png")

img2 = Image.open("broken1.png").convert(img.mode) # immagini da sovrapporre all'Originale
# attenzione a che tipo di sfondo hanno, in quanto potrebbero o dare errore o scurire
# talmente tanto l'immagine che non potrebbero essere considerati come plausibili


img2 = img2.resize(img.size)

img3 = Image.blend(img,img2,0.35)#valori per immagine banding->0.02, banding1->0.05, ice->0.2

plt.figure(num='Fallimento BROKEN LENS')
plt.subplot(121),plt.imshow(img),plt.title('Originale')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img3),plt.title('Broken Lens')
plt.xticks([]), plt.yticks([])
plt.show()

#ok
