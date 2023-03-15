import room
import graphic_main

floor = []
coo = [0, 0]


def create_floor(level):
    global floor
    for i in range(10):
        floor.append([])
        for j in range(0, 10):
            floor[i].append(room.room_1)

create_floor(0)
def next_room():
    graphic_main.r, graphic_main.u, graphic_main.door =floor[coo[0]][coo[1]]()
