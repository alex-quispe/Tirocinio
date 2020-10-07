import os
import cv2

name = "Fallimento_BLURRED"

def img_blurred(immagine, save, valore):
    img = cv2.imread(immagine)
    
    blur = cv2.blur(img,(int(valore),int(valore))) #cambiare valori per aumentare o diminuire sfocatura
    i = 1
    while os.path.exists(os.path.join(save, name+str(i)+".png")):
        i+=1       
    cv2.imwrite(os.path.join(save, name+str(i)+".png"),blur)

def folder_blurred(path, save,valore):
    temp =os.listdir(path)
    for img in temp:
        if (img.endswith('png') or img.endswith('jpg') ):
            img_blurred(os.path.join(path, img), save, valore)
