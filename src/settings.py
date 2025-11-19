"""
Настройки игры
"""

import pygame


pygame.init()


class Settings:
    """
    Класс настроек игры
    """

    def __init__(self, screen: pygame.surface.Surface):
        self.__screen = screen
        self.run()
    
    def run(self) -> None:
        """Основной метод класса."""
        settings_cycle = 1
        
        while settings_cycle:
            pygame.display.flip()

