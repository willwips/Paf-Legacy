import pygame
import graphic_main

Tile_1 = []
Tile_2 = []
Tile_3 = []
Tile_4 = []
Tile_5 = []
door = []
wall = []
_chest = [False for i in range(0, 10)]
chest = []



def load_tile():
    global Tile_1
    global Tile_2
    global Tile_3
    global Tile_4
    global Tile_5
    global door
    global wall

    for i in range(1, 7):
        Tile_1.append(
            pygame.transform.scale(pygame.image.load('picture/tiles/Tile_1-' + str(i) + '.png').convert_alpha(),
                                   [50, 50]))
    
    for i in range(1, 7):
        Tile_2.append(pygame.transform.scale(pygame.image.load('picture/tiles/Tile_2-' + str(i) + '.png').convert_alpha(), [50, 50]))
    
    for i in range(1, 7):
        Tile_3.append(pygame.transform.scale(pygame.image.load('picture/tiles/Tile_3-' + str(i) + '.png').convert_alpha(), [50, 50]))

    for i in range(1, 7):
        #Tile_4.append(pygame.image.load('picture/tiles/Tile_4-' + str(i) + '.png').convert_alpha()) ce que tu as mit
        Tile_4.append(pygame.transform.scale(pygame.image.load('picture/tiles/Tile_4-' + str(i) + '.png').convert_alpha(), [50, 50]))
    

    door.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Door-Black.png').convert_alpha(), [55, 55]), -90))
    door.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Door-Black.png').convert_alpha(), [55, 55]), 0))
    door.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Door-Black.png').convert_alpha(), [55, 55]), 180))
    door.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Door-Black.png').convert_alpha(), [55, 55]), 90))
    
    door.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Door-Blue.png').convert_alpha(), [55, 55]), -90))
    door.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Door-Blue.png').convert_alpha(), [55, 55]), 0))
    door.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Door-Blue.png').convert_alpha(), [55, 55]), 180))
    door.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Door-Blue.png').convert_alpha(), [55, 55]), 90))
    
    door.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Door-Purple.png').convert_alpha(), [55, 55]), -90))
    door.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Door-Purple.png').convert_alpha(), [55, 55]), 0))
    door.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Door-Purple.png').convert_alpha(), [55, 55]), 180))
    door.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Door-Purple.png').convert_alpha(), [55, 55]), 90))

    door.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Door-Red.png').convert_alpha(), [55, 55]), -90))
    door.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Door-Red.png').convert_alpha(), [55, 55]), 0))
    door.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Door-Red.png').convert_alpha(), [55, 55]), 180))
    door.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Door-Red.png').convert_alpha(), [55, 55]), 90))

    door.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Door-White.png').convert_alpha(), [55, 55]), -90))
    door.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Door-White.png').convert_alpha(), [55, 55]), 0))
    door.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Door-White.png').convert_alpha(), [55, 55]), 180))
    door.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Door-White.png').convert_alpha(), [55, 55]), 90))
    

    wall.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Wall-Center-Square.png').convert_alpha(), [55, 55]), -90))
    wall.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Wall-Center-Square.png').convert_alpha(), [55, 55]), 0))
    wall.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Wall-Center-Square.png').convert_alpha(), [55, 55]), 90))
    wall.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Wall-Center-Square.png').convert_alpha(), [55, 55]), 180))
    wall.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Wall-Corner-Square.png').convert_alpha(), [55, 55]), 0))
    wall.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Wall-Corner-Square.png').convert_alpha(), [55, 55]), 90))
    wall.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Wall-Corner-Square.png').convert_alpha(), [55, 55]), 180))
    wall.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('picture/tiles/Wall-Corner-Square.png').convert_alpha(), [55, 55]), -90))


    chest.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Chest-Black-Closed.png').convert_alpha(), [29, 29]),
        -90))
    chest.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Chest-Black-Opened.png').convert_alpha(), [29, 29]),
        -90))

    chest.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Chest-Purple-Closed.png').convert_alpha(), [29, 29]),
        -90))
    chest.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Chest-Purple-Opened.png').convert_alpha(), [29, 29]),
        -90))
    
    chest.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Chest-Red-Closed.png').convert_alpha(), [29, 29]),
        -90))
    chest.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Chest-Red-Opened.png').convert_alpha(), [29, 29]),
        -90))

    chest.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Chest-Blue-Closed.png').convert_alpha(), [29, 29]),
        -90))
    chest.append(pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load('picture/tiles/Chest-Blue-Opened.png').convert_alpha(), [29, 29]),
        -90))
    
    print(door)

    #for i in range(1, 7):
   #     Tile_5.append(pygame.transform.scale(pygame.image.load('picture/tiles/Tile_5-' + str(i) + '.png').convert_alpha(), [50, 50]))
        
