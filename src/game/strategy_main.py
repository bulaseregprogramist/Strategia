"""
Главный файл игры-стратегии
"""

import pygame
from src.anti_repeat import load_texture, exit_game
from src.game.strategy_navigation import StrategyNavigation
from src.game.strategy_pause import StrategyPause
from src.game.strategy_sqlalchemy import StrategySQLAlchemy
from src.game.strategy_shop import StrategyShop
from src.game.strategy_draw import StrategyDraw


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
        self.__run()

    def __play_music(self) -> None:
        """
        Проигрывание музыки в игре
        """
        music = pygame.mixer.Sound('textures/in_game.mp3')
        music.play(-1)
    
    def __initialize_text(self) -> None:
        """Инициализация и вывод текста на экран"""
        self.__text1 = self.__font1.render(f"{self.__counter1}",
                                        1, (255, 255, 255))
        self.__text2 = self.__font1.render(f"{self.__counter2}",
                                        1, (255, 255, 255))
        self.__text3 = self.__font1.render(f"{self.__counter3}",
                                        1, (255, 255, 255))
        
        self.__screen.blit(self.__text1, (70, 1))
        self.__screen.blit(self.__text2, (70, 70))
        self.__screen.blit(self.__text3, (70, 140))

    def __run(self):
        """Основной метод класса."""
        game_cycle = 1
        
        while game_cycle:
            self.__screen.fill((179, 208, 255))
            self.__strategy_draw.draw_resources()
            
            self.__initialize_text()
            exit_game()

            pygame.display.flip()

