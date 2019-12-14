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

def showNewGame(screen):
    # 初始化score
    score = 0
    score_text_font = pygame.font.SysFont("方正粗活意简体", 25)
    score_text = score_text_font.render("Score: " + str(int(score)), True, (0, 0, 0))

    # 初始化timer
    prev_ticks = pygame.time.get_ticks() / 1000
    timer = 5 + random.expovariate(1/5)
    timer_text_font = pygame.font.SysFont("幼圆", 20)
    timer_text_color = pygame.Color("dodgerblue")
    timer_text = timer_text_font.render("距离下次重力反转还有：" + str(round(timer, 2)) + " s", True, timer_text_color)
    
    # 初始化重力
    gravity_direction = 1
    gravity_status_up = pygame.image.load("./images/up_arrow.png").convert_alpha()
    gravity_status_down = pygame.image.load("./images/down_arrow.png").convert_alpha()
    gravity_status = [gravity_status_up, gravity_status_down]
    gravity_indicator = timer_text_font.render("当前重力方向：", True, timer_text_color)
    gravity, force = 0.075, 0.15
    total_gravity = gravity

    screen_size = screen.get_size()
    game_window = pygame.Surface(screen_size)
    game_window = game_window.convert()
    game_window.fill((238, 230, 133))
    ball_color_order = ["red", "yellow", "green", "blue", "purple"]
    num_of_color = len(ball_color_order)
    current_ball_color = 0
    speed_limit = 2 # 4

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
                    total_gravity = gravity - force
                elif event.key == pygame.K_DOWN:
                    total_gravity = gravity + force
                elif event.key == pygame.K_SPACE:
                    current_ball_color = (current_ball_color + 1) % num_of_color
                    ball.color = ball_color_order[current_ball_color]
                    ball.ball_surface.fill(pygame.Color((ball.color)))
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
                    total_gravity = gravity
                elif event.key == pygame.K_DOWN:
                    total_gravity = gravity
            elif event.type == pygame.QUIT:
                sys.exit()
        
        # 检查死亡
        dead = ball.checkDead(screen_size)
        if dead:
            return score
        
        # 更新位置
        ball.speed += total_gravity
        if ball.speed >= speed_limit:
            ball.speed = speed_limit
        elif ball.speed <= -speed_limit:
            ball.speed = -speed_limit
        ball.ball_rect[1] += int(ball.speed)
        ball.ball_rect[0] += ball.left + ball.right

        # 更新重力方向和timer
        current_ticks = pygame.time.get_ticks() / 1000
        dt = current_ticks - prev_ticks
        prev_ticks = current_ticks
        gravity, timer, gravity_direction = environment.updateGravity(gravity, timer, dt)
        timer_text = timer_text_font.render("距离下次重力反转还有：" + str(round(timer, 2)) + " s", True, timer_text_color)

        # 更新分数
        score += 0.01
        score_text = score_text_font.render("Score: " + str(int(score)), True, (0, 0, 0))
        
        # 刷新屏幕
        game_window.fill((238, 230, 133))
        game_window.blit(ball.ball_surface, ball.ball_rect)
        game_window.blit(timer_text, (20, 20))
        game_window.blit(gravity_indicator, (20, 50))
        game_window.blit(gravity_status[gravity_direction], (150, 40))
        game_window.blit(score_text, (450, 20))
        screen.blit(game_window, (0, 0))
        pygame.display.update()
    
    return score

def showScore(screen, score):
    return # True or False

def showGame(screen):
    while True:
        score = showNewGame(screen)
        '''
        go_to_welcome = showScore(screen, score)
        if go_to_welcome:
            break
        '''