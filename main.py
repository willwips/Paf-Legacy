# importation
import pygame.image

import graphic_main
import ennemy
import player
import room
import weapon
import tiles
import world

# initialisation des module
screen = graphic_main.initialisation(True)
tiles.load_tile()
frame = graphic_main.import_character_picture(6)
start = True

weapon.import_weapon()
#graphic_main.r, graphic_main.u, graphic_main.door, graphic_main.top, graphic_main.bottom, graphic_main.left, graphic_main.right = world.next_room()
#graphic_main.r()
world.next_room(0)

accueil_1 = pygame.transform.scale(pygame.image.load('picture/ui/ecran_dacceuil_.png').convert_alpha(), [pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1]])
accueil_2 = pygame.transform.scale(pygame.image.load('picture/ui/ecran_dacceuil_2.png').convert_alpha(), [pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1]])
death_screen = pygame.transform.scale(pygame.image.load('picture/ui/Death_screen .png').convert_alpha(), [pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1]])

accueil = accueil_1
# boucle de fonctionnement
while True:
    if start:
        if start:
            if accueil == accueil_1:
                accueil = accueil_2
            else:
                accueil = accueil_1
            graphic_main.screen.blit(accueil, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    start = False
                    graphic_main.screen.fill((0, 0, 0))
                    pygame.display.update()

                    world.create_floor(0)
                    world.show_next_room()
                    pygame.display.update()

                    break
            graphic_main.clock.tick(10)


    elif player.dead:
        graphic_main.screen.blit(death_screen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                player.dead = False
                start = True
                break
        graphic_main.clock.tick(10)
    else:
        graphic_main.boucle()
