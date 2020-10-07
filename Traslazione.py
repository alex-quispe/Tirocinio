import os
import cv2
import numpy as np

name = "Fallimento_TRASLAZIONE"

def img_traslata(immagine,save,x,y):
    img = cv2.imread(immagine)
    num_rows, num_cols = img.shape[:2]
    traslazione = np.float32([ [1,0,x], [0,1,y] ])
    imgT = cv2.warpAffine(img, traslazione, (num_cols, num_rows))
    i = 1
    while os.path.exists(os.path.join(save, name+str(i)+".png")):
        i+=1       
    cv2.imwrite(os.path.join(save, name+str(i)+".png"),imgT)
    

def folder_traslazione(path, save, x, y):
    temp =os.listdir(path)
    for img in temp:
        if (img.endswith('png') or img.endswith('jpg') ):
            img_traslata(os.path.join(path, img), save, x, y) 
    