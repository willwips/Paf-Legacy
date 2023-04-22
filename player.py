# importation
import sys
import pygame
import ennemy
import graphic_main

import tiles
# import main
import weapon
import world


def _pass():
    pass
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
xp = 0
lvl = 0
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
possible_object = _pass
possible_object_picture = None
mana = 100
mana_max = 100
heal = 15
heal_duration = 120
heal_duration_max = 120
is_heal = False
timer = 60
dead = False
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
    global timer
    old_pos = pos
    timer -= 1
    lvl_up()

    if folie < 0: # Permet de ne pas avoir de valeur en folie négative
        folie = 0
    for event in pygame.event.get(): # Boucle pour chaque event
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.KEYDOWN: # S'occupe des évènements quand un bouton est préssé
            if event.key == pygame.K_ESCAPE: 
                sys.exit()
            if event.key == pygame.K_z: # Oriente le personnage vers le haut en changeant l'image affichée et lui permet de se déplacer quand le bouton z est appuyé
                move_down = True
                last_move_is_right = False
                last_move_is_left = False
                last_move_is_up = False
                last_move_is_down = True
                is_movement += 1
                graphic_main.frame = graphic_main.frame_back
            if event.key == pygame.K_s: # Oriente le personnage vers la bas en changeant l'image affichée et lui permet de se déplacer quand le bouton s est appuyé
                move_up = True
                is_movement += 1
                graphic_main.frame = graphic_main.frame_front
                last_move_is_right = False
                last_move_is_left = False
                last_move_is_up = True
                last_move_is_down = False
            if event.key == pygame.K_d: # Oriente le personnage vers la droite en changeant l'image affichée et lui permet de se déplacer quand le bouton d est appuyé
                move_right = True
                is_movement += 1
                graphic_main.frame = graphic_main.frame_R
                last_move_is_right = True
                last_move_is_left = False
                last_move_is_up = False
                last_move_is_down = False
            if event.key == pygame.K_q: # Oriente le personnage vers la gauche en changeant l'image affichée et lui permet de se déplacer quand le bouton q est appuyé
                move_left = True
                is_movement += 1
                graphic_main.frame = graphic_main.frame_L
                last_move_is_right = False
                last_move_is_left = True
                last_move_is_up = False
                last_move_is_down = False
            if event.key == pygame.K_u: # Permet au joueur d'attaquer quand le bouton u est pressé
                weapon.is_attacking = True
                folie += weapon.weapon[weapon.current_weapon][4] # Augmente la folie du joueur en fonction de l'arme équippée
                if folie >= floie_max: # Si la folie est supérieur à celle pouvant être supporté, le joueur meurt
                    death()
            if event.key == pygame.K_i: # Permet au joueur d'utiliser la capacité équippée
                if dash_unlocked: # Utilisable que si débloqué
                    if mana - 10 >= 0: # Diminue le mana
                        if dash == -45:
                            dash = 15
                            if dash_invicibility_unlocked: # Si l'amélioration est débloqué
                                dash_inv = True # Active cette variable qui donne une invincibilité pendant le dash
                            mana -= 10 # Diminue le mana du joueur
            if event.key == pygame.K_a: # Si le bouton a est pressé, la variable est activé et permet au joueur de se soigner
                is_heal=True
            if event.key == pygame.K_o: # Si le bouton o est pressé, utilise un objet si il en est possible
                possible_object()

        if event.type == pygame.KEYUP: # Effectue ce qui suit une fois un bouton relaché
            if event.key == pygame.K_z: # Si la touche z est relachée, la vitesse de mouvement devient nulle et le joueur s'arrête dans la direction où il regardait
                move_down = False
                is_movement -= 1

            if event.key == pygame.K_s: # Si la touche s est relachée, la vitesse de mouvement devient nulle et le joueur s'arrête dans la direction où il regardait
                move_up = False
                is_movement -= 1
            if event.key == pygame.K_d: # Si la touche d est relachée, la vitesse de mouvement devient nulle et le joueur s'arrête dans la direction où il regardait
                move_right = False
                is_movement -= 1
            if event.key == pygame.K_q: # Si la touche z est relachée, la vitesse de mouvement devient nulle et le joueur s'arrête dans la direction où il regardait
                move_left = False
                is_movement -= 1
            if event.key == pygame.K_a: # Si la touche a est relaché, le joueur arrête de se soigner
                heal_duration = heal_duration_max
                is_heal=False
    if cooldown_move < 0 and (dash <= 0 or not dash_unlocked):
        dash_inv = False
        if move_up: # Si le joueur se déplace vers le haut
            pos[1] += 2 # Augmente les coordonées y du joueur de 2
        if move_down: # Si le joueur se déplace vers le bas
            pos[1] -= 2 # Diminue les coordonées y du joueur de 2
        if move_left: # Si le joueur se déplace vers la gauche
            pos[0] -= 2  # Diminue les coordonées x du joueur de 2
        if move_right: # Si le joueur se déplace vers la droite
            pos[0] += 2 # Augmente les coordonées x du joueur de 2
    if possible_object_picture == None: # Si pas d'objet
        rect = pygame.rect.Rect(100, 0, 100, 100) # Créer un rectangle avec ces paramètres (de largeur et hauteur 100 pixel en haut à gauche) et l'associe à la variable
        graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (0, 0, 0), rect)) # Affiche le rectangle précédemment défini
    else: # Si le joueur à un objet
        graphic_main.update.append(graphic_main.screen.blit(possible_object_picture, (100, 0))) # Affiche l'objet avec ces coordonées

    if cooldown_move < 0 and dash > 0 and dash_unlocked: # Si le dash est débloqué et que les conditions sont remplies
        if last_move_is_up: # Si le joueur se déplace vers le haut
            pos[1] += 10 # Augmente les coordonées y du joueur de 10
        if last_move_is_down: # Si le joueur se déplace vers le bas
            pos[1] -= 10 # Diminue les coordonées y du joueur de 10
        if last_move_is_left: # Si le joueur se déplace vers la gauche
            pos[0] -= 10 # Diminue les coordonées x du joueur de 10
        if last_move_is_right: # Si le joueur se déplace vers la droite
            pos[0] += 10  # Augmente les coordonées x du joueur de 10
    if is_heal: # Si la variable est active, la fonction pour se soigné est activé
        _heal()
    if dash > -45: # Si le dash est au dessus de -45 (donc une fois activé), sa valeur est diminuée de 1 jusqu'à réatteidre cette valeur et être réutilisé
        dash -= 1
    if collision_with_door(graphic_main.door): # Ne se passe rien de plus si le joueur touche la porte
        pass
    if collision_with_chest(): # Ne se passe rien de plus si le joueur touche la porte
        pass
    if collision_with_wall(): # Si le joueur cogne un mur son emplacement est modifié
        if move_up: # Si le joueur se déplace vers le haut
            pos[1] -= 2 # Diminue les coordonées y du joueur de 2
        if move_down: # Si le joueur se déplace vers le bas
            pos[1] += 2 # Augmente les coordonées y du joueur de 2
        if move_left: # Si le joueur se déplace vers la gauche
            pos[0] += 2 # Augmente les coordonées x du joueur de 2
        if move_right: # Si le joueur se déplace vers la droite
            pos[0] -= 2 # Diminue les coordonées x du joueur de 2

    if dash_inv == False: # Si l'invulnérabilité lors d'une dash est pas obtenue et activé le joueur perd des pv quand il touche un ennemi
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

        if collision_with_ennemy_3_2():
            if cooldown <= 0:
                pv -= 20 - 20 * resistance
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

        if collision_with_ennemy_2_2():
            if cooldown <= 0:
                pv -= 20 - 20 * resistance
                cooldown = 60
                cooldown_move = 0

        _coll = collision_with_projectile() # De même avec les projectiles
        if _coll:
            if cooldown <= 0:
                pv -= _coll[0] - _coll[0] * resistance
                folie += _coll[1]
                cooldown = 60
                cooldown_move = 0

        if collision_with_ennemy_slime(): # De même avec les slimes
            if cooldown <= 0:
                pv -= 20 - 20 * resistance
                cooldown = 60
                cooldown_move = 0
                
        if collision_with_ennemy_4_1():
            if cooldown <= 0:
                pv -= 20 - 20 * resistance
                cooldown = 60
                cooldown_move = 0

        if collision_with_ennemy_4_2():
            if cooldown <= 0:
                #pv -= 0 - 0 * resistance
                cooldown = 60
                cooldown_move = 0

        if collision_with_boss_4():
            if cooldown <= 0:
                pv -= 15 - 15 * resistance
                cooldown = 60
                cooldown_move = 0

        if collision_with_boss_2():
            if cooldown <= 0:
                pv -= 15 - 15 * resistance
                cooldown = 60
                cooldown_move = 0

        if collision_with_boss_3():
            if cooldown <= 0:
                pv -= 15 - 15 * resistance
                cooldown = 60
                cooldown_move = 0

        if collision_with_final_boss():
            if cooldown <= 0:
                pv -= 15 - 15 * resistance
                cooldown = 60
                cooldown_move = 0


    if is_movement < 0:
        is_movement = 0
    if pv <= 0: # Si les pv du joueur sont inférieur ou égaux à 0, le joueur meurt et la fonction est activé
        death()
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

    if pv > pv_max:
        pv = pv_max

