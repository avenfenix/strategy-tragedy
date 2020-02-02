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