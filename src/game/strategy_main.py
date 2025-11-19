"""
Главный файл игры-стратегии
"""

import pygame


pygame.init()


class StrategyMain:
    """
    Главный класс игры-стратегии
    """

    def __init__(self):
        self.__play_music()
        self.__run()

    def __play_music(self) -> None:
        """
        Проигрывание музыки в игре
        """
        music = pygame.mixer.Sound('textures/in_game.mp3')
        music.play(-1)

    def __run(self):
        """Основной метод класса."""
        pass

