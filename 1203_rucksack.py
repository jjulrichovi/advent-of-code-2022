from itertools import product
from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parent / "input"

def prio(x):
    if ord('a') <= ord(x) <= ord('z'): return ord(x) - ord('a') + 1
    if ord('A') <= ord(x) <= ord('Z'): return ord(x) - ord('A') + 27
s = 0
for line in open(INPUT_DIR / '1203_rucksack.txt', 'r').readlines():
    m = int(len(line)/2)
    for a, b in product(line[m:], line[:m]):
        if a == b:
            s += prio(a)
            break
print(s)

from numpy import array_split
s = 0
lines = open(INPUT_DIR / '1203_rucksack.txt', 'r').readlines()
for s1, s2, s3 in array_split(lines, len(lines)/3):
    for a, b, c in product(s1, s2, s3):
        if a == b == c: 
            s += prio(a)
            break
print(s)


