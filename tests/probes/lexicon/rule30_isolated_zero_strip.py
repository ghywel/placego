#!/usr/bin/env python3
"""rule30_isolated_zero_strip.py: SG, an independent reimplementation of the strip-graph certificate for the black-end
walls 0 1^q (an external agent-run repository claims exclusions for q = 7 and every q >= 9; Cloud's CL085 item 1).
Built only from GPT's specification in GC805 (RULE30-GPT.md); no third-party code was downloaded or run. Local's run
(chat L428), with these predictions pushed before it.

RUN-ON:     cpu (Python 3, standard library); minutes
COMMAND:    python3 tests/probes/lexicon/rule30_isolated_zero_strip.py [QMAX=16]

The relaxation (GC805). A vertex is a row on positions -6 .. 6 with a phase in 0 .. q; the centre (position 0) is 0 at
phase 0 and 1 at phases 1 .. q, so column 0 reads 0 1^q with period p = q + 1. An edge applies Rule 30 exactly to
positions -5 .. 5 (x'(i) = x(i - 1) xor (x(i) or x(i + 1))), leaves the new row's two outer cells free, and advances the
phase by one (mod q + 1). Every actual strip of a Rule 30 history whose column 0 follows 0 1^q from some time on is an
infinite path in this graph, whatever lies outside the strip, so it ends in one cyclic strongly connected component.
For each cyclic component, the period P is the gcd of its cycle lengths (from BFS levels), and its vertices fall into
P time classes. If column -1 or column +1 takes one value on each class, every path in the component makes that column
periodic, and two adjacent eventually periodic columns are impossible from a finite nonzero seed (Jen's theorem with a
clock, PROOFS.md entry 5). So a q at which every cyclic component forces column -1 or +1 excludes the wall 0 1^q for
finite seeds. A component that forces neither is a failure of the certificate, not a counterexample to the wall.

PREDICTIONS (Local's, published before the run):
  SG-C1 (control, from the repository's own claim as GPT read it): q = 8 fails (some cyclic component forces neither
        column -1 nor +1).
  SG-C2 (control): q = 1, the period-2 wall 0101..., fails. A pass there would exclude period 2 for finite seeds, so it
        would mean a bug (confidence 0.97).
  SG-P1 (blind, confidence 0.75): q = 7 and every q from 9 to 16 pass.
  SG-D1 (descriptive): for q = 1 .. 16, the cyclic components (count, sizes, periods) and which side each forces.
  Counterfactual: a failure at 7 or at some q in 9 .. 16 means the repository's finite certificate does not hold as
  specified (or the specification differs from its code), whatever the uniform proof says.
OUTCOME, 2026-10-09 16:10 BST (M5, 1.4 s, run at commit 7848e5ad): SG-C1 PASS, SG-C2 PASS, SG-P1 HELD.
  q = 1: one cyclic component of 84 vertices, period 2, forcing neither (the 84-ring's strip, as expected). q = 2 .. 6
  and 8 fail too (one component forcing neither; q = 2 and 4 also have a small component that forces both). q = 7 and
  every q from 9 to 16: exactly one cyclic component, period p = q + 1, forcing column -1 (not +1); sizes 218 at q = 7,
  then 14q + 74 for q >= 9.
  So, by Jen's theorem with a clock (PROOFS.md entry 5), no finite nonzero seed has a column that eventually reads
  0 1^q with q = 7 or 9 <= q <= 16 (p = 8 and 10 .. 17). The method is the external repository's (cochon123/rule30-prize,
  pinned 3915b39, read by GPT in GC805); its finite cases are here reproduced independently. Its uniform claim (every
  q >= 9) is NOT established: GPT's GC805 found a gap in its Lemma F.
  Exploratory, after the run (no predictions): q = 17 .. 40 all pass with the same shape (one component, size 14q + 74,
  period q + 1, column -1 forced). Consistent with the uniform claim, and a hint at what a uniform proof must describe;
  not a proof.
"""
import sys
from math import gcd

W = 13
CENTRE, LEFT, RIGHT = 6, 5, 7                  # bit k is position k - 6


def inner(r):
    """the 11 updated cells on positions -5 .. 5, as bits 1 .. 11 of a 13-bit row"""
    out = 0
    for k in range(1, W - 1):
        b = ((r >> (k - 1)) & 1) ^ (((r >> k) & 1) | ((r >> (k + 1)) & 1))
        out |= b << k
    return out


INNER = [inner(r) for r in range(1 << W)]


def graph(q):
    p = q + 1
    want = [0] + [1] * q                       # centre value at each phase
    verts = [(r, ph) for ph in range(p) for r in range(1 << W) if ((r >> CENTRE) & 1) == want[ph]]
    idx = {v: i for i, v in enumerate(verts)}
    succ = [[] for _ in verts]
    for i, (r, ph) in enumerate(verts):
        nph = (ph + 1) % p
        base = INNER[r]
        if ((base >> CENTRE) & 1) != want[nph]:
            continue
        for outer in (0, 1, 2, 3):
            r2 = base | (outer & 1) | ((outer >> 1) << (W - 1))
            succ[i].append(idx[(r2, nph)])
    return verts, succ


def sccs(n, succ):
    """iterative Tarjan; returns a list of components (lists of vertex ids)"""
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


def analyse(q):
    verts, succ = graph(q)
    comps = sccs(len(verts), succ)
    out = []
    for comp in comps:
        cs = set(comp)
        if len(comp) == 1 and comp[0] not in succ[comp[0]]:
            continue                            # not cyclic
        root = comp[0]
        level, queue = {root: 0}, [root]
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
        for side, bit in (('-1', LEFT), ('+1', RIGHT)):
            vals = {}
            ok = True
            for v in comp:
                c = level[v] % P
                b = (verts[v][0] >> bit) & 1
                if vals.setdefault(c, b) != b:
                    ok = False
                    break
            forced[side] = ok
        out.append((len(comp), P, forced))
    return out


def main():
    qmax = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    verdict = {}
    for q in range(1, qmax + 1):
        res = analyse(q)
        bad = [c for c in res if not (c[2]['-1'] or c[2]['+1'])]
        verdict[q] = not bad and bool(res)
        desc = '; '.join('size %d P %d forces %s' % (n, P, '/'.join(s for s in ('-1', '+1') if f[s]) or 'NONE')
                         for n, P, f in sorted(res, key=lambda c: -c[0])[:6])
        print('q = %2d (p = %2d): %d cyclic components, %s; %s%s' % (
            q, q + 1, len(res), 'PASS' if verdict[q] else 'FAIL (%d forcing neither)' % len(bad), desc,
            ' ...' if len(res) > 6 else ''), flush=True)
    print('SG-C1', 'PASS' if qmax >= 8 and not verdict[8] else 'FAIL')
    print('SG-C2', 'PASS' if not verdict[1] else 'FAIL')
    ps = [7] + list(range(9, qmax + 1))
    print('SG-P1', 'HELD' if all(verdict[q] for q in ps) else 'REFUTED at q = %s' % [q for q in ps if not verdict[q]])
    print('COMPLETE')


if __name__ == '__main__':
    main()
