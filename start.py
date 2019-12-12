import pygame
import sys
import random

import text
import showscreen

pygame.init()
window = pygame.display.set_mode((1024, 768), 32) # 窗口大小
window_size = window.get_size()
pygame.display.set_caption("Adaptation") # 窗口名，Adaptation
clock = pygame.time.Clock()
clock.tick(60)
start_window = pygame.Surface(window_size)
start_window = start_window.convert()
start_window.fill((178, 233, 238))

(title, ksyx, ksyx1, yxsm, yxsm1, gyzz, gyzz1, tcyx, tcyx1) = text.getWelcomeText()
start_font_size = ksyx.get_size()

while True:
    buttons = pygame.mouse.get_pressed()
    x1, y1 = pygame.mouse.get_pos()
    if x1 >= (window_size[0] - start_font_size[0])/2 and x1 <= (window_size[0] + start_font_size[0])/2 \
        and y1 >= 400 and y1 <= 400 + start_font_size[1]:
        start_window.blit(ksyx1, ((window_size[0] - start_font_size[0])/2, 400))
        if buttons[0]:
            showscreen.showGame(window) # 进入游戏
    elif x1 >= (window_size[0] - start_font_size[0])/2 and x1 <= (window_size[0] + start_font_size[0])/2 and \
        y1 >= 480 and y1 <= 480 + start_font_size[1]:
        start_window.blit(yxsm1, ((window_size[0] - start_font_size[0])/2, 480))
        if buttons[0]:
            showscreen.showIntro(window) # 进入游戏说明界面
    elif x1 >= (window_size[0] - start_font_size[0])/2 and x1 <= (window_size[0] + start_font_size[0])/2 and \
        y1 >= 560 and y1 <= 560 + start_font_size[1]:
        start_window.blit(gyzz1, ((window_size[0] - start_font_size[0])/2, 560))
        if buttons[0]:
            showscreen.showAuthor(window) # 进入作者界面
    elif x1 >= (window_size[0] - start_font_size[0])/2 and x1 <= (window_size[0] + start_font_size[0])/2 and \
        y1 >= 640 and y1 <= 640 + start_font_size[1]:
        start_window.blit(tcyx1, ((window_size[0] - start_font_size[0])/2, 640))
        if buttons[0]:
            print("Exiting...")
            sys.exit() # 退出游戏
    else:
        start_window.blit(title, (((window_size[0] - title.get_size()[0])/2, 50)))
        start_window.blit(ksyx, ((window_size[0] - start_font_size[0])/2, 400))
        start_window.blit(yxsm, ((window_size[0] - start_font_size[0])/2, 480))
        start_window.blit(gyzz, ((window_size[0] - start_font_size[0])/2, 560))
        start_window.blit(tcyx, ((window_size[0] - start_font_size[0])/2, 640))
    
    window.blit(start_window, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting...")
            sys.exit()