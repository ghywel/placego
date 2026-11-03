#!/usr/bin/env python3
"""L1363 T54b (Local, 2026-11-03): greedy local search for right tails that break the A1 entry target inside the four
gaps of reports/rule30-genealogy.md section 58 (58a). Run: python3 tests/probes/rooted_front_climb.py SECONDS_PER_CUT

For entry (c0, c1) with time t1 and target Q = xB + 13, and a cut b, a tail is the initial bits b+1 .. b+2*t1 (bits
beyond cannot reach any cell x <= Q by t1; E elsewhere). Objective: the leftmost difference L(t1) from E (lower is
better; a healed row scores +inf). Single-bit flips are tried in random order and kept when L(t1) does not increase
(sideways moves allowed); a restart after 400 non-improving tries. L(t1) <= Q is a witness that b does not suffice,
replayed independently on a fresh wide row before it is reported.
"""
import random
import sys
import time

SECS = float(sys.argv[1]) if len(sys.argv) > 1 else 8
TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
GAPS = {(0, 3): (186, -26, 51, 83), (1, 0): (185, -27, 49, 81), (4, 1): (148, -23, 45, 66), (5, 1): (148, -24, 43, 61)}
LO, HI = -800, 800
n = HI - LO + 1
mask = (1 << n) - 1
rng = random.Random(5402)


def ev(a, T):
    for _ in range(T):
        a = ((a << 1) ^ (a | (a >> 1))) & mask
    return a


for (c0, c1), (T, xB, lo_end, rooted) in sorted(GAPS.items()):
    Q = xB + 13
    E0 = lambda x: TAB[(x + c0) % 7][c1] if x < 0 else int(x == 0)
    base = sum(E0(x) << (x - LO) for x in range(LO, HI + 1))
    ref = ev(base, T)
    valid = sum(1 << i for i in range(T + 1, n - T - 1))

    def score(a):
        d = (ev(a, T) ^ ref) & valid
        return (d & -d).bit_length() - 1 + LO if d else 10 ** 9   # leftmost differing x

    found = []
    for b in range(lo_end - 1, rooted):                     # lo_end - 1 is the control: random tails break it
        free = list(range(b + 1, b + 2 * T + 1))
        keep = base & ((1 << (b + 1 - LO)) - 1)
        t0 = time.time(); best = None; wit = None
        while time.time() - t0 < SECS and wit is None:
            a = keep | (base & ~((1 << (b + 1 - LO)) - 1))
            for x in free:
                if rng.random() < 0.5:
                    a ^= 1 << (x - LO)
            s = score(a); stall = 0
            while stall < 400 and time.time() - t0 < SECS:
                x = rng.choice(free)
                a2 = a ^ (1 << (x - LO))
                s2 = score(a2)
                if s2 <= s:
                    stall = 0 if s2 < s else stall + 1
                    a, s = a2, s2
                else:
                    stall += 1
                if s <= Q:
                    break
            best = s if best is None else min(best, s)
            if s <= Q:
                assert all(((a >> (x - LO)) & 1) == E0(x) for x in range(LO, b + 1))
                if score(a) <= Q:                           # replay
                    wit = a
        found.append('%d:%s' % (b, 'W' if wit is not None else 'best L %s (Q %d)' % (best, Q)))
        if wit is None:
            break                                           # the first cut without a witness ends this entry
    print('(%d,%d) gap [%d, %d]: %s' % (c0, c1, lo_end, rooted, '; '.join(found)), flush=True)
print('ROOTED_FRONT_CLIMB_DONE')
