#!/usr/bin/env python3
"""rule30_isolated_zero_wide.py: SGW, the black-end strip-graph certificate (rule30_isolated_zero_strip.py, SG) on wider
strips, for the walls still open after SG and WT: 0 1^q with q = 2 .. 6 and 8 (p = 3 .. 7 and 9). Local's own-lane
step (chat L432), with these predictions pushed before the run.

RUN-ON:     cpu (Python 3, standard library); minutes
COMMAND:    python3 tests/probes/lexicon/rule30_isolated_zero_wide.py [RMAX=8]

The relaxation is SG's at radius R: rows on positions -R .. R with a phase in 0 .. q, centre 0 at phase 0 and 1 after;
an edge updates positions -(R - 1) .. R - 1 exactly and leaves the two outer cells free. A wider strip keeps more of
the real dynamics, so it can only remove paths that a narrower strip allowed through its free cells. The test per
cyclic component is SG's: does column -1 or +1 take one value on each time class of the component's period? A pass at
q, with Jen's theorem with a clock (PROOFS.md entry 5), excludes the wall 0 1^q for finite nonzero seeds.

PREDICTIONS (Local's, published before the run):
  SGW-C1 (control): q = 7 passes at R = 7 and R = 8, as at R = 6.
  SGW-C2 (control): q = 1 (period 2) fails at every R tried (confidence 0.97; a pass would exclude period 2).
  SGW-P1 (blind, confidence 0.5): q = 8 passes at R = 7 or R = 8.
  SGW-P2 (blind, confidence 0.4): some q in 2 .. 6 passes at some R <= 8.
  SGW-D1 (descriptive): for each R = 6, 7, 8 and q = 1 .. 8, the cyclic components (count, sizes, periods, forced side).
  Counterfactual: if nothing new passes by R = 8, the strip method stalls on these walls at affordable widths, and the
  open cases need a different argument (the WT style of forcing, or real right-side compatibility).
OUTCOME, 2026-10-09 16:13 BST (M5, about a minute, run at commit 15608467): SGW-C1 PASS, SGW-C2 PASS, SGW-P1 REFUTED,
  SGW-P2 REFUTED. At R = 7 and 8, q = 7 still passes (one component, period 8, column -1 forced; 376 and 656
  vertices), and every open wall still fails: q = 1 .. 6 and 8 each keep one large component forcing neither neighbour
  (q = 1: 84, 150, 264 vertices at R = 6, 7, 8), beside small components that force both.
  Exploratory, after the run (no predictions): ring orbits whose column 0 reads exactly 0 1^q, searched over every row
  of rings of 2 .. 22 cells (3000 steps, last 48 checked; one witness per q re-verified over 400 steps): q = 1 (7, 14,
  21 cells; row 0001001), q = 2 (12; 000011111001), q = 3 (7, 14, 21; 0000001), q = 4 (15; 001011010001111), q = 6
  (15; 000001011000011); none for q = 5, 7 or 8. A ring is an infinite configuration, so this excludes nothing and
  proves nothing about strip certificates (a ring's strip passes the class test on its own cycle); it records which open
  walls have exact periodic models, the shape a counter-model library (CL084) wants.
"""
import sys
from math import gcd


def build(R, q):
    W = 2 * R + 1
    C, mask = R, ((1 << (W - 1)) - 1) & ~1                            # centre bit; inner bits 1 .. W - 2
    p = q + 1
    want = [0] + [1] * q
    vid = {}
    verts = []
    for ph in range(p):
        for r in range(1 << W):
            if ((r >> C) & 1) == want[ph]:
                vid[(r, ph)] = len(verts)
                verts.append((r, ph))
    succ = [[] for _ in verts]
    for i, (r, ph) in enumerate(verts):
        base = ((r << 1) ^ (r | (r >> 1))) & mask
        nph = (ph + 1) % p
        if ((base >> C) & 1) != want[nph]:
            continue
        succ[i] = [vid[(base | o1 | (o2 << (W - 1)), nph)] for o1 in (0, 1) for o2 in (0, 1)]
    return verts, succ, C


def sccs(n, succ):
    index, low, on, stack, comps = [-1] * n, [0] * n, [False] * n, [], []
    counter = 0
    for s in range(n):
        if index[s] != -1:
            continue
        work = [(s, 0)]
        index[s] = low[s] = counter; counter += 1
        stack.append(s); on[s] = True
        while work:
            v, i = work[-1]
            if i < len(succ[v]):
                work[-1] = (v, i + 1)
                w = succ[v][i]
                if index[w] == -1:
                    index[w] = low[w] = counter; counter += 1
                    stack.append(w); on[w] = True
                    work.append((w, 0))
                elif on[w]:
                    low[v] = min(low[v], index[w])
            else:
                work.pop()
                if work:
                    low[work[-1][0]] = min(low[work[-1][0]], low[v])
                if low[v] == index[v]:
                    comp = []
                    while True:
                        w = stack.pop(); on[w] = False; comp.append(w)
                        if w == v:
                            break
                    if len(comp) > 1 or comp[0] in succ[comp[0]]:
                        comps.append(comp)
    return comps


def analyse(R, q):
    verts, succ, C = build(R, q)
    out = []
    for comp in sccs(len(verts), succ):
        cs = set(comp)
        level, queue = {comp[0]: 0}, [comp[0]]
        for v in queue:
            for w in succ[v]:
                if w in cs and w not in level:
                    level[w] = level[v] + 1
                    queue.append(w)
        P = 0
        for v in comp:
            for w in succ[v]:
                if w in cs:
                    P = gcd(P, level[v] + 1 - level[w])
        P = abs(P)
        forced = {}
        for side, b in (('-1', C - 1), ('+1', C + 1)):
            vals, ok = {}, True
            for v in comp:
                if vals.setdefault(level[v] % P, (verts[v][0] >> b) & 1) != (verts[v][0] >> b) & 1:
                    ok = False
                    break
            forced[side] = ok
        out.append((len(comp), P, forced))
    return out


def main():
    rmax = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    passed = {}
    for R in range(6, rmax + 1):
        for q in range(1, 9):
            res = analyse(R, q)
            ok = bool(res) and all(f['-1'] or f['+1'] for _, _, f in res)
            passed[(R, q)] = ok
            desc = '; '.join('%d P%d %s' % (n, P, '/'.join(s for s in ('-1', '+1') if f[s]) or 'NONE')
                             for n, P, f in sorted(res, key=lambda c: -c[0])[:5])
            print('R = %d, q = %d: %s, %d cyclic components: %s' % (R, q, 'PASS' if ok else 'FAIL', len(res), desc),
                  flush=True)
    rs = [R for R in (7, 8) if R <= rmax]
    print('SGW-C1', 'PASS' if all(passed[(R, 7)] for R in rs) else 'FAIL')
    print('SGW-C2', 'PASS' if not any(passed[(R, 1)] for R in range(6, rmax + 1)) else 'FAIL')
    print('SGW-P1', 'HELD' if any(passed[(R, 8)] for R in rs) else 'REFUTED')
    new = sorted((q, R) for (R, q), ok in passed.items() if ok and 2 <= q <= 6)
    print('SGW-P2', ('HELD %s' % new) if new else 'REFUTED')
    print('COMPLETE')


if __name__ == '__main__':
    main()
