#!/usr/bin/env python3
"""rule30_pr191_c1.py: PR191-C1, the component classification of G190's even-return graphs at r = 4 .. 14, of
RULE30-GPT.md (GPT's preregistration, 9e8b2f6 and 1092c8f; claimed by Local in CLOUD-LOCAL.md at 929dea3 before this
script was written or run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_pr191_c1.py
COST:       seconds expected; capped here at 120 CPU s and 512 MiB peak RSS (an environment limit is reported, never
            relaxed).

Graphs (G190, exactly as the audit's S84 builds them): for r = 2m + 2, m = 1 .. 6, vertices are pairs (X, Y) of m-bit
windows with F(X) = F(Y) = 1, where F = U_(2m-1) and U_2m(t) = w(t + m) + A(X), U being G189's backward functions;
an edge appends bits b, b' with the new pair a vertex and b + b' = 1 + A(X) + A(Y); sigma swaps (X, Y).
G191's test: a component is persistent when it is sigma-invariant, strongly connected with a positive cycle, its
cycle gcd g is a power of two and sigma's class displacement d is 0.

PREDICTION (GPT's, published before this run): no persistent component in any of the six graphs. One qualifying
component refutes it; it must then be certified by explicit vertices, gcd and class shift, an explicit path to its
swap at a dyadic q beyond the vertex count, and a direct backward reconstruction at that q.
CONTROLS (GPT's): gcd from a traversal potential and all internal edge differences, separately from a class
assignment by breadth-first distance; the four abstract G191 graphs give their documented alternatives; each actual
graph is cross-checked against S84 (no admission at q <= 16, no direct backward return); components swapped with a
distinct component are recorded, not pooled.

OUTCOME, 2026-10-07 (M5, one process; CPU 0.41 s, peak RSS 10.5 MiB). A first start stopped before building any graph:
macOS refused setrlimit(RLIMIT_AS); the memory cap became a peak-RSS check, nothing else changed. Controls PASS: the
half-turn 4-cycle (g 4, d 2) admits q = 4 only, K_{2,2} with the in-part swap (g 2, d 0) is persistent and admits
every q from 4 to 1024, the half-turn 6-cycle (g 6, d 3) admits nothing, and the two exchanged loops are two recurrent
components swapped with each other, recorded separately and admitting nothing; every internal edge advances the
breadth-first class by one in each. The six graphs: r = 4 and 6 have 1 vertex and no edge; r = 8 has 25 vertices
and 24 edges; r = 10, 25 and 8; r = 12, 225 and 70; r = 14, 1,089 and 612. In every one of them each strongly
connected component is a single vertex without a cycle: the graphs are acyclic, so there is no recurrent component,
invariant or swapped, and no gcd or class shift to report. S84's cross-check (no admission and no direct backward
return at q <= 16) PASS at all six. PR191-C1's prediction HELD. Beyond the prediction, and immediate from acyclicity: a
swap path of length h >= 1 followed by its swapped copy would be a closed walk, so these graphs admit no dyadic q at
all. With G190, no prefix entered by an odd doubling to any dyadic q returns to zero at an even position 4 to 14.
This covers six fixed graphs only, as the preregistration says; nothing about r >= 16.
"""
import resource
import sys
import time
from itertools import product
from math import gcd

sys.setrecursionlimit(10000)


def rot(w, d, q):
    d %= q
    return ((w >> d) | (w << (q - d))) & ((1 << q) - 1)


def U(n, w):
    """G189's backward functions on a finite word (list of bits), at t = 0."""
    L = [w, w]
    for i in range(2, n + 1):
        a, b = L[i - 2], L[i - 1]
        L.append([a[t + 1] ^ (b[t] | a[t]) for t in range(min(len(a) - 1, len(b)))])
    return L[n][0]


def Ucyc(n, w, q):
    L = [w, w]
    for i in range(2, n + 1):
        L.append(rot(L[i - 2], 1, q) ^ (L[i - 1] | L[i - 2]))
    return L[n]


