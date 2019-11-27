import pygame

# 定义常量
SCREEN_RECT = pygame.Rect(0, 0, 400, 700)
CLOCK_TICK = 60


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
