"""
Магазин в игре-стратегии
"""

import pygame


pygame.init()


class StrategyShop:
    """
    Класс магазина в игре-стратегии.
    """
    
    def __init__(self, screen: pygame.surface.Surface):
        self.__screen = screen
        
        # Первая цифра - пшеница, вторая - дерево
        # Третья - железо, четвёртая - нужное количество работников
        self.__prices = {
            "ratusha_1": [0, 30, 30, 1],
            #"ratusha_2": [0, 300, 100, 5],
            #"ratusha_3": [0, 1000, 600, 10]
            "valut_food": [0, 30, 30, 1],
            "vault_wood": [0, 300, 100, 5],
            "vault_iron": [0, 1000, 600, 10],
            
            "collect_food": [0, 30, 30, 1],
            "collect_wood": [0, 300, 100, 5],
            "collect_iron": [0, 1000, 600, 10]
        }

