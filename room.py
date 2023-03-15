import pygame

import ennemy
import player
import tiles
import graphic_main


def room_1():
    room = []
    door = []

    def create():
        for i in range(0, int(graphic_main.screen.get_size()[0] / 50) + 1):
            room.append([])
            for j in range(0, int(graphic_main.screen.get_size()[1] / 50) + 1):
                if (j == 3 and i == 11):
                    room[i].append(tiles.blit_door_black(i * 50, j * 50, tiles.blit_wall_mid(i*50, j*50)))
                elif (i==0 or i == 11):
                    room[i].append(tiles.blit_wall_mid(i * 50, j * 50))
                elif (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_1(i * 50, j * 50))
                elif j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_3_1(i * 50, j * 50))

        print(room)
        ennemy.spawn_enemy_1_2([50, 50], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 50)
        ennemy.spawn_enemy_1_2([250, 150], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 50)
        ennemy.spawn_enemy_2_1([123, 150], ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                            'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                            'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)
        ennemy.spawn_enemy_2_1([350, 350], ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
                                            'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
                                            'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)
        ennemy.spawn_enemy_1([21, 223], 'picture/character/player1.png', 50)
        ennemy.spawn_enemy_1([49, 27], 'picture/character/player1.png', 50)
        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())

        player.pos = [50, 500]
        door.append(pygame.Rect(550, 150, 50, 50))
        #graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (0, 0, 0), door[0]))

    create()

    def update(list):
        for i in list:
            try:
                room[int(i.left / 50)][int(i.top / 50)]()
                room[int(i.left / 50) + 1][int(i.top / 50)]()
                room[int(i.left / 50)][int(i.top / 50) + 1]()
                room[int(i.left / 50) + 1][int(i.top / 50) + 1]()
            except:
                pass

    return create, update, door
