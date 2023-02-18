import pygame

enemy_1_list = []
def spawn_enemy(pos, img):
    img = pygame.image.load(img).convert_alpha()
    pos = pos
    global enemy_1_list
    enemy_1_list.append([img, pos])

