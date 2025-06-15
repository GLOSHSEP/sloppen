"""
Marley Ardrey
13/06/2025
Get David
Get David is a game where you play as a blob named Edwin with a task to get the diabolical square David
All instructions explained in game
Requires pygame install via
pip install pygame
pip3 install pygame
One font from https://www.1001freefonts.com/3d-fonts.php was used
Menu background from https://www.reddit.com/r/earthbound/comments/morrbn/i_made_a_funky_earthbound_battle_background/
Level background from earthbound
Death sound from super mario world
Dash sound effect from ultrakill
Victory music from deltarune
All other music and sound effects are from undertale
"""

try: 
    import pygame 
except: 
    print("ERROR YOU NEED PYGAME INSTALLED") 
    exit(1)

import sloppen

game = sloppen.game_data("Get David", 60, (1280, 720))
game.initalize()
game.map.create_map_file("rooms/menu.map")
game.map.create_map_file("rooms/done.map")
game.map.create_map_file("rooms/level_1.map")
game.map.create_map_file("rooms/level_2.map")
game.map.switch_map("menu")
game.game_loop()