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
    return gravity, timer, gravity_direction

def generateBiofilm(timer, dt, film_lambda):
    """
    Function to generate a biofilm with random color
    on the right most side of the map. 
    """
    timer -= dt
    if timer <= 0:
        time_slot = random.expovariate(film_lambda)
        if time_slot < 2:
            timer = 2
        elif time_slot > 8:
            timer = 8
        else:
            timer = time_slot
        biofilm_form = 1
    else:
        biofilm_form = 0
    return biofilm_form, timer

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