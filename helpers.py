import pygame, sys
from pygame.locals import *

def get_image(filename, transparent=False, conv=False):
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

def getCenter ( _image, position ):
    rect = _image.get_rect()
    rect.center = position
    return rect