def graph(m):
    F, A = {}, {}
    for X in product((0, 1), repeat=m):
        F[X] = U(2 * m - 1, list(X) + [0])
        A[X] = U(2 * m, list(X) + [0])
        assert U(2 * m, list(X) + [1]) == 1 ^ A[X]
    V = [(X, Y) for X in F for Y in F if F[X] == 1 and F[Y] == 1]
    idx = {v: i for i, v in enumerate(V)}
    adj = [[] for _ in V]
    for i, (X, Y) in enumerate(V):
        for b, b2 in product((0, 1), repeat=2):
            if b ^ b2 == 1 ^ A[X] ^ A[Y]:
                nv = (X[1:] + (b,), Y[1:] + (b2,))
                if nv in idx:
                    adj[i].append(idx[nv])
    sig = [idx[(Y, X)] for X, Y in V]
    return V, adj, sig


def sccs(n, adj):
    """Kosaraju, iterative."""
    order, seen = [], [False] * n
    for s in range(n):
        if seen[s]:
            continue
        stack = [(s, 0)]
        seen[s] = True
        while stack:
            v, i = stack.pop()
            if i < len(adj[v]):
                stack.append((v, i + 1))
                w = adj[v][i]
                if not seen[w]:
                    seen[w] = True
                    stack.append((w, 0))
            else:
                order.append(v)
    radj = [[] for _ in range(n)]
    for v in range(n):
        for w in adj[v]:
            radj[w].append(v)
    comp = [-1] * n
    comps = []
    for s in reversed(order):
        if comp[s] >= 0:
            continue
        cid, todo, members = len(comps), [s], []
        comp[s] = cid
        while todo:
            v = todo.pop()
            members.append(v)
            for w in radj[v]:
                if comp[w] < 0:
                    comp[w] = cid
                    todo.append(w)
        comps.append(members)
    return comps, comp


def classify(n, adj, sig):
    comps, comp = sccs(n, adj)
    rows = []
    for cid, C in enumerate(comps):
        Cs = set(C)
        internal = [(u, w) for u in C for w in adj[u] if w in Cs]
        recurrent = bool(internal)
        image = {comp[sig[v]] for v in C}
        assert len(image) == 1                           # sigma maps components onto components
        partner = image.pop()
        row = {'id': cid, 'size': len(C), 'recurrent': recurrent, 'invariant': partner == cid, 'partner': partner,
               'branching': any(sum(1 for w in adj[u] if w in Cs) >= 2 for u in C)}
        if recurrent:
            # gcd by a traversal potential (depth-first tree) and every internal edge difference
            root = C[0]
            pot, todo = {root: 0}, [root]
            while todo:
                u = todo.pop()
                for w in adj[u]:
                    if w in Cs and w not in pot:
                        pot[w] = pot[u] + 1
                        todo.append(w)
            g = 0
            for u, w in internal:
                g = gcd(g, abs(pot[u] + 1 - pot[w]))
            # classes separately, by breadth-first distance mod g; every internal edge must advance the class by one
            dist, frontier = {root: 0}, [root]
            while frontier:
                nxt = []
                for u in frontier:
                    for w in adj[u]:
                        if w in Cs and w not in dist:
                            dist[w] = dist[u] + 1
                            nxt.append(w)
                frontier = nxt
            cls = {v: dist[v] % g for v in C}
            row['classes_ok'] = all((cls[u] + 1) % g == cls[w] for u, w in internal)
            row['g'] = g
            if row['invariant']:
                ds = {(cls[sig[v]] - cls[v]) % g for v in C}
                row['d_values'] = sorted(ds)
                d = ds.pop() if len(ds) == 1 else None
                row['d'] = d
                row['persistent'] = d == 0 and g & (g - 1) == 0
        rows.append(row)
    return comps, rows


def admitted(n, adj, sig, J):
    """Dyadic q = 2^j, j = 1 .. J, with a path of length q/2 from some v to sig(v) (boolean matrix powers)."""
    M = [0] * n
    for v in range(n):
        for w in adj[v]:
            M[v] |= 1 << w

    def mul(A, B):
        out = []
        for row in A:
            r, k = 0, 0
            while row:
                if row & 1:
                    r |= B[k]
                row >>= 1
                k += 1
            out.append(r)
        return out

    P, res = M[:], []
    for j in range(1, J + 1):
        if any((P[v] >> sig[v]) & 1 for v in range(n)):
            res.append(j)
        P = mul(P, P)
    return res


