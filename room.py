import pygame
import ennemy
import player
import tiles
import graphic_main
import weapon


# Fonction qui s'occupe de ce qui est lié au soin
def heal(pv):
    a = pv

    # Fonction qui permet au joueur de se soigner
    def _heal():
        player.pv += a
        player.possible_object_picture = None
        player.possible_object = player._pass

    # Fonction qui affiche l'objet de soin sur l'écran
    def __heal():
        player.possible_object = _heal
        player.possible_object_picture = pygame.image.load('picture/ui/Potions Soin.png').convert_alpha()

    return __heal


# Fonction qui permet de changer d'arme
def change_weapon(_weapon):
    def _change():
        weapon.current_weapon = _weapon

    return _change


# Fonction qui défini la salle 0 du niveau 1 (la salle d'apparition)
def room_1_0(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 20  # Longueur x de la salle
    y = 10  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de 
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                               tiles.blit_bottom_mid(i * 50 + left,
                                                                                     j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_left_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_top_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_4_1(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_4_1(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # ennemy.spawn_enemy_4_2([left + 550, top + 250], 'picture/enemy/snipe/mob_1.png', 20)
        # ennemy.spawn_enemy_4_1([left + 320, top + 400], 'picture/enemy/mage/Mage.png', 20)
        # ennemy.spawn_enemy_4_1([left + 370, top + 80], 'picture/enemy/mage/Mage.png', 20)
        # ennemy.spawn_enemy_4_2([left + 427, top + 79], 'picture/enemy/snipe/mob_1.png', 20)
        # ennemy.spawn_boss_4([left + 427, top + 79], 200)
        # ennemy.spawn_enemy_2_2([left + 427, top + 79], ['picture/enemy/spider/araignee.png'], 20)
        # ennemy.spawn_boss_4([left + 427, top + 79], 200)
        # ennemy.spawn_enemy_2_2([left + 427, top + 79], ['picture/enemy/spider/araignee.png'], 20)
        ennemy.spawn_enemy_3_1([left + 427, top + 79],
                               ['picture/enemy/star/star enemy.png', 'picture/enemy/star/star enemy 2.png'], 20)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Fonction qui défini la salle 1 du niveau 1
def room_1_1(n, _door):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]

    x = 18  # Longueur x de la salle
    y = 7  # Longueur y de la salle

    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == 3 and i == 9:
                    room[i].append(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                           tiles.blit_tile_4_1(i * 50 + left, j * 50 + top), 0)[0])
                    chest.update(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                         tiles.blit_tile_4_1(i * 50 + left, j * 50 + top), heal(50))[1])
                elif j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                               tiles.blit_bottom_mid(i * 50 + left,
                                                                                     j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_left_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_top_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))  # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_4_1(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_2_1(i * 50 + left, j * 50 + top))

        # Créer les ennemies du fichier ennemy et les affiches
        ennemy.spawn_enemy_1_2([left + 300, top + 80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 250, top + 150], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 350, top + 100], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1([left + 180, top + 223], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 60, top + 85], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 400, top + 200], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 210, top + 125], 'picture/enemy/skeleton/skeleton-front.png', 50)

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        player.pos = [50 + left, 220 + top]

        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Fonction qui défini la salle 2 du niveau 1
def room_1_2(n, _door):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]
    x = 9  # Longueur x de la salle
    y = 9  # Longueur y de la salle
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                               tiles.blit_bottom_mid(i * 50 + left,
                                                                                     j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_left_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_top_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))  # Porte 4# Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_1(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_1_1(i * 50 + left, j * 50 + top))

        # ennely (voir main)
        ennemy.spawn_enemy_1_2([left + 80, top + 80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 250, top + 150], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)

        ennemy.spawn_enemy_1([left + 80, top + 223], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 210, top + 85], 'picture/enemy/skeleton/skeleton-front.png', 50)
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        player.pos = [50 + left, 220 + top]

        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Fonction qui défini la salle 3 du niveau 1
def room_1_3(n, _door):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]
    x = 15  # Longueur x de la salle
    y = 8  # Longueur y de la salle
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                               tiles.blit_bottom_mid(i * 50 + left,
                                                                                     j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_left_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_top_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))  # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_4_1(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_4_1(i * 50 + left, j * 50 + top))

        # ennemy (voir main)
        ennemy.spawn_enemy_1_2([left + 80, top + 80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 250, top + 150], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1([left + 72, top + 123], 'picture/enemy/skeleton/skeleton-front.png', 50)

        ennemy.spawn_enemy_1([left + 80, top + 223], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 210, top + 85], 'picture/enemy/skeleton/skeleton-front.png', 50)
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        player.pos = [50 + left, 220 + top]

        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Fonction qui défini la salle 4 du niveau 1
