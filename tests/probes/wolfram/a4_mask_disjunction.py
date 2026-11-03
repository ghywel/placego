#!/usr/bin/env python3
"""L1477 (Local, 2026-11-03): an independent exhaustive check of GC2592's black-mask consequence and its reset/stay
counterexample. (1) For the 24-cell word 101010010001101110011101 on initial positions -8..15 and every assignment of the
13 cells 16..28 (all that the anti-diagonal X(s, 28 - s), s <= 18, can see), some X(s, 28 - s) with 0 <= s <= 18 is black.
Control: the same test with the word's first bit flipped, and with the all-white word, must find a completion with no
black mask. (2) The counterexample 0,1,1,z,0 on q-3..q+1: X(1, q-1) is the same for both z and X(2, q-1) = z.
Run: python3 tests/probes/wolfram/a4_mask_disjunction.py
"""
import itertools

rule = lambda l, c, r: l ^ (c | r)
WORD = '101010010001101110011101'


def black_mask_always(word):
    """True iff every completion of word on -8..15 (cells 16..28 free) has a black among X(s, 28 - s), 0 <= s <= 18."""
    lo = -8; n = 37  # positions -8..28
    for bits in itertools.product((0, 1), repeat=13):
        row = [int(ch) for ch in word] + list(bits)
        found = row[28 - lo] == 1  # s = 0: X(0, 28)
        cur = row; off = lo
        for s in range(1, 19):
            cur = [rule(cur[i - 1], cur[i], cur[i + 1]) for i in range(1, len(cur) - 1)]; off += 1
            x = 28 - s
            if cur[x - off] == 1:
                found = True
            if found:
                break
        if not found:
            return False
    return True


print('(1) every completion of the 24-cell word has a black mask cell X(s, 28 - s), s <= 18: %s' % black_mask_always(WORD))
print('control: first bit flipped: %s; all-white word: %s (expected False, False)' % (
    black_mask_always(str(1 - int(WORD[0])) + WORD[1:]), black_mask_always('0' * 24)))
for z in (0, 1):
    r0 = [0, 1, 1, z, 0]
    r1 = [rule(r0[i - 1], r0[i], r0[i + 1]) for i in range(1, 4)]   # cells q-2, q-1, q at time 1
    r2 = rule(r1[0], r1[1], r1[2])                                   # cell q-1 at time 2
    print('(2) z=%d: time 1 cells (q-2, q-1, q) = %s; X(1, q-1) = %d; X(2, q-1) = %d' % (z, r1, r1[1], r2))
print('A4_MASK_DISJUNCTION_DONE')
