import sloppen
import random

class camera(sloppen.obj):
    def __init__(self, x, y, target, buff, game):
        sloppen.obj.__init__(self, "camera", x, y, False, False, game)

        self.buff = buff

        self.wanted = target
        self.target = None

        self.view_w_half = self.game.screen.resolution[0] / 2
        self.view_h_half = self.game.screen.resolution[1] / 2

        self.x_to = 0
        self.y_to = 0

        self.shake_length = 0
        self.shake_magnitude = 0
        self.shake_remain = 0

        self.zoom_amount = 1

    def instance_code(self):
        if self.target == None:
            for i in self.game.map.current_map.map_objects:
                if i.name == self.wanted:
                    self.target = i
                    self.x_to = self.target.x
                    self.y_to = self.target.y
        else:
            self.x_to = self.target.x #+ (self.target.direction * 128)
            self.y_to = self.target.y

            self.x += (self.x_to - self.x) / 15
            self.y += (self.y_to - self.y) / 15

            self.x = self.clamp(self.x, self.view_w_half + self.buff, self.game.map.current_map.width - self.view_w_half - self.buff)
            self.y = self.clamp(self.y, self.view_h_half + self.buff, self.game.map.current_map.height - self.view_h_half - self.buff)

            self.x += random.uniform(-self.shake_remain, self.shake_remain)
            self.y += random.uniform(-self.shake_remain, self.shake_remain)

            if self.shake_length != 0:
                self.shake_remain = max(0, self.shake_remain - ((1 / self.shake_length) * self.shake_magnitude))
            else: 
                self.shake_remain = 0

            if self.zoom_amount > 1:
                self.zoom_amount -= 0.02
                if self.zoom_amount < 1:
                    self.zoom_amount = 1

            self.game.screen.update_offset_non_gui(self.x - self.view_w_half, self.y - self.view_h_half)
            self.game.screen.scale(1280 * self.zoom_amount, 720 * self.zoom_amount)

    def shake(self, magnitude, length):
        if magnitude > self.shake_remain:
            self.shake_magnitude = magnitude
            self.shake_remain = magnitude
            self.shake_length = length

    def zoom(self, zoom_number):
        self.zoom_amount = zoom_number

    def clamp(self, n, min, max):
        if n < min:
            return min
        elif n > max:
            return max
        else:
            return n