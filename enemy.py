import sloppen

class enemy(sloppen.obj):
    def __init__(self, x, y, game):
        sloppen.obj.__init__(self, "bg_back", 0, 0, True, False, game)

        sprites = []
        for i in range(0, length):
            sprites.append(sprite + "0.png")

        self.sprite_wall = sloppen.sprite(self.name, sprites, fps, 0, self.game)
        self.sprite = self.sprite_wall