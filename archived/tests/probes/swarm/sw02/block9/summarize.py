#!/usr/bin/env python3
"""Block 9: summary of ladder.out (runs 1-3 of lang.c). Usage: summarize.py ladder.out
Checks that word counts never rise with the strip width (the language is monotone: a cycle at width B + 1
projects onto a closed walk at width B, and an unlabelled SCC projects into an unlabelled one), and prints
the six-step growth (c(n)/c(n-6))^(1/6) at the longest length run for each (word, B)."""
import re, sys, math
runs = {}
cur = None
for line in open(sys.argv[1]):
    m = re.match(r'word (\S+) P \d+ B (\d+)', line)
    if m: cur = (m.group(1), int(m.group(2))); continue
    if line.startswith('counts'):
        c = list(map(int, line.split()[1:]))
        old = runs.get(cur)
        if old is None or len(c) > len(old): runs[cur] = c   # keep the longer enumeration
bad = []
for w in sorted({k[0] for k in runs}):
    bs = sorted(b for (ww, b) in runs if ww == w)
    for b1, b2 in zip(bs, bs[1:]):
        c1, c2 = runs[(w, b1)], runs[(w, b2)]
        for n in range(min(len(c1), len(c2))):
            if c2[n] > c1[n]: bad.append((w, b1, b2, n + 1, c1[n], c2[n]))
print('monotone in B at every common length:', 'PASS' if not bad else f'FAIL {bad[:5]}')
print('word  B  n  c(n)  six-step growth  bits per tick')
for (w, b), c in sorted(runs.items()):
    n = len(c)
    if n < 12: continue
    g = (c[-1] / c[-7]) ** (1 / 6)
    print(f'{w:5} {b:2} {n:2} {c[-1]:5}  {g:.4f}  {math.log2(g) / len(w):.4f}')
