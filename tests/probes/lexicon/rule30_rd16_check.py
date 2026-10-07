#!/usr/bin/env python3
"""rule30_rd16_check.py: Local's second reading of GPT's RD16 (rule30_debt16.py, GC319): an independent recomputation
of the phase-zero reference clock and the slope-5/2 whole-prefix debts through all sixteen rooted period-32 entries.

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_rd16_check.py
COST:       under a minute; cap 300 CPU s.

Shared with RD16: only rule30_rq3.children (the child constructor, already audited by GPT in GC288 and by Local's TM5b).
Written separately: the walk, the clock and the debt. The clock starts at T = 0 at the root (0, 1^16), depth 0. At the
state (w_(d-1), w_d) with clock T_d, the reset delay is 0 when w_d = 0 and otherwise 1 + the least i >= 0 with
w_d(T_d + i mod 16) = 1; T_(d+1) = T_d + delay. The debt through depth N is the largest (T_b - T_a) - (5/2)(b - a) over
0 <= a <= b <= N, computed in doubled units on z_d = 2 T_d - 5 d. Each history is followed from the root through its
branches to its exit zero at depth N_5 - 1, and the terminal zero edge to N_5 (delay 0) is included.
Checks: the sixteen N_5 values; every debt equal to RD16's table; each of GPT's witness intervals [a, b] has the stated
elapsed time T_b - T_a on its history and gives exactly the stated debt; the shared prefix to depth 53,207 has debt
26.5. No predictions: this is a verification of a published result, and any disagreement is reported as found.
OUTCOME, 2026-10-07 17:21 (M5, one run; CPU 17.8 s): ALL AGREE. The sixteen N_5 values reproduce; every debt equals
RD16's (28.5, 40, 39.5, 43.5, 39.5, 39.5, 36.5, 39.5, 39.5, 39.5, 42.5, 40, 39.5, 42.5, 60, 60 in N_5 order); each of
GPT's witness intervals has the stated elapsed time on its own history and gives exactly the stated debt; the shared
prefix to depth 53,207 has debt 26.5. So RD16's clock convention (phase zero at the root, delay 0 at zero drivers,
the terminal zero edge counted) and its witness arithmetic are confirmed by a separately written walk, clock and debt.
"""
import resource
import sys

sys.path.insert(0, __import__('os').path.dirname(__file__))
import rule30_rq3 as rq3

Q, FULL = 16, (1 << 16) - 1
RD16 = {87867: (57, (82955, 83020), 191), 183184: (80, (170583, 170617), 125), 196189: (79, (120349, 120368), 87),
        229338: (87, (97505, 97540), 131), 253537: (79, (120349, 120368), 87), 271596: (79, (120349, 120368), 87),
        291257: (73, (235434, 235471), 129), 527724: (79, (120349, 120368), 87), 551910: (79, (120349, 120368), 87),
        555813: (79, (120349, 120368), 87), 575211: (85, (504520, 504561), 145), 634886: (80, (609521, 609551), 115),
        645655: (79, (120349, 120368), 87), 667052: (85, (504520, 504561), 145), 770532: (120, (725127, 725155), 130),
        894235: (120, (725127, 725155), 130)}                       # doubled debt, witness, elapsed


def cpu():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime + r.ru_stime


def reset_delay(w, T):
    if w == 0:
        return 0
    for i in range(Q):
        if (w >> ((T + i) % Q)) & 1:
            return i + 1


def is_rot(u, v):
    return any(rq3.rot(u, k, Q) == v for k in range(Q))


histories = []                                                    # (N_5, clock list T_0 .. T_N5)
stack = [(0, FULL, [0])]                                          # (x, y, clocks so far); state depth = len - 1
while stack:
    x, y, T = stack.pop()
    while True:
        if cpu() > 300:
            print('CAP')
            sys.exit(1)
        d = len(T) - 1
        if y == 0:
            kids = rq3.children(x, 0, Q)
            T.append(T[-1])                                       # the zero edge has delay 0
            if not kids:                                          # odd: the period-32 entry, N_5 = d + 1
                histories.append((d + 1, T))
                break
            c1, c2 = kids
            if not is_rot(c1, c2):
                stack.append((0, c2, T[:]))
            x, y = 0, c1
            continue
        T.append(T[-1] + reset_delay(y, T[-1]))
        x, y = y, rq3.children(x, y, Q)[0]

ok = sorted(n for n, _ in histories) == sorted(RD16)
print('sixteen N_5 values reproduce:', ok, len(histories))
for n, T in sorted(histories):
    z = [2 * T[d] - 5 * d for d in range(len(T))]
    lo, best = z[0], 0
    for v in z:
        best = max(best, v - lo)
        lo = min(lo, v)
    dd, (a, b), el = RD16[n]
    wit = T[b] - T[a] == el and 2 * el - 5 * (b - a) == dd
    print('N_5 %7d: debt %5.1f (RD16 %5.1f) %s; witness [%d, %d] elapsed %d (RD16 %d) %s'
          % (n, best / 2, dd / 2, 'agree' if best == dd else 'DISAGREE', a, b, T[b] - T[a], el,
             'agree' if wit else 'DISAGREE'))
    ok &= best == dd and wit
n0, T0 = min(histories)
z = [2 * T0[d] - 5 * d for d in range(53208)]
lo, best = z[0], 0
for v in z:
    best = max(best, v - lo)
    lo = min(lo, v)
print('shared prefix to depth 53,207: debt %.1f (RD16 26.5) %s' % (best / 2, 'agree' if best == 53 else 'DISAGREE'))
ok &= best == 53
print('ALL AGREE' if ok else 'DISAGREEMENT FOUND', '; CPU %.1f s' % cpu())
