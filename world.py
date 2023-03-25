import room
import graphic_main
import random
import player

floor = []
coo = [0, 0]
#random.seed(25)
def create_floor(level):
    global floor
    if level == 0:
        first_room = room.room_1_0
        liste_level = [room.room_boss_1, room.room_1_1, room.room_1_2, room.room_1_3, room.room_1_4, room.room_1_5, room.room_1_6, room.room_1_7, room.room_1_8]
    for i in range(10):
        floor.append([])
        for j in range(0, 10):
            if j == 0 and i == 0:
                floor[i].append(first_room)
            floor[i].append(random.choice(liste_level))

create_floor(0)
def next_room(n):
    graphic_main.r, graphic_main.u, graphic_main.door, graphic_main.top, graphic_main.bottom, graphic_main.left, graphic_main.right, player.pos, graphic_main.chest=floor[coo[0]][coo[1]](n)
