import pygame, sys
from pygame.locals import *
from colors import *
from settings import *
vec = pygame.math.Vector2

class Personaje(pygame.sprite.Sprite):
    def __init__(self, PosX, PosY):
        pygame.sprite.Sprite.__init__(self)
        self.Pos = vec(PosX, PosY)
        self.Vel = vec(0, 0)
        self.Acc = vec(0, 0)
        self.WalkCount = 0
        self.draw_quieto = self.get_image("personaje/personaje-principal.png", True)
        self.right = False
        self.left = False
        self.lastDir = "Right"
        self.rect = self.draw_quieto.get_rect()
        self.rect.topleft = self.Pos + vec(25,8)
        self.rect.h = self.rect.h - 18
        self.rect.w = self.rect.w - 50
        self.Floor = False
        self.Col = False
        
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

        self.Acc = vec(0, PLAYER_GRAVITY)
        teclado = pygame.key.get_pressed()

        if self.Pos.y > 566:
            self.Pos.y = 566
            self.Vel.y = 0
            self.Floor = True
        else:
            self.Floor = False
        
        
        if teclado[K_RIGHT]:
            if teclado[K_LSHIFT]:
                self.Acc.x += PLAYER_ACC*3
            else:
                self.Acc.x += PLAYER_ACC
            self.right = True
            self.left = False
            self.lastDir = "Right"
        if teclado[K_LEFT]:
            if teclado[K_LSHIFT]:
                self.Acc.x -= PLAYER_ACC*3
            else:
                self.Acc.x -= PLAYER_ACC
            self.left = True
            self.right = False
            self.lastDir = "Left"
        if not (teclado[K_RIGHT] or teclado[K_LEFT]) or  (teclado[K_RIGHT] and teclado[K_LEFT]) :
            self.right = False
            self.left = False
        if self.Floor:
            if teclado[K_SPACE]:
                self.Vel.y = -12
        
        self.Acc.x += self.Vel.x * (PLAYER_FRICTION)
        self.Vel.x += self.Acc.x
        self.Vel.y += self.Acc.y
        self.Pos += self.Vel + 0.5 * self.Acc
         
        self.rect.topleft = self.Pos + vec(23,8)

    def dibujar(self, screen):

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

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class colisiones:
    def __init__(self):
        pass
    def collide_player(self, player, target2):
        col_ = False
        hits = player.rect.colliderect(target2)
        if hits:
            col_=True
        return col_
    def check_distance(self, target1, target2):
        col_= False
        self.h1 = target1.rect.h
        self.w1 = target1.rect.w
        self.h2 = target2.rect.h
        self.w2 = target2.rect.w
        self.x1 =  target1.rect.center[0]
        self.y1 =  target1.rect.center[1]
        self.x2 =  target2.rect.center[0]
        self.y2 =  target2.rect.center[1]
        distance = ((self.x1-self.x2)**2 + (self.y1-self.y2)**2)**(1/2)
        max_distance = (((self.h1+self.h2)/2)**2 + ((self.w1+self.w2)/2)**2)**(1/2)
        if (abs(self.x1-self.x2) == (self.w1+self.w2)/2):
            if distance < max_distance and distance >0:
                col_ = True
        elif (abs(self.y1-self.y2) == (self.w1+self.w2)/2):
            if distance < max_distance and distance >0:
                col_ = True
        return col_
        #para cualquier objeto
    def distance_for_objects(self, target1, target2):
        col_= False
        self.h1 = target1.rect.h
        self.w1 = target1.rect.w
        self.h2 = target2.rect.h
        self.w2 = target2.rect.w
        self.x1 =  target1.rect.center[0]
        self.y1 =  target1.rect.center[1]
        self.x2 =  target2.rect.center[0]
        self.y2 =  target2.rect.center[1]
        distance = ((self.x1-self.x2)**2 + (self.y1-self.y2)**2)**(1/2)
        max_distance = (((self.h1+self.h2)/2)**2 + ((self.w1+self.w2)/2)**2)**(1/2)
        if (abs(self.x1-self.x2) == (self.w1+self.w2)/2):
            if distance < max_distance:
                col_ = True
        elif (abs(self.y1-self.y2) == (self.w1+self.w2)/2):
            if distance < max_distance:
                col_ = True

        return "colisiona: " + str(col_)+ " "+str((self.x1, self.y1)) +str((self.x2, self.y2)) + str(distance) +" "+ str(max_distance)