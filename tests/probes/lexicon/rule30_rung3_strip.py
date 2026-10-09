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
OUTCOME, 2026-10-09 21:20 BST (M5; radius 6: 0.7 s; 7: 2.4 s; 8: 10.6 s and 241 MB; run at commit 9a1d37aa): RG-C1 PASS,
  RG-P1 REFUTED, RG-P2 REFUTED.
  - RG-C1: at radius 6, 01 and the words 0 1^q (p = 3 .. 6) fail with exactly SG's components.
  - No primitive word of period 3 .. 6 passes at radius 6, 7 or 8. Every one has a large cyclic component forcing
    neither column -1 nor +1, which grows with the radius (for 01: 84, 150, 264 vertices).
  - Small components that force both sides exist beside it.
  - So the strip-graph certificate does not reach Rung 3 at these radii.
RING OBSTRUCTION (registered 21:20 BST, before running; COMMAND: ... rule30_rung3_strip.py rings [NMAX=18]):
  - A Rule 30 ring (a spatially periodic row of length n) whose column 0 has least temporal period p reading w, and
    whose column -1 and column +1 both have least periods not dividing p, gives an infinite path in every strip
    relaxation, at every radius below n/2.
  - The component holding that path cannot force either neighbour on P | p classes. So such a word can never pass
    the strip test at radius < n/2. This explains the failures; it is not an exclusion.
  RG-P3 (blind, confidence 0.6): every primitive word of period 3 .. 6 has such a ring witness with n <= 18.
  RG-D2 (descriptive): per word, the smallest n of a witness and the neighbour periods.
RING OUTCOME, 2026-10-09 21:21 BST (M5, 1.9 s, run at commit d886c141): RG-P3 REFUTED. No word of period 3 .. 6 has a ring
  witness up to n = 18.
  - Instrument check (scratch, after the run): the ring step matches literal Rule 30.
  - Small column periods are rare on rings: period 3 only at n = 12, period 4 at n = 7 and 14, period 5 at n = 5, 10
    and 15, period 7 at n = 15. In each case the neighbouring columns' periods divide the column's.
  - So rings do not explain the strip failures. The non-forcing components come from aperiodic configurations, or from
    the relaxation itself.
RADIUS 9 (registered 21:21 BST, before running; about 1 GB): RG-P4 (blind, confidence 0.2): some word of period 3 .. 6
  passes at radius 9.
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


def rings(NMAX=18):
    """ring witnesses: a cycle state of Rule 30 on a ring of length n, with column 0 of least period p reading w and both
    neighbour columns of least periods not dividing p"""
    def step(x, n):
        m = (1 << n) - 1
        l = ((x << 1) | (x >> (n - 1))) & m        # left neighbour of bit i is bit i - 1 (cyclic)
        r = ((x >> 1) | (x << (n - 1))) & m        # right neighbour is bit i + 1
        return l ^ (x | r)
    def lp(seq):
        T = len(seq)
        return next(d for d in range(1, T + 1) if T % d == 0 and all(seq[t] == seq[(t + d) % T] for t in range(T)))
    targets = set()
    for p in range(3, 7):
        targets |= set(necklaces(p))
    found = {}
    for n in range(3, NMAX + 1):
        m = (1 << n) - 1
        seen_cycle = set()
        nxt = [0] * (1 << n)
        for x in range(1 << n):
            nxt[x] = step(x, n)
        # cycle states: iterate the map until the image stabilises
        cur = set(range(1 << n))
        while True:
            img = {nxt[x] for x in cur}
            if img == cur:
                break
            cur = img
        done = set()
        for x0 in cur:
            if x0 in done:
                continue
            cyc = [x0]
            y = nxt[x0]
            while y != x0:
                cyc.append(y)
                y = nxt[y]
            done |= set(cyc)
            T = len(cyc)
            for c in range(n):
                col = [(s >> c) & 1 for s in cyc]
                p = lp(col)
                if p < 3 or p > 6:
                    continue
                s = ''.join(map(str, col[:p]))
                w = min(s[i:] + s[:i] for i in range(p))
                if w not in targets or w in found:
                    continue
                pl = lp([(s2 >> ((c - 1) % n)) & 1 for s2 in cyc])
                pr = lp([(s2 >> ((c + 1) % n)) & 1 for s2 in cyc])
                if p % pl and p % pr:
                    found[w] = (n, T, pl, pr)
        print('n = %2d: witnesses so far %d of %d' % (n, len(found), len(targets)), flush=True)
        if len(found) == len(targets):
            break
    for w in sorted(targets, key=lambda z: (len(z), z)):
        print('  %-7s %s' % (w, ('ring n = %d, cycle length %d, neighbour periods %d, %d' % found[w]) if w in found else 'no witness'))
    print('RG-P3', 'HELD' if len(found) == len(targets) else 'REFUTED (%d without a witness)' % (len(targets) - len(found)))
    print('COMPLETE')


if __name__ == '__main__':
    rings(int(sys.argv[2]) if len(sys.argv) > 2 else 18) if sys.argv[1:2] == ['rings'] else main()