# Définition de la collision avec les différents éléments du jeu
def collision_with_door(door):
    global folie
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=(pos[0] + 15, pos[1] + 25))
    if rectA.collidelist(door) != -1:

        if not ennemy.enemy_1_list and not ennemy.enemy_1_2_list and not ennemy.enemy_2_1_list and not ennemy.enemy_2_2_list and not ennemy.boss_list and not ennemy.enemy_slime_list and not ennemy.enemy_4_1_list and not ennemy.enemy_4_2_list and not ennemy.boss_list_2 and not ennemy.boss_list_3 and not ennemy.enemy_3_2_list and not ennemy.enemy_3_2_list and not ennemy.final_boss and timer < 0:
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

def collision_with_ennemy_3_2():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 40
    rectA.w = 15
    rectA.center = (pos[0] + 15, pos[1] + 25)
    collision = False
    for i in ennemy.enemy_3_2_list:
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

def collision_with_ennemy_2_2():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 40
    rectA.w = 15
    rectA.center = (pos[0] + 15, pos[1] + 25)
    collision = False
    for i in ennemy.enemy_2_2_list:
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
            if i[4][0] == True:
                pos[0] -= 10
            if i[4][1] == True:
                pos[0] += 10
            if i[4][2] == True:
                pos[1] += 10
            if i[4][3] == True:
                pos[1] -= 10
            return collision


