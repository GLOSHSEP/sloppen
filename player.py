import sloppen
import pygame

class player(sloppen.obj):
    def __init__(self, x, y, game):
        sloppen.obj.__init__(self, "player", x, y, True, False, game)

        #controls
        self.key_left = 0
        self.key_right = 0
        self.key_jump = 0
        self.key_dash = 0
        self.key_shoot = 0

        #movement variables
        #general
        self.hsp = 0
        self.hsp_cap = 60
        self.vsp = 0
        self.grv = 0.3
        self.grounded = False
        self.direction = 1
        self.key_dir = 0
        #walk
        self.walk_speed = 0
        self.walk_cap = 20
        self.walk_accelerate = 10
        self.walk_fr = 20
        #dash
        self.dash_speed = 0
        self.dashes = [100, 100, 100]
        self.can_dash = False
        self.dash_jump = 12
        #jump
        self.jump_height = 12
        #wall jump
        self.wall_jump_height = 12
        self.wall_jump_knock_back = 30
        self.wall_jumps = 3
        self.wall_jump_speed = 0
        self.wall_mwj = 6
        #shoot
        self.bullet_cool_down = 20
        self.bullet_fs = 10

        #hurt
        self.hurt_counter = 0

        #status
        self.health = 3
        self.fr = False
        self.fs = False
        self.mwj = False

        #states
        self.state_lock = 0
        self.state_normal = 1
        self.state_dead = 2
        self.state_hurt = 3
        self.states = self.state_normal

        self.hurt_fx = pygame.mixer.Sound("sounds/effects/hurt.mp3")
        self.death_fx = pygame.mixer.Sound("sounds/effects/death.mp3")
        self.powerup_fx = pygame.mixer.Sound("sounds/effects/powerup.wav")

        #sprites
        sprite_path = "tiles/player/"

        self.sprite_idle = sloppen.sprite(self.name, [sprite_path + "idle/0.png", sprite_path + "idle/1.png", sprite_path + "idle/2.png", sprite_path + "idle/3.png", sprite_path + "idle/4.png"], 6, 0, self.game)
        self.sprite_walk = sloppen.sprite(self.name, [sprite_path + "walk/0.png", sprite_path + "walk/1.png", sprite_path + "walk/2.png", sprite_path + "walk/3.png", sprite_path + "walk/4.png", sprite_path + "walk/5.png"], 6, 0, self.game)
        self.sprite_jump = sloppen.sprite(self.name, [sprite_path + "jump/0.png", sprite_path + "jump/1.png", sprite_path + "jump/2.png"], 6, 0, self.game)
        self.sprite_fall = sloppen.sprite(self.name, [sprite_path + "fall/0.png", sprite_path + "fall/1.png", sprite_path + "fall/2.png"], 6, 0, self.game)
        self.sprite_dash = sloppen.sprite(self.name, [sprite_path + "dash/0.png", sprite_path + "dash/1.png", sprite_path + "dash/2.png"], 6, 0, self.game)
        self.sprite_die = sloppen.sprite(self.name, [sprite_path + "die/0.png", sprite_path + "die/1.png", sprite_path + "die/2.png", sprite_path + "die/3.png", sprite_path + "die/4.png", sprite_path + "die/5.png", sprite_path + "die/6.png"], 24, 0, self.game)
        self.sprite_hurt = sloppen.sprite(self.name, [sprite_path + "hurt/0.png"], 0, 0, self.game)
        
        self.sprite = self.sprite_idle

        self.flipped = False

    def instance_code(self):
        if self.states == self.state_lock:
            self.move()
            self.animate()
            self.check_collision()
            self.update_cords()
        elif self.states == self.state_normal:
            self.get_input()
            self.move()
            self.dash()
            self.jump()
            self.wall_jump()
            self.cap_hsp()
            self.animate()
            self.check_collision()
            self.update_cords()
        elif self.states == self.state_dead:
            self.death_animation()
        elif self.states == self.state_hurt:
            self.get_input()
            self.hurting()
            self.check_collision()
            self.update_cords()

    #enable player input
    def get_input(self):
        self.key_left = self.game.keyboard.check("K_LEFT")
        self.key_right = self.game.keyboard.check("K_RIGHT")
        self.key_jump = self.game.keyboard.check_pressed("K_UP")
        self.key_dash = self.game.keyboard.check_pressed("K_LSHIFT")
        self.key_shoot = self.game.keyboard.check_pressed("K_z")

    #enable basic movement and gravity
    def move(self):
        #calculate direction
        self.key_dir = self.key_right - self.key_left

        #save direction
        if self.key_dir != 0:
            self.direction = self.key_dir

        #calculate movement speed
        if self.fr == False:
            self.walk_speed = self.walk_accelerate * self.key_dir
        else:
            self.walk_speed = self.walk_fr * self.key_dir

        #if self.key_dir == 0:
            #self.walk_speed = 0

        self.hsp = self.walk_speed

        #add gravity
        self.vsp += self.grv

    #enable dash
    def dash(self):
        #let the player dash
        if self.dash_speed == 0:
            self.can_dash = True

        #decrease speed
        if self.dash_speed > 0:
            self.dash_speed -= 1

        if self.hsp != 0:
            #disable dashing
            if self.dash_speed >= 40:
                self.can_dash = False

            #preform dash
            if self.key_dash and self.can_dash == True:
                #little jump
                if self.dash_speed <= 10:
                    self.vsp = 0

                #add speed
                self.dash_speed += 20

                #create ghost sprite
                self.game.map.current_map.add_object(player_ghost(self.x, self.y, self.game, self.flipped), self.pos)

                #camera shake
                self.shake(6, 10)
                self.zoom(1.05)

        self.hsp += self.dash_speed * self.sign(self.hsp)

    #enable jump
    def jump(self):
        if self.grounded and self.key_jump == True:
            self.vsp -= self.jump_height
            self.shake(3, 6)

    #enable wall jump
    def wall_jump(self):
        for i in self.game.map.current_map.map_objects:
            if i.name == "wall":
                #can the player wall jump
                if self.wall_jumps > 0 and not self.grounded:
                    #check if the player is pressed against the wall
                    if self.colliding(self.x - 1, self.y, i.collision) and self.key_jump and self.key_left:
                        self.vsp = -self.wall_jump_height
                        self.hsp += self.wall_jump_knock_back
                        self.wall_jumps -= 1
                        self.shake(3, 6)
                        break
                    if self.colliding(self.x + 1, self.y, i.collision) and self.key_jump and self.key_right:
                        self.vsp = -self.wall_jump_height
                        self.hsp -= self.wall_jump_knock_back
                        self.wall_jumps -= 1
                        self.shake(3, 6)
                        break

        #refresh wall jumps
        if self.grounded:
            if self.mwj == False:
                self.wall_jumps = 3
            else:
                self.wall_jumps = self.wall_mwj

    #enable hsp cap
    def cap_hsp(self):
        #make sure the hsp cant get to high
        if self.hsp * self.sign(self.hsp) > self.hsp_cap:
            self.hsp = self.hsp_cap * self.sign(self.hsp)

    #enable animation
    def animate(self):
        #if the player is not dashing
        if self.dash_speed <= 10:
            if not self.grounded:
                if self.sign(self.vsp) > 0: self.sprite = self.sprite_fall #player falling
                else: self.sprite = self.sprite_jump #player jumping
            #if the player is on the ground
            else:
                if self.hsp == 0: self.sprite = self.sprite_idle #player is idle
                else: self.sprite = self.sprite_walk #player is walking

        #player is dashing
        else:
            self.sprite = self.sprite_dash

        #player is facing left
        if self.key_left:
            if self.flipped == False:
                self.flipped = True
                self.sprite_idle.flip(True, False)
                self.sprite_walk.flip(True, False)
                self.sprite_jump.flip(True, False)
                self.sprite_fall.flip(True, False)
                self.sprite_dash.flip(True, False)
                self.sprite_die.flip(True, False)
                self.sprite_hurt.flip(True, False)
        #player is facing right
        elif self.key_right:
            if self.flipped == True:
                self.flipped = False
                self.sprite_idle.flip(True, False)
                self.sprite_walk.flip(True, False)
                self.sprite_jump.flip(True, False)
                self.sprite_fall.flip(True, False)
                self.sprite_dash.flip(True, False)
                self.sprite_die.flip(True, False)
                self.sprite_hurt.flip(True, False)

    #make the player hurt
    def do_hurt(self):
        if self.health <= 0:
            self.states = self.state_dead
            return

        self.shake(10, 20)
        self.zoom(1.1)
        self.hurt_fx.play()

        self.health -= 1
    
        self.sprite = self.sprite_hurt
    
        self.hsp = (self.hsp * -1) / 2

        self.states = self.state_hurt

    #enable hurting
    def hurting(self):
        if self.health <= 0:
            self.states = self.state_dead
            return

        self.vsp += self.grv

        self.hurt_counter += 1
        if self.hurt_counter >= 10:
            self.hurt_counter = 0
            self.states = self.state_normal

    #enable collisions
    def check_collision(self):
        #set grounded to false as we have to check again
        self.grounded = False
        #check game objects
        for i in self.game.map.current_map.map_objects:
            if i.name == "wall":
                if self.colliding(self.x + self.hsp, self.y, i.collision) == True:
                    while self.colliding(self.x + self.sign(self.hsp), self.y, i.collision) != True:
                        self.x += self.sign(self.hsp)
                    if self.x < i.collision[0] + i.collision[2] and self.x > i.collision[0]:
                        self.x = i.collision[0] + i.collision[2]
                    if self.x + self.collision[2] > i.collision[0] and self.x < i.collision[0] + i.collision[2]:
                        self.x = i.collision[0] - self.collision[2]
                    self.hsp = 0

                if self.colliding(self.x, self.y + self.vsp, i.collision) == True:
                    while self.colliding(self.x, self.y + self.sign(self.vsp), i.collision) != True:
                        self.y += self.sign(self.vsp)
                    #if self.y < i.collision[1] + i.collision[3] and self.y > i.collision[1]:
                        #self.y = i.collision[1] + i.collision[3]
                    #if self.y + self.collision[3] > i.collision[1] and self.y < i.collision[1] + i.collision[3]:
                        #self.y = i.collision[1] - self.collision[3]
                    self.vsp = 0

                if self.colliding(self.x, self.y + 1, i.collision) == True:
                    self.grounded = True

            #check hurt conditions
            if i.name == "enemy":
                if self.colliding(self.x, self.y, i.collision) == True:
                    if i.states != i.state_dead:
                        if self.states != self.state_hurt:
                            self.do_hurt()

            if i.name == "enemy_bullet":
                if self.colliding(self.x, self.y, i.collision) == True:
                    if self.states != self.state_hurt:
                        self.do_hurt()
                        i.destroy = True

            #check power ups
            if i.name == "power_fr":
                if self.colliding(self.x, self.y, i.collision) == True:
                    self.fr = True
                    self.powerup_fx.play()
                    i.destroy = True

            if i.name == "power_fs":
                if self.colliding(self.x, self.y, i.collision) == True:
                    self.fs = True
                    self.powerup_fx.play()
                    i.destroy = True

            if i.name == "power_mwj":
                if self.colliding(self.x, self.y, i.collision) == True:
                    self.mwj = True
                    self.powerup_fx.play()
                    i.destroy = True

        if self.x > self.game.map.current_map.width or self.x < 0 - self.sprite.width:
            self.health = 0
            self.states = self.state_dead

        if self.y > self.game.map.current_map.height or self.y < 0 - self.sprite.height:
            self.health = 0
            self.states = self.state_dead
    
    #enable application of horizontal speed and veritcal speed
    def update_cords(self):
        self.x += self.hsp
        self.y += self.vsp
        self.update_collision()

    #enable death animation
    def death_animation(self):
        if self.sprite != self.sprite_die:
            self.x -= 64
            self.y -= 64
            self.sprite = self.sprite_die
            self.shake(20, 60 * 5)
            self.zoom(1.5)
            self.death_fx.play()
        else:
            if self.sprite.frame_index == len(self.sprite.frames) - 1:
                self.sprite.fps = 0

        if self.game.keyboard.check_pressed("K_z"):
            self.death_fx.stop()
            self.game.screen.scale(1280, 720)
            self.game.map.switch_map(self.game.map.current_map.name)
        if self.game.keyboard.check_pressed("K_x"):
            self.death_fx.stop()
            self.game.screen.scale(1280, 720)
            self.game.map.switch_map("menu")

    def shake(self, magnitude, length):
        for i in self.game.map.current_map.map_objects:
            if i.name == "camera":
                i.shake(magnitude, length)

    def zoom(self, zoom_number):
        for i in self.game.map.current_map.map_objects:
            if i.name == "camera":
                i.zoom(zoom_number)

class player_ghost(sloppen.obj):
    def __init__(self, x, y, game, flip):
        sloppen.obj.__init__(self, "ghost", x, y, True, False, game)
        sprite_path = "tiles/player/"
        self.sprite_ghost = sloppen.sprite(self.name, [sprite_path + "ghost/0.png", sprite_path + "ghost/1.png", sprite_path + "ghost/2.png"], 6, 0, self.game)
        self.sprite = self.sprite_ghost
        if flip:
            self.sprite.flip(True, False)

    def instance_code(self):
        if self.frozen != True:
            if self.sprite.frame_index == len(self.sprite.frames) - 1:
                self.sprite.fps = 0
                self.destroy = True
                self.frozen = True