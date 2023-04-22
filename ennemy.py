import math
import random

import pygame

import graphic_main
import player
import tiles
import world

enemy_1_list = []
enemy_1_2_list = []
enemy_2_1_list = []
enemy_2_2_list = []
enemy_3_1_list = []

boss_1_dial = []
boss_2_dial = []
boss_3_dial = []
boss_4_dial = []
boss_final_dial = []

boss_list = []
projectile_list = []
enemy_slime_list = []
enemy_4_1_list = []
enemy_4_2_list = []
enemy_3_2_list = []

boss_list_4 = []
boss_list_2 = []
boss_list_3 = []
final_boss = []


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
    enemy_3_1_list.append([img_, pos, pv + 10, 10, [False, False, False, False], [0, 0], False, 10, 0,
                           [proj_1, proj_2, pygame.transform.rotate(proj_1, 90), pygame.transform.rotate(proj_2, 90),
                            pygame.transform.rotate(proj_1, 180), pygame.transform.rotate(proj_2, 180),
                            pygame.transform.rotate(proj_1, -90), pygame.transform.rotate(proj_2, -90)]])


def spawn_enemy_2_2(pos, img, pv):
    img_ = []
    n = 0
    for i in img:
        img_.append(pygame.image.load(i).convert_alpha())

        n += 1
    pos = pos
    global enemy_2_2_list
    enemy_2_2_list.append([img_, pos, pv, 10, [False, False, False, False], [0, 0], False, 10, [0, 0]])


def spawm_projectile(pos, radius, directon, color, img=None, dgt=[30, 0]):
    global projectile_list
    projectile_list.append([pos, radius, directon, color, img, dgt])


def spawn_enemy_1(pos, img, pv):
    img = pygame.transform.scale(pygame.image.load(img).convert_alpha(), [28, 50])
    pos = pos
    global enemy_1_list
    enemy_1_list.append([img, pos, pv, 10, [False, False, False, False], [0, 0]])


def spawn_enemy_3_2(pos, img, pv):
    _img = []
    for i in img:
        _img.append(pygame.image.load(i).convert_alpha())
    pos = pos
    global enemy_1_2_list
    enemy_3_2_list.append([_img, pos, pv + 10, 10, [False, False, False, False], [0, 0], [0, 0], 0, 0])


def spawn_enemy_1_2(pos, img, pv):
    _img = []
    for i in img:
        _img.append(pygame.transform.scale(pygame.image.load(i).convert_alpha(), [49, 23]))
    pos = pos
    global enemy_1_2_list
    enemy_1_2_list.append([_img, pos, pv, 10, [False, False, False, False], [0, 0], [0, 0], 0, 0])


def spawn_boss_1(pos, pv):
    global boss_1_dial
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
    boss_list.append([_img, pos, pv, [False, False, False, False], -1, 0, 0, [0, 0], 0, [0, 0], 0])
    boss_1_dial = [pygame.image.load('picture/ui/dialogue_boss_1_1.png').convert_alpha(),
                   pygame.transform.scale(pygame.image.load('picture/ui/Etage -5 fin.pdf (3).png').convert_alpha(),
                                          [368, 90])]


def spawn_boss_2(pos, pv, is_reel=True):
    global boss_2_dial
    _img = []
    _img.append(pygame.transform.scale(pygame.image.load('picture/enemy/spider boss/spider_boss_1.png').convert_alpha(),
                                       [50, 45]))
    _img.append(pygame.transform.scale(pygame.image.load('picture/enemy/spider boss/spider_boss_2.png').convert_alpha(),
                                       [50, 45]))
    _img.append(pygame.transform.scale(pygame.image.load('picture/enemy/spider boss/spider_boss_3.png').convert_alpha(),
                                       [50, 45]))

    boss_list_2.append([_img, pos, pv, [False, False, False, False], -1, 0, 0, [0, 0], 0, [0, 0], 0, [0, 0], is_reel])
    boss_2_dial = [
        pygame.transform.scale(pygame.image.load('picture/ui/Etage -4 d�but.pdf (3).png').convert_alpha(), [368, 90]),
        pygame.transform.scale(pygame.image.load('picture/ui/Etage -4 fin.pdf (3).png').convert_alpha(), [368, 90])]


def spawn_boss_3(pos, pv):
    global boss_3_dial
    _img = []
    _img.append(
        pygame.transform.scale(pygame.image.load('picture/enemy/Red_boss/RedBoss_face_standing.png').convert_alpha(),
                               [52, 94]))

    boss_list_3.append([_img, pos, pv, [False, False, False, False], -1, 0, 0, [0, 0], 0, [0, 0], 0, [], [], 0])
    boss_3_dial = [
        pygame.transform.scale(pygame.image.load('picture/ui/Etage -3 d�but.pdf (3).png').convert_alpha(), [368, 100]),
        pygame.transform.scale(pygame.image.load('picture/ui/Etage -3 fin.pdf (3).png').convert_alpha(), [368, 100])]

def spawn_boss_final(pos, pv):
    global boss_final_dial
    _img = []
    _img.append(pygame.transform.scale(pygame.image.load('picture/enemy/ange/ange_1.png').convert_alpha(), [70, 50]))
    _img.append(pygame.transform.scale(pygame.image.load('picture/enemy/ange/ange_2.png').convert_alpha(), [70, 50]))
    _img.append(pygame.transform.scale(pygame.image.load('picture/enemy/ange/ange_3.png').convert_alpha(), [70, 50]))
    _img.append(pygame.transform.scale(pygame.image.load('picture/enemy/ange/ange_4.png').convert_alpha(), [70, 50]))

    final_boss.append([_img, pos, pv, [False, False, False, False], -1, 0, 0, [0, 0], 0, [0, 0], 0, [], [], 0])

    boss_final_dial = [
        pygame.transform.scale(pygame.image.load('picture/ui/Etage -1 d�but.pdf (3).png').convert_alpha(), [368, 100]),
        pygame.transform.scale(pygame.image.load('picture/ui/Etage -1 fin p1.pdf (3).png').convert_alpha(), [368, 100]),
        pygame.transform.scale(pygame.image.load('picture/ui/Etage -1 fin p2.pdf (3).png').convert_alpha(), [368, 100]),
        pygame.transform.scale(pygame.image.load('picture/ui/Etage -1 fin p3.pdf (3).png').convert_alpha(), [368, 100]),
        pygame.transform.scale(pygame.image.load('picture/ui/Etage -1 fin combat.pdf (3).png').convert_alpha(), [368, 100])]

def spawn_boss_4(pos, pv):
    global boss_4_dial
    _img = []
    _img.append(pygame.image.load('picture/enemy/tortue/Boss_tortue_1.png'))

    boss_list_4.append([_img, pos, pv, [False, False, False, False], -1, 0, 0, [0, 0], 0, [0, 0], 0])
    boss_4_dial = [
        pygame.transform.scale(pygame.image.load('picture/ui/Etage -2 d�but.pdf (3).png').convert_alpha(), [368, 100]),
        pygame.transform.scale(pygame.image.load('picture/ui/Etage -2 fin.pdf (3).png').convert_alpha(), [368, 90])]


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
    _img.append(
        pygame.transform.flip(pygame.transform.scale(pygame.image.load(img).convert_alpha(), [40, 40]), True, False))

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
    move_ennemi_3_2()
    move_projectile()
    move_boss_1()
    move_boss_final()
    move_ennemi_slime()
    move_ennemi_4_1()
    move_ennemi_4_2()
    move_boss_4()
    move_boss_2()
    move_boss_3()
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
    for i in enemy_3_2_list:
        if i[3] > 0:
            enemy_3_2_list[n][3] -= 1
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
    n = 0
    for i in boss_list_2:
        if i[6] > 0:
            boss_list_2[n][6] -= 1
        if i[8] > 0:
            boss_list_2[n][8] -= 1
        boss_list_2[n][5] -= 1

        n += 1
    n = 0
    for i in boss_list_3:
        if i[6] > 0:
            boss_list_3[n][6] -= 1
        if i[8] > 0:
            boss_list_3[n][8] -= 1
        boss_list_3[n][5] -= 1

        n += 1
    n = 0
    for i in final_boss:
        if i[6] > 0:
            final_boss[n][6] -= 1
        if i[8] > 0:
            final_boss[n][8] -= 1
        final_boss[n][5] -= 1

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

        if is_touch_wall(enemy_1_2_list[0][1], enemy_1_2_list[i][0][enemy_1_2_list[i][8]].get_rect()) or \
                enemy_1_2_list[i][6] == [0, 0]:
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


