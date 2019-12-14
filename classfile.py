import pygame
import environment

class Ball(object):
    
    def __init__(self):
        self.ball_rect = pygame.Rect(492, 364, 40, 40)
        self.ball_surface = pygame.Surface((40, 40))
        self.color = "red"
        self.ball_surface.fill(pygame.Color(self.color))
        self.left = 0 # 0 or -1
        self.right = 0 # 0 or 1
        self.speed = 0
    
    def checkDead(self, window_size):
        if self.ball_rect.left <= 0 or self.ball_rect.right >= window_size[0] \
            or self.ball_rect.top <= 0 or self.ball_rect.bottom >= window_size[1]:
            return True
        else:
            return False

class Slot(object):

    def __init__(self):
        self.name = "map slot"
class Biofilm(object):
    def __init__(self):
        self.name = "biofilm"
