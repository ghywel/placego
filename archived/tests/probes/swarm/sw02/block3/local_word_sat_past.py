#!/usr/bin/env python3
"""local_word_sat_past.py (Local, 9 November 2026; S-16 construction, step 2b): can a gap word occur inside the gate
trap after the row has already spent P samples there?

Usage: python3 local_word_sat_past.py KIT_DIR WORD P [P ...]

One SAT instance per P. Time tau = 0 is an odd absolute time (a sample) at which the window (cells 1..16) is ONE of
the trap's 829 windows (a disjunction over selector variables, each forcing the 16 cells to its code). The head is
free over samples 0 .. P - 1 (the trap's closure already restricts it to gaps 3 and 5 after its first black), black
at sample P, and spells WORD from there. The rule on the light-cone triangle as in local_word_sat.py. SAT means some
right half that has been inside the trap for P samples reads WORD next; UNSAT, for every right half: once P samples
have passed inside the trap, WORD never starts (and the trap's closure makes that hold at every later time).

PREDICTION (written before this ran; clock read 22:07:09 UTC): the (4, 4, 4) word 3555535555355553 is SAT at P = 20
but UNSAT by P = 60: it is a transient word, possible only shortly after entry, which is why a million real gaps never
show it. Counterfactual: SAT at P = 60 and 100, so the word stays possible late and its absence is rarity.
Result (started 22:07:30 UTC): MISSED; the counterfactual happened. SAT at P = 20, 60 and 100 (4.3 s, 30.1 s,
248.5 s): the (4, 4, 4) word stays possible after 100 samples inside the trap.
"""
import re
import sys
import time
from pathlib import Path

from pysat.solvers import Cadical153

KIT, WORD = Path(sys.argv[1]), sys.argv[2]
PS = [int(x) for x in sys.argv[3:]]
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TRAP = [int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))]
assert len(TRAP) == 829
gaps = [int(c) for c in WORD]
wordheads = [1]
for g in gaps:
    wordheads += [0] * (g - 1) + [1]

for P in PS:
    D = P + len(wordheads) - 1
    T = 2 * D; M = T + 1
    vid = {}

    def v(tau, j):
        if (tau, j) not in vid:
            vid[(tau, j)] = len(vid) + 1
        return vid[(tau, j)]
    cl = []
    for tau in range(T):
        for j in range(1, M - tau):
            z = v(tau + 1, j); b = v(tau, j); c = v(tau, j + 1)
            if j == 1:
                a0 = 1 if tau % 2 == 1 else 0
                for bb in (0, 1):
                    for cc in (0, 1):
                        zz = a0 ^ (bb | cc)
                        cl.append([(-b if bb else b), (-c if cc else c), (z if zz else -z)])
            else:
                a = v(tau, j - 1)
                for aa in (0, 1):
                    for bb in (0, 1):
                        for cc in (0, 1):
                            zz = aa ^ (bb | cc)
                            cl.append([(-a if aa else a), (-b if bb else b), (-c if cc else c), (z if zz else -z)])
    for s, h in enumerate(wordheads):
        cl.append([v(2 * (P + s), 1) if h else -v(2 * (P + s), 1)])
    nv = len(vid)
    sel = [nv + 1 + i for i in range(len(TRAP))]
    cl.append(sel)
    for i, code in enumerate(TRAP):
        for j in range(16):
            cl.append([-sel[i], v(0, j + 1) if (code >> j) & 1 else -v(0, j + 1)])
    t0 = time.time()
    with Cadical153(bootstrap_with=cl) as S:
        res = S.solve()
        win = None
        if res:
            m = set(x for x in S.get_model() if x > 0)
            win = [code for i, code in enumerate(TRAP) if sel[i] in m][:1]
    print(f'{WORD} after P = {P} samples in the trap: {"SAT" if res else "UNSAT"}; {nv} cell variables, {len(cl)} clauses;'
          f' {time.time() - t0:.1f} s{"; start window " + str(win) if win else ""}', flush=True)