def blit_tile_1_1(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_1[0], [x, y])
        return a

    return blit_tile


def blit_tile_1_2(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_1[1], [x, y])
        return a

    return blit_tile


def blit_tile_1_3(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_1[2], [x, y])
        return a

    return blit_tile


def blit_tile_1_4(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_1[3], [x, y])
        return a

    return blit_tile


def blit_tile_1_5(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_1[4], [x, y])
        return a

    return blit_tile

def blit_tile_1_6(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_1[5], [x, y])
        return a

    return blit_tile

def blit_tile_2_1(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_2[0], [x, y])
        return a

    return blit_tile

def blit_tile_2_2(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_2[1], [x, y])
        return a

    return blit_tile

def blit_tile_2_3(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_2[2], [x, y])
        return a

    return blit_tile


def blit_tile_2_4(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_2[3], [x, y])
        return a

    return blit_tile

def blit_tile_2_5(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_2[4], [x, y])
        return a

    return blit_tile


def blit_tile_2_6(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_2[5], [x, y])
        return a

    return blit_tile



def blit_tile_3_1(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_3[0], [x, y])
        return a

    return blit_tile

def blit_tile_3_2(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_3[1], [x, y])
        return a

    return blit_tile

def blit_tile_3_3(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_3[2], [x, y])
        return a

    return blit_tile

def blit_tile_3_4(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_3[3], [x, y])
        return a

    return blit_tile

def blit_tile_3_5(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_3[4], [x, y])
        return a

    return blit_tile

def blit_tile_3_6(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_3[5], [x, y])
        return a

    return blit_tile

def blit_tile_4_1(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_4[0], [x, y])
        return a

    return blit_tile

def blit_tile_4_2(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_4[1], [x, y])
        return a

    return blit_tile

def blit_tile_4_3(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_4[2], [x, y])
        return a

    return blit_tile

def blit_tile_4_4(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_4[3], [x, y])
        return a

    return blit_tile

def blit_tile_4_5(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_4[4], [x, y])
        return a

    return blit_tile

def blit_tile_4_6(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_4[5], [x, y])
        return a

    return blit_tile

def blit_tile_5_1(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_5[0], [x, y])
        return a

    return blit_tile

def blit_tile_5_2(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_5[1], [x, y])
        return a

    return blit_tile

def blit_tile_5_3(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_5[2], [x, y])
        return a

    return blit_tile

def blit_tile_5_4(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_5[3], [x, y])
        return a

    return blit_tile

def blit_tile_5_5(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_5[4], [x, y])
        return a

    return blit_tile

