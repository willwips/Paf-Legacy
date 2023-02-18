# importation
import sys
import pygame
import ennemy
import graphic_main

# initialisation des variables
pos = [0, 0]

move_right = False
move_left = False
move_up = False
move_down = False
is_movement = 0
pv = 100


# boucle permétant de bougé le personage
def boucle():
    global pos
    global move_down
    global move_right
    global move_up
    global move_left
    global is_movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_z:
                move_down = True
                is_movement += 1
            if event.key == pygame.K_s:
                move_up = True
                is_movement += 1

            if event.key == pygame.K_d:
                move_right = True
                is_movement += 1

            if event.key == pygame.K_q:
                move_left = True
                is_movement += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                move_down = False
                is_movement -= 1

            if event.key == pygame.K_s:
                move_up = False
                is_movement -= 1
            if event.key == pygame.K_d:
                move_right = False
                is_movement -= 1
            if event.key == pygame.K_q:
                move_left = False
                is_movement -= 1
    if not collision_with_ennemy_1():
        if move_up:
            pos[1] += 2
        if move_down:
            pos[1] -= 2
        if move_left:
            pos[0] -= 2
        if move_right:
            pos[0] += 2
    if collision_with_ennemy_1():
        if move_up:
            pos[1] -= 2
        if move_down:
            pos[1] += 2
        if move_left:
            pos[0] += 2
        if move_right:
            pos[0] -= 2


def collision_with_ennemy_1():
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 40
    rectA.w = 15
    rectA.center = pos

    for i in ennemy.enemy_1_list:
        rectB = i[0].get_rect(center=i[1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = i[1]
        if rectB.right < rectA.left:
            return False
        if rectB.bottom < rectA.top:
            return False
        if rectB.left > rectA.right:
            return False
        if rectB.top > rectA.bottom:
            return False
        return True
