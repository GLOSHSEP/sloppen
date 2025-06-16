"""
Marley Ardrey
16/06/2025
Get David
Get David is a game where you play as a blob named Edwin with a task to get the diabolical square David
All instructions also explained in game
Left and right to move
Left shift + left or right to dash
Z to shoot
Up to jump
Left and right against a wall + up to wall jump
You have 3 walls jumps initially
You have 3 gearts loose them all and you die
Touch david to win
Shoot enemies they have 3 health
Touch powerups to run faster or get 6 walls jumps or shoot faster
Going off the level will make you die
Requires pygame install via
pip install pygame
pip3 install pygame
Front from https://www.dafont.com/pixellari.font
Menu background from https://www.reddit.com/r/earthbound/comments/morrbn/i_made_a_funky_earthbound_battle_background/
Level background from earthbound
Death sound from super mario world
Dash sound effect from ultrakill
Victory and level 2 and level 3 music from deltarune
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
game.map.create_map_file("rooms/level_3.map")
game.map.switch_map("menu")
game.game_loop()