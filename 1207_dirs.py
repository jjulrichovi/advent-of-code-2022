import re
from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parent / "input"

def read_dir():
    global lines, i, sumTo100k
    size, nam = 0, lines[i]
    i += 2 # skip cd and ls
    while i < len(lines):
        lin = lines[i].strip()
        if lin[:3] == 'dir': 
            i += 1
            continue
        elif lin == '$ cd ..': 
            i += 1
            break
        elif lin[:4] == '$ cd':
            size += read_dir()
        else:
            size += int(re.split(" ", lin)[0])
            i += 1
    print(nam, ' ', size)
    if size <= 100000: sumTo100k += size
    return size

def read_dir2():
    global lines, i, needed, to_be_freed
    size = 0    
    i += 2 # skip cd and ls
    while i < len(lines):
        lin = lines[i].strip()
        if lin[:3] == 'dir': 
            i += 1
            continue
        elif lin == '$ cd ..': 
            i += 1
            break
        elif lin[:4] == '$ cd':
            size += read_dir2()
        else:
            size += int(re.split(" ", lin)[0])
            i += 1
    if size >= needed and size < to_be_freed: to_be_freed = size
    return size

lines, i, sumTo100k = open(INPUT_DIR / '1207_dirs.txt', 'r').readlines(), 0, 0
tot_size = read_dir()
print('Sum of sizes of dirs no bigger than 100000 ', sumTo100k)
needed, to_be_freed, i = 30000000 - (70000000 - tot_size), tot_size, 0
read_dir2()
print('Total size  ', tot_size)
print('Needed      ', needed)
print('To be freed ', to_be_freed)