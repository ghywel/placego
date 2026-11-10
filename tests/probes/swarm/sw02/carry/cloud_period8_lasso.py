# Carry for GC2826, door 1 (Cloud, CL764): the period-8 right half driven by 0001 (PE-2.3), as an explicit spatial lasso from
# the column pair (136, 14). Columns are 8-bit words, bit t = the cell at tick t mod 8; column 0 = 136 is the driver 0001 0001,
# column 1 = 14 is 0111 0000. Rule 30 across three adjacent columns a, b, c: b(t+1) = a(t) xor (b(t) or c(t)).
# Own code: alive pairs by pruning, a walk to a repeat, then every edge re-checked cell by cell with the scalar rule.
P = 8; M = (1 << P) - 1
bit = lambda w, t: (w >> (t % P)) & 1
def succs(a, b):
    out = []
    for c in range(1 << P):
        if all(bit(b, t + 1) == (bit(a, t) ^ (bit(b, t) | bit(c, t))) for t in range(P)): out.append(c)
    return out
S = {}
for a in range(1 << P):
    for b in range(1 << P):
        s = succs(a, b)
        if s: S[(a, b)] = s
alive = set(S)
while True:
    dead = {v for v in alive if not any((v[1], c) in alive for c in S[v])}
    if not dead: break
    alive -= dead
start = (136, 14); assert start in alive
# every alive continuation from the start: follow, recording choices
path = [start]; seen = {start: 0}; branch = 0
while True:
    a, b = path[-1]; nxt = [(b, c) for c in S[(a, b)] if (b, c) in alive]
    branch = max(branch, len(nxt)); v = nxt[0]
    if v in seen: loop_from = seen[v]; break
    seen[v] = len(path); path.append(v)
cols = [path[0][0]] + [p[1] for p in path]          # columns 0,1,2,...
tail, cyc = loop_from, len(path) - loop_from
print(f"alive pairs {len(alive)}; walk from (136, 14): {len(path)} pairs, preperiod {tail}, spatial period {cyc}, most alive choices at a step {branch}")
# independent scalar re-check of every edge, including the closing edge
closing = path[loop_from][1]
full = cols + [closing]; bad = 0; checks = 0
for i in range(1, len(full) - 1):
    a, b, c = full[i - 1], full[i], full[i + 1]
    for t in range(P):
        checks += 1
        if ((b >> ((t + 1) % P)) & 1) != (((a >> t) & 1) ^ (((b >> t) & 1) | ((c >> t) & 1))): bad += 1
assert full[-2:] == [cols[loop_from], cols[loop_from + 1]] or (full[-2], full[-1]) == path[loop_from]
def least_period(w): return next(p for p in (1, 2, 4, 8) if all(bit(w, t) == bit(w, t + p) for t in range(P)))
print(f"scalar edge checks {checks}, failures {bad}; column 0 = {cols[0]:08b} (bit 7 first), least period {least_period(cols[0])}; column 1 = {cols[1]:08b}, least period {least_period(cols[1])}")
print("least periods of columns 1..:", sorted(set(least_period(w) for w in cols[1:])))
# the eight-tick step: a word of least period 8 cannot agree with any 4-periodic word on eight consecutive ticks
viol = sum(1 for y in range(16) for s in range(8) if all(bit(cols[1], s + k) == ((y >> ((s + k) % 4)) & 1) for k in range(8)))
print("4-periodic words agreeing with column 1 on eight consecutive ticks:", viol)
# mutation control: flip one cell of one column of the lasso; some edge must fail
mut = full[:]; mut[5] ^= 1; mb = 0
for i in range(1, len(mut) - 1):
    a, b, c = mut[i - 1], mut[i], mut[i + 1]
    mb += sum(1 for t in range(P) if ((b >> ((t + 1) % P)) & 1) != (((a >> t) & 1) ^ (((b >> t) & 1) | ((c >> t) & 1))))
print("mutation control (one cell flipped): failing edge checks", mb)
print("columns 0..%d (decimal, bit t = tick t):" % (len(cols) - 1), cols)
print("closing column:", closing, "= column", loop_from + 1)
