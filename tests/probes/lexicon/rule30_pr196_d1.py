#!/usr/bin/env python3
"""rule30_pr196_d1.py: PR196-D1, the rooted period-sixteen first-edge diagnostic, of RULE30-GPT.md (GPT's
preregistration at 4e66c9a; claimed by Local in CLOUD-LOCAL.md at 44e44c7, after the G196 review in L164, before this
script was written or run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_pr196_d1.py
COST:       seconds expected; caps 60 s wall and 256 MiB peak RSS (GPT's); a breach stops without raising them.

The witness: S84's rooted q = 16 return, from the q = 8 cap exit (161, 0) doubled, first child at every step, first
zero at r = 52,808; w = the profile at r - 1 (= the one at r - 2), m = 26,403, h = 8. Its paired walk has sixteen
ordered vertices (X(t), X(t + 8)). By G196 the flipped target at phase t has F_m = 1 + d(t), with
    d(t) = (m mod 2) + sum_(k=1..m-1) U_(2k-1)(w)(t + m - k),
so the only alternative edge at phase t (both appended bits flipped) is legal exactly when d(t) = d(t + 8) = 0.

PREDICTION (GPT's, published before this run): no legal alternative at any of the eight unordered decisions. Any
legal one refutes it (an exit only, no return path). If all fail, this rooted component is exactly its sixteen-cycle
(swap displacement 8, admitting q = 16 only).
CONTROLS (GPT's): scalar list and packed-mask recurrences agree on every profile and accumulated derivative; at
m = 1 to 6 the diagonal identity matches direct finite-window F_m(T0) + F_m(T1) for every tail with two paddings;
D0's eight retained F pairs on the q = 8 witness (w = 00111101, m = 43) are reproduced; the sixteen-cycle's edges,
V labels and XOR equation hold; the t + m - k rotation agrees with literal suffix extraction, wraparound included.

OUTCOME, 2026-10-07 (M5, one process, one run; wall 0.65 s, CPU 0.68 s, peak RSS 23.8 MiB). Controls all PASS: the
diagonal identity equals direct F_m(T0) + F_m(T1) for every tail at m = 1 to 6 with both paddings; the t + m - k
rotation equals literal suffix extraction at q = 3, 4, 5, 8, m = 1 to 8, every phase (wraparound included); D0's
eight pairs (1, 0), (0, 0), (0, 1), (0, 1), (0, 1), (0, 0), (1, 0), (1, 0) are reproduced on w = 00111101; the rooted
witness has r = 52,808, m = 26,403, w = 1000101001100001 (least period 16), U_(r-2) = c, U_(r-3) = 1, complementary
halves and an odd source of least period 8; scalar lists equal packed masks on all 52,807 profiles and on d; the
sixteen-cycle's edges satisfy F = 1, the XOR equation, the target V labels and G193's identity. Derivatives by phase
0 to 15: d = 0 0 1 0 0 0 1 1 0 1 1 1 0 1 1 1. The alternative (both appended bits flipped) is legal exactly when
d(t) = d(t + 8) = 0: at phases 0, 4, 8 and 12, that is at unordered decisions 0 and 4 (phase t + 8 mirrors t). Flipping
both bits keeps V(X') + V(Y') = 1, so these alternatives are genuine edges of H_m. PR196-D1's prediction (no legal
alternative) is REFUTED: the rooted component has exits at two of its eight decisions. As preregistered, this supplies
exits only; no return path, recurrence or persistence is established, and no continuation search follows.
"""
import resource
import sys
import time
from itertools import product

T_START = time.time()


def rot(w, d, q):
    d %= q
    return ((w >> d) | (w << (q - d))) & ((1 << q) - 1)


def children(a, b, q):
    out = []
    bit = lambda u, t: (u >> (t % q)) & 1
    for c0 in (0, 1):
        c = [c0]
        for t in range(q - 1):
            c.append(bit(a, t) ^ (bit(b, t) | c[t]))
        if bit(a, q - 1) ^ (bit(b, q - 1) | c[q - 1]) == c0:
            out.append(sum(v << t for t, v in enumerate(c)))
    return out


def walk(q, a, cap):
    c = children(a, 0, q)[0]
    prof, x, y = [0, c], 0, c
    while y and len(prof) < cap:
        x, y = y, children(x, y, q)[0]
        prof.append(y)
    return prof


