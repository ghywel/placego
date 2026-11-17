#!/usr/bin/env python3
"""crystal_orbit.py TABLE KMAX: the crystal's writing law run beyond the data (inquisition round 14, fourth block; Cloud, CL694).
From the last two wheel words of the certificate table, run the recurrence F alone: with parents u (nearer) and w (farther) in
cycles of a common period p, the next wheel's cycle is the unique p-periodic solution of d(t+1) = w(t) ^ (u(t) | d(t)) when u has a
black; when u is all white the next cycle is an integral of w: two solutions of period p if w's weight over its least period is even,
two antiperiodic solutions of period 2p if odd. Every all-white word is a branch point (the seed's bit is not known here), so all
branches are followed, with their periods. Reports each branch's white wheels, the weight of w there, and the period after.
CL680's independent census says the seed's white wheels beyond 12,000 are 53,207 (weight 6), 58,286 (10), 87,866 (5, period 32)."""
import sys
table, KMAX = sys.argv[1], int(sys.argv[2])
words = [l.strip() for l in open(table) if l and not l.startswith('#')]
K0 = len(words)
def lift(c, p):            # repeat a cycle to length p
    return tuple(c[i % len(c)] for i in range(p))
def least_period(c):
    for pp in range(1, len(c) + 1):
        if len(c) % pp == 0 and all(c[i] == c[(i + pp) % len(c)] for i in range(len(c))): return pp
def reduce(c): return c[:least_period(c)]
def F(u, w):
    p = max(len(u), len(w)); u = lift(u, p); w = lift(w, p)
    if any(u):
        r0 = u.index(1); d = [None] * p; d[(r0 + 1) % p] = 1 - w[r0]; r = (r0 + 1) % p
        for _ in range(2 * p):
            nr = (r + 1) % p; d[nr] = w[r] ^ (u[r] | d[r]); r = nr
        return [tuple(d)], None
    pw = least_period(w); par = sum(w[:pw]) % 2
    d0 = [0] * (2 * p if par else p)
    for i in range(len(d0) - 1): d0[i + 1] = d0[i] ^ w[i % p]
    d1 = [1 - x for x in d0]
    return [tuple(d0), tuple(d1)], (pw, par)
def c_of(s): return tuple(int(ch) for ch in s)
start = (reduce(c_of(words[K0 - 2])), reduce(c_of(words[K0 - 1])))
branches = [(start, [], 'seed', K0)]    # (state (w, u) as reduced cycles, events, name, next wheel index k)
done = []
while branches:
    (w, u), events, name, k = branches.pop(0)
    while k < KMAX:
        outs, info = F(u, w)
        if info is None:
            d = outs[0]; w, u = u, reduce(d); k += 1
            continue
        pw, par = info
        ev = (k - 1, pw, sum(w[:pw]), 'odd' if par else 'even', len(reduce(outs[0])))
        if len(events) >= 3:
            done.append((name, events + [ev], 'stopped at 3 branch points')); break
        for i, d in enumerate(outs):
            branches.append(((u, reduce(d)), events + [ev], name + f'.{i}', k + 1))
        k = None; break
    if k is not None and k >= KMAX: done.append((name, events, f'reached {KMAX}'))
print(f"table {table}: {K0} wheels; started from wheels {K0-2}, {K0-1} (periods {len(start[0])}, {len(start[1])}); followed to KMAX={KMAX}")
for name, events, how in done:
    print(f"  branch {name:10s}: white wheels (wheel, least period of w, weight of w over it, parity, period after) = {events}; {how}")
print("CRYSTAL_ORBIT_DONE")
