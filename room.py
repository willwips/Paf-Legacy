import pygame

import ennemy
import player
import tiles
import graphic_main
import weapon

def heal(pv):
    a = pv

    def _heal():
        player.pv += a
    return _heal

def change_weapon(_weapon):
    def _change():
        weapon.current_weapon = _weapon
    return _change

def room_1_0(n):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]

    x = 20  # Longueur x de la salle
    y = 10  # Longueur y de la salle
    print(pygame.display.get_surface().get_size()[0] / 2, 12 * 50, 'e')
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
                    room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_mid(i * 50 + left, j * 50 + top)))  # Porte 1
                elif j == y - 1 and i == int(x / 2):
                    room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                           tiles.blit_bottom_mid(i * 50 + left,
                                                                                 j * 50 + top)))  # Porte 2
                elif j == int(y / 2) and i == 0:
                    room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_left_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 3
                elif j == 0 and i == int(x / 2):
                    room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_top_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 4
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

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
                
        print(top, left, 'ee')
        player.pos = [510 + left, 240 + top]
        print(player.pos)
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


def room_1_1(n):
    room = []
    door = []
    chest = {}
    tiles._chest = [False]
    x = 18  # Longueur x de la salle
    y = 7  # Longueur y de la salle
    print(pygame.display.get_surface().get_size()[0] / 2, 12 * 50, 'e')
    top = pygame.display.get_surface().get_size()[1] / 2 - y / 2 * 50
    bottom = pygame.display.get_surface().get_size()[1] / 2 + y / 2 * 50
    left = pygame.display.get_surface().get_size()[0] / 2 - x / 2 * 50
    right = pygame.display.get_surface().get_size()[0] / 2 + x / 2 * 50
    print(left, top, 'e')
    pos_play = [[(x - 1) * 50 + left - 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, y - 1 * 50 + bottom - 10 - 50], [left + 20, int(y / 2) * 50 + top],
                [int(x / 2) * 50 + left, top + 50]]

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == 5 and i == 3:
                    room[i].append(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                           tiles.blit_tile_2_1(i * 50 + left, j * 50 + top), 0)[0])
                    chest.update(tiles.blit_chest_yellow(i * 50 + left, j * 50 + top,
                                                         tiles.blit_tile_4_1(i * 50 + left, j * 50 + top), change_weapon('final_axe'))[1])
                elif j == int(y / 2) and i == x - 1:
                    room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_mid(i * 50 + left, j * 50 + top)))  # Porte 1
                elif j == y - 1 and i == int(x / 2):
                    room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                           tiles.blit_bottom_mid(i * 50 + left,
                                                                                 j * 50 + top)))  # Porte 2
                elif j == int(y / 2) and i == 0:
                    room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_left_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 3
                elif j == 0 and i == int(x / 2):
                    room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_top_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 4
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
        # ennely (voir main)
        ennemy.spawn_enemy_1_2([left + 80, top + 80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 250, top + 150], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1([left + 80, top + 223], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 210, top + 85], 'picture/character/player1.png', 50)

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        print(top, left, 'ee')
        player.pos = [50 + left, 220 + top]
        print(player.pos)
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


def room_1_2(n):
    room = []
    door = []
    chest = {}

    x = 9  # Longueur x de la salle
    y = 9  # Longueur y de la salle
    print(pygame.display.get_surface().get_size()[0] / 2, 12 * 50, 'e')
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
                    room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_mid(i * 50 + left, j * 50 + top)))  # Porte 1
                elif j == y - 1 and i == int(x / 2):
                    room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                           tiles.blit_bottom_mid(i * 50 + left,
                                                                                 j * 50 + top)))  # Porte 2
                elif j == int(y / 2) and i == 0:
                    room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_left_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 3
                elif j == 0 and i == int(x / 2):
                    room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_top_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 4
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

        ennemy.spawn_enemy_1([left + 80, top + 223], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 210, top + 85], 'picture/character/player1.png', 50)
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        print(top, left, 'ee')
        player.pos = [50 + left, 220 + top]
        print(player.pos)
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


