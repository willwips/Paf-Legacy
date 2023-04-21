import pygame
import graphic_main
import ennemy
import player

weapon = {}

# Fonction qui rempli le dictionnaire avec le nom d'une arme associé à son image
def import_weapon():
    global weapon
    weapon['final_axe'] = (
        pygame.transform.scale(pygame.image.load('picture/weapon/final_axe.png').convert_alpha(), (20, 40)), 15 , [17, 30], 11, 20)
    weapon['final_sword'] = (
        pygame.transform.scale(pygame.image.load('picture/weapon/final_sword.png').convert_alpha(), (12, 70)), 7 , [0, 0], 8, 20)
    weapon['curved_sword'] = (
    pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/weapon/Weapon-Curved.png').convert_alpha(),  (20, 60)), 0), 5 , [0, -50], 12, 10)
    weapon['katana'] = (
        pygame.transform.scale(pygame.image.load('picture/weapon/final_sword.png').convert_alpha(), (12, 70)), 5 , [0, 0], 6, 5)

# Initialisation de variables avec des valeurs initiales
is_attacking = False
angle = 0
current_weapon = 'curved_sword'
modify_angle = 5

# Fonction qui permet de faire rotationner l'image 
def rotate(surface, angle, pivot, offset):
    rotated_image = pygame.transform.rotate(surface, -angle)
    rotated_offset = offset.rotate(angle)
    rect = rotated_image.get_rect(center=pivot + rotated_offset)
    graphic_main.update.append(pygame.draw.circle(graphic_main.screen, (255, 0,0), pivot, 1))
    return rotated_image, rect


def loop(pos_player):
    global angle
    global is_attacking
    global modify_angle
    if current_weapon == 'final_axe':
        return loop_final_axe(pos_player)
    if current_weapon == 'final_sword':
        return loop_final_sword(pos_player)
    if current_weapon == 'curved_sword':
        return loop_curved_sword(pos_player)

def loop_final_axe(pos_player):
    global angle
    global is_attacking
    global modify_angle
    if is_attacking:
        angle += modify_angle
        if angle % 360 == 120:
            modify_angle = -40
        if angle % 360 == 270:
            modify_angle = 10
        if angle % 360 == 0:
            modify_angle = 10
            is_attacking = False

    if player.last_move_is_up:
        a = rotate(
            weapon[current_weapon][0], -180 + angle,
            (pos_player[0] + weapon[current_weapon][2][0] + 12, pos_player[1] + weapon[current_weapon][2][1] + 5),
            pygame.math.Vector2(0, 15))[1]
        w = graphic_main.screen.blit(rotate(
            weapon[current_weapon][0], -180 + angle, (
                pos_player[0] + weapon[current_weapon][2][0] + 12, pos_player[1] + weapon[current_weapon][2][1] + 25),
            pygame.math.Vector2(0, -15))[0], a)
        a.center = (
            pos_player[0] + weapon[current_weapon][2][0] + 12, pos_player[1] + weapon[current_weapon][2][1] + 25)
        if is_attacking:
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength + 1.01**player.folie, weapon[current_weapon][3])
    
    if player.last_move_is_right:
        a = rotate(
            weapon[current_weapon][0], -150 + angle,
            (pos_player[0] + weapon[current_weapon][2][0] + 0, pos_player[1] + weapon[current_weapon][2][1] + 10),
            pygame.math.Vector2(0, 15))[1]
        w = graphic_main.screen.blit(rotate(
            weapon[current_weapon][0], -130 + angle, (
                pos_player[0] + weapon[current_weapon][2][0] + 0, pos_player[1] + weapon[current_weapon][2][1] + 10),
            pygame.math.Vector2(0, -15))[0], a)
        a.center = (
            pos_player[0] + weapon[current_weapon][2][0] + 12, pos_player[1] + weapon[current_weapon][2][1] - 10)
        if is_attacking:
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength + 1.01**player.folie, weapon[current_weapon][3])
    
    if player.last_move_is_down:
        a = rotate(
            weapon[current_weapon][0], -180 - angle,
            (pos_player[0] + weapon[current_weapon][2][0] - 12, pos_player[1] + weapon[current_weapon][2][1] + 5),
            pygame.math.Vector2(0, 15))[1]
        w = graphic_main.screen.blit(rotate(
            weapon[current_weapon][0], -180 - angle, (
                pos_player[0] + weapon[current_weapon][2][0] + 12, pos_player[1] + weapon[current_weapon][2][1] + 25),
            pygame.math.Vector2(0, -15))[0], a)
        a.center = (
            pos_player[0] + weapon[current_weapon][2][0] + 12, pos_player[1] + weapon[current_weapon][2][1] + 25)
        if is_attacking:
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength + 1.01**player.folie, weapon[current_weapon][3])

    if player.last_move_is_left:
        a = rotate(
            weapon[current_weapon][0], 150 - angle,
            (pos_player[0] + weapon[current_weapon][2][0] - 8, pos_player[1] + weapon[current_weapon][2][1] + 10),
            pygame.math.Vector2(0, 15))[1]
        w = graphic_main.screen.blit(rotate(
            weapon[current_weapon][0], 150 - angle, (
                pos_player[0] + weapon[current_weapon][2][0] - 8, pos_player[1] + weapon[current_weapon][2][1] + 10),
            pygame.math.Vector2(0, -15))[0], a)
        a.center = (
            pos_player[0] + weapon[current_weapon][2][0] + 12, pos_player[1] + weapon[current_weapon][2][1] + 25)
        if is_attacking:
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength + 1.01**player.folie, weapon[current_weapon][3])
    return w, a


