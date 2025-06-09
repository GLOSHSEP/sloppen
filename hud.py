import sloppen

class hud(sloppen.obj):
    def __init__(self, game):
        sloppen.obj.__init__(self, "hud", 0, 0, True, False, game)