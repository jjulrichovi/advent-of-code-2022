import re
from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parent / "input"

sum_incl, sum_overlap = 0, 0
for line in open(INPUT_DIR / '1204_overlap.txt', 'r').readlines():
    lo1, hi1, lo2, hi2 = [int(s) for s in re.split("-|,", line.strip())]
    if lo1 >= lo2 and hi1 <= hi2 or lo2 >= lo1 and hi2 <= hi1:
        sum_incl += 1
    if lo2 <= lo1 <= hi2 or lo2 <= hi1 <= hi2 or lo1 <= lo2 <= hi1 or lo1 <= hi2 <= hi1:   
        sum_overlap += 1
print(sum_incl, ' ', sum_overlap)