def loop_final_sword(pos_player):
    global angle
    global is_attacking
    global modify_angle
    if is_attacking:
        angle += modify_angle
        if angle % 360 == 120:
            modify_angle = -40
        if angle % 360 == 270:
            modify_angle = 10
        if angle % 360 == 0:
            modify_angle = 10
            is_attacking = False

    if player.last_move_is_up:
        a = rotate(
            weapon[current_weapon][0], -150 + angle,
            (pos_player[0] + weapon[current_weapon][2][0] + 30, pos_player[1] + weapon[current_weapon][2][1] + 30),
            pygame.math.Vector2(0, 45 ))[1]
        w = graphic_main.screen.blit(rotate(
            weapon[current_weapon][0], -150 + angle, (
                pos_player[0] + weapon[current_weapon][2][0] + 12, pos_player[1] + weapon[current_weapon][2][1] + 0 ),
            pygame.math.Vector2(-10, -0))[0], a)
        a.center = (
            pos_player[0] + weapon[current_weapon][2][0] - 500, pos_player[1] + weapon[current_weapon][2][1] + 25)
        if is_attacking:
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength + 1.01**player.folie, weapon[current_weapon][3])

    if player.last_move_is_right:
        a = rotate(
            weapon[current_weapon][0], -150 + angle,
            (pos_player[0] + weapon[current_weapon][2][0] + 20, pos_player[1] + weapon[current_weapon][2][1] + 35),
            pygame.math.Vector2(0, 35))[1]
        w = graphic_main.screen.blit(rotate(
            weapon[current_weapon][0], -150 + angle, (
                pos_player[0] + weapon[current_weapon][2][0] + 20, pos_player[1] + weapon[current_weapon][2][1] + 35),
            pygame.math.Vector2(0, 35))[0], a)
        a.center = (
            pos_player[0] + weapon[current_weapon][2][0] + 12, pos_player[1] + weapon[current_weapon][2][1] - 10)
        if is_attacking:
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength + 1.01**player.folie, weapon[current_weapon][3])

    if player.last_move_is_down:
        a = rotate(
            weapon[current_weapon][0], -180 - angle,
            (pos_player[0] + weapon[current_weapon][2][0] + 5, pos_player[1] + weapon[current_weapon][2][1] + 25),
            pygame.math.Vector2(0, 20))[1]
        w = graphic_main.screen.blit(rotate(
            weapon[current_weapon][0], -180 - angle, (
                pos_player[0] + weapon[current_weapon][2][0] + 5, pos_player[1] + weapon[current_weapon][2][1] + 25),
            pygame.math.Vector2(0, 20))[0], a)
        a.center = (
            pos_player[0] + weapon[current_weapon][2][0] + 12, pos_player[1] + weapon[current_weapon][2][1] + 25)
        if is_attacking:
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength + 1.01**player.folie, weapon[current_weapon][3])

    if player.last_move_is_left:
        a = rotate(
            weapon[current_weapon][0], 150 - angle,
            (pos_player[0] + weapon[current_weapon][2][0] + 0, pos_player[1] + weapon[current_weapon][2][1] + 30),
            pygame.math.Vector2(0, 40))[1]
        w = graphic_main.screen.blit(rotate(
            weapon[current_weapon][0], 150 - angle, (
                pos_player[0] + weapon[current_weapon][2][0] - 0, pos_player[1] + weapon[current_weapon][2][1] + 30),
            pygame.math.Vector2(0, 40))[0], a)
        a.center = (
            pos_player[0] + weapon[current_weapon][2][0] + 12, pos_player[1] + weapon[current_weapon][2][1] + 25)
        if is_attacking:
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength + 1.01**player.folie, weapon[current_weapon][3])
    return w, a