def blit_tile_5_6(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(Tile_5[5], [x, y])
        return a

    return blit_tile

def blit_wall_mid(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(wall[0], [x, y])
        return a

    return blit_tile

def blit_wall_top_mid(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(wall[1], [x, y])
        return a

    return blit_tile

def blit_wall_left_mid(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(wall[2], [x, y])
        return a

    return blit_tile

def blit_bottom_mid(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(wall[3], [x, y])
        return a

    return blit_tile


def blit_wall_left(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(wall[4], [x, y])
        return a
    return blit_tile



def blit_door_black(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[0], [x, y])
        return a

    return blit_tile

def blit_door_black_2(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[1], [x, y])
        return a

    return blit_tile

def blit_door_black_3(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[2], [x, y])
        return a

    return blit_tile

def blit_door_black_4(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[3], [x, y])
        return a

    return blit_tile


def blit_door_blue(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[4], [x, y])
        return a

    return blit_tile

def blit_door_blue_2(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[5], [x, y])
        return a

    return blit_tile

def blit_door_blue_3(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[6], [x, y])
        return a

    return blit_tile

def blit_door_blue_4(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[7], [x, y])
        return a

    return blit_tile


def blit_door_purple(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[8], [x, y])
        return a

    return blit_tile

def blit_door_purple_2(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[9], [x, y])
        return a

    return blit_tile

def blit_door_purple_3(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[10], [x, y])
        return a

    return blit_tile

def blit_door_purple_4(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[11], [x, y])
        return a

    return blit_tile

def blit_door_red(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[12], [x, y])
        return a

    return blit_tile

def blit_door_red_2(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[13], [x, y])
        return a

    return blit_tile
def blit_door_red_3(x, y, tile):

    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[14], [x, y])
        return a

    return blit_tile

def blit_door_red_4(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[15], [x, y])
        return a

    return blit_tile

def blit_door_white(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[16], [x, y])
        return a

    return blit_tile

def blit_door_white_2(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[17], [x, y])
        return a

    return blit_tile
def blit_door_white_3(x, y, tile):
    
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[18], [x, y])
        return a

    return blit_tile

def blit_door_white_4(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[19], [x, y])
        return a

    return blit_tile

def blit_wall_top(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(wall[5], [x, y])
        return a
    return blit_tile

def blit_wall_right(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(wall[6], [x, y])
        return a
    return blit_tile

def blit_wall_bottom(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(wall[7], [x, y])
        return a
    return blit_tile
def blit_door_black_1(x, y, tile):

    pass
def blit_wall_top(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(wall[5], [x, y])
        return a
    return blit_tile
#a
def blit_wall_right(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(wall[6], [x, y])
        return a
    return blit_tile

def blit_wall_bottom(x, y):
    def blit_tile():
        a = graphic_main.screen.blit(wall[7], [x, y])
        return a
    return blit_tile
def blit_door_black_1(x, y, tile):

    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[0], [x, y])
        return a

    return blit_tile

def blit_door_black_2(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[1], [x, y])
        return a

    return blit_tile
def blit_door_black_3(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[2], [x, y])
        return a

    return blit_tile

def blit_door_black_4(x, y, tile):
    def blit_tile():
        a = tile()
        graphic_main.screen.blit(door[3], [x, y])
        return a

    return blit_tile

def blit_chest_black(x, y, tile, _loot, rot=-90, nbr = 0):
    rect = tile()
    def blit_tile():
        a = tile()
        if _chest[nbr]:
            graphic_main.screen.blit(pygame.transform.rotate(chest[1], rot), [x + 10, y + 10])
        else:
            graphic_main.screen.blit(pygame.transform.rotate(chest[0], rot), [x + 10, y + 10])
        return a
    a = {}
    a[_loot] = rect
    return blit_tile, a

def blit_chest_purple(x, y, tile, _loot, rot=-90, nbr = 0):
    rect = tile()
    def blit_tile():
        a = tile()
        if _chest[nbr]:
            graphic_main.screen.blit(pygame.transform.rotate(chest[3], rot), [x + 10, y + 10])
        else:
            graphic_main.screen.blit(pygame.transform.rotate(chest[2], rot), [x + 10, y + 10])
        return a
    a = {}
    a[_loot] = rect
    return blit_tile, a

def blit_chest_red(x, y, tile, _loot, rot=-90, nbr = 0):
    rect = tile()
    def blit_tile():
        a = tile()
        if _chest[nbr]:
            graphic_main.screen.blit(pygame.transform.rotate(chest[5], rot), [x + 10, y + 10])
        else:
            graphic_main.screen.blit(pygame.transform.rotate(chest[4], rot), [x + 10, y + 10])
        return a
    a = {}
    a[_loot] = rect
    return blit_tile, a

def blit_chest_blue(x, y, tile, _loot, rot=-90, nbr = 0):
    rect = tile()
    def blit_tile():
        a = tile()
        if _chest[nbr]:
            graphic_main.screen.blit(pygame.transform.rotate(chest[7], rot), [x + 10, y + 10])
        else:
            graphic_main.screen.blit(pygame.transform.rotate(chest[6], rot), [x + 10, y + 10])
        return a
    a = {}
    a[_loot] = rect
    return blit_tile, a