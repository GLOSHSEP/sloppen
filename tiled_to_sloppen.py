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
    tiles[i] = tiles[i].replace(',', '')
    tiles[i] = tiles[i].replace(' ', '')

joined_tiles = ''.join(tiles)
width = int(input("width "))
height = int(input("height "))
x = 0
y = 0
for i in range(0, len(joined_tiles)):
    x += 128
    if x >= width:
        x = 0
        y += 128
    print(joined_tiles)
    if joined_tiles[i] != '0':
        if joined_tiles[i] == '10':
            print('player.player(' + str(x) + ',' + str(y) + ', self.game)')
        elif joined_tiles[i] == '11':
            print('camera.camera(' + str(x) + ',' + str(y) + ',"player", 16, self.game)')
        elif joined_tiles[i] == '12':
            print('enemy.enemy(' + str(x) + ',' + str(y) + ', self.game)')
        elif joined_tiles[i] == '13':
            print('hud.hud("sounds/music/level_1.mp3", self.game)')
        elif joined_tiles[i] == '14':
            pass
        elif joined_tiles[i] == '15':
            print('gun.gun(' + str(x) + ',' + str(y) + ', self.game)')
        elif joined_tiles[i] == '16':
            print('power_ups.power_fr(' + str(x) + ',' + str(y) + ', self.game)')
        elif joined_tiles[i] == '17':
            print('power_ups.power_fs(' + str(x) + ',' + str(y) + ', self.game)')
        elif joined_tiles[i] == '18':
            print('power_ups.power_mwj(' + str(x) + ',' + str(y) + ', self.game)')
        else:
            print('wall.wall(' + str(x) + ', ' + str(y) + ', "tiles/wall/' + str(joined_tiles[i]) + '", self.game)')