import pygame
import random
import settings

ai_settings = settings.Settings()

def updateGravity(gravity, gravity_direction, timer, dt):
    timer -= dt
    if timer <= 0:
        timer = random.randint(5, 20)
        gravity = -gravity
        gravity_direction = (gravity_direction + 1) % 2
    '''if gravity > 0:
        gravity_direction = 1 # 重力向下
    else:
        gravity_direction = 0 # 重力向上'''
    return gravity, timer, gravity_direction

def generateBiofilm(timer, dt, bottom_limit, top_limit):
    """
    Function to generate a biofilm with random color
    on the right most side of the map. 
    """
    timer -= dt
    if timer <= 0:
        timer = random.randint(bottom_limit, top_limit)
        biofilm_form = 1
    else:
        biofilm_form = 0
    return biofilm_form, timer

def generateBomb(timer, dt, bottom_limit, top_limit, height, upperbound, size, safe_distance):
    """
    Function to generate a macrophage as a bomb at 
    random position on the right most side of the map. 
    """
    timer -= dt
    if timer <= 0:
        timer = random.randint(bottom_limit, top_limit)
        bomb_pos = (1024, random.randint(upperbound + safe_distance, upperbound + height - size[1] - safe_distance))
        bomb_form = 1
    else:
        bomb_pos = (0, 0)
        bomb_form = 0
    return bomb_form, timer, bomb_pos

def checkDead(film_color, screen_width, ball, slots):
    pos_left = ball.ball_rect.left
    pos_right = ball.ball_rect.right
    for i in range(int(pos_left/ai_settings.slot_width), int(pos_right/ai_settings.slot_width) + 1):
        if ball.ball_rect.top <= slots[i].top_slot_rect.bottom or ball.ball_rect.bottom >= slots[i].bottom_slot_rect.top:
            return True
    if pos_left <= 0 or pos_right >= screen_width:
        return True

    # 判断ball穿膜
    if film_color != "white" and ball.color != film_color:
        return True

    return False