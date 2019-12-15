import pygame
import sys
import random

import text
import classfile
import environment
import settings
import os

filepath = os.path.dirname(__file__)
ai_settings = settings.Settings()

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

def setLevel(screen):
    screen_size = screen.get_size()
    level_window = pygame.Surface(screen_size)
    level_window = level_window.convert()
    level_window.fill(ai_settings.level_bg_color)

    #text
    (level_title, v3color, v5color, v7color, SpeedLow, SpeedMid, SpeedHig, back, back1, click, click1) = text.getLevelText()
    middle_pos = (screen_size[0] - v5color.get_size()[0])/2
    middle_pos1 = (screen_size[0] - SpeedMid.get_size()[0])/2
    quater_pos = (middle_pos - v3color.get_size()[0])/2
    # quater_pos1 = (middle_pos1 - SpeedLow.get_size()[0])/2
    quater3_pos = (middle_pos + v5color.get_size()[0]) + (screen_size[0] - (middle_pos + v5color.get_size()[0]) - v7color.get_size()[0])/2
    # quater3_pos1 = (middle_pos + SpeedMid.get_size()[0]) + (screen_size[0] - (middle_pos + SpeedMid.get_size()[0]) - SpeedHig.get_size()[0])/2
    
    back_size = back.get_size()
    click_size = click.get_size()
    back_pos = (612, 640)
    click_pos = (412-click_size[0],640)

    v3color_surface = pygame.Surface(v3color.get_size())
    v5color_surface = pygame.Surface(v5color.get_size())
    v7color_surface = pygame.Surface(v7color.get_size())
    SpeedLow_surface = pygame.Surface(SpeedLow.get_size())
    SpeedMid_surface = pygame.Surface(SpeedMid.get_size())
    SpeedHig_surface = pygame.Surface(SpeedHig.get_size())

    level_button_color = ai_settings.level_button_color
    
    v3color_surface.fill(level_button_color)
    v5color_surface.fill(level_button_color)
    v7color_surface.fill(level_button_color)
    SpeedLow_surface.fill(level_button_color)
    SpeedMid_surface.fill(level_button_color)
    SpeedHig_surface.fill(level_button_color)

    color_check = 0
    speed_check = 0
    option_font_height = v3color.get_size()[1]

    while True:
        buttons = pygame.mouse.get_pressed()
        x1, y1 = pygame.mouse.get_pos()
        if color_check == 0 and buttons[0] and x1 >= quater_pos  and x1 <= quater_pos + v3color.get_size()[0] \
            and y1 >= 320 and y1 <= 320 + option_font_height:
            v3color_surface.fill(pygame.Color("red"))
            color_check = 1
        elif color_check == 0 and buttons[0] and x1 >= middle_pos and x1 <= middle_pos + v5color.get_size()[0] \
            and y1 >= 320 and y1 <= 320 + option_font_height:
            v5color_surface.fill(pygame.Color("red"))
            color_check = 2
        elif color_check == 0 and buttons[0] and x1 >= quater3_pos and x1 <= quater3_pos + v7color.get_size()[0] \
            and y1 >= 320 and y1 <= 320 + option_font_height:
            v7color_surface.fill(pygame.Color("red"))
            color_check = 3

        if speed_check == 0 and buttons[0] and x1 >= quater_pos and x1 <= quater_pos + SpeedLow.get_size()[0] \
            and y1 >= 480 and y1 <= 480 + option_font_height:
            SpeedLow_surface.fill(pygame.Color("red"))
            speed_check = 1
        elif speed_check == 0 and buttons[0] and x1 >= middle_pos1 and x1 <= middle_pos1 + SpeedMid.get_size()[0] \
            and y1 >= 480 and y1 <= 480 + option_font_height:
            SpeedMid_surface.fill(pygame.Color("red"))
            speed_check = 2
        elif speed_check == 0 and buttons[0] and x1 >= quater_pos and x1 <= quater3_pos + SpeedHig.get_size()[0] \
            and y1 >= 480 and y1 <= 480 + option_font_height:
            SpeedHig_surface.fill(pygame.Color("red"))
            speed_check = 3

        if color_check != 0 and speed_check !=0 and x1 >= click_pos[0] and x1 <= click_pos[0] + click_size[0] \
            and y1 >= click_pos[1] and y1 <= click_pos[1] + click_size[1]:
            level_window.blit(click1, click_pos)
            if buttons[0]:
                showGame(screen, color_check, speed_check)
        elif x1 >= back_pos[0] and x1 <= back_pos[0] + back_size[0] \
            and y1 >= back_pos[1] and y1 <= back_pos[1] + back_size[1]:
            level_window.blit(back1, back_pos)
            if buttons[0]:
                break
        else:
            level_window.blit(click,click_pos)
            level_window.blit(back,back_pos)

        level_window.blit(level_title, (((screen_size[0] - level_title.get_size()[0])/2, 50)))
        
        level_window.blit(v3color_surface, (quater_pos, 320))
        level_window.blit(v5color_surface, (middle_pos, 320))
        level_window.blit(v7color_surface, (quater3_pos, 320))
        level_window.blit(SpeedLow_surface, (quater_pos, 480))
        level_window.blit(SpeedMid_surface, (middle_pos1, 480))
        level_window.blit(SpeedHig_surface, (quater3_pos, 480))
        
        level_window.blit(v3color, (quater_pos, 320))
        level_window.blit(v5color, (middle_pos, 320))
        level_window.blit(v7color, (quater3_pos, 320))
        level_window.blit(SpeedLow, (quater_pos, 480))
        level_window.blit(SpeedMid, (middle_pos1, 480))
        level_window.blit(SpeedHig, (quater3_pos, 480))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(level_window, (0, 0))
        pygame.display.update()
    return # 返回难度情况，给showNewGame作为参数传入

