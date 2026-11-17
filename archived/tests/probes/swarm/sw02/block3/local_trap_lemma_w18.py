#!/usr/bin/env python3
"""local_trap_lemma_w18.py (Local, 9 November 2026): the kit's gate trap lifted to 18 columns, and its gap language.

Usage: python3 local_trap_lemma_w18.py KIT_DIR

The lift: every 18-column window (columns 1..18 at an odd time) whose first 16 columns are a window of the kit's trap.
Columns 17 and 18 at the first step and column 17 at the second are now inside the window. The double step leaves
columns 19 (both steps) free, and its first 16 columns are the kit's step2 with the window's own column 17. So the
lifted set (829 * 4 = 3,316 windows) is closed, and a right half whose 16-column window is in the trap has its
18-column window in the lift. A gap word with no path in the lift is never read after entry, by every right half.

PREDICTION, written before the first run (19:21 UTC): the 16-column trap graph allows 3535353 (local_trap_lemma.py's
completeness says so), and the lift kills it, as CP-2.2 (SW02-RESULTS, COMPUTED) and Lee's R30-20261030-60990f (for
the one-cell seed R1, an 18-cell pool, Lean) both report. The lift's minimal forbidden words up to 14 gaps are the
five of width 16 plus 3535353 and a few longer ones (SW02-BACKLOG names 353555535353 and 553535555353 as candidates).
Counterfactual: 3535353 survives the lift, in which case CP-2.2's and Lee's exclusions use more than 18 columns or
more than the trap, and this route to it for every trapped right half is closed.

Record searched: SW02-RESULTS CP-2.2 (33 transient, no 3553, no 3535353 inside the kit's trap, tail entropy at most
0.12707, COMPUTED); SW02-BACKLOG CP-2 (C16, the 18-column statement for 3535353, the family 33, 3553, 3535353,
353555535353, 553535555353); known_find 3535353 (portal R30-20261030-60990f, Lee: R1 only, 33, 3553, 3535353 at every
index, an 18-cell window relaxation with 2,040 states).
"""
import re
import sys
from pathlib import Path

src = (Path(sys.argv[1]) / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TRAP = [int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))]
TS = set(TRAP)


def stepW(s, c, x, W):
    e = s | (x << W)
    return (((e << 1) | c) ^ (e | (e >> 1))) & ((1 << W) - 1)


def step2W(s, a, b, W):
    return stepW(stepW(s, 0, a, W), 1, b, W)


W = 18
LIFT = [w | (h << 16) for w in TRAP for h in range(4)]
LS = set(LIFT)
closed = all(step2W(w, a, b, W) in LS for w in LIFT for a in (0, 1) for b in (0, 1))
# the prefix of the lifted step is the kit's step: check
pref = all((step2W(w, a, b, W) & 0xFFFF) == step2W(w & 0xFFFF, (w >> 16) & 1, (stepW(w, 0, a, W) >> 16) & 1, 16)
           for w in LIFT for a in (0, 1) for b in (0, 1))
print('lift: windows', len(LIFT), 'closed', closed, '; prefix of the lifted step = kit step with own column 17:', pref)


def succ(w, Wd, S_ok):
    return {v for a in (0, 1) for b in (0, 1) for v in [step2W(w, a, b, Wd)]}


def after_gap(S, g, Wd):
    for k in range(g):
        y = 1 if k == g - 1 else 0
        S = {v for w in S for v in succ(w, Wd, None) if (v & 1) == y}
    return frozenset(S)


def language(START, Wd, NMAX):
    allowed = {(): frozenset(w for w in START if w & 1)}
    frontier = [()]; forb = []
    for n in range(1, NMAX + 1):
        nxt = []
        for wd in frontier:
            for g in (3, 5):
                v = wd + (g,)
                S = after_gap(allowed[wd], g, Wd)
                if S:
                    allowed[v] = S; nxt.append(v)
                else:
                    forb.append(v)
        frontier = nxt
    return allowed, [v for v in forb if v[1:] in allowed]


for Wd, START, name in ((16, TRAP, 'trap (16 columns)'), (18, LIFT, 'lift (18 columns)')):
    allowed, minimal = language(START, Wd, 14)
    cnt = [sum(1 for v in allowed if len(v) == n) for n in range(15)]
    print(name, ': 3535353 allowed', (3, 5, 3, 5, 3, 5, 3) in allowed, '; minimal forbidden up to 14 gaps:',
          [''.join(map(str, v)) for v in minimal])
    print('   allowed counts by length', cnt, '; distinct path sets', len(set(allowed.values())))
