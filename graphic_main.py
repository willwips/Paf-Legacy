import time

import pygame
import sys

screen = None
frame = None



def initialisation(full_screen=False):
    pygame.init()
    global screen
    if full_screen:
        screen = pygame.display.set_mode((300, 200), flags=pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((300, 200))

    return screen


current = 0


def boucle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    global frame
    global current
    global screen
    screen.fill((0, 0, 0))
    screen.blit(frame[current], frame[current].get_rect())
    time.sleep(0.1)
    pygame.display.flip()
    current += 1
    current = current%4


def import_character_picture():
    player1 = pygame.image.load('picture/character/player1.png').convert()
    player2 = pygame.image.load('picture/character/player2.png').convert()
    player3 = pygame.image.load('picture/character/player3.png').convert()
    global frame
    frame = [player1, player2, player1, player3]
    return frame
