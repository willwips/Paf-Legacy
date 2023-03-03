# importation
import graphic_main
import ennemy
import room
import weapon
import tiles
# initialisation des modules
screen = graphic_main.initialisation()
tiles.load_tile()
frame = graphic_main.import_character_picture(6)
ennemy.spawn_enemy_2_1([50, 50], 'picture/enemy/foe/foe_L_1.png', 50)

for i in range(0, 600, 50):
    for j in range(0, 600, 50):
        ennemy.spawn_enemy_2_1([i, j], 'picture/enemy/foe/foe_L_1.png', 50)
weapon.import_weapon()
graphic_main.r, graphic_main.u = room.room_1()
graphic_main.r()
# boucle de fonctionnement
while True:
    graphic_main.boucle()

