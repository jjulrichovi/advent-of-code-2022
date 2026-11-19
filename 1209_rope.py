from itertools import chain
from itertools import product
from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parent / "input"

# Possible positions of tail of the rope before head moveL: all "." plus also "H" (same position as head)
# . . .
# . H .
# . . .
# logic: start at (x=0,y=0), logic like standard x,y axes in math

hx, hy, tx, ty = 0, 0, 0, 0
tail_positions = set()
tail_positions.add('{}_{}'.format(tx, ty))
for direction in chain.from_iterable([[direction] * int(distance) for direction, distance in [line.strip().split(' ') for line in open(INPUT_DIR / '1209_rope.txt', 'r').readlines()]]):
    if   direction == "U": hy += 1
    elif direction == "D": hy -= 1
    elif direction == "R": hx += 1
    elif direction == "L": hx -= 1
    # head cannot make diagonal move (=> max 1 dimension can differ by 2)
    if   hy - ty == 2: tx, ty = tx + (hx - tx), ty + 1
    elif ty - hy == 2: tx, ty = tx + (hx - tx), ty - 1
    if   hx - tx == 2: tx, ty = tx + 1, ty + (hy - ty)
    elif tx - hx == 2: tx, ty = tx - 1, ty + (hy - ty)
    #print("H[{},{}] T[{},{}]".format(hx, hy, tx, ty))
    tail_positions.add('{}_{}'.format(tx, ty))
print(len(tail_positions))


from numpy import zeros
from numpy import sign
def rope_tail_pos_cnt(rope_len, txt_file):
    rope = zeros((rope_len,2))
    tail_positions = set()
    tail_positions.add('{}_{}'.format(rope[rope_len - 1][0], rope[rope_len - 1][1]))
    for direction in chain.from_iterable([[direction] * int(distance) for direction, distance in [line.strip().split(' ') for line in open(INPUT_DIR / txt_file, 'r').readlines()]]):
        if   direction == "U": rope[0][1] += 1
        elif direction == "D": rope[0][1] -= 1
        elif direction == "R": rope[0][0] += 1
        elif direction == "L": rope[0][0] -= 1    
        for n in range(1, rope_len):
            # knot behind the head can make diagonal move -> both dimensions may differ by 2 (if next node touches diagonal)
            if abs(rope[n - 1][0] - rope[n][0]) > 1 or abs(rope[n - 1][1] - rope[n][1]) > 1:
                rope[n][0] += sign(rope[n - 1][0] - rope[n][0])
                rope[n][1] += sign(rope[n - 1][1] - rope[n][1])
        tail_positions.add('{}_{}'.format(rope[rope_len - 1][0], rope[rope_len - 1][1]))
    return len(tail_positions)
print(rope_tail_pos_cnt(2, '1209_rope.txt'))
print(rope_tail_pos_cnt(10, '1209_rope.txt'))
