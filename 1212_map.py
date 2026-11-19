from itertools import product
from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parent / "input"

# 0,0 -> upper left corner, x .. rows down, y .. cols right
map = [[{ 
        'ele' : 99 if s == 'S' else -1 if s == 'E' else ord(s) - ord('a') + 1, 
        'letter' : s, 'dist' : -1, 'prev' : { 'x' : -1, 'y' : -1 }, 'dir' : '.', 
    } for s in line.strip()] for line in open(INPUT_DIR / '1212_map.txt', 'r').readlines()]
dim_x, dim_y, sx, sy, ex, ey = len(map), len(map[1]),  -1, -1, -1, -1  # dimension of the map and location of start and end
max_ele = -1
for x, y in product(range(dim_x), range(dim_y)):
    if map[x][y]['letter'] == 'S': sx, sy = x, y
    elif map[x][y]['letter'] == 'E': ex, ey = x, y
    else: 
        if map[x][y]['ele'] > max_ele: max_ele = map[x][y]['ele']
map[ex][ey]['ele'] = max_ele + 1
shortest_dist = dim_x*dim_y

def discover_E_withPath(x, y, dist, prev_x, prev_y):
    global map, dim_x, dim_y, sx, sy, ex, ey, shortest_dist
    if dist <= shortest_dist and (map[x][y]['dist'] < 0 or dist < map[x][y]['dist']):
       #print(f'map[{x}][{y}]: {map[x][y]["letter"]}/{map[xy"ele"]} {map[x][y]["dist"]}->{dist}')
        map[x][y]['dist'], map[x][y]['prev']['x'], map[x][y]['prev']['y'] = dist, prev_x, prev_y
        if x == ex and y == ey: 
            shortest_dist = dist
            return dist
        tot_dist = -1
        if x > 0 and map[x - 1][y]['ele'] - map[x][y]['ele'] <= 1: 
            tot_dist = discover_E_withPath(x - 1, y, dist + 1, x, y)
        if x < dim_x - 1 and map[x + 1][y]['ele'] - map[x][y]['ele'] <= 1: 
            if (td := discover_E_withPath(x + 1, y, dist + 1, x, y)) >= 0 and (tot_dist < 0 or td < tot_dist): tot_dist = td
        if y > 0 and map[x][y - 1]['ele'] - map[x][y]['ele'] <= 1: 
            if (td := discover_E_withPath(x, y - 1, dist + 1, x, y)) >= 0 and (tot_dist < 0 or td < tot_dist): tot_dist = td
        if y < dim_y -1 and map[x][y + 1]['ele'] - map[x][y]['ele'] <= 1: 
            if (td := discover_E_withPath(x, y + 1, dist + 1, x, y)) >= 0 and (tot_dist < 0 or td < tot_dist): tot_dist = td
        return tot_dist
    return -1

def printPathInMap():
    global map, dim_x, dim_y, sx, sy, ex, ey
    for r in map: 
        for c in r: c['dir'] = '.'
    map[sx][sy]['dir'], map[ex][ey]['dir'] = 'S', 'E'         
    x, y = ex, ey
    while x != sx or y != sy:
        px, py = map[x][y]['prev']['x'], map[x][y]['prev']['y']
        if px == -1 or py == -1: break
        if   px < x: map[px][py]['dir'] = 'v'
        elif px > x: map[px][py]['dir'] = '^'
        elif py < y: map[px][py]['dir'] = '>'
        elif py > y: map[px][py]['dir'] = '<'
        x, y = px, py
    [print('# ', ''.join([c['dir'] for c in r])) for r in map] 

discover_E_withPath(sx, sy, 0, 0, 0)
printPathInMap()
print('Shortest=',shortest_dist)

###############

def discover_a(x, y, dist):
    global map, dim_x, dim_y, sx, sy, ex, ey, shortest_dist
    if dist <= shortest_dist and (map[x][y]['dist'] < 0 or dist < map[x][y]['dist']):
        map[x][y]['dist'] = dist
        if map[x][y]['letter'] == 'a': 
            shortest_dist = dist
            return dist
        tot_dist = -1
        if x > 0 and map[x - 1][y]['ele'] - map[x][y]['ele'] >= -1: 
            tot_dist = discover_a(x - 1, y, dist + 1)
        if x < dim_x - 1 and map[x + 1][y]['ele'] - map[x][y]['ele'] >= -1: 
            if (td := discover_a(x + 1, y, dist + 1)) >= 0 and (tot_dist < 0 or td < tot_dist): tot_dist = td
        if y > 0 and map[x][y - 1]['ele'] - map[x][y]['ele'] >= -1: 
            if (td := discover_a(x, y - 1, dist + 1)) >= 0 and (tot_dist < 0 or td < tot_dist): tot_dist = td
        if y < dim_y -1 and map[x][y + 1]['ele'] - map[x][y]['ele'] >= -1: 
            if (td := discover_a(x, y + 1, dist + 1)) >= 0 and (tot_dist < 0 or td < tot_dist): tot_dist = td
        return tot_dist
    return -1

shortest_dist = dim_x*dim_y
for x, y in product(range(dim_x), range(dim_y)): map[x][y]['dist'] = -1
discover_a(ex, ey, 0)
print('Shortest from a=',shortest_dist)
