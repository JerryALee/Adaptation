#minimized development framework

import sys
import pygame
def run_game():
    #initialize game and create a dispaly object
    pygame.init()
    screen = pygame.display.set_mode((369,224))
    pygame.display.set_caption("Adaptation")
    # set backgroud
    background=pygame.image.load("./graphics/level_1.png")

    # game loop
    while True:
        # supervise keyboard and mouse item
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # fill color
        screen.blit(background,(0,0))  #对齐的坐标
        # visualiaze the window
        pygame.display.flip()
run_game()