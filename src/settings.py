"""
Настройки игры
"""

import pygame
from src.anti_repeat import exit_game
from keyboard import is_pressed


pygame.init()


class Settings:
    """
    Класс настроек игры
    """

    def __init__(self, screen: pygame.surface.Surface):
        self.__screen = screen
        
        self.__font1 = pygame.font.Font("textures/font1.otf", 63)
        
        self.__text1 = self.__font1.render("НАСТРОЙКИ", 1, (0, 0, 0))
        self.__text2 = self.__font1.render("МУЗЫКА", 1, (0, 0, 0))
        self.__text3 = self.__font1.render("НАСТРОЙКИ", 1, (0, 0, 0))
        self.run()
    
    def run(self) -> None:
        """Основной метод класса."""
        settings_cycle = 1
        
        while settings_cycle:
            self.__screen.fill((255, 255, 255))
            self.__screen.blit(self.__text1, (410, 40))
            self.__screen.blit(self.__text2, (40, 200))
            self.__screen.blit(self.__text3, (40, 330))
            
            exit_game()
            
            if is_pressed("esc"):
                settings_cycle = 0
            
            pygame.display.flip()

