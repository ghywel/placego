#!/usr/bin/env python3
"""L1366 (Local, 2026-11-03): data and a Python mirror of the Lean rooted-front checker (tests/probes/lean/RootedFront.lean).
Run: python3 tests/probes/rooted_front_lean_data.py [B] [--lean]

For each of A1's 28 entries: E = the inserted edge's evolution, target Q = xB + 13 at T = t1, cut B (default 87). The
untrusted data list ks = A2's backward thresholds thr[0..T] (GC2423); the Lean checker needs no proof of them. The mirror
runs exactly the Lean algorithm: window 2; successors of rooted states (succR); the half-line states' A2 step; their
minimum, expanded to k; conversion of rooted states with L - 1 >= k to half-line states; deduplication; and at T the
final check (every rooted L > Q, the half-line m >= Q). With --lean it prints the ks lists as Lean source.
"""
import sys

args = [a for a in sys.argv[1:] if not a.startswith('--')]
B = int(args[0]) if args else 87
LEAN = '--lean' in sys.argv
TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
ENTRY = {(0, 0): (81, -19), (0, 1): (13, -5), (0, 2): (10, 2), (0, 3): (186, -26), (1, 0): (185, -27), (1, 1): (17, -6),
         (1, 2): (9, 1), (1, 3): (9, 1), (2, 0): (8, 0), (2, 1): (17, -7), (2, 2): (16, -7), (2, 3): (8, 0),
         (3, 0): (7, -1), (3, 1): (7, -1), (3, 2): (16, -8), (3, 3): (7, -1), (4, 0): (6, -2), (4, 1): (148, -23),
         (4, 2): (6, -2), (4, 3): (222, -37), (5, 0): (221, -38), (5, 1): (148, -24), (5, 2): (5, -3), (5, 3): (5, -3),
         (6, 0): (4, -4), (6, 1): (25, -11), (6, 2): (4, -4), (6, 3): (82, -18)}
LO = -1000


def mis(dl, dc, dr, c, r):
    return dl ^ ((1 - r) & dc) ^ ((1 - c) & dr) ^ (dc & dr)


def opts(o):
    return [0, 1] if o is None else [o]


def tv(dl, dc, dr, c, r):
    vs = {mis(a, b, d, c, r) for a in opts(dl) for b in opts(dc) for d in opts(dr)}
    return vs.pop() if len(vs) == 1 else None


def succR(e, s):
    L, a, b = s
    n0 = 1 - e(L - 1)
    n1 = tv(0, 1, a, e(L), e(L + 1))
    n2 = tv(1, a, b, e(L + 1), e(L + 2))
    n3 = tv(a, b, None, e(L + 2), e(L + 3))
    if n0:
        return [(L - 1, n1, n2)], None
    r1 = [] if n1 == 0 else [(L, n2, n3)]
    if n1 == 1:
        return r1, None
    r2 = [] if n2 == 0 else [(L + 1, n3, None)]
    if n2 == 1:
        return r1 + r2, None
    r3 = [] if n3 == 0 else [(L + 2, None, None)]
    if n3 == 1:
        return r1 + r2 + r3, None
    return r1 + r2 + r3, L + 2


def expand(m, n):
    return [(m + 1 + i, None, None) for i in range(n)]


def tick(e, k, R, H):
    outs = [succR(e, s) for s in R]
    R1 = [s for o in outs for s in o[0]]
    Hs = [o[1] for o in outs if o[1] is not None] + ([H if e(H) else H - 1] if H is not None else [])
    R2, H2 = R1, None
    if Hs:
        m = min(Hs)
        n = max(k - m, 0)
        R2 = R1 + expand(m, n); H2 = m + n
    keep = [s for s in R2 if s[0] - 1 < k]
    conv = [s[0] - 1 for s in R2 if k <= s[0] - 1] + ([H2] if H2 is not None else [])
    out, seen = [], set()
    for s in keep:
        if s not in seen:
            seen.add(s); out.append(s)
    return out, (min(conv) if conv else None)


worst = 0
for (c0, c1), (T, xB) in sorted(ENTRY.items()):
    Q = xB + 13
    rows = [[TAB[(x + c0) % 7][c1] if x < 0 else int(x == 0) for x in range(LO, 1300)]]
    for t in range(T):
        r = rows[-1]
        rows.append([0] + [r[i - 1] ^ (r[i] | r[i + 1]) for i in range(1, len(r) - 1)] + [0])
    E = lambda t, x: rows[t][x - LO]
    thr = [0] * (T + 1); thr[T] = Q
    for t in range(T - 1, -1, -1):
        thr[t] = thr[t + 1] if E(t, thr[t + 1]) else thr[t + 1] + 1
    R, H = expand(B, max(thr[0] - B, 0)), B + max(thr[0] - B, 0)
    peak = len(R); ok = True
    for t in range(T):
        if not all(LO + t <= s[0] - 1 for s in R) or (H is not None and H < LO + t):
            ok = False; break
        R, H = tick(lambda x, t=t: E(t, x), thr[t + 1], R, H)
        peak = max(peak, len(R))
    ok = ok and all(Q < s[0] for s in R) and (H is None or Q <= H)
    worst = max(worst, peak)
    print('(%d,%d) T %3d Q %4d cut %d: %s; A2 thr[0] %d; peak rooted states %d' % (
        c0, c1, T, Q, B, 'PASS' if ok else 'FAIL', thr[0], peak), flush=True)
    if LEAN:
        print('def ks_%d_%d : List Int := [%s]' % (c0, c1, ', '.join(str(v) for v in thr)))
print('MIRROR_DONE (worst peak %d)' % worst)
