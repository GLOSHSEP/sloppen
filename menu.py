import sloppen
import pygame
import os

class menu(sloppen.obj): 
    def __init__(self, game): 
        sloppen.obj.__init__(self, "menu", 0, 0, True, False, game)

        self.state_main = 0
        self.state_how = 1
        self.states = self.state_main

        self.cursor = 10

        self.bg_toggle_value = False
        if os.path.exists("options"):
            file = open("options", "r")
            data = file.readlines()
            file.close()
            if data[0] == "true":
                self.bg_toggle_value = True
            else:
                self.bg_toggle_value = False

        self.show_error = False
        self.bg_toggle_text = False

        self.game.screen.scale(1280, 720)

        self.music = pygame.mixer.Sound("sounds/music/menu.mp3")
        self.music.play(-1)

        sprite_path = "backgrounds/menu/"
        sprite_path_2 = "tiles/"

        sprite_bg_temp = []

        for i in range(0, 20):
            sprite_bg_temp.append(sprite_path + str(i) + ".png")

        self.sprite_bg = sloppen.sprite(self.name, sprite_bg_temp, 0, 0, self.game)

        for i in range(0, len(self.sprite_bg.frames)):
            self.sprite_bg.frames[i] = pygame.transform.scale(self.sprite_bg.frames[i], (1280, 720))
    
        self.sprite_title = sloppen.sprite(self.name, [sprite_path_2 + "title/0.png"], 0, 0, self.game)
        self.sprite_how = sloppen.sprite(self.name, [sprite_path_2 + "how/0.png"], 0, 0, self.game)

        self.font_draw = pygame.font.Font("fonts/fontgame.ttf", 30)

    def instance_code(self):
        #set it to false so it only display if you are hovering over the load button same with the background toggle
        self.show_error = False
        self.bg_toggle_text = False

        if self.bg_toggle_value == True and self.sprite_bg.fps == 0:
            self.sprite_bg.fps = 12
        
        if self.bg_toggle_value == False and self.sprite_bg.fps != 0:
            self.sprite_bg.fps = 0
            self.sprite_bg.frame_index = 0

        #main menu
        if self.states == self.state_main:
            #play
            if self.cursor == 10 and self.game.keyboard.check_pressed("K_z"):
                self.music.stop()
                self.game.map.switch_map("level_1")
            #load
            elif self.cursor == 70: 
                if os.path.exists("save"):
                    if self.game.keyboard.check_pressed("K_z"):
                        file = open("save", 'r')
                        data = file.readlines()
                        file.close()
                        self.music.stop()
                        self.game.map.switch_map(data[0])
                else:
                    self.show_error = True
            #delete
            elif self.cursor == 130 and self.game.keyboard.check_pressed("K_z"):
                if os.path.exists("save"):
                    os.remove("save")
            #background toggle
            elif self.cursor == 190:
                self.bg_toggle_text = True
                if self.game.keyboard.check_pressed("K_z"):
                    self.bg_toggle_value = not self.bg_toggle_value

                    if os.path.exists("options"):
                        file = open("options", 'w')
                    else:
                        file = open("options", 'x')

                    if self.bg_toggle_value == True:
                        file.write("true")
                    else:
                        file.write("false")

                    file.close()
                            
            #how
            elif self.cursor == 250 and self.game.keyboard.check_pressed("K_z"): 
                self.states = self.state_how
            #exit
            elif self.cursor == 310 and self.game.keyboard.check_pressed("K_z"): 
                exit(0)

            #move cursor
            if self.cursor > 10 and self.game.keyboard.check_pressed("K_UP"): self.cursor -= 60 
            if self.cursor < 310 and self.game.keyboard.check_pressed("K_DOWN"): self.cursor += 60
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
            menu_draw = self.font_draw.render("LOAD GAME", False, (255, 255, 255))
            self.game.screen.queue_for_blit(menu_draw, 10, 70, [0, 0], True, "menu_text", 0)
            menu_draw = self.font_draw.render("DELETE SAVE", False, (255, 255, 255))
            self.game.screen.queue_for_blit(menu_draw, 10, 130, [0, 0], True, "menu_text", 0)
            menu_draw = self.font_draw.render("ANIMATE BG", False, (255, 255, 255))
            self.game.screen.queue_for_blit(menu_draw, 10, 190, [0, 0], True, "menu_text", 0)
            menu_draw = self.font_draw.render("HOW TO PLAY", False, (255, 255, 255))
            self.game.screen.queue_for_blit(menu_draw, 10, 250, [0, 0], True, "menu_text", 0)
            menu_draw = self.font_draw.render("EXIT", False, (255, 255, 255))
            self.game.screen.queue_for_blit(menu_draw, 10, 310, [0, 0], True, "menu_text", 0)
            controlls_z = self.font_draw.render("Z TO SELECT", False, (255, 255, 255))
            self.game.screen.queue_for_blit(controlls_z, 980, 10, [0, 0], True, "menu_text", 0)
            controlls_arrows = self.font_draw.render("ARROWS TO MOVE", False, (255, 255, 255))
            self.game.screen.queue_for_blit(controlls_arrows, 960, 50, [0, 0], True, "menu_text", 0)
            controlls_leave = self.font_draw.render("ESC IN GAME TO RETURN", False, (255, 255, 255))
            self.game.screen.queue_for_blit(controlls_leave, 900, 90, [0, 0], True, "menu_text", 0)
            controlls_leave = self.font_draw.render("TO THE MENU", False, (255, 255, 255))
            self.game.screen.queue_for_blit(controlls_leave, 980, 130, [0, 0], True, "menu_text", 0)
            if self.show_error:
                error_message = self.font_draw.render("YOU NEED A SAVE FILE TO LOAD", False, (255, 255, 255))
                self.game.screen.queue_for_blit(error_message, 400, 70, [0, 0], True, "menu_text", 0)
            if self.bg_toggle_text:
                toggle_message = self.font_draw.render("CURRENTLY " + str(self.bg_toggle_value).upper(), False, (255, 255, 255))
                self.game.screen.queue_for_blit(toggle_message, 400, 190, [0, 0], True, "menu_text", 0)
            self.sprite_title.draw_sprite(180, 0)
        #how to play screen
        elif self.states == self.state_how:
            self.sprite_how.draw_sprite(0, 0)