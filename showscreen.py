import pygame
import sys
import random

import text
import classfile
import environment

def showAuthor(screen):
    screen_size = screen.get_size()
    author_window = pygame.Surface(screen_size)
    author_window = author_window.convert()
    author_window.fill((178, 233, 238))

    back_pos = (850, 650)
    (hmc, lcr, htq, wsn, jby, back, back1) = text.getAuthorText()
    author_font_size = hmc.get_size()
    back_font_size = back.get_size()
    author_window.blit(hmc, ((screen_size[0] - author_font_size[0])/2, 100))
    author_window.blit(lcr, ((screen_size[0] - author_font_size[0])/2, 150))
    author_window.blit(htq, ((screen_size[0] - author_font_size[0])/2, 200))
    author_window.blit(wsn, ((screen_size[0] - author_font_size[0])/2, 250))
    author_window.blit(jby, ((screen_size[0] - author_font_size[0])/2, 300))
    while True:
        buttons = pygame.mouse.get_pressed()
        x1, y1 = pygame.mouse.get_pos()
        if x1 >= back_pos[0] and x1 <= back_pos[0] + back_font_size[0] and \
            y1 >= back_pos[1] and y1 <= back_pos[1] + back_font_size[1]:
            author_window.blit(back1, back_pos)
            if buttons[0]:
                break
        else:
            author_window.blit(back, back_pos)
        screen.blit(author_window, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def showIntro(screen):
    screen_size = screen.get_size()
    intro_window = pygame.Surface(screen_size)
    intro_window = intro_window.convert()
    intro_window.fill((178, 233, 238))

    back_pos = (850, 650)
    (intro, back, back1) = text.getIntroText()
    intro_font_size = intro.get_size()
    back_font_size = back.get_size()
    intro_window.blit(intro, ((screen_size[0] - intro_font_size[0])/2, 100))
    while True:
        buttons = pygame.mouse.get_pressed()
        x1, y1 = pygame.mouse.get_pos()
        if x1 >= back_pos[0] and x1 <= back_pos[0] + back_font_size[0] and \
            y1 >= back_pos[1] and y1 <= back_pos[1] + back_font_size[1]:
            intro_window.blit(back1, back_pos)
            if buttons[0]:
                break
        else:
            intro_window.blit(back, back_pos)
        screen.blit(intro_window, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def showGame(screen):
    screen_size = screen.get_size()
    game_window = pygame.Surface(screen_size)
    game_window = game_window.convert()
    game_window.fill((238, 230, 133))
    ball_color_order = ["red", "yellow", "green", "blue", "purple"]
    num_of_color = len(ball_color_order)
    current_ball_color = 0
    speed_limit = 7
    force = 0.11

    ball = classfile.Ball()

    # 准备阶段
    go_start = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                go_start = True
            elif event.type == pygame.QUIT:
                sys.exit()
        if go_start:
            break
        game_window.fill((238, 230, 133))
        game_window.blit(ball.ball_surface, ball.ball_rect)
        screen.blit(game_window, (0, 0))
        pygame.display.update()

    # 游戏部分
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.gravity -= force
                elif event.key == pygame.K_DOWN:
                    ball.gravity += force
                elif event.key == pygame.K_SPACE:
                    current_ball_color = (current_ball_color + 1) % num_of_color
                    ball.color = ball_color_order[current_ball_color]
                    ball.ball_surface.fill(environment.convertColor(ball.color))
                elif event.key == pygame.K_LEFT:
                    ball.left = -1
                elif event.key == pygame.K_RIGHT:
                    ball.right = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ball.left = 0
                elif event.key == pygame.K_RIGHT:
                    ball.right = 0
                elif event.key == pygame.K_UP:
                    ball.gravity += force
                elif event.key == pygame.K_DOWN:
                    ball.gravity -= force
            elif event.type == pygame.QUIT:
                sys.exit()
        ball.speed += ball.gravity
        if ball.speed >= speed_limit:
            ball.speed = speed_limit
        elif ball.speed <= -speed_limit:
            ball.speed = -speed_limit
        ball.ball_rect[1] += int(ball.speed)

        ball.ball_rect[0] += ball.left + ball.right
        game_window.fill((238, 230, 133))
        game_window.blit(ball.ball_surface, ball.ball_rect)
        screen.blit(game_window, (0, 0))
        pygame.display.update()