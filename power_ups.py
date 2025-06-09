import sloppen

class power_fr(sloppen.obj):
    def __init__(self, x, y, sprite, game):
        sloppen.obj.__init__(self, "power_fr", x, y, True, False, game)
        self.sprite_block = sloppen.sprite(self.name, [sprite + ".png"], 0, 0, self.game)
        self.sprite = self.sprite_block

    def instance_code(self):
        self.update_collision()

class power_fs(sloppen.obj):
    def __init__(self, x, y, sprite, game):
        sloppen.obj.__init__(self, "power_fs", x, y, True, False, game)
        self.sprite_block = sloppen.sprite(self.name, [sprite + ".png"], 0, 0, self.game)
        self.sprite = self.sprite_block

    def instance_code(self):
        self.update_collision()

class power_mwj(sloppen.obj):
    def __init__(self, x, y, sprite, game):
        sloppen.obj.__init__(self, "power_mwj", x, y, True, False, game)
        self.sprite_block = sloppen.sprite(self.name, [sprite + ".png"], 0, 0, self.game)
        self.sprite = self.sprite_block

    def instance_code(self):
        self.update_collision()