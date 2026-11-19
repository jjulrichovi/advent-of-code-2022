from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parent / "input"

def snafu2dec(snafu):
    dec, p = 0, 1
    for s in snafu[::-1]:
        dec += 2*p if s == '2' else 1*p if s == '1' else -1*p if s == '-' else -2*p if s == '=' else 0 
        p *= 5
    return dec

def dec2snafu(dec):
    snafu = []
    # convert to base 5
    p = 5
    while dec > p*5: p *= 5
    while dec >= 5 and p > 1:
        snafu.append(dec//p)
        dec -= (dec//p)*p
        p //= 5
    snafu.append(dec)
    # from base 5 to snafu
    i = len(snafu) - 1
    while i >= 0:
        if (snafu[i] > 2):
            snafu[i] -= 5
            if i == 0: snafu.insert(0, 1)
            else: snafu[i - 1] += 1
        i -= 1
    return ''.join(['2' if i == 2 else '1' if i == 1 else '-' if i == -1 else '=' if i == -2 else '0' for i in snafu])

print(i := 1, '->', dec2snafu(i), ' 1')
print(i := 2, '->', dec2snafu(i), ' 2')
print(i := 3, '->', dec2snafu(i), ' 1=')
print(i := 4, '->', dec2snafu(i), ' 1-')
print(i := 5, '->', dec2snafu(i), ' 10')
print(i := 6, '->', dec2snafu(i), ' 11')
print(i := 7, '->', dec2snafu(i), ' 12')
print(i := 8, '->', dec2snafu(i), ' 2=')
print(i := 9, '->', dec2snafu(i), ' 2-')
print(i := 10, '->', dec2snafu(i), ' 20')
print(i := 15, '->', dec2snafu(i), ' 1=0')
print(i := 20, '->', dec2snafu(i), ' 1-0')
print(i := 2022, '->', dec2snafu(i), ' 1=11-2')
print(i := 12345, '->', dec2snafu(i), ' 1-0---0')
print(i := 314159265, '->', dec2snafu(i), ' 1121-1110-1=0')

print(dec2snafu(sum([ snafu2dec(ln.strip()) for ln in open(INPUT_DIR / '1225_snafu.txt', 'r').readlines()])))