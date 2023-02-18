# importation
import graphic_main
import ennemy
# initialisation des modules
screen = graphic_main.initialisation()
frame = graphic_main.import_character_picture(6)
ennemy.spawn_enemy([50, 50], 'picture/character/player1.png')

# boucle de fonctionement
while True:
    graphic_main.boucle()