def move_ennemi_3_2():
    global enemy_3_2_list
    for i in range(0, len(enemy_3_2_list)):
        rectB = enemy_3_2_list[i][0][enemy_3_2_list[i][8]].get_rect(center=enemy_3_2_list[i][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (enemy_3_2_list[i][1][0] + 15, enemy_3_2_list[i][1][1] + 25)
        dist = math.sqrt(
            (enemy_3_2_list[i][1][0] - player.pos[0]) ** 2 + (enemy_3_2_list[i][1][1] - player.pos[1]) ** 2)
        enemy_3_2_list[i][4][0] = False
        enemy_3_2_list[i][4][1] = False
        enemy_3_2_list[i][4][2] = False
        enemy_3_2_list[i][4][3] = False

        if is_touch_wall(enemy_3_2_list[i][1], enemy_3_2_list[i][0][enemy_3_2_list[i][8]].get_rect()) or \
                enemy_3_2_list[i][6] == [0, 0]:
            dir_to_player = [-3 * (enemy_3_2_list[i][1][0] - player.pos[0]) / (
                    abs(enemy_3_2_list[i][1][1] - player.pos[1]) + abs((enemy_3_2_list[i][1][0] - player.pos[0]))),
                             -3 * (enemy_3_2_list[i][1][1] - player.pos[1]) / (
                                     abs(enemy_3_2_list[i][1][1] - player.pos[1]) + abs(
                                 enemy_3_2_list[i][1][0] - player.pos[0]))]
            enemy_3_2_list[i][6] = dir_to_player

        enemy_3_2_list[i][1] = touch_wall(enemy_3_2_list[i][1], enemy_3_2_list[i][0][enemy_3_2_list[i][8]].get_rect())

        if enemy_3_2_list[i][6][0] > 0:
            if enemy_3_2_list[i][6][0] > abs(enemy_3_2_list[i][6][1]):
                enemy_3_2_list[i][8] = 1
            else:
                if enemy_3_2_list[i][6][0] > 0:
                    enemy_3_2_list[i][8] = 3
                if enemy_3_2_list[i][6][0] < 0:
                    enemy_3_2_list[i][8] = 2
        elif enemy_3_2_list[i][6][0] < 0:
            if abs(enemy_3_2_list[i][6][0]) > abs(enemy_3_2_list[i][6][1]):
                enemy_3_2_list[i][8] = 0
            else:
                if enemy_3_2_list[i][6][1] > 0:
                    enemy_3_2_list[i][8] = 3
                if enemy_3_2_list[i][6][1] < 0:
                    enemy_3_2_list[i][8] = 2

        if enemy_3_2_list[i][3] % 2 == 0 and enemy_3_2_list[i][3] > 0:
            enemy_3_2_list[i][1][0] += enemy_3_2_list[i][5][0]



        else:
            if (enemy_3_2_list[i][1][0] - player.pos[0]) >= 0:
                enemy_3_2_list[i][1][0] += enemy_3_2_list[i][6][0] * 3
                enemy_3_2_list[i][4][0] = True

            elif (enemy_3_2_list[i][1][0] - player.pos[0]) <= 0:
                enemy_3_2_list[i][1][0] += enemy_3_2_list[i][6][0] * 3
                enemy_3_2_list[i][4][1] = True

            if (enemy_3_2_list[i][1][1] - player.pos[1]) >= 0:
                enemy_3_2_list[i][1][1] += enemy_3_2_list[i][6][1] * 3

                enemy_3_2_list[i][4][2] = True

            elif (enemy_3_2_list[i][1][1] - player.pos[1]) <= 0:
                enemy_3_2_list[i][1][1] += enemy_3_2_list[i][6][1] * 3

                enemy_3_2_list[i][4][3] = True

        enemy_3_2_list[i][7] += 1 / 20


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
                                      (player.pos[1] - enemy_2_1_list[i][1][1]) / total * 5], (75, 0, 130), None,
                                     [15, 20])
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
                enemy_2_1_list[i][7] = 100


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
                enemy_2_2_list[i][8][0] = max((min((enemy_2_2_list[i][8][
                                                        0] + random.random() * 100 - random.random() * 100,
                                                    graphic_main.right - 100)), graphic_main.left + 50))
                enemy_2_2_list[i][8][1] = max((min((enemy_2_2_list[i][8][
                                                        1] + random.random() * 100 - random.random() * 100,
                                                    graphic_main.bottom - 100)), graphic_main.top + 50))

            if -30 > enemy_2_2_list[i][7] > -50:
                graphic_main.update.append(pygame.draw.circle(graphic_main.screen, (0, 0, 0), (
                enemy_2_2_list[i][8][0] + 24, enemy_2_2_list[i][8][1] + 25), 20, 0))
            if enemy_2_2_list[i][7] == -50:
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
    if -1 <= boss_list[0][4] < 0:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('picture/musique/musique_boss.mp3')
        pygame.mixer.music.play(loops=-1)
        boss_list[0][4] += 0.005
        graphic_main.update.append(graphic_main.screen.blit(boss_1_dial[0], (
        pygame.display.get_surface().get_size()[0] / 2 - 368 / 2, pygame.display.get_surface().get_size()[1] / 5 * 4)))
        if boss_list[0][4] > 0:
            boss_list[0][4] = 0
            if len(boss_list) > 1:
                boss_list = [boss_list[0]]
            graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (0, 0, 0), pygame.Rect((
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        0] / 2 - 368 / 2,
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        1] / 5 * 4, 368,
                                                                                                    62))))
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
    if 0 < boss_list[0][4] < 1:
        boss_list[0][4] += 0.01
        if 0.5 < boss_list[0][4] < 0.51:
            boss_list[0][4] = 0.5
        if boss_list[0][4] == 0.5:
            boss_list[0][10] += 2
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
        # boss_list[0][1] = touch_wall(boss_list[0][1], boss_list[0][0][0].get_rect())

        boss_list[0][3][0] = False
        boss_list[0][3][1] = False
        boss_list[0][3][2] = False
        boss_list[0][3][3] = False

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
        if 1.17 < boss_list[0][4] < 1.18:
            boss_list[0][4] = 1.17
        if boss_list[0][4] == 1.17:
            boss_list[0][10] = 16
        if 1.26 < boss_list[0][4] < 1.27:
            boss_list[0][4] = 1.26
        if boss_list[0][4] == 1.26:
            boss_list[0][10] += 1
        if 1.5 < boss_list[0][4] < 1.51:
            boss_list[0][4] = 1.5
        if boss_list[0][4] == 1.5:
            boss_list[0][10] += 1
        if 1.7 < boss_list[0][4] < 1.71:
            boss_list[0][4] = 1.7
        if boss_list[0][4] == 1.7:
            boss_list[0][10] += 1
        if 1.92 < boss_list[0][4] < 1.93:
            boss_list[0][4] = 1.92
        if boss_list[0][4] == 1.92:
            boss_list[0][10] += 1
        if boss_list[0][4] >= 2:
            spawn_boss_1([boss_list[0][1][0] + 90, boss_list[0][1][1]], 100)
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
            # dist = math.sqrt((boss_list[0][1][0] - player.pos[0]) ** 2 + (boss_list[0][1][1] - player.pos[1]) ** 2)

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
                    boss_list[i][10] = 4 + 6 * i

                elif (boss_list[i][1][0] - player.pos[0]) <= 0:
                    boss_list[i][1][0] += boss_list[i][9][0] * 1 + math.cos(boss_list[i][5]) * 2.5
                    boss_list[i][3][1] = True
                    boss_list[i][10] = 7 + 6 * i

                if (boss_list[i][1][1] - player.pos[1]) >= 0:
                    boss_list[i][1][1] += boss_list[i][9][1] * 1 + math.sin(boss_list[i][5]) * 2.5

                    boss_list[i][3][2] = True
                elif (boss_list[i][1][1] - player.pos[1]) <= 0:
                    boss_list[i][1][1] += boss_list[i][9][1] * 1 + math.sin(boss_list[i][5]) * 2.5

                    boss_list[i][3][3] = True
            boss_list[i][5] += 1 / 20
    if 2 < boss_list[0][4] < 3:
        boss_list[0][4] += 0.005
        graphic_main.update.append(graphic_main.screen.blit(boss_1_dial[1], (
        pygame.display.get_surface().get_size()[0] / 2 - 368 / 2, pygame.display.get_surface().get_size()[1] / 5 * 4)))
        if boss_list[0][4] > 3:
            boss_list[0][4] = 3
            graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (0, 0, 0), pygame.Rect((
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        0] / 2 - 368 / 2,
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        1] / 5 * 4, 368,
                                                                                                    62))))
            boss_list = []

            player.dash_unlocked = True
            world.next_level()
            player.xp += 100


