from PIL import Image
from matplotlib import pyplot as plt

def img_black(immagine):
    picture1 = Image.open(immagine)
    picture = Image.open(immagine)
    
    pixels = picture.load()
    width, height = picture.size
    
    for i in range(0,width):
        for j in range(0,height):
            pixels[i,j] = (0, 0, 0)
    
    #picture e picture1 --> <class 'PIL.JpegImagePlugin.JpegImageFile'>
    
    #il codice sotto serve come presentazione per mostrare il fallimento
    plt.figure(num='Fallimento BLACK')
    plt.subplot(121),plt.imshow(picture1),plt.title('Originale')
    plt.xticks([]), plt.yticks([])
    picture1.show()
    plt.subplot(122),plt.imshow(picture),plt.title('Black')
    plt.xticks([]), plt.yticks([])
    plt.show()


#ok
