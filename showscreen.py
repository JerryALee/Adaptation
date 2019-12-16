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
    # intro is a list, containing all the introduction information exept 'back'.
    intro_font_size = intro[0].get_size()
    back_font_size = back.get_size()
    # intro_window.blit(intro, ((screen_size[0] - intro_font_size[0])/2, 100))
    intro_window.blit(intro[0],((screen_size[0] - intro_font_size[0])/2, 40))
    intro_window.blit(intro[1],(50, 80))
    intro_window.blit(intro[2],(50, 120))
    intro_window.blit(intro[3],(50, 160))
    intro_window.blit(intro[4],(50, 200))
    intro_window.blit(intro[5],(50, 240))
    intro_window.blit(intro[6],(50, 280))
    intro_window.blit(intro[7],(50, 330))
    intro_window.blit(intro[8],(50, 370))
    intro_window.blit(intro[9],(50, 410))
    intro_window.blit(intro[10],(50, 450))
    intro_window.blit(intro[11],(50, 500))
    intro_window.blit(intro[12],(50, 540))
    intro_window.blit(intro[13],(50, 580))
    intro_window.blit(intro[14],(50, 620))
    intro_window.blit(intro[15],((screen_size[0] - intro_font_size[0])/2, 670))

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
    color_surface_list = (v3color_surface, v5color_surface, v7color_surface)
    SpeedLow_surface = pygame.Surface(SpeedLow.get_size())
    SpeedMid_surface = pygame.Surface(SpeedMid.get_size())
    SpeedHig_surface = pygame.Surface(SpeedHig.get_size())
    speed_surface_list = (SpeedLow_surface, SpeedMid_surface, SpeedHig_surface)

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
        if buttons[0] and x1 >= quater_pos  and x1 <= quater_pos + v3color.get_size()[0] \
            and y1 >= 320 and y1 <= 320 + option_font_height:
            if color_check != 0:
                color_surface_list[color_check - 1].fill(level_button_color)
            v3color_surface.fill(pygame.Color("red"))
            color_check = 1
        elif buttons[0] and x1 >= middle_pos and x1 <= middle_pos + v5color.get_size()[0] \
            and y1 >= 320 and y1 <= 320 + option_font_height:
            if color_check != 0:
                color_surface_list[color_check - 1].fill(level_button_color)
            v5color_surface.fill(pygame.Color("red"))
            color_check = 2
        elif buttons[0] and x1 >= quater3_pos and x1 <= quater3_pos + v7color.get_size()[0] \
            and y1 >= 320 and y1 <= 320 + option_font_height:
            if color_check != 0:
                color_surface_list[color_check - 1].fill(level_button_color)
            v7color_surface.fill(pygame.Color("red"))
            color_check = 3

        if buttons[0] and x1 >= quater_pos and x1 <= quater_pos + SpeedLow.get_size()[0] \
            and y1 >= 480 and y1 <= 480 + option_font_height:
            if speed_check != 0:
                speed_surface_list[speed_check - 1].fill(level_button_color)
            SpeedLow_surface.fill(pygame.Color("red"))
            speed_check = 1
        elif buttons[0] and x1 >= middle_pos1 and x1 <= middle_pos1 + SpeedMid.get_size()[0] \
            and y1 >= 480 and y1 <= 480 + option_font_height:
            if speed_check != 0:
                speed_surface_list[speed_check - 1].fill(level_button_color)
            SpeedMid_surface.fill(pygame.Color("red"))
            speed_check = 2
        elif buttons[0] and x1 >= quater_pos and x1 <= quater3_pos + SpeedHig.get_size()[0] \
            and y1 >= 480 and y1 <= 480 + option_font_height:
            if speed_check != 0:
                speed_surface_list[speed_check - 1].fill(level_button_color)
            SpeedHig_surface.fill(pygame.Color("red"))
            speed_check = 3

        if color_check != 0 and speed_check !=0 and x1 >= click_pos[0] and x1 <= click_pos[0] + click_size[0] \
            and y1 >= click_pos[1] and y1 <= click_pos[1] + click_size[1]:
            level_window.blit(click1, click_pos)
            if buttons[0]:
                return color_check, speed_check 
        elif x1 >= back_pos[0] and x1 <= back_pos[0] + back_size[0] \
            and y1 >= back_pos[1] and y1 <= back_pos[1] + back_size[1]:
            level_window.blit(back1, back_pos)
            if buttons[0]:
                return 0, 0
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
    # 返回难度情况，给showNewGame作为参数传入

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
    gravity_timer_text = gravity_timer_text_font.render("距离下次重力反转还有：", True, gravity_timer_text_color)
    gravity_timer_text_amount = gravity_timer_text_font.render(str(round(gravity_timer, 1)) + " s", True, gravity_timer_text_color)
    
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
    slot_width = ai_settings.slot_width
    for i in range(int(screen_size[0]/slot_width) + 1):
        slots.append(classfile.Slot(screen_size, 84, 600))
        slots[i].top_slot_rect[0] = slot_width * i
        slots[i].bottom_slot_rect[0] = slot_width * i

    # 显示难度信息
    level_option_font = pygame.font.Font(os.path.join(filepath, "fonts/ARLRDBD.ttf"), 18)
    v3color = level_option_font.render("Three Color", True, (0,0,0))
    v5color = level_option_font.render("Five Color", True, (0,0,0))
    v7color = level_option_font.render("Seven Color", True, (0,0,0))
    SpeedLow = level_option_font.render("Low Speed", True, (0,0,0))
    SpeedMid = level_option_font.render("Middle Speed", True, (0,0,0))
    SpeedHig = level_option_font.render("High Speed", True, (0,0,0))
    color_levels = (v3color, v5color, v7color)
    speed_levels = (SpeedLow, SpeedMid, SpeedHig)
    
    color_choice = color_levels[color_check - 1]
    speed_choice = speed_levels[speed_check - 1]

    # 初始化Biofilm
    biofilm_top_timer_limit = ai_settings.top_timer_limit
    biofilm_bottom_timer_limit = ai_settings.bottom_timer_limit
    biofilm_timer = random.randint(biofilm_bottom_timer_limit, biofilm_top_timer_limit)
    biofilm_form = 0

    # 初始化Bomb: Macrophage
    bomb_top_timer_limit = ai_settings.bomb_up_limit
    bomb_bottom_timer_limit = ai_settings.bomb_down_limit
    bomb_timer = random.randint(bomb_bottom_timer_limit, bomb_top_timer_limit)
    bomb_form = 0

    screen_size = screen.get_size()
    game_window = pygame.Surface(screen_size)
    game_window = game_window.convert()
    game_window.fill((238, 230, 133))

    ball_color_order = ai_settings.ball_color_order[:(2*color_check + 1)]
    num_of_color = len(ball_color_order)
    current_ball_color = 0
    if speed_check == 1:
        speed_limit = ai_settings.ball_speed_limit_low
    elif speed_check == 2:
        speed_limit = ai_settings.ball_speed_limit_mid
    elif speed_check == 3:
        speed_limit = ai_settings.ball_speed_limit_hig 

    ball = classfile.Ball()
    biofilm_queue = []
    bomb_queue = []

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
                    ball.ball_surface = ball.ball_surface_dict[ball.color]
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
        gravity, gravity_timer, gravity_direction = environment.updateGravity(gravity, gravity_direction, gravity_timer, dt)
        total_gravity = gravity + curr_force
        gravity_timer_amount = gravity_timer_text_font.render(str(round(gravity_timer, 1)) + " s", True, gravity_timer_text_color)

        # 判断ball穿膜
        colli_film_color = "white"
        for biofilm in biofilm_queue:
            if ball.ball_rect[0] + ai_settings.ball_size[0] == biofilm.film_rect[0]:
                score += 10
                if biofilm.film_color == "white":
                    after_ball_color = ball.color
                    while ball.color == after_ball_color:
                        ball.color = ball_color_order[random.randint(0, num_of_color - 1)]
                    ball.ball_surface = ball.ball_surface_dict[ball.color]
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
            biofilm.film_rect[0] -= ai_settings.film_speed
        for bomb in bomb_queue:
            bomb.bomb_rect[0] -= ai_settings.bomb_speed

        # 更新slots和分数
        flag = (flag + 1) % slot_width
        if flag % 8 == 0:
            for slot in slots:
                slot.top_slot_rect[0] -= 8
                slot.bottom_slot_rect[0] -= 8
        if flag == 0:
            slots.pop(0)
            last_slot = slots[-1]
            # print(last_slot.level, last_slot.height)
            slots.append(classfile.Slot(screen_size, last_slot.level, last_slot.height))
            score += 1
            score_text = score_text_font.render("Score: " + str(score), True, (0, 0, 0))

        temp_slot = slots[-1]
        # 随机生成Biofilm
        biofilm_form, biofilm_timer = environment.generateBiofilm(biofilm_timer, dt, biofilm_bottom_timer_limit, biofilm_top_timer_limit)
        if biofilm_form == 1:
            biofilm_queue.append(classfile.Biofilm(color_check, temp_slot.height, screen_size[1] - temp_slot.level - temp_slot.height))
            biofilm_form = 0

        # 删除出屏Biofilm
        if len(biofilm_queue) > 0 and biofilm_queue[0].film_rect[0] <= 0:
            biofilm_queue.pop(0)
    
        # 出现bomb: macrophage
        bomb_size = ai_settings.bomb_size
        bomb_safe_distance = ai_settings.bomb_safe_distance
        bomb_form, bomb_timer, bomb_pos = environment.generateBomb(bomb_timer, dt, bomb_bottom_timer_limit, bomb_top_timer_limit, temp_slot.height, screen_size[1] - temp_slot.level - temp_slot.height, bomb_size, bomb_safe_distance)
        if bomb_form == 1 and bomb_pos != (0, 0):
            bomb_queue.append(classfile.Bomb(bomb_pos))
            bomb_form = 0
        
        # 删除出屏bomb
        if len(bomb_queue) > 0 and bomb_queue[0].bomb_rect[0] <= 0:
            bomb_queue.pop(0)

        # 检查死亡：位置+颜色+炸弹
        if environment.checkDead(colli_film_color, screen_size[0], ball, slots, bomb_queue):
            return score

        # 刷新屏幕
        game_window.fill((238, 230, 133))
        for slot in slots:
            game_window.blit(slot.top_slot_surface, slot.top_slot_rect)
            game_window.blit(slot.bottom_slot_surface, slot.bottom_slot_rect)
        game_window.blit(ball.ball_surface, ball.ball_rect)
        for biofilm in biofilm_queue:
            game_window.blit(biofilm.film_surface, biofilm.film_rect)
        for bomb in bomb_queue:
            game_window.blit(bomb.bomb_surface, bomb.bomb_rect)
        game_window.blit(gravity_timer_text, (20, 20))
        game_window.blit(gravity_timer_amount, (235, 20))
        game_window.blit(gravity_indicator, (20, 80))
        game_window.blit(gravity_status[gravity_direction], (150, 60))
        game_window.blit(score_text, (450, 20))
        game_window.blit(color_choice, (700, 20))
        game_window.blit(speed_choice, (850, 20))
        screen.blit(game_window, (0, 0))
        pygame.display.update()
    
    return score

