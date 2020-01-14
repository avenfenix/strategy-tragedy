import pygame,sys
from pygame.locals import *

velocidad = 10
MposX = 100

def imagen(filename, transparent=False, conv=False):
    try: image = pygame.image.load(filename)
    except pygame.error:
        raise SystemExit
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    if conv:
        image = image.convert()
    return image

def teclado():
    teclado = pygame.key.get_pressed()
    global MposX

    if teclado[K_RIGHT]:
        MposX+=2

    if teclado[K_LEFT]:
        MposX-=2

    if teclado[K_q]:
        MposX+=2

def main():    
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("The Furrnite")    
    personaje = imagen("personaje/personaje.png",True)
    clock = pygame.time.Clock()
    
    while True:
        time = clock.tick(60)
        teclado()
        ventana.fill((255,255,255))
        ventana.blit(personaje,(MposX,0))        
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    main()



