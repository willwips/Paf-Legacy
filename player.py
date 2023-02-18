# importation
import sys
import pygame

# initialisation des variables
pos = [0, 0]

move_right = False
move_left = False
move_up = False
move_down = False
is_movement = 0


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
    if move_up:
        pos[1] += 2
    if move_down:
        pos[1] -= 2
    if move_left:
        pos[0] -= 2
    if move_right:
        pos[0] += 2
