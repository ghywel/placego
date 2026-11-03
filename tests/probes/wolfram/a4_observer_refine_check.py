#!/usr/bin/env python3
"""L1491 (Local, 2026-11-03): bounded self-checks of GC2607's retreat refinement, from an implementation written here from the
register meanings (p0 = X(t+1, B), p1 = X(t+1, B+1), c = X(t, B+1); GC2571, GC2577), not GPT's probe.
Run: python3 tests/probes/wolfram/a4_observer_refine_check.py TRIALS STEPS SEED
A. Physical soundness: random rows, W = 6 strips and random motions in {0, -1}. In both modes (literal, enriched) and both
   versions (original, refined): no rejection, every known register true, at most one pending register. Also the remark:
   old p1 = 1 with c' unknown gives r = not b' truly.
B. Information order on abstract paths (random labels drive the cell beyond the strip; not physical): whenever the refined
   observer accepts, the original accepts and refined memory extends original memory, componentwise. Counts strict rejections.
C. The tableau: initial 111011 on [x, x+5] forces X(4, x+4) = 1 for all eight exteriors; rows as in GC2607.
Prints counts and PASS/FAIL only.
"""
import random
import sys
from itertools import product

TR, ST, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rnd = random.Random(SEED)
rule = lambda a, b, c: a ^ (b | c)
W = 6
ok = True


def report(name, cond):
    global ok
    ok &= bool(cond)
    print('%s: %s' % (name, 'PASS' if cond else 'FAIL'))


def join(u, v):
    """Returns (value, conflict)."""
    if u is None:
        return v, False
    if v is None or u == v:
        return u, False
    return None, True


def a10(s, i):
    """The a10 forecast of the triple ending at strip index i: (v, 1, 0) gives v."""
    return s[i - 2] if s[i - 1] == 1 and s[i] == 0 else None


def update(mem, strip, nxt_last, mv, active, label, literal, refined):
    p0, p1, c = mem
    if c is not None and active and label != c:
        return None
    kc = c if (c is not None or literal) else (label if active else None)
    a, b = strip[-2], strip[-1]
    gm1, g0 = a10(strip, len(strip) - 2), a10(strip, len(strip) - 1)
    g1 = a if (b == 1 and kc == 0) else None
    if mv == 0:
        q = (1 - b) if kc == 1 else None
        cc, bad = join(p1, q)
        return None if bad else (g0, g1, cc)
    q = (1 - a) if b == 1 else ((a ^ kc) if kc is not None else None)
    cc, bad = join(p0, q)
    if bad:
        return None
    n0, n1 = gm1, g0
    if refined and n0 is None:
        r = (1 - nxt_last) if cc == 1 else ((nxt_last ^ p1) if (cc == 0 and p1 is not None) else None)
        n1, bad = join(n1, r)
        if bad:
            return None
    return (n0, n1, cc)


# A. physical soundness
checks = 0; rem = 0; a_ok = True
for trial in range(TR):
    T = ST; width = 2 * T + W + 12
    x = {j: rnd.randint(0, 1) for j in range(-width, width + 1)}
    rows = [x]
    for t in range(T + 3):
        r = rows[-1]
        rows.append({j: rule(r[j - 1], r[j], r[j + 1]) for j in range(min(r) + 1, max(r))})
    mot = [rnd.choice((0, -1)) for _ in range(T)]
    for literal, refined in product((True, False), (False, True)):
        B = W; mem = (None, None, None)
        for t in range(T):
            X = rows[t]; strip = [X[j] for j in range(B - W + 1, B + 1)]; mv = mot[t]
            active = mv == 0 and strip[-1] == 0; label = X[B + 1]
            nxt_last = rows[t + 1][B + mv]
            p1_old = mem[1]
            new = update(mem, strip, nxt_last, mv, active, label, literal, refined)
            if new is None:
                a_ok = False; break
            B2 = B + mv; n0, n1, nc = new
            a_ok &= n0 is None or n0 == rows[t + 2][B2]
            a_ok &= n1 is None or n1 == rows[t + 2][B2 + 1]
            a_ok &= nc is None or nc == rows[t + 1][B2 + 1]
            a_ok &= n0 is None or n1 is None
            if mv == -1 and p1_old == 1:
                rem += 1; a_ok &= (1 - nxt_last) == rows[t + 2][B]
            checks += 1; mem = new; B = B2
report('A. physical soundness (%d ticks over 4 variants; remark case seen %d times)' % (checks, rem), a_ok and rem > 0)

# B. information order on abstract paths
ext = lambda u, v: all(a is None or a == b for a, b in zip(u, v))   # v extends u
b_ok = True; strict = 0; ticks = 0
for trial in range(TR * 4):
    T = ST
    row = {j: rnd.randint(0, 1) for j in range(-2 * T - W - 8, W + 2)}
    for literal in (True, False):
        r = dict(row); B = W; mo = (None, None, None); mr = (None, None, None); alive_r = True
        for t in range(T):
            mv = rnd.choice((0, -1)); label = rnd.randint(0, 1)
            strip = [r[j] for j in range(B - W + 1, B + 1)]
            active = mv == 0 and strip[-1] == 0
            r[B + 1] = label; r[B + 2] = 0                       # the abstract incoming cell
            new = {j: rule(r[j - 1], r[j], r[j + 1]) for j in range(min(r) + 1, B + 2)}
            nxt_last = new[B + mv]
            no = update(mo, strip, nxt_last, mv, active, label, literal, False)
            nr = update(mr, strip, nxt_last, mv, active, label, literal, True)
            ticks += 1
            if nr is not None and no is None:
                b_ok = False
            if nr is None:
                strict += no is not None
                break
            if no is None:
                break
            b_ok &= ext(no, nr)
            mo, mr = no, nr
            B += mv
            r = {j: v for j, v in new.items() if j <= B}
report('B. refined accepts => original accepts, refined extends original (%d ticks; refined-only rejections %d)' % (ticks, strict), b_ok and strict > 0)

# C. the tableau
c_ok = True
for ext3 in product((0, 1), repeat=3):
    row = dict(zip(range(11, 20), (1, 1, 1, 0, 1, 1) + ext3)); rs = [row]
    for _ in range(4):
        r = rs[-1]; rs.append({j: rule(r[j - 1], r[j], r[j + 1]) for j in range(min(r) + 1, max(r))})
    c_ok &= [rs[1][j] for j in range(12, 17)] == [0, 0, 0, 1, 0]
    c_ok &= [rs[2][j] for j in range(13, 16)] == [0, 1, 1]
    c_ok &= [rs[3][j] for j in range(14, 17)] == [1, 0, 0]
    c_ok &= rs[4][15] == 1
report('C. tableau 111011 -> 00010 -> 011 -> 100 -> 1, all eight exteriors', c_ok)
print('ALL PASS' if ok else 'SOME FAIL')
