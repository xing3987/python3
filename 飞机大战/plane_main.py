import pygame
from 飞机大战.plane_sprites import *


class PlaneGame(object):
    """飞机大战主程序"""

    def __init__(self):
        print("游戏初始化")

        # 1 创建游戏的窗口
        self.screen = pygame.display.set_mode((400, 700))
        # 2 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

    def __create_sprites(self):
        pass

    def start_game(self):
        print("游戏开始")


if __name__ == "__main__":
    # 创建游戏对象
    game = PlaneGame()
    game.start_game()
