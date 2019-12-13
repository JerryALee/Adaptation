import pygame

def convertColor(color_string):
    color_dict = {"red": (255, 0, 0), "yellow": (255, 255, 0), "green": (0, 255, 0), "blue": (0, 0, 255), "purple": (255, 0, 255)}
    return color_dict[color_string]