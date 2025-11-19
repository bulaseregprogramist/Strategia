"""
Меню паузы в игре-стратегии
"""

import pygame
from src.anti_repeat import exit_game


pygame.init()


class StrategyPause:
    """
    Класс, отвечающий за меню паузы в игре.
    """

    def __init__(self, screen: pygame.surface.Surface):
        self.__screen = screen
        self.__font1 = pygame.font.Font("textures/font1.otf", 25)
        self.__text1 = self.__font1.render("ПАУЗА", 1, (255, 255, 255))
        self.run()

    def run(self) -> None:
        pause_cycle = 1
        
        while pause_cycle:
            self.__screen.blit(self.__text1, (50, 50))

            exit_game()
            pygame.display.flip()

