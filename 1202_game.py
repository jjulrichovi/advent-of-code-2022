from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parent / "input"

# A or X for Rock, B or Y for Paper, and C or Z for Scissors
sum_score  = 0
print(sum([{
    'A X' : 1 + 3,
    'A Y' : 2 + 6,
    'A Z' : 3 + 0,

    'B X' : 1 + 0,
    'B Y' : 2 + 3,
    'B Z' : 3 + 6,

    'C X' : 1 + 6,
    'C Y' : 2 + 0,
    'C Z' : 3 + 3                               
    }[line.strip()] for line in open(INPUT_DIR / '1202_game.txt', 'r').readlines()]),'\n')

# A for Rock, B for Paper, and C for Scissors
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
sum_score  = 0
print(sum([{
    'A X' : 3 + 0,
    'A Y' : 1 + 3,
    'A Z' : 2 + 6,

    'B X' : 1 + 0,
    'B Y' : 2 + 3,
    'B Z' : 3 + 6,

    'C X' : 2 + 0,
    'C Y' : 3 + 3,
    'C Z' : 1 + 6                               
    }[line.strip()] for line in open(INPUT_DIR / '1202_game.txt', 'r').readlines()]),'\n')

