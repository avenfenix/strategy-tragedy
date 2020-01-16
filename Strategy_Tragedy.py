import pygame,sys
from pygame.locals import *

velocidad = 10
MposX = 100

cont= 4
direc=True
i=0
xixf={}
Rxixf={}


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

def sprite():
    global cont

    xixf[0]=(0,0,30,100)
    xixf[1]=(30,0,30,100)
    xixf[2]=(60,0,30,100)
    xixf[3]=(90,0,30,100)

    Rxixf[0]=(90,0,0,100)
    Rxixf[1]=(60,0,0,100)
    Rxixf[2]=(30,0,0,100)
    Rxixf[3]=(0,0,0,100)

    p=4

    global i

    if cont==p*2:
        i=0
    if cont==p*4:
        i=1
    if cont==p*6:
        i=2
    if cont==p*8:
        i=3
        cont=0
    return
    
    

def teclado():
    teclado = pygame.key.get_pressed()
    global MposX, cont

    if teclado[K_RIGHT]:
        MposX+=2
        cont+=1

    if teclado[K_LEFT]:
        MposX-=2
        cont+=1

    if teclado[K_q]:
        MposX+=2

def main():
    
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("The Furrnite")    
    personaje = imagen("personaje/personaje_sprite.png",True)
    personaje_inv = pygame.transform.flip(personaje,True,False);
    clock = pygame.time.Clock()
    
    while True:
        time = clock.tick(60)
        sprite()
        teclado()
        ventana.fill((255,255,255))
        
        if direc == True:
            ventana.blit(personaje,(MposX,0),(xixf[i]))
        if direc == False:
            ventana.blit(personaje_inv,(MposX,0),(Rxixf[i]))
            
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    main()



