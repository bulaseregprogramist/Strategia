"""
Перемещение игрока по карте
"""

from keyboard import is_pressed


class StrategyNavigation:
    """
    Класс перемещения
    """
    
    def __init__(self):
        pass
    
    def move(self, cord1: int, cord2: int) -> tuple:
        """
        Перемещение по карте благодаря клавишам
        
        Args:
            cord1 (int): Размещение всех объектов №1
            cord2 (int): Размещение всех объектов №2
        Returns:
            tuple: Изменённое (или нет) положение игрока на карте игры
        """
        if is_pressed('w'):
            cord1 += 1
        elif is_pressed('s'):
            cord1 -= 1
        elif is_pressed('a'):
            cord2 += 1
        elif is_pressed('d'):
            cord2 += 1
        return cord1, cord2

