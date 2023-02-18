# importation
import pygame
import player
import ennemy

# initialisation des variables
screen = None
frame = None

clock = pygame.time.Clock()


def initialisation(full_screen=False):
    pygame.init()
    global screen
    if full_screen:
        screen = pygame.display.set_mode((300, 200), flags=pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((300, 200))
    screen.fill((255, 0, 0))

    return screen


current = 0
player_pos = None
old_player_pos = None


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
    old_player_pos = player_pos
    screen.fill((0, 0, 0))
    update = []
    player_pos = screen.blit(frame[current], player.pos)
    update.append(player_pos)
    update.append(old_player_pos)
    for i in ennemy.enemy_1_list:
        ennemy_pos = screen.blit(i[0], i[1])
        update.append(ennemy_pos)
    if old_player_pos != None:
        pygame.display.update(update)
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
    global frame
    frame = []
    for i in range(0, nbr):
        frame.append(player1)
    for i in range(0, nbr):
        frame.append(player2)
    for i in range(0, nbr):
        frame.append(player3)
    return frame
