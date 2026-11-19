from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parent / "input"

max, s  = [0, 0, 0, 0], 0
for line in open(INPUT_DIR / '1201_food.txt', 'r').readlines():
    if (line.strip() == ''):
        if s > max[0]: 
            max[0] = s
            max.sort()
        s = 0
    else: s += int(line)
if s > max[0]:
    max[0] = s
    max.sort()
print(max[1:], sum(max[1:])) # get top 3 sums of parts divided by empty lines + sum of top 3
