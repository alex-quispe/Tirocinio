from PIL import Image
#from matplotlib import pyplot as plt

def img_scaling(immagine, x):
    img = Image.open(immagine)
    imgS = Image.open(immagine)
    imgS = imgS.resize((round(img.size[0]*x), round(img.size[1]*x)))

 
    '''#il codice sotto serve come presentazione per mostrare il fallimento
    plt.figure(num='Fallimento ROTAZIONE')
    plt.subplot(121),plt.imshow(img),plt.title('Originale')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(imgS),plt.title('Rotazione')
    plt.xticks([]), plt.yticks([])
    plt.show()'''