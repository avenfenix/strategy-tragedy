import pygame,sys
from pygame.locals import *

velocidad = 2
MposX = 100
MposY = 0
Width = 800
Height = 600


class Personaje:

    cont = 4
    PosX = 0
    PosY = 0
    drawed = 0
    draw_inv = 0
    isJumping = False
    JumpCount = 10
    direc = True
    i = 0

    ### Sprites
    xixf = {}
    xixf[0] = (0, 0, 26, 100)
    xixf[1] = (27, 0, 31, 100)
    xixf[2] = (61, 0, 24, 100)
    xixf[3] = (87, 0, 33, 100)

    Rxixf = {}
    Rxixf[0] = (97, 0, 23, 100)
    Rxixf[1] = (60, 0, 35, 100)
    Rxixf[2] = (37, 0, 23, 100)
    Rxixf[3] = (0, 0, 33, 100)

    def __init__(self,PosX,PosY):
        self.PosX = PosX
        self.PosY = PosY
        self.drawed = self.draw("personaje/personaje_sprite.png", True)
        self.draw_inv = pygame.transform.flip(self.drawed,True,False)

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


    def teclado(self):
        teclado = pygame.key.get_pressed()
        if teclado[K_RIGHT] and self.PosX <= Width-30-velocidad:
            self.PosX += velocidad
            self.cont += 1
            self.direc = True

        if teclado[K_LEFT] and self.PosX >= 0+velocidad:
            self.PosX -= velocidad
            self.cont += 1
            self.direc = False

        if not(self.isJumping):
            if teclado[K_UP] and self.PosY >= 0+velocidad:
                self.PosY -= velocidad
            if teclado[K_DOWN] and self.PosY <= Height-100-velocidad:
                self.PosY += velocidad
            if teclado[K_SPACE]:
                self.isJumping = True
        else:
            if self.JumpCount >= -10:
                neg = 1
                if self.JumpCount < 0:
                    neg = -1
                self.PosY-=(self.JumpCount**2)*0.5*neg
                self.JumpCount -=1
            else:
                self.isJumping = False
                self.JumpCount = 10
        

    def movimiento(self, screen):
        if self.direc:
            screen.blit(self.drawed, (self.PosX, self.PosY), (self.xixf[self.i]))
        if not self.direc:
            screen.blit(self.draw_inv, (self.PosX, self.PosY), (self.Rxixf[self.i]))

    def anim (self):

        p = 6

        if self.cont == p:
            self.i = 0

        if self.cont == p * 2:
            self.i = 1

        if self.cont == p * 3:
            self.i = 2

        if self.cont == p * 4:
            self.i = 3
            self.cont = 0

        return

def main():
    myfont = pygame.font.SysFont('Comic Sans MS', 28)

    ventana = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("Strategy Tragedy")
    clock = pygame.time.Clock()
    Charac = Personaje(10,500)
    run = True
    while run:
        time = clock.tick(60)
        Charac.anim()
        Charac.teclado()
        ventana.fill((255, 255, 255))
        Charac.movimiento(ventana)
        textsurface = myfont.render("Pos: "+str(Charac.PosX)+"-"+str(Charac.PosY)+" Vel: "+str(velocidad), False, (0, 0, 0))
        ventana.blit(textsurface,(0,0))

        for evento in pygame.event.get():
            if evento.type == QUIT:
                run = False
                
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    main()

