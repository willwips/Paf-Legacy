# importation
import graphic_main
import ennemy
import room
import weapon
import tiles
import world

# initialisation des module
screen = graphic_main.initialisation(True)
tiles.load_tile()
frame = graphic_main.import_character_picture(6)

weapon.import_weapon()
#graphic_main.r, graphic_main.u, graphic_main.door, graphic_main.top, graphic_main.bottom, graphic_main.left, graphic_main.right = world.next_room()
world.next_room(0)
#graphic_main.r()
# boucle de fonctionnement
while True:
    graphic_main.boucle()
