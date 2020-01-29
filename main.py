import pygame, sys
from pygame.locals import *
from Character_class import Personaje

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Strategy Tragedy")
clock = pygame.time.Clock()

velocidad = 2

def create_text(text, textFont, color, posX, posY):
    textSurf = textFont.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.center = (posX, posY)
    gameDisplay.blit(textSurf,textRect)


def buttonMenu(text, w, h, x, y, colorNormal,colorHover,xText, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(gameDisplay, colorHover, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()


    else:
        pygame.draw.rect(gameDisplay, colorNormal, (x, y, w, h))

    create_text(text, smallText, (0,0,0), xText, y+(h/2))


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

    while menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                menu = False
                quit()

        # Dibujar fondo
        gameDisplay.fill((255, 255, 255))

        # Crear y posicionar Titulo
        create_text("Strategy Tragedy", Title, (0,0,0), display_width/2, display_height/4)

        # Parametros Botones
        buttonWidth = 150
        buttonHeight = 50
        PosXbuttonMenu = (display_width - buttonWidth) / 2

        # Button Single Player
        buttonMenu("Un Jugador",buttonWidth,buttonHeight, PosXbuttonMenu, 250, (0,255,0), (0,100,0), display_width/2, main)

        # Button Coop
        buttonMenu("Cooperativo", buttonWidth, buttonHeight, PosXbuttonMenu, 250+70*1, (0, 0, 255), (0, 0, 100), display_width / 2, Coop)

        # Button Programar
        buttonMenu("Programar", buttonWidth, buttonHeight, PosXbuttonMenu, 250+70*2, (255, 155, 0), (150, 90, 0), display_width / 2, Program)

        # Button Exit
        buttonMenu("Salir", buttonWidth, buttonHeight, PosXbuttonMenu, 250+70*3, (255, 0, 0), (100, 0, 0 ), display_width / 2, Quit)

        # Actualizacion pantalla
        pygame.display.update()
        clock.tick(15)





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

