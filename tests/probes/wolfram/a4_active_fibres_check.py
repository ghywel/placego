#!/usr/bin/env python3
"""L1479 (Local, 2026-11-03): exhaustive checks of GC2594's finite hand steps (GPT-ACTIVE-INPUT-FIBRES-20261103.md).
Run: python3 tests/probes/wolfram/a4_active_fibres_check.py
1. The one-step table of the adjacent rays: v' = c xor (u or v), h' = u xor (v or h), against GC2594's printed table.
2. The two-tick reset: (c_s, u_s) = (0, 1) sends all four (v_s, h_s) to (not c_{s+1}, not u_{s+1}) at s + 2.
3. The seven-cell counterexample 1,0,0,1,z,1,0 on q-4..q+2, by direct Rule 30 steps.
4. The derivative/reset law on whole rows: for every initial word of width 2T+1 on [q-2T, q], the cell (T, q-T) equals
   A xor (z and G), with A the value at z = 0 and G = AND over s < T of NOT X(s, q-s-1). T <= 6, all 2^(2T+1) words.
5. The 0/1/2 elimination: exists z with b = A xor (z and G) iff G or A == b, over all eight (A, G, b).
Prints counts and PASS/FAIL only.
"""
from itertools import product

rule = lambda a, b, c: a ^ (b | c)
ok = True


def report(name, cond):
    global ok
    ok &= cond
    print('%s: %s' % (name, 'PASS' if cond else 'FAIL'))


# 1. GC2594's table: rows (c,u), columns (v,h) in the order 00, 01, 10, 11, entries v'h'.
table = {(0, 0): ['00', '01', '11', '11'], (0, 1): ['11', '10', '10', '10'],
         (1, 0): ['10', '11', '01', '01'], (1, 1): ['01', '00', '00', '00']}
step = lambda c, u, v, h: (c ^ (u | v), u ^ (v | h))
report('1. one-step table (16 entries)', all('%d%d' % step(c, u, v, h) == table[(c, u)][2 * v + h]
                                              for c, u, v, h in product((0, 1), repeat=4)))

# 2. two-tick reset, over all (v_s, h_s) and all (c_{s+1}, u_{s+1}).
report('2. two-tick reset (16 cases)', all(step(c1, u1, *step(0, 1, v, h)) == (1 - c1, 1 - u1)
                                           for v, h, c1, u1 in product((0, 1), repeat=4)))


def evolve(row, steps):
    """row: dict position -> bit on a contiguous interval; returns the list of rows, each shrinking by one cell a side."""
    rows = [row]
    for _ in range(steps):
        r = rows[-1]; lo, hi = min(r), max(r)
        rows.append({x: rule(r[x - 1], r[x], r[x + 1]) for x in range(lo + 1, hi)})
    return rows


# 3. seven-cell counterexample, q = 0.
res = []
for z in (0, 1):
    rows = evolve(dict(zip(range(-4, 3), [1, 0, 0, 1, z, 1, 0])), 3)
    res.append(([rows[1][x] for x in range(-3, 2)], [rows[2][x] for x in range(-2, 1)], rows[3][-1]))
c3 = all(res[z] == ([1, 1, 1, 0, 1 - z], [0, 0, z], z) for z in (0, 1))
# the read path retreat, stay, stay: positions q, q-1, q-1, q-1 at t = 0..3, right labels t + p = q, q, q+1, q+2
c3 &= [t + p for t, p in enumerate([0, -1, -1, -1])] == [0, 0, 1, 2]
report('3. seven-cell counterexample (pair (q, q+1) rays 00 at t = 2 for both z; X(3, q-1) = z)', c3)

# 4. derivative/reset law on whole rows.
n4 = 0; c4 = True
for T in range(1, 7):
    for bits in product((0, 1), repeat=2 * T):
        vals = {}
        for z in (0, 1):
            rows = evolve(dict(zip(range(-2 * T, 1), list(bits) + [z])), T)
            vals[z] = rows
        A = vals[0][T][-T]
        G = int(all(vals[0][s][-s - 1] == 0 for s in range(T)))
        c4 &= all(vals[z][T][-T] == A ^ (z & G) for z in (0, 1))
        # the masking cells do not depend on z
        c4 &= all(vals[0][s][-s - 1] == vals[1][s][-s - 1] for s in range(T))
        n4 += 1
report('4. derivative/reset law, T = 1..6 (%d older words)' % n4, c4)

# 5. elimination.
report('5. 0/1/2 elimination (8 cases)', all((any(b == A ^ (z & G) for z in (0, 1)) == bool(G or A == b)) and
                                             (sum(b == A ^ (z & G) for z in (0, 1)) == (1 if G else (2 if A == b else 0)))
                                             for A, G, b in product((0, 1), repeat=3)))
print('ALL PASS' if ok else 'SOME FAIL')
