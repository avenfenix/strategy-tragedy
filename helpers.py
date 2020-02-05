import pygame, sys
from pygame.locals import *

def get_image(filename, conv_alpha = True):
    try:
        image = pygame.image.load(filename)
    except pygame.error:
        raise SystemExit
    if conv_alpha:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image

def getCenter ( _image, position ):
    rect = _image.get_rect()
    rect.center = position
    return rect

def create_text(text, textFont, color, position,display):
    textSurf = textFont.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.center = position
    display.blit(textSurf, textRect)

class Button_color:
    def __init__(self, position, size, colorNormal, colorHover, text,textColor, font,  display):

        self.limits = [position[0] - size[0] /2, position[0] + size[0] / 2, position[1] - size[1] / 2, position[1] + size[1] / 2]

        self.surf = pygame.Surface(size)
        self.surf.fill(colorNormal)

        self.surfHover = pygame.Surface(size)
        self.surfHover.fill(colorHover)

        self.rect = pygame.Rect((0,0),size)
        self.display = display
        self.hover = False


        textSurf = font.render(text, True, (0,0,0))
        textRect = textSurf.get_rect()
        textRect.center = self.rect.center
        self.surf.blit(textSurf, textRect)

        self.rect.center = position

        self.surf.blit(textSurf,textRect)
        self.surfHover.blit(textSurf,textRect)

    def draw(self, mouse):

        if self.limits[0] <= mouse[0] <= self.limits[1] and self.limits[2] <= mouse[1] <= self.limits[3]:
            self.display.blit(self.surfHover,self.rect)
            self.hover = True
        else:
            self.display.blit(self.surf,self.rect)
            self.hover = False

    def is_clicked(self, event, action=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and action != None and self.hover:
                action()




class Button_image:
    def __init__(self, position, size, imageNormal, imageHover,  display):

        self.limits = [position[0] - size[0] /2, position[0] + size[0] / 2, position[1] - size[1] / 2, position[1] + size[1] / 2]

        self.surf = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.surf.blit(imageNormal,imageNormal.get_rect())

        self.surfHover = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.surfHover.blit(imageHover, imageNormal.get_rect())

        self.rect = pygame.Rect((0,0),size)
        self.display = display
        self.hover = False

        self.rect.center = position

    def draw(self, mouse):

        if self.limits[0] <= mouse[0] <= self.limits[1] and self.limits[2] <= mouse[1] <= self.limits[3]:
            self.display.blit(self.surfHover,self.rect)
            self.hover = True
        else:
            self.display.blit(self.surf,self.rect)
            self.hover = False

    def is_clicked(self, event, action=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and action != None and self.hover:
                action()


