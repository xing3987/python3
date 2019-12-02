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
hero_rect = pygame.Rect(150, 600, 102, 126)
# 更新显示
pygame.display.update()

# 创建时钟对象(可以指定循环内部的频率)
clock = pygame.time.Clock()

while True:
    event_list = pygame.event.get()
    if(len(event_list)>0):
        print(event_list)

    # 设置每秒执行多少次
    clock.tick(1)
    # 修改飞机的位置
    hero_rect.y -= 50

    if hero_rect.y <= -120:
        hero_rect.y = 700
    # 绘制图像(先绘制背景刷新)
    screen.blit(bg, (0, 0))
    screen.blit(me1, hero_rect)
    # 更新图片
    pygame.display.update()
pygame.quit()
