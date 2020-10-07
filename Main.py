import argparse
from pathlib import Path

from black import img_black, folder_black
from blurred import img_blurred, folder_blurred
from brightness import img_brightness, folder_brightness
from chromatic import img_chromatic, folder_chromatic
from greyscale import img_greyscale, folder_greyscale
from noise import img_noise, folder_noise
from sharpness import img_sharpness, folder_sharpness
from white import img_white, folder_white

from Rotazione import img_rotazione, folder_rotazione
from Traslazione import img_traslata, folder_traslazione
from Ridimenzionare import img_scaling, folder_scaling
from BloccoObiettivo import img_bloccoObiettivo, folder_bloccoObiettivo
from Flare import img_flare, folder_flare
from ColorTemperature import img_colorTemperature, folder_colorTemperature


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group_img = parser.add_mutually_exclusive_group()
    group_img.add_argument('--immagine', help="immagine da elavorare")
    group_img.add_argument('--folder', type=Path, help="immagini da elavorare")
    
    parser.add_argument("--save", type=Path )
   
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--black', action='store_true', help="immagine completamente nero")
    group.add_argument('--blurred', action='store_true',help="immagine sfocato")
    group.add_argument('--brightness', action='store_true',help="luminosita dell'immagine ")
    group.add_argument('--chromatic', action='store_true',help="immagine no chromatic")
    group.add_argument('--greyscale', action='store_true',help="immagine grigio")
    group.add_argument('--noise', action='store_true',help="immagine noise")
    group.add_argument('--sharpness', action='store_true',help="nitidezza dell'immagine ")
    group.add_argument('--white', action='store_true',help="immagine completamente biacno")
    
    group.add_argument('--rotazione', action='store_true',help="immagine ruotato")
    group.add_argument('--traslazione', action='store_true',help="immagine traslato")
    group.add_argument('--scaling', action='store_true',help="immagine ridimenzionato")
    group.add_argument('--obiettivo', action='store_true',help="immagine cone parzile aperture obiettivo")
    group.add_argument('--flare', action='store_true',help="immagine con flare")  
    group.add_argument('--temperatura', action='store_true',help="immagine traslato")
    
    group.add_argument('--all', action='store_true',help="tutte le elavorazioni")
    
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument('--value1', type=float , default=0, help="valore per alcune elavorazioni")
    group1.add_argument('--immagine1', help="immagine da elavorare" )
    
    parser.add_argument('--value2', type=float, default=0, help="valore per alcune elavorazioni")
    args = parser.parse_args()  
    
    if args.black:
        if args.folder:
           folder_black(args.folder,args.save)
        else:    
            img_black(args.immagine,args.save)
    elif args.blurred:
        if args.folder:
           folder_blurred(args.folder,args.save,args.value1)
        else:
            img_blurred(args.immagine,args.save,args.value1)
    elif args.brightness:
        if args.folder:
           folder_brightness(args.folder,args.save,args.value1)
        else:
            img_brightness(args.immagine,args.save,args.value1)
    elif args.chromatic:
        if args.folder:
           folder_chromatic(args.folder,args.save,args.value1)
        else:
            img_chromatic(args.immagine,args.save,args.value1)
    elif args.greyscale:
        if args.folder:
           folder_greyscale(args.folder,args.save)
        else:
            img_greyscale(args.immagine,args.save)
    elif args.noise:
        if args.folder:
           folder_noise(args.folder,args.save)
        else:
            img_noise(args.immagine,args.save)
    elif args.sharpness:
        if args.folder:
           folder_sharpness(args.folder,args.save, args.value1)
        else:
            img_sharpness(args.immagine,args.save, args.value1)
    elif args.white:
        if args.folder:
           folder_white(args.folder,args.save)
        else:
            img_white(args.immagine,args.save)
    
    
    elif args.rotazione:
        if args.folder:
            folder_rotazione(args.folder,args.save,args.value1)
        else:    
            img_rotazione(args.immagine,args.save , args.value1)
    elif args.traslazione:
        if args.folder:
            folder_traslazione(args.folder,args.save,args.value1,args.value2)
        else:
            img_traslata(args.immagine,args.save,args.value1,args.value2)
    elif args.scaling:
        if args.folder:
            folder_scaling(args.folder,args.save,args.value1)
        else:
            img_scaling(args.immagine,args.save,args.value1)
    elif args.obiettivo:
        if args.folder:
            folder_bloccoObiettivo(args.folder,args.save,args.immagine1)
        else:
            img_bloccoObiettivo(args.immagine,args.save,args.immagine1) 
    elif args.flare:
        if args.folder:
            folder_flare(args.folder,args.save,args.immagine1)
        else:
            img_flare(args.immagine,args.save,args.immagine1)
    elif args.temperatura:
        if args.folder:
            folder_colorTemperature(args.immagine,args.save,args.value1)
        else:
            img_colorTemperature(args.immagine,args.save,args.value1)
