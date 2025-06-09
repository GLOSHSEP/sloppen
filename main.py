"""
Marley Ardrey
16/05/2025
Game menu
This program contains a rock paper scissors high low guessing and tic tac toe game implemented using pygame built on top of my home grown pygame engine "sloppen"
you must have pygame installed to run this game
pip install pygame
pip3 install pygame
1 font from https://www.1001freefonts.com/3d-fonts.php was used
High low guessing game background taken from earthbound
"""

try: 
    import pygame 
except: 
    print("ERROR YOU NEED PYGAME INSTALLED") 
    exit(1)

import sloppen

game = sloppen.game_data("Game Collection", 60, (1280, 720))
game.initalize()
game.map.create_map_file("level/level_1/level_1.map")
game.map.switch_map("level_1")
game.game_loop()