#!/usr/bin/env python3
"""rule30_rc2.py: RC2, actual two-edge context before feature compression, of RULE30-GPT.md §G180 (GPT's design;
requested in GC222; claimed by Local in CLOUD-LOCAL.md at 3025cd1 before this script was written or run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_rc2.py
COST:       seconds expected; caps 60 CPU s and 128 MiB RSS (GPT's).

Domain: RQ3's root-reached aligned graph at q = 1, 2, 4, 8 (rule30_rq3.reached), RQO's labels phi (rule30_rqo.feat).
Each actual edge e = (s, t) becomes an edge-state labelled L(e) = (phi(s), phi(t)), with reward w(e) = 2 delay - 5. An
arc e -> f exists only for an actual f = (t, u) with the same middle state t, charged by the second edge's reward
w(f). Edge-states are then compressed by L (largest reward per label arc, with a representative triple). A
nonnegative K on labels with K(x) >= w + K(y) on every label arc exists exactly when there is no positive label cycle;
if it exists, h(s) = max(0, max over outgoing e of w(e) + K(L(e))) is lifted and checked on every original edge.

PREDICTIONS, GPT's, published in RULE30-GPT.md §G180 before this run:
  RC-P1 (blind): the context quotient is feasible at q = 8.
  RC-C1 (control): q = 1, 2, 4 pass.
  RC-C2 (control): through q = 4, an independent absolute-time construction (rule30_rq3.absolute_construction)
        reproduces the consecutive-edge arcs; q = 8 witness triples are checked literally; reached counts match RQ3.
  RC-CF (counterfactual): G178's two particular joins are rejected by middle-state identity, while the line graph
        formed after feature compression still admits its seven-edge, elapsed-21 cycle.
  Synthetic controls: a one-positive-edge graph (K = 0, lift gives the source its reward) and a two-edge path with
        distinct rewards (the arc carries the second edge's reward, not the sum).
Required: edge-state and arc counts, compressed vertex and arc counts, then K and h maxima with h <= K + max(0, 2q - 5)
and every lifted inequality verified, or a positive label cycle with actual triples and root paths.

OUTCOME, 2026-10-07 (M5, one process; CPU 0.01 s, peak RSS 11.1 MiB). Synthetic controls PASS (one positive edge:
K = 0, lift gives the source 5; two-edge path: the arc carries -1, the second reward). Domain guard PASS. RC-C2 PASS:
the absolute-time construction reproduces every consecutive-edge arc through q = 4. RC-C1 PASS: q = 1, 2, 4 feasible
(K max 0, 0, 1). RC-P1 HELD: q = 8 is feasible, K max 14 and h max 14 (within K max + 11), every lifted original
edge inequality holds. RC-CF PASS: both G178 joins fail the middle-state identity, while the line graph formed
after compression still carries the reward-7 cycle. Counts: edge-states and actual arcs 2/1, 9/9, 32/33, 411/413;
context labels and label arcs 2/1, 9/9, 32/33, 398/412. Caveat, beyond the predictions: at q = 8 the labels barely
compress (398 labels for 411 edge-states), and the reached domain is close to a single chain, so this pass shows
that two-edge context removes the aliasing here, not that a small context family certifies large periods.
"""
import os
import resource
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rule30_rq3 as r3                                   # noqa: E402
import rule30_rqo as ro                                   # noqa: E402


def context_test(edges, label, reward):
    """Generic: edges = list of (s, t, payload); returns (feasible, K, quot, cycle, n_arcs)."""
    by_src = {}
    for i, (s, t, _) in enumerate(edges):
        by_src.setdefault(s, []).append(i)
    L = [(label(s), label(t)) for s, t, _ in edges]
    quot = {}
    n_arcs = 0
    for i, (s, t, _) in enumerate(edges):
        for j in by_src.get(t, []):
            n_arcs += 1
            key, w = (L[i], L[j]), reward(edges[j])
            if key not in quot or w > quot[key][0]:
                quot[key] = (w, (i, j))
    verts = sorted(set(L))
    K = {x: 0 for x in verts}
    pred, changed, rounds, last = {}, True, 0, None
    while changed and rounds <= len(verts) + 1:
        changed, rounds = False, rounds + 1
        for (x, y), (w, rep) in quot.items():
            if w + K[y] > K[x]:
                K[x], pred[x], changed, last = w + K[y], y, True, x
    if not changed:
        return True, K, quot, None, n_arcs, L
    x = last
    for _ in range(len(verts)):
        x = pred[x]
    cyc, y = [x], pred[x]
    while y != x:
        cyc.append(y)
        y = pred[y]
    cyc.append(x)
    return False, K, quot, cyc, n_arcs, L


def lift(edges, L, K, reward, vertices):
    h = {v: 0 for v in vertices}
    for i, (s, t, _) in enumerate(edges):
        h[s] = max(h[s], reward(edges[i]) + K[L[i]])
    ok = all(h[s] >= reward(edges[i]) + h[t] for i, (s, t, _) in enumerate(edges))
    return ok, h


