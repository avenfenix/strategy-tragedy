import pygame, sys
from pygame.locals import *
from Character_class import Personaje
from colors import *

display_width = 900
display_height = 700
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Strategy Tragedy")
clock = pygame.time.Clock()

velocidad = 2

def create_text(text, textFont, color, posX, posY):
    textSurf = textFont.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.center = (posX, posY)
    gameDisplay.blit(textSurf,textRect)


class GameMenu:

    def __init__(self, ):
        self.image_Background = self.get_image("Graphics\Menu\Background_test.png")
        self.image_Title = self.get_image("Graphics\Menu\Title.png")
        self.image_button_SP = self.get_image("Graphics\Menu\SP_text.png")
        self.image_button_SPhover = self.get_image("Graphics\Menu\SP_Hover_text.png")
        self.image_button_Coop = self.get_image("Graphics\Menu\Coop_text.png")
        self.image_button_Coophover = self.get_image("Graphics\Menu\Coop_Hover_text.png")
        self.image_button_Prog = self.get_image("Graphics\Menu\Prog_text.png")
        self.image_button_Proghover = self.get_image("Graphics\Menu\Prog_Hover_text.png")
        self.image_button_Exit = self.get_image("Graphics\Menu\Exit_text.png")
        self.image_button_Exithover = self.get_image("Graphics\Menu\Exit_Hover_text.png")

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

def buttonMenu(text, w, h, x, y, imageNormal,imageHover,xText, action = None):
    mouse = pygame.mouse.get_pos()

    imgNormal = pygame.image.load(imageNormal)
    imgHover = pygame.image.load(imageHover)
    rect = imgNormal.get_rect()
    rect.center = (x,y)
    click = pygame.mouse.get_pressed()
    if x - w/2 < mouse[0] < x + w/2 and y - h/2 < mouse[1] < y + h/2:
        gameDisplay.blit( imgHover, rect)
        if click[0] == 1 and action != None:
            action()


    else:
        gameDisplay.blit( imgNormal, rect)

    create_text(text, smallText, WHITE, xText, y)


def Single_Player():
    print("Hola")

def Coop ():
    print("Hola")


def Program ():
    print("Hola")


def Quit():
    pygame.quit()
    quit()


def game_menu():

    menu = True

    background = pygame.image.load("Graphics\Menu\Background_test.png")
    gameDisplay.blit(background,(0,0))
    while menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                menu = False
                quit()

        # Dibujar fondo

        # Crear y posicionar Titulo
        Title_image = pygame.image.load("Graphics/Menu/Title.png")
        rect = Title_image.get_rect()
        rect.center = (display_width/2, display_height / 4)
        gameDisplay.blit(Title_image,rect)

        # Parametros Botones
        buttonWidth = 200
        buttonHeight = 80
        PosXbuttonMenu = (display_width ) / 2
        YbuttonMenu = (display_height) / 2 + 10
        separation = 100

        # Button Single Player
        buttonMenu("",buttonWidth,buttonHeight, PosXbuttonMenu, YbuttonMenu, "Graphics\Menu\SP_text.png", "Graphics\Menu\SP_Hover_text.png", display_width/2, main)

        # Button Coop
        buttonMenu("", buttonWidth, buttonHeight, PosXbuttonMenu, YbuttonMenu + separation, "Graphics\Menu\Coop_text.png", "Graphics\Menu\Coop_Hover_text.png", display_width / 2, Coop)

        # Button Programar
        buttonMenu("", buttonWidth, buttonHeight, PosXbuttonMenu, YbuttonMenu + separation*2, "Graphics\Menu\Prog_text.png", "Graphics\Menu\Prog_Hover_text.png", display_width / 2, Program)

        # Button Exit
        buttonMenu("", buttonWidth, buttonHeight, display_width -60, display_height - 60, "Graphics\Menu\Exit_text.png", "Graphics\Menu\Exit_Hover_text.png", display_width -60, Quit)

        # Actualizacion pantalla
        pygame.display.update()
        clock.tick(30)





def main():
    myfont = pygame.font.SysFont('Comic Sans MS', 28)

    Charac = Personaje(10, 466)
    run = True
    while run:
        time = clock.tick(75)
        Charac.teclado()
        gameDisplay.fill((255, 255, 255))
        Charac.movimiento(gameDisplay)
        textsurface = myfont.render("Pos: " + str(Charac.PosX) + "-" + str(Charac.PosY) + " Vel: " + str(velocidad),
                                    False, (0, 0, 0))
        gameDisplay.blit(textsurface, (0, 0))

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

