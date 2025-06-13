tiled_map = open(input("Tiled .tmj file "), "r")
data = tiled_map.readlines()
tiles_start = 0
tiles_end = 0
for i in range(0, len(data)):
    if '"data"' in data[i]:
        tiles_start = i
        for b in range(tiles_start, len(data)):
            if '],' in data[b]:
                tiles_end = b
                break
        break
tiled_map.close()

tiles = data[tiles_start : tiles_end + 1]
for i in range(0, len(tiles)):
    tiles[i] = tiles[i].strip()
    tiles[i] = tiles[i].replace('\n', '')
    tiles[i] = tiles[i].replace('"data":', '')
    tiles[i] = tiles[i].replace('[', '')
    tiles[i] = tiles[i].replace(']', '')

joined_tiles_string = ''.join(tiles)
joined_tiles_string = joined_tiles_string[:-1]
joined_tiles = joined_tiles_string.split(",")

for i in range(0, len(joined_tiles)):
    joined_tiles[i] = joined_tiles[i].replace(' ', '')

width = int(input("width "))
height = int(input("height "))

x = 0
y = 0

camera = []
hud = []
gun = []
player = []
win = []
enemy = []
power_up = []
wall = []
background = []

for i in range(0, len(joined_tiles)):
    x += 128
    if x >= width:
        x = 0
        y += 128
    if joined_tiles[i] != '0':
        if joined_tiles[i] == '10':
            player.append('player.player(' + str(x) + ',' + str(y) + ', self.game)')
        elif joined_tiles[i] == '11':
            camera.append('camera.camera(' + str(x) + ',' + str(y) + ',"player", 16, self.game)')
        elif joined_tiles[i] == '12':
            enemy.append('enemy.enemy(' + str(x) + ',' + str(y) + ', self.game)')
        elif joined_tiles[i] == '13':
            hud.append('hud.hud("sounds/music/level_1.mp3", self.game)')
        elif joined_tiles[i] == '14':
            win.append('win.win(' + str(x) + ',' + str(y) + ', "done", self.game)')
        elif joined_tiles[i] == '15':
            gun.append('gun.gun(' + str(x) + ',' + str(y) + ', self.game)')
        elif joined_tiles[i] == '16':
            power_up.append('power_ups.power_fr(' + str(x) + ',' + str(y) + ', self.game)')
        elif joined_tiles[i] == '17':
            power_up.append('power_ups.power_fs(' + str(x) + ',' + str(y) + ', self.game)')
        elif joined_tiles[i] == '18':
            power_up.append('power_ups.power_mwj(' + str(x) + ',' + str(y) + ', self.game)')
        else:
            wall.append('wall.wall(' + str(x) + ', ' + str(y) + ', "tiles/wall/' + str(joined_tiles[i]) + '", self.game)')

for i in background:
    print(i)

for i in wall:
    print(i)

for i in power_up:
    print(i)

for i in enemy:
    print(i)

for i in win:
    print(i)

for i in player:
    print(i)

for i in gun:
    print(i)

for i in hud:
    print(i)

for i in camera:
    print(i)