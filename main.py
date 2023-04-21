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
world.next_room(0)

# Variables qui regroupent les deux images d'écran d'acceuil et l'image de mort du personnage
accueil_1 = pygame.transform.scale(pygame.image.load('picture/ui/ecran_dacceuil_.png').convert_alpha(), [pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1]])
accueil_2 = pygame.transform.scale(pygame.image.load('picture/ui/ecran_dacceuil_2.png').convert_alpha(), [pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1]])
death_screen = pygame.transform.scale(pygame.image.load('picture/ui/Death_screen .png').convert_alpha(), [pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1]])

accueil = accueil_1 # Défini l'image d'acceuil entre les deux possibles

# boucle de fonctionnement qui permet le lancement du jeu
while True:
    if start:
        if start: # L'écran d'acceuil change à chaque instant 
            if accueil == accueil_1:
                accueil = accueil_2
            else:
                accueil = accueil_1
            graphic_main.screen.blit(accueil, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: # Quand un bouton est pressé, le gameplay commence et l'écran d'acceuil disparaît pour afficher le premier niveau 
                    start = False
                    graphic_main.screen.fill((0, 0, 0))
                    pygame.display.update()

                    world.create_floor(0) # Créer le premier niveau
                    world.show_next_room() # Montre la première la du niveau
                    pygame.display.update() # Update l'écran
                    break
            graphic_main.clock.tick(10) # Permet de gérer les fps


    elif player.dead: # Affiche l'écran de mort du personnage
        graphic_main.screen.blit(death_screen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # Si un bouton est pressé, le jeu repasse sur l'écran d'acceuil
                player.dead = False
                start = True
                break
        graphic_main.clock.tick(10)
    else:
        graphic_main.boucle()