def synthetic_controls():
    # one positive edge: line graph has one vertex, no arcs
    E1 = [('s', 't', 5)]
    f1, K1, q1, c1, n1, L1 = context_test(E1, lambda v: v, lambda e: e[2])
    ok1, h1 = lift(E1, L1, K1, lambda e: e[2], ['s', 't'])
    one = f1 and n1 == 0 and all(v == 0 for v in K1.values()) and ok1 and h1['s'] == 5 and h1['t'] == 0
    # two-edge path with distinct rewards: the arc carries the second edge's reward
    E2 = [('s', 't', 3), ('t', 'u', -1)]
    f2, K2, q2, c2, n2, L2 = context_test(E2, lambda v: v, lambda e: e[2])
    arcw = list(q2.values())[0][0] if q2 else None
    ok2, h2 = lift(E2, L2, K2, lambda e: e[2], ['s', 't', 'u'])
    two = f2 and n2 == 1 and arcw == -1 and ok2 and h2 == {'s': 3, 't': 0, 'u': 0}
    return one, two


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (65, 65))
    t0 = time.process_time()
    one, two = synthetic_controls()
    print('synthetic controls: one positive edge %s; two-edge path charges the second reward %s'
          % ('PASS' if one else 'FAIL', 'PASS' if two else 'FAIL'))
    expected_counts = {1: (3, 2), 2: (9, 9), 4: (31, 32), 8: (409, 411)}
    verdict = {}
    for q in (1, 2, 4, 8):
        root, depth, parent, edges, exits = r3.reached(q)
        guard = (len(depth), len(edges)) == expected_counts[q]
        lab = {s: ro.feat(s, q) for s in depth}
        reward = (lambda e: 2 * e[2] - 5)
        feas, K, quot, cyc, n_arcs, L = context_test(edges, lambda v: lab[v], reward)
        line = ('q = %d: reached %d/%d (RQ3 guard %s); edge-states %d, actual arcs %d; context labels %d, label arcs %d'
                % (q, len(depth), len(edges), 'PASS' if guard else 'FAIL', len(edges), n_arcs, len(set(L)), len(quot)))
        if q <= 4:
            st, ed = r3.absolute_construction(q)
            arcs_abs = {(e1, e2) for e1 in ed for e2 in ed if e1[1] == e2[0]}
            arcs_rel = {(e1, e2) for e1 in edges for e2 in edges if e1[1] == e2[0]}
            line += '; RC-C2 arcs reproduced %s' % ('PASS' if arcs_abs == arcs_rel else 'FAIL')
        if feas:
            verdict[q] = 'feasible'
            ok, h = lift(edges, L, K, reward, list(depth))
            hmax, kmax = max(h.values()), max(K.values())
            line += '; FEASIBLE, K max %d, h max %d (<= K max + %d: %s), every lifted edge %s' % (
                kmax, hmax, max(0, 2 * q - 5), hmax <= kmax + max(0, 2 * q - 5), 'PASS' if ok else 'FAIL')
            print(line, flush=True)
        else:
            verdict[q] = 'cycle'
            print(line + '; POSITIVE CONTEXT CYCLE of %d label arcs' % (len(cyc) - 1), flush=True)
            tot = 0
            for k in range(len(cyc) - 1):
                w, (i, j) = quot[(cyc[k], cyc[k + 1])]
                tot += w
                (s, t, d), (t2, u, d2) = edges[i], edges[j]
                c_ = r3.rot(u[1], -d2, q)
                ok = t2 == t and c_ in r3.children_brute(t[0], t[1], q)
                path = r3.root_path(parent, s)
                ok &= all(cc in r3.children_brute(a_, b_, q) for (a_, b_), tgt, dd, cc in path)
                print('   triple %r -> %r -> %r (delays %d, %d), arc reward %d, depths %d/%d/%d; literal %s'
                      % (s, t, u, d, d2, w, depth[s], depth[t], depth[u], 'PASS' if ok else 'FAIL'))
            print('   total reward %d' % tot)
        if q == 8:
            ed = {(s, t): d for s, t, d in edges}
            joins = [((140, 168), (138, 140), (182, 84), (138, 152)), ((138, 152), (137, 206), (143, 26), (134, 186))]
            rej = all(t1 != s2 for s1, t1, s2, t2 in joins) and all((s1, t1) in ed and (s2, t2) in ed
                                                                     for s1, t1, s2, t2 in joins)
            seg = [((143, 26), (134, 186)), ((134, 186), (174, 62)), ((174, 62), (143, 200)), ((143, 200), (140, 168)),
                   ((140, 168), (138, 140)), ((182, 84), (138, 152)), ((138, 152), (137, 206))]
            fl = [(lab[s], lab[t]) for s, t in seg]
            post = all(fl[k][1] == fl[(k + 1) % 7][0] for k in range(7))
            post &= sum(2 * ed[seg[(k + 1) % 7]] - 5 for k in range(7)) == 7
            print('RC-CF', 'PASS (both G178 joins fail middle-state identity; after-compression line graph keeps the '
                  'reward-7 cycle)' if rej and post else 'FAIL')
        if time.process_time() - t0 > 60 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 128 * 1024 * 1024:
            print('CAP REACHED after q = %d: partial, not a result' % q)
            return 2
    print('RC-C1', 'PASS' if all(verdict[q] == 'feasible' for q in (1, 2, 4)) else 'FAIL')
    print('RC-P1', 'HELD' if verdict[8] == 'feasible' else 'REFUTED')
    rus = resource.getrusage(resource.RUSAGE_SELF)
    print('resources: CPU %.2f s, peak RSS %.1f MiB' % (time.process_time() - t0, rus.ru_maxrss / 1048576))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
