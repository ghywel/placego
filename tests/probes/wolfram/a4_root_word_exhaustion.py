#!/usr/bin/env python3
"""L1470 (Local, 2026-11-03): GC2574's provenance request for L1469. Two finite facts, by plain evaluation, no solver:
(1) Exhaustion: every row whose cells -9..15 carry WORD (25 cells), arbitrary elsewhere, has X(19, 10) = 1. The light cone
    of (19, 10) at time 0 is exactly -9..29, so the 14 cells 16..29 are the only free ones: all 2^14 completions are run.
(2) The word is the actual root: pattern 3 on 1010000 at (r, s) = (0, 4) at t0 = 3000, at A0 - 9 .. A0 + 15 (A0 = F - 1).
Controls: the cone width is asserted (19 ticks reduce 39 cells to 1); a corrupted word (one bit flipped at each of the 25
positions, separately) must NOT force X(19, 10) = 1 for at least one flip, and the all-white word must not force it.
Run: python3 tests/probes/wolfram/a4_root_word_exhaustion.py DATA63.json
"""
import itertools
import json
import sys

import numpy as np

WORD = '0101010010001101110011101'
rule = lambda l, c, r: l ^ (c | r)


def forced(word):
    """True iff every completion of word on -9..15 (cells 16..29 free) gives X(19, 10) = 1."""
    for bits in itertools.product((0, 1), repeat=14):
        row = [int(ch) for ch in word] + list(bits)
        for _ in range(19):
            row = [rule(row[i - 1], row[i], row[i + 1]) for i in range(1, len(row) - 1)]
        assert len(row) == 1, 'cone width'
        if row[0] != 1:
            return False
    return True


print('(1) all 16384 completions of the word force X(19, 10) = 1: %s' % forced(WORD))
flips_not_forced = sum(1 for i in range(25) if not forced(WORD[:i] + str(1 - int(WORD[i])) + WORD[i + 1:]))
print('control: single-bit corruptions of the word that no longer force it: %d of 25' % flips_not_forced)
print('control: the all-white word forces it: %s (expected False)' % forced('0' * 25))
d = json.load(open(sys.argv[1])); orb = [tuple(o) for o in d['orb']]; q = len(orb); N = d['N']; r0, s0 = d['r'], d['s']
E = lambda x, t: orb[(t + s0) % q][((t - x) + r0) % N]
T0 = 3000; lo = -2 * T0 - 10; hi = T0 + 50; c = -lo
row = np.array([E(x, 0) for x in range(lo, hi)], dtype=np.uint8); bg = row.copy(); row[c] ^= 1; row[c + 1] ^= 1  # pattern 3
for _ in range(T0):
    n = np.zeros_like(row); n[1:-1] = row[:-2] ^ (row[1:-1] | row[2:]); row = n
    m = np.zeros_like(bg); m[1:-1] = bg[:-2] ^ (bg[1:-1] | bg[2:]); bg = m
A0 = int(np.flatnonzero(row ^ bg).min()) - 1
assert A0 + 15 < len(row) - T0 - 1 and A0 - 9 > T0 + 1, 'root cells outside the exact range'
actual = ''.join(str(int(row[A0 + i])) for i in range(-9, 16))
print('(2) actual root cells A0-9..A0+15 = %s; equal to the word: %s' % (actual, actual == WORD))
print('A4_ROOT_WORD_EXHAUSTION_DONE')
