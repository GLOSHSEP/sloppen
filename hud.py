import sloppen

class hud(sloppen.obj):
    def __init__(self, song, game):
        sloppen.obj.__init__(self, "hud", 0, 0, True, False, game)

        self.target = None

        self.music = pygame.mixer.Sound(song)
        self.music.play(-1)

        sprite_path = "hud/"
        self.sprite_main = sloppen.sprite(self.name, [sprite_path + "main/0.png"], 0, 0, self.game)
        self.sprite_h1 = sloppen.sprite(self.name, [sprite_path + "heart_1/0.png"], 0, 0, self.game)
        self.sprite_h2 = sloppen.sprite(self.name, [sprite_path + "heart_2/0.png"], 0, 0, self.game)
        self.sprite_h3 = sloppen.sprite(self.name, [sprite_path + "heart_3/0.png"], 0, 0, self.game)
        self.sprite_fr = sloppen.sprite(self.name, [sprite_path + "fr/0.png"], 0, 0, self.game)
        self.sprite_fs = sloppen.sprite(self.name, [sprite_path + "fs/0.png"], 0, 0, self.game)
        self.sprite_mwj = sloppen.sprite(self.name, [sprite_path + "mwj/0.png"], 0, 0, self.game)
        self.sprite_died = sloppen.sprite(self.name, [sprite_path + "died/0.png"], 0, 0, self.game)

    def instance_code(self):
        if self.target == None:
            for i in self.game.map.current_map.map_objects:
                if i.name == "player":
                    self.target = i
        else:
            if self.target.states = self.target.state_dead:
                self.music.stop()

    def instance_draw(self):
        self.sprite_main.draw_sprite_gui(0, 0)
        
        if self.target != None:
            if self.target.health == 3:
                self.sprite_h3.draw_sprite_gui(0, 0)
            elif self.target.health == 2:
                self.sprite_h2.draw_sprite_gui(0, 0)
            elif self.target.health == 1:
                self.sprite_h1.draw_sprite_gui(0, 0)

            if self.target.fr == True:
                self.sprite_fr.draw_sprite_gui(0, 0)
            if self.target.fs == True:
                self.sprite_fs.draw_sprite_gui(0, 0)
            if self.target.mwj == True:
                self.sprite_mwj.draw_sprite_gui(0, 0)

            if self.target.states == self.target.state_dead:
                self.sprite_died.draw_sprite_gui(0, 0)
