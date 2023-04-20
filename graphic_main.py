# importation
import pygame
import player
import ennemy
import tiles
import weapon
import room
import world

# initialisation des variables
screen = None
frame = None
frame_front = None
frame_L = None
frame_R = None
frame_back = None
frame_front_wounded = None
frame_back_wounded = None
frame_L_wounded = None
frame_R_wounded = None
clock = pygame.time.Clock()
r, u, door = None, None, None
trash_update = []
timer = 0
modifie = None
def initialisation(full_screen=False):
    pygame.init()
    pygame.mouse.set_visible(False)

    global screen
    if full_screen:
        screen = pygame.display.set_mode((0, 0), flags=pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((600, 400))
    pygame.display.flip()
    return screen


current = 0
player_pos = None
old_player_pos = None
old_w = None
w = None
update = []
old_update = []
chest = {}

"""
fonction boucle

Dans cette fonction, on affiche les differentes images afin de déplacer le personnage.
On utilise les variable p et old_p pour pouvoir stocker les coordonées des images et ainsi pour ne pas à avoir à update tout l'écran

"""


def boucle():
    global timer
    global player_pos
    global old_player_pos
    global frame
    global current
    global screen
    global w
    global old_w
    global update
    global old_update
    global trash_update
    global r
    timer -= 1
    if timer == 0:

        world.show_next_room()
    elif timer <= 0:
        u(old_update)
        player.boucle()
        old_update = update
        update = []
        player_pos = screen.blit(frame[current], player.pos)
        update.append(player_pos)
        update.extend(player.showpv())
        update.extend(player.showfolie())
        old_w = w
        for i in ennemy.enemy_1_list:
            ennemy_pos = screen.blit(i[0], i[1])
            update.append(ennemy_pos)

        for i in ennemy.enemy_1_2_list:
            ennemy_pos = screen.blit(i[0][i[8]], i[1])
            update.append(ennemy_pos)
        for i in ennemy.enemy_2_1_list:
            ennemy_pos = screen.blit(i[0][i[8]], i[1])
            update.append(ennemy_pos)
        for i in ennemy.enemy_2_2_list:
            ennemy_pos = screen.blit(i[0][0], i[1])
            update.append(ennemy_pos)
        for i in ennemy.enemy_3_1_list:
            ennemy_pos = screen.blit(i[0][i[8]], i[1])
            update.append(ennemy_pos)
        for i in ennemy.projectile_list:
            if type(i[4]) != int and i[4]:
                proj_pos = screen.blit(i[4], i[0])
            else:
                proj_pos = pygame.draw.circle(screen, i[3], i[0], i[1], 0)
            update.append(proj_pos)
        for i in ennemy.enemy_slime_list:
            ennemy_pos = screen.blit(i[0], i[1])
            update.append(ennemy_pos)
        for i in ennemy.boss_list:

            ennemy_pos = screen.blit(i[0][i[10]], i[1])
            update.append(ennemy_pos)
        for i in ennemy.enemy_4_1_list:
            ennemy_pos = screen.blit(i[0], i[1])
            update.append(ennemy_pos)
        for i in ennemy.enemy_4_2_list:
            ennemy_pos = screen.blit(i[0][i[8]], i[1])
            update.append(ennemy_pos)
        for i in ennemy.boss_list_4:
            ennemy_pos = screen.blit(i[0][0], i[1])
            update.append(ennemy_pos)
        for i in ennemy.boss_list_2:
            ennemy_pos = screen.blit(i[0][i[10]], i[1])
            update.append(ennemy_pos)
        for i in ennemy.boss_list_3:
            ennemy_pos = screen.blit(i[0][0], i[1])
            update.append(ennemy_pos)
        for i in ennemy.final_boss:
            print(i[1])
            ennemy_pos = screen.blit(i[0][i[13]], i[1])
            update.append(ennemy_pos)
        for i in ennemy.enemy_3_2_list:
            ennemy_pos = screen.blit(i[0][i[8]], i[1])
            update.append(ennemy_pos)
        w, a = weapon.loop(player.pos)

        update.append(w)
        update.append(a)
        ennemy.boucle()
        r = pygame.rect.Rect(0, 0, 50, 50)
        update.append(pygame.draw.rect(screen,(0, 0, 0), r))
        r = pygame.rect.Rect(150, 0, 50, 50)
        update.append(pygame.draw.rect(screen,(0, 0, 0), r))
        update.append(screen.blit(pygame.font.SysFont(None ,30).render(str(int(player.mana)), 1, (0, 0, 255)), (10, 10)))
        update.append(screen.blit(pygame.font.SysFont(None ,30).render(str(int(player.xp)), 1, (0, 255, 0)), (150, 10)))
        update.append(screen.blit(pygame.font.SysFont(None ,30).render(str(int(player.lvl)), 1, (0, 255, 0)), (200, 10)))

        pygame.display.update(update + old_update + trash_update)
        trash_update = []
        clock.tick(60)
        #print(clock.get_fps())
        if player.is_movement:
            current += 1
            current = current % len(frame)
        else:
            current = 0
    else:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)



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
    player1 = pygame.transform.scale(pygame.image.load('picture/character/Player_L_1.png').convert_alpha(), (30*(47/56), 47))
    player2 = pygame.transform.scale(pygame.image.load('picture/character/Player_L_3.png').convert_alpha(), (31*(47/55), 47))
    player3 = pygame.transform.scale(pygame.image.load('picture/character/Player_L_2.png').convert_alpha(), (30*(47/56), 47))
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
    player1 = pygame.transform.scale(pygame.image.load('picture/character/Player_R_1.png').convert_alpha(), (28*(47/54), 47))
    player2 = pygame.transform.scale(pygame.image.load('picture/character/Player_R_2.png').convert_alpha(), (28*(47/54), 47))
    player3 = pygame.transform.scale(pygame.image.load('picture/character/Player_R_3.png').convert_alpha(), (29*(47/55), 47))
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
    player1 = pygame.image.load('picture/character/player1_wounded.png').convert_alpha()
    player2 = pygame.image.load('picture/character/player2_wounded.png').convert_alpha()
    player3 = pygame.image.load('picture/character/player3_wounded.png').convert_alpha()
    global frame_front_wounded
    frame_front_wounded = []
    for i in range(0, nbr):
        frame_front_wounded.append(player1)
    for i in range(0, nbr):
        frame_front_wounded.append(player2)
    for i in range(0, nbr):
        frame_front_wounded.append(player1)
    for i in range(0, nbr):
        frame_front_wounded.append(player3)
    player1 = pygame.image.load('picture/character/Player_back_wounded_1.png').convert_alpha()
    player2 = pygame.image.load('picture/character/Player_back_wounded_2.png').convert_alpha()
    player3 = pygame.image.load('picture/character/Player_back_wounded_3.png').convert_alpha()
    global frame_back_wounded
    frame_back_wounded = []
    for i in range(0, nbr):
        frame_back_wounded.append(player1)
    for i in range(0, nbr):
        frame_back_wounded.append(player2)
    for i in range(0, nbr):
        frame_back_wounded.append(player1)
    for i in range(0, nbr):
        frame_back_wounded.append(player3)

    player1 = pygame.transform.scale(pygame.image.load('picture/character/Player_L_wounded_1.png').convert_alpha(), (28*(47/54), 47))
    player2 = pygame.transform.scale(pygame.image.load('picture/character/Player_L_wounded_3.png').convert_alpha(), (28*(47/54), 47))
    player3 = pygame.transform.scale(pygame.image.load('picture/character/Player_L_wounded_2.png').convert_alpha(), (29*(47/55), 47))
    global frame_L_wounded
    frame_L_wounded = []
    for i in range(0, nbr):
        frame_L_wounded.append(player1)
    for i in range(0, nbr):
        frame_L_wounded.append(player2)
    for i in range(0, nbr):
        frame_L_wounded.append(player1)
    for i in range(0, nbr):
        frame_L_wounded.append(player3)


    player1 = pygame.transform.scale(pygame.image.load('picture/character/Player_R_wounded_1.png').convert_alpha(), (28*(47/54), 47))
    player2 = pygame.transform.scale(pygame.image.load('picture/character/Player_R_wounded_2.png').convert_alpha(), (28*(47/54), 47))
    player3 = pygame.transform.scale(pygame.image.load('picture/character/Player_R_wounded_3.png').convert_alpha(), (29*(47/55), 47))
    global frame_R_wounded
    frame_R_wounded = []
    for i in range(0, nbr):
        frame_R_wounded.append(player1)
    for i in range(0, nbr):
        frame_R_wounded.append(player2)
    for i in range(0, nbr):
        frame_R_wounded.append(player1)
    for i in range(0, nbr):
        frame_R_wounded.append(player3)

    global frame
    frame = frame_back
    w, h = pygame.display.get_surface().get_size()
    player.barre_de_folie =  pygame.transform.scale(pygame.image.load('picture/ui/img1.jpg'
                                                                      ).convert_alpha(), [73 * w / 1920, 634 * h / 1080])
    return frame
