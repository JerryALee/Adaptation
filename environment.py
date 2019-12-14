import pygame
import random

def updateGravity(gravity, timer, dt):
    timer -= dt
    if timer <= 0:
        timer = 5 + random.expovariate(1/5)
        gravity = -gravity
    if gravity > 0:
        gravity_direction = 1 # 重力向下
    else:
        gravity_direction = 0 # 重力向上
    return gravity, timer, gravity_direction

def generateBiofilm(timer,dt,film_lambda):
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

def checkDead(screen_size, ball, slots):
    pos_left = ball.ball_rect.left
    pos_right = ball.ball_rect.right
    for i in range(int(pos_left/32), int(pos_right/32) + 1):
        if ball.ball_rect.top <= slots[i].top_slot_rect.bottom or ball.ball_rect.bottom >= slots[i].bottom_slot_rect.top:
            return True
    if pos_left <= 0 or pos_right >= screen_size[0]:
        return True
    return False