def room_1_3(n):
    room = []
    door = []
    chest = {}

    x = 15  # Longueur x de la salle
    y = 8  # Longueur y de la salle
    print(pygame.display.get_surface().get_size()[0] / 2, 12 * 50, 'e')
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
                    room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_mid(i * 50 + left, j * 50 + top)))  # Porte 1
                elif j == y - 1 and i == int(x / 2):
                    room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                           tiles.blit_bottom_mid(i * 50 + left,
                                                                                 j * 50 + top)))  # Porte 2
                elif j == int(y / 2) and i == 0:
                    room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_left_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 3
                elif j == 0 and i == int(x / 2):
                    room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_top_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 4
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

        # ennely (voir main)
        ennemy.spawn_enemy_1_2([left + 80, top + 80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1_2([left + 250, top + 150], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'],
                               30)
        ennemy.spawn_enemy_1([left + 72, top + 123], 'picture/character/player1.png', 50)

        ennemy.spawn_enemy_1([left + 80, top + 223], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 210, top + 85], 'picture/character/player1.png', 50)
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        print(top, left, 'ee')
        player.pos = [50 + left, 220 + top]
        print(player.pos)
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

def room_1_4(n):
    room = []
    door = []
    chest = {}

    x = 27 # Longueur x de la salle
    y = 4  # Longueur y de la salle
    print(pygame.display.get_surface().get_size()[0]/2 , 12 * 50, 'e')
    top = pygame.display.get_surface().get_size()[1]/2 - y/2 * 50
    bottom = pygame.display.get_surface().get_size()[1]/2 + y/2 * 50
    left = pygame.display.get_surface().get_size()[0]/2 - x/2 * 50
    right = pygame.display.get_surface().get_size()[0]/2 + x/2 * 50
    pos_play = [[(x-1) * 50 + left - 20, int(y/2) * 50+ top], [int(x/2) * 50 + left , y - 1 * 50+ bottom - 10 - 50], [left + 20, int(y/2) * 50+ top], [int(x/2) * 50 + left,  top + 50]]
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0,0,0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y/2) and i == x - 1:
                    room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 1
                elif j == y - 1 and i == int(x/2):
                    room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top, tiles.blit_bottom_mid(i*50 + left, j*50 + top))) # Porte 2
                elif j == int(y/2) and i == 0:
                    room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top, tiles.blit_wall_left_mid(i*50 + left, j*50 + top))) # Porte 3
                elif j == 0 and i == int(x/2):
                    room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top, tiles.blit_wall_top_mid(i*50 + left, j*50 + top))) # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x-1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x-1 and j == y-1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y-1:
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
                    
        ennemy.spawn_enemy_1([left + 100, top + 75], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 150, top+75], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 200, top + 75], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 250, top +75], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 300, top +75], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 500, top + 100], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 500, top + 50], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 450, top + 100], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 450, top + 50], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 400, top + 100], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 400, top + 50], 'picture/character/player1.png', 50)

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        print(top, left, 'ee')
        player.pos = [50 + left, 220 + top]
        print(player.pos)
        door.append(pygame.Rect((x-1) * 50 + left , int(y/2) * 50+ top, 50, 50)) # Porte 1
        door.append(pygame.Rect(int(x/2) * 50 + left , y - 1 * 50+ bottom - 10, 50, 50)) # Porte 2
        door.append(pygame.Rect(left , int(y/2) * 50+ top, 50, 50)) # Porte 3
        door.append(pygame.Rect(int(x/2) * 50 + left,  top , 50, 50)) # Porte 4


    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left)/ 50)][int((i.top-top) / 50)-1]()
                room[int((i.left - left) / 50)-1][int((i.top-top) / 50)-1]()
                room[int((i.left - left) / 50)-1][int((i.top-top) / 50)]()
            except: pass
            try:
                room[int((i.left - left) / 50)][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top-top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top-top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest

def room_1_5(n):
    room = []
    door = []
    chest = {}

    x = 7 # Longueur x de la salle
    y = 7  # Longueur y de la salle
    print(pygame.display.get_surface().get_size()[0]/2 , 12 * 50, 'e')
    top = pygame.display.get_surface().get_size()[1]/2 - y/2 * 50
    bottom = pygame.display.get_surface().get_size()[1]/2 + y/2 * 50
    left = pygame.display.get_surface().get_size()[0]/2 - x/2 * 50
    right = pygame.display.get_surface().get_size()[0]/2 + x/2 * 50
    pos_play = [[(x-1) * 50 + left - 20, int(y/2) * 50+ top], [int(x/2) * 50 + left , y - 1 * 50+ bottom - 10 - 50], [left + 20, int(y/2) * 50+ top], [int(x/2) * 50 + left,  top + 50]]
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0,0,0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y/2) and i == x - 1:
                    room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 1
                elif j == y - 1 and i == int(x/2):
                    room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top, tiles.blit_bottom_mid(i*50 + left, j*50 + top))) # Porte 2
                elif j == int(y/2) and i == 0:
                    room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top, tiles.blit_wall_left_mid(i*50 + left, j*50 + top))) # Porte 3
                elif j == 0 and i == int(x/2):
                    room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top, tiles.blit_wall_top_mid(i*50 + left, j*50 + top))) # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x-1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x-1 and j == y-1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y-1:
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
        print(top, left, 'ee')
        player.pos = [50 + left, 220 + top]
        print(player.pos)
        door.append(pygame.Rect((x-1) * 50 + left , int(y/2) * 50+ top, 50, 50)) # Porte 1
        door.append(pygame.Rect(int(x/2) * 50 + left , y - 1 * 50+ bottom - 10, 50, 50)) # Porte 2
        door.append(pygame.Rect(left , int(y/2) * 50+ top, 50, 50)) # Porte 3
        door.append(pygame.Rect(int(x/2) * 50 + left,  top , 50, 50)) # Porte 4


    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left)/ 50)][int((i.top-top) / 50)-1]()
                room[int((i.left - left) / 50)-1][int((i.top-top) / 50)-1]()
                room[int((i.left - left) / 50)-1][int((i.top-top) / 50)]()
            except: pass
            try:
                room[int((i.left - left) / 50)][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top-top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top-top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest

def room_1_6(n):
    room = []
    door = []
    chest = {}

    x = 20 # Longueur x de la salle
    y = 15  # Longueur y de la salle
    print(pygame.display.get_surface().get_size()[0]/2 , 12 * 50, 'e')
    top = pygame.display.get_surface().get_size()[1]/2 - y/2 * 50
    bottom = pygame.display.get_surface().get_size()[1]/2 + y/2 * 50
    left = pygame.display.get_surface().get_size()[0]/2 - x/2 * 50
    right = pygame.display.get_surface().get_size()[0]/2 + x/2 * 50
    pos_play = [[(x-1) * 50 + left - 20, int(y/2) * 50+ top], [int(x/2) * 50 + left , y - 1 * 50+ bottom - 10 - 50], [left + 20, int(y/2) * 50+ top], [int(x/2) * 50 + left,  top + 50]]
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0,0,0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y/2) and i == x - 1:
                    room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 1
                elif j == y - 1 and i == int(x/2):
                    room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top, tiles.blit_bottom_mid(i*50 + left, j*50 + top))) # Porte 2
                elif j == int(y/2) and i == 0:
                    room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top, tiles.blit_wall_left_mid(i*50 + left, j*50 + top))) # Porte 3
                elif j == 0 and i == int(x/2):
                    room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top, tiles.blit_wall_top_mid(i*50 + left, j*50 + top))) # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x-1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x-1 and j == y-1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y-1:
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
                    
        ennemy.spawn_enemy_1_2([left + 80, top + 80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 120, top + 250], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 180, top + 180], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 300, top + 250], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 280, top + 280], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 250, top + 150], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 400, top + 400], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 550, top + 530], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 450, top + 580], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 500, top + 650], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 550, top + 280], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 600, top + 90], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)            
        ennemy.spawn_enemy_1_2([left + 650, top + 680], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 700, top + 250], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 750, top + 240], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 250, top + 50], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)  

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        print(top, left, 'ee')
        player.pos = [50 + left, 220 + top]
        print(player.pos)
        door.append(pygame.Rect((x-1) * 50 + left , int(y/2) * 50+ top, 50, 50)) # Porte 1
        door.append(pygame.Rect(int(x/2) * 50 + left , y - 1 * 50+ bottom - 10, 50, 50)) # Porte 2
        door.append(pygame.Rect(left , int(y/2) * 50+ top, 50, 50)) # Porte 3
        door.append(pygame.Rect(int(x/2) * 50 + left,  top , 50, 50)) # Porte 4


    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left)/ 50)][int((i.top-top) / 50)-1]()
                room[int((i.left - left) / 50)-1][int((i.top-top) / 50)-1]()
                room[int((i.left - left) / 50)-1][int((i.top-top) / 50)]()
            except: pass
            try:
                room[int((i.left - left) / 50)][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top-top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top-top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest

def room_1_7(n):
    room = []
    door = []
    chest = {}

    x = 12 # Longueur x de la salle
    y = 8  # Longueur y de la salle
    print(pygame.display.get_surface().get_size()[0]/2 , 12 * 50, 'e')
    top = pygame.display.get_surface().get_size()[1]/2 - y/2 * 50
    bottom = pygame.display.get_surface().get_size()[1]/2 + y/2 * 50
    left = pygame.display.get_surface().get_size()[0]/2 - x/2 * 50
    right = pygame.display.get_surface().get_size()[0]/2 + x/2 * 50
    pos_play = [[(x-1) * 50 + left - 20, int(y/2) * 50+ top], [int(x/2) * 50 + left , y - 1 * 50+ bottom - 10 - 50], [left + 20, int(y/2) * 50+ top], [int(x/2) * 50 + left,  top + 50]]
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0,0,0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y/2) and i == x - 1:
                    room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 1
                elif j == y - 1 and i == int(x/2):
                    room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top, tiles.blit_bottom_mid(i*50 + left, j*50 + top))) # Porte 2
                elif j == int(y/2) and i == 0:
                    room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top, tiles.blit_wall_left_mid(i*50 + left, j*50 + top))) # Porte 3
                elif j == 0 and i == int(x/2):
                    room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top, tiles.blit_wall_top_mid(i*50 + left, j*50 + top))) # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x-1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x-1 and j == y-1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y-1:
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
                    
        ennemy.spawn_enemy_1_2([left + 80, top + 80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 120, top + 250], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 180, top + 180], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1([left + 60, top + 100], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 60, top + 52], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 110, top + 52], 'picture/character/player1.png', 50)

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        print(top, left, 'ee')
        player.pos = [50 + left, 220 + top]
        print(player.pos)
        door.append(pygame.Rect((x-1) * 50 + left , int(y/2) * 50+ top, 50, 50)) # Porte 1
        door.append(pygame.Rect(int(x/2) * 50 + left , y - 1 * 50+ bottom - 10, 50, 50)) # Porte 2
        door.append(pygame.Rect(left , int(y/2) * 50+ top, 50, 50)) # Porte 3
        door.append(pygame.Rect(int(x/2) * 50 + left,  top , 50, 50)) # Porte 4


    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left)/ 50)][int((i.top-top) / 50)-1]()
                room[int((i.left - left) / 50)-1][int((i.top-top) / 50)-1]()
                room[int((i.left - left) / 50)-1][int((i.top-top) / 50)]()
            except: pass
            try:
                room[int((i.left - left) / 50)][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top-top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top-top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest

def room_1_8(n):
    room = []
    door = []
    chest = {}


    x = 15 # Longueur x de la salle
    y = 10  # Longueur y de la salle
    print(pygame.display.get_surface().get_size()[0]/2 , 12 * 50, 'e')
    top = pygame.display.get_surface().get_size()[1]/2 - y/2 * 50
    bottom = pygame.display.get_surface().get_size()[1]/2 + y/2 * 50
    left = pygame.display.get_surface().get_size()[0]/2 - x/2 * 50
    right = pygame.display.get_surface().get_size()[0]/2 + x/2 * 50
    pos_play = [[(x-1) * 50 + left - 20, int(y/2) * 50+ top], [int(x/2) * 50 + left , y - 1 * 50+ bottom - 10 - 50], [left + 20, int(y/2) * 50+ top], [int(x/2) * 50 + left,  top + 50]]
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0,0,0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y/2) and i == x - 1:
                    room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 1
                elif j == y - 1 and i == int(x/2):
                    room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top, tiles.blit_bottom_mid(i*50 + left, j*50 + top))) # Porte 2
                elif j == int(y/2) and i == 0:
                    room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top, tiles.blit_wall_left_mid(i*50 + left, j*50 + top))) # Porte 3
                elif j == 0 and i == int(x/2):
                    room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top, tiles.blit_wall_top_mid(i*50 + left, j*50 + top))) # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x-1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x-1 and j == y-1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y-1:
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

        ennemy.spawn_enemy_1([left + 60, top + 100], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 110, top + 52], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 650, top + 100], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 600, top + 52], 'picture/character/player1.png', 50)#
        ennemy.spawn_enemy_1([left + 60, top + 350], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 110, top + 400], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 650, top + 350], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 600, top + 400], 'picture/character/player1.png', 50)
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        print(top, left, 'ee')
        player.pos = [50 + left, 220 + top]
        print(player.pos)
        door.append(pygame.Rect((x-1) * 50 + left , int(y/2) * 50+ top, 50, 50)) # Porte 1
        door.append(pygame.Rect(int(x/2) * 50 + left , y - 1 * 50+ bottom - 10, 50, 50)) # Porte 2
        door.append(pygame.Rect(left , int(y/2) * 50+ top, 50, 50)) # Porte 3
        door.append(pygame.Rect(int(x/2) * 50 + left,  top , 50, 50)) # Porte 4


    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left)/ 50)][int((i.top-top) / 50)-1]()
                room[int((i.left - left) / 50)-1][int((i.top-top) / 50)-1]()
                room[int((i.left - left) / 50)-1][int((i.top-top) / 50)]()
            except: pass
            try:
                room[int((i.left - left) / 50)][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top-top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top-top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n], chest

