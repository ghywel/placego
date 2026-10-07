#!/usr/bin/env python3
"""rule30_dq3.py: DQ3, the nonlinear three-distance quotient test of RULE30-GPT.md §G172 (GPT's design; requested in
GC214; claimed by Local in CLOUD-LOCAL.md at 9639aa4 before this script was written or run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_dq3.py
COST:       seconds expected; caps 60 CPU s and 128 MiB RSS (GPT's).

Domain: HG4's clock-aligned gated compatible graph (rule30_hg4.py: aligned states at arrival phase 0, G160's gate,
plus the zero state), with doubled slope-5/2 reward 2 delta - 5. Each state maps to its feature
Phi = (D(A, 0), D(B, 0), D(A XOR B, 0)), D the reset distance (0 for a zero word). The quotient keeps, for each
ordered pair of features, the largest reward among the original edges between them and one edge attaining it. A
finite nonnegative F on features with F(x) >= w + F(y) on every quotient edge exists exactly when the quotient has
no positive-reward cycle (G8's finite criterion); F then lifts to every original gated edge by composition.

PREDICTIONS, GPT's, published in RULE30-GPT.md §G172 before this run:
  DQ-P1 (blind): q = 8 has a positive quotient cycle (nonlinear three-distance certificates fail there too).
  DQ-U (blind, the unexpected check): q = 4 has no positive quotient cycle.
  DQ-C1 (control): q = 1 and 2 have no positive quotient cycle (every original edge has reward <= -1).
  DQ-C2 (control): at q <= 4 every original edge is checked independently (scalar compatibility, gate bits, reset
        delay, feature labels); if F exists, every lifted original edge inequality is checked, not only
        representatives.
  DQ-CF (counterfactual): the q = 4 edge (8, 8) -> (8, 0), reward 3, must survive the compression and reject F = 0.
Required output: feature vertex and edge counts, the verdict, and either F with every lifted inequality checked or
a positive quotient cycle with each edge's labels, reward and actual pair/phase representative, each representative
checked by literal scalar equations, and whether successive representatives concatenate (they need not).

OUTCOME, 2026-10-07 (M5, one process; CPU 0.09 s, peak RSS 25.5 MiB). Feature vertices and quotient edges: 3 and 2
at q = 1, 10 and 11 at q = 2, 31 and 93 at q = 4 (from 137 gated edges), 109 and 1,070 at q = 8. DQ-C1 PASS: no
positive cycle at q = 1, 2 (F max 0, every lifted original inequality holds). DQ-C2 PASS: every original edge at
q <= 4 passes the literal scalar, gate, delay and feature checks. DQ-CF PASS. DQ-U REFUTED: q = 4 already has a
positive quotient cycle, a self-loop at feature (1, 3, 1) with reward 1, represented by (A, B) = (15, 12) -> (9, 4),
delay 3. DQ-P1 HELD: q = 8 has a positive cycle of three feature edges, total reward 17: (1, 4, 1) -> (3, 6, 3)
reward 3 by (203, 200) -> (140, 32); (3, 6, 3) -> (1, 6, 1) reward 7 by (236, 224) -> (131, 32); (1, 6, 1) ->
(1, 4, 1) reward 7 by (227, 224) -> (131, 8). Every representative passes the literal checks, and in neither cycle
do successive representatives concatenate, as GPT's interpretation guard expects: the positive cycles reject the
three-distance compression, not the underlying graph, whose feasibility at these periods is the G10 control.
"""
import os
import resource
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rule30_hg4 as hg                                   # noqa: E402
from rule30_gpt_cycles import bit                         # noqa: E402

CPU_CAP, MEM_CAP = 60.0, 128 * 1024 * 1024


def D(w, p):
    if not w:
        return 0
    u = 0
    while not bit(w, u, p):
        u += 1
    return u + 1


def feat(state, p):
    a, b = state >> p, state & ((1 << p) - 1)
    return (D(a, p), D(b, p), D(a ^ b, p))


def literal_edge_ok(s, t, d, p):
    """Scalar compatibility, gates, delay and alignment for one aligned edge, independently of the graph builder."""
    mask = (1 << p) - 1
    a, b = s >> p, s & mask
    tb, tc = hg.rotate(t >> p, -d, p), hg.rotate(t & mask, -d, p)
    ok = tb == b and all(bit(tc, x + 1, p) == (bit(a, x, p) ^ (bit(b, x, p) | bit(tc, x, p))) for x in range(p))
    ok &= d == D(b, p)
    ok &= (s == 0 or hg.gated(s, p)) and (t == 0 or hg.gated(t, p))
    return ok


