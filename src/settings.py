"""
Настройки игры
"""

import pygame


pygame.init()


class Settings:
    """
    Класс настроек игры
    """

    def __init__(self):
        self.__screen = pygame.display.set_mode((1200, 900))
        self.run()
    
    def run(self) -> None:
        """Основной метод класса."""
        settings_cycle = 1
        
        while settings_cycle:
            pygame.display.flip()

