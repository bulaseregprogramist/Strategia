"""
Магазин в игре-стратегии
"""

import pygame
from src.anti_repeat import exit_game
from keyboard import is_pressed
from time import sleep


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
        self.__run()
    
    def __run(self) -> None:
        """
        Основной метод класса
        """
        shop_cycle = 1
        
        while shop_cycle:
            pygame.draw.rect(self.__screen, (255, 255, 255),
                            (70, 70, 1060, 760))
            
            exit_game()
            pygame.display.flip()
            
            if is_pressed('esc'):
                sleep(0.89109)
                shop_cycle = 0

