"""
Функции игры, которые используются много раз
(Во избежание повторов в коде)
"""

import pygame
import sys


pygame.init()


def exit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
