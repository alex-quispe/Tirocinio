import argparse
from pathlib import Path
from black import img_black
from blurred import img_blurred
from brightness import img_brightness
from chromatic import img_chromatic
from greyscale import img_greyscale
from noise import img_noise
from sharpness import img_sharpness

from white import img_white


from rotazione import img_rotazione, folder_rotazione
from traslazione import img_traslata
from ridimenzionare import img_scaling

from Flare import img_flare
from ColorTemperature import img_colorTemperature


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
    #group.add_argument('--sovrapposizine', action='store_true',help="immagine sovrapposto")
    group.add_argument('--white', action='store_true',help="immagine completamente biacno")
    
    group.add_argument('--rotazione', action='store_true',help="immagine ruotato")
    group.add_argument('--traslazione', action='store_true',help="immagine traslato")
    group.add_argument('--scaling', action='store_true',help="immagine ridimenzionato")
    
    group.add_argument('--flare', action='store_true',help="immagine con flare")  
    group.add_argument('--temperatura', action='store_true',help="immagine traslato")
    
    group.add_argument('--all', action='store_true',help="tutte le elavorazioni")
    
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument('--value1', type=float , default=0, help="valore per alcune elavorazioni")
    group1.add_argument('--immagine1', help="immagine da elavorare" )
    
    parser.add_argument('--value2', type=float, default=0, help="valore per alcune elavorazioni")
    args = parser.parse_args()  
    
    if args.black:
        img_black(args.immagine)
    elif args.blurred:
        img_blurred(args.immagine,args.value1)
    elif args.brightness:
        img_brightness(args.immagine,args.value1)
    elif args.chromatic:
        img_chromatic(args.immagine,args.value1)
    elif args.greyscale:
        img_greyscale(args.immagine)
    elif args.noise:
        img_noise(args.immagine)
    elif args.sharpness:
        img_sharpness(args.immagine, args.value1)
        
    
    elif args.white:
        img_white(args.immagine)
    
    
    
    elif args.rotazione:
        if args.folder:
            folder_rotazione(args.folder,args.save,args.value1)
        else:    
            img_rotazione(args.immagine,args.save , args.value1)
    elif args.traslazione:
        img_traslata(args.immagine, args.value1,args.value2)
    elif args.scaling:
        img_scaling(args.immagine, args.value1)
    
    
    elif args.flare:
        img_flare(args.immagine, args.immagine1)
    elif args.temperatura:
        img_colorTemperature(args.immagine, args.value1)
    
    
    
    #elif args.all:
    #   img_black(args.immagine)
    #    img_blurred(args.immagine,args.value)
    #    img_brightness(args.immagine,args.value)
    #    img_chromatic(args.immagine,args.value)
    #    img_greyscale(args.immagine)
    #    img_noise(args.immagine)
    #    img_sharpness(args.immagine, args.value)
    #    
    #    img_white(args.immagine)