def run(p, t0):
    count = 1 << (2 * p)
    isv = [v == 0 or hg.gated(v, p) for v in range(count)]
    edges = [(s, t, d) for s, t, d in hg.aligned_edges(p) if isv[s] and isv[t]]
    F = {v: feat(v, p) for v in range(count) if isv[v]}
    quot = {}
    for s, t, d in edges:
        key, w = (F[s], F[t]), 2 * d - 5
        if key not in quot or w > quot[key][0]:
            quot[key] = (w, (s, t, d))
    verts = sorted(set(F.values()))
    c2 = all(literal_edge_ok(s, t, d, p) for s, t, d in edges) if p <= 4 else None
    # Bellman-Ford longest paths with stopping (h >= 0); a positive cycle keeps relaxing after |V| rounds.
    h = {x: 0 for x in verts}
    pred = {}
    changed = True
    rounds = 0
    last = None
    while changed and rounds <= len(verts) + 1:
        changed = False
        rounds += 1
        for (x, y), (w, rep) in quot.items():
            if w + h[y] > h[x]:
                h[x] = w + h[y]
                pred[x] = y
                changed = True
                last = x
        if time.process_time() - t0 > CPU_CAP:
            return dict(stop='cpu cap')
    if not changed:
        lift = all(h[F[s]] >= 2 * d - 5 + h[F[t]] for s, t, d in edges)
        return dict(verdict='no positive cycle', nv=len(verts), ne=len(quot), maxF=max(h.values()), lift=lift, c2=c2,
                    quot=quot, nedges=len(edges))
    x = last
    for _ in range(len(verts)):
        x = pred[x]
    cyc, y = [x], pred[x]
    while y != x:
        cyc.append(y)
        y = pred[y]
    cyc.append(x)
    cedges = [(cyc[i], cyc[i + 1], quot[(cyc[i], cyc[i + 1])]) for i in range(len(cyc) - 1)]
    return dict(verdict='positive cycle', nv=len(verts), ne=len(quot), cycle=cedges, c2=c2, quot=quot, nedges=len(edges))


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (65, 65))
    t0 = time.process_time()
    res = {}
    for p in (1, 2, 4, 8):
        r = run(p, t0)
        res[p] = r
        if r.get('stop'):
            print('q = %d: CAP REACHED (%s): partial, not a result' % (p, r['stop']))
            return 2
        line = 'q = %d: feature vertices %d, quotient edges %d (from %d gated edges): %s' % (p, r['nv'], r['ne'],
                                                                                          r['nedges'], r['verdict'])
        if r['verdict'] == 'no positive cycle':
            line += '; F max %d; every lifted original inequality %s' % (r['maxF'], 'PASS' if r['lift'] else 'FAIL')
        if r['c2'] is not None:
            line += '; DQ-C2 literal edges %s' % ('PASS' if r['c2'] else 'FAIL')
        print(line, flush=True)
        if r['verdict'] == 'positive cycle':
            tot = sum(e[2][0] for e in r['cycle'])
            print('  cycle of %d feature edges, total reward %d:' % (len(r['cycle']), tot))
            conc = True
            for i, (x, y, (w, (s, t, d))) in enumerate(r['cycle']):
                ok = literal_edge_ok(s, t, d, p) and feat(s, p) == x and feat(t, p) == y and 2 * d - 5 == w
                mask = (1 << p) - 1
                print('   %r -> %r reward %d; representative (A, B) = (%d, %d) -> (%d, %d), delay %d; literal %s'
                      % (x, y, w, s >> p, s & mask, t >> p, t & mask, d, 'PASS' if ok else 'FAIL'))
                nxt = r['cycle'][(i + 1) % len(r['cycle'])][2][1][0]
                conc &= t == nxt
            print('  successive representatives concatenate: %s' % conc)
    cf = (((4, 4, 0), (4, 0, 4)) in res[4]['quot']) and res[4]['quot'][((4, 4, 0), (4, 0, 4))][0] >= 3
    print('DQ-CF', 'PASS (the q = 4 edge (8, 8) -> (8, 0) survives with reward 3 and rejects F = 0)' if cf else 'FAIL')
    print('DQ-C1', 'PASS' if all(res[p]['verdict'] == 'no positive cycle' for p in (1, 2)) else 'FAIL')
    print('DQ-U', 'HELD' if res[4]['verdict'] == 'no positive cycle' else 'REFUTED')
    print('DQ-P1', 'HELD' if res[8]['verdict'] == 'positive cycle' else 'REFUTED')
    rus = resource.getrusage(resource.RUSAGE_SELF)
    print('resources: CPU %.2f s, peak RSS %.1f MiB' % (time.process_time() - t0, rus.ru_maxrss / 1048576))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
