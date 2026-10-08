#!/usr/bin/env python3
"""GC502 bounded clamped-wall output controls; no asymptotic entropy estimate.
COMMAND: python3 tests/probes/lexicon/rule30_gpt_boundary_collision.py
RUN-ON: GPT, standard Python; at most 8192 initial words at n=7.
PREDICTIONS (before first run, 2026-10-08):
 BC0 must: integer strip matches literal decimal Rule 30 on full finite sets
     for all cone initial words at n=1..4; no visible output contains 11.
 BC1 must: counts at n=1,2 are 2,3; n=2 multiplicities are 3,1,4
     for 00,01,10, and collision is 13/32.
 BC2 blind: an extra missing word with no 11 appears by n=7.
 CF must fail: n=2 is uniform over its allowed output words.
 UNEXPECTED: identify a shortest extra missing word, if present, and test
     all its nonempty proper contiguous factors against their own languages.
 REFUTED-BY: BC0/BC1 failure invalidates instrument; BC2 failure retained.
 OUTCOME (2026-10-08, GPT): BC0/BC1 PASS, 170 independent literal
 comparisons. Counts n=1..7: 2,3,5,8,12,17,25. Exact collisions:
 1/2, 13/32, 67/256, 1433/8192, 15689/131072,
 209233/2097152, 1036453/16777216. CF REFUTED; BC2 HELD.
 Shortest extra missing word 00000, all its proper factors admitted.
 Additional hand-derived control: initial sites 0111000 give 0000
 in both implementations. GC502 supplies a separate local proof of
 the five-zero exclusion; enumeration alone is only bounded evidence.
"""
from collections import Counter
from fractions import Fraction


def packed(seed, n):
    mask = (1 << (2*n-1)) - 1
    row, out = seed, []
    for t in range(2*n-1):
        if t % 2 == 0:
            out.append(str(row & 1))
        row = (((row << 1) | (t & 1)) ^ (row | (row >> 1))) & mask
    return ''.join(out)


def literal(seed, n):
    black = {i+1 for i in range(2*n-1) if seed >> i & 1}
    out = []
    for t in range(2*n-1):
        if t % 2 == 0:
            out.append(str(int(1 in black)))
        black.discard(0)
        if t & 1:
            black.add(0)
        # Include the outward-growing finite row; column 0 is overwritten
        # each tick, and only positive sites evolve by the literal table.
        upper = max(black, default=0) + 1
        black = {i for i in range(1, upper+1)
                 if 30 >> (4*int(i-1 in black)+2*int(i in black)+int(i+1 in black)) & 1}
    return ''.join(out)


def main():
    languages = {}
    first = None
    checked = 0
    for n in range(1, 8):
        counts = Counter(packed(seed, n) for seed in range(1 << (2*n-1)))
        assert all('11' not in word for word in counts)
        if n <= 4:
            for seed in range(1 << (2*n-1)):
                assert packed(seed, n) == literal(seed, n)
                checked += 1
        languages[n] = set(counts)
        missing = [format(i, '0%db' % n) for i in range(1 << n)
                   if '11' not in format(i, '0%db' % n)
                   and format(i, '0%db' % n) not in counts]
        total = sum(counts.values())
        collision = Fraction(sum(c*c for c in counts.values()), total*total)
        print('n=%d inputs=%d words=%d collision=%s extra_missing=%d' %
              (n, total, len(counts), collision, len(missing)))
        if missing and first is None:
            first = missing[0]
        if n == 1:
            assert len(counts) == 2
        if n == 2:
            assert counts == {'00':3, '01':1, '10':4}
            assert collision == Fraction(13,32)
            assert len(set(counts.values())) > 1  # uniform CF refuted
    print('BC0/BC1 PASS; literal comparisons=%d; CF REFUTED' % checked)
    print('BC2 %s' % ('HELD' if first else 'REFUTED'))
    if first:
        proper = {first[a:b] for a in range(len(first))
                  for b in range(a+1, len(first)+1) if b-a < len(first)}
        assert all(word in languages[len(word)] for word in proper)
        print('UNEXPECTED shortest extra missing=%s; proper factors all admitted' % first)
    else:
        print('UNEXPECTED no extra missing word through declared horizon')
    print('ALL CHECKS PASS')


if __name__ == '__main__':
    main()
