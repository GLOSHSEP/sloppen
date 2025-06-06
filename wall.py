import sloppen

class wall(sloppen.obj):
    def __init__(self, x, y, sprite, game):
        sloppen.obj.__init__(self, "wall", x, y, True, False, game)
        self.sprite_wall = sloppen.sprite(self.name, [sprite + ".png"], 0, 0, self.game)
        self.sprite = self.sprite_wall

    def instance_code(self):
        self.update_collision()