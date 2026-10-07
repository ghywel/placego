#!/usr/bin/env python3
"""rule30_rq3.py: RQ3, the root-reached clock quotient with least pair period, of RULE30-GPT.md §G175 (GPT's design;
requested in GC217; claimed by Local in CLOUD-LOCAL.md at 341e772 before this script was written or run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_rq3.py
COST:       seconds expected; caps 60 CPU s and 128 MiB RSS (GPT's).

Domain. Aligned states (A, B) of q-bit temporal words (bit t is time t), aligned so the front arrives at phase 0.
Start at the root (0, 2^q - 1) and follow every compatible child C (S C = A XOR (B OR C), closing at period q); the
edge's delay is the reset distance of B from phase 0 (0 for a zero driver) and its target is (B, C) rotated by that
delay. Only states reached this way are kept. A zero driver with odd block parity whose integration needs period 2q
has no q-periodic child: a cap exit, counted separately. Each reached state maps to (Phi, p): Phi = the three reset
distances (D(A, 0), D(B, 0), D(A XOR B, 0)) and p its least pair period. The quotient keeps the largest reward
2 delta - 5 per feature edge with a reached representative; a positive quotient cycle rejects every function of
(Phi, p) on this domain; otherwise the longest-reward potential F is lifted and checked on every retained edge.

PREDICTIONS, GPT's, published in RULE30-GPT.md §G175 before this run:
  RQ-P1 (blind): no positive feature cycle at q = 4 or q = 8.
  RQ-C1 (control): q = 1 and 2 pass, every edge reward being nonpositive.
  RQ-C2 (control): an independent absolute-time construction (brute-force children, scalar clock scans, every root
        phase) reproduces the aligned reached set and edges through q = 4; least pair periods, gates (all reached
        states but the root), compatibility and delays are verified.
  RQ-CF (counterfactual): at q = 4 the ambient DQ3 representative (15, 12) at clock 0 is not reached, while the
        aligned (15, 6) is reached at depth 10.
  Boundary checks: the root is not gated; its first edge costs 1 (reward -3) and enters the gate; cap exits are
        separate. Known word-tree depth ceilings 28 (q = 4) and 399 (q = 8) are controls.

OUTCOME, 2026-10-07 (M5, one process; CPU 0.05 s, peak RSS 9.8 MiB). Reached aligned states and edges: 3 and 2 at
q = 1, 9 and 9 at q = 2, 31 and 32 at q = 4, 409 and 411 at q = 8, one cap exit each; maximal depths 2, 7, 28, 399
(the depth controls hold). Gates on every reached state but the root, and the root boundary (first edge cost 1,
reward -3, gated target), PASS at every q. RQ-C1 PASS (max edge rewards -3 and -1). RQ-C2 PASS: the absolute-time
construction from every root phase reproduces the reached states and edges exactly through q = 4. RQ-CF PASS:
(15, 12) is unreached and (15, 6) is reached at depth 10. q = 4: no positive feature cycle (F max 1, every lifted
edge holds). RQ-P1 REFUTED at q = 8: a positive feature self-loop at (1, 5, 1, 8), reward 5, represented by the
reached edge (183, 176) -> (133, 208), delay 5, from depth 190 to 191. Checked after the run, outside the script's
verdicts: that edge is a literal compatible edge with identical features and both ends gated, and its full
191-edge root path, unaligned to absolute time, passes every triple and reset scan (arrival 365). The edge's
source and target differ, so it is not a real self-loop; it shows these features cannot separate two actually
reached states whose edge costs 5, so no function of them certifies any slope below 5 on the reached q = 8 domain.
"""
import resource
import sys
import time
from collections import deque


def bit(w, t, q):
    return (w >> (t % q)) & 1


def rot(w, d, q):
    d %= q
    return ((w >> d) | (w << (q - d))) & ((1 << q) - 1)


def D(w, q):
    if not w:
        return 0
    u = 0
    while not bit(w, u, q):
        u += 1
    return u + 1


def gated(a, b, q):
    if a:
        return bit(a, q - 1, q) == 1
    return (bit(b, 0, q) ^ bit(b, q - 1, q)) == 1


def children(a, b, q):
    """Children by the descending recursion from two seeds (as in the S46 helper), confirmed forward."""
    out = []
    for c0 in (0, 1):
        c = [c0]
        for t in range(q - 1):
            c.append(bit(a, t, q) ^ (bit(b, t, q) | c[t]))
        if bit(a, q - 1, q) ^ (bit(b, q - 1, q) | c[q - 1]) == c0:
            out.append(sum(v << t for t, v in enumerate(c)))
    return out


def children_brute(a, b, q):
    return [c for c in range(1 << q) if all(bit(c, t + 1, q) == bit(a, t, q) ^ (bit(b, t, q) | bit(c, t, q))
                                            for t in range(q))]


def pair_lp(a, b, q):
    for d in range(1, q + 1):
        if q % d == 0 and rot(a, d, q) == a and rot(b, d, q) == b:
            return d


def reached(q):
    root = (0, (1 << q) - 1)
    depth, parent, edges, exits = {root: 0}, {root: None}, [], 0
    todo = deque([root])
    while todo:
        a, b = todo.popleft()
        kids = children(a, b, q)
        if not kids:
            exits += 1
        d = D(b, q)
        for c in kids:
            tgt = (rot(b, d, q), rot(c, d, q))
            edges.append(((a, b), tgt, d))
            if tgt not in depth:
                depth[tgt] = depth[(a, b)] + 1
                parent[tgt] = ((a, b), d, c)
                todo.append(tgt)
    return root, depth, parent, edges, exits


