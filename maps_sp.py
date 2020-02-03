import pygame, sys
from objects import *
from colors import *

class Maps_Sp:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((900, 700))
        pygame.display.set_caption("TEST")
        self.clock = pygame.time.Clock()
        self.running = True

    def load_map1(self):
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Personaje(100,200)
        self.all_sprites.add(self.player)
        p1 = Platform(0, 700 - 40, 900, 40)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        p2 = Platform(900 / 2 - 50, 700 * 3 / 4, 100, 20)
        self.all_sprites.add(p2)
        self.platforms.add(p2)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.Pos.y = hits[0].rect.top
            self.player.Vel.y = 0

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()
