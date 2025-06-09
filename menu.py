import pygame
import sloppen

class menu(sloppen.obj): 
    def __init__(self, game): 
        sloppen.obj.__init__(self, "menu", 0, 0, True, False, game)
        self.state_main = 0
        self.state_how = 1
        self.states = self.state_main

        self.cursor = 10

        sprite_path = "menu/"

        sprite_bg_temp = []

        for i in range(0, 20):
            sprite_bg_temp.append(sprite_path + "bg/" + str(i) + ".png")

        self.sprite_bg = sloppen.sprite(self.name, sprite_bg_temp, 12, 0, self.game)

        for i in range(0, len(self.sprite_bg.frames)):
            self.sprite_bg.frames[i] = pygame.transform.scale(self.sprite_bg.frames[i], (1280, 720))
    
        self.sprite_title = sloppen.sprite(self.name, [sprite_path + "title/0.png"], 0, 0, self.game)

        self.font_draw = pygame.font.Font("fonts/fontgame.ttf", 30)

    def instance_code(self):
        #main menu
        if self.states == self.state_main:
            #play
            if self.cursor == 10 and self.game.keyboard.check_pressed("K_z"):
                self.game.map.switch_map("level_1")
            #how
            elif self.cursor == 70 and self.game.keyboard.check_pressed("K_z"): 
                self.states = self.state_how
            #exit
            elif self.cursor == 130 and self.game.keyboard.check_pressed("K_z"): 
                exit(0)

            #move cursor
            if self.cursor > 10 and self.game.keyboard.check_pressed("K_UP"): self.cursor -= 60 
            if self.cursor < 130 and self.game.keyboard.check_pressed("K_DOWN"): self.cursor += 60
        #how to play
        elif self.states == self.state_how:
            #back
            if self.game.keyboard.check_pressed("K_z"): 
                self.states = self.state_main

    def instance_draw(self):
        self.sprite_bg.draw_sprite(0, 0)

        #main menu
        if self.states == self.state_main:
            cursor_draw = self.font_draw.render("          <", False, (255, 255, 255))
            self.game.screen.queue_for_blit(cursor_draw, 200, self.cursor, [0, 0], True, "menu_text", 0)
            menu_draw = self.font_draw.render("PLAY GAME", False, (255, 255, 255))
            self.game.screen.queue_for_blit(menu_draw, 10, 10, [0, 0], True, "menu_text", 0)
            menu_draw = self.font_draw.render("HOW TO PLAY", False, (255, 255, 255))
            self.game.screen.queue_for_blit(menu_draw, 10, 70, [0, 0], True, "menu_text", 0)
            menu_draw = self.font_draw.render("EXIT", False, (255, 255, 255))
            self.game.screen.queue_for_blit(menu_draw, 10, 130, [0, 0], True, "menu_text", 0)
            controlls_z = self.font_draw.render("Z TO SELECT", False, (255, 255, 255))
            self.game.screen.queue_for_blit(controlls_z, 1000, 10, [0, 0], True, "menu_text", 0)
            controlls_arrows = self.font_draw.render("ARROWS TO MOVE", False, (255, 255, 255))
            self.game.screen.queue_for_blit(controlls_arrows, 980, 50, [0, 0], True, "menu_text", 0)

        self.sprite_title.draw_sprite(0, 0)