def lhs(m, q):
    full, h = (1 << q) - 1, q // 2
    for w in range(1 << q):
        if Ucyc(2 * m - 1, w, q) == full:
            c = Ucyc(2 * m, w, q)
            if rot(c, h, q) == c ^ full:
                return True
    return False


def abstract_controls():
    cyc = lambda n: [[(v + 1) % n] for v in range(n)]
    out = {}
    for name, adj, sig in (('C4 half-turn', cyc(4), [2, 3, 0, 1]), ('K22 in-part swap', [[2, 3], [2, 3], [0, 1], [0, 1]],
                                                                                         [1, 0, 3, 2]),
                           ('C6 half-turn', cyc(6), [3, 4, 5, 0, 1, 2]), ('two exchanged loops', [[0], [1]], [1, 0])):
        comps, rows = classify(len(adj), adj, sig)
        pers = any(r.get('persistent') for r in rows)
        out[name] = (pers, admitted(len(adj), adj, sig, 10), rows)
    return out


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (125, 125))
    t0 = time.process_time()
    ctl = abstract_controls()
    expect = {'C4 half-turn': (False, [2]), 'K22 in-part swap': (True, list(range(2, 11))),
              'C6 half-turn': (False, []), 'two exchanged loops': (False, [])}
    for name, (pers, adm, rows) in ctl.items():
        ok = (pers, adm) == expect[name] and all(r.get('classes_ok', True) for r in rows)
        extra = ''
        if name == 'two exchanged loops':
            ok &= all(not r['invariant'] and r['recurrent'] for r in rows) and len(rows) == 2
            extra = '; components recurrent but swapped with each other (not pooled)'
        print('control %-20s persistent %s, admitted j %s: %s%s' % (name, pers, adm, 'PASS' if ok else 'FAIL', extra))
    refuted = False
    for m in range(1, 7):
        r = 2 * m + 2
        V, adj, sig = graph(m)
        n, ne = len(V), sum(len(a) for a in adj)
        comps, rows = classify(n, adj, sig)
        rec_inv = [x for x in rows if x['recurrent'] and x['invariant']]
        rec_non = [x for x in rows if x['recurrent'] and not x['invariant']]
        trivial = [x for x in rows if not x['recurrent']]
        s84 = admitted(n, adj, sig, 4) == [] and not any(lhs(m, q) for q in (2, 4, 8, 16))
        print('r = %d (m = %d): %d vertices, %d edges; components %d (%d without a cycle, %d recurrent swapped in '
              'pairs, %d recurrent invariant); S84 cross-check (no admission or direct return at q <= 16) %s'
              % (r, m, n, ne, len(rows), len(trivial), len(rec_non), len(rec_inv), 'PASS' if s84 else 'FAIL'),
              flush=True)
        for x in rec_inv:
            print('   invariant recurrent component: size %d, g %d, d %s, branching %s, classes consistent %s, '
                  'persistent %s' % (x['size'], x['g'], x['d_values'], x['branching'], x['classes_ok'],
                                     x['persistent']))
            if x['persistent']:
                refuted = True
        for x in rec_non:
            print('   swapped recurrent component: size %d (partner %d), g %d, branching %s, classes consistent %s'
                  % (x['size'], x['partner'], x['g'], x['branching'], x['classes_ok']))
        if time.process_time() - t0 > 120 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 512 * 1024 * 1024:
            print('ENVIRONMENT LIMIT after r = %d: partial, not a result' % r)
            return 2
    print('PR191-C1 prediction (no persistent component at r = 4 .. 14):', 'REFUTED' if refuted else 'HELD')
    print('control gcds and shifts:', {name: [(r['size'], r.get('g'), r.get('d_values')) for r in rows if r['recurrent']]
                                       for name, (p, a, rows) in ctl.items()})
    if refuted:
        print('a positive case needs the explicit swap path and direct reconstruction at one dyadic q > n (not done here)')
    rus = resource.getrusage(resource.RUSAGE_SELF)
    print('resources: CPU %.2f s, peak RSS %.1f MiB' % (time.process_time() - t0, rus.ru_maxrss / 1048576))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
