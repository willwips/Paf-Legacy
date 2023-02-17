import pygame

screen = None


def initialisation(full_screen=False):
    pygame.init()
    global screen
    if full_screen:
        screen = pygame.display.set_mode((300, 200), flags=pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((300, 200), flags=pygame.FULLSCREEN)

    return screen