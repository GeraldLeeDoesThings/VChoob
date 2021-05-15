import sys
import pygame

from pygame import display
from pygame import event as events

import constants as c
import gamevars as vars
import objects

pygame.init()

size = width, height = 1920, 1080

screen = display.set_mode(size)

while True:

    for event in events.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

