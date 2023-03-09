import pygame

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
                if (j % 2 + i % 2) % 2 == 0:
                    room[i].append(tiles.blit_tile_3_1(i * 50, j * 50))
                if j % 2 + i % 2 == 1:
                    room[i].append(tiles.blit_tile_3_1(i * 50, j * 50))

        for i in room:
            for j in i:
                graphic_main.trash_update.append(j())
        player.pos = [50, 500]
        door.append(pygame.Rect(550, 140, 50, 120))
        graphic_main.update.append(pygame.draw.rect(graphic_main.screen, (0, 0, 0), door[0]))

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
