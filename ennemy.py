import pygame

enemy_1_list = []
def spawn_enemy(pos, img, pv):
    img = pygame.image.load(img).convert_alpha()
    pos = pos
    global enemy_1_list
    enemy_1_list.append([img, pos, pv, 10])

def boucle():
    global enemy_1_list
    n = 0
    for i in enemy_1_list:
        if i[3] > 0:
            enemy_1_list[n][3] -= 1
        n+=1

def collision_with_weapon(a, strenght):
    n = 0
    for i in enemy_1_list:

        collision = False
        rectB = i[0].get_rect(center=i[1])
        rectB.h = 40
        rectB.w = 15
        rectB.center = (i[1][0]+15, i[1][1]+25)
        collision = rectB.colliderect(a)
        if collision and i[3] <= 0:
            enemy_1_list[n][2] -= strenght
            enemy_1_list[n][3] = 60
            print(enemy_1_list[n][2])
            if enemy_1_list[n][2] <= 0:
                del enemy_1_list[n]

        n += 1