def lp(u, q):
    return next(d for d in range(1, q + 1) if q % d == 0 and rot(u, d, q) == u)


def U_masks(w, q, n):
    """Packed-mask cyclic backward functions U_0 .. U_n of w (bit t = time t)."""
    U = [w, w]
    for i in range(2, n + 1):
        U.append(rot(U[i - 2], 1, q) ^ (U[i - 1] | U[i - 2]))
    return U


def U_lists(w, q, n):
    """Independent scalar periodic lists: U_(i+2)(t) = U_i(t + 1) + (U_(i+1)(t) OR U_i(t))."""
    a = [(w >> t) & 1 for t in range(q)]
    U = [a, a[:]]
    for i in range(2, n + 1):
        x, y = U[i - 2], U[i - 1]
        U.append([x[(t + 1) % q] ^ (y[t] | x[t]) for t in range(q)])
    return U


def d_masks(U, q, m):
    """d(t) for all phases: (m mod 2) + sum_k rot(U_(2k-1), m - k), as a mask."""
    acc = ((1 << q) - 1) if m % 2 else 0
    for k in range(1, m):
        acc ^= rot(U[2 * k - 1], m - k, q)
    return acc


def d_lists(U, q, m):
    acc = [m % 2] * q
    for k in range(1, m):
        u = U[2 * k - 1]
        acc = [acc[t] ^ u[(t + m - k) % q] for t in range(q)]
    return acc


def U_fin(n, bits):
    L = [list(bits), list(bits)]
    for i in range(2, n + 1):
        x, y = L[i - 2], L[i - 1]
        L.append([x[t + 1] ^ (y[t] | x[t]) for t in range(min(len(x) - 1, len(y)))])
    return L[n][0]


def check_caps():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576
    if time.time() - T_START > 60 or rss > 256:
        print('CAP REACHED (wall %.1f s, peak RSS %.1f MiB): stopped, not a result' % (time.time() - T_START, rss))
        sys.exit(2)