def collision_with_ennemy_slime():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 40
    rectA.w = 15
    rectA.center = (pos[0] + 15, pos[1] + 25)
    collision = False
    for i in ennemy.enemy_slime_list:
        rectB = i[0].get_rect()
        rectB.h = 20
        rectB.w = 30
        rectB.center = (i[1][0] + 15, i[1][1] + 10)

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
        collision = i[5]
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
def collision_with_ennemy_4_1():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 40
    rectA.w = 15
    rectA.center = (pos[0] + 15, pos[1] + 25)
    collision = False
    for i in ennemy.enemy_4_1_list:
        rectB = i[0].get_rect()
        rectB.h = 20
        rectB.w = 30
        rectB.center = (i[1][0] + 15, i[1][1] + 10)

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

def collision_with_ennemy_4_2():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 40
    rectA.w = 15
    rectA.center = (pos[0] + 15, pos[1] + 25)
    collision = False
    for i in ennemy.enemy_4_2_list:
        rectB = i[0][i[8]].get_rect()
        rectB.h = 20
        rectB.w = 30
        rectB.center = (i[1][0] + 15, i[1][1] + 10)

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

def collision_with_boss_4():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 40
    rectA.w = 15
    rectA.center = (pos[0] + 15, pos[1] + 25)
    collision = False
    for i in ennemy.boss_list_4:
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

def collision_with_boss_2():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 40
    rectA.w = 15
    rectA.center = (pos[0] + 15, pos[1] + 25)
    collision = False
    for i in ennemy.boss_list_2:
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

