import sloppen

class win(sloppen.obj):
    def __init__(self, x, y, next, game):
        sloppen.obj.__init__(self, "win", x, y, True, False, game)

        self.next = next
        self.won = False

        self.sprite_clear = sloppen.sprite(self.name, ["tiles/win/clear/0.png"], 0, 0, self.game)
        self.sprite_win = sloppen.sprite(self.name, ["tiles/player/idle/0.png"], 0, 0, self.game)
        self.sprite = self.sprite_win

    def instance_code(self):
        if self.won == False:
            self.update_collision()

            for i in self.game.map.current_map.map_objects:
                if i.name == "player":
                    if self.colliding(self.x, self.y, i.collision):
                        for i in self.game.map.current_map.map_objects:
                            if i.name != "win":
                                if i.name == "hud":
                                    i.music.stop()
                                i.destroy = True
                        self.won = True

                        #save progress if you arent done the game
                        if self.next != "done":
                            try:
                                file = open("save", 'x')
                            except:
                                file = open("save", 'w')
                            file.write(self.next)
                            file.close()
        else:
            if self.game.keyboard.check_pressed("K_z"):
                self.game.map.switch_map(self.next)
            if self.game.keyboard.check_pressed("K_x"):
                self.game.map.switch_map("menu")

    def instance_draw(self):
        if self.won == False:
            self.draw_self()
        else:
            self.sprite_clear.draw_sprite(0, 0)

class done(sloppen.obj):
    def __init__(self, game):
        sloppen.obj.__init__(self, "done", 0, 0, True, False, game)

        self.sprite_win = sloppen.sprite(self.name, ["tiles/win/end/0.png"], 0, 0, self.game)
        self.sprite = self.sprite_win

    def instance_code(self):
        if self.game.keyboard.check_pressed("K_z"):
            self.game.map.switch_map("menu")