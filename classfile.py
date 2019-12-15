import pygame
import random
import environment
import settings

ai_settings = settings.Settings()

class Ball(object):
    
    def __init__(self, ai_settings):
        self.ball_size = ai_settings.ball_size
        self.ball_pos = ai_settings.ball_iniPos
        self.ball_rect = pygame.Rect(self.ball_pos+self.ball_size)
        self.ball_surface = pygame.Surface(self.ball_size)
        self.color = ai_settings.ball_iniCol
        self.ball_surface.fill(pygame.Color(self.color))
        self.left = ai_settings.ball_left
        self.right = ai_settings.ball_right
        self.speed = ai_settings.ball_speed

class Slot(object):

    def __init__(self, screen_size, prev_slot_level, prev_slot_height):
        self.level = prev_slot_level + 10 * random.randint(-1, 1)
        if self.level <= 0:
            self.level = 10
        elif self.level >= screen_size[1] - 600:
            self.level = screen_size[1] - 610
        self.height = prev_slot_height + 10 * random.randint(-3, 3)
        if self.height <= 400:
            self.height = 410
        elif self.height >= 600:
            self.height = 590
        self.bottom_slot_rect = pygame.Rect(screen_size[0], screen_size[1] - self.level, ai_settings.slot_width, self.level)
        self.bottom_slot_surface = pygame.Surface((ai_settings.slot_width, self.level))
        self.bottom_slot_surface.fill((192, 192, 192))
        self.top_slot_rect = pygame.Rect(screen_size[0], 0, ai_settings.slot_width, screen_size[1] - self.level - self.height)
        self.top_slot_surface = pygame.Surface((ai_settings.slot_width, screen_size[1] - self.level - self.height))
        self.top_slot_surface.fill((192, 192, 192))
        
    def updateSlot(self):
        self.bottom_slot_rect[0] -= 1
        self.top_slot_rect[0] -= 1

        
class Biofilm(object):
    def __init__(self, color_check):
        self.name = "biofilm"
        self.film_pos = ai_settings.film_iniPos
        self.film_rect = pygame.Rect((self.film_pos, 0) + ai_settings.film_size)
        self.film_surface = pygame.Surface(ai_settings.film_size)
        self.film_color_order = ai_settings.color_order[:(2*color_check+1)]+["white"]
        self.film_color = self.film_color_order[random.randint(0,len(self.film_color_order) - 1)]
        self.film_surface.fill(pygame.Color(self.film_color))
        self.film_speed = ai_settings.film_speed
        