#!/usr/bin/env python3
"""Search A (|A| = n, max A <= X) for the worst interval position; report max_I g(A, I).
usage: search.py n X tlim [cap_configs] [minmax]
Pruning: a configuration is solved exactly only if its greedy cover exceeds the best value found so far
for this A (min <= greedy). Sets with sum omega(a) <= current global best are skipped (Hall bound, see notes).
"""
import itertools, sys, time
sys.path.insert(0, '.')
import g708
from g708 import factor, demands, patterns, min_cover

n = int(sys.argv[1]); X = int(sys.argv[2]); TL = float(sys.argv[3])
CAP = int(sys.argv[4]) if len(sys.argv) > 4 else 200000
MINMAX = int(sys.argv[5]) if len(sys.argv) > 5 else n
T0 = time.time()


def greedy(dem, elems):
    rem = list(dem); g = 0; P = len(dem); used = set()
    while any(rem):
        best, bi = 0, -1
        for i, e in enumerate(elems):
            if i in used:
                continue
            s = 0
            for k in range(P):
                if rem[k] and e[k]:
                    s += min(e[k], rem[k])
            if s > best:
                best, bi = s, i
        used.add(bi); g += 1
        for k in range(P):
            rem[k] = max(0, rem[k] - elems[bi][k])
    return g


def worst(A, floor):
    """max over configs of min|B|, but only resolved exactly when it can exceed `floor`."""
    M = max(A); e = demands(A); primes = sorted(e)
    dem = tuple(e[p] for p in primes)
    per = [list(patterns(p, e[p], M).items()) for p in primes]
    tot = 1
    for x in per:
        tot *= len(x)
    if tot > CAP:
        return None, None, tot
    best, wit = floor, None
    for combo in itertools.product(*per):
        elems = [tuple(combo[k][0][j] for k in range(len(primes))) for j in range(M)]
        elems = [x for x in elems if any(x)]
        if greedy(dem, elems) <= best:
            continue
        v = min_cover(dem, elems)
        if v > best:
            best, wit = v, tuple((primes[k], combo[k][1]) for k in range(len(primes)))
        if time.time() - T0 > TL:
            raise TimeoutError
    return best, wit, tot


gbest = MINMAX - 1
records = []
skipped_cap = 0
checked = 0
try:
    for top in range(n + 1, X + 1):
        for rest in itertools.combinations(range(2, top), n - 1):
            A = list(rest) + [top]
            om = sum(len(factor(a)) for a in A)
            if om <= gbest:  # Hall bound: worst <= sum omega
                continue
            v, w, tot = worst(A, gbest)
            if v is None:
                skipped_cap += 1
                continue
            checked += 1
            if w is not None and v > gbest:
                gbest = v
                records.append((v, A, w, tot))
                print('NEW BEST n=%d: %d  A=%s  witness=%s configs=%d  t=%.0fs' % (n, v, A, w, tot, time.time() - T0), flush=True)
            elif w is not None and v == gbest:
                print('  tie %d: A=%s witness=%s' % (v, A, w), flush=True)
        print('done max<=%d  best=%d checked=%d skipped_cap=%d t=%.0fs' % (top, gbest, checked, skipped_cap, time.time() - T0), flush=True)
except TimeoutError:
    print('TIMEOUT at top=%d best=%d' % (top, gbest), flush=True)
print('FINAL n=%d X=%d best=%d records=%s' % (n, X, gbest, records), flush=True)