def room_1_4(n, _door):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]
    x = 27  # Longueur x de la salle
    y = 4  # Longueur y de la salle
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                               tiles.blit_bottom_mid(i * 50 + left,
                                                                                     j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_left_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_top_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))  # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_2_1(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_3_1(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_1([left + 100, top + 75], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 150, top + 75], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 200, top + 75], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 250, top + 75], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 300, top + 75], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 500, top + 100], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 500, top + 50], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 450, top + 100], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 450, top + 50], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 400, top + 100], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 400, top + 50], 'picture/enemy/skeleton/skeleton-front.png', 50)

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        player.pos = [50 + left, 220 + top]
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Fonction qui défini la salle 5 du niveau 1
def room_1_5(n, _door):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]
    x = 5  # Longueur x de la salle
    y = 5  # Longueur y de la salle
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == 2 and i == 2:
                    room[i].append(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                           tiles.blit_tile_2_1(i * 50 + left, j * 50 + top), 0)[0])
                    chest.update(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                         tiles.blit_tile_2_1(i * 50 + left, j * 50 + top), heal(50))[1])

                elif j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                               tiles.blit_bottom_mid(i * 50 + left,
                                                                                     j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_left_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_top_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))  # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_2_1(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_2_1(i * 50 + left, j * 50 + top))

        # Apparition du coffre

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        player.pos = [50 + left, 220 + top]
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Fonction qui défini la salle 6 du niveau 1
def room_1_6(n, _door):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]
    x = 20  # Longueur x de la salle
    y = 15  # Longueur y de la salle
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == 7 and i == 10:
                    room[i].append(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                           tiles.blit_tile_4_1(i * 50 + left, j * 50 + top), 0)[0])
                    chest.update(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                         tiles.blit_tile_4_1(i * 50 + left, j * 50 + top), heal(50))[1])
                elif j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                               tiles.blit_bottom_mid(i * 50 + left,
                                                                                     j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_left_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_top_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))  # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_1_1(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_4_1(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_1_2([left + 80, top + 80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 120, top + 250], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 180, top + 180], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 300, top + 250], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 280, top + 280], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 250, top + 150], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 400, top + 400], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 550, top + 530], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 450, top + 580], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 500, top + 650], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 550, top + 280], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 600, top + 90], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 650, top + 680], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 700, top + 250], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 750, top + 240], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 250, top + 50], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        player.pos = [50 + left, 220 + top]
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Fonction qui défini la salle 7 du niveau 1
def room_1_7(n, _door):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]
    x = 12  # Longueur x de la salle
    y = 8  # Longueur y de la salle
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                               tiles.blit_bottom_mid(i * 50 + left,
                                                                                     j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_left_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_top_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))  # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_1(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_4_1(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_1_2([left + 80, top + 80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 120, top + 250], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 180, top + 180], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1([left + 60, top + 100], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 60, top + 52], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 110, top + 52], 'picture/enemy/skeleton/skeleton-front.png', 50)

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        player.pos = [50 + left, 220 + top]
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Fonction qui défini la salle 8 du niveau 1
def room_1_8(n, _door):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]
    x = 15  # Longueur x de la salle
    y = 10  # Longueur y de la salle
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == 5 and i == 7:
                    room[i].append(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                           tiles.blit_tile_3_1(i * 50 + left, j * 50 + top), 0)[0])
                    chest.update(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                         tiles.blit_tile_3_1(i * 50 + left, j * 50 + top), heal(50))[1])
                elif j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                               tiles.blit_bottom_mid(i * 50 + left,
                                                                                     j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_left_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_top_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))  # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_1(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_4_1(i * 50 + left, j * 50 + top))

        # Coffre au milieu de la salle

        ennemy.spawn_enemy_1([left + 60, top + 100], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 110, top + 52], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 650, top + 100], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 600, top + 52], 'picture/enemy/skeleton/skeleton-front.png', 50)  #
        ennemy.spawn_enemy_1([left + 60, top + 350], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 110, top + 400], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 650, top + 350], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 600, top + 400], 'picture/enemy/skeleton/skeleton-front.png', 50)
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        player.pos = [50 + left, 220 + top]
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Fonction qui défini la salle 9 du niveau 1
def room_1_9(n, _door):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]
    x = 9  # Longueur x de la salle
    y = 14  # Longueur y de la salle
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == 7 and i == 4:
                    room[i].append(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                           tiles.blit_tile_2_1(i * 50 + left, j * 50 + top), 0)[0])
                    chest.update(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                         tiles.blit_tile_2_1(i * 50 + left, j * 50 + top), heal(50))[1])

                elif j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                               tiles.blit_bottom_mid(i * 50 + left,
                                                                                     j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_left_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_top_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))  # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_1_1(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_2_1(i * 50 + left, j * 50 + top))
        # Coffre au milieu de la salle
        ennemy.spawn_enemy_1([left + 360, top + 50], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 60, top + 50], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1_2([left + 120, top + 250], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 180, top + 180], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1([left + 60, top + 600], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 360, top + 600], 'picture/enemy/skeleton/skeleton-front.png', 50)

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        player.pos = [50 + left, 220 + top]
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Fonction qui défini la salle 10 du niveau 1
def room_1_10(n, _door):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]
    x = 3  # Longueur x de la salle
    y = 10  # Longueur y de la salle
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                               tiles.blit_bottom_mid(i * 50 + left,
                                                                                     j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_left_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_top_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))  # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_1(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_2_1(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_1([left + 60, top + 200], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 60, top + 250], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 60, top + 300], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 60, top + 350], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 60, top + 400], 'picture/enemy/skeleton/skeleton-front.png', 50)

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        player.pos = [50 + left, 220 + top]
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Fonction qui défini la salle 11 du niveau 1
def room_1_11(n, _door):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]
    x = 7  # Longueur x de la salle
    y = 12  # Longueur y de la salle
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                               tiles.blit_bottom_mid(i * 50 + left,
                                                                                     j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_left_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_top_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))  # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_4_1(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_3_1(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_1([left + 190, top + 120], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 130, top + 120], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 220, top + 60], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 160, top + 60], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 100, top + 60], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 220, top + 180], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 160, top + 180], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 100, top + 180], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 260, top + 500], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 60, top + 500], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1_2([left + 280, top + 80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 120, top + 450], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        player.pos = [50 + left, 220 + top]
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Fonction qui défini la salle 12 du niveau 1
def room_1_12(n, _door):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]
    x = 13  # Longueur x de la salle
    y = 5  # Longueur y de la salle
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                               tiles.blit_bottom_mid(i * 50 + left,
                                                                                     j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_left_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_top_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))  # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_1(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_2_1(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_1([left + 310, top + 100], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 360, top + 150], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 260, top + 65], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 210, top + 50], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1_2([left + 150, top + 80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               50)
        ennemy.spawn_enemy_1([left + 260, top + 150], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 360, top + 65], 'picture/enemy/skeleton/skeleton-front.png', 50)
        ennemy.spawn_enemy_1([left + 410, top + 50], 'picture/enemy/skeleton/skeleton-front.png', 50)

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        player.pos = [50 + left, 220 + top]
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Fonction qui défini la salle du boss du niveau 1
def room_boss_1(n, _door):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]
    x = 12  # Longueur x de la salle
    y = 12  # Longueur y de la salle
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                               tiles.blit_bottom_mid(i * 50 + left,
                                                                                     j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_left_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                               tiles.blit_wall_top_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))  # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_1(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_2_1(i * 50 + left, j * 50 + top))

        if n == 0:
            ennemy.spawn_boss_1([left + 80, top + 275], 100)
        elif n == 1:
            ennemy.spawn_boss_1([left + 300, top + 80], 100)
        elif n == 2:
            ennemy.spawn_boss_1([left + 450, top + 275], 100)
        elif n == 3:
            ennemy.spawn_boss_1([left + 300, top + 450], 100)

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        player.pos = [50 + left, 220 + top]
        door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4

    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Initialisation des salles du niveau 2
