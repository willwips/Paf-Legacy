import room
import graphic_main
import random
import player
import pygame
floor = []
coo = [0, 0]
level = 0
pos_p = None
pygame.mixer.init()

# permet de créer le labyrinthe pour chaque niveau
def create_floor(_level):
    global floor
    floor = []
    _level = 2
    # pour chaque niveau, met les différentes salles dans un labyrinthe et lance la musique de la zone
    if _level == 0:
        pygame.mixer.music.load('picture/musique/musique_zone_1.mp3')
        pygame.mixer.music.play(loops=-1)
        first_room = room.room_1_0
        liste_level = [room.room_1_1, room.room_1_2, room.room_1_3, room.room_1_4, room.room_1_5, room.room_1_6, room.room_1_7, room.room_1_8, room.room_1_9, room.room_1_10, room.room_1_11, room.room_1_12]
        boss_room = room.room_boss_1
        pos_boss = [9,random.randint(0, 9)]
    if _level == 1:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('picture/musique/musique_zone_2.mp3')
        pygame.mixer.music.play(loops=-1)
        first_room = room.room_2_0
        liste_level = [room.room_2_1, room.room_2_2, room.room_2_3, room.room_2_4, room.room_2_5, room.room_2_6, room.room_2_7, room.room_2_8, room.room_2_9, room.room_2_10, room.room_2_11, room.room_2_12]
        boss_room = room.room_boss_2
        pos_boss = [9, random.randint(0, 9)]
    if _level == 2:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('picture/musique/musique_zone3.mp3')
        pygame.mixer.music.play(loops=-1)
        first_room = room.room_3_0
        liste_level = [room.room_3_1, room.room_3_2, room.room_3_3, room.room_3_4, room.room_3_5, room.room_3_6, room.room_3_7, room.room_3_8, room.room_3_9, room.room_3_10, room.room_3_11, room.room_3_12]
        boss_room = room.room_boss_3
        pos_boss = [9, random.randint(0, 9)]
    if _level == 3:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('picture/musique/musique_zone_4.mp3')
        pygame.mixer.music.play(loops=-1)
        first_room = room.room_4_0
        liste_level = [room.room_4_1, room.room_4_2, room.room_4_3, room.room_4_4, room.room_4_5, room.room_4_6, room.room_4_7, room.room_4_8, room.room_4_9, room.room_4_10, room.room_4_11, room.room_4_12]
        boss_room = room.room_boss_4
        pos_boss = [9, random.randint(0, 9)]
    if _level == 4:
        pygame.mixer.music.stop()
        first_room = room.room_5_0
        liste_level = [room.room_boss_5]
        pos_boss = None
    # créer le labyrinthe avec ces salles
    for i in range(10):
        floor.append([])    
        for j in range(0, 10):
            if j == 0 and i == 0:
                floor[i].append(first_room)
            elif pos_boss != None and i == pos_boss[0] and j == pos_boss[1]:
                floor[i].append(boss_room)
            else:
                floor[i].append(random.choice(liste_level))

# permet de passer au prochain niveau en recréant le labyrinthe et en réinitialisant la position du joueur
def next_level():
    global level
    global coo
    graphic_main.timer = 60
    coo = [0, 0]
    level += 1
    create_floor(level)
    next_room(0, 120)

create_floor(0)

# permet d'actualiser les coordonnés du joueur par rapport à la porte et d'afficher un écran noir
def next_room(n, time = 20):
    global pos_p
    pos_p = n
    graphic_main.timer = time
    player.timer = 120

# charge la prochaine salle et l'affiche sur l'écran
def show_next_room():
    try:
        graphic_main.r, graphic_main.u, graphic_main.door, graphic_main.top, graphic_main.bottom, graphic_main.left, graphic_main.right, player.pos, graphic_main.chest, graphic_main.modifie = \
        floor[coo[0] % 10][coo[1] % 10](pos_p, [not coo[0] == 9, not coo[1] == 9, not coo[0] == 0, not coo[1] == 0])
    except:
        graphic_main.r, graphic_main.u, graphic_main.door, graphic_main.top, graphic_main.bottom, graphic_main.left, graphic_main.right, player.pos, graphic_main.chest = floor[coo[0]%10][coo[1]%10](pos_p, [not coo[0] ==9, not coo[1] == 9, not coo[0]==0, not coo[1] == 0])
