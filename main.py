from objects import *
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

        #Inicializar Botones
        self.Button_SinglePlayer = Button_image( (display_width/2, (display_height) / 2 + 10), (200,80), self.image_button_SP, self.image_button_SPhover, gameDisplay )
        self.Button_Coop = Button_image( (display_width/2, (display_height) / 2 + 110), (200,80), self.image_button_Coop, self.image_button_Coophover, gameDisplay )
        self.Button_Progra = Button_image( (display_width/2, (display_height) / 2 + 210), (200,80), self.image_button_Prog, self.image_button_Proghover, gameDisplay )
        self.Button_Exit = Button_image( (display_width - 50, (display_height) - 50), (80,80), self.image_button_Exit, self.image_button_Exithover, gameDisplay )

        self.selector = False


    #Crear y Posicionar Texto



    # Generar boton de color con texto

    def buttonMenu_color(self, text, w, h, x, y, colorNormal, colorHover, action=None):

        mouse = pygame.mouse.get_pos()

        rect1 = pygame.Rect (x,y,w,h)

        rect1.center = (x,y)

        if x - w / 2 < mouse[0] < x + w / 2 and y - h / 2 < mouse[1] < y + h / 2:
            pygame.draw.rect(gameDisplay, colorHover, rect1)
            if action != None:
                action()
            else:
                pygame.draw.rect(gameDisplay, colorNormal, rect1)

        self.create_text( text, smallText, BLACK, (x,y))


    # Funcion general para generar botones con fondo de imagen
    def buttonMenu_image (self, w,h,x,y, imageNormal,imageHover, action = None):
        mouse = pygame.mouse.get_pos()

        temp = getCenter(imageNormal, (x,y))

        if x - w / 2 < mouse[0] < x + w / 2 and y - h / 2 < mouse[1] < y + h / 2:
            gameDisplay.blit(imageHover, temp)
            for event in pygame.event.get():

                if action != None:
                    action()
        else:
            gameDisplay.blit(imageNormal, temp)



    def Menu(self):

        menu = True

        gameDisplay.blit(self.image_Background, (0, 0))

        while menu:
            pygame.display.update()
            clock.tick(30)
            mouse = pygame.mouse.get_pos()
            gameDisplay.blit(self.image_Title, getCenter(self.image_Title, (display_width / 2, display_height / 4)))

            for event in pygame.event.get():

                #Acciones de los botones al ser clickeados
                self.Button_SinglePlayer.is_clicked(event, main)
                self.Button_Coop.is_clicked(event)
                self.Button_Progra.is_clicked(event)
                self.Button_Exit.is_clicked(event,Quit)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    menu = False
                    quit()



            # Dibujar botones
            self.Button_SinglePlayer.draw(mouse)
            self.Button_Coop.draw(mouse)
            self.Button_Progra.draw(mouse)
            self.Button_Exit.draw(mouse)


    def Select_LevelSP (self):

        self.selector = True
        gameDisplay.blit(self.image_Background, (0, 0))
        self.create_text("Selecciona un Nivel - Single Player", Title, WHITE, (display_width/2, 50))

        separation = 150
        cont = -2

        while self.selector:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    selector = False
                    quit()

            #self.buttonMenu_color("1",100,100, display_width/2 + separation * (-2),250, WHITE, LIGHTGRAY, main)
            #self.buttonMenu_color("2",100,100, display_width/2 + separation * (-1),250, GRAY, BLACK)
            #self.buttonMenu_color("3",100,100, display_width/2 + separation * (0),250, GRAY, BLACK)
            #self.buttonMenu_color("4",100,100, display_width/2 + separation * (1),250, GRAY, BLACK)
            #self.buttonMenu_color("5",100,100, display_width/2 + separation * (2),250, GRAY, BLACK)

            #self.buttonMenu_color("6", 100, 100, display_width / 2 + separation * (-2), 400, GRAY, BLACK)
            #self.buttonMenu_color("7", 100, 100, display_width / 2 + separation * (-1), 400, GRAY, BLACK)
            #self.buttonMenu_color("8", 100, 100, display_width / 2 + separation * (0), 400, GRAY, BLACK,self.back)
            #self.buttonMenu_color("9", 100, 100, display_width / 2 + separation * (1), 400, GRAY, BLACK)
            #self.buttonMenu_color("10", 100, 100, display_width / 2 + separation * (2), 400, GRAY, BLACK)


            #self.buttonMenu_color("Volver", 70, 70, display_width - 120, display_height - 150, RED, (150, 0, 0),self.back)

            # Actualizacion pantalla
            pygame.display.update()
            clock.tick(30)

    def back (self):
        self.selector = False
        print ("xd")



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
    #Maps = Maps_Sp()

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
