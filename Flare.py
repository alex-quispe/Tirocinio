from matplotlib import pyplot as plt
from PIL import Image

def img_flare(immagine,imgFlare):
    img = Image.open(immagine)
    img1 = Image.open(imgFlare).convert(img.mode)
    img1 = img1.resize(img.size)
    img2 = Image.blend(img,img1,0.5)
    
    plt.figure(num='Fallimento Flare')
    plt.subplot(121),plt.imshow(img),plt.title('Originale')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img2),plt.title('Flare')
    plt.xticks([]), plt.yticks([])
    plt.show()