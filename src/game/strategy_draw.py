"""
Отрисовка большинства текстур в игре
"""

import pygame
from src.anti_repeat import load_texture


pygame.init()


class StrategyDraw:
    """
    Класс отрисовки текстур
    """
    
    def __init__(self, screen: pygame.surface.Surface):
        self.__screen = screen
        self.__wood = load_texture('textures/wood.png',
                                    (65, 65))
        self.__iron = load_texture('textures/iron.png',
                                    (65, 65))
        self.__food = load_texture('textures/food.png',
                                    (65, 65))
        self.__shop = load_texture('textures/shop.png',
                                    (65, 65))
        self.__upgrade = load_texture('textures/upgrade.png',
                                    (65, 65))
    
    def draw_resources(self) -> None:
        """
        Отрисовка текстур ресурсов
        """
        pygame.draw.rect(self.__screen, (145, 145, 145), (0, 0, 160, 200))
        
        self.__screen.blit(self.__food, (1, 1))
        self.__screen.blit(self.__wood, (1, 70))
        self.__screen.blit(self.__iron, (1, 140))
    
    def draw_buildings(self) -> None:
        """Отрисовка построек"""
        pass
    
    def draw_buttons(self) -> pygame.rect.Rect:
        """
        Отрисовка важных кнопок
        
        Returns:
            pygame.rect.Rect: 'Квадраты' кнопкок
        """
        self.__screen.blit(self.__shop, (0, 835))
        self.__screen.blit(self.__upgrade, (66, 835))
        
        rect = self.__shop.get_rect(topleft=(0, 835))
        rect2 = self.__upgrade.get_rect(topleft=(66, 835))
        return rect, rect2
    
    def draw_minigames(self) -> None:
        """Отрисовка мини-игр (текстур мини-игр)"""
        pass

