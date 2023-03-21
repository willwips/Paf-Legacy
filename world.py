import room
import graphic_main
import random

floor = []
coo = [0, 0]


def create_floor(level):
    global floor
    if level == 0:
        liste_level = [room.room_1_1, room.room_1_2, room.room_1_3]
    for i in range(10):
        floor.append([])
        for j in range(0, 10):
            floor[i].append(random.choice(liste_level))

create_floor(0)
def next_room():
    graphic_main.r, graphic_main.u, graphic_main.door, graphic_main.top, graphic_main.bottom, graphic_main.left, graphic_main.right =floor[coo[0]][coo[1]]()
