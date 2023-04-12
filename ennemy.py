import math
import random

import pygame

import graphic_main
import player
import world

enemy_1_list = []
enemy_1_2_list = []
enemy_2_1_list = []
enemy_2_2_list = []
enemy_3_1_list = []

boss_list = []
projectile_list = []
enemy_slime_list = []
enemy_4_1_list = []
enemy_4_2_list = []
boss_list_4 = []

def spawn_enemy_2_1(pos, img, pv):
    img_ = []
    n = 0
    for i in img:

        if n % 3 == 2:
            img_.append(pygame.transform.scale(pygame.image.load(i).convert_alpha(), [40, 40]))
        else:
            img_.append(pygame.transform.scale(pygame.image.load(i).convert_alpha(), [25, 49]))
        n += 1
    pos = pos
    global enemy_2_1_list
    enemy_2_1_list.append([img_, pos, pv, 10, [False, False, False, False], [0, 0], False, 10, 0])

def spawn_enemy_3_1(pos, img, pv):
    img_ = [pygame.image.load(img[i]).convert_alpha() for i in range(2)]
    proj_1 = pygame.image.load('picture/enemy/star/proj_star_1.png')
    proj_2 = pygame.image.load('picture/enemy/star/proj_star_2.png')

    pos = pos
    global enemy_3_1_list
    enemy_3_1_list.append([img_, pos, pv, 10, [False, False, False, False], [0, 0], False, 10, 0, [proj_1, proj_2, pygame.transform.rotate(proj_1, 90), pygame.transform.rotate(proj_2, 90), pygame.transform.rotate(proj_1, 180), pygame.transform.rotate(proj_2, 180), pygame.transform.rotate(proj_1, -90), pygame.transform.rotate(proj_2, -90)]])
def spawn_enemy_2_2(pos, img, pv):
    img_ = []
    n = 0
    for i in img:

        img_.append(pygame.image.load(i).convert_alpha())

        n += 1
    pos = pos
    global enemy_2_2_list
    enemy_2_2_list.append([img_, pos, pv, 10, [False, False, False, False], [0, 0], False, 10, [0, 0]])
def spawm_projectile(pos, radius, directon, color, img = None):
    global projectile_list
    projectile_list.append([pos, radius, directon, color, img])


def spawn_enemy_1(pos, img, pv):
    img = pygame.transform.scale(pygame.image.load(img).convert_alpha(), [28, 50])
    pos = pos
    global enemy_1_list
    enemy_1_list.append([img, pos, pv, 10, [False, False, False, False], [0, 0]])


def spawn_enemy_1_2(pos, img, pv):
    _img = []
    for i in img:
        _img.append(pygame.transform.scale(pygame.image.load(i).convert_alpha(), [49, 23]))
    pos = pos
    global enemy_1_2_list
    enemy_1_2_list.append([_img, pos, pv, 10, [False, False, False, False], [0, 0], [0, 0], 0, 0])


def spawn_boss_1(pos, pv):
    _img = []
    _img.append(pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p1_L.png'), [46, 80]))
    _img.append(pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p1_R.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p1_to_p2_L.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p1_to_p2_R.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_1_L_1.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_1_L_2.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_1_L_3.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_1_R_1.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_1_R_2.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_1_R_3.png'), [46, 80]))

    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_2_L_1.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_2_L_2.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_2_L_3.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_2_R_1.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_2_R_2.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_2_R_3.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_to_p3_1.png'), [60, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_to_p3_2.png'), [70, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_to_p3_3.png'), [85, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_to_p3_4.png'), [80, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_to_p3_5.png'), [92, 80]))
    boss_list.append([_img, pos, pv, [False, False, False, False], 0, 0, 0, [0, 0], 0, [0, 0], 0])


def spawn_boss_4(pos, pv):
    _img = []
    _img.append(pygame.image.load('picture/enemy/tortue/Boss_tortue_1.png'))
    """    _img = []
    _img.append(pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p1_L.png'), [46, 80]))
    _img.append(pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p1_R.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p1_to_p2_L.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p1_to_p2_R.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_1_L_1.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_1_L_2.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_1_L_3.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_1_R_1.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_1_R_2.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_1_R_3.png'), [46, 80]))

    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_2_L_1.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_2_L_2.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_2_L_3.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_2_R_1.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_2_R_2.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_2_R_3.png'), [46, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_to_p3_1.png'), [60, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_to_p3_2.png'), [70, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_to_p3_3.png'), [85, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_to_p3_4.png'), [80, 80]))
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Dark_shadow/Dark_shadow_p2_to_p3_5.png'), [92, 80]))"""
    boss_list_4.append([_img, pos, pv, [False, False, False, False], 0, 0, 0, [0, 0], 0, [0, 0], 0])

def spawn_enemy_slime(pos, img, pv):
    img = pygame.image.load(img).convert_alpha()
    pos = pos
    global enemy_slime_list
    enemy_slime_list.append([img, pos, pv, 10, [False, False, False, False], [0, 0]])
def spawn_enemy_4_1(pos, img, pv):
    n = 0
    img = pygame.transform.scale(pygame.image.load(img).convert_alpha(), [40, 40])

    pos = pos
    global enemy_4_1_list
    enemy_4_1_list.append([img, pos, pv, 10, [False, False, False, False], [0, 0], False, 10, 0])

def spawn_enemy_4_2(pos, img, pv):
    n = 0
    _img = []
    _img.append(pygame.transform.scale(pygame.image.load(img).convert_alpha(), [40, 40]))
    _img.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(img).convert_alpha(), [40, 40]), True, False))

    pos = pos
    global enemy_4_2_list
    enemy_4_2_list.append([_img, pos, pv, 10, [False, False, False, False], [0, 0], False, 10, 0])
def boucle():
    global enemy_1_list
    global enemy_2_1_list

    n = 0
    move_ennemi_1()
    move_ennemi_2_1()
    move_ennemi_2_2()
    move_ennemi_1_2()
    move_ennemi_3_1()
    move_projectile()
    move_boss_1()
    move_ennemi_slime()
    move_ennemi_4_1()
    move_ennemi_4_2()
    move_boss_4()
    for i in enemy_1_list:
        if i[3] > 0:
            enemy_1_list[n][3] -= 1
        n += 1
    n = 0
    for i in enemy_1_2_list:
        if i[3] > 0:
            enemy_1_2_list[n][3] -= 1
        n += 1
    n = 0
    for i in enemy_2_1_list:
        if i[3] > 0:
            enemy_2_1_list[n][3] -= 1
        enemy_2_1_list[n][7] -= 1
        n += 1
    n = 0
    for i in enemy_3_1_list:
        if i[3] > 0:
            enemy_3_1_list[n][3] -= 1
        enemy_3_1_list[n][7] -= 1
        n += 1
    n = 0
    for i in enemy_2_2_list:
        if i[3] > 0:
            enemy_2_2_list[n][3] -= 1
        enemy_2_2_list[n][7] -= 1
        n += 1
    n = 0
    for i in boss_list:
        if i[6] > 0:
            boss_list[n][6] -= 1
        if i[8] > 0:
            boss_list[n][8] -= 1
        n += 1
    n = 0
    for i in enemy_slime_list:
        if i[3] > 0:
            enemy_slime_list[n][3] -= 1
        n += 1
    n = 0
    for i in enemy_4_1_list:
        if i[3] > 0:
            enemy_4_1_list[n][3] -= 1
        enemy_4_1_list[n][7] -= 1
        n += 1
    n = 0
    for i in enemy_4_2_list:
        if i[3] > 0:
            enemy_4_2_list[n][3] -= 1
        enemy_4_2_list[n][7] -= 1
        n += 1

    n = 0
    for i in boss_list_4:
        if i[6] > 0:
            boss_list_4[n][6] -= 1
        if i[8] > 0:
            boss_list_4[n][8] -= 1
        boss_list_4[n][5] -= 1

        n += 1
def test_collision__ennemy_1(rect, index=-1):
    n = 0
    for i in enemy_1_list:
        if n != index:
            rectB = i[0].get_rect(center=i[1])
            rectB.h = 40
            rectB.w = 15
            rectB.center = (i[1][0] + 15, i[1][1] + 25)
            if rectB.colliderect(rect):
                return True

        n += 1


def is_touch_wall(pos, size):
    if pos[0] < graphic_main.left + 50:
        return True
    if pos[1] < graphic_main.top + 50:
        return True
    if pos[0] + size[0] > graphic_main.right - 50:
        return True
    if pos[1] + size[1] > graphic_main.bottom - 50:
        return True

    return False


