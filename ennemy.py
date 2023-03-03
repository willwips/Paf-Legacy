import math

import pygame
import player

enemy_1_list = []
enemy_2_1_list = []
projectile_list = []


def spawn_enemy_2_1(pos, img, pv):
    img = pygame.transform.scale(pygame.image.load(img).convert_alpha(), [25, 49])
    pos = pos
    global enemy_2_1_list
    enemy_2_1_list.append([img, pos, pv, 10, [False, False, False, False], [0, 0], False, 10])

def spawm_projectile(pos, radius, directon):
    global projectile_list
    projectile_list.append([pos, radius, directon])

def spawn_enemy_1(pos, img, pv):
    img = pygame.image.load(img).convert_alpha()
    pos = pos
    global enemy_1_list
    enemy_1_list.append([img, pos, pv, 10, [False, False, False, False], [0, 0]])


def boucle():
    global enemy_1_list
    global enemy_2_1_list
    n = 0
    move_ennemi_1()
    move_ennemi_2_1()
    move_projectile()
    for i in enemy_1_list:
        if i[3] > 0:
            enemy_1_list[n][3] -= 1
        n += 1
    n = 0
    for i in enemy_2_1_list:
        if i[3] > 0:
            enemy_2_1_list[n][3] -= 1
        enemy_2_1_list[n][7] -= 1
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

def is_touch_wall(pos):
    if pos[0] < 0:
        return True
    if pos[1] < 0:
        return True
    if pos[0] > pygame.display.get_surface().get_size()[0]:
        return True
    if pos[1] > pygame.display.get_surface().get_size()[1]:
        return True

    return False
def touch_wall(pos):
    if pos[0] < 0:
        pos[0] += 10
    if pos[1] < 0:
        pos[1] += 10
    if pos[0] > pygame.display.get_surface().get_size()[0]:
        pos[0] -= 10
    if pos[1] > pygame.display.get_surface().get_size()[1]:
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
        enemy_1_list[i][1] = touch_wall(enemy_1_list[i][1])
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



def move_ennemi_2_1():
    global enemy_2_1_list
    for i in range(0, len(enemy_2_1_list)):
        rectB = enemy_2_1_list[i][0].get_rect(center=enemy_2_1_list[i][1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (enemy_2_1_list[i][1][0] + 15, enemy_2_1_list[i][1][1] + 25)
        dist = math.sqrt(
            (enemy_2_1_list[i][1][0] - player.pos[0]) ** 2 + (enemy_2_1_list[i][1][1] - player.pos[1]) ** 2)
        enemy_2_1_list[i][4][0] = False
        enemy_2_1_list[i][4][1] = False
        enemy_2_1_list[i][4][2] = False
        enemy_2_1_list[i][4][3] = False
        enemy_2_1_list[i][1] = touch_wall(enemy_2_1_list[i][1])
        if enemy_2_1_list[i][3] % 2 == 0 and enemy_2_1_list[i][3] > 0:
            enemy_2_1_list[i][1][0] += enemy_2_1_list[i][5][0]
        if 15 < dist <= 200 and enemy_2_1_list[i][7] > 0:
            if (enemy_2_1_list[i][1][0] - player.pos[0]) >= 0:
                enemy_2_1_list[i][1][0] -= abs((enemy_2_1_list[i][1][0] - player.pos[0]) / (
                        abs(enemy_2_1_list[i][1][1] - player.pos[1]) + abs((enemy_2_1_list[i][1][0] - player.pos[0]))))
                enemy_2_1_list[i][4][0] = True
            elif (enemy_2_1_list[i][1][0] - player.pos[0]) <= 0:
                enemy_2_1_list[i][1][0] += abs((enemy_2_1_list[i][1][0] - player.pos[0]) / (
                        abs(enemy_2_1_list[i][1][1] - player.pos[1]) + abs(enemy_2_1_list[i][1][0] - player.pos[0])))
                enemy_2_1_list[i][4][1] = True
            if (enemy_2_1_list[i][1][1] - player.pos[1]) >= 0:
                enemy_2_1_list[i][1][1] -= abs((enemy_2_1_list[i][1][1] - player.pos[1]) / (
                        abs(enemy_2_1_list[i][1][1] - player.pos[1]) + abs(enemy_2_1_list[i][1][0] - player.pos[0])))
                enemy_2_1_list[i][4][2] = True
            elif (enemy_2_1_list[i][1][1] - player.pos[1]) <= 0:
                enemy_2_1_list[i][1][1] += abs((enemy_2_1_list[i][1][1] - player.pos[1]) / (
                        abs(enemy_2_1_list[i][1][1] - player.pos[1]) + abs(enemy_2_1_list[i][1][0] - player.pos[0])))
                enemy_2_1_list[i][4][3] = True
        if enemy_2_1_list[i][7] < 0:
            enemy_2_1_list[i][6] = True

        if enemy_2_1_list[i][6] == True:
            try:
                total = abs(enemy_2_1_list[i][1][0]-player.pos[0])+abs(enemy_2_1_list[i][1][1]-player.pos[1])
                spawm_projectile([enemy_2_1_list[i][1][0], enemy_2_1_list[i][1][1]], 10, [(player.pos[0]-enemy_2_1_list[i][1][0])/total*5, (player.pos[1]-enemy_2_1_list[i][1][1])/total*5])
            except:
                pass
            enemy_2_1_list[i][6] = False
            enemy_2_1_list[i][7] = 300

def move_projectile():
    global projectile_lists
    for i in range(0, len(projectile_list)):

        print(len(projectile_list))
        projectile_list[i][0][0] += projectile_list[i][2][0]
        projectile_list[i][0][1] += projectile_list[i][2][1]

    n = 0
    for i in projectile_list:
        if is_touch_wall(i[0]):
            del projectile_list[n]
        n += 1

def collision_with_weapon(a, strenght, knockback):
    n = 0
    global enemy_1_list
    global enemy_2_1_list
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
            if player.last_move_is_up or player.last_move_is_right:
                enemy_1_list[n][5][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                enemy_1_list[n][5][0] = -knockback

            if enemy_1_list[n][2] <= 0:
                del enemy_1_list[n]

        n += 1
    for i in enemy_2_1_list:
        print(i)
        collision = False
        rectB = i[0].get_rect(center=i[1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (i[1][0] + 15, i[1][1] + 25)
        collision = rectB.colliderect(a)
        if collision and i[3] <= 0:
            enemy_2_1_list[n][2] -= strenght
            enemy_2_1_list[n][3] = 30
            if player.last_move_is_up or player.last_move_is_right:
                enemy_2_1_list[n][5][0] = knockback
            if player.last_move_is_down or player.last_move_is_left:
                enemy_2_1_list[n][5][0] = -knockback

            if enemy_2_1_list[n][2] <= 0:
                del enemy_2_1_list[n]

        n += 1