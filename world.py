import room
import graphic_main
import random
import player

floor = []
coo = [0, 0]
level = 0
pos_p = None
def create_floor(_level):
    global floor
    _level = 0
    if _level == 0:
        first_room = room.room_1_0
        liste_level = [room.room_1_1, room.room_1_2, room.room_1_3, room.room_1_4, room.room_1_5, room.room_1_6, room.room_1_7, room.room_1_8, room.room_1_9, room.room_1_10, room.room_1_11, room.room_1_12]
        boss_room = room.room_boss_1
        pos_boss = [9,random.randint(0, 9)]
    if _level == 4:
        first_room = room.room_4_0
        liste_level = [room.room_4_1, room.room_4_2, room.room_4_3, room.room_4_5]
        boss_room = room.room_boss_1
        pos_boss = [9, random.randint(0, 9)]
    for i in range(10):
        floor.append([])    
        for j in range(0, 10):
            if j == 0 and i == 0:
                floor[i].append(first_room)
            elif i == pos_boss[0] and j == pos_boss[1]:
                floor[i].append(boss_room)
            else:
                floor[i].append(random.choice(liste_level))
    print(floor)

def next_level():
    global level
    global coo
    graphic_main.timer = 60
    next_room(0, 120)
    coo = [0, 0]
    #level += 1
    create_floor(level)
create_floor(0)
def next_room(n, time = 20):
    global pos_p
    pos_p = n
    graphic_main.timer = time
    player.timer = 120
def show_next_room():
    graphic_main.r, graphic_main.u, graphic_main.door, graphic_main.top, graphic_main.bottom, graphic_main.left, graphic_main.right, player.pos, graphic_main.chest = floor[coo[0]%10][coo[1]%10](pos_p, [not coo[0] ==9, not coo[1] == 9, not coo[0]==0, not coo[1] == 0])
