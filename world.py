# importation
import room
import graphic_main
import random
import player

# initialisation de variables
floor = []
coo = [0, 0]
level = 0
pos_p = None

# Définition d'une variable permettant la création des niveaux
def create_floor(_level):
    global floor
    floor = []
    _level = 1
    if _level == 0: # Si le joueur est au premier niveau c'est ce dernier qui va être affiché
        first_room = room.room_1_0 # Première salle du jeu
        liste_level = [room.room_1_1, room.room_1_2, room.room_1_3, room.room_1_4, room.room_1_5, room.room_1_6, room.room_1_7, room.room_1_8, room.room_1_9, room.room_1_10, room.room_1_11, room.room_1_12] # Salles qui composent le niveau
        boss_room = room.room_boss_1 # Salle du boss
        pos_boss = [9,random.randint(0, 9)] # Permet de positionner la salle du boss
    if _level == 1: # Même procédé que les autres niveaux pour le niveau 2
        first_room = room.room_boss_2
        liste_level = [room.room_2_1, room.room_2_2, room.room_2_3, room.room_2_4, room.room_2_5, room.room_2_6, room.room_2_7, room.room_2_8, room.room_2_9, room.room_2_10, room.room_2_11, room.room_2_12]
        boss_room = room.room_boss_2
        pos_boss = [9, random.randint(0, 9)]
    if _level == 2: # Même procédé que les autres niveaux pour le niveau 3
        first_room = room.room_3_0
        liste_level = [room.room_3_1, room.room_3_2, room.room_3_3, room.room_3_4, room.room_3_5, room.room_3_6, room.room_3_7, room.room_3_8, room.room_3_9, room.room_3_10, room.room_3_11, room.room_3_12]
        boss_room = room.room_boss_3
        pos_boss = [9, random.randint(0, 9)]
    if _level == 3: # Même procédé que les autres niveaux pour le niveau 4
        first_room = room.room_4_0
        liste_level = [room.room_4_1, room.room_4_2, room.room_4_3, room.room_4_4, room.room_4_5, room.room_4_6, room.room_4_7, room.room_4_8, room.room_4_9, room.room_4_10, room.room_4_11, room.room_4_12]
        boss_room = room.room_boss_4
        pos_boss = [9, random.randint(0, 9)]
    if _level == 4: # Même procédé que les autres niveaux pour le niveau final (5)
        player.xp = 1000 # Redéfini les ponts d'expérience du joueur
        first_room = room.room_5_0
        liste_level = [room.room_boss_5]
        pos_boss = None
    for i in range(10): # Permet de créer le niveau
        floor.append([]) # Regroupe les salles du niveau du joueur
        for j in range(0, 10):
            if j == 0 and i == 0: # Affiche la première salle du niveau 
                floor[i].append(first_room)
            elif pos_boss != None and i == pos_boss[0] and j == pos_boss[1]:
                floor[i].append(boss_room)
            else: # Ajoute une salle de manière aléatoire pour ne pas toujours avoir le même niveau à chaque partie
                floor[i].append(random.choice(liste_level))

# Fonciton qui permet le changement de niveau
def next_level(): 
    global level
    global coo
    graphic_main.timer = 60 # Temps d'attente défini 
    coo = [0, 0] # Coordonnées réinitialisées
    level += 1 # Création du niveau supérieur à l'actuel
    create_floor(level) # Créer le niveau
    next_room(0, 120) # Affiche les salles

create_floor(0) # Le premier niveau du jeu est crée

def next_room(n, time = 20):
    global pos_p
    pos_p = n
    graphic_main.timer = time
    player.timer = 120
def show_next_room():
    try:
        graphic_main.r, graphic_main.u, graphic_main.door, graphic_main.top, graphic_main.bottom, graphic_main.left, graphic_main.right, player.pos, graphic_main.chest, graphic_main.modifie = \
        floor[coo[0] % 10][coo[1] % 10](pos_p, [not coo[0] == 9, not coo[1] == 9, not coo[0] == 0, not coo[1] == 0])
    except:
        graphic_main.r, graphic_main.u, graphic_main.door, graphic_main.top, graphic_main.bottom, graphic_main.left, graphic_main.right, player.pos, graphic_main.chest = floor[coo[0]%10][coo[1]%10](pos_p, [not coo[0] ==9, not coo[1] == 9, not coo[0]==0, not coo[1] == 0])
