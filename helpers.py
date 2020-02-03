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

    def __init__(self, position, size, colorNormal, colorHover, text,font,textColor,  display):
        self.leftLimit = position[0] - size[0] /2
        self.rightLimit = position[0] + size[0] / 2
        self.upperLimit = position[1] - size[1] / 2
        self.lowerLimit = position[1] + size[1] / 2
        self.surf = pygame.Surface(size)
        self.surf.fill(colorNormal)
        self.surfHover = pygame.Surface(size)
        self.surfHover.fill(colorHover)
        self.rect = pygame.Rect((0,0),size)
        self.rect.center = position
        self.display = display
        self.hover = False
        create_text(text, font, textColor, position,display)


    def draw(self, mouse):
        if self.leftLimit <= mouse[0] <= self.rightLimit and self.upperLimit <= mouse[1] <= self.lowerLimit:
            self.display.blit(self.surfHover,self.rect)
            self.hover = True
        else:
            self.display.blit(self.surf,self.rect)
            self.hover = False

    def is_clicked(self, event, action=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and action != None and self.hover:
                action()