def move_boss_2():
    global boss_list_2
    if not boss_list_2:
        return
    if -1 <= boss_list_2[0][4] < 0:
        pygame.mixer.music.stop()
        #pygame.mixer.music.load('picture/musique/musique_boss_2.mp3')
        #pygame.mixer.music.play(loops=-1)
        boss_list_2[0][4] += 0.005
        graphic_main.update.append(graphic_main.screen.blit(boss_2_dial[0], (
        pygame.display.get_surface().get_size()[0] / 2 - 368 / 2, pygame.display.get_surface().get_size()[1] / 5 * 4)))
        if boss_list_2[0][4] > 0:
            boss_list_2[0][4] = 0
            if len(boss_list_2) > 1:
                boss_list_2 = [boss_list_2[0]]
            graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (0, 0, 0), pygame.Rect((
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        0] / 2 - 368 / 2,
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        1] / 5 * 4, 368,
                                                                                                    90))))

    if boss_list_2[0][4] == 0:
        rectB = boss_list_2[0][0][0].get_rect(center=boss_list_2[0][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (boss_list_2[0][1][0] + 15, boss_list_2[0][1][1] + 25)
        dist = math.sqrt(
            (boss_list_2[0][1][0] - player.pos[0]) ** 2 + (boss_list_2[0][1][1] - player.pos[1]) ** 2)
        boss_list_2[0][1] = touch_wall(boss_list_2[0][1], (20, 20))
        if boss_list_2[0][6] % 2 == 0 and boss_list_2[0][6] > 0:
            boss_list_2[0][1][0] += boss_list_2[0][7][0]

        if boss_list_2[0][5] < 0:
            boss_list_2[0][6] = True
        if boss_list_2[0][6] == True:
            if boss_list_2[0][5] == -1:
                boss_list_2[0][9] = random.randrange(0, 2)
                if boss_list_2[0][9] == 1:
                    if abs(boss_list_2[0][1][1] - player.pos[1]) + abs((boss_list_2[0][1][0] - player.pos[0])) != 0:
                        dir_to_player = [-12 * (boss_list_2[0][1][0] - player.pos[0]) / (
                                abs(boss_list_2[0][1][1] - player.pos[1]) + abs(
                            (boss_list_2[0][1][0] - player.pos[0]))),
                                         -12 * (boss_list_2[0][1][1] - player.pos[1]) / (
                                                 abs(boss_list_2[0][1][1] - player.pos[1]) + abs(
                                             boss_list_2[0][1][0] - player.pos[0]))]
                        boss_list_2[0][11] = dir_to_player
                    else:
                        boss_list_2[0][11] = [12, 12]
                if boss_list_2[0][9] == 0:
                    boss_list_2[0][11] = (player.pos[0], player.pos[1])
                    boss_list_2[0][1] = [-100000, -100000]

            if boss_list_2[0][5] < -1:
                if boss_list_2[0][9] == 1:

                    boss_list_2[0][1][0] += boss_list_2[0][11][0]
                    boss_list_2[0][1][1] += boss_list_2[0][11][1]
                    if is_touch_wall(boss_list_2[0][1], (40, 40)):
                        boss_list_2[0][5] = 10

            if boss_list_2[0][5] == -30:
                if boss_list_2[0][9] == 0:
                    boss_list_2[0][1] = [boss_list_2[0][11][0], boss_list_2[0][11][1]]
                    boss_list_2[0][5] = 30
    if 0 < boss_list_2[0][4] < 1:
        boss_list_2[0][4] += 0.01

        if boss_list_2[0][4] > 1:
            boss_list_2[0][4] = 1
            boss_list_2[0][5] = 60
            boss_list_2[0][2] = 80

            for i in range(0, 5):
                spawn_boss_2([-10000, -10000], 50, False)
                boss_list_2[i + 1][10] = 2
                boss_list_2[i + 1][4] = 1
                boss_list_2[i + 1][1] = [random.randrange(graphic_main.left + 50, graphic_main.right - 50),
                                         random.randrange(graphic_main.top + 50, graphic_main.bottom - 50)]

            boss_list_2[0][11] = [0, 0]
            boss_list_2[0][5] = 20
    if boss_list_2[0][4] == 1:

        for i in range(0, len(boss_list_2)):
            rectB = boss_list_2[i][0][0].get_rect(center=boss_list_2[i][1])
            rectB.h = 90
            rectB.w = 46
            rectB.center = (boss_list_2[i][1][0] + 23, boss_list_2[i][1][1] + 40)
            # zadezd = pygame.draw.rect(graphic_main.screen, (255, 255, 255), rectB)
            # graphic_main.update.append(zadezd)
            dist = math.sqrt((boss_list_2[0][1][0] - player.pos[0]) ** 2 + (boss_list_2[0][1][1] - player.pos[1]) ** 2)
            if boss_list_2[i][5] == -1:
                boss_list_2[i][3][0] = False
                boss_list_2[i][3][1] = False
                boss_list_2[i][3][2] = False
                boss_list_2[i][3][3] = False
                if random.random() < 1 / len(boss_list_2):
                    if abs(boss_list_2[i][1][1] - player.pos[1]) + abs((boss_list_2[i][1][0] - player.pos[0])) != 0:
                        dir_to_player = [-6 * (boss_list_2[i][1][0] - player.pos[0]) / (
                                abs(boss_list_2[i][1][1] - player.pos[1]) + abs(
                            (boss_list_2[i][1][0] - player.pos[0]))),
                                         -6 * (boss_list_2[i][1][1] - player.pos[1]) / (
                                                 abs(boss_list_2[i][1][1] - player.pos[1]) + abs(
                                             boss_list_2[i][1][0] - player.pos[0]))]
                        boss_list_2[i][11] = dir_to_player
                    else:
                        boss_list_2[i][11] = [12, 12]
                else:
                    boss_list_2[i][5] = 20
            if boss_list_2[i][5] < -1:
                boss_list_2[i][1][0] += boss_list_2[i][11][0]
                boss_list_2[i][1][1] += boss_list_2[i][11][1]
            if boss_list_2[i][5] < -1:

                if is_touch_wall(boss_list_2[i][1], (40, 40)):
                    boss_list_2[i][5] = 50
                    boss_list_2[i][11] = [0, 0]
                    # boss_list_2[i][1] = [-10000, -10000]
            if boss_list_2[i][6] % 2 == 0 and boss_list_2[i][6] > 0:
                boss_list_2[i][1][0] += boss_list_2[i][7][0]

            boss_list_2[i][1] = touch_wall(boss_list_2[i][1], (20, 20))

    if 1 < boss_list_2[0][4] < 2:
        boss_list_2[0][4] += 0.01
        """ if 1.17 < boss_list_2[0][4] < 1.18:
            boss_list_2[0][4]=1.17
        if boss_list_2[0][4] == 1.17:
            boss_list_2[0][10] = 16
        if 1.26 < boss_list_2[0][4] < 1.27:
            boss_list_2[0][4]=1.26
        if boss_list_2[0][4] == 1.26:
            boss_list_2[0][10] += 1
        if 1.5 < boss_list_2[0][4] < 1.51:
            boss_list_2[0][4]=1.5
        if boss_list_2[0][4] == 1.5:
            boss_list_2[0][10] += 1
        if 1.7 < boss_list_2[0][4] < 1.71:
            boss_list_2[0][4]=1.7
        if boss_list_2[0][4] == 1.7:
            boss_list_2[0][10] += 1
        if 1.92 < boss_list_2[0][4] < 1.93:
            boss_list_2[0][4]=1.92
        if boss_list_2[0][4] == 1.92:
            boss_list_2[0][10] += 1"""
        if boss_list_2[0][4] >= 2:

            # spawn_boss_4([boss_list_2[0][1][0]+90, boss_list_2[0][1][1]], 100)
            boss_list_2[0][2] = 100
            boss_list_2[0][4] = 2
            boss_list_2[0][5] = 20
            for i in range(0, 5):
                spawn_boss_2([-10000, -10000], 70, False)
                boss_list_2[i + 1][10] = 2
                boss_list_2[i + 1][4] = 1
                boss_list_2[i + 1][1] = [random.randrange(graphic_main.left + 50, graphic_main.right - 50),
                                         random.randrange(graphic_main.top + 50, graphic_main.bottom - 50)]

            boss_list_2[0][11] = [0, 0]
            boss_list_2[0][5] = 20
    if boss_list_2[0][4] == 2:
        for i in range(0, len(boss_list_2)):
            rectB = boss_list_2[i][0][0].get_rect(center=boss_list_2[i][1])
            rectB.h = 40
            rectB.w = 15
            rectB.center = (boss_list_2[i][1][0] + 15, boss_list_2[i][1][1] + 25)

            boss_list_2[i][1] = touch_wall(boss_list_2[i][1], (20, 20))
            if boss_list_2[i][6] % 2 == 0 and boss_list_2[i][6] > 0:
                boss_list_2[i][1][0] += boss_list_2[i][7][0]

            if boss_list_2[i][5] < 0:
                boss_list_2[i][6] = True
            if boss_list_2[i][6] == True:
                if boss_list_2[i][5] == -1:
                    boss_list_2[i][9] = random.randrange(0, 2)
                    if boss_list_2[i][9] == 1:
                        if abs(boss_list_2[i][1][1] - player.pos[1]) + abs((boss_list_2[i][1][0] - player.pos[0])) != 0:
                            dir_to_player = [-12 * (boss_list_2[i][1][0] - player.pos[0]) / (
                                    abs(boss_list_2[i][1][1] - player.pos[1]) + abs(
                                (boss_list_2[i][1][0] - player.pos[0]))),
                                             -12 * (boss_list_2[i][1][1] - player.pos[1]) / (
                                                     abs(boss_list_2[i][1][1] - player.pos[1]) + abs(
                                                 boss_list_2[i][1][0] - player.pos[0]))]
                            boss_list_2[i][11] = dir_to_player
                        else:
                            boss_list_2[i][11] = [12, 12]
                    if boss_list_2[i][9] == 0:
                        boss_list_2[i][11] = (player.pos[0], player.pos[1])
                        boss_list_2[i][1] = [-100000, -100000]

                if boss_list_2[i][5] < -1:
                    if boss_list_2[i][9] == 1:

                        boss_list_2[i][1][0] += boss_list_2[i][11][0]
                        boss_list_2[i][1][1] += boss_list_2[i][11][1]
                        if is_touch_wall(boss_list_2[i][1], (40, 40)):
                            boss_list_2[i][5] = 10

                if boss_list_2[i][5] == -30:
                    if boss_list_2[i][9] == 0:
                        boss_list_2[i][1] = [boss_list_2[i][11][0], boss_list_2[i][11][1]]
                        boss_list_2[i][5] = 30
        if 0 < boss_list_2[0][4] < 1:
            boss_list_2[0][4] += 0.01

            if boss_list_2[0][4] > 1:
                boss_list_2[0][4] = 1
                boss_list_2[0][5] = 60
                for i in range(0, 5):
                    spawn_boss_2([-10000, -10000], 10, False)
                    boss_list_2[i + 1][10] = 2
                    boss_list_2[i + 1][4] = 1
                    boss_list_2[i + 1][1] = [random.randrange(graphic_main.left + 50, graphic_main.right - 50),
                                             random.randrange(graphic_main.top + 50, graphic_main.bottom - 50)]

                boss_list_2[0][11] = [0, 0]
                boss_list_2[0][5] = 20
    if 2 < boss_list_2[0][4] < 3:
        graphic_main.update.append(graphic_main.screen.blit(boss_2_dial[1], (
        pygame.display.get_surface().get_size()[0] / 2 - 368 / 2, pygame.display.get_surface().get_size()[1] / 5 * 4)))
        boss_list_2[0][4] += 0.005
        if boss_list_2[0][4] >= 3:
            player.dash_invicibility_unlocked = True
            world.next_level()
            player.xp += 120


def move_ennemi_slime():
    global enemy_slime_list
    for i in range(0, len(enemy_slime_list)):
        rectB = enemy_slime_list[i][0].get_rect(center=enemy_slime_list[i][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (enemy_slime_list[i][1][0] + 15, enemy_slime_list[i][1][1] + 25)
        dist = math.sqrt(
            (enemy_slime_list[i][1][0] - player.pos[0]) ** 2 + (enemy_slime_list[i][1][1] - player.pos[1]) ** 2)
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
                        abs(enemy_slime_list[i][1][1] - player.pos[1]) + abs(
                    (enemy_slime_list[i][1][0] - player.pos[0])))) * 2
                enemy_slime_list[i][4][0] = True
            elif (enemy_slime_list[i][1][0] - player.pos[0]) <= 0:
                enemy_slime_list[i][1][0] += abs((enemy_slime_list[i][1][0] - player.pos[0]) / (
                        abs(enemy_slime_list[i][1][1] - player.pos[1]) + abs(
                    enemy_slime_list[i][1][0] - player.pos[0]))) * 2
                enemy_slime_list[i][4][1] = True
            if (enemy_slime_list[i][1][1] - player.pos[1]) >= 0:
                enemy_slime_list[i][1][1] -= abs((enemy_slime_list[i][1][1] - player.pos[1]) / (
                        abs(enemy_slime_list[i][1][1] - player.pos[1]) + abs(
                    enemy_slime_list[i][1][0] - player.pos[0]))) * 2
                enemy_slime_list[i][4][2] = True
            elif (enemy_slime_list[i][1][1] - player.pos[1]) <= 0:
                enemy_slime_list[i][1][1] += abs((enemy_slime_list[i][1][1] - player.pos[1]) / (
                        abs(enemy_slime_list[i][1][1] - player.pos[1]) + abs(
                    enemy_slime_list[i][1][0] - player.pos[0]))) * 2
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
            if enemy_4_1_list[i][7] == -1 and len(enemy_slime_list) / len(enemy_4_1_list) < 4:

                try:
                    total = abs(enemy_4_1_list[i][1][0] - player.pos[0]) + abs(enemy_4_1_list[i][1][1] - player.pos[1])
                    spawn_enemy_slime([enemy_4_1_list[i][1][0], enemy_4_1_list[i][1][1]],
                                      'picture/enemy/mage/slime.png', 20)

                except:
                    raise

            if enemy_4_1_list[i][7] == -30:
                enemy_4_1_list[i][6] = False
                enemy_4_1_list[i][7] = 20


def move_ennemi_4_2():
    global enemy_4_2_list
    for i in range(0, len(enemy_4_2_list)):
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
                enemy_4_2_list[i][1][1] -= abs((enemy_4_2_list[i][1][1] - player.pos[1])) / 5
                enemy_4_2_list[i][4][2] = True
            elif (enemy_4_2_list[i][1][1] - player.pos[1]) <= 0:
                enemy_4_2_list[i][1][1] += abs((enemy_4_2_list[i][1][1] - player.pos[1])) / 5
                enemy_4_2_list[i][4][3] = True

        if enemy_4_2_list[i][7] < 0:
            enemy_4_2_list[i][6] = True

        if enemy_4_2_list[i][6] == True:
            if enemy_4_2_list[i][7] == -1:

                try:
                    if enemy_4_2_list[i][8] == 0:
                        spawm_projectile([enemy_4_2_list[i][1][0] + 30, enemy_4_2_list[i][1][1] + 22], 5, [5, 0],
                                         (0, 0, 255), 5)
                    if enemy_4_2_list[i][8] == 1:
                        spawm_projectile([enemy_4_2_list[i][1][0] + 0, enemy_4_2_list[i][1][1] + 22], 5, [-5, 0],
                                         (0, 0, 255), 10)
                except:
                    raise

            if enemy_4_2_list[i][7] == -5:
                enemy_4_2_list[i][6] = False
                enemy_4_2_list[i][7] = 20


def move_boss_3():
    global boss_list_3
    if not boss_list_3:
        return
    if -1 <= boss_list_3[0][4] < 0:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('picture/musique/musique_boss_3.mp3')
        pygame.mixer.music.play(loops=-1)
        boss_list_3[0][4] += 0.005
        graphic_main.update.append(graphic_main.screen.blit(boss_3_dial[0], (pygame.display.get_surface().get_size()[0] / 2 - 368 / 2, pygame.display.get_surface().get_size()[1] / 5 * 4)))
        if boss_list_3[0][4] > 0:
            boss_list_3[0][4] = 0
            if len(boss_list_3) > 1:
                boss_list_3 = [boss_list_3[0]]
            graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (0, 0, 0), pygame.Rect((
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        0] / 2 - 368 / 2,
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        1] / 5 * 4, 368,
                                                                                                    100))))
            boss_list_3[0][5] = 0

    if boss_list_3[0][4] == 0:

        rectB = boss_list_3[0][0][0].get_rect(center=boss_list_3[0][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (boss_list_3[0][1][0] + 15, boss_list_3[0][1][1] + 25)
        dist = math.sqrt(
            (boss_list_3[0][1][0] - player.pos[0]) ** 2 + (boss_list_3[0][1][1] - player.pos[1]) ** 2)
        boss_list_3[0][1] = touch_wall(boss_list_3[0][1], (
            boss_list_3[0][0][0].get_rect().w,
            boss_list_3[0][0][0].get_rect().h))
        if boss_list_3[0][6] % 2 == 0 and boss_list_3[0][6] > 0:
            boss_list_3[0][1][0] += boss_list_3[0][7][0]

        if random.random() < 0.01:
            boss_list_3[0][1] = [2 * ((graphic_main.right - graphic_main.left) / 2 + graphic_main.left) - player.pos[0],
                                 2 * ((graphic_main.bottom - graphic_main.top) / 2 + graphic_main.top) - player.pos[1]]
        if boss_list_3[0][5] == -1:
            for i in boss_list_3[0][11]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_3_3)

            boss_list_3[0][11] = []
            boss_list_3[0][12] = []
            if boss_list_3[0][6] > 0:

                boss_list_3[0][11].append([int((boss_list_3[0][1][0] - graphic_main.left) / 50 - 1) * 50,
                                           int((boss_list_3[0][1][1] - graphic_main.top) / 50) * 50])
                boss_list_3[0][11].append([int((boss_list_3[0][1][0] - graphic_main.left) / 50 + 1) * 50,
                                           int((boss_list_3[0][1][1] - graphic_main.top) / 50) * 50])
                boss_list_3[0][11].append([int((boss_list_3[0][1][0] - graphic_main.left) / 50) * 50,
                                           int((boss_list_3[0][1][1] - graphic_main.top) / 50) * 50])
                boss_list_3[0][11].append([int((boss_list_3[0][1][0] - graphic_main.left) / 50) * 50,
                                           int((boss_list_3[0][1][1] - graphic_main.top) / 50 + 1) * 50])
                boss_list_3[0][11].append([int((boss_list_3[0][1][0] - graphic_main.left) / 50) * 50,
                                           int((boss_list_3[0][1][1] - graphic_main.top) / 50 - 1) * 50])
                boss_list_3[0][11].append([int((boss_list_3[0][1][0] - graphic_main.left) / 50 + 1) * 50,
                                           int((boss_list_3[0][1][1] - graphic_main.top) / 50 - 1) * 50])
                boss_list_3[0][11].append([int((boss_list_3[0][1][0] - graphic_main.left) / 50 + 1) * 50,
                                           int((boss_list_3[0][1][1] - graphic_main.top) / 50 + 1) * 50])
                boss_list_3[0][11].append([int((boss_list_3[0][1][0] - graphic_main.left) / 50 - 1) * 50,
                                           int((boss_list_3[0][1][1] - graphic_main.top) / 50 + 1) * 50])
                boss_list_3[0][11].append([int((boss_list_3[0][1][0] - graphic_main.left) / 50 - 1) * 50,
                                           int((boss_list_3[0][1][1] - graphic_main.top) / 50 - 1) * 50])

            else:
                boss_list_3[0][11].append([int((player.pos[0] - graphic_main.left) / 50 + 1) * 50,
                                           int((player.pos[1] - graphic_main.top) / 50) * 50])
                boss_list_3[0][11].append([int((player.pos[0] - graphic_main.left) / 50 - 1) * 50,
                                           int((player.pos[1] - graphic_main.top) / 50) * 50])
                boss_list_3[0][11].append([int((player.pos[0] - graphic_main.left) / 50) * 50,
                                           int((player.pos[1] - graphic_main.top) / 50) * 50])
                boss_list_3[0][11].append([int((player.pos[0] - graphic_main.left) / 50) * 50,
                                           int((player.pos[1] - graphic_main.top) / 50 + 1) * 50])
                boss_list_3[0][11].append([int((player.pos[0] - graphic_main.left) / 50) * 50,
                                           int((player.pos[1] - graphic_main.top) / 50 - 1) * 50])
                boss_list_3[0][11].append([int((player.pos[0] - graphic_main.left) / 50 + 1) * 50,
                                           int((player.pos[1] - graphic_main.top) / 50 - 1) * 50])
                boss_list_3[0][11].append([int((player.pos[0] - graphic_main.left) / 50 + 1) * 50,
                                           int((player.pos[1] - graphic_main.top) / 50 + 1) * 50])
                boss_list_3[0][11].append([int((player.pos[0] - graphic_main.left) / 50 - 1) * 50,
                                           int((player.pos[1] - graphic_main.top) / 50 + 1) * 50])
                boss_list_3[0][11].append([int((player.pos[0] - graphic_main.left) / 50 - 1) * 50,
                                           int((player.pos[1] - graphic_main.top) / 50 - 1) * 50])
            for i in boss_list_3[0][11]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_lave_1)

        if boss_list_3[0][5] == -15:
            for i in boss_list_3[0][11]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_lave_2)

        if boss_list_3[0][5] == -50:
            for i in boss_list_3[0][11]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_lave_3)
                boss_list_3[0][12].append(pygame.Rect(i[0] + graphic_main.left, i[1] + graphic_main.top, 50, 50))

        if boss_list_3[0][5] == -60:
            boss_list_3[0][5] = 20
        if boss_list_3[0][6] % 2 == 0 and boss_list_3[0][6] > 0:
            boss_list_3[0][1][0] += boss_list_3[0][7][0]
    if 0 < boss_list_3[0][4] < 1:
        boss_list_3[0][4] += 0.01
        if 0.5 < boss_list_3[0][4] < 0.51:
            boss_list_3[0][4] = 0.5
        if boss_list_3[0][4] == 0.5:
            boss_list_3[0][10] += 2
        if boss_list_3[0][4] > 1:
            boss_list_3[0][4] = 1
            boss_list_3[0][5] = 60
            boss_list_3[0][2] = 200

    if boss_list_3[0][4] == 1:

        rectB = boss_list_3[0][0][0].get_rect(center=boss_list_3[0][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (boss_list_3[0][1][0] + 23, boss_list_3[0][1][1] + 40)
        # zadezd = pygame.draw.rect(graphic_main.screen, (255, 255, 255), rectB)
        # graphic_main.update.append(zadezd)
        dist = math.sqrt((boss_list_3[0][1][0] - player.pos[0]) ** 2 + (boss_list_3[0][1][1] - player.pos[1]) ** 2)

        boss_list_3[0][3][0] = False
        boss_list_3[0][3][1] = False
        boss_list_3[0][3][2] = False
        boss_list_3[0][3][3] = False
        boss_list_3[0][1] = touch_wall(boss_list_3[0][1], (
            boss_list_3[0][0][0].get_rect().w,
            boss_list_3[0][0][0].get_rect().h))
        if boss_list_3[0][5] == -1:
            for i in boss_list_3[0][11]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_3_3)

            boss_list_3[0][11] = []
            boss_list_3[0][12] = []
            n = random.randrange(0, 9)

            if n == 0:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if (i + j) % 2 == 0:
                            boss_list_3[0][11].append([i * 50, j * 50])
            if n == 1:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if i % 2 == 0:
                            boss_list_3[0][11].append([i * 50, j * 50])
            if n == 2:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if j % 2 == 0:
                            boss_list_3[0][11].append([i * 50, j * 50])
            if n == 3:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if i % 2 == 1:
                            boss_list_3[0][11].append([i * 50, j * 50])
            if n == 4:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if j % 2 == 1:
                            boss_list_3[0][11].append([i * 50, j * 50])
            if n == 5:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if (i + j) % 3 == 0 or (i + j) % 5 == 2:
                            boss_list_3[0][11].append([i * 50, j * 50])
            if n == 6:
                pass
            if n == 7 or random.random() < 0.2:
                boss_list_3[0][1] = [
                    2 * ((graphic_main.right - graphic_main.left) / 2 + graphic_main.left) - player.pos[0],
                    2 * ((graphic_main.bottom - graphic_main.top) / 2 + graphic_main.top) - player.pos[1]]
            for i in boss_list_3[0][11]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_lave_1)

        if boss_list_3[0][5] == -15:
            for i in boss_list_3[0][11]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_lave_2)

        if boss_list_3[0][5] == -50:
            for i in boss_list_3[0][11]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_lave_3)
                boss_list_3[0][12].append(pygame.Rect(i[0] + graphic_main.left, i[1] + graphic_main.top, 50, 50))

        if boss_list_3[0][5] == -60:
            boss_list_3[0][5] = 20
        if boss_list_3[0][6] % 2 == 0 and boss_list_3[0][6] > 0:
            boss_list_3[0][1][0] += boss_list_3[0][7][0]
    if 1 < boss_list_3[0][4] < 2:
        boss_list_3[0][4] += 0.01
        if 1.17 < boss_list_3[0][4] < 1.18:
            boss_list_3[0][4] = 1.17
        if boss_list_3[0][4] == 1.17:
            boss_list_3[0][10] = 16
        if 1.26 < boss_list_3[0][4] < 1.27:
            boss_list_3[0][4] = 1.26
        if boss_list_3[0][4] == 1.26:
            boss_list_3[0][10] += 1
        if 1.5 < boss_list_3[0][4] < 1.51:
            boss_list_3[0][4] = 1.5
        if boss_list_3[0][4] == 1.5:
            boss_list_3[0][10] += 1
        if 1.7 < boss_list_3[0][4] < 1.71:
            boss_list_3[0][4] = 1.7
        if boss_list_3[0][4] == 1.7:
            boss_list_3[0][10] += 1
        if 1.92 < boss_list_3[0][4] < 1.93:
            boss_list_3[0][4] = 1.92
        if boss_list_3[0][4] == 1.92:
            boss_list_3[0][10] += 1
        if boss_list_3[0][4] >= 2:
            # spawn_boss_4([boss_list_3[0][1][0]+90, boss_list_3[0][1][1]], 100)
            boss_list_3[0][2] = 100
            boss_list_3[0][4] = 2
            boss_list_3[0][5] = 20
    if boss_list_3[0][4] == 2:
        rectB = boss_list_3[0][0][0].get_rect(center=boss_list_3[0][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (boss_list_3[0][1][0] + 23, boss_list_3[0][1][1] + 40)
        # zadezd = pygame.draw.rect(graphic_main.screen, (255, 255, 255), rectB)
        # graphic_main.update.append(zadezd)
        dist = math.sqrt((boss_list_3[0][1][0] - player.pos[0]) ** 2 + (boss_list_3[0][1][1] - player.pos[1]) ** 2)

        boss_list_3[0][3][0] = False
        boss_list_3[0][3][1] = False
        boss_list_3[0][3][2] = False
        boss_list_3[0][3][3] = False
        boss_list_3[0][1] = touch_wall(boss_list_3[0][1], (
            boss_list_3[0][0][0].get_rect().w,
            boss_list_3[0][0][0].get_rect().h))
        if boss_list_3[0][5] == -1:
            for i in boss_list_3[0][11]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_3_3)

            boss_list_3[0][11] = []
            boss_list_3[0][12] = []
            n = random.randrange(0, 14)

            if n == 0:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if random.random() < 0.6:
                            boss_list_3[0][11].append([i * 50, j * 50])

            if n == 1:
                a = [random.randrange(int(int(player.pos[0] - graphic_main.left) / 50) - 3,
                                      int(int(player.pos[0] - graphic_main.left) / 50) + 3),
                     random.randrange(int(int(player.pos[1] - graphic_main.top) / 50) - 3,
                                      int(int(player.pos[1] - graphic_main.top) / 50) + 3)]
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if i not in [a[0] - 1, a[0], a[0] + 1] or j not in [a[1] - 1, a[1], a[1] + 1]:
                            boss_list_3[0][11].append([i * 50, j * 50])

            if n == 2:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if (j + i) % 3 == 0 or (j + i) % 3 == 1:
                            boss_list_3[0][11].append([i * 50, j * 50])
            if n == 3:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if (j + i) % 3 == 0 or (j + i) % 3 == 2:
                            boss_list_3[0][11].append([i * 50, j * 50])
            if n == 4:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if (j + i) % 3 == 1 or (j + i) % 3 == 2:
                            boss_list_3[0][11].append([i * 50, j * 50])
            if n == 5:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if (i + j) % 3 == 0 or (i + j) % 5 == 2:
                            boss_list_3[0][11].append([i * 50, j * 50])
            if n == 6:
                pass

            if n == 7:
                pass
            if n == 12 or n == 13 or random.random() < 0.2:
                boss_list_3[0][1] = [
                    2 * ((graphic_main.right - graphic_main.left) / 2 + graphic_main.left) - player.pos[0],
                    2 * ((graphic_main.bottom - graphic_main.top) / 2 + graphic_main.top) - player.pos[1]]

            if n == 8:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if i % 2 == 0 or j % 2 == 1:
                            boss_list_3[0][11].append([i * 50, j * 50])
            if n == 9:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if i % 2 == 1 or j % 2 == 1:
                            boss_list_3[0][11].append([i * 50, j * 50])
            if n == 10:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if i % 2 == 0 or j % 2 == 0:
                            boss_list_3[0][11].append([i * 50, j * 50])
            if n == 11:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if i % 2 == 1 or j % 2 == 0:
                            boss_list_3[0][11].append([i * 50, j * 50])

            for i in boss_list_3[0][11]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_lave_1)

        if boss_list_3[0][5] == -15:
            for i in boss_list_3[0][11]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_lave_2)
            if not boss_list_3:
                boss_list_3[0][5] = 30

        if boss_list_3[0][5] == -30:
            for i in boss_list_3[0][11]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_lave_3)
                boss_list_3[0][12].append(pygame.Rect(i[0] + graphic_main.left, i[1] + graphic_main.top, 50, 50))

        if boss_list_3[0][5] == -60:
            boss_list_3[0][5] = 20
        if boss_list_3[0][6] % 2 == 0 and boss_list_3[0][6] > 0:
            boss_list_3[0][1][0] += boss_list_3[0][7][0]
    if 2< boss_list_3[0][4] < 3:
        boss_list_3[0][4] +=0.005
        graphic_main.update.append(graphic_main.screen.blit(boss_3_dial[1], (pygame.display.get_surface().get_size()[0] / 2 - 368 / 2, pygame.display.get_surface().get_size()[1] / 5 * 4)))
        if boss_list_3[0][4] > 3:
            boss_list_3 = []
            player.folie -= 70
            world.next_level()
            player.xp += 150

