import pygame
import sys
import random

import text

def showAuthor(window):
    window_size = window.get_size()
    author_window = pygame.Surface(window_size)
    author_window = author_window.convert()
    author_window.fill((178, 233, 238))

    back_pos = (850, 650)
    (hmc, lcr, htq, wsn, jby, back, back1) = text.getAuthorText()
    author_font_size = hmc.get_size()
    back_font_size = back.get_size()
    author_window.blit(hmc, ((window_size[0] - author_font_size[0])/2, 100))
    author_window.blit(lcr, ((window_size[0] - author_font_size[0])/2, 150))
    author_window.blit(htq, ((window_size[0] - author_font_size[0])/2, 200))
    author_window.blit(wsn, ((window_size[0] - author_font_size[0])/2, 250))
    author_window.blit(jby, ((window_size[0] - author_font_size[0])/2, 300))
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
        window.blit(author_window, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("退出游戏…")
                sys.exit()

def showIntro(window):
    window_size = window.get_size()
    intro_window = pygame.Surface(window_size)
    intro_window = intro_window.convert()
    intro_window.fill((178, 233, 238))

    back_pos = (850, 650)
    (intro, back, back1) = text.getIntroText()
    intro_font_size = intro.get_size()
    back_font_size = back.get_size()
    intro_window.blit(intro, ((window_size[0] - intro_font_size[0])/2, 100))
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
        window.blit(intro_window, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("退出游戏…")
                sys.exit()

def showGame(window):
    while True:
        background = pygame.image.load('./images/background.png').convert_alpha()
        window.blit(background, (100, 100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("退出游戏…")
                sys.exit()