def room_1_9(n):
    room = []
    door = []
    x = 9 # Longueur x de la salle
    y = 14 # Longueur y de la salle
    print(pygame.display.get_surface().get_size()[0]/2 , 12 * 50, 'e')
    top = pygame.display.get_surface().get_size()[1]/2 - y/2 * 50
    bottom = pygame.display.get_surface().get_size()[1]/2 + y/2 * 50
    left = pygame.display.get_surface().get_size()[0]/2 - x/2 * 50
    right = pygame.display.get_surface().get_size()[0]/2 + x/2 * 50
    pos_play = [[(x-1) * 50 + left - 20, int(y/2) * 50+ top], [int(x/2) * 50 + left , y - 1 * 50+ bottom - 10 - 50], [left + 20, int(y/2) * 50+ top], [int(x/2) * 50 + left,  top + 50]]
    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0,0,0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y/2) and i == x - 1:
                    room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 1
                elif j == y - 1 and i == int(x/2):
                    room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top, tiles.blit_bottom_mid(i*50 + left, j*50 + top))) # Porte 2
                elif j == int(y/2) and i == 0:
                    room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top, tiles.blit_wall_left_mid(i*50 + left, j*50 + top))) # Porte 3
                elif j == 0 and i == int(x/2):
                    room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top, tiles.blit_wall_top_mid(i*50 + left, j*50 + top))) # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                elif i == x-1 and j == 0:
                    room[i].append(tiles.blit_wall_bottom(i * 50 + left, j * 50 + top))
                elif i == x-1 and j == y-1:
                    room[i].append(tiles.blit_wall_right(i * 50 + left, j * 50 + top))
                elif i == 0 and j == y-1:
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
        ennemy.spawn_enemy_1([left + 360, top + 50], 'picture/character/player1.png', 50)  
        ennemy.spawn_enemy_1([left + 60, top + 50], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1_2([left + 120, top + 250], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1_2([left + 180, top + 180], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        ennemy.spawn_enemy_1([left + 60, top + 600], 'picture/character/player1.png', 50)   
        ennemy.spawn_enemy_1([left + 360, top + 600], 'picture/character/player1.png', 50)     
       
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        print(top, left, 'ee')
        player.pos = [50 + left, 220 + top]
        print(player.pos)
        door.append(pygame.Rect((x-1) * 50 + left , int(y/2) * 50+ top, 50, 50)) # Porte 1
        door.append(pygame.Rect(int(x/2) * 50 + left , y - 1 * 50+ bottom - 10, 50, 50)) # Porte 2
        door.append(pygame.Rect(left , int(y/2) * 50+ top, 50, 50)) # Porte 3
        door.append(pygame.Rect(int(x/2) * 50 + left,  top , 50, 50)) # Porte 4


    create()

    def update(list):
        for i in list:
            try:
                room[int((i.left - left)/ 50)][int((i.top-top) / 50)-1]()
                room[int((i.left - left) / 50)-1][int((i.top-top) / 50)-1]()
                room[int((i.left - left) / 50)-1][int((i.top-top) / 50)]()
            except: pass
            try:
                room[int((i.left - left) / 50)][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50) + 1][int((i.top-top) / 50)]()
                room[int((i.left - left) / 50)][int((i.top-top) / 50) + 1]()
                room[int((i.left - left) / 50) + 1][int((i.top-top) / 50) + 1]()
            except:
                pass

    return create, update, door, top, bottom, left, right, pos_play[n]

def room_boss_1(n):
    room = []
    door = []
    chest = {}

    x = 12  # Longueur x de la salle
    y = 12  # Longueur y de la salle
    print(pygame.display.get_surface().get_size()[0] / 2, 12 * 50, 'e')
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
                    room[i].append(tiles.blit_door_black_1(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_mid(i * 50 + left, j * 50 + top)))  # Porte 1
                elif j == y - 1 and i == int(x / 2):
                    room[i].append(tiles.blit_door_black_3(i * 50 + left, j * 50 + top,
                                                           tiles.blit_bottom_mid(i * 50 + left,
                                                                                 j * 50 + top)))  # Porte 2
                elif j == int(y / 2) and i == 0:
                    room[i].append(tiles.blit_door_black_4(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_left_mid(i * 50 + left,
                                                                                    j * 50 + top)))  # Porte 3
                elif j == 0 and i == int(x / 2):
                    room[i].append(tiles.blit_door_black_2(i * 50 + left, j * 50 + top,
                                                           tiles.blit_wall_top_mid(i * 50 + left,
                                                                                   j * 50 + top)))  # Porte 4
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
        # ennely (voir main)
        # ennemy.spawn_enemy_1_2([left + 80, top +80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        # ennemy.spawn_enemy_1_2([left + 250, top + 150], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 30)
        # ennemy.spawn_enemy_1([left + 80, top+223], 'picture/character/player1.png', 50)
        # ennemy.spawn_enemy_1([left + 210, top + 85], 'picture/character/player1.png', 50)
        
        # Permet de modifier le point d'apparition en fonction de la porte emprunté
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
                
        print(top, left, 'ee')
        player.pos = [50 + left, 220 + top]
        print(player.pos)
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
