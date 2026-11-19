from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parent / "input"

c_no, x, sig_stren, check_cycle = 0, 1, 0, lambda c, x: c*x if (c - 20)%40 == 0 else 0
for instr in [line.strip() for line in open(INPUT_DIR / '1210_display.txt', 'r').readlines()]:
    c_no += 1
    sig_stren += check_cycle(c_no, x)
    if instr.startswith('addx'):
        c_no += 1
        sig_stren += check_cycle(c_no, x)
        x += int(instr.split(' ')[1])
    if (c_no >= 220): break
print(sig_stren)

c_no, x = 0, 1
for instr in [line.strip() for line in open(INPUT_DIR / '1210_display.txt', 'r').readlines()]:
    print('#' if abs(c_no - x) < 2 else '.', end='') 
    if c_no < 39: c_no += 1
    else: 
        print()
        c_no = 0
    if instr.startswith('addx'):
        print('#' if abs(c_no - x) < 2 else '.', end='') 
        if c_no < 39: c_no += 1
        else: 
            print()
            c_no = 0  
        x += int(instr.split(' ')[1])