def room_2_0(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 20  # Longueur x de la salle
    y = 10  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_purple(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_mid(i * 50 + left,
                                                                                  j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_purple_3(i * 50 + left, j * 50 + top,
                                                                tiles.blit_bottom_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_purple_4(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_left_mid(i * 50 + left,
                                                                                         j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_purple_2(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_top_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_4_2(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_1_2(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]
        # ennemy.spawn_boss_2([left + 427, top + 79], 80)

        # ennemy.spawn_boss_2([left + 427, top + 79], 80)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_2_1(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 13  # Longueur x de la salle
    y = 7  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_purple(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_mid(i * 50 + left,
                                                                                  j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_purple_3(i * 50 + left, j * 50 + top,
                                                                tiles.blit_bottom_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_purple_4(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_left_mid(i * 50 + left,
                                                                                         j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_purple_2(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_top_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_2_2(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_1_2(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_2_2([left + 350, top + 150], ['picture/enemy/spider/araignee.png'], 20)
        ennemy.spawn_enemy_2_2([left + 300, top + 150], ['picture/enemy/spider/araignee.png'], 20)
        ennemy.spawn_enemy_2_2([left + 250, top + 150], ['picture/enemy/spider/araignee.png'], 20)
        # ennemy.spawn_enemy_2_1([350, 350],  ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png', 'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png', 'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_2_2(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 11  # Longueur x de la salle
    y = 7  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_purple(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_mid(i * 50 + left,
                                                                                  j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_purple_3(i * 50 + left, j * 50 + top,
                                                                tiles.blit_bottom_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_purple_4(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_left_mid(i * 50 + left,
                                                                                         j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_purple_2(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_top_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_2(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_1_2(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_2_1([left + 60, top + 50], ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                                       'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                                       'picture/enemy/foe/foe_R_2.png',
                                                       'picture/enemy/foe/foe_R_3.png'], 40)
        ennemy.spawn_enemy_2_1([left + 460, top + 50],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 40)
        ennemy.spawn_enemy_2_1([left + 60, top + 250],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 40)
        ennemy.spawn_enemy_2_1([left + 460, top + 250],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 40)

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_2_3(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 17  # Longueur x de la salle
    y = 11  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == 5 and i == 8:
                    room[i].append(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                           tiles.blit_tile_1_2(i * 50 + left, j * 50 + top), 0)[0])
                    chest.update(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                         tiles.blit_tile_1_2(i * 50 + left, j * 50 + top), heal(50))[1])
                elif j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_purple(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_mid(i * 50 + left,
                                                                                  j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_purple_3(i * 50 + left, j * 50 + top,
                                                                tiles.blit_bottom_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_purple_4(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_left_mid(i * 50 + left,
                                                                                         j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_purple_2(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_top_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_4_2(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_1_2(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_2_1([left + 110, top + 50],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 40)
        ennemy.spawn_enemy_2_1([left + 60, top + 100],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 40)
        ennemy.spawn_enemy_2_1([left + 710, top + 50],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 40)
        ennemy.spawn_enemy_2_1([left + 760, top + 100],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 40)

        ennemy.spawn_enemy_2_1([left + 110, top + 450],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 40)
        ennemy.spawn_enemy_2_1([left + 60, top + 400],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 40)
        ennemy.spawn_enemy_2_1([left + 760, top + 450],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 40)
        ennemy.spawn_enemy_2_1([left + 760, top + 400],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 40)

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_2_4(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 19  # Longueur x de la salle
    y = 5  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_purple(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_mid(i * 50 + left,
                                                                                  j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_purple_3(i * 50 + left, j * 50 + top,
                                                                tiles.blit_bottom_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_purple_4(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_left_mid(i * 50 + left,
                                                                                         j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_purple_2(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_top_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_2_2(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_3_2(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_2_1([left + 410, top + 100],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 40)
        ennemy.spawn_enemy_2_1([left + 510, top + 100],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 40)
        ennemy.spawn_enemy_2_2([left + 460, top + 100], ['picture/enemy/spider/araignee.png'], 20)

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_2_5(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 5  # Longueur x de la salle
    y = 5  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == 2 and i == 2:
                    room[i].append(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                           tiles.blit_tile_2_2(i * 50 + left, j * 50 + top), 0)[0])
                    chest.update(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                         tiles.blit_tile_2_2(i * 50 + left, j * 50 + top), heal(50))[1])
                elif j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_purple(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_mid(i * 50 + left,
                                                                                  j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_purple_3(i * 50 + left, j * 50 + top,
                                                                tiles.blit_bottom_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_purple_4(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_left_mid(i * 50 + left,
                                                                                         j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_purple_2(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_top_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_2_2(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_2_2(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_2_6(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 17  # Longueur x de la salle
    y = 11  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == 5 and i == 8:
                    room[i].append(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                           tiles.blit_tile_4_2(i * 50 + left, j * 50 + top), 0)[0])
                    chest.update(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                         tiles.blit_tile_4_2(i * 50 + left, j * 50 + top), heal(50))[1])
                elif j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_purple(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_mid(i * 50 + left,
                                                                                  j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_purple_3(i * 50 + left, j * 50 + top,
                                                                tiles.blit_bottom_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_purple_4(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_left_mid(i * 50 + left,
                                                                                         j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_purple_2(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_top_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_2_2(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_4_2(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_2_1([left + 360, top + 250],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)
        ennemy.spawn_enemy_2_1([left + 460, top + 250],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)

        ennemy.spawn_enemy_2_1([left + 410, top + 200],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)
        ennemy.spawn_enemy_2_1([left + 410, top + 300],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)

        ennemy.spawn_enemy_2_2([left + 410, top + 250], ['picture/enemy/spider/araignee.png'], 20)
        ennemy.spawn_enemy_2_2([left + 410, top + 250], ['picture/enemy/spider/araignee.png'], 20)

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_2_7(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 7  # Longueur x de la salle
    y = 7  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_purple(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_mid(i * 50 + left,
                                                                                  j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_purple_3(i * 50 + left, j * 50 + top,
                                                                tiles.blit_bottom_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_purple_4(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_left_mid(i * 50 + left,
                                                                                         j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_purple_2(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_top_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_2(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_4_2(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_2_2([left + 150, top + 150], ['picture/enemy/spider/araignee.png'], 20)

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_2_8(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 6  # Longueur x de la salle
    y = 11  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_purple(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_mid(i * 50 + left,
                                                                                  j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_purple_3(i * 50 + left, j * 50 + top,
                                                                tiles.blit_bottom_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_purple_4(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_left_mid(i * 50 + left,
                                                                                         j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_purple_2(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_top_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_2_2(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_1_2(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_2_2([left + 100, top + 250], ['picture/enemy/spider/araignee.png'], 20)
        ennemy.spawn_enemy_2_2([left + 100, top + 250], ['picture/enemy/spider/araignee.png'], 20)

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_2_9(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 10  # Longueur x de la salle
    y = 13  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_purple(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_mid(i * 50 + left,
                                                                                  j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_purple_3(i * 50 + left, j * 50 + top,
                                                                tiles.blit_bottom_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_purple_4(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_left_mid(i * 50 + left,
                                                                                         j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_purple_2(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_top_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_2_2(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_3_2(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_2_2([left + 250, top + 300], ['picture/enemy/spider/araignee.png'], 20)
        ennemy.spawn_enemy_2_2([left + 250, top + 300], ['picture/enemy/spider/araignee.png'], 20)

        ennemy.spawn_enemy_2_1([left + 200, top + 150],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)
        ennemy.spawn_enemy_2_1([left + 250, top + 150],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)
        ennemy.spawn_enemy_2_1([left + 300, top + 150],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)
        ennemy.spawn_enemy_2_1([left + 150, top + 100],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)
        ennemy.spawn_enemy_2_1([left + 350, top + 100],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_2_10(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 7  # Longueur x de la salle
    y = 9  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_purple(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_mid(i * 50 + left,
                                                                                  j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_purple_3(i * 50 + left, j * 50 + top,
                                                                tiles.blit_bottom_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_purple_4(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_left_mid(i * 50 + left,
                                                                                         j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_purple_2(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_top_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_2_2(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_4_2(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_2_2([left + 100, top + 200], ['picture/enemy/spider/araignee.png'], 20)
        ennemy.spawn_enemy_2_2([left + 200, top + 200], ['picture/enemy/spider/araignee.png'], 20)

        ennemy.spawn_enemy_2_1([left + 150, top + 200],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_2_11(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 9  # Longueur x de la salle
    y = 9  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == 4 and i == 4:
                    room[i].append(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                           tiles.blit_tile_3_2(i * 50 + left, j * 50 + top), 0)[0])
                    chest.update(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                         tiles.blit_tile_3_2(i * 50 + left, j * 50 + top), heal(50))[1])
                elif j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_purple(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_mid(i * 50 + left,
                                                                                  j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_purple_3(i * 50 + left, j * 50 + top,
                                                                tiles.blit_bottom_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_purple_4(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_left_mid(i * 50 + left,
                                                                                         j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_purple_2(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_top_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_2(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_4_2(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_2_2([left + 200, top + 200], ['picture/enemy/spider/araignee.png'], 20)

        ennemy.spawn_enemy_2_1([left + 150, top + 200],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)
        ennemy.spawn_enemy_2_1([left + 250, top + 200],
                               ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_2_12(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 4  # Longueur x de la salle
    y = 11  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_purple(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_mid(i * 50 + left,
                                                                                  j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_purple_3(i * 50 + left, j * 50 + top,
                                                                tiles.blit_bottom_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_purple_4(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_left_mid(i * 50 + left,
                                                                                         j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_purple_2(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_top_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_2(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_4_2(i * 50 + left, j * 50 + top))

        ennemy.spawn_enemy_2_2([left + 50, top + 150], ['picture/enemy/spider/araignee.png'], 20)

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_boss_2(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 21  # Longueur x de la salle
    y = 9  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_purple(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_mid(i * 50 + left,
                                                                                  j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_purple_3(i * 50 + left, j * 50 + top,
                                                                tiles.blit_bottom_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_purple_4(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_left_mid(i * 50 + left,
                                                                                         j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_purple_2(i * 50 + left, j * 50 + top,
                                                                tiles.blit_wall_top_mid(i * 50 + left,
                                                                                        j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_4_2(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_1_2(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_boss_2([left + 427, top + 79], 80)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


# Initialisation des salles du niveau 4
def room_4_0(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 20  # Longueur x de la salle
    y = 10  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_4_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_1_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # ennemy.spawn_enemy_4_2([left + 550, top + 250], 'picture/enemy/snipe/mob_1.png', 20)
        # ennemy.spawn_enemy_4_1([left + 320, top + 400], 'picture/enemy/mage/Mage.png', 20)
        # ennemy.spawn_enemy_4_1([left + 370, top + 80], 'picture/enemy/mage/Mage.png', 20)
        # ennemy.spawn_enemy_4_2([left + 427, top + 79], 'picture/enemy/snipe/mob_1.png', 20)
        # ennemy.spawn_boss_4([left + 427, top + 79], 200)
        # ennemy.spawn_enemy_2_2([left + 427, top + 79], ['picture/enemy/spider/araignee.png'], 20)
        ennemy.spawn_boss_2([left + 427, top + 79], 80)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_4_1(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 13  # Longueur x de la salle
    y = 13  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_2_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_1_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_enemy_4_2([left + 350, top + 250], 'picture/enemy/snipe/mob_1.png', 20)
        ennemy.spawn_enemy_4_1([left + 320, top + 100], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 370, top + 80], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_2([left + 450, top + 100], 'picture/enemy/snipe/mob_1.png', 20)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_4_2(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 21  # Longueur x de la salle
    y = 5  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == 2 and i == 10:
                    room[i].append(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                           tiles.blit_tile_3_4(i * 50 + left, j * 50 + top), 0)[0])
                    chest.update(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                         tiles.blit_tile_3_4(i * 50 + left, j * 50 + top), heal(50))[1])
                elif j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_1_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_enemy_4_1([left + 550, top + 50], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 450, top + 50], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 550, top + 150], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 450, top + 150], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_2([left + 500, top + 100], 'picture/enemy/snipe/mob_1.png', 20)
        ennemy.spawn_enemy_4_2([left + 500, top + 100], 'picture/enemy/snipe/mob_1.png', 20)
        # ennemy.spawn_boss_4([left + 427, top + 79], 200)
        # ennemy.spawn_enemy_2_2([left + 427, top + 79], ['picture/enemy/spider/araignee.png'], 20)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_4_3(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 9  # Longueur x de la salle
    y = 13  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_2_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_enemy_4_1([left + 200, top + 250], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 200, top + 300], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 200, top + 350], 'picture/enemy/mage/Mage.png', 20)

        # ennemy.spawn_boss_4([left + 427, top + 79], 200)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_4_4(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 15  # Longueur x de la salle
    y = 9  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_4_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_enemy_4_1([left + 50, top + 50], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 50, top + 350], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 650, top + 50], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 650, top + 350], 'picture/enemy/mage/Mage.png', 20)
        # ennemy.spawn_boss_4([left + 427, top + 79], 200)
        # ennemy.spawn_enemy_2_2([left + 427, top + 79], ['picture/enemy/spider/araignee.png'], 20)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_4_5(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 5  # Longueur x de la salle
    y = 5  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == 2 and i == 2:
                    room[i].append(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                           tiles.blit_tile_2_4(i * 50 + left, j * 50 + top), 0)[0])
                    chest.update(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                         tiles.blit_tile_2_4(i * 50 + left, j * 50 + top), heal(50))[1])
                elif j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_2_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_2_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_4_6(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 23  # Longueur x de la salle
    y = 15  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == 7 and i == 11:
                    room[i].append(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                           tiles.blit_tile_1_4(i * 50 + left, j * 50 + top), 0)[0])
                    chest.update(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                         tiles.blit_tile_1_4(i * 50 + left, j * 50 + top), heal(50))[1])
                elif j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_1_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_4_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_enemy_4_1([left + 450, top + 300], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 450, top + 350], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 450, top + 400], 'picture/enemy/mage/Mage.png', 20)

        ennemy.spawn_enemy_4_1([left + 650, top + 300], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 650, top + 350], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 650, top + 400], 'picture/enemy/mage/Mage.png', 20)

        ennemy.spawn_enemy_4_1([left + 500, top + 250], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 550, top + 250], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 600, top + 250], 'picture/enemy/mage/Mage.png', 20)

        ennemy.spawn_enemy_4_1([left + 500, top + 450], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 550, top + 450], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 600, top + 450], 'picture/enemy/mage/Mage.png', 20)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_4_7(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 17  # Longueur x de la salle
    y = 11  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_2_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_enemy_4_1([left + 400, top + 200], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 400, top + 300], 'picture/enemy/mage/Mage.png', 20)

        ennemy.spawn_enemy_4_2([left + 250, top + 250], 'picture/enemy/snipe/mob_1.png', 20)
        ennemy.spawn_enemy_4_2([left + 550, top + 250], 'picture/enemy/snipe/mob_1.png', 20)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_4_8(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 9  # Longueur x de la salle
    y = 9  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_2_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_4_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_enemy_4_1([left + 200, top + 100], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 100, top + 250], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 300, top + 250], 'picture/enemy/mage/Mage.png', 20)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_4_9(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 7  # Longueur x de la salle
    y = 7  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_3_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_enemy_4_1([left + 150, top + 150], 'picture/enemy/mage/Mage.png', 20)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_4_10(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 5  # Longueur x de la salle
    y = 5  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_3_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_enemy_4_1([left + 100, top + 100], 'picture/enemy/mage/Mage.png', 20)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_4_10(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 21  # Longueur x de la salle
    y = 13  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_4_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_2_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_enemy_4_2([left + 350, top + 300], 'picture/enemy/snipe/mob_1.png', 20)
        ennemy.spawn_enemy_4_2([left + 450, top + 300], 'picture/enemy/snipe/mob_1.png', 20)
        ennemy.spawn_enemy_4_2([left + 550, top + 300], 'picture/enemy/snipe/mob_1.png', 20)
        ennemy.spawn_enemy_4_2([left + 650, top + 300], 'picture/enemy/snipe/mob_1.png', 20)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_4_11(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 9  # Longueur x de la salle
    y = 13  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == 6 and i == 4:
                    room[i].append(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                           tiles.blit_tile_1_4(i * 50 + left, j * 50 + top), 0)[0])
                    chest.update(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                         tiles.blit_tile_1_4(i * 50 + left, j * 50 + top), heal(50))[1])
                elif j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_1_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_2_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_enemy_4_2([left + 100, top + 300], 'picture/enemy/snipe/mob_1.png', 20)
        ennemy.spawn_enemy_4_2([left + 300, top + 300], 'picture/enemy/snipe/mob_1.png', 20)

        ennemy.spawn_enemy_4_1([left + 200, top + 200], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 200, top + 400], 'picture/enemy/mage/Mage.png', 20)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_4_12(n, _door):
    # Listes qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 11  # Longueur x de la salle
    y = 11  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_2_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_4_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_enemy_4_2([left + 250, top + 250], 'picture/enemy/snipe/mob_1.png', 20)
        ennemy.spawn_enemy_4_1([left + 200, top + 200], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 300, top + 200], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 200, top + 300], 'picture/enemy/mage/Mage.png', 20)
        ennemy.spawn_enemy_4_1([left + 300, top + 300], 'picture/enemy/mage/Mage.png', 20)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_boss_4(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 19  # Longueur x de la salle
    y = 13  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_4(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_2_4(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_boss_4([left + 450, top + 300], 200)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest


def room_boss_3(n, _door):
    # Liste qui vont recueillir des éléments pour l'affichage de la salle
    room = []
    door = []
    chest = {}

    tiles._chest = [False]  # Liste qui permet ou non la création de coffre

    x = 19  # Longueur x de la salle
    y = 13  # Longueur y de la salle

    # Associe les différentes parties de l'écran dans des variables pour faciliter la position des entitées quelque soit l'écran
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50

    # Donne la position initialie de
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    # Fonction qui créer les tuiles de la salle (murs, portes et potentiel coffre)
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y / 2) and i == x - 1:
                    if _door[0]:
                        room[i].append(tiles.blit_door_blue(i * 50 + left, j * 50 + top,
                                                            tiles.blit_wall_mid(i * 50 + left,
                                                                                j * 50 + top)))  # Porte 1
                    else:
                        room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))

                elif j == y - 1 and i == int(x / 2):
                    if _door[1]:
                        room[i].append(tiles.blit_door_blue_3(i * 50 + left, j * 50 + top,
                                                              tiles.blit_bottom_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 2
                    else:
                        room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))

                elif j == int(y / 2) and i == 0:
                    if _door[2]:
                        room[i].append(tiles.blit_door_blue_4(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_left_mid(i * 50 + left,
                                                                                       j * 50 + top)))  # Porte 3
                    else:
                        room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))

                elif j == 0 and i == int(x / 2):
                    if _door[3]:
                        room[i].append(tiles.blit_door_blue_2(i * 50 + left, j * 50 + top,
                                                              tiles.blit_wall_top_mid(i * 50 + left,
                                                                                      j * 50 + top)))  # Porte 4
                    else:
                        room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))

                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x - 1 and j == y - 1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y - 1:
                    room[i].append(tiles.blit_wall_top(i * 50 + left, j * 50 + top))

                elif i == 0:
                    room[i].append(tiles.blit_wall_left_mid(i * 50 + left, j * 50 + top))
                elif j == 0:
                    room[i].append(tiles.blit_wall_top_mid(i * 50 + left, j * 50 + top))
                elif j == y - 1:
                    room[i].append(tiles.blit_bottom_mid(i * 50 + left, j * 50 + top))
                elif i == x - 1:
                    room[i].append(tiles.blit_wall_mid(i * 50 + left, j * 50 + top))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_3(i * 50 + left, j * 50 + top))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_3_3(i * 50 + left, j * 50 + top))

        # Affiche les éléments de la salle
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        # Initie la position d'apparition du joueur
        player.pos = [510 + left, 240 + top]

        ennemy.spawn_boss_3([left + 450, top + 300], 150)

        # Affiche les portes des quatres cotés de l'écran en fonction des éléments de la variable _door
        if _door[0]:
            door.append(pygame.Rect((x - 1) * 50 + left, int(y / 2) * 50 + top, 50, 50))  # Porte 1
        else:
            door.append(pygame.Rect(0, 0, 0, 0))  # Porte 1

        if _door[1]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10, 50, 50))  # Porte 2
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[2]:
            door.append(pygame.Rect(left, int(y / 2) * 50 + top, 50, 50))  # Porte 3
        else:
            door.append(pygame.Rect(0, 0, 0, 0))
        if _door[3]:
            door.append(pygame.Rect(int(x / 2) * 50 + left, top, 50, 50))  # Porte 4
        else:
            door.append(pygame.Rect(0, 0, 0, 0))

    # La salle est crée
    create()

    # Fonction qui permet d'update la salle
    def update(list):
        for i in list:
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50) - 1]()
                room[int((i.left - left) / 50) - 1][int((i.top - top) / 50)]()
            except:
                pass
            try:
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top - top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top - top) / 50) + 1]()
            except:
                pass

    def modifie(x, y, tile):
        try:
            print((right-left)/50, "fuhoidsjdzsf")
            if x == 0 or x == int((right-left)/50)-1 or y == 0 or y == (bottom-top)/50 - 1:
                raise
            print(x, 'e')
            room[int(x)][int(y)] = tile(x*50 + left, y*50+top)
            graphic_main.update.append(room[int(x)][int(y)]())
        except:
            pass



    # Retourne les éléments suivant
    return create, update, door, top, bottom, left, right, pos_play[n], chest, modifie
