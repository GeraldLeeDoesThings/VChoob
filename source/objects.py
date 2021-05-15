import pygame
import constants as c
import gamevars as vars


class Drawable:

    def draw(self):
        pass


class CanTrigger:

    def check_if_triggered(self):
        pass

    def trigger(self, **kwargs):
        pass


class Button(Drawable, CanTrigger):

    def __init__(self, x, y, width, height, screen: pygame.Surface, sprite: str = "", text: str = ""):
        # TODO: Implement this whole class
        pass

    def draw(self):
        pass