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
        pygame.time.set_timer(HERO_FIRE_EVENT, 700)

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

        # 2.创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 3.创建英雄的精灵组
        # 将英雄精灵添加到英雄的精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

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
            '''  
            第一种方式，使用事件监听的方式，获取按键，但是不能获取连续按键，只能一个一个获取 
            elif event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
                print("向右移动。")
            '''
            # 使用键盘提供的方法获取键盘按键，一直按住可以一直连续获取
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_RIGHT]:
                # print("向右移动。")
                self.hero.speed = 2
            elif key_pressed[pygame.K_LEFT]:
                # print("向左移动。")
                self.hero.speed = -2
            else:
                self.hero.speed = 0
            # 定义调用发射字弹的事件
            if event.type == HERO_FIRE_EVENT:
                self.hero.fire()

    # 碰撞检测
    def __check_collide(self):
        # 1.子弹摧毁敌机groupcollide(第一个参数为对象1，第二个参数为对象2，
        # 第三个参数为对象1是否销毁，第四个参数为对象2是否销毁,返回值为碰撞的所有对象)
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)

        # 2.敌机摧毁英雄（判断是否碰撞，如果碰撞游戏结束）
        """
        #第一种方法，使用组碰撞的方法
        list = pygame.sprite.groupcollide(self.hero_group, self.enemy_group, True, True)
        if list:
            self.__game_over()
        """
        # 第二种方法，使用精灵和精灵组碰撞的方法
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if enemies:
            self.__game_over()

    def __update_sprites(self):
        # 1.更新背景精灵组并绘制到屏幕
        self.back_group.update()
        self.back_group.draw(self.screen)
        # 2.更新敌机精灵组并绘制到屏幕
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        # 3.更新英雄精灵组并绘制到屏幕
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        # 4.更新子弹精灵组并绘制到屏幕
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

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
