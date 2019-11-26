import pygame

pygame.init()
# 创建窗口
screen = pygame.display.set_mode((400, 700))

# 加载背景图片
bg = pygame.image.load("../images/background.png")
me1 = pygame.image.load("../images/me1.png")

# blit绘制背景
screen.blit(bg, (0, 0))

# 绘制小飞机
screen.blit(me1, (150, 500))
# 更新显示
pygame.display.update()

# 创建时钟对象(可以指定循环内部的频率)
clock = pygame.time.Clock()

i = 0
while True:
    # 设置每秒执行多少次
    clock.tick(1)
    print(i)
    i = i + 1
    pass

pygame.quit()
