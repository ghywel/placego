#!/usr/bin/env python3
"""rule30_rung3_strip.py: RG, the strip-graph certificate (entry 38's method, Local's SG) applied to every primitive
column word of period 2 .. 6. That covers Rung 3 (PERIOD-TWO.md §6, "periods 3 to 6", parked since 2026-10-06) and,
in passing, the Condrey white end's words 1 0^q. Drawn by Local under draw-and-work (seed 1791577080, chat L488);
predictions pushed before the run.

RUN-ON:     cpu (Python 3, standard library); minutes
COMMAND:    python3 tests/probes/lexicon/rule30_rung3_strip.py [RADIUS=6] [PMAX=6]

The same relaxation as rule30_isolated_zero_strip.py (GC805), with the column word w in place of 0 1^q and the strip
radius as a parameter.
  - A vertex is a row on positions -R .. R, with a phase in 0 .. p - 1; the centre equals w[phase].
  - An edge applies Rule 30 exactly on -(R - 1) .. R - 1, leaves the two outer cells free, and advances the phase.
  - Every actual strip of a history whose column 0 eventually reads w (periodically) is an infinite path, so it ends in
    a cyclic strongly connected component.
  - For each cyclic component, take P = the gcd of its cycle lengths and its P time classes.
    - If column -1 or column +1 takes one value per class in every cyclic component, then by Jen's theorem with a clock
      (PROOFS.md entry 5) no finite nonzero seed has a column eventually reading w: the word PASSES.
    - A graph with no cyclic component excludes w outright (GC811's EXCLUDED-ACYCLIC).
    - A component forcing neither column is a failure of the certificate, not a counterexample.
GC811: passes are monotone in the radius, so a word that passes at R also passes at R + 1.

PREDICTIONS (Local's, published before the run):
  RG-C1 (control): at radius 6, the period-2 word 01 FAILS (SG-C2). The words 0 1^q for p = 3 .. 6 (011, 0111, 01111,
        011111) FAIL, reproducing SG's q = 2 .. 5, with the same component sizes as SG.
  RG-P1 (blind, confidence 0.4): at radius 6, at least one primitive word of period 3 .. 6 PASSES (or is
        EXCLUDED-ACYCLIC).
  RG-P2 (blind, confidence 0.3): at radius 7, at least one word that fails at radius 6 passes.
  RG-D1 (descriptive): per word, the cyclic components (count, sizes, periods) and the side each forces.
"""
import sys
from math import gcd


def necklaces(p):
    """primitive binary necklaces of length p, as least-rotation strings"""
    out = []
    for n in range(1 << p):
        s = format(n, '0%db' % p)
        rots = [s[i:] + s[:i] for i in range(p)]
        if s == min(rots) and len(set(rots)) == p:
            out.append(s)
    return out


def build(R):
    W = 2 * R + 1
    inner = []
    for r in range(1 << W):
        out = 0
        for k in range(1, W - 1):
            b = ((r >> (k - 1)) & 1) ^ (((r >> k) & 1) | ((r >> (k + 1)) & 1))
            out |= b << k
        inner.append(out)
    return W, inner


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
                    u = work[-1][0]
                    low[u] = min(low[u], low[v])
                if low[v] == index[v]:
                    comp = []
                    while True:
                        w = stack.pop(); on[w] = False; comp.append(w)
                        if w == v:
                            break
                    comps.append(comp)
    return comps


def analyse(word, R, W, inner):
    p = len(word)
    want = [int(c) for c in word]
    C, L, Rt = R, R - 1, R + 1                       # bit k is position k - R
    verts = [(r, ph) for ph in range(p) for r in range(1 << W) if ((r >> C) & 1) == want[ph]]
    idx = {v: i for i, v in enumerate(verts)}
    succ = [[] for _ in verts]
    for i, (r, ph) in enumerate(verts):
        nph = (ph + 1) % p
        base = inner[r]
        if ((base >> C) & 1) != want[nph]:
            continue
        for outer in (0, 1, 2, 3):
            r2 = base | (outer & 1) | ((outer >> 1) << (W - 1))
            succ[i].append(idx[(r2, nph)])
    comps = sccs(len(verts), succ)
    res = []
    for comp in comps:
        cs = set(comp)
        if len(comp) == 1 and comp[0] not in succ[comp[0]]:
            continue
        root = comp[0]
        level, queue = {root: 0}, [root]
        for v in queue:
            for w2 in succ[v]:
                if w2 in cs and w2 not in level:
                    level[w2] = level[v] + 1
                    queue.append(w2)
        P = 0
        for v in comp:
            for w2 in succ[v]:
                if w2 in cs:
                    P = gcd(P, level[v] + 1 - level[w2])
        P = abs(P)
        forced = {}
        for side, bit in (('-1', L), ('+1', Rt)):
            vals, ok = {}, True
            for v in comp:
                if vals.setdefault(level[v] % P, (verts[v][0] >> bit) & 1) != (verts[v][0] >> bit) & 1:
                    ok = False
                    break
            forced[side] = ok
        res.append((len(comp), P, forced))
    return res


def verdict(res):
    if not res:
        return 'EXCLUDED-ACYCLIC'
    bad = [c for c in res if not (c[2]['-1'] or c[2]['+1'])]
    return 'PASS' if not bad else 'FAIL (%d of %d forcing neither)' % (len(bad), len(res))


def main():
    R = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    PMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    W, inner = build(R)
    out = {}
    for p in range(2, PMAX + 1):
        for word in necklaces(p):
            res = analyse(word, R, W, inner)
            v = verdict(res)
            out[word] = (v, res)
            desc = '; '.join('size %d P %d forces %s' % (n, P, '/'.join(s for s in ('-1', '+1') if f[s]) or 'NONE')
                             for n, P, f in sorted(res, key=lambda c: -c[0])[:4])
            print('radius %d, p = %d, w = %-7s %s; %d cyclic: %s%s' % (R, p, word, v, len(res), desc,
                                                                      ' ...' if len(res) > 4 else ''), flush=True)
    good = lambda v: v == 'PASS' or v == 'EXCLUDED-ACYCLIC'
    if R == 6:
        c1 = not good(out['01'][0]) and all(not good(out[w][0]) for w in ('011', '0111', '01111', '011111') if w in out)
        sys.argv = sys.argv[:1]
        sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
        import rule30_isolated_zero_strip as sg
        for q, w in ((1, '01'), (2, '011'), (3, '0111'), (4, '01111'), (5, '011111')):
            if w in out:
                c1 &= sorted((n, P, f['-1'], f['+1']) for n, P, f in sg.analyse(q)) == \
                    sorted((n, P, f['-1'], f['+1']) for n, P, f in out[w][1])
        print('RG-C1', 'PASS' if c1 else 'FAIL')
        passing = [w for w in out if len(w) >= 3 and good(out[w][0])]
        print('RG-P1', ('HELD %s' % passing) if passing else 'REFUTED')
    else:
        passing = [w for w in out if len(w) >= 3 and good(out[w][0])]
        print('passing at radius %d: %s' % (R, passing or 'none'))
    print('COMPLETE')


if __name__ == '__main__':
    main()
