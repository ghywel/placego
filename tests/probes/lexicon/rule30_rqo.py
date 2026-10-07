#!/usr/bin/env python3
"""rule30_rqo.py: RQO, temporal difference orders alongside reached reset distances, of RULE30-GPT.md §G177 (GPT's
design; requested in GC219; claimed by Local in CLOUD-LOCAL.md at b8f8d10 before this script was written or run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_rqo.py
COST:       seconds expected; caps 60 CPU s and 128 MiB RSS (GPT's).

Domain: RQ3's exact root-reached aligned graph at q = 1, 2, 4, 8 (rule30_rq3.reached, reused, not rebuilt
differently). Each state (A, B) maps to (Phi, p, nu(A), nu(B), nu(A XOR B)), where Phi and p are RQ3's three reset
distances and least pair period and nu(w) = min{k >= 0 : Delta^k w = 0} with the cyclic difference
(Delta w)(t) = w(t) XOR w(t + 1), so nu(0) = 0. The quotient keeps the largest reward 2 delta - 5 per feature edge with
a reached representative, and the positive-cycle test is RQ3's.

PREDICTIONS, GPT's, published in RULE30-GPT.md §G177 before this run:
  RO-P1 (blind): q = 8 still has a positive refined feature cycle.
  RO-C1 (control): q = 1, 2, 4 pass (their feasible feature potentials lift to the refinement).
  RO-C2 (control): every order agrees with q - v, v the multiplicity of (X + 1) found by independent polynomial
        division over GF(2), for all 2^q words at q = 8 and below, with nu(0) = 0.
  RO-CF (counterfactual): the G176 endpoints (183, 176) and (133, 208) now have different features.
  Unexpected checks: at q = 8, nu(0) = 0 and nu(255) = 1; nu is invariant under temporal rotation.
  Reached counts must equal RQ3's (3/2, 9/9, 31/32, 409/411) as a domain guard.

OUTCOME, 2026-10-07 (M5, one process; CPU 0.39 s, peak RSS 10.7 MiB). RO-C2 PASS (orders equal q minus the
multiplicity of X + 1 for every word to q = 8, and are rotation invariant); unexpected checks PASS (nu(0) = 0,
nu(255) = 1). Domain guard PASS at every q. RO-C1 PASS: no positive refined cycle at q = 1, 2, 4 (F max 0, 0, 1, every
lifted edge holds). RO-CF PASS: the G176 endpoints now differ, (1, 5, 1, 8, 7, 8, 8) against (1, 5, 1, 8, 8, 8, 2).
RO-P1 HELD: q = 8 has a positive refined feature cycle of seven edges, total reward 7, over 264 refined vertices and
398 quotient edges. Its representatives are reached edges at depths 270 -> 275 (five consecutive edges, rewards -1,
-1, -1, 3, 3) and 318 -> 320 (rewards 1, 3); each representative edge and its whole root path pass the literal
checks. The cycle closes only in feature space: the last representative ends at (137, 206), not at the first source
(143, 26), so it is a compression failure, not a real cycle.
"""
import os
import resource
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rule30_rq3 as r3                                   # noqa: E402


def delta(w, q):
    return (w ^ r3.rot(w, 1, q)) & ((1 << q) - 1)       # (Delta w)(t) = w(t) XOR w(t + 1)


def nu(w, q):
    k = 0
    while w:
        w = delta(w, q)
        k += 1
    return k


def mult_x_plus_1(w):
    """Multiplicity of (X + 1) in w(X) = sum w_t X^t over GF(2), by repeated synthetic division."""
    if w == 0:
        return None
    m = 0
    while True:
        if bin(w).count('1') % 2:                         # w(1) != 0: not divisible
            return m
        # divide by (X + 1): coefficients from the top, c_i = w_(i+1) XOR c_(i+1)
        deg = w.bit_length() - 1
        quo, carry = 0, 0
        for i in range(deg, 0, -1):
            carry ^= (w >> i) & 1
            quo |= carry << (i - 1)
        w = quo
        m += 1


def feat(s, q):
    a, b = s
    return r3.feat(s, q) + (nu(a, q), nu(b, q), nu(a ^ b, q))


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (65, 65))
    t0 = time.process_time()
    c2 = True
    for q in (1, 2, 4, 8):
        for w in range(1 << q):
            m = mult_x_plus_1(w)
            c2 &= (nu(w, q) == 0) if w == 0 else (nu(w, q) == q - m)
            c2 &= all(nu(r3.rot(w, d, q), q) == nu(w, q) for d in range(q))
    unexpected = nu(0, 8) == 0 and nu(255, 8) == 1
    print('RO-C2', 'PASS' if c2 else 'FAIL', '(orders = q - multiplicity of X + 1, all words to q = 8; rotation invariant)')
    print('unexpected checks', 'PASS' if unexpected else 'FAIL', '(nu(0) = 0, nu(255) = 1 at q = 8)')
    expected_counts = {1: (3, 2), 2: (9, 9), 4: (31, 32), 8: (409, 411)}
    verdict = {}
    for q in (1, 2, 4, 8):
        root, depth, parent, edges, exits = r3.reached(q)
        guard = (len(depth), len(edges)) == expected_counts[q]
        F = {s: feat(s, q) for s in depth}
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
        line = 'q = %d: reached %d/%d (RQ3 guard %s); refined feature vertices %d, quotient edges %d' % (
            q, len(depth), len(edges), 'PASS' if guard else 'FAIL', len(verts), len(quot))
        if not changed:
            verdict[q] = 'none'
            lift = all(h[F[s]] >= 2 * d - 5 + h[F[t]] for s, t, d in edges)
            line += '; no positive feature cycle, F max %d, every lifted edge %s' % (max(h.values()),
                                                                                   'PASS' if lift else 'FAIL')
            print(line, flush=True)
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
            print(line + '; POSITIVE FEATURE CYCLE of %d edges' % (len(cyc) - 1), flush=True)
            tot = 0
            for i in range(len(cyc) - 1):
                w, (s, t, d) = quot[(cyc[i], cyc[i + 1])]
                tot += w
                path = r3.root_path(parent, s)
                ok = all(c in r3.children_brute(a_, b_, q) for (a_, b_), tgt, dd, c in path)
                c_ = r3.rot(t[1], -d, q)
                ok &= c_ in r3.children_brute(s[0], s[1], q) and (r3.rot(s[1], d, q), r3.rot(c_, d, q)) == t
                print('   %r -> %r reward %d; rep %r -> %r delay %d, depths %d -> %d; root path and edge literal %s'
                      % (cyc[i], cyc[i + 1], w, s, t, d, depth[s], depth[t], 'PASS' if ok else 'FAIL'))
            print('   total reward %d' % tot)
        if q == 8:
            fs, ft = F.get((183, 176)), F.get((133, 208))
            print('RO-CF', 'PASS (G176 endpoints now differ: %r vs %r)' % (fs, ft) if fs is not None and ft is not None
                  and fs != ft else 'FAIL (%r, %r)' % (fs, ft))
        if time.process_time() - t0 > 60 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 128 * 1024 * 1024:
            print('CAP REACHED after q = %d: partial, not a result' % q)
            return 2
    print('RO-C1', 'PASS' if all(verdict[q] == 'none' for q in (1, 2, 4)) else 'FAIL')
    print('RO-P1', 'HELD' if verdict[8] == 'cycle' else 'REFUTED')
    rus = resource.getrusage(resource.RUSAGE_SELF)
    print('resources: CPU %.2f s, peak RSS %.1f MiB' % (time.process_time() - t0, rus.ru_maxrss / 1048576))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
