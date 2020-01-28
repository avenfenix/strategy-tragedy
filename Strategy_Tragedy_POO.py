import pygame, sys
from pygame.locals import *

from Character_class import *

velocidad = 2

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Strategy Tragedy")
clock = pygame.time.Clock()



def create_text(text, textFont, color, posX, posY):
    textSurf = textFont.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.center = (posX, posY)
    gameDisplay.blit(textSurf,textRect)


def buttonMenu(text, w, h, x, y, colorNormal,colorHover,xText):
    mouse = pygame.mouse.get_pos()

    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(gameDisplay, colorNormal, (x, y, w, h))
    else:
        pygame.draw.rect(gameDisplay, colorHover, (x, y, w, h))

    create_text(text, smallText, (0,0,0), xText, y+(h/2))


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

        mouse = pygame.mouse.get_pos()

        # Parametros Botones
        buttonWidth = 150
        buttonHeight = 50
        PosXbuttonMenu = (display_width - buttonWidth) / 2

        # Button Single Player
        buttonMenu("Un Jugador",buttonWidth,buttonHeight, PosXbuttonMenu, 250, (0,0,0), (100,100,100), display_width/2)

        # Button Coop
        buttonMenu("Cooperativo", buttonWidth, buttonHeight, PosXbuttonMenu, 250+70*1, (0, 0, 0), (100, 100, 100), display_width / 2)

        # Button Programar
        buttonMenu("Programar", buttonWidth, buttonHeight, PosXbuttonMenu, 250+70*2, (0, 0, 0), (100, 100, 100), display_width / 2)

        # Button Exit
        buttonMenu("Salir", buttonWidth, buttonHeight, PosXbuttonMenu, 250+70*3, (0, 0, 0), (100, 100, 100), display_width / 2)


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

