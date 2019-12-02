"""
设计一个Game类，
定义一个类属性top_sore继续游戏的历史最高分
定义一个实例属性player_name记录当前游戏的玩家姓名

静态方法show_help显示游戏帮助信息
类方法show_top_score显示历史最高分
实例方法star_game开始当前玩家的游戏

程序步骤
1.查看帮助信息
2.查看历史最高分
3.创建游戏对象，开始游戏
"""

import random


# 定义游戏类
class Game:
    top_sore = 0
    top_sore_player = None

    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0

    @staticmethod
    def show_help():
        print("这是游戏的帮助信息。")

    @classmethod
    def show_top_score(cls):
        if (cls.top_sore > 0):
            print("游戏的最高分为%d,获得者是%s" % (cls.top_sore, cls.top_sore_player))

    # 实例方法可以获取实例属性和类属性
    def play(self):
        self.score = random.randint(0, 100)
        print("玩家%s获得分数%d." % (self.player_name, self.score))
        if (self.score > Game.top_sore):
            Game.top_sore = self.score
            Game.top_sore_player = self.player_name


player1 = Game("player1")
Game.show_help()
Game.show_top_score()
player1.play()

player2 = Game("player2")
Game.show_help()
Game.show_top_score()
player2.play()

Game.show_top_score()
