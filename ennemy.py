import math

import pygame
import player

enemy_1_list = []


def spawn_enemy(pos, img, pv):
    img = pygame.image.load(img).convert_alpha()
    pos = pos
    global enemy_1_list
    enemy_1_list.append([img, pos, pv, 10, [False, False, False, False]])


def boucle():
    global enemy_1_list
    n = 0
    move_ennemi_1()
    for i in enemy_1_list:
        if i[3] > 0:
            enemy_1_list[n][3] -= 1
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


def touch_wall(pos):
    if pos[0] < 0 or pos[1] < 0 or pos[1] > pygame.display.get_surface().get_size()[1] or pos[0] > \
            pygame.display.get_surface().get_size()[0]:
        return True
    return False


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

        if 15 < dist <= 200 and not touch_wall(enemy_1_list[i][1]):
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

        if touch_wall(enemy_1_list[i][1]):
            enemy_1_list[i][1][0] -= 11
            if touch_wall(enemy_1_list[i][1]):
                enemy_1_list[i][1][0] += 22
                if touch_wall(enemy_1_list[i][1]):
                    enemy_1_list[i][1][0] -= 11
                    enemy_1_list[i][1][1] -= 11
                    if touch_wall(enemy_1_list[i][1]):
                        enemy_1_list[i][1][1] += 22
                        if touch_wall(enemy_1_list[i][1]):
                            enemy_1_list[i][1][0] -= 11
            else:
                enemy_1_list[i][1][0] += 9


def collision_with_weapon(a, strenght):
    n = 0
    for i in enemy_1_list:

        collision = False
        rectB = i[0].get_rect(center=i[1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (i[1][0] + 15, i[1][1] + 25)
        collision = rectB.colliderect(a)
        if collision and i[3] <= 0:
            enemy_1_list[n][2] -= strenght
            enemy_1_list[n][3] = 30
            if player.last_move_is_down or player.last_move_is_right:
                enemy_1_list[n][1][0] += 20
            if player.last_move_is_up or player.last_move_is_left:
                enemy_1_list[n][1][0] -= 20

            if enemy_1_list[n][2] <= 0:
                del enemy_1_list[n]

        n += 1
