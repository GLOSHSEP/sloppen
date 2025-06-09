"""
Marley Ardrey
09/06/2025
Get David
Get David is a game where you play as a blob named Edwin with a task to get the diabolical square David
All instructions explained in game
Requires pygame install via
pip install pygame
pip3 install pygame
One font from https://www.1001freefonts.com/3d-fonts.php was used
Menu background from https://www.reddit.com/r/earthbound/comments/morrbn/i_made_a_funky_earthbound_battle_background/
"""

try: 
    import pygame 
except: 
    print("ERROR YOU NEED PYGAME INSTALLED") 
    exit(1)

import sloppen

game = sloppen.game_data("Game Collection", 60, (1280, 720))
game.initalize()
game.map.create_map_file("menu/menu.map")
game.map.create_map_file("level/level_1/level_1.map")
game.map.switch_map("menu")
game.game_loop()