def main():
    ok = True
    # control 1: the diagonal identity against direct finite windows, m = 1 to 6, every tail, two paddings
    c1 = True
    for m in range(1, 7):
        for T in product((0, 1), repeat=m - 1):
            for pad in (0, 1):
                D = U_fin(2 * m - 1, list(T) + [0, pad]) ^ U_fin(2 * m - 1, list(T) + [1, pad])
                S = m % 2
                for k in range(1, m):
                    S ^= U_fin(2 * k - 1, list(T[len(T) - k:]) + [pad])
                c1 &= D == S
    print('control: diagonal identity = direct F_m(T0) + F_m(T1), m = 1-6, every tail, both paddings: %s'
          % ('PASS' if c1 else 'FAIL'))
    ok &= c1
    # control 2: the t + m - k rotation against literal suffix extraction on cyclic words, wraparound included
    c2 = True
    for q in (3, 4, 5, 8):
        for w in range(1 << q):
            for m in range(1, 9):
                U = U_masks(w, q, 2 * m)
                dm = d_masks(U, q, m)
                for t in range(q):
                    T = [(w >> ((t + 1 + i) % q)) & 1 for i in range(m - 1)]
                    S = m % 2
                    for k in range(1, m):
                        S ^= U_fin(2 * k - 1, T[len(T) - k:] + [(w >> ((t + m) % q)) & 1])
                    c2 &= ((dm >> t) & 1) == S
    print('control: rotation t + m - k = literal suffix extraction (q = 3, 4, 5, 8; m = 1-8; all phases): %s'
          % ('PASS' if c2 else 'FAIL'))
    ok &= c2
    check_caps()
    # control 3: D0's retained pairs on the q = 8 witness (block 1000, first child, r = 88)
    a8 = next(b | (b << 4) for b in range(16) if bin(b).count('1') % 2 and len(walk(8, b | (b << 4), 1000)) - 1 == 88)
    pr8 = walk(8, a8, 1000)
    w8, m8 = pr8[-2], 43
    U8 = U_masks(w8, 8, 2 * m8)
    d8 = d_masks(U8, 8, m8)
    pairs8 = [(1 ^ ((d8 >> t) & 1), 1 ^ ((d8 >> ((t + 4) % 8)) & 1)) for t in range(8)]
    c3 = ''.join(str((w8 >> t) & 1) for t in range(8)) == '00111101' and \
        pairs8 == [(1, 0), (0, 0), (0, 1), (0, 1), (0, 1), (0, 0), (1, 0), (1, 0)]
    print("control: D0's eight F43 pairs reproduced on w = 00111101: %s %s" % ('PASS' if c3 else 'FAIL', pairs8))
    ok &= c3
    check_caps()
    # the rooted witness
    Q, H = 16, 8
    pr = walk(Q, 161 | (161 << 8), 60000)
    r = len(pr) - 1
    w = pr[r - 1]
    m = (r - 2) // 2
    full = (1 << Q) - 1
    wit = r == 52808 and pr[r - 2] == w and lp(w, Q) == Q and m == 26403
    Um = U_masks(w, Q, r)
    c = pr[1]
    src = c ^ rot(c, 1, Q)
    wit &= Um[r - 2] == c and Um[r - 3] == full and rot(c, H, Q) == c ^ full and lp(src, Q) == H
    wit &= bin(src & ((1 << H) - 1)).count('1') % 2 == 1
    print('witness: r = %d, m = %d, w = %s (least period %d); U_(r-2) = c, U_(r-3) = 1, complementary halves, odd '
          'source of least period 8: %s' % (r, m, ''.join(str((w >> t) & 1) for t in range(Q)), lp(w, Q),
                                           'PASS' if wit else 'FAIL'))
    ok &= wit
    check_caps()
    # control 4: scalar lists agree with masks on every profile and on the accumulated derivative
    Ul = U_lists(w, Q, 2 * m)
    c4 = all(sum(b << t for t, b in enumerate(Ul[n])) == Um[n] for n in range(2 * m + 1))
    dm = d_masks(Um, Q, m)
    dl = d_lists(Ul, Q, m)
    c4 &= sum(b << t for t, b in enumerate(dl)) == dm
    print('control: scalar lists = packed masks on all %d profiles and on d: %s' % (2 * m + 1, 'PASS' if c4 else 'FAIL'))
    ok &= c4
    check_caps()
    # control 5: the sixteen-cycle's edges: F = 1 at every phase, XOR equation (complementary c), V labels on targets
    F, Vm, Cm = Um[2 * m - 1], Um[2 * m - 2], Um[2 * m]
    c5 = F == full and all(((Cm >> t) & 1) ^ ((Cm >> ((t + H) % Q)) & 1) == 1 for t in range(Q))
    c5 &= all(((Vm >> ((t + 1) % Q)) & 1) ^ ((Vm >> ((t + 1 + H) % Q)) & 1) == 1 for t in range(Q))
    c5 &= Cm == full ^ rot(Vm, 1, Q)                       # G193: U_2m = 1 + V_m of the next window when F = 1
    print('control: sixteen-cycle edges (F = 1, XOR equation, target V labels, G193 identity): %s'
          % ('PASS' if c5 else 'FAIL'))
    ok &= c5
    # the sixteen ordered decisions
    rows = []
    for t in range(Q):
        dt, dth = (dm >> t) & 1, (dm >> ((t + H) % Q)) & 1
        rows.append((t, dt, dth, 1 ^ dt, 1 ^ dth, dt == 0 and dth == 0))
    for t, dt, dth, fx, fy, legal in rows:
        print('phase %2d: d = %d, d(t + 8) = %d; flipped F = %d, %d; legal %s' % (t, dt, dth, fx, fy, legal))
    sym = all(rows[t][5] == rows[t + H][5] and rows[t][1] == rows[t + H][2] for t in range(H))
    print('phase t + 8 mirrors t: %s' % ('PASS' if sym else 'FAIL'))
    ok &= sym
    legal = [t for t in range(H) if rows[t][5]]
    print('eight unordered decisions (phases 0-7): legal alternatives at %s' % (legal or 'none'))
    print('PR196-D1 prediction (no legal alternative):', 'HELD' if not legal else 'REFUTED')
    if not legal:
        print('so this rooted component is exactly its directed sixteen-cycle (swap displacement 8; q = 16 only)')
    print('all controls %s' % ('PASS' if ok else 'FAIL'))
    rus = resource.getrusage(resource.RUSAGE_SELF)
    print('resources: wall %.2f s, CPU %.2f s, peak RSS %.1f MiB' % (time.time() - T_START, time.process_time(),
                                                                     rus.ru_maxrss / 1048576))
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
