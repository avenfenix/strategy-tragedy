

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