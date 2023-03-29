# importation
import sys
import pygame
import ennemy
import graphic_main
import tiles
# import main
import weapon
import world

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
pv = 120
pv_max = 120
strength = 10
resistance = 0.1
cooldown = 0
cooldown_move = 0
dash_unlocked = False
dash = 0
dash_invicibility_unlocked = False
dash_inv = False
folie = 0
floie_max = 200
barre_de_folie =None

mana = 100
mana_max = 100
heal = 15
heal_duration = 120
heal_duration_max = 120
is_heal = False
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
    global dash
    global dash_inv
    global folie
    global heal_duration
    global is_heal
    global mana
    old_pos = pos
    if folie < 0:
        folie = 0
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
            if event.key == pygame.K_u:
                weapon.is_attacking = True
                folie += weapon.weapon[weapon.current_weapon][4]
                #print(folie, 'ezsdzfezfiuezoçduftj')
                if folie >= floie_max:
                    sys.exit()
            if event.key == pygame.K_i:
                if dash_unlocked:
                    if mana - 10 >= 0:
                        print('e')
                        if dash == -45:
                            dash = 15
                            if dash_invicibility_unlocked:
                                dash_inv = True
                            mana -= 10
            if event.key == pygame.K_a:
                is_heal=True
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
            if event.key == pygame.K_a:
                heal_duration = heal_duration_max
                is_heal=False
    if cooldown_move < 0 and (dash <= 0 or not dash_unlocked):
        dash_inv = False
        if move_up:
            pos[1] += 2
        if move_down:
            pos[1] -= 2
        if move_left:
            pos[0] -= 2
        if move_right:
            pos[0] += 2
    if cooldown_move < 0 and dash > 0 and dash_unlocked:
        if last_move_is_up:
            pos[1] += 10
        if last_move_is_down:
            pos[1] -= 10
        if last_move_is_left:
            pos[0] -= 10
        if last_move_is_right:
            pos[0] += 10
    if is_heal:
        _heal()
    if dash > -45:
        dash -= 1
    if collision_with_door(graphic_main.door):
        pass
    if collision_with_chest():
        pass
    if collision_with_wall():
        if move_up:
            pos[1] -= 2
        if move_down:
            pos[1] += 2
        if move_left:
            pos[0] += 2
        if move_right:
            pos[0] -= 2
    if dash_inv == False:
        if collision_with_ennemy_1():

            if cooldown <= 0:
                pv -= 20 - 20 * resistance
                cooldown = 60

                cooldown_move = 0
        if collision_with_ennemy_1_2():

            if cooldown <= 0:
                pv -= 10 - 10 * resistance
                cooldown = 60

                cooldown_move = 0
        if collision_with_boss_1():
            if cooldown <= 0:
                pv -= 15 - 15 * resistance
                cooldown = 60

                cooldown_move = 0
        if collision_with_ennemy_2_1():

            if cooldown <= 0:
                pv -= 20 - 20 * resistance
                cooldown = 60

                cooldown_move = 0

        if collision_with_projectile():
            if cooldown <= 0:
                pv -= 30 - 30 * resistance
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


def collision_with_door(door):
    global folie
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=(pos[0] + 15, pos[1] + 25))
    if rectA.collidelist(door) != -1:

        if not ennemy.enemy_1_list and not ennemy.enemy_1_2_list and not ennemy.enemy_1_2_list and not ennemy.boss_list:
            folie -= 100
            if folie < 0:
                folie = 0
            if rectA.collidelist(door) == 0: # Porte de gauche
                world.coo[0] += 1
                world.next_room(2)

            if rectA.collidelist(door) == 1: # Porte de x
                world.coo[1] -= 1
                world.next_room(3)

            if rectA.collidelist(door) == 2: # Porte de y
                world.coo[0] -= 1
                world.next_room(0)

            if rectA.collidelist(door) == 3: # Porte de z
                world.coo[1] += 1
                world.next_room(1)

