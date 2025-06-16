import sloppen
import pygame

class gun(sloppen.obj):
    def __init__(self, x, y, game):
        sloppen.obj.__init__(self, "gun", x, y, True, False, game)
        self.target = None
        self.shoot_timer = 0
        self.x_offset = 0
        self.flipped = False

        self.shoot_fx = pygame.mixer.Sound("sounds/effects/shoot.wav")

        sprite_path = "tiles/player/"
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
                if self.target.states == self.target.state_normal:
                    if self.shoot_timer == 0:
                        if self.target.key_shoot:
                            if self.target.fs == False:
                                self.shoot_timer = self.target.bullet_cool_down
                            else:
                                self.shoot_timer = self.target.fs
                            self.sprite = self.sprite_gun_shoot
                            self.x_offset = 20
                            self.shoot_fx.play()
                            self.game.map.current_map.add_object(bullet((self.x + 64) + (32 * self.target.direction), self.y + 64, self.target.direction, self.game), self.pos)
                            for i in self.game.map.current_map.map_objects:
                                if i.name == "camera":
                                    i.shake(10, 3)

                #decrease the x offset
                if self.x_offset > 0:
                    self.x_offset -= 1

                #update position
                self.x = self.target.x + (self.x_offset * self.target.direction * -1)
                self.y = self.target.y

                #flip sprites
                if self.target.states == self.target.state_normal:
                    if self.target.key_dir == -1:
                        if self.flipped == False:
                            self.flipped = True
                            self.sprite_gun.flip(True, False)
                            self.sprite_gun_shoot.flip(True, False)
                    elif self.target.key_dir == 1:
                        if self.flipped == True:
                            self.flipped = False
                            self.sprite_gun.flip(True, False)
                            self.sprite_gun_shoot.flip(True, False)

class bullet(sloppen.obj):
    def __init__(self, x, y, direction, game):
        sloppen.obj.__init__(self, "bullet", x, y, True, False, game)
        self.direction = direction

        sprite_path = "tiles/player/"
        self.sprite_bullet = sloppen.sprite(self.name, [sprite_path + "bullet/0.png", sprite_path + "bullet/1.png"], 2, 0, self.game)
        self.sprite = self.sprite_bullet

    def instance_code(self):
        if self.frozen != True:
            self.x += self.direction * 50

            self.update_collision()

            for i in self.game.map.current_map.map_objects:
                if i.name == "wall":
                    if self.colliding(self.x + self.direction * 50, self.y, i.collision) == True:
                        self.destroy = True
                        self.shake(5, 5)

            if self.x > self.game.map.current_map.width or self.x < 0 - self.sprite.width:
                self.destroy = True
                self.shake(5, 5)

            if self.y > self.game.map.current_map.height or self.y < 0 - self.sprite.height:
                self.destroy = True
                self.shake(5, 5)

    def shake(self, magnitude, length):
        for i in self.game.map.current_map.map_objects:
            if i.name == "camera":
                i.shake(magnitude, length)