def collision_with_final_boss():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 40
    rectA.w = 15
    rectA.center = (pos[0] + 15, pos[1] + 25)

    collision = False
    for i in ennemy.final_boss:
        rectB = i[0][0].get_rect(center=(i[1][0], i[1][1]))
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
            if last_move_is_right:
                pos[0] -= 10
            if last_move_is_left:
                pos[0] += 10
            if last_move_is_down:
                pos[1] += 10
            if last_move_is_up:
                pos[1] -= 10
            return collision
        rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
        rectA.h = 15
        rectA.w = 15
        rectA.center = (pos[0] + 15, pos[1] + 40)
        for i in i[12]:
            if rectA.colliderect(i):
                collision = True
                return collision


def collision_with_boss_3():
    global pos
    rectA = graphic_main.frame[graphic_main.current].get_rect(center=pos)
    rectA.h = 15
    rectA.w = 15
    rectA.center = (pos[0] + 15, pos[1] + 40)

    collision = False
    for i in ennemy.boss_list_3:
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
        for i in i[12]:
            if rectA.colliderect(i):
                collision = True
        if collision:
            return collision

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


def lvl_up():
    global xp
    global pv
    global mana_max
    global pv_max
    global strength
    global mana
    global resistance
    global heal
    global lvl
    if xp >= 200+ 4*lvl**2 + 6*lvl:
        xp -= 200+4**lvl*2 + 6* lvl
        pv *= (pv_max+10)/pv_max
        pv_max += 10
        strength += 1
        mana *= (mana_max+10)/mana_max
        mana_max+=10
        resistance *= 1.05
        heal+=3
        lvl += 1


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

def death(): # Réinitialisation de toutes les variables à la mort du joueur et la fonction est activé
    global pos
    global move_down
    global move_right
    global move_up
    global move_left
    global last_move_is_up
    global last_move_is_down
    global last_move_is_left
    global last_move_is_right
    global is_movement
    global pv
    global pv_max
    global strength
    global xp
    global lvl
    global resistance
    global cooldown
    global cooldown_move
    global dash_unlocked
    global dash
    global dash_invicibility_unlocked
    global dash_inv
    global folie
    global floie_max
    global barre_de_folie
    global possible_object
    global possible_object_picture
    global mana
    global mana_max
    global heal
    global heal_duration
    global heal_duration_max
    global is_heal
    global timer
    global dead
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
    xp = 0
    lvl = 0
    resistance = 0.1
    cooldown = 0
    cooldown_move = 0
    dash_unlocked = False
    dash = 0
    dash_invicibility_unlocked = False
    dash_inv = False
    folie = 0
    floie_max = 200
    possible_object = _pass
    possible_object_picture = None
    mana = 100
    mana_max = 100
    heal = 15
    heal_duration = 120
    heal_duration_max = 120
    is_heal = False
    timer = 60
    dead = True
    world.create_floor(0)
    world.coo = [0, 0]
    ennemy.enemy_4_2_list = []
    ennemy.enemy_4_1_list = []
    ennemy.final_boss = []
    ennemy.boss_list = []
    ennemy.enemy_3_2_list = []
    ennemy.enemy_3_1_list = []
    ennemy.boss_list_4 = []
    ennemy.boss_list_3 = []
    ennemy.enemy_2_2_list = []
    ennemy.enemy_2_1_list = []
    ennemy.boss_list_2 = []
    ennemy.enemy_1_list = []
    ennemy.enemy_1_2_list = []
    ennemy.enemy_slime_list = []

# Fonction qui affiche la barre de folie en l'actualisant
def showfolie():
    w, h = pygame.display.get_surface().get_size()
    rectA = graphic_main.screen.blit(barre_de_folie, (w/300, h * 20/100))
    rectB = pygame.Rect((w/300, (h* 20/100) + 55 * h / 1080 + (folie/floie_max) * (634 * h / 1080  - 55 * h / 1080 ), 73 * w / 1920 , (634 - 55)* h / 1080  - (folie/floie_max) * (634 - 55)* h / 1080  + 1))
    rectB = pygame.draw.rect(graphic_main.screen, (0,0,0), rectB)
    return rectA, rectB
