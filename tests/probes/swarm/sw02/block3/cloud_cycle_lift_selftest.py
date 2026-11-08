import sys, random, numpy as np
sys.argv = ['selftest', '1', '/nonexistent', '1', 'A4EA7E']
exec(open(sys.argv_file).read().split("if __name__")[0]) if False else None
src = open(sys.argv[0].replace('selftest','cycle_lift') if False else 'cycle_lift.py').read().split('if __name__ == "__main__":')[0]
exec(src)
random.seed(7)
def rule30_tick(cells, centre):
    # cells: list of 0/1 for columns 1..n; centre = column 0; column n+1.. unknown -> only cells 1..n-1 exact
    n = len(cells); out = []
    for i in range(1, n):          # cell i (1-based) -> index i-1; left = cells[i-2] or centre
        left = centre if i == 1 else cells[i-2]
        out.append(left ^ (cells[i-1] | cells[i]))
    return out
bad = 0
for trial in range(3000):
    W = random.randint(1, 40); e = random.randint(0, 3)
    cells = [random.randint(0,1) for _ in range(W)] + [e & 1, (e >> 1) & 1]
    r1 = rule30_tick(cells, 0)          # W+1 exact cells after the white-centre tick
    r2 = rule30_tick(r1, 1)             # W exact cells after the black-centre tick
    direct = sum(b << i for i, b in enumerate(r2))
    x = np.array([sum(b << i for i, b in enumerate(cells[:W]))], dtype=np.uint64)
    mine = int(move(x, e, W)[0])
    bad += (mine != direct)
print("move() vs direct simulator, 3000 random cases W<=40:", "OK" if bad == 0 else f"{bad} mismatches")
# label reader: column 8 over 14 ticks from an odd row, centre white first, against direct simulation with enough cells
bad = 0
for trial in range(2000):
    W = random.randint(21, 40)
    cells = [random.randint(0,1) for _ in range(W)]
    row = cells[:]; word = 0; centre = 0
    for k in range(14):
        word |= row[7] << k                     # column 8 = index 7
        row = rule30_tick(row + [0, 0], centre)  # pad; only the first len-? cells are exact, but column 8 at tick k needs cells <= 8+k <= 21 <= W
        row = row[:len(cells)]                   # keep W cells (the last ones may be inexact but are never read within range)
        centre ^= 1
    x = np.array([sum(b << i for i, b in enumerate(cells))], dtype=np.uint64)
    mine = int(label_words(x, None, W)[0])
    bad += (mine != word)
print("label_words() vs direct simulator, 2000 random cases W in 21..40:", "OK" if bad == 0 else f"{bad} mismatches")
