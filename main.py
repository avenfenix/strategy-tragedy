from Character_class import *
from maps_sp import *
from helpers import *
# Se importan todas las clases necesarias en Chracter_class y helpers

display_width = 900
display_height = 700
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Strategy Tragedy")
clock = pygame.time.Clock()

velocidad = 2

class Game:

    def __init__(self, ):

        # Cargar imagenes del Menu
        self.image_Background = get_image("Graphics\Menu\Background_test.png", False)
        self.image_Title = get_image("Graphics\Menu\Title.png")
        self.image_button_SP = get_image("Graphics\Menu\SP_text.png")
        self.image_button_SPhover = get_image("Graphics\Menu\SP_Hover_text.png")
        self.image_button_Coop = get_image("Graphics\Menu\Coop_text.png")
        self.image_button_Coophover = get_image("Graphics\Menu\Coop_Hover_text.png")
        self.image_button_Prog = get_image("Graphics\Menu\Prog_text.png")
        self.image_button_Proghover = get_image("Graphics\Menu\Prog_Hover_text.png")
        self.image_button_Exit = get_image("Graphics\Menu\Exit_text.png")
        self.image_button_Exithover = get_image("Graphics\Menu\Exit_Hover_text.png")


    # Funcion general para generar botones
    def buttonMenu (self, w,h,x,y, imageNormal,imageHover, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        temp = getCenter (imageNormal, (x,y))

        if x - w / 2 < mouse[0] < x + w / 2 and y - h / 2 < mouse[1] < y + h / 2:
            gameDisplay.blit(imageHover, temp )
            if click[0] == 1 and action != None:
                action()
        else:
            gameDisplay.blit(imageNormal, temp)



    def Menu(self):

        menu = True

        gameDisplay.blit(self.image_Background, (0, 0))
        gameDisplay.blit(self.image_Title, getCenter(self.image_Title, (display_width / 2, display_height / 4)))

        buttonWidth = 200
        buttonHeight = 80
        PosXbuttonMenu = (display_width) / 2
        YbuttonMenu = (display_height) / 2 + 10
        separation = 100

        while menu:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    menu = False
                    quit()

            # Button Single Player
            self.buttonMenu(buttonWidth, buttonHeight, PosXbuttonMenu, YbuttonMenu, self.image_button_SP,self.image_button_SPhover,  main)

            # Button Coop
            self.buttonMenu(buttonWidth, buttonHeight, PosXbuttonMenu, YbuttonMenu + separation,self.image_button_Coop,self.image_button_Coophover, Coop)

            # Button Programar
            self.buttonMenu(buttonWidth, buttonHeight, PosXbuttonMenu, YbuttonMenu + separation * 2, self.image_button_Prog, self.image_button_Proghover, Program)

            # Button Exit
            self.buttonMenu(80, 80, display_width - 60, display_height - 60, self.image_button_Exit, self.image_button_Exithover, Quit)

            # Actualizacion pantalla
            pygame.display.update()
            clock.tick(30)

def Single_Player():
    print("Hola")

def Coop ():
    print("Hola")


def Program ():
    print("Hola")


def Quit():
    pygame.quit()
    quit()




def main():
    myfont = pygame.font.SysFont('Comic Sans MS', 28)
    Maps = Maps_Sp()

    Background_test = get_image("Graphics\SP\Background.png", False)
    #Maps.load_map1()

    Charac = Personaje(10, 466)
    Plataforma = Platform (0,700,900,20)
    run = True
    while run:
        time = clock.tick(75)
        Charac.teclado()
        gameDisplay.blit(Background_test, (0, 0))

        Charac.movimiento(gameDisplay)
        textsurface = myfont.render("Pos: " + str(Charac.Pos.x) + "-" + str(Charac.Pos.y) + " Vel: " + str(velocidad),False, WHITE)
        gameDisplay.blit(textsurface, (0, 0))

        for evento in pygame.event.get():
            if evento.type == QUIT:
                run = False

        pygame.display.update()
    Quit()


if __name__ == "__main__":
    pygame.init()

    # Inicializar Fuentes
    Title = pygame.font.SysFont('Comic Sans MS', 56)
    smallText = pygame.font.SysFont('Comic Sans MS', 23)

    # Menu inicial
    START = Game()
    START.Menu()
