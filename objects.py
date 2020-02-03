import pygame, sys
from pygame.locals import *
from colors import *
vec = pygame.math.Vector2
velocidad = 2

class Personaje:

    def __init__(self, PosX, PosY):
        self.Pos = vec(PosX, PosY)
        self.Vel = vec(2, 0)
        self.Acc = vec(0, 0)
        self.WalkCount = 0
        self.draw_quieto = self.get_image("personaje/personaje-principal.png", True)
        self.right = False
        self.left = False
        self.lastDir = "Right"
        self.hitbox = self.draw_quieto.get_rect()
        self.Floor = False
        

        # Carga de Sprites
        self.xixf = []
        for i in range(1, 23):
            if i < 10:
                p = "0" + str(i)
            else:
                p = str(i)
            draw = self.get_image(f"personaje/corriendo/personaje-corriendo00{p}.png", True)
            self.xixf.append(draw)
        self.Rxixf = []
        for i in range(0, 22):
            draw = pygame.transform.flip(self.xixf[i], True, False)
            self.Rxixf.append(draw)

    def get_image(self, filename, transparent=False, convertir=False):
        try:
            image = pygame.image.load(filename)
        except pygame.error:
            raise SystemExit
        if transparent:
            color = image.get_at((0, 0))
            image.set_colorkey(color, RLEACCEL)
        if convertir:
            image = image.convert()
        return image

    def teclado(self):

        self.Acc = vec(0, 0.5)
        self.Acc.x += self.Vel.x * (-0.12)
        self.Vel.y += self.Acc.y
        self.Pos.y += self.Vel.y + 0.5 * self.Acc.y

        teclado = pygame.key.get_pressed()

        if self.Pos.y > 566:
            self.Pos.y = 566
            self.Floor = True
        else:
            self.Floor = False

        if teclado[K_RIGHT]:
            if teclado[K_LSHIFT]:
                self.Pos.x += velocidad*3
            else:
                self.Pos.x += velocidad
            self.right = True
            self.left = False
            self.lastDir = "Right"

        if teclado[K_LEFT]:
            if teclado[K_LSHIFT]:
                self.Pos.x -= velocidad*3
            else:
                self.Pos.x -= velocidad
            self.left = True
            self.right = False
            self.lastDir = "Left"

        if not (teclado[K_RIGHT] or teclado[K_LEFT]) or  (teclado[K_RIGHT] and teclado[K_LEFT]) :
            self.right = False
            self.left = False

        if self.Floor:
            if teclado[K_SPACE]:
                self.Vel.y = -10
            

        self.hitbox.midbottom = self.Pos + vec(0,self.hitbox.h)

    def movimiento(self, screen):

        if self.WalkCount + 1 >= 66:
            self.WalkCount = 0
        if self.right:
            screen.blit(self.xixf[self.WalkCount // 3], (self.Pos.x, self.Pos.y))
            self.WalkCount += 2
        if self.left:
            screen.blit(self.Rxixf[self.WalkCount // 3], (self.Pos.x, self.Pos.y))
            self.WalkCount += 2
        if (self.left or self.right) == False and self.lastDir == "Right":
            screen.blit(self.draw_quieto, (self.Pos.x, self.Pos.y))
        if (self.left or self.right) == False and self.lastDir == "Left":
            screen.blit(pygame.transform.flip(self.draw_quieto, True, False), (self.Pos.x, self.Pos.y))

        return

class Platform():
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y