def loop_curved_sword(pos_player):
    global angle
    global is_attacking
    global modify_angle
    if is_attacking:
        angle += modify_angle
        if angle % 360 == 120:
            modify_angle = -40
        if angle % 360 == 270:
            modify_angle = 10
        if angle % 360 == 0:
            modify_angle = 10
            is_attacking = False

    if player.last_move_is_up:
        a = rotate(
            pygame.transform.flip(weapon[current_weapon][0], True, False), -0 + angle,
            (pos_player[0] + weapon[current_weapon][2][0] + 30, pos_player[1] + weapon[current_weapon][2][1] +85),
            pygame.math.Vector2(0, -20 ))[1]
        w = graphic_main.screen.blit(rotate(
            pygame.transform.flip(weapon[current_weapon][0], True, False), -0 + angle, (
                pos_player[0] + weapon[current_weapon][2][0] + 30, pos_player[1] + weapon[current_weapon][2][1] + 85),
            pygame.math.Vector2(-0, -20))[0], a)
        a.center = (
            pos_player[0] + weapon[current_weapon][2][0] - 500, pos_player[1] + weapon[current_weapon][2][1] + 25)
        if is_attacking:
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength + player.folie/100, weapon[current_weapon][3])

    if player.last_move_is_right:
        a = rotate(
            pygame.transform.flip(weapon[current_weapon][0], True, False), -0 + angle,
            (pos_player[0] + weapon[current_weapon][2][0] + 25, pos_player[1] + weapon[current_weapon][2][1] + 80),
            pygame.math.Vector2(5,-20))[1]
        w = graphic_main.screen.blit(rotate(
            pygame.transform.flip(weapon[current_weapon][0], True, False), -0 + angle, (
                pos_player[0] + weapon[current_weapon][2][0] + 25, pos_player[1] + weapon[current_weapon][2][1] + 80),
            pygame.math.Vector2(5, -20))[0], a)
        a.center = (
            pos_player[0] + weapon[current_weapon][2][0] + 12, pos_player[1] + weapon[current_weapon][2][1] - 10)
        if is_attacking:
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength + player.folie/100, weapon[current_weapon][3])

    if player.last_move_is_down:
        a = rotate(
            weapon[current_weapon][0], -0 - angle,
            (pos_player[0] + weapon[current_weapon][2][0] + 0, pos_player[1] + weapon[current_weapon][2][1] + 80),
            pygame.math.Vector2(0, -20))[1]
        w = graphic_main.screen.blit(rotate(
            weapon[current_weapon][0], -0 - angle, (
                pos_player[0] + weapon[current_weapon][2][0] + 0, pos_player[1] + weapon[current_weapon][2][1] + 80),
            pygame.math.Vector2(0, -20))[0], a)
        a.center = (
            pos_player[0] + weapon[current_weapon][2][0] + 12, pos_player[1] + weapon[current_weapon][2][1] + 25)
        if is_attacking:
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength + player.folie/100, weapon[current_weapon][3])

    if player.last_move_is_left:
        a = rotate(
            weapon[current_weapon][0], 0 - angle,
            (pos_player[0] + weapon[current_weapon][2][0] + -5, pos_player[1] + weapon[current_weapon][2][1] + 80),
            pygame.math.Vector2(0, -20))[1]
        w = graphic_main.screen.blit(rotate(
            weapon[current_weapon][0], 0 - angle, (
                pos_player[0] + weapon[current_weapon][2][0] - 5, pos_player[1] + weapon[current_weapon][2][1] + 80),
            pygame.math.Vector2(0, -20))[0], a)
        a.center = (
            pos_player[0] + weapon[current_weapon][2][0] + 12, pos_player[1] + weapon[current_weapon][2][1] + 25)
        if is_attacking:
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength + player.folie/100, weapon[current_weapon][3])
    return w, a
