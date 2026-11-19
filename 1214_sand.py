from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parent / "input"

shapes = [[[int(e) for e in  p.strip().split(',')] for p in ln.split('->')] for ln in open(INPUT_DIR / '1214_sand_small.txt', 'r').readlines()]
max_x, max_y, min_x = max([x for s in shapes for x, _ in s]) + 1, max([y for s in shapes for _, y in s]) + 1, min([x for s in shapes for x, _ in s]) - 1
rock = [e[:] for e in [['.']*(max_x + 2)]*(max_y + 2)] # rock[y][x] -> height will be the first index
rock[0][500] = '+'  # source
for shape in shapes: 
    px, py, i = shape[0][0], shape[0][1], 1
    rock[py][px] = '#'
    while i < len(shape): 
        x, y = shape[i][0], shape[i][1]
        rock[y][x] = '#'
        for j in range(py, y, 1 if y > py else -1): rock[j][x] = '#'
        for j in range(px, x, 1 if x > px else -1): rock[y][j] = '#'
        px, py, i = x, y, i + 1

print_rock = lambda: print('\n'.join([''.join(ln[max(min_x - 1,0):]) for ln in rock]))

def fall_sand(x, y, rock, min_x, max_x, max_y):
    if y > max_y or x < min_x or x > max_x: return False                                      # free fall
    if rock[y + 1][x] == '.':     return fall_sand(x    , y + 1, rock, min_x, max_x, max_y)   # one down
    if rock[y + 1][x - 1] == '.': return fall_sand(x - 1, y + 1, rock, min_x, max_x, max_y)   # down left
    if rock[y + 1][x + 1] == '.': return fall_sand(x + 1, y + 1, rock, min_x, max_x, max_y)   # down left
    rock[y][x] = 'o'
    return True

snd = 0
while fall_sand(500, 0, rock, min_x, max_x, max_y): snd += 1
print_rock()
print(snd)

### part 2

shapes = [[[int(e) for e in  p.strip().split(',')] for p in ln.split('->')] for ln in open(INPUT_DIR / '1214_sand.txt', 'r').readlines()]
max_x, max_y = max([x for s in shapes for x, _ in s]) + 1, max([y for s in shapes for _, y in s]) + 2
max_x += max_y
rock = [e[:] for e in [['.']*(max_x + 2)]*(max_y + 2)] # rock[y][x] -> height will be the first index
rock[0][500] = '+'  # source
for shape in shapes: 
    px, py, i = shape[0][0], shape[0][1], 1
    rock[py][px] = '#'
    while i < len(shape): 
        x, y = shape[i][0], shape[i][1]
        rock[y][x] = '#'
        for j in range(py, y, 1 if y > py else -1): rock[j][x] = '#'
        for j in range(px, x, 1 if x > px else -1): rock[y][j] = '#'
        px, py, i = x, y, i + 1
for i in range(len(rock[0])): rock[max_y][i] = '#'

def fall_sand2(x, y, rock):
    if rock[y][x] == 'o': return False
    if rock[y + 1][x] == '.':     return fall_sand2(x    , y + 1, rock)   # one down
    if rock[y + 1][x - 1] == '.': return fall_sand2(x - 1, y + 1, rock)   # down left
    if rock[y + 1][x + 1] == '.': return fall_sand2(x + 1, y + 1, rock)   # down left
    rock[y][x] = 'o'
    return True
snd = 0
while fall_sand2(500, 0, rock): snd += 1
print(snd)