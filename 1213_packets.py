from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
INPUT_DIR = ROOT_DIR / "input"

f = open(ROOT_DIR / "temp_packets_py.py", 'w')
f.write("packet_pairs = [")
lines, i = open(INPUT_DIR / '1213_packets.txt', 'r').readlines(), 0
while i < len(lines):
  l, r = lines[i].strip(), lines[i+1].strip()
  f.write(f"\n  {{ 'L' : {l} ,\n    'R' : {r}  }},")    
  i += 3
f.write(" ]\n")
f.close()

from temp_packets_py import packet_pairs

def compare_packets(l,r):
  # print(f"  L({type(l)})={l}, R({type(r)})={r}")
  if type(l) == int and type(r) == int: return -1 if l < r else 1 if l > r else 0
  elif type(l) == list and type(r) == list:
    il, ir = 0, 0
    while il < len(l) and ir < len(r):
      if (cmp := compare_packets(l[il], r[ir])) != 0: return cmp
      il += 1
      ir += 1
    return -1 if len(l) < len(r) else 1 if len(l) > len(r) else 0
  else: return compare_packets(l if type(l) == list else [l], r if type(r) == list else [r])  

i, s = 1, 0
for l, r in [(p['L'], p['R']) for p in packet_pairs]:
  if compare_packets(l, r) == -1: s += i
  i += 1
print(s)

import functools
packets = [key1:=[[2]], key2:=[[6]]]
for p in packet_pairs:
  packets.append(p['L'])
  packets.append(p['R'])
sorted_packets = sorted(packets, key=functools.cmp_to_key(compare_packets))
i=0
while i < len(sorted_packets):
  p = sorted_packets[i]
  i += 1
  if p == key1: decode_key = i
  elif p == key2:
    decode_key *= i
    break
print(decode_key)
