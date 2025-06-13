import sloppen
import pygame

class background(sloppen.obj):
    def __init__(self, sprite, length, fps, width, height, game):
        sloppen.obj.__init__(self, "background", 0, 0, True, False, game)

        sprites = []
        for i in range(0, length):
            sprites.append(sprite + str(i) + ".png")

        self.sprite_background = sloppen.sprite(self.name, sprites, fps, 0, self.game)

        for i in range(0, len(self.sprite_background.frames)):
            self.sprite_background.frames[i] = pygame.transform.scale(self.sprite_background.frames[i], (width, height))

        self.sprite = self.sprite_background

    def instance_draw(self):
        self.draw_self_gui()