def touch_wall(pos, size):
    if pos[0] < graphic_main.left + 50:
        pos[0] += 10
    if pos[1] < graphic_main.top + 50:
        pos[1] += 10
    if pos[0] + size[0] > graphic_main.right - 50:
        pos[0] -= 10
    if pos[1] + size[1] > graphic_main.bottom - 50:
        pos[1] -= 10

    return pos


def move_ennemi_1():
    global enemy_1_list
    for i in range(0, len(enemy_1_list)):
        rectB = enemy_1_list[i][0].get_rect(center=enemy_1_list[i][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (enemy_1_list[i][1][0] + 15, enemy_1_list[i][1][1] + 25)
        dist = math.sqrt((enemy_1_list[i][1][0] - player.pos[0]) ** 2 + (enemy_1_list[i][1][1] - player.pos[1]) ** 2)
        enemy_1_list[i][4][0] = False
        enemy_1_list[i][4][1] = False
        enemy_1_list[i][4][2] = False
        enemy_1_list[i][4][3] = False
        enemy_1_list[i][1] = touch_wall(enemy_1_list[i][1], enemy_1_list[i][0].get_rect())
        if enemy_1_list[i][3] % 2 == 0 and enemy_1_list[i][3] > 0:
            enemy_1_list[i][1][0] += enemy_1_list[i][5][0]
        if 15 < dist <= 200:
            if (enemy_1_list[i][1][0] - player.pos[0]) >= 0:
                enemy_1_list[i][1][0] -= abs((enemy_1_list[i][1][0] - player.pos[0]) / (
                        abs(enemy_1_list[i][1][1] - player.pos[1]) + abs((enemy_1_list[i][1][0] - player.pos[0]))))
                enemy_1_list[i][4][0] = True
            elif (enemy_1_list[i][1][0] - player.pos[0]) <= 0:
                enemy_1_list[i][1][0] += abs((enemy_1_list[i][1][0] - player.pos[0]) / (
                        abs(enemy_1_list[i][1][1] - player.pos[1]) + abs(enemy_1_list[i][1][0] - player.pos[0])))
                enemy_1_list[i][4][1] = True
            if (enemy_1_list[i][1][1] - player.pos[1]) >= 0:
                enemy_1_list[i][1][1] -= abs((enemy_1_list[i][1][1] - player.pos[1]) / (
                        abs(enemy_1_list[i][1][1] - player.pos[1]) + abs(enemy_1_list[i][1][0] - player.pos[0])))
                enemy_1_list[i][4][2] = True
            elif (enemy_1_list[i][1][1] - player.pos[1]) <= 0:
                enemy_1_list[i][1][1] += abs((enemy_1_list[i][1][1] - player.pos[1]) / (
                        abs(enemy_1_list[i][1][1] - player.pos[1]) + abs(enemy_1_list[i][1][0] - player.pos[0])))
                enemy_1_list[i][4][3] = True


def move_ennemi_1_2():
    global enemy_1_2_list
    for i in range(0, len(enemy_1_2_list)):
        rectB = enemy_1_2_list[i][0][enemy_1_2_list[i][8]].get_rect(center=enemy_1_2_list[i][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (enemy_1_2_list[i][1][0] + 15, enemy_1_2_list[i][1][1] + 25)
        dist = math.sqrt(
            (enemy_1_2_list[i][1][0] - player.pos[0]) ** 2 + (enemy_1_2_list[i][1][1] - player.pos[1]) ** 2)
        enemy_1_2_list[i][4][0] = False
        enemy_1_2_list[i][4][1] = False
        enemy_1_2_list[i][4][2] = False
        enemy_1_2_list[i][4][3] = False

        # if is_touch_wall(enemy_1_2_list[i][1], enemy_1_2_list[i][0][enemy_1_2_list[i][8]].get_rect()) or \
        #         enemy_1_2_list[i][6] == [0, 0]:

        if is_touch_wall(enemy_1_2_list[i][1],  enemy_1_2_list[i][0][enemy_1_2_list[i][8]].get_rect()) or enemy_1_2_list[i][6] == [0, 0]:
            dir_to_player = [-3 * (enemy_1_2_list[i][1][0] - player.pos[0]) / (
                    abs(enemy_1_2_list[i][1][1] - player.pos[1]) + abs((enemy_1_2_list[i][1][0] - player.pos[0]))),
                             -3 * (enemy_1_2_list[i][1][1] - player.pos[1]) / (
                                     abs(enemy_1_2_list[i][1][1] - player.pos[1]) + abs(
                                 enemy_1_2_list[i][1][0] - player.pos[0]))]
            enemy_1_2_list[i][6] = dir_to_player

        enemy_1_2_list[i][1] = touch_wall(enemy_1_2_list[i][1], enemy_1_2_list[i][0][enemy_1_2_list[i][8]].get_rect())

        if 0 <= enemy_1_2_list[i][7] * 20 % 60 < 30:
            enemy_1_2_list[i][8] = 1
        else:
            enemy_1_2_list[i][8] = 0

        if enemy_1_2_list[i][3] % 2 == 0 and enemy_1_2_list[i][3] > 0:
            enemy_1_2_list[i][1][0] += enemy_1_2_list[i][5][0]

        else:
            if (enemy_1_2_list[i][1][0] - player.pos[0]) >= 0:
                enemy_1_2_list[i][1][0] += enemy_1_2_list[i][6][0] + math.cos(enemy_1_2_list[i][7]) * 5
                enemy_1_2_list[i][4][0] = True
            elif (enemy_1_2_list[i][1][0] - player.pos[0]) <= 0:
                enemy_1_2_list[i][1][0] += enemy_1_2_list[i][6][0] + math.cos(enemy_1_2_list[i][7]) * 5
                enemy_1_2_list[i][4][1] = True
            if (enemy_1_2_list[i][1][1] - player.pos[1]) >= 0:
                enemy_1_2_list[i][1][1] += enemy_1_2_list[i][6][1] + math.sin(enemy_1_2_list[i][7]) * 5

                enemy_1_2_list[i][4][2] = True
            elif (enemy_1_2_list[i][1][1] - player.pos[1]) <= 0:
                enemy_1_2_list[i][1][1] += enemy_1_2_list[i][6][1] + math.sin(enemy_1_2_list[i][7]) * 5

                enemy_1_2_list[i][4][3] = True
        enemy_1_2_list[i][7] += 1 / 20


def move_ennemi_2_1():
    global enemy_2_1_list
    for i in range(0, len(enemy_2_1_list)):
        rectB = enemy_2_1_list[i][0][enemy_2_1_list[i][8]].get_rect(center=enemy_2_1_list[i][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (enemy_2_1_list[i][1][0] + 15, enemy_2_1_list[i][1][1] + 25)
        dist = math.sqrt(
            (enemy_2_1_list[i][1][0] - player.pos[0]) ** 2 + (enemy_2_1_list[i][1][1] - player.pos[1]) ** 2)
        enemy_2_1_list[i][4][0] = False
        enemy_2_1_list[i][4][1] = False
        enemy_2_1_list[i][4][2] = False
        enemy_2_1_list[i][4][3] = False
        enemy_2_1_list[i][1] = touch_wall(enemy_2_1_list[i][1], (
            enemy_2_1_list[i][0][enemy_2_1_list[i][8]].get_rect().w,
            enemy_2_1_list[i][0][enemy_2_1_list[i][8]].get_rect().h))
        if enemy_2_1_list[i][3] % 2 == 0 and enemy_2_1_list[i][3] > 0:
            enemy_2_1_list[i][1][0] += enemy_2_1_list[i][5][0]
        if 10 < dist <= 300 and enemy_2_1_list[i][7] > 0:
            if (enemy_2_1_list[i][1][0] - player.pos[0]) >= 0:
                enemy_2_1_list[i][1][0] += abs((enemy_2_1_list[i][1][0] - player.pos[0]) / (
                        abs(enemy_2_1_list[i][1][1] - player.pos[1]) + abs((enemy_2_1_list[i][1][0] - player.pos[0]))))
                enemy_2_1_list[i][4][0] = True
                if 0 <= enemy_2_1_list[i][7] % 12 < 6:
                    enemy_2_1_list[i][8] = 3
                elif 6 <= enemy_2_1_list[i][7] % 12 < 12:
                    enemy_2_1_list[i][8] = 4
            elif (enemy_2_1_list[i][1][0] - player.pos[0]) <= 0:
                enemy_2_1_list[i][1][0] -= abs((enemy_2_1_list[i][1][0] - player.pos[0]) / (
                        abs(enemy_2_1_list[i][1][1] - player.pos[1]) + abs(enemy_2_1_list[i][1][0] - player.pos[0])))
                enemy_2_1_list[i][4][1] = True
                if 0 <= enemy_2_1_list[i][7] % 12 < 6:
                    enemy_2_1_list[i][8] = 0
                elif 6 <= enemy_2_1_list[i][7] % 12:
                    enemy_2_1_list[i][8] = 1

            if (enemy_2_1_list[i][1][1] - player.pos[1]) >= 0:
                enemy_2_1_list[i][1][1] += abs((enemy_2_1_list[i][1][1] - player.pos[1]) / (
                        abs(enemy_2_1_list[i][1][1] - player.pos[1]) + abs(enemy_2_1_list[i][1][0] - player.pos[0])))
                enemy_2_1_list[i][4][2] = True
            elif (enemy_2_1_list[i][1][1] - player.pos[1]) <= 0:
                enemy_2_1_list[i][1][1] -= abs((enemy_2_1_list[i][1][1] - player.pos[1]) / (
                        abs(enemy_2_1_list[i][1][1] - player.pos[1]) + abs(enemy_2_1_list[i][1][0] - player.pos[0])))
                enemy_2_1_list[i][4][3] = True

        if enemy_2_1_list[i][7] < 0:
            enemy_2_1_list[i][6] = True

        if enemy_2_1_list[i][6] == True:
            if enemy_2_1_list[i][7] == -1:
                if enemy_2_1_list[i][8] == 0 or enemy_2_1_list[i][8] == 1:
                    enemy_2_1_list[i][8] = 5
                if enemy_2_1_list[i][8] == 3 or enemy_2_1_list[i][8] == 4:
                    enemy_2_1_list[i][8] = 2
                try:
                    total = abs(enemy_2_1_list[i][1][0] - player.pos[0]) + abs(enemy_2_1_list[i][1][1] - player.pos[1])
                    spawm_projectile([enemy_2_1_list[i][1][0], enemy_2_1_list[i][1][1]], 10,
                                     [(player.pos[0] - enemy_2_1_list[i][1][0]) / total * 5,
                                      (player.pos[1] - enemy_2_1_list[i][1][1]) / total * 5], (75, 0, 130))
                except:
                    pass
            if -1 < enemy_2_1_list[i][7] < -30:
                if enemy_2_1_list[i][8] == 0 or enemy_2_1_list[i][8] == 1:
                    enemy_2_1_list[i][8] = 5
                if enemy_2_1_list[i][8] == 3 or enemy_2_1_list[i][8] == 4:
                    enemy_2_1_list[i][8] = 2
            if enemy_2_1_list[i][7] == -30:
                if enemy_2_1_list[i][8] == 2:
                    enemy_2_1_list[i][8] = 3
                if enemy_2_1_list[i][8] == 5:
                    enemy_2_1_list[i][8] = 0

                enemy_2_1_list[i][6] = False
                enemy_2_1_list[i][7] = 300

def move_ennemi_2_2():
    global enemy_2_2_list
    for i in range(0, len(enemy_2_2_list)):
        rectB = enemy_2_2_list[i][0][0].get_rect(center=enemy_2_2_list[i][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (enemy_2_2_list[i][1][0] + 15, enemy_2_2_list[i][1][1] + 25)
        dist = math.sqrt(
            (enemy_2_2_list[i][1][0] - player.pos[0]) ** 2 + (enemy_2_2_list[i][1][1] - player.pos[1]) ** 2)
        enemy_2_2_list[i][4][0] = False
        enemy_2_2_list[i][4][1] = False
        enemy_2_2_list[i][4][2] = False
        enemy_2_2_list[i][4][3] = False
        enemy_2_2_list[i][1] = touch_wall(enemy_2_2_list[i][1], (
            enemy_2_2_list[i][0][0].get_rect().w,
            enemy_2_2_list[i][0][0].get_rect().h))
        if enemy_2_2_list[i][3] % 2 == 0 and enemy_2_2_list[i][3] > 0:
            enemy_2_2_list[i][1][0] += enemy_2_2_list[i][5][0]
        if enemy_2_2_list[i][7] < 0:
            enemy_2_2_list[i][6] = True

        if enemy_2_2_list[i][6] == True:
            if enemy_2_2_list[i][7] == -1:
                enemy_2_2_list[i][8] = [player.pos[0], player.pos[1]]
                enemy_2_2_list[i][1][0] = -150000
                enemy_2_2_list[i][1][1] = -150000
            if enemy_2_2_list[i][7] == -30:
                print(enemy_2_2_list)
                enemy_2_2_list[i][1][0] = enemy_2_2_list[i][8][0]
                enemy_2_2_list[i][1][1] = enemy_2_2_list[i][8][1]
                enemy_2_2_list[i][6] = False
                enemy_2_2_list[i][7] = 50
        """if enemy_2_2_list[i][3] % 2 == 0 and enemy_2_2_list[i][3] > 0:
                enemy_2_2_list[i][1][0] += enemy_2_2_list[i][5][0]
            if 10 < dist <= 300 and enemy_2_2_list[i][7] > 0:
                if (enemy_2_2_list[i][1][0] - player.pos[0]) >= 0:
                    enemy_2_2_list[i][1][0] += abs((enemy_2_2_list[i][1][0] - player.pos[0]) / (
                            abs(enemy_2_2_list[i][1][1] - player.pos[1]) + abs((enemy_2_2_list[i][1][0] - player.pos[0]))))
                    enemy_2_2_list[i][4][0] = True
                    if 0 <= enemy_2_2_list[i][7] % 12 < 6:
                        enemy_2_2_list[i][8] = 3
                    elif 6 <= enemy_2_2_list[i][7] % 12 < 12:
                        enemy_2_2_list[i][8] = 4
                elif (enemy_2_2_list[i][1][0] - player.pos[0]) <= 0:
                    enemy_2_2_list[i][1][0] -= abs((enemy_2_2_list[i][1][0] - player.pos[0]) / (
                            abs(enemy_2_2_list[i][1][1] - player.pos[1]) + abs(enemy_2_2_list[i][1][0] - player.pos[0])))
                    enemy_2_2_list[i][4][1] = True
                    if 0 <= enemy_2_2_list[i][7] % 12 < 6:
                        enemy_2_2_list[i][8] = 0
                    elif 6 <= enemy_2_2_list[i][7] % 12:
                        enemy_2_2_list[i][8] = 1
    
                if (enemy_2_2_list[i][1][1] - player.pos[1]) >= 0:
                    enemy_2_2_list[i][1][1] += abs((enemy_2_2_list[i][1][1] - player.pos[1]) / (
                            abs(enemy_2_2_list[i][1][1] - player.pos[1]) + abs(enemy_2_2_list[i][1][0] - player.pos[0])))
                    enemy_2_2_list[i][4][2] = True
                elif (enemy_2_2_list[i][1][1] - player.pos[1]) <= 0:
                    enemy_2_2_list[i][1][1] -= abs((enemy_2_2_list[i][1][1] - player.pos[1]) / (
                            abs(enemy_2_2_list[i][1][1] - player.pos[1]) + abs(enemy_2_2_list[i][1][0] - player.pos[0])))
                    enemy_2_2_list[i][4][3] = True
    
            if enemy_2_2_list[i][7] < 0:
                enemy_2_2_list[i][6] = True
    
            if enemy_2_2_list[i][6] == True:
                if enemy_2_2_list[i][7] == -1:
                    if enemy_2_2_list[i][8] == 0 or enemy_2_2_list[i][8] == 1:
                        enemy_2_2_list[i][8] = 5
                    if enemy_2_2_list[i][8] == 3 or enemy_2_2_list[i][8] == 4:
                        enemy_2_2_list[i][8] = 2
                    try:
                        total = abs(enemy_2_2_list[i][1][0] - player.pos[0]) + abs(enemy_2_2_list[i][1][1] - player.pos[1])
                        spawm_projectile([enemy_2_2_list[i][1][0], enemy_2_2_list[i][1][1]], 10,
                                         [(player.pos[0] - enemy_2_2_list[i][1][0]) / total * 5,
                                          (player.pos[1] - enemy_2_2_list[i][1][1]) / total * 5], (75, 0, 130))
                    except:
                        pass
                if -1 < enemy_2_2_list[i][7] < -30:
                    if enemy_2_2_list[i][8] == 0 or enemy_2_2_list[i][8] == 1:
                        enemy_2_2_list[i][8] = 5
                    if enemy_2_2_list[i][8] == 3 or enemy_2_2_list[i][8] == 4:
                        enemy_2_2_list[i][8] = 2
                if enemy_2_2_list[i][7] == -30:
                    if enemy_2_2_list[i][8] == 2:
                        enemy_2_2_list[i][8] = 3
                    if enemy_2_2_list[i][8] == 5:
                        enemy_2_2_list[i][8] = 0
    
                    enemy_2_2_list[i][6] = False
                    enemy_2_2_list[i][7] = 300
        """
def move_boss_1():
    global boss_list
    if not boss_list:
        return
    if boss_list[0][4] == 0:
        rectB = boss_list[0][0][0].get_rect(center=boss_list[0][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (boss_list[0][1][0] + 23, boss_list[0][1][1] + 40)
        # zadezd = pygame.draw.rect(graphic_main.screen, (255, 255, 255), rectB)
        # graphic_main.update.append(zadezd)
        dist = math.sqrt((boss_list[0][1][0] - player.pos[0]) ** 2 + (boss_list[0][1][1] - player.pos[1]) ** 2)
        boss_list[0][1] = touch_wall(boss_list[0][1], [46, 80])

        boss_list[0][3][0] = False
        boss_list[0][3][1] = False
        boss_list[0][3][2] = False
        boss_list[0][3][3] = False
        if boss_list[0][6] % 2 == 0 and boss_list[0][6] > 0:
            boss_list[0][1][0] += boss_list[0][7][0]
        if 15 < dist <= 800:
            if (boss_list[0][1][0] - player.pos[0]) >= 0:
                boss_list[0][1][0] -= (abs((boss_list[0][1][0] - player.pos[0]) / (
                        abs(boss_list[0][1][1] - player.pos[1]) + abs((boss_list[0][1][0] - player.pos[0]))))) * 2
                boss_list[0][10] = 0
                boss_list[0][3][0] = True

            elif (boss_list[0][1][0] - player.pos[0]) <= 0:
                boss_list[0][1][0] += (abs((boss_list[0][1][0] - player.pos[0]) / (
                        abs(boss_list[0][1][1] - player.pos[1]) + abs(boss_list[0][1][0] - player.pos[0])))) * 2
                boss_list[0][3][1] = True
                boss_list[0][10] = 1

            if (boss_list[0][1][1] - player.pos[1]) >= 0:

                boss_list[0][1][1] -= (abs((boss_list[0][1][1] - player.pos[1]) / (
                        abs(boss_list[0][1][1] - player.pos[1]) + abs(boss_list[0][1][0] - player.pos[0])))) * 2
                boss_list[0][3][3] = True

            elif (boss_list[0][1][1] - player.pos[1]) <= 0:

                boss_list[0][1][1] += (abs((boss_list[0][1][1] - player.pos[1]) / (
                        abs(boss_list[0][1][1] - player.pos[1]) + abs(boss_list[0][1][0] - player.pos[0])))) * 2
                boss_list[0][3][3] = True
    if  0 < boss_list[0][4] < 1:
        boss_list[0][4] += 0.01
        print(boss_list[0][4])
        if 0.5 < boss_list[0][4] < 0.51:
            boss_list[0][4]=0.5
        if boss_list[0][4] == 0.5:
            boss_list[0][10] += 2
            print(boss_list[0][10])
        if boss_list[0][4] > 1:
            boss_list[0][4] = 1
    if boss_list[0][4] == 1:
        rectB = boss_list[0][0][0].get_rect(center=boss_list[0][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (boss_list[0][1][0] + 23, boss_list[0][1][1] + 40)
        # zadezd = pygame.draw.rect(graphic_main.screen, (255, 255, 255), rectB)
        # graphic_main.update.append(zadezd)
        dist = math.sqrt((boss_list[0][1][0] - player.pos[0]) ** 2 + (boss_list[0][1][1] - player.pos[1]) ** 2)
        #boss_list[0][1] = touch_wall(boss_list[0][1], boss_list[0][0][0].get_rect())

        boss_list[0][3][0] = False
        boss_list[0][3][1] = False
        boss_list[0][3][2] = False
        boss_list[0][3][3] = False
        print(boss_list[0][9])
        print(is_touch_wall(boss_list[0][1], boss_list[0][0][0].get_rect()))
        print(boss_list[0][1])

        if is_touch_wall(boss_list[0][1], boss_list[0][0][0].get_rect()) or boss_list[0][9] == [0, 0]:
            dir_to_player = [-3 * (boss_list[0][1][0] - player.pos[0]) / (
                    abs(boss_list[0][1][1] - player.pos[1]) + abs((boss_list[0][1][0] - player.pos[0]))),
                             -3 * (boss_list[0][1][1] - player.pos[1]) / (
                                     abs(boss_list[0][1][1] - player.pos[1]) + abs(
                                 boss_list[0][1][0] - player.pos[0]))]
            boss_list[0][9] = dir_to_player

        boss_list[0][1] = touch_wall(boss_list[0][1], boss_list[0][0][0].get_rect())

        if boss_list[0][6] % 2 == 0 and boss_list[0][6] > 0:
            boss_list[0][1][0] += boss_list[0][7][0]

        else:
            if (boss_list[0][1][0] - player.pos[0]) >= 0:
                boss_list[0][1][0] += boss_list[0][9][0] * 1 + math.cos(boss_list[0][5]) * 5
                boss_list[0][3][0] = True
                boss_list[0][10] = 4
            elif (boss_list[0][1][0] - player.pos[0]) <= 0:
                boss_list[0][1][0] += boss_list[0][9][0] * 1 + math.cos(boss_list[0][5]) * 5
                boss_list[0][3][1] = True
                boss_list[0][10] = 7
            if (boss_list[0][1][1] - player.pos[1]) >= 0:
                boss_list[0][1][1] += boss_list[0][9][1] * 1 + math.sin(boss_list[0][5]) * 5

                boss_list[0][3][2] = True
            elif (boss_list[0][1][1] - player.pos[1]) <= 0:
                boss_list[0][1][1] += boss_list[0][9][1] * 1 + math.sin(boss_list[0][5]) * 5

                boss_list[0][3][3] = True
        boss_list[0][5] += 1 / 20
    if 1 < boss_list[0][4] < 2:
        boss_list[0][4] += 0.01
        print(boss_list[0][10])
        if 1.17 < boss_list[0][4] < 1.18:
            boss_list[0][4]=1.17
        if boss_list[0][4] == 1.17:
            boss_list[0][10] = 16
        if 1.26 < boss_list[0][4] < 1.27:
            boss_list[0][4]=1.26
        if boss_list[0][4] == 1.26:
            boss_list[0][10] += 1
        if 1.5 < boss_list[0][4] < 1.51:
            boss_list[0][4]=1.5
        if boss_list[0][4] == 1.5:
            boss_list[0][10] += 1
        if 1.7 < boss_list[0][4] < 1.71:
            boss_list[0][4]=1.7
        if boss_list[0][4] == 1.7:
            boss_list[0][10] += 1
        if 1.92 < boss_list[0][4] < 1.93:
            boss_list[0][4]=1.92
        if boss_list[0][4] == 1.92:
            boss_list[0][10] += 1
        if boss_list[0][4] >= 2:
            spawn_boss_1([boss_list[0][1][0]+90, boss_list[0][1][1]], 100)
            boss_list[1][4] = 2
            boss_list[1][10] = 10
            boss_list[0][2] = 100
            boss_list[0][4] = 2
    if boss_list[0][4] == 2:
        for i in range(0, len(boss_list)):
            rectB = boss_list[i][0][0].get_rect(center=boss_list[i][1])
            rectB.h = 90
            rectB.w = 46
            rectB.center = (boss_list[i][1][0] + 23, boss_list[i][1][1] + 40)
            # zadezd = pygame.draw.rect(graphic_main.screen, (255, 255, 255), rectB)
            # graphic_main.update.append(zadezd)
            #dist = math.sqrt((boss_list[0][1][0] - player.pos[0]) ** 2 + (boss_list[0][1][1] - player.pos[1]) ** 2)

            boss_list[i][3][0] = False
            boss_list[i][3][1] = False
            boss_list[i][3][2] = False
            boss_list[i][3][3] = False
            if is_touch_wall(boss_list[i][1], boss_list[i][0][0].get_rect()) or boss_list[0][6] == [0, 0]:
                dir_to_player = [-3 * (boss_list[i][1][0] - player.pos[0]) / (
                        abs(boss_list[i][1][1] - player.pos[1]) + abs((boss_list[i][1][0] - player.pos[0]))),
                                 -3 * (boss_list[i][1][1] - player.pos[1]) / (
                                         abs(boss_list[i][1][1] - player.pos[1]) + abs(
                                     boss_list[i][1][0] - player.pos[0]))]
                boss_list[i][9] = dir_to_player

            boss_list[i][1] = touch_wall(boss_list[i][1], boss_list[i][0][0].get_rect())

            if boss_list[i][6] % 2 == 0 and boss_list[i][6] > 0:
                boss_list[i][1][0] += boss_list[i][7][0]

            else:
                if (boss_list[i][1][0] - player.pos[0]) >= 0:
                    boss_list[i][1][0] += boss_list[i][9][0] * 1 + math.cos(boss_list[i][5]) * 2.5
                    boss_list[i][3][0] = True
                    boss_list[i][10] = 4 + 6*i

                elif (boss_list[i][1][0] - player.pos[0]) <= 0:
                    boss_list[i][1][0] += boss_list[i][9][0] * 1 + math.cos(boss_list[i][5]) * 2.5
                    boss_list[i][3][1] = True
                    boss_list[i][10] = 7 +6*i

                if (boss_list[i][1][1] - player.pos[1]) >= 0:
                    boss_list[i][1][1] += boss_list[i][9][1] * 1 + math.sin(boss_list[i][5]) * 2.5

                    boss_list[i][3][2] = True
                elif (boss_list[i][1][1] - player.pos[1]) <= 0:
                    boss_list[i][1][1] += boss_list[i][9][1] * 1 + math.sin(boss_list[i][5]) * 2.5

                    boss_list[i][3][3] = True
            boss_list[i][5] += 1 / 20


def move_ennemi_slime():
    global enemy_slime_list
    for i in range(0, len(enemy_slime_list)):
        rectB = enemy_slime_list[i][0].get_rect(center=enemy_slime_list[i][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (enemy_slime_list[i][1][0] + 15, enemy_slime_list[i][1][1] + 25)
        dist = math.sqrt((enemy_slime_list[i][1][0] - player.pos[0]) ** 2 + (enemy_slime_list[i][1][1] - player.pos[1]) ** 2)
        enemy_slime_list[i][4][0] = False
        enemy_slime_list[i][4][1] = False
        enemy_slime_list[i][4][2] = False
        enemy_slime_list[i][4][3] = False
        enemy_slime_list[i][1] = touch_wall(enemy_slime_list[i][1], enemy_slime_list[i][0].get_rect())
        if enemy_slime_list[i][3] % 2 == 0 and enemy_slime_list[i][3] > 0:
            enemy_slime_list[i][1][0] += enemy_slime_list[i][5][0]
        if 15 < dist <= 800:
            if (enemy_slime_list[i][1][0] - player.pos[0]) >= 0:
                enemy_slime_list[i][1][0] -= abs((enemy_slime_list[i][1][0] - player.pos[0]) / (
                        abs(enemy_slime_list[i][1][1] - player.pos[1]) + abs((enemy_slime_list[i][1][0] - player.pos[0])))) * 2
                enemy_slime_list[i][4][0] = True
            elif (enemy_slime_list[i][1][0] - player.pos[0]) <= 0:
                enemy_slime_list[i][1][0] += abs((enemy_slime_list[i][1][0] - player.pos[0]) / (
                        abs(enemy_slime_list[i][1][1] - player.pos[1]) + abs(enemy_slime_list[i][1][0] - player.pos[0]))) * 2
                enemy_slime_list[i][4][1] = True
            if (enemy_slime_list[i][1][1] - player.pos[1]) >= 0:
                enemy_slime_list[i][1][1] -= abs((enemy_slime_list[i][1][1] - player.pos[1]) / (
                        abs(enemy_slime_list[i][1][1] - player.pos[1]) + abs(enemy_slime_list[i][1][0] - player.pos[0]))) * 2
                enemy_slime_list[i][4][2] = True
            elif (enemy_slime_list[i][1][1] - player.pos[1]) <= 0:
                enemy_slime_list[i][1][1] += abs((enemy_slime_list[i][1][1] - player.pos[1]) / (
                        abs(enemy_slime_list[i][1][1] - player.pos[1]) + abs(enemy_slime_list[i][1][0] - player.pos[0]))) * 2
                enemy_slime_list[i][4][3] = True

def move_ennemi_4_1():
    global enemy_4_1_list
    for i in range(0, len(enemy_4_1_list)):
        rectB = enemy_4_1_list[i][0].get_rect(center=enemy_4_1_list[i][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (enemy_4_1_list[i][1][0] + 15, enemy_4_1_list[i][1][1] + 25)
        dist = math.sqrt(
            (enemy_4_1_list[i][1][0] - player.pos[0]) ** 2 + (enemy_4_1_list[i][1][1] - player.pos[1]) ** 2)
        enemy_4_1_list[i][4][0] = False
        enemy_4_1_list[i][4][1] = False
        enemy_4_1_list[i][4][2] = False
        enemy_4_1_list[i][4][3] = False
        enemy_4_1_list[i][1] = touch_wall(enemy_4_1_list[i][1], (
            enemy_4_1_list[i][0].get_rect().w,
            enemy_4_1_list[i][0].get_rect().h))
        if enemy_4_1_list[i][3] % 2 == 0 and enemy_4_1_list[i][3] > 0:
            enemy_4_1_list[i][1][0] += enemy_4_1_list[i][5][0]
        if 10 < dist <= 300 and enemy_4_1_list[i][7] > 0:
            if (enemy_4_1_list[i][1][0] - player.pos[0]) >= 0:
                enemy_4_1_list[i][1][0] += abs((enemy_4_1_list[i][1][0] - player.pos[0]) / (
                        abs(enemy_4_1_list[i][1][1] - player.pos[1]) + abs((enemy_4_1_list[i][1][0] - player.pos[0]))))
                enemy_4_1_list[i][4][0] = True
                if 0 <= enemy_4_1_list[i][7] % 12 < 6:
                    enemy_4_1_list[i][8] = 3
                elif 6 <= enemy_4_1_list[i][7] % 12 < 12:
                    enemy_4_1_list[i][8] = 4
            elif (enemy_4_1_list[i][1][0] - player.pos[0]) <= 0:
                enemy_4_1_list[i][1][0] -= abs((enemy_4_1_list[i][1][0] - player.pos[0]) / (
                        abs(enemy_4_1_list[i][1][1] - player.pos[1]) + abs(enemy_4_1_list[i][1][0] - player.pos[0])))
                enemy_4_1_list[i][4][1] = True
                if 0 <= enemy_4_1_list[i][7] % 12 < 6:
                    enemy_4_1_list[i][8] = 0
                elif 6 <= enemy_4_1_list[i][7] % 12:
                    enemy_4_1_list[i][8] = 1

            if (enemy_4_1_list[i][1][1] - player.pos[1]) >= 0:
                enemy_4_1_list[i][1][1] += abs((enemy_4_1_list[i][1][1] - player.pos[1]) / (
                        abs(enemy_4_1_list[i][1][1] - player.pos[1]) + abs(enemy_4_1_list[i][1][0] - player.pos[0])))
                enemy_4_1_list[i][4][2] = True
            elif (enemy_4_1_list[i][1][1] - player.pos[1]) <= 0:
                enemy_4_1_list[i][1][1] -= abs((enemy_4_1_list[i][1][1] - player.pos[1]) / (
                        abs(enemy_4_1_list[i][1][1] - player.pos[1]) + abs(enemy_4_1_list[i][1][0] - player.pos[0])))
                enemy_4_1_list[i][4][3] = True

        if enemy_4_1_list[i][7] < 0:
            enemy_4_1_list[i][6] = True

        if enemy_4_1_list[i][6] == True:
            if enemy_4_1_list[i][7] == -1 and len(enemy_slime_list)/len(enemy_4_1_list) < 4:

                try:
                    total = abs(enemy_4_1_list[i][1][0] - player.pos[0]) + abs(enemy_4_1_list[i][1][1] - player.pos[1])
                    spawn_enemy_slime([enemy_4_1_list[i][1][0], enemy_4_1_list[i][1][1]], 'picture/enemy/mage/slime.png', 20)

                except:
                    raise

            if enemy_4_1_list[i][7] == -30:


                enemy_4_1_list[i][6] = False
                enemy_4_1_list[i][7] = 20

def move_ennemi_4_2():
    global enemy_4_2_list
    for i in range(0, len(enemy_4_2_list)):
        print( len(enemy_4_2_list))
        rectB = enemy_4_2_list[i][0][enemy_4_2_list[i][8]].get_rect(center=enemy_4_2_list[i][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (enemy_4_2_list[i][1][0] + 15, enemy_4_2_list[i][1][1] + 25)
        dist = math.sqrt(
            (enemy_4_2_list[i][1][0] - player.pos[0]) ** 2 + (enemy_4_2_list[i][1][1] - player.pos[1]) ** 2)
        enemy_4_2_list[i][4][0] = False
        enemy_4_2_list[i][4][1] = False
        enemy_4_2_list[i][4][2] = False
        enemy_4_2_list[i][4][3] = False
        enemy_4_2_list[i][1] = touch_wall(enemy_4_2_list[i][1], (
            enemy_4_2_list[i][0][enemy_4_2_list[i][8]].get_rect().w,
            enemy_4_2_list[i][0][enemy_4_2_list[i][8]].get_rect().h))
        if enemy_4_2_list[i][3] % 2 == 0 and enemy_4_2_list[i][3] > 0:
            enemy_4_2_list[i][1][0] += enemy_4_2_list[i][5][0]
        if True:
            if (enemy_4_2_list[i][1][0] - player.pos[0]) >= 0:
                enemy_4_2_list[i][8] = 1

            elif (enemy_4_2_list[i][1][0] - player.pos[0]) <= 0:

                enemy_4_2_list[i][8] = 0

            if (enemy_4_2_list[i][1][1] - player.pos[1]) >= 0:
                enemy_4_2_list[i][1][1] -= abs((enemy_4_2_list[i][1][1] - player.pos[1]))/5
                enemy_4_2_list[i][4][2] = True
            elif (enemy_4_2_list[i][1][1] - player.pos[1]) <= 0:
                enemy_4_2_list[i][1][1] += abs((enemy_4_2_list[i][1][1] - player.pos[1]))/5
                enemy_4_2_list[i][4][3] = True


        if enemy_4_2_list[i][7] < 0:
            enemy_4_2_list[i][6] = True

        if enemy_4_2_list[i][6] == True:
            if enemy_4_2_list[i][7] == -1:

                try:
                    if enemy_4_2_list[i][8] == 0:

                        spawm_projectile([enemy_4_2_list[i][1][0]+30, enemy_4_2_list[i][1][1]+22], 5, [5, 0], (0, 0, 255))
                    if enemy_4_2_list[i][8] == 1:

                        spawm_projectile([enemy_4_2_list[i][1][0]+0, enemy_4_2_list[i][1][1]+22], 5, [-5, 0], (0, 0, 255))
                except:
                    raise

            if enemy_4_2_list[i][7] == -20:


                enemy_4_2_list[i][6] = False
                enemy_4_2_list[i][7] = 5
def move_ennemi_3_1():
    global enemy_3_1_list
    for i in range(0, len(enemy_3_1_list)):
        rectB = enemy_3_1_list[i][0][0].get_rect(center=enemy_3_1_list[i][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (enemy_3_1_list[i][1][0] + 15, enemy_3_1_list[i][1][1] + 25)
        dist = math.sqrt(
            (enemy_3_1_list[i][1][0] - player.pos[0]) ** 2 + (enemy_3_1_list[i][1][1] - player.pos[1]) ** 2)
        enemy_3_1_list[i][4][0] = False
        enemy_3_1_list[i][4][1] = False
        enemy_3_1_list[i][4][2] = False
        enemy_3_1_list[i][4][3] = False
        enemy_3_1_list[i][1] = touch_wall(enemy_3_1_list[i][1], (
            enemy_3_1_list[i][0][0].get_rect().w,
            enemy_3_1_list[i][0][0].get_rect().h))
        if enemy_3_1_list[i][3] % 2 == 0 and enemy_3_1_list[i][3] > 0:
            enemy_3_1_list[i][1][0] += enemy_3_1_list[i][5][0]

        if enemy_3_1_list[i][7] < 0:
            enemy_3_1_list[i][6] = True
        print('eee', enemy_3_1_list[i][8])
        if enemy_3_1_list[i][6] == True:
            if enemy_3_1_list[i][7] == -1:
                enemy_3_1_list[i][8] = 1
            #if -1 < enemy_3_1_list[i][7] < -30:
            #    enemy_3_1_list[i][1] = [-10000, -10000]



            if enemy_3_1_list[i][7] == -40:
                spawm_projectile([enemy_3_1_list[i][1][0]+ 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [5, 0], (75, 0, 130), enemy_3_1_list[i][9][4])
                spawm_projectile([enemy_3_1_list[i][1][0]+ 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [5, 5], (75, 0, 130), enemy_3_1_list[i][9][3])
                spawm_projectile([enemy_3_1_list[i][1][0]+ 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [0, 5], (75, 0, 130), enemy_3_1_list[i][9][2])
                spawm_projectile([enemy_3_1_list[i][1][0]+ 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [-5, 5], (75, 0, 130), enemy_3_1_list[i][9][1])
                spawm_projectile([enemy_3_1_list[i][1][0]+ 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [-5, 0], (75, 0, 130), enemy_3_1_list[i][9][0])
                spawm_projectile([enemy_3_1_list[i][1][0]+ 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [-5, -5], (75, 0, 130), enemy_3_1_list[i][9][7])
                spawm_projectile([enemy_3_1_list[i][1][0]+ 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [0, -5], (75, 0, 130), enemy_3_1_list[i][9][6])
                spawm_projectile([enemy_3_1_list[i][1][0]+ 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [5, -5], (75, 0, 130), enemy_3_1_list[i][9][5])
                enemy_3_1_list[i][6] = False
                enemy_3_1_list[i][8] = 0
                enemy_3_1_list[i][7] = 120

def move_boss_4():
    global boss_list_4
    if not boss_list_4:
        return
    if boss_list_4[0][4] == 0:
        rectB = boss_list_4[0][0][0].get_rect(center=boss_list_4[0][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (boss_list_4[0][1][0] + 15, boss_list_4[0][1][1] + 25)
        dist = math.sqrt(
            (boss_list_4[0][1][0] - player.pos[0]) ** 2 + (boss_list_4[0][1][1] - player.pos[1]) ** 2)
        boss_list_4[0][1] = touch_wall(boss_list_4[0][1], (
            boss_list_4[0][0][0].get_rect().w,
            boss_list_4[0][0][0].get_rect().h))
        if boss_list_4[0][6] % 2 == 0 and boss_list_4[0][6] > 0:

            boss_list_4[0][1][0] += boss_list_4[0][7][0]
        if dist <200:
            if (boss_list_4[0][1][0] - player.pos[0]) >= 0:
                boss_list_4[0][1][0] += abs((boss_list_4[0][1][0] - player.pos[0]) / (
                        abs(boss_list_4[0][1][1] - player.pos[1]) + abs((boss_list_4[0][1][0] - player.pos[0]))))


            elif (boss_list_4[0][1][0] - player.pos[0]) <= 0:
                boss_list_4[0][1][0] -= abs((boss_list_4[0][1][0] - player.pos[0]) / (
                        abs(boss_list_4[0][1][1] - player.pos[1]) + abs(boss_list_4[0][1][0] - player.pos[0])))

            if (boss_list_4[0][1][1] - player.pos[1]) >= 0:
                boss_list_4[0][1][1] += abs((boss_list_4[0][1][1] - player.pos[1]) / (
                        abs(boss_list_4[0][1][1] - player.pos[1]) + abs(boss_list_4[0][1][0] - player.pos[0])))
            elif (boss_list_4[0][1][1] - player.pos[1]) <= 0:
                boss_list_4[0][1][1] -= abs((boss_list_4[0][1][1] - player.pos[1]) / (
                        abs(boss_list_4[0][1][1] - player.pos[1]) + abs(boss_list_4[0][1][0] - player.pos[0])))

        if dist < 100 and  -10 >= boss_list_4[0][5]  >= -20:
            boss_list_4[0][1][0] = random.randrange(graphic_main.left +50, graphic_main.right-50)
            boss_list_4[0][1][1] = random.randrange(graphic_main.top+50, graphic_main.bottom-50)
        if boss_list_4[0][5] < 0:
            boss_list_4[0][6] = True
        print(boss_list_4[0][5])
        if boss_list_4[0][6] == True:
            if boss_list_4[0][5] == -1:

                try:

                    spawn_enemy_4_1([boss_list_4[0][1][0], boss_list_4[0][1][1]], 'picture/enemy/mage/Mage.png', 20)
                except:
                    raise

            if boss_list_4[0][5] == -20:
                boss_list_4[0][6] = False
                boss_list_4[0][5] = 120
    if  0 < boss_list_4[0][4] < 1:
        boss_list_4[0][4] += 0.01
        print(boss_list_4[0][4])
        if 0.5 < boss_list_4[0][4] < 0.51:
            boss_list_4[0][4]=0.5
        if boss_list_4[0][4] == 0.5:
            boss_list_4[0][10] += 2
            print(boss_list_4[0][10])
        if boss_list_4[0][4] > 1:
            boss_list_4[0][4] = 1
            boss_list_4[0][5] = 60

    if boss_list_4[0][4] == 1:

        rectB = boss_list_4[0][0][0].get_rect(center=boss_list_4[0][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (boss_list_4[0][1][0] + 23, boss_list_4[0][1][1] + 40)
        # zadezd = pygame.draw.rect(graphic_main.screen, (255, 255, 255), rectB)
        # graphic_main.update.append(zadezd)
        dist = math.sqrt((boss_list_4[0][1][0] - player.pos[0]) ** 2 + (boss_list_4[0][1][1] - player.pos[1]) ** 2)

        boss_list_4[0][3][0] = False
        boss_list_4[0][3][1] = False
        boss_list_4[0][3][2] = False
        boss_list_4[0][3][3] = False
        print(boss_list_4[0][5])
        if boss_list_4[0][5] == 0:
            boss_list_4[0][1][0] = player.pos[0] + random.randrange(0, 50)
            boss_list_4[0][1][1] = player.pos[1] + random.randrange(0, 50)
            boss_list_4[0][5] = 120
        if boss_list_4[0][5] == 60:
            boss_list_4[0][1][0] = random.randrange(graphic_main.left +50, graphic_main.right-50)
            boss_list_4[0][1][1] = random.randrange(graphic_main.top+50, graphic_main.bottom-50)
        if 0 < boss_list_4[0][5] < 10:
            boss_list_4[0][1][0] += random.randrange(-10, 10)
            boss_list_4[0][1][1] += random.randrange(-10, 10)
        if boss_list_4[0][6] % 2 == 0 and boss_list_4[0][6] > 0:

            boss_list_4[0][1][0] += boss_list_4[0][7][0]

        """        
        rectB = boss_list_4[0][0][0].get_rect(center=boss_list_4[0][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (boss_list_4[0][1][0] + 23, boss_list_4[0][1][1] + 40)
        # zadezd = pygame.draw.rect(graphic_main.screen, (255, 255, 255), rectB)
        # graphic_main.update.append(zadezd)
        dist = math.sqrt((boss_list_4[0][1][0] - player.pos[0]) ** 2 + (boss_list_4[0][1][1] - player.pos[1]) ** 2)
        #boss_list_4[0][1] = touch_wall(boss_list_4[0][1], boss_list_4[0][0][0].get_rect())

        boss_list_4[0][3][0] = False
        boss_list_4[0][3][1] = False
        boss_list_4[0][3][2] = False
        boss_list_4[0][3][3] = False
        print(boss_list_4[0][9])
        print(is_touch_wall(boss_list_4[0][1], boss_list_4[0][0][0].get_rect()))
        print(boss_list_4[0][1])

        if is_touch_wall(boss_list_4[0][1], boss_list_4[0][0][0].get_rect()) or boss_list_4[0][9] == [0, 0]:
            dir_to_player = [-3 * (boss_list_4[0][1][0] - player.pos[0]) / (
                    abs(boss_list_4[0][1][1] - player.pos[1]) + abs((boss_list_4[0][1][0] - player.pos[0]))),
                             -3 * (boss_list_4[0][1][1] - player.pos[1]) / (
                                     abs(boss_list_4[0][1][1] - player.pos[1]) + abs(
                                 boss_list_4[0][1][0] - player.pos[0]))]
            boss_list_4[0][9] = dir_to_player

        boss_list_4[0][1] = touch_wall(boss_list_4[0][1], boss_list_4[0][0][0].get_rect())

        if boss_list_4[0][6] % 2 == 0 and boss_list_4[0][6] > 0:
            boss_list_4[0][1][0] += boss_list_4[0][7][0]

        else:
            if (boss_list_4[0][1][0] - player.pos[0]) >= 0:
                boss_list_4[0][1][0] += boss_list_4[0][9][0] * 1 + math.cos(boss_list_4[0][5]) * 5
                boss_list_4[0][3][0] = True
                boss_list_4[0][10] = 4
            elif (boss_list_4[0][1][0] - player.pos[0]) <= 0:
                boss_list_4[0][1][0] += boss_list_4[0][9][0] * 1 + math.cos(boss_list_4[0][5]) * 5
                boss_list_4[0][3][1] = True
                boss_list_4[0][10] = 7
            if (boss_list_4[0][1][1] - player.pos[1]) >= 0:
                boss_list_4[0][1][1] += boss_list_4[0][9][1] * 1 + math.sin(boss_list_4[0][5]) * 5

                boss_list_4[0][3][2] = True
            elif (boss_list_4[0][1][1] - player.pos[1]) <= 0:
                boss_list_4[0][1][1] += boss_list_4[0][9][1] * 1 + math.sin(boss_list_4[0][5]) * 5

                boss_list_4[0][3][3] = True
        boss_list_4[0][5] += 1 / 20"""
    if 1 < boss_list_4[0][4] < 2:
        boss_list_4[0][4] += 0.01
        print(boss_list_4[0][10])
        if 1.17 < boss_list_4[0][4] < 1.18:
            boss_list_4[0][4]=1.17
        if boss_list_4[0][4] == 1.17:
            boss_list_4[0][10] = 16
        if 1.26 < boss_list_4[0][4] < 1.27:
            boss_list_4[0][4]=1.26
        if boss_list_4[0][4] == 1.26:
            boss_list_4[0][10] += 1
        if 1.5 < boss_list_4[0][4] < 1.51:
            boss_list_4[0][4]=1.5
        if boss_list_4[0][4] == 1.5:
            boss_list_4[0][10] += 1
        if 1.7 < boss_list_4[0][4] < 1.71:
            boss_list_4[0][4]=1.7
        if boss_list_4[0][4] == 1.7:
            boss_list_4[0][10] += 1
        if 1.92 < boss_list_4[0][4] < 1.93:
            boss_list_4[0][4]=1.92
        if boss_list_4[0][4] == 1.92:
            boss_list_4[0][10] += 1
        if boss_list_4[0][4] >= 2:
            #spawn_boss_4([boss_list_4[0][1][0]+90, boss_list_4[0][1][1]], 100)
            boss_list_4[0][2] = 200
            boss_list_4[0][4] = 2
            boss_list_4[0][5] = 20
    if boss_list_4[0][4] == 2:
        rectB = boss_list_4[0][0][0].get_rect(center=boss_list_4[0][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (boss_list_4[0][1][0] + 23, boss_list_4[0][1][1] + 40)
        # zadezd = pygame.draw.rect(graphic_main.screen, (255, 255, 255), rectB)
        # graphic_main.update.append(zadezd)
        dist = math.sqrt((boss_list_4[0][1][0] - player.pos[0]) ** 2 + (boss_list_4[0][1][1] - player.pos[1]) ** 2)

        boss_list_4[0][3][0] = False
        boss_list_4[0][3][1] = False
        boss_list_4[0][3][2] = False
        boss_list_4[0][3][3] = False
        print(boss_list_4[0][5])
        if boss_list_4[0][6] % 2 == 0 and boss_list_4[0][6] > 0:

            boss_list_4[0][1][0] += boss_list_4[0][7][0]
        if boss_list_4[0][5] == 0:
            boss_list_4[0][1][0] = player.pos[0] + random.randrange(0, 50)
            boss_list_4[0][1][1] = player.pos[1] + random.randrange(0, 50)
            boss_list_4[0][5] = 120
        if boss_list_4[0][5] == 60:
            boss_list_4[0][1][0] = random.randrange(graphic_main.left +50, graphic_main.right-50)
            boss_list_4[0][1][1] = random.randrange(graphic_main.top+50, graphic_main.bottom-50)
            spawn_enemy_slime([boss_list_4[0][1][0], boss_list_4[0][1][1]], 'picture/enemy/mage/slime.png', 20)
        if 0 < boss_list_4[0][5] < 10:

            boss_list_4[0][1][0] += random.randrange(-10, 10)
            boss_list_4[0][1][1] += random.randrange(-10, 10)

def move_projectile():
    global projectile_lists
    for i in range(0, len(projectile_list)):
        projectile_list[i][0][0] += projectile_list[i][2][0]
        projectile_list[i][0][1] += projectile_list[i][2][1]

    n = 0
    for i in projectile_list:
        if is_touch_wall(i[0], [10, 10]):
            del projectile_list[n]
        n += 1


def collision_with_weapon(a, strenght, knockback):

    n = 0
    global enemy_1_list
    global enemy_1_2_list
    global enemy_2_1_list
    global boss_list
    global enemy_4_1_list
    global enemy_slime_list
    global enemy_4_2_list
    for i in enemy_1_list:

        collision = False
        rectB = i[0].get_rect(center=i[1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (i[1][0] + 15, i[1][1] + 25)
        collision = rectB.colliderect(a)
        if collision and i[3] <= 0:
            player.mana += 3
            player.folie -= 5

            enemy_1_list[n][2] -= strenght
            enemy_1_list[n][3] = 30
            if player.last_move_is_up or player.last_move_is_right:
                enemy_1_list[n][5][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                enemy_1_list[n][5][0] = -knockback

            if enemy_1_list[n][2] <= 0:
                player.folie -= 30
                del enemy_1_list[n]

        n += 1
    n = 0
    for i in enemy_1_2_list:
        collision = False
        rectB = i[0][i[8]].get_rect(center=i[1])
        rectB.h = 12
        rectB.w = 49
        rectB.center = (i[1][0] + 24, i[1][1] + 11)

        collision = rectB.colliderect(a)
        if collision and i[3] <= 0:
            player.mana += 3

            player.folie -= 5

            enemy_1_2_list[n][2] -= strenght
            enemy_1_2_list[n][3] = 30
            if player.last_move_is_up or player.last_move_is_right:
                enemy_1_2_list[n][5][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                enemy_1_2_list[n][5][0] = -knockback

            if enemy_1_2_list[n][2] <= 0:
                player.folie -= 20
                del enemy_1_2_list[n]

        n += 1
    n = 0
    for i in enemy_2_1_list:
        collision = False
        rectB = i[0][i[8]].get_rect(center=i[1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (i[1][0] + 15, i[1][1] + 25)
        collision = rectB.colliderect(a)
        if collision and i[3] <= 0:
            player.mana += 3

            player.folie -= 5

            enemy_2_1_list[n][2] -= strenght
            enemy_2_1_list[n][3] = 30
            if player.last_move_is_up or player.last_move_is_right:
                enemy_2_1_list[n][5][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                enemy_2_1_list[n][5][0] = -knockback

            if enemy_2_1_list[n][2] <= 0:
                del enemy_2_1_list[n]
                player.folie -= 30

        n += 1
    n = 0
    for i in enemy_3_1_list:
        collision = False
        rectB = i[0][0].get_rect(center=i[1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (i[1][0] + 15, i[1][1] + 25)
        collision = rectB.colliderect(a)
        if collision and i[3] <= 0 and i[6]:
            player.mana += 3

            player.folie -= 5

            enemy_3_1_list[n][2] -= strenght
            enemy_3_1_list[n][3] = 30
            if player.last_move_is_up or player.last_move_is_right:
                enemy_3_1_list[n][5][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                enemy_3_1_list[n][5][0] = -knockback

            if enemy_3_1_list[n][2] <= 0:
                del enemy_3_1_list[n]
                player.folie -= 30

        n += 1
    n = 0
    for i in enemy_2_2_list:
        collision = False
        rectB = i[0][0].get_rect(center=i[1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (i[1][0] + 15, i[1][1] + 25)
        collision = rectB.colliderect(a)
        if collision and i[3] <= 0:
            player.mana += 3

            player.folie -= 5

            enemy_2_2_list[n][2] -= strenght
            enemy_2_2_list[n][3] = 30
            if player.last_move_is_up or player.last_move_is_right:
                enemy_2_2_list[n][5][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                enemy_2_2_list[n][5][0] = -knockback

            if enemy_2_2_list[n][2] <= 0:
                del enemy_2_2_list[n]
                player.folie -= 30

        n += 1
    n = 0
    for i in boss_list:

        rectB = boss_list[n][0][0].get_rect(center=boss_list[n][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (boss_list[n][1][0] + 23, boss_list[n][1][1] + 40)

        collision = rectB.colliderect(a)
        if collision and i[8] <= 0:
            player.mana += 3

            player.folie -= 5
            boss_list[n][2] -= strenght
            boss_list[n][6] = 10
            boss_list[n][8] = 30
            if player.last_move_is_up or player.last_move_is_right:
                boss_list[n][7][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                boss_list[n][7][0] = -knockback
            if boss_list[n][2] <= 0:
                if boss_list[n][4] == 0:
                    boss_list[n][4] += 0.01
                    boss_list[n][2] = 100
                    player.folie -= 50

                elif boss_list[n][4] == 1:
                    boss_list[n][4] += 0.01
                    boss_list[n][2] = 80
                    player.folie -= 120

                elif boss_list[n][4] == 2:
                    del boss_list[n]
                    player.folie -= 70
                    if len(boss_list) == 0:
                        player.dash_unlocked=True
                        world.next_level()

        n += 1
    n = 0
    for i in enemy_slime_list:

        collision = False
        rectB = i[0].get_rect()
        rectB.h = 20
        rectB.w = 30
        rectB.center = (i[1][0] + 15, i[1][1] + 10)
        collision = rectB.colliderect(a)
        print(collision)
        if collision and i[3] <= 0:
            #player.mana += 3
            player.folie -= 3

            enemy_slime_list[n][2] -= strenght
            enemy_slime_list[n][3] = 30
            if player.last_move_is_up or player.last_move_is_right:
                enemy_slime_list[n][5][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                enemy_slime_list[n][5][0] = -knockback

            if enemy_slime_list[n][2] <= 0:
                #player.folie -= 30
                del enemy_slime_list[n]
        n += 1
    n = 0
    for i in enemy_4_1_list:
        collision = False
        rectB = i[0].get_rect(center=i[1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (i[1][0] + 15, i[1][1] + 25)
        collision = rectB.colliderect(a)
        if collision and i[3] <= 0:
            player.mana += 3

            player.folie -= 5

            enemy_4_1_list[n][2] -= strenght
            enemy_4_1_list[n][3] = 30
            if player.last_move_is_up or player.last_move_is_right:
                enemy_4_1_list[n][5][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                enemy_4_1_list[n][5][0] = -knockback

            if enemy_4_1_list[n][2] <= 0:
                del enemy_4_1_list[n]
                player.folie -= 30

        n += 1
    n = 0
    for i in enemy_4_2_list:
        collision = False
        rectB = i[0][i[8]].get_rect(center=i[1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (i[1][0] + 15, i[1][1] + 25)
        collision = rectB.colliderect(a)
        if collision and i[3] <= 0:
            player.mana += 3

            player.folie -= 5

            enemy_4_2_list[n][2] -= strenght
            enemy_4_2_list[n][3] = 30
            if player.last_move_is_up or player.last_move_is_right:
                enemy_4_2_list[n][5][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                enemy_4_2_list[n][5][0] = -knockback

            if enemy_4_2_list[n][2] <= 0:
                del enemy_4_2_list[n]
                player.folie -= 30

        n += 1
    n = 0
    for i in boss_list_4:

        rectB = boss_list_4[n][0][0].get_rect(center=boss_list_4[n][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (boss_list_4[n][1][0] + 23, boss_list_4[n][1][1] + 40)

        collision = rectB.colliderect(a)
        if collision and i[8] <= 0:
            player.mana += 3

            player.folie -= 5
            boss_list_4[n][2] -= strenght
            boss_list_4[n][6] = 10
            boss_list_4[n][8] = 30
            if player.last_move_is_up or player.last_move_is_right:
                boss_list_4[n][7][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                boss_list_4[n][7][0] = -knockback
            if boss_list_4[n][2] <= 0:
                if boss_list_4[n][4] == 0:
                    boss_list_4[n][4] += 0.01
                    boss_list_4[n][2] = 100
                    player.folie -= 50

                elif boss_list_4[n][4] == 1:
                    boss_list_4[n][4] += 0.01
                    boss_list_4[n][2] = 80
                    player.folie -= 120

                elif boss_list_4[n][4] == 2:
                    del boss_list_4[n]
                    player.folie -= 70
                    if len(boss_list) == 0:
                        player.dash_unlocked=True
                        world.next_level()

        n += 1
    if player.mana > player.mana_max:
        player.mana=player.mana_max