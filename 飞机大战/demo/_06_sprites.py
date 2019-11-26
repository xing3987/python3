import pygame
from 飞机大战.plane_sprites import *

pygame.init()
# 创建窗口
screen = pygame.display.set_mode((400, 700))

# 加载背景图片
bg = pygame.image.load("../images/background.png")
me1 = pygame.image.load("../images/me1.png")

# blit绘制背景
screen.blit(bg, (0, 0))

# 绘制小飞机
hero_rect = pygame.Rect(150, 600, 102, 126)
# 更新显示
pygame.display.update()

# 创建时钟对象(可以指定循环内部的频率)
clock = pygame.time.Clock()

# 创建敌机的精灵
enemy1 = GameSprite("../images/enemy1.png", 10)
enemy2 = GameSprite("../images/enemy2.png", 20)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy1, enemy2)

while True:
    # 事件监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏。。")
            pygame.quit()
            exit()

    # 设置每秒执行多少次
    clock.tick(10)
    # 修改飞机的位置
    hero_rect.y -= 50
    if hero_rect.y <= -120:
        hero_rect.y = 700
    # 绘制图像(先绘制背景刷新)
    screen.blit(bg, (0, 0))
    screen.blit(me1, hero_rect)

    # 让精灵组调用两个方法绘制精灵
    # update-让族中的精灵更新位置
    enemy_group.update()
    # draw-在屏幕上绘制所有的精灵
    enemy_group.draw(screen)

    # 更新图片
    pygame.display.update()
pygame.quit()
