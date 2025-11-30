"""
Главный файл игры-стратегии
"""

import pygame
from src.anti_repeat import load_texture, exit_game
from src.game.strategy_navigation import StrategyNavigation
from src.game.strategy_pause import StrategyPause
from src.game.strategy_sqlalchemy import StrategySQLAlchemy
from src.game.strategy_shop import StrategyShop
from src.game.strategy_rects import StrategyRects
from src.game.strategy_draw import StrategyDraw
from src.game.strategy_upgrade import StrategyUpgrade
from keyboard import is_pressed
from time import sleep


pygame.init()


class StrategyMain:
    """
    Главный класс игры-стратегии
    """

    def __init__(self, screen: pygame.surface.Surface):
        self.__screen = screen
        self.__play_music()
        self.__strategy_draw = StrategyDraw(self.__screen)
        self.__font1 = pygame.font.Font("textures/font1.otf", 20)
        self.__counter1, self.__counter2, self.__counter3 = 0, 0, 0
        
        self.__vault1 = 1
        self.__vault2 = 1
        self.__vault3 = 1
        self.__run()

    def __play_music(self) -> None:
        """
        Проигрывание музыки в игре
        """
        music = pygame.mixer.Sound('textures/in_game.mp3')
        music.play(-1)
    
    def __update_text(self) -> None:
        """Инициализация и вывод текста на экран"""
        self.__text1 = self.__font1.render(
            f"{self.__counter1}/{self.__vault1 * 1000}",
                                1, (255, 255, 255))
        self.__text2 = self.__font1.render(
            f"{self.__counter2}/{self.__vault2 * 1000}",
                                1, (255, 255, 255))
        self.__text3 = self.__font1.render(
            f"{self.__counter3}/{self.__vault3 * 1000}",
                                1, (255, 255, 255))
        
        self.__screen.blit(self.__text1, (70, 1))
        self.__screen.blit(self.__text2, (70, 70))
        self.__screen.blit(self.__text3, (70, 140))
    
    def redirect(self, rect: pygame.rect.Rect,
                rect2: pygame.rect.Rect) -> None:
        """
        Перенаправление игрока при нажатии кнопки
        на другие страницы
        
        Args:
            rect (pygame.rect.Rect): 'Квадрат' магазина,
            rect2 (pygame.rect.Rect): 'Квадрат' улучшения
        """
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        
        if (rect.collidepoint(mouse_pos)  # Магазин
                and pygame.mouse.get_pressed()[0]):
            StrategyShop(self.__screen)
        elif (rect2.collidepoint(mouse_pos)  # Улучшения построек
                and pygame.mouse.get_pressed()[0]):
            StrategyUpgrade(self.__screen)

    def __run(self):
        """Основной метод класса."""
        game_cycle = 1
        
        while game_cycle:
            self.__screen.fill((28, 194, 19))
            
            self.__strategy_draw.draw_resources()
            self.__strategy_draw.draw_buildings()
            rect, rect2 = self.__strategy_draw.draw_buttons()
            self.__strategy_draw.draw_minigames()
            
            self.__update_text()
            self.redirect(rect, rect2)
            exit_game()
            
            if is_pressed('esc'):
                sleep(0.89109)
                StrategyPause()

            pygame.display.flip()

