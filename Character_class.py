import pygame, sys
from pygame.locals import *
display_width = 800
display_height = 600
velocidad = 2
class Personaje:

    def __init__(self, PosX, PosY):
        self.PosX = PosX
        self.PosY = PosY
        self.WalkCount = 4
        self.draw_quieto = self.get_image("personaje/personaje-principal.png", True)
        self.isJumping = False
        self.JumpCount = 10
        self.right = False
        self.left = False
        self.lastDir = "Right"

        #Carga de Sprites
        self.xixf = []
        for i in range(1,23):
            if i < 10:
              p = "0"+str(i)
            else:
                p = str(i)
            draw = self.get_image(f"personaje/corriendo/personaje-corriendo00{p}.png", True)
            self.xixf.append(draw)
        self.Rxixf = []
        for i in range(0,22):
            draw = pygame.transform.flip(self.xixf[i], True, False)
            self.Rxixf.append(draw)

    def get_image(self, filename, transparent=False, conv=False):
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
        if teclado[K_RIGHT] and self.PosX <= display_width - 133 - velocidad:
            self.PosX += velocidad
            self.right = True
            self.left = False
            self.lastDir = "Right"

        if teclado[K_LEFT] and self.PosX >= 0 + velocidad:
            self.PosX -= velocidad
            self.left = True
            self.right = False
            self.lastDir = "Left"
            
        if not (teclado[K_RIGHT] or teclado[K_LEFT]):
            self.right = False
            self.left = False

        if not (self.isJumping):
            if teclado[K_UP] and self.PosY >= 0 + velocidad:
                self.PosY -= velocidad
            if teclado[K_DOWN] and self.PosY <= display_height - 133 - velocidad:
                self.PosY += velocidad
            if teclado[K_SPACE]:
                self.isJumping = True
        else:
            if self.JumpCount >= -10:
                neg = 1
                if self.JumpCount < 0:
                    neg = -1
                self.PosY -= (self.JumpCount ** 2) * 0.5 * neg
                self.JumpCount -= 1
            else:
                self.isJumping = False
                self.JumpCount = 10

    def movimiento(self, screen):
        if self.WalkCount + 1 >= 66:
            self.WalkCount = 0
        if self.right:
            screen.blit(self.xixf[self.WalkCount//3], (self.PosX, self.PosY))
            self.WalkCount += 2
        if self.left:
            screen.blit(self.Rxixf[self.WalkCount//3], (self.PosX, self.PosY))
            self.WalkCount += 2
        if (self.left or self.right) == False and self.lastDir == "Right":
            screen.blit(self.draw_quieto, (self.PosX, self.PosY) )
        if (self.left or self.right) == False and self.lastDir == "Left":
            screen.blit(pygame.transform.flip(self.draw_quieto,True, False), (self.PosX, self.PosY) )

        return
