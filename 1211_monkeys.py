from itertools import product
from math import floor
from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parent / "input"

monkeys = {}
i, lines = 0, open(INPUT_DIR / '1211_monkeys.txt', 'r').readlines()
while i < len(lines):
    monkeys[int(lines[i].strip()[7:-1])] = {
        'activity' : 0, 
        'items' : [int(s) for s in lines[i + 1].strip()[16:].split(", ")],
        'op' : lines[i + 2].strip()[21:],
        'test' : int(lines[i + 3].strip()[19:]),
        'throw' : { 
            True : int(lines[i + 4].strip()[25:]),
            False : int(lines[i + 5].strip()[26:])
        }
    }
    i += 7
#print(monkeys)
for m in [m[1] for _, m in product(range(20), monkeys.items())]:
    for i in m['items']:
        m['activity'] += 1
        if   m['op'] == '* old': i *= i
        elif m['op'].startswith('+'): i += int(m['op'][2:])
        else: i *= int(m['op'][2:])
        i //= 3
        next_m = m['throw'][i%m['test'] == 0]
        monkeys[next_m]['items'].append(i)
    m['items'] = []
(sorted_monkeys := [m[1] for m in monkeys.items()]).sort(key=lambda x: x['activity'], reverse=True)
print(sorted_monkeys[0]['activity']*sorted_monkeys[1]['activity'])

monkeys = {}
i, lines = 0, open(INPUT_DIR / '1211_monkeys.txt', 'r').readlines()
m_mod = 1
while i < len(lines):
    monkeys[int(lines[i].strip()[7:-1])] = {
        'activity' : 0, 
        'items' : [int(s) for s in lines[i + 1].strip()[16:].split(", ")],
        'op' : lines[i + 2].strip()[21:],
        'test' : int(lines[i + 3].strip()[19:]),
        'throw' : { 
            True : int(lines[i + 4].strip()[25:]),
            False : int(lines[i + 5].strip()[26:])
        }
    }
    m_mod *= int(lines[i + 3].strip()[19:])
    i += 7
for m in [m[1] for _, m in product(range(10000), monkeys.items())]:
    for i in m['items']:
        m['activity'] += 1
        if   m['op'] == '* old': i *= i
        elif m['op'].startswith('+'): i += int(m['op'][2:])
        else: i *= int(m['op'][2:])
        i = i % m_mod
        next_m = m['throw'][i%m['test'] == 0]
        monkeys[next_m]['items'].append(i)
    m['items'] = []
(sorted_monkeys := [m[1] for m in monkeys.items()]).sort(key=lambda x: x['activity'], reverse=True)
[print(k,' ',m['activity'], ' ', m['items']) for k, m in monkeys.items()] 
print(sorted_monkeys[0]['activity'],'*',sorted_monkeys[1]['activity'], '=', sorted_monkeys[0]['activity']*sorted_monkeys[1]['activity'])