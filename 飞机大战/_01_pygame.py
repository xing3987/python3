import pygame

pygame.init()
# 绘制矩形
hero_rect = pygame.Rect(100, 500, 120, 125)
print(hero_rect.x, hero_rect.width, hero_rect.height)
# 创建窗口
screen = pygame.display.set_mode((400, 700))


pygame.quit()
