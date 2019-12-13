import pygame
import environment

class Ball(object):
    
    def __init__(self):
        self.ball_rect = pygame.Rect(492, 364, 40, 40)
        self.ball_surface = pygame.Surface((40, 40))
        self.color = "red"
        self.ball_surface.fill(environment.convertColor(self.color))
        self.left = 0 # 0 or -1
        self.right = 0 # 0 or 1
        self.gravity = 0.055
        self.speed = 0