def move_boss_final():
    global final_boss
    if not final_boss:
        return
    if -1 <= final_boss[0][4] < 0:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('picture/musique/musique_boss_final.mp3')
        pygame.mixer.music.play(loops=-1)
        final_boss[0][4] += 0.005
        graphic_main.update.append(graphic_main.screen.blit(boss_final_dial[0], (pygame.display.get_surface().get_size()[0] / 2 - 368 / 2, pygame.display.get_surface().get_size()[1] / 5 * 4)))
        if final_boss[0][4] > 0:
            final_boss[0][4] = 0
            if len(final_boss) > 1:
                final_boss = [final_boss[0]]
            graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (0, 0, 0), pygame.Rect((
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        0] / 2 - 368 / 2,
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        1] / 5 * 4, 368,
                                                                                                    100))))
            final_boss[0][5] = 0

    if final_boss[0][4] == 0:
        final_boss[0][4] = 0
        final_boss[0][4] = 1.1

        #    final_boss.append([_img, pos, pv, [False, False, False, False], 0, 0, 0, [0, 0], 0, [0, 0], 0, [], [], 0])

        rectB = final_boss[0][0][0].get_rect(center=final_boss[0][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (final_boss[0][1][0] + 15, final_boss[0][1][1] + 25)
        dist = math.sqrt(
            (final_boss[0][1][0] - player.pos[0]) ** 2 + (final_boss[0][1][1] - player.pos[1]) ** 2)

        if final_boss[0][6] % 2 == 0 and final_boss[0][6] > 0:
            final_boss[0][1][0] += final_boss[0][7][0]

        if not final_boss[0][11] or is_touch_wall(final_boss[0][1], (
                final_boss[0][0][0].get_rect().w,
                final_boss[0][0][0].get_rect().h)) or final_boss[0][5] == 0:
            dir_to_player = [-3 * (final_boss[0][1][0] - player.pos[0]) / (
                    abs(final_boss[0][1][1] - player.pos[1]) + abs((final_boss[0][1][0] - player.pos[0]))),
                             -3 * (final_boss[0][1][1] - player.pos[1]) / (
                                     abs(final_boss[0][1][1] - player.pos[1]) + abs(
                                 final_boss[0][1][0] - player.pos[0]))]
            final_boss[0][11] = dir_to_player

        final_boss[0][1] = touch_wall(final_boss[0][1], (
            final_boss[0][0][0].get_rect().w,
            final_boss[0][0][0].get_rect().h))
        if final_boss[0][5] < 0:
            final_boss[0][1][0] += final_boss[0][11][0] * 2 + math.sin(final_boss[0][5] / 5) * 10
            final_boss[0][1][1] += final_boss[0][11][1] * 2 + math.cos(final_boss[0][5] / 5) * 10
        if random.random() < 0.005:
            final_boss[0][5] = 60
    print(final_boss[0][4])
    if 0 < final_boss[0][4] < 1:
        final_boss[0][4] += 0.005
        graphic_main.update.append(graphic_main.screen.blit(boss_final_dial[1], (pygame.display.get_surface().get_size()[0] / 2 - 368 / 2, pygame.display.get_surface().get_size()[1] / 5 * 4)))


        if final_boss[0][4] > 1:
            final_boss[0][4] = 1
            final_boss[0][5] = 60
            final_boss[0][2] = 200
            final_boss[0][11] = []
            final_boss[0][13] = 1
            graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (0, 0, 0), pygame.Rect((
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        0] / 2 - 368 / 2,
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        1] / 5 * 4, 368,
                                                                                                    100))))

    if final_boss[0][4] == 1:

        rectB = final_boss[0][0][0].get_rect(center=final_boss[0][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (final_boss[0][1][0] + 23, final_boss[0][1][1] + 40)
        # zadezd = pygame.draw.rect(graphic_main.screen, (255, 255, 255), rectB)
        # graphic_main.update.append(zadezd)
        dist = math.sqrt((final_boss[0][1][0] - player.pos[0]) ** 2 + (final_boss[0][1][1] - player.pos[1]) ** 2)
        if final_boss[0][6] % 2 == 0 and final_boss[0][6] > 0:
            final_boss[0][1][0] += final_boss[0][7][0]
            final_boss[0][5] = 10
        if final_boss[0][5] == -1:
            if random.random() <= 0.5:

                dir_to_player = [-3 * (final_boss[0][1][0] - player.pos[0]) / (
                        abs(final_boss[0][1][1] - player.pos[1]) + abs((final_boss[0][1][0] - player.pos[0]))),
                                 -3 * (final_boss[0][1][1] - player.pos[1]) / (
                                         abs(final_boss[0][1][1] - player.pos[1]) + abs(
                                     final_boss[0][1][0] - player.pos[0]))]
                final_boss[0][11] = [dir_to_player[0], dir_to_player[1], 0]
            else:
                final_boss[0][11] = [player.pos[0], player.pos[1], 1]
                final_boss[0][1] = [-1000000, -1000000]
        final_boss[0][1] = touch_wall(final_boss[0][1], (
            final_boss[0][0][0].get_rect().w,
            final_boss[0][0][0].get_rect().h))
        if final_boss[0][5] < -1:

            if final_boss[0][11][2] == 0:
                final_boss[0][1][0] += final_boss[0][11][0] * 5
                final_boss[0][1][1] += final_boss[0][11][1] * 5
                if is_touch_wall(final_boss[0][1], (
                        final_boss[0][0][0].get_rect().w,
                        final_boss[0][0][0].get_rect().h)):
                    final_boss[0][5] = 20
            if final_boss[0][11][2] == 1:
                if final_boss[0][5] == -20:
                    final_boss[0][1] = final_boss[0][11][:2]
                    final_boss[0][5] = 10

    if 1 < final_boss[0][4] < 2:
        final_boss[0][4] += 0.01
        graphic_main.update.append(graphic_main.screen.blit(boss_final_dial[2], (pygame.display.get_surface().get_size()[0] / 2 - 368 / 2, pygame.display.get_surface().get_size()[1] / 5 * 4)))

        if 1.17 < final_boss[0][4] < 1.18:
            final_boss[0][4] = 1.17
        if final_boss[0][4] == 1.17:
            final_boss[0][10] = 16
        if 1.26 < final_boss[0][4] < 1.27:
            final_boss[0][4] = 1.26
        if final_boss[0][4] == 1.26:
            final_boss[0][10] += 1
        if 1.5 < final_boss[0][4] < 1.51:
            final_boss[0][4] = 1.5
        if final_boss[0][4] == 1.5:
            final_boss[0][10] += 1
        if 1.7 < final_boss[0][4] < 1.71:
            final_boss[0][4] = 1.7
        if final_boss[0][4] == 1.7:
            final_boss[0][10] += 1
        if 1.92 < final_boss[0][4] < 1.93:
            final_boss[0][4] = 1.92
        if final_boss[0][4] == 1.92:
            final_boss[0][10] += 1
        if final_boss[0][4] >= 2:
            # spawn_boss_4([final_boss[0][1][0]+90, final_boss[0][1][1]], 100)
            final_boss[0][2] = 250
            final_boss[0][4] = 2
            final_boss[0][5] = 20
            final_boss[0][11] = []
            final_boss[0][13] = 2
            graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (0, 0, 0), pygame.Rect((
                pygame.display.get_surface().get_size()[
                    0] / 2 - 368 / 2,
                pygame.display.get_surface().get_size()[
                    1] / 5 * 4, 368,
                100))))

    if final_boss[0][4] == 2:
        rectB = final_boss[0][0][0].get_rect(center=final_boss[0][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (final_boss[0][1][0] + 23, final_boss[0][1][1] + 40)
        # zadezd = pygame.draw.rect(graphic_main.screen, (255, 255, 255), rectB)
        # graphic_main.update.append(zadezd)
        dist = math.sqrt((final_boss[0][1][0] - player.pos[0]) ** 2 + (final_boss[0][1][1] - player.pos[1]) ** 2)

        final_boss[0][3][0] = False
        final_boss[0][3][1] = False
        final_boss[0][3][2] = False
        final_boss[0][3][3] = False
        final_boss[0][1] = touch_wall(final_boss[0][1], (
            final_boss[0][0][0].get_rect().w,
            final_boss[0][0][0].get_rect().h))
        if not final_boss[0][11] or is_touch_wall(final_boss[0][1], (
                final_boss[0][0][0].get_rect().w,
                final_boss[0][0][0].get_rect().h)) or final_boss[0][5] == -2:
            dir_to_player = [-3 * (final_boss[0][1][0] - player.pos[0]) / (
                    abs(final_boss[0][1][1] - player.pos[1]) + abs((final_boss[0][1][0] - player.pos[0]))),
                             -3 * (final_boss[0][1][1] - player.pos[1]) / (
                                     abs(final_boss[0][1][1] - player.pos[1]) + abs(
                                 final_boss[0][1][0] - player.pos[0]))]
            final_boss[0][11][:2] = dir_to_player
        if final_boss[0][5] == -1:
            for i in final_boss[0][11][2:]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_3_3)

            final_boss[0][12] = []
            final_boss[0][11] = final_boss[0][11][:2]

            n = random.randrange(0, 14)

            if n == 0:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if random.random() < 0.6:
                            final_boss[0][11].append([i * 50, j * 50])

            if n == 1:
                a = [random.randrange(int(int(player.pos[0] - graphic_main.left) / 50) - 3,
                                      int(int(player.pos[0] - graphic_main.left) / 50) + 3),
                     random.randrange(int(int(player.pos[1] - graphic_main.top) / 50) - 3,
                                      int(int(player.pos[1] - graphic_main.top) / 50) + 3)]
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if i not in [a[0] - 1, a[0], a[0] + 1] or j not in [a[1] - 1, a[1], a[1] + 1]:
                            final_boss[0][11].append([i * 50, j * 50])

            if n == 2:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if (j + i) % 3 == 0 or (j + i) % 3 == 1:
                            final_boss[0][11].append([i * 50, j * 50])
            if n == 3:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if (j + i) % 3 == 0 or (j + i) % 3 == 2:
                            final_boss[0][11].append([i * 50, j * 50])
            if n == 4:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if (j + i) % 3 == 1 or (j + i) % 3 == 2:
                            final_boss[0][11].append([i * 50, j * 50])
            if n == 5:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if (i + j) % 3 == 0 or (i + j) % 5 == 2:
                            final_boss[0][11].append([i * 50, j * 50])
            if n == 6:
                pass

            if n == 7:
                pass
            if n == 12 or n == 13 or True:
                final_boss[0][1] = [
                    2 * ((graphic_main.right - graphic_main.left) / 2 + graphic_main.left) - player.pos[0],
                    2 * ((graphic_main.bottom - graphic_main.top) / 2 + graphic_main.top) - player.pos[1]]

            if n == 8:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if i % 2 == 0 or j % 2 == 1:
                            final_boss[0][11].append([i * 50, j * 50])
            if n == 9:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if i % 2 == 1 or j % 2 == 1:
                            final_boss[0][11].append([i * 50, j * 50])
            if n == 10:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if i % 2 == 0 or j % 2 == 0:
                            final_boss[0][11].append([i * 50, j * 50])
            if n == 11:
                for i in range(0, int((graphic_main.right - graphic_main.left) / 50)):
                    for j in range(0, int((graphic_main.bottom - graphic_main.top) / 50)):
                        if i % 2 == 1 or j % 2 == 0:
                            final_boss[0][11].append([i * 50, j * 50])
            a = 0
            for i in final_boss[0][11][2:]:
                a += 1
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_lave_1)

        if final_boss[0][5] == -15:
            for i in final_boss[0][11][2:]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_lave_2)
            if not final_boss:
                final_boss[0][5] = 30

        if final_boss[0][5] == -30:
            for i in final_boss[0][11][2:]:
                graphic_main.modifie(i[0] / 50, i[1] / 50, tiles.blit_tile_lave_3)
                final_boss[0][12].append(pygame.Rect(i[0] + graphic_main.left, i[1] + graphic_main.top, 50, 50))

        if final_boss[0][5] == -60:
            final_boss[0][5] = 20
        if final_boss[0][6] % 2 == 0 and final_boss[0][6] > 0:
            final_boss[0][1][0] += final_boss[0][7][0]

        if final_boss[0][5] < -1:
            final_boss[0][1][0] += final_boss[0][11][0] * 3
            final_boss[0][1][1] += final_boss[0][11][1] * 3
    if 2 < final_boss[0][4] < 3:
        final_boss[0][4] += 0.0025
        graphic_main.update.append(graphic_main.screen.blit(boss_final_dial[3], (pygame.display.get_surface().get_size()[0] / 2 - 368 / 2, pygame.display.get_surface().get_size()[1] / 5 * 4)))


        if final_boss[0][4] > 3:
            final_boss[0][4] = 3
            final_boss[0][5] = 60
            final_boss[0][2] = 350
            final_boss[0][11] = []
            final_boss[0][12] = []

            final_boss[0][13] = 3
            graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (0, 0, 0), pygame.Rect((
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        0] / 2 - 368 / 2,
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        1] / 5 * 4, 368,
                                                                                                    100))))
    if final_boss[0][4] == 3:

        rectB = final_boss[0][0][0].get_rect(center=final_boss[0][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (final_boss[0][1][0] + 23, final_boss[0][1][1] + 40)
        # zadezd = pygame.draw.rect(graphic_main.screen, (255, 255, 255), rectB)
        # graphic_main.update.append(zadezd)
        dist = math.sqrt((final_boss[0][1][0] - player.pos[0]) ** 2 + (final_boss[0][1][1] - player.pos[1]) ** 2)
        if final_boss[0][6] % 2 == 0 and final_boss[0][6] > 0:
            final_boss[0][1][0] += final_boss[0][7][0]
            final_boss[0][5] = 10
        if final_boss[0][5] == -1:
            final_boss[0][11] = [player.pos[0], player.pos[1]]
            final_boss[0][1] = [-1000000, -1000000]
        final_boss[0][1] = touch_wall(final_boss[0][1], (
            final_boss[0][0][0].get_rect().w,
            final_boss[0][0][0].get_rect().h))

        if final_boss[0][5] == -20:
            if random.random() < 1 / 2:
                final_boss[0][1] = final_boss[0][11]
            else:
                final_boss[0][1][0] = random.randrange(graphic_main.left + 50, graphic_main.right - 50)
                final_boss[0][1][1] = random.randrange(graphic_main.top + 50, graphic_main.bottom - 50)
            final_boss[0][5] = 20
            if random.random() < 1 / 4 and not len(enemy_4_1_list) + len(enemy_4_2_list) > 4:
                if random.random() < 0.5:
                    spawn_enemy_4_1([final_boss[0][1][0], final_boss[0][1][1]], 'picture/enemy/mage/Mage.png', 20)
                else:
                    spawn_enemy_4_2([final_boss[0][1][0], final_boss[0][1][1]], 'picture/enemy/snipe/mob_1.png', 20)
    if 3 < final_boss[0][4] < 4:
        final_boss[0][4] += 0.005
        graphic_main.update.append(graphic_main.screen.blit(boss_final_dial[0], (pygame.display.get_surface().get_size()[0] / 2 - 368 / 2, pygame.display.get_surface().get_size()[1] / 5 * 4)))
        if final_boss[0][4] >= 3:
            world.next_level()
            final_boss = []

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
        if enemy_3_1_list[i][6] == True:
            if enemy_3_1_list[i][7] == -1:
                enemy_3_1_list[i][8] = 1
            # if -1 < enemy_3_1_list[i][7] < -30:
            #    enemy_3_1_list[i][1] = [-10000, -10000]

            if enemy_3_1_list[i][7] == -40:
                spawm_projectile([enemy_3_1_list[i][1][0] + 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [5, 0], (75, 0, 130), enemy_3_1_list[i][9][4])
                spawm_projectile([enemy_3_1_list[i][1][0] + 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [5, 5], (75, 0, 130), enemy_3_1_list[i][9][3])
                spawm_projectile([enemy_3_1_list[i][1][0] + 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [0, 5], (75, 0, 130), enemy_3_1_list[i][9][2])
                spawm_projectile([enemy_3_1_list[i][1][0] + 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [-5, 5], (75, 0, 130), enemy_3_1_list[i][9][1])
                spawm_projectile([enemy_3_1_list[i][1][0] + 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [-5, 0], (75, 0, 130), enemy_3_1_list[i][9][0])
                spawm_projectile([enemy_3_1_list[i][1][0] + 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [-5, -5], (75, 0, 130), enemy_3_1_list[i][9][7])
                spawm_projectile([enemy_3_1_list[i][1][0] + 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [0, -5], (75, 0, 130), enemy_3_1_list[i][9][6])
                spawm_projectile([enemy_3_1_list[i][1][0] + 30, enemy_3_1_list[i][1][1] + 28], 10,
                                 [5, -5], (75, 0, 130), enemy_3_1_list[i][9][5])
                enemy_3_1_list[i][6] = False
                enemy_3_1_list[i][8] = 0
                enemy_3_1_list[i][7] = 120


def move_boss_4():
    global boss_list_4
    if not boss_list_4:
        return
    if -1 <= boss_list_4[0][4] < 0:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('picture/musique/musique_boss_4.mp3')
        pygame.mixer.music.play(loops=-1)
        boss_list_4[0][4] += 0.0025
        graphic_main.update.append(graphic_main.screen.blit(boss_4_dial[0], (
        pygame.display.get_surface().get_size()[0] / 2 - 368 / 2, pygame.display.get_surface().get_size()[1] / 5 * 4)))
        if boss_list_4[0][4] > 0:
            boss_list_4[0][4] = 0
            if len(boss_list_4) > 1:
                boss_list_4 = [boss_list_4[0]]
            graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (0, 0, 0), pygame.Rect((
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        0] / 2 - 368 / 2,
                                                                                                    pygame.display.get_surface().get_size()[
                                                                                                        1] / 5 * 4, 368,
                                                                                                    95))))
            boss_list_4[0][5] = 120

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
        if dist < 200:
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

        if dist < 100 and -10 >= boss_list_4[0][5] >= -20:
            boss_list_4[0][1][0] = random.randrange(graphic_main.left + 50, graphic_main.right - 50)
            boss_list_4[0][1][1] = random.randrange(graphic_main.top + 50, graphic_main.bottom - 50)
        if boss_list_4[0][5] < 0:
            boss_list_4[0][6] = True
        if boss_list_4[0][6] == True:
            if boss_list_4[0][5] == -1:

                try:

                    spawn_enemy_4_1([boss_list_4[0][1][0], boss_list_4[0][1][1]], 'picture/enemy/mage/Mage.png', 20)
                except:
                    raise

            if boss_list_4[0][5] == -20:
                boss_list_4[0][6] = False
                boss_list_4[0][5] = 120
    if 0 < boss_list_4[0][4] < 1:
        boss_list_4[0][4] += 0.01
        if 0.5 < boss_list_4[0][4] < 0.51:
            boss_list_4[0][4] = 0.5
        if boss_list_4[0][4] == 0.5:
            boss_list_4[0][10] += 2
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
        if boss_list_4[0][5] == 0:
            boss_list_4[0][1][0] = player.pos[0] + random.randrange(0, 50)
            boss_list_4[0][1][1] = player.pos[1] + random.randrange(0, 50)
            boss_list_4[0][5] = 120
        if boss_list_4[0][5] == 60:
            boss_list_4[0][1][0] = random.randrange(graphic_main.left + 50, graphic_main.right - 50)
            boss_list_4[0][1][1] = random.randrange(graphic_main.top + 50, graphic_main.bottom - 50)
        if 0 < boss_list_4[0][5] < 10:
            boss_list_4[0][1][0] += random.randrange(-10, 10)
            boss_list_4[0][1][1] += random.randrange(-10, 10)
        if boss_list_4[0][6] % 2 == 0 and boss_list_4[0][6] > 0:
            boss_list_4[0][1][0] += boss_list_4[0][7][0]

    if 1 < boss_list_4[0][4] < 2:
        boss_list_4[0][4] += 0.01
        if 1.17 < boss_list_4[0][4] < 1.18:
            boss_list_4[0][4] = 1.17
        if boss_list_4[0][4] == 1.17:
            boss_list_4[0][10] = 16
        if 1.26 < boss_list_4[0][4] < 1.27:
            boss_list_4[0][4] = 1.26
        if boss_list_4[0][4] == 1.26:
            boss_list_4[0][10] += 1
        if 1.5 < boss_list_4[0][4] < 1.51:
            boss_list_4[0][4] = 1.5
        if boss_list_4[0][4] == 1.5:
            boss_list_4[0][10] += 1
        if 1.7 < boss_list_4[0][4] < 1.71:
            boss_list_4[0][4] = 1.7
        if boss_list_4[0][4] == 1.7:
            boss_list_4[0][10] += 1
        if 1.92 < boss_list_4[0][4] < 1.93:
            boss_list_4[0][4] = 1.92
        if boss_list_4[0][4] == 1.92:
            boss_list_4[0][10] += 1
        if boss_list_4[0][4] >= 2:
            # spawn_boss_4([boss_list_4[0][1][0]+90, boss_list_4[0][1][1]], 100)
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
        if boss_list_4[0][6] % 2 == 0 and boss_list_4[0][6] > 0:
            boss_list_4[0][1][0] += boss_list_4[0][7][0]
        if boss_list_4[0][5] == 0:
            boss_list_4[0][1][0] = player.pos[0] + random.randrange(0, 50)
            boss_list_4[0][1][1] = player.pos[1] + random.randrange(0, 50)
            boss_list_4[0][5] = 120
        if boss_list_4[0][5] == 60:
            boss_list_4[0][1][0] = random.randrange(graphic_main.left + 50, graphic_main.right - 50)
            boss_list_4[0][1][1] = random.randrange(graphic_main.top + 50, graphic_main.bottom - 50)
            spawn_enemy_slime([boss_list_4[0][1][0], boss_list_4[0][1][1]], 'picture/enemy/mage/slime.png', 20)
        if 0 < boss_list_4[0][5] < 10:
            boss_list_4[0][1][0] += random.randrange(-10, 10)
            boss_list_4[0][1][1] += random.randrange(-10, 10)
    if 2 < boss_list_4[0][4] < 3:
        boss_list_4[0][4] += 0.0025
        graphic_main.update.append(graphic_main.screen.blit(boss_4_dial[1], (
        pygame.display.get_surface().get_size()[0] / 2 - 368 / 2, pygame.display.get_surface().get_size()[1] / 5 * 4)))
        if boss_list_4[0][4] >= 3:
            del boss_list_4[0]
            player.folie -= 70
            if len(boss_list) == 0:
                player.xp += 170

                world.next_level()

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
    global boss_list_2
    global boss_list_3
    global final_boss

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
                player.xp += 1

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
                player.xp += 1

        n += 1
    n = 0
    for i in enemy_3_2_list:
        collision = False
        rectB = i[0][i[8]].get_rect(center=i[1])
        rectB.h = 12
        rectB.w = 49
        rectB.center = (i[1][0] + 24, i[1][1] + 11)

        collision = rectB.colliderect(a)
        if collision and i[3] <= 0:
            player.mana += 3

            player.folie -= 5

            enemy_3_2_list[n][2] -= strenght
            enemy_3_2_list[n][3] = 30
            if player.last_move_is_up or player.last_move_is_right:
                enemy_3_2_list[n][5][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                enemy_3_2_list[n][5][0] = -knockback

            if enemy_3_2_list[n][2] <= 0:
                player.folie -= 20
                del enemy_3_2_list[n]
                player.xp += 1.5

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
                player.xp += 1.1

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
                player.xp += 1.5

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
                player.xp += 1.1

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
                    player.folie -= 70
                    if len(boss_list) == 1:
                        boss_list[n][4] += 0.01

                    else:
                        del boss_list[n]

                elif boss_list[n][4] == 3:
                    del boss_list[n]
                    player.folie -= 70

        n += 1
    n = 0
    for i in enemy_slime_list:

        collision = False
        rectB = i[0].get_rect()
        rectB.h = 20
        rectB.w = 30
        rectB.center = (i[1][0] + 15, i[1][1] + 10)
        collision = rectB.colliderect(a)
        if collision and i[3] <= 0:
            player.mana += 1
            player.folie -= 3

            enemy_slime_list[n][2] -= strenght
            enemy_slime_list[n][3] = 30
            if player.last_move_is_up or player.last_move_is_right:
                enemy_slime_list[n][5][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                enemy_slime_list[n][5][0] = -knockback

            if enemy_slime_list[n][2] <= 0:
                # player.folie -= 30
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
                player.xp += 2

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
                player.xp += 2

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
                    boss_list_4[n][4] += 0.01


        n += 1
    n = 0
    for i in boss_list_2:
        rectB = boss_list_2[n][0][0].get_rect(center=boss_list_2[n][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (boss_list_2[n][1][0] + 23, boss_list_2[n][1][1] + 40)

        collision = rectB.colliderect(a)
        if collision and i[8] <= 0:
            player.mana += 3

            player.folie -= 5
            boss_list_2[n][2] -= strenght
            boss_list_2[n][6] = 10
            boss_list_2[n][8] = 30
            if boss_list_2[n][12]:
                boss_list_2[n][5] = 30

            if player.last_move_is_up or player.last_move_is_right:
                boss_list_2[n][7][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                boss_list_2[n][7][0] = -knockback
            if boss_list_2[n][2] <= 0:
                if boss_list_2[n][12]:
                    if boss_list_2[n][4] == 0:
                        boss_list_2[n][4] += 0.01
                        boss_list_2[n][2] = 10
                        player.folie -= 50

                    elif boss_list_2[n][4] == 1:
                        boss_list_2[n][4] += 0.01
                        boss_list_2[n][2] = 10
                        player.folie -= 120
                        boss_list_2 = [boss_list_2[0]]
                        break
                    elif boss_list_2[n][4] == 2:
                        boss_list_2 = [boss_list_2[0]]
                        player.folie -= 70
                        boss_list_2[n][4] += 0.01

                        break

                else:
                    del boss_list_2[n]

        n += 1
    for i in boss_list_3:
        rectB = boss_list_3[n][0][0].get_rect(center=boss_list_3[n][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (boss_list_3[n][1][0] + 23, boss_list_3[n][1][1] + 40)

        collision = rectB.colliderect(a)
        if collision and i[8] <= 0:
            player.mana += 3

            player.folie -= 5
            boss_list_3[n][2] -= strenght
            boss_list_3[n][6] = 10
            boss_list_3[n][8] = 30

            if player.last_move_is_up or player.last_move_is_right:
                boss_list_3[n][7][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                boss_list_3[n][7][0] = -knockback
            if boss_list_3[n][2] <= 0:
                if boss_list_3[n][4] == 0:
                    boss_list_3[n][4] += 0.01
                    boss_list_3[n][2] = 10
                    player.folie -= 50

                elif boss_list_3[n][4] == 1:
                    boss_list_3[n][4] += 0.01
                    boss_list_3[n][2] = 10
                    player.folie -= 120
                    break
                elif boss_list_3[n][4] == 2:
                    boss_list_3[n][4] += 0.01


        n += 1

    for i in final_boss:
        rectB = final_boss[n][0][0].get_rect(center=final_boss[n][1])
        rectB.h = 90
        rectB.w = 46
        rectB.center = (final_boss[n][1][0] + 23, final_boss[n][1][1] + 40)

        collision = rectB.colliderect(a)
        if collision and i[8] <= 0:
            player.mana += 3

            player.folie -= 5
            final_boss[n][2] -= strenght
            final_boss[n][6] = 10
            final_boss[n][8] = 30

            if player.last_move_is_up or player.last_move_is_right:
                final_boss[n][7][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                final_boss[n][7][0] = -knockback
            if final_boss[n][2] <= 0:
                if final_boss[n][4] == 0:
                    final_boss[n][4] += 0.01
                    final_boss[n][2] = 10
                    player.folie -= 50

                elif final_boss[n][4] == 1:
                    final_boss[n][4] += 0.01
                    final_boss[n][2] = 10
                    player.folie -= 120
                    break
                elif final_boss[n][4] == 2:
                    player.folie -= 70
                    final_boss[n][4] += 0.01
                    final_boss[n][2] = 10
                elif final_boss[n][4] == 3:
                    final_boss[n][4] += 0.01


        n += 1

    if player.mana > player.mana_max:
        player.mana = player.mana_max
