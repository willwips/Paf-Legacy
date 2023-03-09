# importation
import graphic_main
import ennemy
import room
import weapon
import tiles
# initialisation des module
screen = graphic_main.initialisation()
tiles.load_tile()
frame = graphic_main.import_character_picture(6)
"""
ennemy.spawn_enemy_1_2([50, 50], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 50)
ennemy.spawn_enemy_1_2([250, 150], ['picture/enemy/bat/Bat_1.png', 'picture/enemy/bat/Bat_2.png'], 50)
ennemy.spawn_enemy_2_1([123, 150], ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png', 'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png', 'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)
ennemy.spawn_enemy_2_1([350, 350], ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png', 'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png', 'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)
ennemy.spawn_enemy_1([21, 223], 'picture/character/player1.png', 50)
ennemy.spawn_enemy_1([49, 27], 'picture/character/player1.png', 50)

"""
#for i in range(1, 10):
#    for j in range(1, 10):
#        ennemy.spawn_enemy_2_1([i*50, j*50], ['picture/enemy/foe/foe_L_1.png', 'picture/enemy/foe/foe_L_2.png',
#                                            'picture/enemy/foe/foe_L_3.png', 'picture/enemy/foe/foe_R_1.png',
#                                            'picture/enemy/foe/foe_R_2.png', 'picture/enemy/foe/foe_R_3.png'], 50)

weapon.import_weapon()
graphic_main.r, graphic_main.u, graphic_main.door = room.room_1()
graphic_main.r()
# boucle de fonctionnement
while True:
    graphic_main.boucle()

