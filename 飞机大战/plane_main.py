from 飞机大战.plane_sprites import *


class PlaneGame(object):
    """飞机大战主程序"""

    def __init__(self):
        print("游戏初始化")

        # 1 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 4 设置定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __create_sprites(self):
        """创建精灵和精灵组"""

        # 1.创建背景精灵和精灵组
        # bg1 = Background("./images/background.png")
        bg1 = Background()
        # 定义第二个背景精灵，使两个背景相互滚动，注意第二张背景图片初始位置在屏幕上方
        # bg2 = Background("./images/background.png")
        # bg2.rect.y = -bg2.rect.height
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()
        pass

    def start_game(self):
        print("游戏开始")

        while True:
            # 1.设置刷新帧率
            self.clock.tick(CLOCK_TICK)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("退出游戏。。")
                pygame.quit()
                exit()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场。。")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机的精灵组
                self.enemy_group.add(enemy)

    def __check_collide(self):
        pass

    def __update_sprites(self):
        # 1.更新背景精灵组并绘制到屏幕
        self.back_group.update()
        self.back_group.draw(self.screen)
        # 2.更新敌机精灵组并绘制到屏幕
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    @staticmethod
    def __game_over():
        """
        游戏结束定义成静态方法
        """
        print("游戏结束。")
        pygame.quit()
        exit()


if __name__ == "__main__":
    # 创建游戏对象
    game = PlaneGame()
    game.start_game()
