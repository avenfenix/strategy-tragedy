import pygame,sys
from pygame.locals import *

velocidad = 10
MposX = 100
MposY = 0
Width = 800
Height = 600



class Personaje:

    PosX = 0
    PosY = 0
    drawed = 0
    isJumping = False

    def __init__(self,PosX,PosY):
        self.PosX = PosX
        self.PosY = PosY
        self.drawed = self.draw("personaje/personaje.png", True)

    def draw (self , filename, transparent=False, conv=False):
        try:
            image = pygame.image.load(filename)
        except pygame.error:
            raise SystemExit
        if transparent:
            color = image.get_at((0, 0))
            image.set_colorkey(color, RLEACCEL)
        if conv:
            image = image.convert()
        return image


    def movimiento(self):
        teclado = pygame.key.get_pressed()

        
        if teclado[K_RIGHT] and self.PosX <= Width-40:
            self.PosX += velocidad

        if teclado[K_LEFT] and self.PosX >= 10:
            self.PosX -= velocidad

        if teclado[K_DOWN] and self.PosY <= Height-110:
            self.PosY += velocidad

        if self.isJumping == False:
            if teclado[K_UP] and self.PosY >= 0:
                self.PosY -= velocidad

        
    


def main():
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    ventana = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("The Furrnite")
    clock = pygame.time.Clock()
    Charac = Personaje(10,50)

    while True:
        time = clock.tick(60)
        Charac.movimiento()
        ventana.fill((255, 255, 255))
        ventana.blit(Charac.drawed, (Charac.PosX, Charac.PosY))
        textsurface = myfont.render(str(Charac.PosX)+"-"+str(Charac.PosY), False, (0, 0, 0))
        ventana.blit(textsurface,(0,0))

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()

