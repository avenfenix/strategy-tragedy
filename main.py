from objects import *
from maps_sp import *
from helpers import *
# Se importan todas las clases necesarias en Chracter_class y helpers



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

        self.selector = False

    def Menu(self):

        Button_SinglePlayer = Button_image((display_width / 2, (display_height) / 2 + 10), (200, 80), self.image_button_SP, self.image_button_SPhover, gameDisplay)
        Button_Coop = Button_image((display_width / 2, (display_height) / 2 + 110), (200, 80), self.image_button_Coop, self.image_button_Coophover, gameDisplay)
        Button_Progra = Button_image((display_width / 2, (display_height) / 2 + 210), (200, 80), self.image_button_Prog, self.image_button_Proghover, gameDisplay)
        Button_Exit = Button_image((display_width - 50, (display_height) - 50), (80, 80), self.image_button_Exit, self.image_button_Exithover, gameDisplay)


        menu = True
        while menu:

            pygame.display.update()
            clock.tick(30)
            gameDisplay.blit(self.image_Background, (0, 0))

            mouse = pygame.mouse.get_pos()
            gameDisplay.blit(self.image_Title, getCenter(self.image_Title, (display_width / 2, display_height / 4)))

            for event in pygame.event.get():

                #Acciones de los botones al ser clickeados
                Button_SinglePlayer.is_clicked(event, self.Select_LevelSP)
                Button_Coop.is_clicked(event, self.Select_LevelCOOP)
                Button_Progra.is_clicked(event, self.Select_LevelPROGRA)
                Button_Exit.is_clicked(event,Quit)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    menu = False
                    quit()

            # Dibujar botones
            Button_SinglePlayer.draw(mouse)
            Button_Coop.draw(mouse)
            Button_Progra.draw(mouse)
            Button_Exit.draw(mouse)


    def Select_LevelSP (self):

        self.selector = True
        gameDisplay.blit(self.image_Background, (0, 0))
        create_text("Selecciona un Nivel - Single Player", Title, WHITE, (display_width/2, 50),gameDisplay)

        separation = 150

        N1 = Button_color((display_width / 2 + separation * (-2), 250), (100, 100), WHITE, LIGHTGRAY, "1", BLACK, smallText,gameDisplay)
        N2 = Button_color((display_width / 2 + separation * (-1), 250), (100, 100), GRAY, BLACK, "2", BLACK, smallText,gameDisplay)
        N3 = Button_color((display_width / 2 + separation * (0), 250), (100, 100), GRAY, BLACK, "3", BLACK, smallText,gameDisplay)
        N4 = Button_color((display_width / 2 + separation * (1), 250), (100, 100), GRAY, BLACK, "4", BLACK, smallText,gameDisplay)
        N5 = Button_color((display_width / 2 + separation * (2), 250), (100, 100), GRAY, BLACK, "5", BLACK, smallText,gameDisplay)

        N6 = Button_color((display_width / 2 + separation * (-2), 400), (100, 100), GRAY, BLACK, "6", BLACK, smallText,gameDisplay)
        N7 = Button_color((display_width / 2 + separation * (-1), 400), (100, 100), GRAY, BLACK, "7", BLACK, smallText,gameDisplay)
        N8 = Button_color((display_width / 2 + separation * (0), 400), (100, 100), GRAY, BLACK, "8", BLACK, smallText,gameDisplay)
        N9 = Button_color((display_width / 2 + separation * (1), 400), (100, 100), GRAY, BLACK, "9", BLACK, smallText,gameDisplay)
        N10 = Button_color((display_width / 2 + separation * (2), 400), (100, 100), GRAY, BLACK, "10", BLACK, smallText,gameDisplay)

        BACK = Button_color((display_width - 50, display_height - 50), (70, 70), RED, (100, 0, 0), "Volver", BLACK, smallText,gameDisplay)

        while self.selector:

            for event in pygame.event.get():

                N1.is_clicked(event, self.main)
                N2.is_clicked(event)
                N3.is_clicked(event)
                N4.is_clicked(event)
                N5.is_clicked(event)
                N6.is_clicked(event)
                N7.is_clicked(event)
                N8.is_clicked(event)
                N9.is_clicked(event)
                N10.is_clicked(event)
                BACK.is_clicked(event, self.back)


                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            mouse = pygame.mouse.get_pos()

            #DRAW

            N1.draw(mouse)
            N2.draw(mouse)
            N3.draw(mouse)
            N4.draw(mouse)
            N5.draw(mouse)
            N6.draw(mouse)
            N7.draw(mouse)
            N8.draw(mouse)
            N9.draw(mouse)
            N10.draw(mouse)
            BACK.draw(mouse)

            # Actualizacion pantalla
            pygame.display.update()
            clock.tick(30)

    def Select_LevelCOOP (self):

        self.selector = True
        gameDisplay.blit(self.image_Background, (0, 0))
        create_text("Selecciona un Nivel - Cooperativo", Title, WHITE, (display_width/2, 50),gameDisplay)

        separation = 150

        N1 = Button_color((display_width / 2 + separation * (-2), 250), (100, 100), GRAY, BLACK, "1", BLACK, smallText,gameDisplay)
        N2 = Button_color((display_width / 2 + separation * (-1), 250), (100, 100), GRAY, BLACK, "2", BLACK, smallText,gameDisplay)
        N3 = Button_color((display_width / 2 + separation * (0), 250), (100, 100), GRAY, BLACK, "3", BLACK, smallText,gameDisplay)
        N4 = Button_color((display_width / 2 + separation * (1), 250), (100, 100), GRAY, BLACK, "4", BLACK, smallText,gameDisplay)
        N5 = Button_color((display_width / 2 + separation * (2), 250), (100, 100), GRAY, BLACK, "5", BLACK, smallText,gameDisplay)

        N6 = Button_color((display_width / 2 + separation * (-2), 400), (100, 100), GRAY, BLACK, "6", BLACK, smallText,gameDisplay)
        N7 = Button_color((display_width / 2 + separation * (-1), 400), (100, 100), GRAY, BLACK, "7", BLACK, smallText,gameDisplay)
        N8 = Button_color((display_width / 2 + separation * (0), 400), (100, 100), GRAY, BLACK, "8", BLACK, smallText,gameDisplay)
        N9 = Button_color((display_width / 2 + separation * (1), 400), (100, 100), GRAY, BLACK, "9", BLACK, smallText,gameDisplay)
        N10 = Button_color((display_width / 2 + separation * (2), 400), (100, 100), GRAY, BLACK, "10", BLACK, smallText,gameDisplay)

        BACK = Button_color((display_width - 50, display_height - 50), (70, 70), RED, (100, 0, 0), "Volver", BLACK, smallText,gameDisplay)

        while self.selector:

            for event in pygame.event.get():

                N1.is_clicked(event)
                N2.is_clicked(event)
                N3.is_clicked(event)
                N4.is_clicked(event)
                N5.is_clicked(event)
                N6.is_clicked(event)
                N7.is_clicked(event)
                N8.is_clicked(event)
                N9.is_clicked(event)
                N10.is_clicked(event)
                BACK.is_clicked(event, self.back)


                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            mouse = pygame.mouse.get_pos()

            #DRAW

            N1.draw(mouse)
            N2.draw(mouse)
            N3.draw(mouse)
            N4.draw(mouse)
            N5.draw(mouse)
            N6.draw(mouse)
            N7.draw(mouse)
            N8.draw(mouse)
            N9.draw(mouse)
            N10.draw(mouse)
            BACK.draw(mouse)

            # Actualizacion pantalla
            pygame.display.update()
            clock.tick(30)

    def Select_LevelPROGRA (self):

        self.selector = True
        gameDisplay.blit(self.image_Background, (0, 0))
        create_text("Selecciona un Nivel - Programar", Title, WHITE, (display_width/2, 50),gameDisplay)

        separation = 150

        N1 = Button_color((display_width / 2 + separation * (-2), 250), (100, 100), GRAY, BLACK, "1", BLACK, smallText,gameDisplay)
        N2 = Button_color((display_width / 2 + separation * (-1), 250), (100, 100), GRAY, BLACK, "2", BLACK, smallText,gameDisplay)
        N3 = Button_color((display_width / 2 + separation * (0), 250), (100, 100), GRAY, BLACK, "3", BLACK, smallText,gameDisplay)
        N4 = Button_color((display_width / 2 + separation * (1), 250), (100, 100), GRAY, BLACK, "4", BLACK, smallText,gameDisplay)
        N5 = Button_color((display_width / 2 + separation * (2), 250), (100, 100), GRAY, BLACK, "5", BLACK, smallText,gameDisplay)

        N6 = Button_color((display_width / 2 + separation * (-2), 400), (100, 100), GRAY, BLACK, "6", BLACK, smallText,gameDisplay)
        N7 = Button_color((display_width / 2 + separation * (-1), 400), (100, 100), GRAY, BLACK, "7", BLACK, smallText,gameDisplay)
        N8 = Button_color((display_width / 2 + separation * (0), 400), (100, 100), GRAY, BLACK, "8", BLACK, smallText,gameDisplay)
        N9 = Button_color((display_width / 2 + separation * (1), 400), (100, 100), GRAY, BLACK, "9", BLACK, smallText,gameDisplay)
        N10 = Button_color((display_width / 2 + separation * (2), 400), (100, 100), GRAY, BLACK, "10", BLACK, smallText,gameDisplay)

        BACK = Button_color((display_width - 50, display_height - 50), (70, 70), RED, (100, 0, 0), "Volver", BLACK, smallText,gameDisplay)

        while self.selector:

            for event in pygame.event.get():

                N1.is_clicked(event)
                N2.is_clicked(event)
                N3.is_clicked(event)
                N4.is_clicked(event)
                N5.is_clicked(event)
                N6.is_clicked(event)
                N7.is_clicked(event)
                N8.is_clicked(event)
                N9.is_clicked(event)
                N10.is_clicked(event)
                BACK.is_clicked(event, self.back)


                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            mouse = pygame.mouse.get_pos()

            #DRAW

            N1.draw(mouse)
            N2.draw(mouse)
            N3.draw(mouse)
            N4.draw(mouse)
            N5.draw(mouse)
            N6.draw(mouse)
            N7.draw(mouse)
            N8.draw(mouse)
            N9.draw(mouse)
            N10.draw(mouse)
            BACK.draw(mouse)

            # Actualizacion pantalla
            pygame.display.update()
            clock.tick(30)

    def back (self):
        self.selector = False

    def main(self):
        myfont = pygame.font.SysFont('Comic Sans MS', 28)
        # Maps = Maps_Sp()

        Background_test = get_image("Graphics\SP\Background.png", False)
        # Maps.load_map1()

        Charac = Personaje(0, 466)
        Cuadrado = Platform(100, 600, 100, 100)
        crearColision = colisiones()
        self.run = True
        while self.run:
            time = clock.tick(75)
            Charac.teclado()
            gameDisplay.blit(Background_test, (0, 0))
            Cuadrado.draw(gameDisplay)
            check = crearColision.distance_for_player(Charac, Cuadrado)
            # distance = crearColision.distance_for_objects(Charac,Cuadrado)
            colision = crearColision.collide_player(Charac, Cuadrado)
            print(colision)
            Charac.movimiento(gameDisplay)
            textsurface = myfont.render(
                "Pos: " + str(Charac.Pos.x) + "-" + str(Charac.Pos.y) + " Vel: " + str(velocidad), False, WHITE)
            gameDisplay.blit(textsurface, (0, 0))

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_p:
                        self.pause = True
                        self.Pause()

                if evento.type == QUIT:
                    self.run = False

            pygame.display.update()

    # helpers(?)
    def Pause(self):
        create_text("Pausa", Title, WHITE, (900 / 2, 50), gameDisplay)
        smallPauseText = pygame.font.SysFont('Comic Sans MS', 23)

        CONTINUE = Button_color((display_width / 2, 50), (200, 80), WHITE, WHITE, "Continuar", BLACK, smallPauseText,gameDisplay)
        QUIT = Button_color((display_width / 2, 150), (200, 80), WHITE, GRAY, "Salir", BLACK, smallPauseText,gameDisplay)

        while self.pause:
            for event in pygame.event.get():

                CONTINUE.is_clicked(event,self.continuegame)
                QUIT.is_clicked(event, self.back_mainmenu)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            mouse = pygame.mouse.get_pos()
            # gameDisplay.fill(white)
            CONTINUE.draw(mouse)
            QUIT.draw(mouse)

            pygame.display.update()
            clock.tick(15)

    def continuegame (self):
        self.pause = False

    def back_mainmenu(self):
        self.pause = False
        self.run = False
        self.selector = False


def Single_Player():
    print("Hola")

def Coop ():
    print("Hola")


def Program ():
    print("Hola")


def Quit():
    pygame.quit()
    quit()







if __name__ == "__main__":
    pygame.init()

    # Inicializar Fuentes
    Title = pygame.font.SysFont('Comic Sans MS', 56)
    smallText = pygame.font.SysFont('Comic Sans MS', 23)

    # Menu inicial
    START = Game()
    START.Menu()
