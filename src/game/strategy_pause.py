"""
Меню паузы в игре-стратегии
"""

import pygame


pygame.init()


class StrategyPause:
    """
    Класс, отвечающий за меню паузы в игре.
    """

    def __init__(self, screen: pygame.surface.Surface):
        self.run()

    def run(self) -> None:
        pause_cycle = 1
        
        while pause_cycle:
            pygame.display.flip()

