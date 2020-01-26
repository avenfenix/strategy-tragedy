import pygame, sys
from pygame.locals import *

velocidad = 2

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Strategy Tragedy")
clock = pygame.time.Clock()


class Personaje:
    ### Sprites caminar derecha
    xixf = {}
    xixf[0] = (0, 0, 26, 100)
    xixf[1] = (27, 0, 31, 100)
    xixf[2] = (61, 0, 24, 100)
    xixf[3] = (87, 0, 33, 100)

    ### Sprites Caminar izquierda
    Rxixf = {}
    Rxixf[0] = (97, 0, 23, 100)
    Rxixf[1] = (60, 0, 35, 100)
    Rxixf[2] = (37, 0, 23, 100)
    Rxixf[3] = (0, 0, 33, 100)

    def __init__(self, PosX, PosY):
        self.PosX = PosX
        self.PosY = PosY
        self.cont = 4
        self.drawed = self.get_image("personaje/personaje_sprite.png", True)
        self.draw_inv = pygame.transform.flip(self.drawed, True, False)
        self.isJumping = False
        self.JumpCount = 10
        self.direc = True
        self.i = 0

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
        if teclado[K_RIGHT] and self.PosX <= Width - 30 - velocidad:
            self.PosX += velocidad
            self.cont += 1
            self.direc = True

        if teclado[K_LEFT] and self.PosX >= 0 + velocidad:
            self.PosX -= velocidad
            self.cont += 1
            self.direc = False

        if not (self.isJumping):
            if teclado[K_UP] and self.PosY >= 0 + velocidad:
                self.PosY -= velocidad
            if teclado[K_DOWN] and self.PosY <= Height - 100 - velocidad:
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
        if self.direc:
            screen.blit(self.drawed, (self.PosX, self.PosY), (self.xixf[self.i]))
        if not self.direc:
            screen.blit(self.draw_inv, (self.PosX, self.PosY), (self.Rxixf[self.i]))

    def anim(self):

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


def text_block(text, textFont, color):
    textSurf = textFont.render(text, True, color)
    textRect = textSurf.get_rect()

    return textSurf, textRect


def game_menu():
    menu = True

    while menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                menu = False
                quit()

        # Crear y posicionar Titulo
        textSurf, textRect = text_block("Strategy Tragedy", Title, (0, 0, 0))
        textRect.center = ((display_width / 2), (display_height / 4))

        # Dibujar fondo y renderizar el Titulo
        gameDisplay.fill((255, 255, 255))
        gameDisplay.blit(textSurf, textRect)

        # Parametros Botones y Posicion del Mouse
        buttonWidth = 150
        buttonHeight = 50
        mouse = pygame.mouse.get_pos()

        # Button Single Player
        if (display_width - buttonWidth) / 2 < mouse[0] < (display_width + buttonWidth) / 2 and 250 < mouse[
            1] < 250 + buttonHeight:
            pygame.draw.rect(gameDisplay, (100, 200, 100),
                             ((display_width - buttonWidth) / 2, 250, buttonWidth, buttonHeight))
        else:
            pygame.draw.rect(gameDisplay, (0, 255, 0),
                             ((display_width - buttonWidth) / 2, 250, buttonWidth, buttonHeight))

        textSurf, textRect = text_block("Un jugador", smallText, (0, 0, 0))
        textRect.center = ((display_width / 2), 250 + buttonHeight / 2)
        gameDisplay.blit(textSurf, textRect)

        # Button Coop
        if (display_width - buttonWidth) / 2 < mouse[0] < (display_width + buttonWidth) / 2 and 320 < mouse[
            1] < 320 + buttonHeight:
            pygame.draw.rect(gameDisplay, (100, 100, 200),
                             ((display_width - buttonWidth) / 2, 320, buttonWidth, buttonHeight))
        else:
            pygame.draw.rect(gameDisplay, (0, 0, 255),
                             ((display_width - buttonWidth) / 2, 320, buttonWidth, buttonHeight))

        textSurf, textRect = text_block("Cooperativo", smallText, (0, 0, 0))
        textRect.center = ((display_width / 2), 320 + buttonHeight / 2)
        gameDisplay.blit(textSurf, textRect)

        # Button Program
        if (display_width - buttonWidth) / 2 < mouse[0] < (display_width + buttonWidth) / 2 and 390 < mouse[
            1] < 390 + buttonHeight:
            pygame.draw.rect(gameDisplay, (155, 155, 155),
                             ((display_width - buttonWidth) / 2, 390, buttonWidth, buttonHeight))
        else:
            pygame.draw.rect(gameDisplay, (200, 200, 200),
                             ((display_width - buttonWidth) / 2, 390, buttonWidth, buttonHeight))

        textSurf, textRect = text_block("Aprende a \n Programar", smallText, (0, 0, 0))
        textRect.center = ((display_width / 2), 380 + buttonHeight / 2)
        gameDisplay.blit(textSurf, textRect)

        # Button Exit
        if (display_width - buttonWidth) / 2 < mouse[0] < (display_width + buttonWidth) / 2 and 460 < mouse[
            1] < 460 + buttonHeight:
            pygame.draw.rect(gameDisplay, (200, 100, 100),
                             ((display_width - buttonWidth) / 2, 460, buttonWidth, buttonHeight))
        else:
            pygame.draw.rect(gameDisplay, (255, 0, 0),
                             ((display_width - buttonWidth) / 2, 460, buttonWidth, buttonHeight))

        textSurf, textRect = text_block("Salir", smallText, (0, 0, 0))
        textRect.center = ((display_width / 2), 460 + buttonHeight / 2)
        gameDisplay.blit(textSurf, textRect)

        # Actualizacion pantalla
        pygame.display.update()
        clock.tick(15)


def main():
    myfont = pygame.font.SysFont('Comic Sans MS', 28)

    screen = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("Strategy Tragedy")
    clock = pygame.time.Clock()
    Charac = Personaje(10, 500)
    run = True
    while run:
        time = clock.tick(60)
        Charac.anim()
        Charac.teclado()
        screen.fill((255, 255, 255))
        Charac.movimiento(screen)
        textsurface = myfont.render("Pos: " + str(Charac.PosX) + "-" + str(Charac.PosY) + " Vel: " + str(velocidad),
                                    False, (0, 0, 0))
        screen.blit(textsurface, (0, 0))
        print("ASDTEST")
        for evento in pygame.event.get():
            if evento.type == QUIT:
                run = False

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    pygame.init()

    # Inicializar Fuentes
    Title = pygame.font.SysFont('Comic Sans MS', 56)
    smallText = pygame.font.SysFont('Comic Sans MS', 23)

    # Menu inicial
    game_menu()

