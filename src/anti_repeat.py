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


def load_texture(filename: str,
                size: tuple[int, int]) -> pygame.surface.Surface:
    """
    Загрузка текстур
    
    Args:
        filename (str): Путь к файлу
        size (tuple[int, int]): Размер текстуры в игре
    Returns:
        pygame.surface.Surface: Загруженная в игру текстура.
    """
    texture = pygame.transform.scale(
        pygame.image.load(filename).convert_alpha(), size)
    return texture

