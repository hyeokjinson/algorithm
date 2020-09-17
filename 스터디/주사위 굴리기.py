import sys

height, width, start_y, start_x, _ = map(int, sys.stdin.readline().split())
maps = []
for _ in range(height):
    maps.append(list(map(int, sys.stdin.readline().split())))
order = list(map(int, sys.stdin.readline().split()))


class Dice:
    def __init__(self):
        self.t = 0
        self.b = 0
        self.e = 0
        self.w = 0
        self.n = 0
        self.s = 0


dice = Dice()

for i in order:
    if i == 1:
        dy, dx = 0, 1
        ny, nx = start_y + dy, start_x + dx
        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
            dice.e, dice.b, dice.w, dice.t = dice.t, dice.e, dice.b, dice.w
            if maps[ny][nx] == 0:
                maps[ny][nx] = dice.b
            else:
                dice.b = maps[ny][nx]
                maps[ny][nx] = 0
            print(dice.t)
            start_y, start_x = ny, nx
    elif i == 2:
        dy, dx = 0, -1
        ny, nx = start_y + dy, start_x + dx
        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
            dice.w, dice.b, dice.e, dice.t = dice.t, dice.w, dice.b, dice.e
            if maps[ny][nx] == 0:
                maps[ny][nx] = dice.b
            else:
                dice.b = maps[ny][nx]
                maps[ny][nx] = 0
            print(dice.t)
            start_y, start_x = ny, nx
    elif i == 3:
        dy, dx = -1, 0
        ny, nx = start_y + dy, start_x + dx
        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
            dice.n, dice.b, dice.s, dice.t = dice.t, dice.n, dice.b, dice.s
            if maps[ny][nx] == 0:
                maps[ny][nx] = dice.b
            else:
                dice.b = maps[ny][nx]
                maps[ny][nx] = 0
            print(dice.t)
            start_y, start_x = ny, nx

    elif i == 4:
        dy, dx = 1, 0
        ny, nx = start_y + dy, start_x + dx
        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
            dice.s, dice.t, dice.n, dice.b = dice.t, dice.n, dice.b, dice.s
            if maps[ny][nx] == 0:
                maps[ny][nx] = dice.b
            else:
                dice.b = maps[ny][nx]
                maps[ny][nx] = 0
            print(dice.t)
            start_y, start_x = ny, nx