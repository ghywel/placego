#!/usr/bin/env python3
"""L1364 T55c (Local, 2026-11-03): does any spatially periodic right half invade the classic ether?
reports/rule30-genealogy.md section 59. Run: python3 tests/probes/ether_periodic_right.py PMAX

Left half: the classic ether at alignment (c0, c1) on x < 0 (all 28). Right half: a word w of length p <= PMAX repeated
on x >= 0 (one word per necklace class, all-white and all-black included). The left front of the difference from the
ether is read at t = 400 and t = 1200; its leftward speed over that span is reported, with the fastest cases.
T55b's strip bound is 7/44 = 0.159; A2's is 7/12.
"""
import sys

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10
TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
LO, HI, T = -1500, 1500, 1200
N = HI - LO + 1
mask = (1 << N) - 1


def necklaces(p):
    seen = set()
    for v in range(1 << p):
        w = format(v, '0%db' % p)
        if min(w[i:] + w[:i] for i in range(p)) == w and w not in seen:
            if any(p % q == 0 and w == w[:q] * (p // q) for q in range(1, p)):
                continue                                    # not primitive
            seen.add(w)
            yield w


words = [w for p in range(1, PMAX + 1) for w in necklaces(p)]
res = []
for c0 in range(7):
    for c1 in range(4):
        ref = sum(TAB[(x + c0) % 7][c1] << (x - LO) for x in range(LO, HI + 1))
        left = sum(TAB[(x + c0) % 7][c1] << (x - LO) for x in range(LO, 0))
        for w in words:
            p = len(w)
            a = left | sum(int(w[x % p]) << (x - LO) for x in range(0, HI + 1))
            r = ref; fr = {}
            for t in range(1, T + 1):
                a = ((a << 1) ^ (a | (a >> 1))) & mask
                r = ((r << 1) ^ (r | (r >> 1))) & mask
                if t in (400, 1200):
                    d = (a ^ r) >> (t + 1) << (t + 1)
                    fr[t] = (d & -d).bit_length() - 1 + LO if d else None
            sp = None if None in fr.values() else -(fr[1200] - fr[400]) / 800
            res.append((sp, (c0, c1), w, fr))
ok = sorted((s for s in res if s[0] is not None), key=lambda s: -s[0])
print('%d cases (%d words of period <= %d, 28 alignments); %d healed; leftward speed t = 400..1200: max %.4f' % (
    len(res), len(words), PMAX, len(res) - len(ok), ok[0][0]))
for s in ok[:15]:
    print('  alignment %s right word %s: speed %.4f, fronts %s' % (s[1], s[2], s[0], s[3]))
print('ETHER_PERIODIC_RIGHT_DONE')
