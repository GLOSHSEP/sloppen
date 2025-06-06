import sloppen

class gun(sloppen.obj):
    def __init__(self, x, y, game):
        sloppen.obj.__init__(self, "gun", x, y, True, False, game)
        self.target = None
        self.shoot_timer = 0
        self.x_offset = 0
        self.flipped = False

        sprite_path = "player/"
        self.sprite_gun = sloppen.sprite(self.name, [sprite_path + "gun/0.png", sprite_path + "gun/1.png", sprite_path + "gun/2.png"], 3, 0, self.game)
        self.sprite_gun_shoot = sloppen.sprite(self.name, [sprite_path + "gun_shoot/0.png"], 0, 0, self.game)
        self.sprite = self.sprite_gun

    def instance_code(self):
        if self.frozen != True:
            #find the player
            if self.target == None:
                for i in self.game.map.current_map.map_objects:
                    if i.name == "player":
                        self.target = i
            #player has been found
            else:
                #disable if the player is dead
                if self.target.states == self.target.state_dead:
                    self.visible = False
                    self.frozen = True

                #decrease the shooting timer and set the sprite back when done
                if self.shoot_timer > 0:
                    self.shoot_timer -= 1
                    if self.shoot_timer == 0:
                        self.sprite = self.sprite_gun

                #check if the player can shoot
                if self.shoot_timer == 0:
                    if self.target.key_shoot:
                        self.shoot_timer = 20
                        self.sprite = self.sprite_gun_shoot
                        self.x_offset = 20
                        self.game.map.current_map.add_object(bullet((self.x + 64) + (32 * self.target.direction), self.y + 64, self.target.direction, self.game), self.pos)

                #decrease the x offset
                if self.x_offset > 0:
                    self.x_offset -= 1

                #update position
                self.x = self.target.x + (self.x_offset * self.target.direction * -1)
                self.y = self.target.y

                #flip sprites
                if self.target.key_left:
                    if self.flipped == False:
                        self.flipped = True
                        self.sprite_gun.flip(True, False)
                        self.sprite_gun_shoot.flip(True, False)
                elif self.target.key_right:
                    if self.flipped == True:
                        self.flipped = False
                        self.sprite_gun.flip(True, False)
                        self.sprite_gun_shoot.flip(True, False)

class bullet(sloppen.obj):
    def __init__(self, x, y, direction, game):
        sloppen.obj.__init__(self, "bullet", x, y, True, False, game)
        self.direction = direction

        sprite_path = "player/"
        self.sprite_bullet = sloppen.sprite(self.name, [sprite_path + "bullet/0.png", sprite_path + "bullet/1.png"], 2, 0, self.game)
        self.sprite = self.sprite_bullet

    def instance_code(self):
        if self.frozen != True:
            self.x += self.direction * 15

            self.update_collision()

            for i in self.game.map.current_map.map_objects:
                if i.name == "wall":
                    if self.colliding(self.x + self.direction * 15, self.y, i.collision) == True:
                        self.game.map.current_map.remove_object(self.pos)