def showScore(screen, score):

    screen_size = screen.get_size()
    score_window = pygame.Surface(screen_size)
    score_window = score_window.convert()
    score_window.fill(ai_settings.game_bg_color)

    (score_title, score_text, back, back1, again, again1) = text.getScoreText(score)

    back_size = back.get_size()
    again_size = again.get_size()
    back_pos = (612, 640)
    again_pos = (412 - again_size[0], 640)

    while True:
        buttons = pygame.mouse.get_pressed()
        x1, y1 = pygame.mouse.get_pos()
        if x1 >= again_pos[0] and x1 <= again_pos[0] + again_size[0] \
            and y1 >= again_pos[1] and y1 <= again_pos[1] + again_size[1]:
            score_window.blit(again1, again_pos)
            if buttons[0]:
                return True
        elif x1 >= back_pos[0] and x1 <= back_pos[0] + back_size[0] \
            and y1 >= back_pos[1] and y1 <= back_pos[1] + back_size[1]:
            score_window.blit(back1, back_pos)
            if buttons[0]:
                return False
        else:
            score_window.blit(again, again_pos)
            score_window.blit(back, back_pos)

        score_window.blit(score_title, (((screen_size[0] - score_title.get_size()[0])/2, 50)))
        score_window.blit(score_text, (((screen_size[0] - score_text.get_size()[0])/2, 360)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(score_window, (0, 0))
        pygame.display.update()


def showGame(screen):
    while True:
        color_check, speed_check = setLevel(screen)
        game_state = True
        if color_check == 0 or speed_check == 0:
            break
        else:
            while game_state:
                score = showNewGame(screen, color_check, speed_check)
                game_state = showScore(screen, score)
            
        '''
        go_to_welcome = showScore(screen, score)
        if go_to_welcome:
            break
        '''