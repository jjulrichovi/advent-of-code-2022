from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parent / "input"

vals, exprs = {}, {}  # variable and expressions
for line in open(INPUT_DIR / '1221_yelling.txt', 'r').readlines():
    line = line.strip()
    if len(line) < 17: vals[line[:4]] = int(line[6:])
    else: exprs[line[:4]] = {'o' : line[11:12], 'L' : line[6:10], 'R' : line[13:] }
while len(exprs) > 0:
    for v, e in exprs.items():
        try:
            o, l, r = e['o'], vals[e['L']], vals[e['R']]
            vals[v]=l+r if o=='+' else l-r if o=='-' else l*r if o=='*' else l/r;
            exprs.pop(v)
            break  # cannot change the dict during interration
        except KeyError: continue
print('root: ', int(vals['root'])) # 38914458159166

vals, exprs = {}, {}
for line in open(INPUT_DIR / '1221_yelling.txt', 'r').readlines():
    line = line.strip()
    if   line.startswith('root'): eq1, eq2 = line[6:10], line[13:]; continue
    elif line.startswith('humn'): continue  # skip the human for now 
    elif len(line) < 17: vals[line[:4]] = int(line[6:])
    else: exprs[line[:4]] = {'o' : line[11:12], 'L' : line[6:10], 'R' : line[13:] }
changed = True
while changed > 0:
    changed = False
    for v, e in exprs.items():
        try:
            o, l, r = e['o'], vals[e['L']], vals[e['R']]
            vals[v] = l + r if o == '+' else l - r if o == '-' else l*r if o == '*' else l/r;
            exprs.pop(v)
            changed = True
            break  # cannot change the dict during interration
        except KeyError: continue
if   eq1 in vals.keys(): print(f"Found eq1 {eq1}: {vals[eq1]} -> start from {eq2}"); target, vals[eq2] = eq2, vals[eq1]
elif eq2 in vals.keys(): print(f"Found eq2 {eq2}: {vals[eq2]} -> start from {eq1}"); target, vals[eq1] = eq1, vals[eq2]
else: print('ERROR 1') ; exit()
while True:
    e, v = exprs[target], vals[target]
    o, ln, rn = e['o'], e['L'], e['R']
    if   ln in vals.keys():
        l = vals[ln]
        r = v-l if o=='+' else l-v if o=='-' else v/l if o=='*' else l/v  # v = l op r
        vals[rn], target = r, rn
    elif rn in vals.keys():
        r = vals[rn]
        l = v-r if o=='+' else v+r if o=='-' else v/r if o=='*' else v*r  # v = l op r
        vals[ln], target = l, ln
    else: print('ERROR 2') ; exit()
    if target == 'humn': break
print('humn: ', vals['humn'])
