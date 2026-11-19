from itertools import product
from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parent / "input"

forest = [[int(c) for c in line.strip()] for line in open(INPUT_DIR / '1208_trees.txt', 'r').readlines()]
n, visible_cnt = len(forest), 4*len(forest) - 4
for i, j in product(range(1, n - 1), range(1, n - 1)):
    
    tree, v = forest[i][j], False
    if abs(tree) > forest[i][0]: v, forest[i][0] = True, abs(tree)
    if abs(tree) > forest[0][j]: v, forest[0][j] = True, abs(tree)
    if v and tree >= 0: visible_cnt, forest[i][j] = visible_cnt + 1, -tree
    
    tree, v = forest[n - 1 - i][n - 1 - j], False
    if abs(tree) > forest[n - 1 - i][n - 1]: v, forest[n - 1 - i][n - 1] = True, abs(tree)
    if abs(tree) > forest[n - 1][n - 1 - j]: v, forest[n - 1][n - 1 - j] = True, abs(tree)
    if v and tree >= 0:  visible_cnt, forest[n - 1 - i][n - 1 - j] = visible_cnt + 1, -tree

print(visible_cnt)   


forest = [[int(c) for c in line.strip()] for line in open(INPUT_DIR / '1208_trees.txt', 'r').readlines()]
n, max_score = len(forest), 0
for i, j in product(range(0, n), range(0, n)):
    tree, view_top, view_left, view_down, view_right = forest[i][j], 0, 0, 0, 0 
    
    x = i - 1
    while x >= 0:
        view_top += 1
        if forest[x][j] >= tree: break
        x -= 1
    
    x = j - 1
    while x >= 0:
        view_left += 1
        if forest[i][x] >= tree: break
        x -= 1

    x = i + 1
    while x < n:
        view_down += 1
        if forest[x][j] >= tree: break
        x += 1

    x = j + 1
    while x < n:
        view_right += 1
        if forest[i][x] >= tree: break
        x += 1

    score = view_top*view_left*view_down*view_right
    if score > max_score: max_score = score

print(max_score)
