import argparse
from black import img_black
from blurred import img_blurred
from brightness import img_brightness
from chromatic import img_chromatic
from greyscale import img_greyscale
from noise import img_noise
from sharpness import img_sharpness

from white import img_white
from rotazione import img_rotazione

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--immagine', help="immagine da elavorare")
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
   
    group.add_argument('--all', action='store_true',help="tutte le elavorazioni")
    parser.add_argument('--value', type=float, default=0, help="valore per alcune elavorazioni")
    args = parser.parse_args()  
    
    if args.black:
        img_black(args.immagine)
    elif args.blurred:
        img_blurred(args.immagine,args.value)
    elif args.brightness:
        img_brightness(args.immagine,args.value)
    elif args.chromatic:
        img_chromatic(args.immagine,args.value)
    elif args.greyscale:
        img_greyscale(args.immagine)
    elif args.noise:
        img_noise(args.immagine)
    elif args.sharpness:
        img_sharpness(args.immagine, args.value)
        
    
    elif args.white:
        img_white(args.immagine)
    elif args.rotazione:
        img_rotazione(args.immagine, args.value)
    
    
    
    
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