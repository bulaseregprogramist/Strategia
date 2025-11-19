"""
Главное меню игры
"""

import pygame
from src.anti_repeat import exit_game
from src.settings import Settings
from src.game.strategy_main import StrategyMain
from random import randint
import sys


pygame.init()


class MainMenu:
    """
    Класс главного меню игры
    """
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((1200, 900))
        self.__clock = pygame.time.Clock()
        pygame.display.set_caption("Стратегия.")
        pygame.display.set_icon(pygame.image.load("textures/icon.png"))
        
        self.__font = pygame.font.Font('textures/font1.otf', 73)
        self.__font2 = pygame.font.Font('textures/font1.otf', 37)
        self.__text1 = self.__font.render("СТРАТЕГИЯ", 1, (255, 255, 255))
        
        self.__text2 = self.__font2.render("ИГРАТЬ", 1, (255, 255, 255))
        self.__text3 = self.__font2.render("НАСТРОЙКИ", 1, (255, 255, 255))
        self.__text4 = self.__font2.render("ВЫХОД", 1, (255, 255, 255))
        
        self.__color1, self.__color2, self.__color3 = 0, 0, 0
        self.__counter = 0
        
        self.__clock.tick(60)
        
        self.__play_music()
        self.__run()

    def __play_music(self) -> None:
        """
        Проигрывание музыки в главном меню
        """
        music = pygame.mixer.Sound('textures/in_menu.mp3')
        music.play(-1)
    
    def __exit_game(self) -> None:
        """
        Выход из игры
        """
        pygame.quit()
        sys.exit()

    def draw_menu(self) -> None:
        """
        Отрисовка главного меню
        """
        pygame.draw.rect(self.__screen,
                    (self.__color1, self.__color2, self.__color3),
                    (0, 0, 1200, 900))
        self.__screen.blit(self.__text1, (410, 60))
            
        self.__screen.blit(self.__text2, (510, 200))
        self.__screen.blit(self.__text3, (510, 300))
        self.__screen.blit(self.__text4, (510, 400))

        self.__counter += 1
        
        if self.__counter > 10:
            num: int = randint(1, 3)
            
            if num == 1:
                self.__color1 += 1
            if num == 2:
                self.__color2 += 1
            if num == 3:
                self.__color3 += 1
            
            self.__counter = 0

        if self.__color1 > 235:
            self.__color1 = 0
        if self.__color2 > 235:
            self.__color2 = 0
        if self.__color3 > 235:
            self.__color3 = 0

    def menu_buttons(self) -> None:
        """
        Кнопки главного меню
        """
        square1 = pygame.Surface((135, 40))
        self.__screen.blit(square1, (510, 200))
        square2 = pygame.Surface((135, 40))
        self.__screen.blit(square2, (510, 300))
        square3 = pygame.Surface((135, 40))
        self.__screen.blit(square3, (510, 400))

        rect1 = square1.get_rect(topleft=(510, 200))
        rect2 = square2.get_rect(topleft=(510, 300))
        rect3 = square3.get_rect(topleft=(510, 400))

        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()

        if rect1.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            StrategyMain()
        elif rect2.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            Settings()
        elif rect3.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.__exit_game()

    def __run(self):
        """Основная функция класса"""
        cycle = 1
        
        while cycle:
            self.menu_buttons()
            self.draw_menu()
            exit_game()

            pygame.display.flip()

