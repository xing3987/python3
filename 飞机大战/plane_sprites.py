import random
import pygame

# 定义常量
SCREEN_RECT = pygame.Rect(0, 0, 400, 700)
CLOCK_TICK = 60
# 定义敌机定时器常量(事件type)
CREATE_ENEMY_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):
    """
    飞机大战游戏精灵,精灵类要提供初始化的方法和update方法
    """

    def __init__(self, image_name, speed=1):
        # 继承的不是Object类要调用父类的初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        """is_alt参数用来区分第一张图片还是第二张图片，默认是第一张，如果为True则是第二张"""
        super().__init__("./images/background.png")
        if not is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 重写背景类的移动方法
        # 1.调用父类的方法
        super().update()
        # 2.判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")
        # 2.指定敌机的初始随机速度1-3
        self.speed = random.randint(1, 3)
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1.调用父类的方法，保存垂直方向的飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            print("飞出屏幕，需要从精灵组删除。")
            self.kill()

    def __del__(self):
        print("销毁了敌机。%s" % self.rect)


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        super().__init__("./images/me1.png", 0)
        # 设置英雄初始化位置(x中心为屏幕的中心，y为屏幕底部向上100像素)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 100

    # 重写update方法使英雄移动
    def update(self):
        self.rect.x += self.speed
