#!/usr/bin/env python3
"""L1364 T55 (Local, 2026-11-03): ether-ether domain walls in the classic ether. reports/rule30-genealogy.md section 59.
Run: python3 tests/probes/ether_walls.py

Left half: the classic ether at alignment (c0, c1) on x < 0; right half: the ether at another alignment (d0, d1) on
x >= 0 (all 28 x 27 ordered pairs), white beyond x = 3000. The left front of the difference from the left ether is
sampled every 250 ticks from t = 500 to 2000; its leftward speed over that span is reported per pair, with the
fastest pairs listed.
"""
TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
LO, HI, T = -4000, 3000, 2000
N = HI - LO + 1
mask = (1 << N) - 1


def row(f):
    return sum(f(x) << (x - LO) for x in range(LO, HI + 1))


res = []
for c0 in range(7):
    for c1 in range(4):
        ref = row(lambda x: TAB[(x + c0) % 7][c1])
        for d0 in range(7):
            for d1 in range(4):
                if (d0, d1) == (c0, c1):
                    continue
                a = row(lambda x: TAB[(x + c0) % 7][c1] if x < 0 else TAB[(x + d0) % 7][d1])
                r = ref
                fr = []
                for t in range(1, T + 1):
                    a = ((a << 1) ^ (a | (a >> 1))) & mask
                    r = ((r << 1) ^ (r | (r >> 1))) & mask
                    if t >= 500 and t % 250 == 0:
                        d = (a ^ r) >> (t + 1) << (t + 1)
                        fr.append((d & -d).bit_length() - 1 + LO if d else None)
                sp = None if None in fr else -(fr[-1] - fr[0]) / (T - 500)
                res.append((sp, (c0, c1), (d0, d1), fr))
ok = sorted((s for s in res if s[0] is not None), key=lambda s: -s[0])
print('%d pairs; %d healed (no difference left); leftward speeds over t = 500..2000: max %.4f, min %.4f' % (
    len(res), len(res) - len(ok), ok[0][0], ok[-1][0]))
hist = {}
for s in ok:
    hist[round(s[0], 3)] = hist.get(round(s[0], 3), 0) + 1
print('speed histogram (rounded): %s' % sorted(hist.items(), reverse=True))
for s in ok[:12]:
    print('  left %s right %s: speed %.4f, fronts %s' % (s[1], s[2], s[0], s[3]))
print('ETHER_WALLS_DONE')
