import pygame
import sloppen

class menu(sloppen.obj): 
    def __init__(self, game): 
        sloppen.obj.__init__(self, "menu", 0, 0, True, False, game)
        self.state_main = 0
        self.state_how = 1
        self.states = self.state_main
        self.cursor = 10
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
        #main menu
        if self.states == self.state_main:
            surface = pygame.Surface((self.game.screen.resolution[0], self.game.screen.resolution[1]))
            cursor_draw = self.font_draw.render("          <", False, (255, 255, 255))
            surface.blit(cursor_draw, (200, self.cursor))
            menu_draw = self.font_draw.render("PLAY GAME", False, (255, 255, 255))
            surface.blit(menu_draw, (10, 10))
            menu_draw = self.font_draw.render("HOW TO PLAY", False, (255, 255, 255))
            surface.blit(menu_draw, (10, 70))
            menu_draw = self.font_draw.render("EXIT", False, (255, 255, 255))
            surface.blit(menu_draw, (10, 130))
            controlls_z = self.font_draw.render("Z TO SELECT", False, (255, 255, 255))
            surface.blit(controlls_z, (400, 10))
            controlls_arrows = self.font_draw.render("ARROWS TO MOVE", False, (255, 255, 255))
            surface.blit(controlls_arrows, (360, 50))
            self.game.screen.queue_for_blit(surface, 0, 0, [0, 0], True, "menu_surface", 0)