from collections import deque
from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parent / "input"

stacks = {}
for line in open(INPUT_DIR / '1205_stacks.txt', 'r').readlines():
    if line.find('[') != -1:
        i, k = 1, 1
        while k <= len(line):
            if (line[k] != ' '): 
                try: stacks[i].appendleft(line[k])
                except KeyError: stacks[i] = deque(line[k])
            i, k = i + 1, k + 4
    elif line.startswith('move'):
        n, f, t = [int(s) for s in str.split(line) if s.isdigit()]
        [stacks[t].append(stacks[f].pop()) for _ in range(0, n)]
print(''.join([stacks[s].pop() for s in sorted(stacks.keys())]))
#GFTNRBZPF

stacks = {}
for line in open(INPUT_DIR / '1205_stacks.txt', 'r').readlines():
    if line.find('[') != -1:
        i, k = 1, 1
        while k <= len(line):
            if (line[k] != ' '): 
                try: stacks[i].appendleft(line[k])
                except KeyError: stacks[i] = deque(line[k])
            i, k = i + 1, k + 4
    elif line.startswith('move'):
        n, f, t = [int(s) for s in str.split(line) if s.isdigit()]
        crane = deque()
        [crane.append(stacks[f].pop()) for _ in range(0, n)]
        [stacks[t].append(crane.pop()) for _ in range(0, n)]
print(''.join([stacks[s].pop() for s in sorted(stacks.keys())]))
#VRQWPDSGP