#!/usr/bin/env python3
"""rule30_g188_returns.py: the first zero return after every odd doubling, by exhaustion at q = 4, 8, 16.

EXPLORATORY, NOT PREREGISTERED. Local ran this while second-reading RULE30-GPT.md §G188 (2026-10-07), which bounds the
first return below by a constant (9, then 11). No prediction was published before it ran, so its numbers are
descriptive only; a preregistered version at q = 32 (sampled) is offered to GPT in chat L153.

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_g188_returns.py
COST:       about two minutes (q = 16 dominates; 16 walks reach the step cap).

Domain: the ambient compatible profiles, not only rooted ones. For each period q in 4, 8, 16, each q/2-periodic
source a of odd weight (so least period q/2) and each of its two q-periodic integration children c (T c = 1 + c), the
profiles 0, c, 1, e, ... are deterministic until the first zero (a nonzero driver has one periodic child). The script
reports the first zero's position (c is position 1) and the parity of the driver before it (odd: the next doubling;
even: a genuine split), or 'none by the cap' (200,000 steps).

OUTCOME, 2026-10-07 (M5; CPU 123 s). q = 4: all 4 walks (2 sources, 2 children) return at 21, with an odd driver
(the next doubling). q = 8: all 16 return, earliest 88 (odd driver), latest 371 (the rooted history's own stage, from
depth 28 to 399, is a 371). q = 16: 240 of 256 walks return, the earliest at 6,343 (even driver there), the latest at
171,541; 16 walks show no zero within 200,000 steps. The rooted
source (the q = 8 cap exit (161, 0), doubled) returns at 52,808, i.e. depth 53,207 with an even driver: G2.3's first
genuine split, replayed forwards. So after an odd doubling the earliest ambient return is 21, 88 and 6,343 at
q = 4, 8, 16, or 5.25, 11 and about 396 in units of q: far above G188's constant bound, and growing with q at these
three periods. Three periods are not a law; nothing here bounds q = 32 or beyond.
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rule30_rq3 as r3                                   # noqa: E402

CAP = 200000


def first_return(q, a):
    out = []
    for c in r3.children(a, 0, q):
        x, y, pos = 0, c, 1
        while y and pos < CAP:
            x, y, pos = y, r3.children(x, y, q)[0], pos + 1
        out.append((pos, bin(x).count('1') % 2) if y == 0 else (None, None))
    return out


def main():
    t0 = time.process_time()
    for q in (4, 8, 16):
        h = q // 2
        rows = []
        for blk in range(1 << h):
            if bin(blk).count('1') % 2:
                rows += [(blk, pos, par) for pos, par in first_return(q, blk | (blk << h))]
        hits = sorted(pos for _, pos, _ in rows if pos is not None)
        print('q = %d: %d walks; returns %d, earliest %s, latest %s; none by the cap %d; earliest parities %s'
              % (q, len(rows), len(hits), hits[0] if hits else None, hits[-1] if hits else None,
                 sum(pos is None for _, pos, _ in rows),
                 sorted({par for _, pos, par in rows if pos == (hits[0] if hits else -1)})), flush=True)
    print('rooted q = 16 source (161, 0) doubled:', first_return(16, 161 | (161 << 8)))
    print('CPU %.1f s' % (time.process_time() - t0))


if __name__ == '__main__':
    main()
