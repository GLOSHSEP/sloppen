import sloppen
import pygame
import statistics

class enemy(sloppen.obj):
    def __init__(self, x, y, game):
        sloppen.obj.__init__(self, "enemy", x, y, True, False, game)

        self.hsp = 0
        self.vsp = 0
        self.grv = 0.3
        self.walksp = 3
        self.direction = True
        self.hurt_timer = 0
        self.hp = 3
        self.target = None
        self.shoot_cool_down = 0

        self.state_walk = 0
        self.state_hurt = 1
        self.state_dead = 2
        self.states = self.state_walk

        self.hurt_fx = pygame.mixer.Sound("sounds/effects/en_hurt.wav")

        sprite_path = "tiles/enemy/"
        self.sprite_idle = sloppen.sprite(self.name, [sprite_path + "idle/0.png", sprite_path + "idle/1.png", sprite_path + "idle/2.png", sprite_path + "idle/3.png"], 6, 0, self.game)
        self.sprite_hurt = sloppen.sprite(self.name, [sprite_path + "hurt/0.png"], 0, 0, self.game)
        self.sprite_dead = sloppen.sprite(self.name, [sprite_path + "dead/0.png"], 0, 0, self.game)
        self.sprite = self.sprite_idle

        self.flipped = False

    def instance_code(self):
        #find player object
        if self.target == None:
            for i in self.game.map.current_map.map_objects:
                if i.name == "player":
                    self.target = i

        #apply gravity
        self.vsp += self.grv

        #count down the cooldown timer
        if self.shoot_cool_down > 0:
            self.shoot_cool_down -= 1

        #walking state
        if self.states == self.state_walk:
            #switch sprite
            if self.sprite != self.sprite_idle:
                self.sprite = self.sprite_idle

            #make the enemy move based on the direction
            if self.direction == False:
                self.hsp = self.walksp
            else:
                self.hsp = self.walksp * -1

            #add shooting
            if self.target != None:
                #make sure the enemy only shoots if the player is within range
                if (self.target.y - self.y) < 720 and (self.target.y - self.y) > - 720:
                    if self.direction == False:
                        if (self.target.x - self.x) > 0 and (self.target.x - self.x) < 1280:
                            if self.shoot_cool_down == 0:
                                self.game.map.current_map.add_object(enemy_bullet((self.x + 64) + (32 * self.direction * -1), self.y + 64, self.target, self.game), self.pos)
                                self.shoot_cool_down = 120
                    else:
                        if (self.target.x - self.x) < 0 and (self.target.x - self.x) > -1280:
                            if self.shoot_cool_down == 0:
                                self.game.map.current_map.add_object(enemy_bullet((self.x + 64) + (32 * self.direction * -1), self.y + 64, self.target, self.game), self.pos)
                                self.shoot_cool_down = 120

            #add direction switching

        #hurt state
        elif self.states == self.state_hurt:
            #switch sprite
            if self.sprite != self.sprite_hurt:
                #make the enemy stay still
                self.hsp = 0
                #apply hurt effects
                self.sprite = self.sprite_hurt
                self.shake(5, 10)
    
            #count down the hurt timer
            self.hurt_timer += 1
            if self.hurt_timer >= 20:
                self.hurt_timer = 0
                self.states = self.state_walk

        #dead state
        elif self.states == self.state_dead:
            #switch sprite
            if self.sprite != self.sprite_dead:
                #make the enemy stay still
                self.hsp = 0
                #apply dead effects
                self.sprite = self.sprite_dead
                self.shake(10, 20)

        self.flipping()
        self.check_collision()
        self.update_cords()

    def flipping(self):
        if self.direction:
            if self.flipped == False:
                self.flipped = True
                self.sprite_idle.flip(True, False)
                self.sprite_hurt.flip(True, False)
                self.sprite_dead.flip(True, False)
        else:
            if self.flipped == True:
                self.flipped = False
                self.sprite_idle.flip(True, False)
                self.sprite_hurt.flip(True, False)
                self.sprite_dead.flip(True, False)

    #enable collisions
    def check_collision(self):
        #variable for tracking if there is a free space causing the enemy to fall off
        free = True

        #game objects checks
        for i in self.game.map.current_map.map_objects:
            #wall check
            if i.name == "wall":
                if self.colliding(self.x + self.hsp, self.y, i.collision) == True:
                    while self.colliding(self.x + self.sign(self.hsp), self.y, i.collision) != True:
                        self.x += self.sign(self.hsp)
                    self.hsp = 0

                    #enemy hit a wall flip direction
                    self.direction = not self.direction

                if self.colliding(self.x, self.y + self.vsp, i.collision) == True:
                    while self.colliding(self.x, self.y + self.sign(self.vsp), i.collision) != True:
                        self.y += self.sign(self.vsp)
                    self.vsp = 0
                
                if self.direction == False:
                    if self.colliding(self.x + 129, self.y + 129, i.collision) == True:
                        free = False
                else:
                    if self.colliding(self.x - 128, self.y + 129, i.collision) == True:
                        free = False
            
            #bullet check
            if i.name == "bullet":
                if self.colliding(self.x + self.hsp, self.y, i.collision) == True:
                    i.destroy = True
                    self.vsp -= 3
                    self.hp -= 1
                    self.hurt_fx.play()
                    if self.hp > 0:
                        self.states = self.state_hurt
                    else:
                        self.states = self.state_dead

        #out of bounds check
        if self.x > self.game.map.current_map.width or self.x < 0 - self.sprite.width:
            self.health = 0
            self.states = self.state_dead
            self.destroy = True

        if self.y > self.game.map.current_map.height or self.y < 0 - self.sprite.height:
            self.health = 0
            self.states = self.state_dead
            self.destroy = True
        
        #switch direction if needed
        if free:
            self.direction = not self.direction

    #enable application of horizontal speed and veritcal speed
    def update_cords(self):
        self.x += self.hsp
        self.y += self.vsp
        self.update_collision()

    def shake(self, magnitude, length):
        for i in self.game.map.current_map.map_objects:
            if i.name == "camera":
                i.shake(magnitude, length)

class enemy_bullet(sloppen.obj):
    def __init__(self, x, y, target, game):
        sloppen.obj.__init__(self, "enemy_bullet", x, y, True, False, game)

        self.target = target
        self.timer = 120

        sprite_path = "tiles/enemy/"
        self.sprite_bullet = sloppen.sprite(self.name, [sprite_path + "bullet/0.png"], 2, 0, self.game)
        self.sprite = self.sprite_bullet

    def instance_code(self):
        self.x = statistics.median([(self.x - 3), self.target.x, (self.x + 3)])
        self.y = statistics.median([(self.y - 2), self.target.y, (self.y + 2)])

        self.timer -= 1
        if self.timer <= 0:
            self.destroy = True

        self.update_collision()

        for i in self.game.map.current_map.map_objects:
            if i.name == "wall":
                if self.colliding(self.x, self.y, i.collision):
                    self.destroy = True
                    self.shake(5, 5)
                if self.colliding(self.x, self.y, i.collision):
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