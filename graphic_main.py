# importation
import pygame
import player
import ennemy
import weapon

# initialisation des variables
screen = None
frame = None
frame_front = None
frame_L = None
frame_R = None
frame_back = None
clock = pygame.time.Clock()


def initialisation(full_screen=False):
    pygame.init()
    global screen
    if full_screen:
        screen = pygame.display.set_mode((300, 200), flags=pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((300, 200))
    screen.fill((125, 125, 125))
    pygame.display.flip()
    return screen


current = 0
player_pos = None
old_player_pos = None
old_w = None
w = None
update = []
old_update = []

"""
fonction boucle

dans cette fonction, on affiche les differentes images afin de déplacé le personnage
on utilise les variable p et old_p pour pouvoir stocké les coordoné des images et ainsi pour ne pas à avoir à update tout l'écran

"""


def boucle():
    global player_pos
    global old_player_pos
    player.boucle()
    global frame
    global current
    global screen
    global w
    global old_w
    global update
    global old_update
    old_update = update
    screen.fill((125, 125, 125))
    update = []
    player_pos = screen.blit(frame[current], player.pos)
    update.append(player_pos)
    update.extend(player.showpv())
    old_w = w

    for i in ennemy.enemy_1_list:
        ennemy_pos = screen.blit(i[0], i[1])
        update.append(ennemy_pos)
    w, a = weapon.loop(player.pos)

    update.append(w)
    update.append(a)
    ennemy.boucle()

    pygame.display.update(update + old_update)
    clock.tick(60)
    if player.is_movement:
        current += 1
        current = current % len(frame)
    else:
        current = 0


def import_character_picture(nbr):
    player1 = pygame.image.load('picture/character/player1.png').convert_alpha()
    player2 = pygame.image.load('picture/character/player2.png').convert_alpha()
    player3 = pygame.image.load('picture/character/player3.png').convert_alpha()
    global frame_front
    frame_front = []
    for i in range(0, nbr):
        frame_front.append(player1)
    for i in range(0, nbr):
        frame_front.append(player2)
    for i in range(0, nbr):
        frame_front.append(player1)
    for i in range(0, nbr):
        frame_front.append(player3)
    player1 = pygame.image.load('picture/character/Player_L_1.png').convert_alpha()
    player2 = pygame.image.load('picture/character/Player_L_3.png').convert_alpha()
    player3 = pygame.image.load('picture/character/Player_L_2.png').convert_alpha()
    global frame_L
    frame_L = []
    for i in range(0, nbr):
        frame_L.append(player1)
    for i in range(0, nbr):
        frame_L.append(player2)
    for i in range(0, nbr):
        frame_L.append(player1)
    for i in range(0, nbr):
        frame_L.append(player3)
    player1 = pygame.image.load('picture/character/Player_R_1.png').convert_alpha()
    player2 = pygame.image.load('picture/character/Player_R_2.png').convert_alpha()
    player3 = pygame.image.load('picture/character/Player_R_3.png').convert_alpha()
    global frame_R
    frame_R = []
    for i in range(0, nbr):
        frame_R.append(player1)
    for i in range(0, nbr):
        frame_R.append(player2)
    for i in range(0, nbr):
        frame_R.append(player1)
    for i in range(0, nbr):
        frame_R.append(player3)
    player1 = pygame.image.load('picture/character/Player_back_1.png').convert_alpha()
    player2 = pygame.image.load('picture/character/Player_back_2.png').convert_alpha()
    player3 = pygame.image.load('picture/character/Player_back_3.png').convert_alpha()
    global frame_back
    frame_back = []
    for i in range(0, nbr):
        frame_back.append(player1)
    for i in range(0, nbr):
        frame_back.append(player2)
    for i in range(0, nbr):
        frame_back.append(player1)
    for i in range(0, nbr):
        frame_back.append(player3)
    global frame
    frame=frame_L

    return frame
