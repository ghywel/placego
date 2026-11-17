"""edge_levels_look.py: does the right edge's ruler continue past its first level for every half-ruler seed?

Local, 2026-10-26, after L1000 (DQ-022, Theorem E). An exploratory look: one run, over every seed to width 12,
300 steps. It answers a yes/no question; it is not a census toward a bound.

Question. Theorem E proves level 1 for every finite seed: in a half-ruler, the emitted widths alternate between exactly 2
and at least 3. For the single seed, the widths at least 3 again alternate between exactly 3 and at least 5, and so on
(8.73's ruler). Is level 2 universal too: for every half-ruler seed, do the widths of at least 3 alternate between one
fixed value and larger ones?

Predictions (written before the run):
  Q1  Level 2 is NOT universal: at least two different level-2 patterns occur among half-ruler seeds.
  Q2  Every half-ruler seed's level-2 sequence is eventually periodic within 300 steps (the edge strip is autonomous,
      G249), but the period may exceed 2.
  Q3  The single seed shows 3, >= 5 alternating (8.73).
Counterfactual: if every half-ruler seed shows the same level-2 alternation from the start, level 2 is universal, and
a hand proof of the whole hierarchy becomes the next block.
Record searched: "half-ruler" 0 (introduced in L1000), "edge.{0,20}triangle" (8.73, 8.68), "Right-prefix periods" (G249).

Run: python3 -I tests/probes/wolfram/edge_levels_look.py

Outcome (2026-10-26, M5, 0.45 s):
- Q1 held: level 2 is not one pattern; it is (3, >= 5) for 1,028 half-ruler seeds and (3, 4) for 1,020.
- But every half-ruler seed alternates exactly 3 with something larger. That led to the hand levels 2 and 3, then
  to edge_hierarchy_look.py and Theorem U (L1001).
- Q2 held. Q3 held: the single seed shows 3, 5, 3, 6, 3, 5, 3, 8, ...
"""
from collections import Counter

T = 300


def emissions(seed_int):
    xi = seed_int << (T + 4)
    prevL = None
    out = []
    for t in range(T):
        e = xi.bit_length() - 1
        L = 0
        while (xi >> (e - L)) & 1:
            L += 1
        if prevL is not None and prevL >= 2:
            k = 0
            while not (xi >> (e - 1 - k)) & 1:
                k += 1
            out.append(k)
        prevL = L
        xi = (xi << 1) ^ (xi | (xi >> 1))
    return out


patterns = Counter()
examples = {}
for w in range(1, 13):
    for bits in range(1 << (w - 1)):
        s = bits | (1 << (w - 1))
        ws = emissions(s)
        if 1 in ws[1:]:
            continue                                   # rain edge
        big = [v for v in ws if v >= 3]
        tail = big[10:]                                # skip transients
        # level-2 shape: is every other value one constant, and what are the two interleaved streams?
        a, b = tail[0::2], tail[1::2]
        if len(set(a)) == 1:
            key = ("alternating", a[0], min(b))
        elif len(set(b)) == 1:
            key = ("alternating", b[0], min(a))
        else:
            key = ("not alternating", tuple(tail[:8]))
        patterns[key] += 1
        examples.setdefault(key, (bin(s)[2:][::-1], big[:12]))
print("half-ruler seeds by level-2 shape:")
for key, n in patterns.most_common(12):
    print(" ", n, key, "e.g. seed", examples[key][0], "widths >= 3:", examples[key][1])
print("distinct shapes:", len(patterns))
