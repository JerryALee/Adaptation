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
