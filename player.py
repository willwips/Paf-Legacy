# importation
import sys
import pygame
import ennemy
import graphic_main
import weapon

# initialisation des variables
pos = [0, 0]

move_right = False
move_left = False
move_up = False
move_down = False
last_move_is_right = False
last_move_is_left = True
last_move_is_up = False
last_move_is_down = False
is_movement = 0
pv = 100
pv_max = 120
strength = 10
resistance = 0.1
cooldown = 0
cooldown_move = 0


# boucle permettant de bouger le personage
def boucle():
    global pos
    global move_down
    global move_right
    global move_up
    global move_left
    global is_movement
    global pv
    global cooldown
    global cooldown_move
    global last_move_is_down
    global last_move_is_left
    global last_move_is_right
    global last_move_is_up
    old_pos = pos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_z:
                move_down = True
                last_move_is_right = False
                last_move_is_left = False
                last_move_is_up = False
                last_move_is_down = True
                is_movement += 1
                graphic_main.frame = graphic_main.frame_back
            if event.key == pygame.K_s:
                move_up = True
                is_movement += 1
                graphic_main.frame = graphic_main.frame_front
                last_move_is_right = False
                last_move_is_left = False
                last_move_is_up = True
                last_move_is_down = False
            if event.key == pygame.K_d:
                move_right = True
                is_movement += 1
                graphic_main.frame = graphic_main.frame_R
                last_move_is_right = True
                last_move_is_left = False
                last_move_is_up = False
                last_move_is_down = False
            if event.key == pygame.K_q:
                move_left = True
                is_movement += 1
                graphic_main.frame = graphic_main.frame_L
                last_move_is_right = False
                last_move_is_left = True
                last_move_is_up = False
                last_move_is_down = False
            if event.key == pygame.K_a:
                weapon.is_attacking = True

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
    if cooldown_move < 0:
        if move_up:
            pos[1] += 2
        if move_down:
            pos[1] -= 2
        if move_left:
            pos[0] -= 2
        if move_right:
            pos[0] += 2
    if collision_with_wall():
        if move_up:
            pos[1] -= 2
        if move_down:
            pos[1] += 2
        if move_left:
            pos[0] += 2
        if move_right:
            pos[0] -= 2

    if collision_with_ennemy_1():

        if cooldown <= 0:
            pv -= 20 - 20 * resistance
            cooldown = 60

            cooldown_move = 0
    if collision_with_ennemy_2_1():

        if cooldown <= 0:
            pv -= 20 - 20 * resistance
            cooldown = 60

            cooldown_move = 0

    if collision_with_projectile():
        if cooldown <= 0:
            pv -= 20 - 20 * resistance
            cooldown = 60
            cooldown_move = 0
    if pv <= 0:
        sys.exit()

    cooldown -= 1
    cooldown_move -= 1
    if cooldown > 0 and cooldown % 20 == 10:
        if last_move_is_up:
            graphic_main.frame = graphic_main.frame_front_wounded
        if last_move_is_down:
            graphic_main.frame = graphic_main.frame_back_wounded
        if last_move_is_left:
            graphic_main.frame = graphic_main.frame_L_wounded
        if last_move_is_right:
            graphic_main.frame = graphic_main.frame_R_wounded
    if cooldown >= 0 and cooldown % 20 == 0:
        if last_move_is_up:
            graphic_main.frame = graphic_main.frame_front
        if last_move_is_down:
            graphic_main.frame = graphic_main.frame_back
        if last_move_is_left:
            graphic_main.frame = graphic_main.frame_L
        if last_move_is_right:
            graphic_main.frame = graphic_main.frame_R


def collision_with_wall():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=(pos[0] + 15, pos[1] + 25))
    if rectA.left < 0:
        pos[0] += 10
        return True
    if rectA.right > pygame.display.get_surface().get_size()[0]:
        pos[0] -= 10
        return True
    if rectA.top < 0:
        pos[1] += 10
        return True
    if rectA.bottom > pygame.display.get_surface().get_size()[1]:
        pos[1] -= 10
        return True
    return False


def collision_with_ennemy_1():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 40
    rectA.w = 15
    rectA.center = (pos[0] + 15, pos[1] + 25)
    collision = False
    for i in ennemy.enemy_1_list:
        rectB = i[0].get_rect(center=i[1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (i[1][0] + 15, i[1][1] + 25)
        collision = True
        if rectB.right < rectA.left:
            collision = False
        if rectB.bottom < rectA.top:
            collision = False
        if rectB.left > rectA.right:
            collision = False
        if rectB.top > rectA.bottom:
            collision = False
        if collision:
            if i[4][0] == True:
                pos[0] -= 10
            if i[4][1] == True:
                pos[0] += 10
            if i[4][2] == True:
                pos[1] += 10
            if i[4][3] == True:
                pos[1] -= 10
            return collision


def collision_with_ennemy_2_1():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 40
    rectA.w = 15
    rectA.center = (pos[0] + 15, pos[1] + 25)
    collision = False
    for i in ennemy.enemy_2_1_list:
        rectB = i[0].get_rect(center=i[1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (i[1][0] + 15, i[1][1] + 25)
        collision = True
        if rectB.right < rectA.left:
            collision = False
        if rectB.bottom < rectA.top:
            collision = False
        if rectB.left > rectA.right:
            collision = False
        if rectB.top > rectA.bottom:
            collision = False
        if collision:
            if i[4][0] == True:
                pos[0] -= 10
            if i[4][1] == True:
                pos[0] += 10
            if i[4][2] == True:
                pos[1] += 10
            if i[4][3] == True:
                pos[1] -= 10
            return collision

def collision_with_projectile():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 70
    rectA.w = 30
    rectA.center = (pos[0] + 15, pos[1] + 25)

    n = 0
    for i in ennemy.projectile_list:
        rectB = pygame.draw.circle(graphic_main.screen, (0, 0, 0), i[0], i[1], -1)
        collision = True
        if rectB.right < rectA.left:
            collision = False
        if rectB.bottom < rectA.top:
            collision = False
        if rectB.left > rectA.right:
            collision = False
        if rectB.top > rectA.bottom:
            collision = False
        if collision:
            del ennemy.projectile_list[n]
            return collision
        n += 1
def showpv():
    global pv
    w, h = pygame.display.get_surface().get_size()
    widht = 0.3
    height = 0.05
    life_red = pygame.Rect(w / 2 - (widht * w) / 2, h - 0.1 * h, widht * w, height * h)
    rectA = pygame.draw.rect(graphic_main.screen, (255, 0, 0), life_red)
    life_black = pygame.Rect(w / 2 - (widht * w) / 2 + widht * w - (widht * w - widht * w * pv / pv_max), h - 0.1 * h,
                             widht * w - widht * w * pv / pv_max + 1, height * h)
    rectB = pygame.draw.rect(graphic_main.screen, (0, 0, 0), life_black)
    return rectA, rectB
