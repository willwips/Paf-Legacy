# importation
import graphic_main
import ennemy
import weapon
# initialisation des modules
screen = graphic_main.initialisation()
frame = graphic_main.import_character_picture(6)
ennemy.spawn_enemy([50, 50], 'picture/character/player1.png', 50)

for i in range(0, 600, 50):
    for j in range(0, 600, 50):
        ennemy.spawn_enemy([i, j], 'picture/character/player1.png', 50)

weapon.import_weapon()

# boucle de fonctionement
while True:
    graphic_main.boucle()

