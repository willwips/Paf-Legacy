import pygame

import ennemy
import player
import tiles
import graphic_main


def room_1_1():
    room = []
    door = []
    x = 18 # Longueur x de la salle
    y = 7  # Longueur y de la salle
    print(pygame.display.get_surface().get_size()[0]/2 , 12 * 50, 'e')
    top = pygame.display.get_surface().get_size()[1]/2 - y/2 * 50
    bottom = pygame.display.get_surface().get_size()[1]/2 + y/2 * 50
    left = pygame.display.get_surface().get_size()[0]/2 - x/2 * 50
    right = pygame.display.get_surface().get_size()[0]/2 + x/2 * 50

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y/2) and i == x - 1:
                    room[i].append(tiles.blit_door_black(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 1
                elif j == y - 1 and i == int(x/2):
                    room[i].append(tiles.blit_door_black(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 2
                elif j == int(y/2) and i == 0:
                    room[i].append(tiles.blit_door_black(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 3
                elif j == 0 and i == int(x/2):
                    room[i].append(tiles.blit_door_black(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                    print('r')

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
        #ennely (voir main)
        ennemy.spawn_enemy_1_2([left + 80, top +80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 10)
        ennemy.spawn_enemy_1_2([left + 250, top + 150], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 10)
        ennemy.spawn_enemy_1([left + 80, top+223], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 210, top + 85], 'picture/character/player1.png', 50)

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

        graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (255, 255, 255), door[1]))

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

    return create, update, door, top, bottom, left, right



def room_1_2():
    room = []
    door = []
    x = 9 # Longueur x de la salle
    y = 9  # Longueur y de la salle
    print(pygame.display.get_surface().get_size()[0]/2 , 12 * 50, 'e')
    top = pygame.display.get_surface().get_size()[1]/2 - y/2 * 50
    bottom = pygame.display.get_surface().get_size()[1]/2 + y/2 * 50
    left = pygame.display.get_surface().get_size()[0]/2 - x/2 * 50
    right = pygame.display.get_surface().get_size()[0]/2 + x/2 * 50

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y/2) and i == x - 1:
                    room[i].append(tiles.blit_door_black(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 1
                elif j == y - 1 and i == int(x/2):
                    room[i].append(tiles.blit_door_black(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 2
                elif j == int(y/2) and i == 0:
                    room[i].append(tiles.blit_door_black(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 3
                elif j == 0 and i == int(x/2):
                    room[i].append(tiles.blit_door_black(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                    print('r')

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

        #ennely (voir main)
        ennemy.spawn_enemy_1_2([left + 80, top +80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 10)
        ennemy.spawn_enemy_1_2([left + 250, top + 150], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 10)

        ennemy.spawn_enemy_1([left + 80, top+223], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 210, top + 85], 'picture/character/player1.png', 50)
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        print(top, left, 'ee')
        player.pos = [50 + left, 220 + top]
        print(player.pos)
        door.append(pygame.Rect((x-1) * 50 + left , int(y/2) * 50+ top, 50, 50)) # Porte 1
        door.append(pygame.Rect(int(x/2) * 50 + left , y - 1 * 50+ bottom - 10, 50, 50)) # Porte 2
        door.append(pygame.Rect(left , int(y/2) * 50+ top, 50, 50)) # Porte 3
        door.append(pygame.Rect(int(x/2) * 50 + left,  top, 50, 50)) # Porte 4
        graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (255, 255, 255), door[1]))


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

    return create, update, door, top, bottom, left, right


def room_1_3():
    room = []
    door = []
    x = 15 # Longueur x de la salle
    y = 8  # Longueur y de la salle
    print(pygame.display.get_surface().get_size()[0]/2 , 12 * 50, 'e')
    top = pygame.display.get_surface().get_size()[1]/2 - y/2 * 50
    bottom = pygame.display.get_surface().get_size()[1]/2 + y/2 * 50
    left = pygame.display.get_surface().get_size()[0]/2 - x/2 * 50
    right = pygame.display.get_surface().get_size()[0]/2 + x/2 * 50

    def create():
        graphic_main.trash_update.append(graphic_main.screen.fill((0, 0, 0)))
        for i in range(0, x):
            room.append([])
            for j in range(0, y):
                if j == int(y/2) and i == x - 1:
                    room[i].append(tiles.blit_door_black(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 1
                elif j == y - 1 and i == int(x/2):
                    room[i].append(tiles.blit_door_black(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 2
                elif j == int(y/2) and i == 0:
                    room[i].append(tiles.blit_door_black(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 3
                elif j == 0 and i == int(x/2):
                    room[i].append(tiles.blit_door_black(i * 50 + left, j * 50 + top, tiles.blit_wall_mid(i*50 + left, j*50 + top))) # Porte 4
                elif i == 0 and j == 0:
                    room[i].append(tiles.blit_wall_left(i * 50 + left, j * 50 + top))
                    print('r')

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

        #ennely (voir main)
        ennemy.spawn_enemy_1_2([left + 80, top +80], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 10)
        ennemy.spawn_enemy_1_2([left + 250, top + 150], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 10)
        ennemy.spawn_enemy_1([left + 27, top+45], 'picture/character/player1.png', 50)

        ennemy.spawn_enemy_1([left + 80, top+223], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([left + 210, top + 85], 'picture/character/player1.png', 50)
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        print(top, left, 'ee')
        player.pos = [50 + left, 220 + top]
        print(player.pos)
        door.append(pygame.Rect((x-1) * 50 + left , int(y/2) * 50+ top, 50, 50)) # Porte 1
        door.append(pygame.Rect(int(x/2) * 50 + left , y - 1 * 50+ bottom - 10, 50, 50)) # Porte 2
        door.append(pygame.Rect(left , int(y/2) * 50+ top, 50, 50)) # Porte 3
        door.append(pygame.Rect(int(x/2) * 50 + left,  top, 50, 50)) # Porte 4
        graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (255, 255, 255), door[1]))


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

    return create, update, door, top, bottom, left, right