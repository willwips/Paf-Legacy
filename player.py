import sys

import pygame

pos = [0, 0]

move_right = False
move_left = False
move_up = False
move_down = False


def boucle():
    global pos
    global move_down
    global move_right
    global move_up
    global move_left
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                move_down = True
            if event.key == pygame.K_s:
                move_up = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_q:
                move_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                move_down = False
            if event.key == pygame.K_s:
                move_up = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_q:
                move_left = False
    if move_up:
        pos[1] += 1
    if move_down:
        pos[1] -= 1
    if move_left:
        pos[0] -= 1
    if move_right:
        pos[0] += 1
