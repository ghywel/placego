#!/usr/bin/env python3
"""local_trap_ladder2.py (Local, 9 November 2026): the eventual gap language of the gate trap at widths 16..WMAX.

Usage: python3 local_trap_ladder2.py KIT_DIR [WMAX] [NGAPS]

local_trap_ladder.py found that the ladder keeps adding minimal forbidden words with width (3535353 at 18,
5335555535353 at 20, 53355555535353 at 22), but the two late ones begin with 533, the pair 33 allowed once just after
entry, so they look like transient start words. This probe separates the eventual language. At width W, let B0 be the
lift's windows with a black column 1 (all possible black cells after entry), and B(k+1) the windows at the next black
cell after a gap of 3 or 5 from B(k). The sequence is decreasing (B1 is inside B0 because every window after a gap
is a black lift window) and stabilises at the recurrent core C. The eventual language at width W is the gap language
read from C. It prints C's size, the step at which B(k) stabilises, the minimal forbidden words read from C up to NGAPS
gaps, and the per-sample entropy of the shift of finite type those words define (exact transfer count).

PREDICTION, written before the first run (first run started 20:17:01 UTC). The eventual minimal forbidden words are 33 and 3553 at width
16, and 33, 3553, 3535353 at widths 18, 20 and 22, with nothing new up to 20 gaps. So the eventual language stops
moving at width 18, and the transient start words are the only thing wider windows add. Entropy at width 18 and
above: CP-2.2's 0.12707 bit per sample (for the shift without 33, 3553, 3535353). Counterfactual: a new eventual word
at width 20 or 22, in which case S-16 is a genuine ladder (Block 9's shape: the language shrinks with width) and
deserves a research block of its own before any Lean.

First run (20:17:01 UTC): HELD to width 22 and 20 gaps. But local_trap_core18_complete.py then found disagreements
at widths 24 and 26 (histories ending 5535353, 3555353), so the eventual language moves again past 22.
ADDENDUM PREDICTION, before the second run (W to 26, 18 gaps; started 20:19:15 UTC): at 24 the new eventual minimal words are
of the 35353 kind, about 7 to 12 gaps long, and include one of the backlog's candidates (353555535353 or 553535555353);
26 adds more; the entropy keeps falling but stays above 0.10 bit per sample at 26. Counterfactual: a sharp drop
towards zero, which would make the limit language thin and S-16 a question about the left statement's kind.
Second run: (a) MISSED: width 24 adds nothing up to 18 gaps (its new words are longer: the product test sees them),
and width 26 adds five words of 14 to 18 gaps (35553535555353, 353555555535353, 3535355553555353, 3555553535555353,
353555555535355553), none of them the backlog's candidates. (b) HELD: the entropy of the shift these words define
falls only to 0.12604 at 26.

Record searched: local_trap_ladder.out (this session), L1608/GC2789/CL760, SW02-RESULTS CP-2.2 (tail entropy at
most 0.12707), SW02-BACKLOG CP-2 (candidates 353555535353, 553535555353; no structural law found).
"""
import math
import re
import sys
from pathlib import Path

import numpy as np

KIT = Path(sys.argv[1])
WMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 22
NG = int(sys.argv[3]) if len(sys.argv) > 3 else 20
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TRAP = np.array([int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))],
                dtype=np.int64)


def step(s, c, x, W):
    e = s | (x << W)
    return (((e << 1) | c) ^ (e | (e >> 1))) & ((1 << W) - 1)


def sft_entropy(F):
    """Per-sample entropy of the words over gaps 3, 5 with no factor in F: count words by sample length (DP on the
    last max|F|-1 gaps), and take the growth between sample lengths 2000 and 3000."""
    m = max(len(f) for f in F) - 1
    from collections import defaultdict
    N = 3000
    cnt = [defaultdict(int) for _ in range(N + 1)]
    cnt[0][()] = 1
    for n in range(N + 1):
        for st, c in list(cnt[n].items()):
            for g in (3, 5):
                h = st + (g,)
                if n + g <= N and not any(len(h) >= len(f) and h[-len(f):] == f for f in F):
                    cnt[n + g][h[-m:] if m else ()] += c
    tot = [sum(c.values()) for c in cnt]
    a, b = 2000, 3000
    s1 = sum(tot[a - 4:a + 1]); s2 = sum(tot[b - 4:b + 1])
    return (math.log2(s2) - math.log2(s1)) / (b - a)


for W in range(16, WMAX + 1, 2):
    lift = (TRAP[:, None] | (np.arange(1 << (W - 16), dtype=np.int64)[None, :] << 16)).ravel()
    order = np.argsort(lift); sl = lift[order]
    succ = np.empty((len(lift), 4), dtype=np.int64)
    k = 0
    for a in (0, 1):
        for b in (0, 1):
            v = step(step(lift, 0, a, W), 1, b, W)
            pos = np.searchsorted(sl, v)
            assert np.all(sl[np.minimum(pos, len(sl) - 1)] == v), 'lift not closed'
            succ[:, k] = order[pos]; k += 1
    head = (lift & 1).astype(bool)

    def after_gap(S, g):
        for j in range(g):
            nxt = np.zeros(len(lift), dtype=bool)
            nxt[succ[S].ravel()] = True
            S = np.flatnonzero(nxt & (head == (j == g - 1)))
            if len(S) == 0:
                break
        return S

    B = np.flatnonzero(head)
    sizes = [len(B)]
    for it in range(400):
        B2 = np.union1d(after_gap(B, 3), after_gap(B, 5))
        assert np.all(np.isin(B2, B)), 'not decreasing'
        if len(B2) == len(B):
            break
        B = B2; sizes.append(len(B))
    C = B
    allowed = {(): C}
    frontier = [()]
    forb = []
    for n in range(1, NG + 1):
        nf = []
        for wd in frontier:
            for g in (3, 5):
                v = wd + (g,)
                S = after_gap(allowed[wd], g)
                if len(S):
                    allowed[v] = S; nf.append(v)
                else:
                    forb.append(v)
        frontier = nf
    minimal = [v for v in forb if v[1:] in allowed]
    ent = sft_entropy(minimal) if minimal else None
    print(f'W={W}: lift {len(lift)}, black {sizes[0]}, recurrent core {len(C)} after {len(sizes) - 1} gap steps '
          f'(sizes {sizes[:6]}{"..." if len(sizes) > 6 else ""})', flush=True)
    print('   eventual minimal forbidden up to', NG, 'gaps:', [''.join(map(str, v)) for v in minimal], flush=True)
    print('   allowed words by gaps (last three):', [sum(1 for v in allowed if len(v) == n) for n in range(NG - 2, NG + 1)],
          '; entropy of the shift these words define:', round(ent, 5) if ent else None, 'bit per sample', flush=True)