def absolute_construction(q):
    """RQ-C2: literal pairs with absolute clocks from every root phase, brute-force children, scalar scans; then
    aligned by rotating each pair by its clock residue."""
    states, edges = set(), set()
    for t0 in range(q):
        start = (0, (1 << q) - 1, t0)
        seen, todo = {start}, [start]
        while todo:
            a, b, t = todo.pop()
            states.add((rot(a, t, q), rot(b, t, q)))
            u = t
            if b:
                while not bit(b, u, q):
                    u += 1
                u += 1
            for c in children_brute(a, b, q):
                edges.add(((rot(a, t, q), rot(b, t, q)), (rot(b, u, q), rot(c, u, q)), u - t))
                nxt = (b, c, u % q)
                if nxt not in seen:
                    seen.add(nxt)
                    todo.append(nxt)
    return states, edges


def feat(s, q):
    a, b = s
    return (D(a, q), D(b, q), D(a ^ b, q), pair_lp(a, b, q))


def root_path(parent, s):
    path = []
    while parent[s] is not None:
        prev, d, c = parent[s]
        path.append((prev, s, d, c))
        s = prev
    return list(reversed(path))


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (65, 65))
    t0 = time.process_time()
    verdict = {}
    for q in (1, 2, 4, 8):
        root, depth, parent, edges, exits = reached(q)
        F = {s: feat(s, q) for s in depth}
        gates_ok = all(gated(a, b, q) for (a, b) in depth if (a, b) != root) and not gated(*root, q)
        first = [e for e in edges if e[0] == root]
        boundary = len(first) == 1 and first[0][2] == 1 and 2 * first[0][2] - 5 == -3 and gated(*first[0][1], q)
        quot = {}
        for s, t, d in edges:
            key, w = (F[s], F[t]), 2 * d - 5
            if key not in quot or w > quot[key][0]:
                quot[key] = (w, (s, t, d))
        verts = sorted(set(F.values()))
        h = {x: 0 for x in verts}
        pred, changed, rounds, last = {}, True, 0, None
        while changed and rounds <= len(verts) + 1:
            changed, rounds = False, rounds + 1
            for (x, y), (w, rep) in quot.items():
                if w + h[y] > h[x]:
                    h[x], pred[x], changed, last = w + h[y], y, True, x
        line = ('q = %d: reached states %d, edges %d, cap exits %d, max depth %d; feature vertices %d, quotient edges '
                '%d; gates %s; root boundary %s' % (q, len(depth), len(edges), exits, max(depth.values()), len(verts),
                                                    len(quot), 'PASS' if gates_ok else 'FAIL',
                                                    'PASS' if boundary else 'FAIL'))
        if not changed:
            lift = all(h[F[s]] >= 2 * d - 5 + h[F[t]] for s, t, d in edges)
            verdict[q] = 'none'
            line += '; no positive feature cycle, F max %d, every lifted edge %s' % (max(h.values()),
                                                                                   'PASS' if lift else 'FAIL')
            if q <= 2:
                line += '; max edge reward %d' % max(2 * d - 5 for _, _, d in edges)
        else:
            verdict[q] = 'cycle'
            x = last
            for _ in range(len(verts)):
                x = pred[x]
            cyc, y = [x], pred[x]
            while y != x:
                cyc.append(y)
                y = pred[y]
            cyc.append(x)
            line += '; POSITIVE FEATURE CYCLE of %d edges' % (len(cyc) - 1)
        if q <= 4:
            st, ed = absolute_construction(q)
            c2 = st == set(depth) and ed == set(edges)
            line += '; RQ-C2 absolute construction %s' % ('PASS' if c2 else 'FAIL')
        print(line, flush=True)
        if verdict[q] == 'cycle':
            tot = 0
            for i in range(len(cyc) - 1):
                w, (s, t, d) = quot[(cyc[i], cyc[i + 1])]
                tot += w
                path = root_path(parent, s)
                ok = all(c in children_brute(a_, b_, q) for (a_, b_), tgt, dd, c in path)
                print('   %r -> %r reward %d; rep %r -> %r delay %d; root path of %d edges, literal %s'
                      % (cyc[i], cyc[i + 1], w, s, t, d, len(path), 'PASS' if ok else 'FAIL'))
            print('   total reward %d' % tot)
        if q == 4:
            cf = (15, 12) not in depth and depth.get((15, 6)) == 10
            print('RQ-CF', 'PASS ((15, 12) unreached; (15, 6) reached at depth 10)' if cf else 'FAIL (%r, %r)'
                  % ((15, 12) in depth, depth.get((15, 6))))
        if time.process_time() - t0 > 60 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 128 * 1024 * 1024:
            print('CAP REACHED after q = %d: partial, not a result' % q)
            return 2
    print('RQ-C1', 'PASS' if verdict[1] == 'none' and verdict[2] == 'none' else 'FAIL')
    print('RQ-P1', 'HELD' if verdict[4] == 'none' and verdict[8] == 'none' else 'REFUTED', verdict)
    rus = resource.getrusage(resource.RUSAGE_SELF)
    print('resources: CPU %.2f s, peak RSS %.1f MiB' % (time.process_time() - t0, rus.ru_maxrss / 1048576))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
