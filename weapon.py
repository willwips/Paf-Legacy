import pygame
import graphic_main
import ennemy
import player

weapon = {}


def import_weapon():
    global weapon
    weapon['final_axe'] = (
        pygame.transform.scale(pygame.image.load('picture/weapon/final_axe.png').convert_alpha(), (20, 40)), 10, [17, 30], 10)


is_attacking = False
angle = 0
current_weapon = 'final_axe'
modify_angle = 5


def rotate(surface, angle, pivot, offset):
    rotated_image = pygame.transform.rotate(surface, -angle)
    rotated_offset = offset.rotate(angle)
    rect = rotated_image.get_rect(center=pivot + rotated_offset)
    return rotated_image, rect


def loop(pos_player):
    global angle
    global is_attacking
    global modify_angle
    if current_weapon == 'final_axe':
        return loop_final_axe(pos_player)


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
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength, weapon[current_weapon][3])
    
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
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength, weapon[current_weapon][3])
    
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
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength, weapon[current_weapon][3])

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
            ennemy.collision_with_weapon(w, weapon[current_weapon][1] + player.strength, weapon[current_weapon][3])
    return w, a