def showNewGame(screen, color_check, speed_check):
    screen_size = screen.get_size()
    game_window = pygame.Surface(screen_size)
    game_window = game_window.convert()
    game_window.fill(ai_settings.game_bg_color)

    # 初始化score
    score = 0
    score_text_font = pygame.font.Font(os.path.join(filepath,"fonts/FZCHYJW.ttf"), 25)
    score_text = score_text_font.render("Score: " + str(int(score)), True, (0, 0, 0))

    # 初始化timer
    prev_ticks = pygame.time.get_ticks() / 1000
    gravity_timer = 5 + random.expovariate(1/5)
    gravity_timer_text_font = pygame.font.Font(os.path.join(filepath,"fonts/SIMYOU.ttf"), 20)
    gravity_timer_text_color = pygame.Color("dodgerblue")
    gravity_timer_text = gravity_timer_text_font.render("距离下次重力反转还有：" + str(round(gravity_timer, 2)) + " s", True, gravity_timer_text_color)
    
    # 初始化重力
    gravity_direction = 1
    gravity_status_up = pygame.image.load(os.path.join(filepath,"images/up_arrow.png")).convert_alpha()
    gravity_status_down = pygame.image.load(os.path.join(filepath,"images/down_arrow.png")).convert_alpha()
    gravity_status = [gravity_status_up, gravity_status_down]
    gravity_indicator = gravity_timer_text_font.render("当前重力方向：", True, gravity_timer_text_color)
    gravity, curr_force = 0.075, 0
    force_const = 0.15
    total_gravity = gravity + curr_force

    # 初始化地图
    slots = []
    flag = 0
    num_of_slots = int(screen_size[0]/ai_settings.slot_width) + 1
    for i in range(num_of_slots):
        slots.append(classfile.Slot(screen_size, 84, 600))
        slots[i].top_slot_rect[0] = ai_settings.slot_width * i
        slots[i].bottom_slot_rect[0] = ai_settings.slot_width * i

    # 显示难度信息
    level_option_font = pygame.font.Font(os.path.join(filepath,"fonts/ARLRDBD.ttf"), 18)
    v3color = level_option_font.render("Three Color", True, (0,0,0))
    v5color = level_option_font.render("Five Color", True, (0,0,0))
    v7color = level_option_font.render("Seven Color", True, (0,0,0))
    SpeedLow = level_option_font.render("Low Speed", True, (0,0,0))
    SpeedMid = level_option_font.render("Middle Speed", True, (0,0,0))
    SpeedHig = level_option_font.render("High Speed", True, (0,0,0))
    color_levels = (v3color, v5color, v7color)
    speed_levels = (SpeedLow, SpeedMid, SpeedHig)
    
    color_choice = color_levels[color_check-1]
    speed_choice = speed_levels[speed_check-1]

    # 初始化Biofilm
    biofilm_lambda = ai_settings.film_lambda
    biofilm_timer = random.expovariate(biofilm_lambda)
    biofilm_top_timer_limit = ai_settings.top_timer_limit
    biofilm_bottom_timer_limit = ai_settings.bottom_timer_limit
    if biofilm_timer < biofilm_bottom_timer_limit:
        biofilm_timer = biofilm_bottom_timer_limit
    elif biofilm_timer > biofilm_top_timer_limit:
        biofilm_timer = biofilm_top_timer_limit
    biofilm_form = 0

    screen_size = screen.get_size()
    game_window = pygame.Surface(screen_size)
    game_window = game_window.convert()
    game_window.fill((238, 230, 133))

    ball_color_order = ai_settings.ball_color_order[:(2*color_check+1)]
    num_of_color = len(ball_color_order)
    current_ball_color = 0
    if speed_check == 1:
        speed_limit = ai_settings.ball_speed_limit_low
    elif speed_check == 2:
        speed_limit = ai_settings.ball_speed_limit_mid
    elif speed_check == 3:
        speed_limit = ai_settings.ball_speed_limit_hig 

    ball = classfile.Ball(ai_settings)
    biofilm_queue = []
    # biofilm = classfile.Biofilm(ai_settings)

    # 准备阶段
    go_start = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_i:
                    go_start = True
            elif event.type == pygame.QUIT:
                sys.exit()
        if go_start:
            break
        game_window.fill((238, 230, 133))
        game_window.blit(ball.ball_surface, ball.ball_rect)
        # game_window.blit(biofilm.film_surface, biofilm.film_rect)
        screen.blit(game_window, (0, 0))
        pygame.display.update()

    # 游戏部分
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    curr_force -= force_const
                elif event.key == pygame.K_k:
                    curr_force += force_const
                elif event.key == pygame.K_SPACE:
                    current_ball_color = (current_ball_color + 1) % num_of_color
                    ball.color = ball_color_order[current_ball_color]
                    ball.ball_surface.fill(pygame.Color((ball.color)))
                elif event.key == pygame.K_j:
                    ball.left = -1
                elif event.key == pygame.K_l:
                    ball.right = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_j:
                    ball.left = 0
                elif event.key == pygame.K_l:
                    ball.right = 0
                elif event.key == pygame.K_i:
                    curr_force += force_const
                elif event.key == pygame.K_k:
                    curr_force -= force_const
            elif event.type == pygame.QUIT:
                sys.exit()
        
        # 更新重力方向和timer
        current_ticks = pygame.time.get_ticks() / 1000
        dt = current_ticks - prev_ticks
        prev_ticks = current_ticks
        gravity, gravity_timer, gravity_direction = environment.updateGravity(gravity, gravity_timer, dt)
        total_gravity = gravity + curr_force

        gravity_timer_text = gravity_timer_text_font.render("距离下次重力反转还有：" + str(round(gravity_timer, 2)) + " s", True, gravity_timer_text_color)

        # 随机生成Biofilm
        biofilm_form, biofilm_timer = environment.generateBiofilm(biofilm_timer,dt,biofilm_lambda)
        if biofilm_form == 1:
            biofilm_queue.append(classfile.Biofilm(ai_settings, color_check))
            biofilm_form = 0
        # print(biofilm_timer)

        # 删除出屏Biofilm
        if len(biofilm_queue) > 0 and biofilm_queue[0].film_pos <= 0:
            biofilm_queue.pop(0)

        # 判断ball穿膜
        colli_film_color = "white"
        for biofilm in biofilm_queue:
            if ball.ball_rect[0] + ai_settings.ball_size[0] == biofilm.film_pos:
                score += 10
                if biofilm.film_color == "white":
                    ball.color = ai_settings.ball_color_order[random.randint(0,len(ai_settings.ball_color_order)-1)]
                    ball.ball_surface.fill(pygame.Color((ball.color)))
                    colli_film_color = "white"
                else:
                    colli_film_color = biofilm.film_color

        # 更新位置
        ball.speed += total_gravity
        if ball.speed >= speed_limit:
            ball.speed = speed_limit
        elif ball.speed <= -speed_limit:
            ball.speed = -speed_limit
        ball.ball_rect[1] += int(ball.speed)
        ball.ball_rect[0] += ball.left + ball.right
        for biofilm in biofilm_queue:
            biofilm.film_pos -= biofilm.film_speed

        # 更新slots
        flag = (flag + 1) % ai_settings.slot_width
        if flag % 8 == 0:
            for i in range(num_of_slots):
                slots[i].top_slot_rect[0] -= 8
                slots[i].bottom_slot_rect[0] -= 8
        if flag == 0:
            slots.pop(0)
            last_slot = slots[-1]
            slots.append(classfile.Slot(screen_size, last_slot.level, last_slot.height))

        # 更新分数
        score += 0.01
        score_text = score_text_font.render("Score: " + str(int(score)), True, (0, 0, 0))
        
        # 检查死亡：位置+颜色
        if environment.checkDead(ai_settings, colli_film_color, ball.color, screen_size, ball, slots):
            return score

        # 刷新屏幕
        game_window.fill((238, 230, 133))
        for i in range(num_of_slots):
            temp_slot = slots[i]
            game_window.blit(temp_slot.top_slot_surface, temp_slot.top_slot_rect)
            game_window.blit(temp_slot.bottom_slot_surface, temp_slot.bottom_slot_rect)
        game_window.blit(ball.ball_surface, ball.ball_rect)
        for biofilm in biofilm_queue:
            game_window.blit(biofilm.film_surface, (biofilm.film_pos,0))
        game_window.blit(gravity_timer_text, (20, 20))
        game_window.blit(gravity_indicator, (20, 80))
        game_window.blit(gravity_status[gravity_direction], (150, 60))
        game_window.blit(score_text, (450, 20))
        game_window.blit(color_choice, (800, 20))
        game_window.blit(speed_choice, (900, 20))
        screen.blit(game_window, (0, 0))
        pygame.display.update()
    
    return score

def showScore(screen, score):
    return # True or False

def showGame(screen, color_check, speed_check):
    while True:
        score = showNewGame(screen, color_check, speed_check)
        '''
        go_to_welcome = showScore(screen, score)
        if go_to_welcome:
            break
        '''