def collision_with_chest():
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=(pos[0] + 15, pos[1] + 25))
    if rectA.collidelist(list(graphic_main.chest.values())) != -1:
        rect = list(graphic_main.chest.values())[rectA.collidelist(list(graphic_main.chest.values()))]
        ex_current_arm = weapon.current_weapon
        list(graphic_main.chest.keys())[rectA.collidelist(list(graphic_main.chest.values()))]()
        if ex_current_arm != weapon.current_weapon:
            def old_weapon():
                weapon.current_weapon = ex_current_arm
            graphic_main.chest[old_weapon] = rect
        tiles._chest[rectA.collidelist(list(graphic_main.chest.values())) ] = True
        graphic_main.chest.pop(list(graphic_main.chest.keys())[rectA.collidelist(list(graphic_main.chest.values()))])
        graphic_main.update.append(rect)
def collision_with_wall():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=(pos[0] + 15, pos[1] + 25))
    if rectA.left < graphic_main.left + 50:
        pos[0] += 20
        return True
    if rectA.right > graphic_main.right - 50:
        pos[0] -= 20
        return True
    if rectA.top < graphic_main.top + 50:
        pos[1] += 20
        return True
    if rectA.bottom > graphic_main.bottom - 50:
        pos[1] -= 20
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

def collision_with_boss_1():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 40
    rectA.w = 15
    rectA.center = (pos[0] + 15, pos[1] + 25)
    collision = False
    for i in ennemy.boss_list:
        rectB = i[0][0].get_rect(center=i[1])
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
            if i[3][0] == True:
                pos[0] -= 10
            if i[3][1] == True:
                pos[0] += 10
            if i[3][2] == True:
                pos[1] += 10
            if i[3][3] == True:
                pos[1] -= 10
            return collision

def collision_with_ennemy_1_2():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 40
    rectA.w = 15
    rectA.center = (pos[0] + 15, pos[1] + 25)
    collision = False
    for i in ennemy.enemy_1_2_list:
        rectB = i[0][i[8]].get_rect(center=i[1])
        rectB.h = 12
        rectB.w = 49
        rectB.center = (i[1][0] + 24, i[1][1] + 11)
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
        rectB = i[0][i[8]].get_rect(center=i[1])
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

def _heal():
    global heal_duration
    global mana
    global pv
    heal_duration -= 1
    mana -= 20/120
    if mana < 0:
        mana = 0
        heal_duration = heal_duration_max
    if heal_duration == 0 and mana >= 0:
        pv += heal
        heal_duration = heal_duration_max



def showpv():
    global pv
    w, h = pygame.display.get_surface().get_size()
    widht = 0.3
    height = 0.05
    life_red = pygame.Rect(w / 2 - (widht * w) / 2, h - 0.1 * h, widht * w, height * h)
    rectA = pygame.draw.rect(graphic_main.screen, (255, 0, 0), life_red)
    life_black = pygame.Rect(w / 2 - (widht * w) / 2 + widht * w - (widht * w - widht * w * pv / pv_max), h - 0.1 * h,
                             widht * w - widht * w * pv / pv_max + 1, height * h)
    rectB = pygame.draw.rect(graphic_main.screen, (40, 40, 40), life_black)
    return rectA, rectB


def showfolie():
    w, h = pygame.display.get_surface().get_size()
    rectA = graphic_main.screen.blit(barre_de_folie, (w/300, h * 20/100))
    rectB = pygame.Rect((w/300, (h* 20/100) + 55 * h / 1080 + (folie/floie_max) * (634 * h / 1080  - 55 * h / 1080 ), 73 * w / 1920 , (634 - 55)* h / 1080  - (folie/floie_max) * (634 - 55)* h / 1080  + 1))
    rectB = pygame.draw.rect(graphic_main.screen, (54,57,66), rectB)
    return rectA, rectB
