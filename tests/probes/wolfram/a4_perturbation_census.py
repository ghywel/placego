#!/usr/bin/env python3
"""L1434 (Local, 2026-11-03): the A4 finite-perturbation census (GC2535's pull).
Run: python3 tests/probes/wolfram/a4_perturbation_census.py DATA.json W_PERT [TMAX] [SAVE.npz]

DATA.json is a4_closure_export.py's closure (kept outside git): ring orbit, alignment (r, s), window W, (P, S), the closure
states and their potential. Every nonzero pattern u < 2 ^ W_PERT is XORed onto the background on cells [0, W_PERT): a finite
perturbation. All patterns evolve together under Rule 30 on a row wide enough that truncation never reaches the left front
(x from -2 TMAX - 10 to TMAX + W_PERT + 10; the right-front check runs while the right truncation cannot reach it). The left front F(t) is the leftmost difference; at each checkpoint t the anchored
state is (t mod q, (t - A) mod N, the W cells right of A) with A = F - 1, exactly as a4_closure_export.start_state.
A state in the closure is certified: the closure holds every successor under both values of the cell beyond the window
(the kernel-checked step_sound / closure_ok of A4), so from then on P (A(t) - A(t_c)) + (P - S)(t - t_c) = psi(now) - psi(t_c),
and the front's speed is exactly (P - S) / P. States outside the closure at every checkpoint get their own closure (cap) and
a potential test. Also checked: the rightmost difference is R0 + t (left permutivity). Prints counts only, no paths.
"""
import json
import sys
from collections import deque

import numpy as np

data = json.load(open(sys.argv[1]))
WP = int(sys.argv[2]); TMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 1200
SAVE = sys.argv[4] if len(sys.argv) > 4 else None  # optional: save F(t) for every pattern (outside git)
orb = [tuple(o) for o in data['orb']]; q = len(orb); N = data['N']; r0, s0 = data['r'], data['s']
W, P, S = data['W'], data['P'], data['S']
CL = {(st[0], st[1], tuple(st[2])): data['lo'][i] for i, st in enumerate(data['states'])}
assert data['lo'] == data['hi']
rule = lambda a, b, c: a ^ (b | c)
E = lambda x, t: orb[(t + s0) % q][((t - x) + r0) % N]
CHECK = [300, 600, 900, 1200]
assert max(CHECK) <= TMAX


def transitions(state):
    """a4_closure_export.transitions, verbatim in content."""
    tq, dq, strip = state; L = len(strip)
    Eb = lambda i, dt=0: orb[(tq + dt + s0) % q][((dq + dt - i) + r0) % N]
    outs = []
    for b in (0, 1):
        cell = lambda i: Eb(i) if i <= 0 else (strip[i - 1] if i <= L else b)
        new = {i: rule(cell(i - 1), cell(i), cell(i + 1)) for i in range(0, L + 1)}
        if new[0] != Eb(0, 1):
            ns = tuple(new[i] for i in range(0, L)); ndq = (dq + 2) % N; mv = -1
        else:
            ns = tuple(new[i] for i in range(1, L + 1)); ndq = (dq + 1) % N; mv = 0
        Enew = lambda i: orb[(tq + 1 + s0) % q][((ndq - i) + r0) % N]
        if not any(ns[i] != Enew(i + 1) for i in range(len(ns))):
            return None
        outs.append((((tq + 1) % q, ndq, ns), mv))
        if mv == -1:
            break
    return outs


def own_closure(start, cap=60000):
    seen = {start: 0}; order = [start]; edges = {}; dq_ = deque([start])
    while dq_:
        st = dq_.popleft(); outs = transitions(st)
        if outs is None:
            return None, 'a successor loses its difference'
        edges[st] = outs
        for nst, _ in outs:
            if nst not in seen:
                seen[nst] = len(order); order.append(nst); dq_.append(nst)
                if len(order) > cap:
                    return None, 'cap'
    return (order, edges), None


def potential(order, edges):
    """Bellman-Ford for one potential psi with psi(s') - psi(s) = w on every edge; None if no such potential."""
    idx = {st: i for i, st in enumerate(order)}; INF = 10 ** 18
    d = [INF] * len(order); d[0] = 0
    for _ in range(len(order) + 1):
        ch = False
        for st, outs in edges.items():
            for nst, mv in outs:
                w = P * mv + (P - S)
                if d[idx[st]] + w < d[idx[nst]]:
                    d[idx[nst]] = d[idx[st]] + w; ch = True
        if not ch:
            break
    else:
        return None
    ok = all(d[idx[n]] - d[idx[st]] == P * mv + (P - S) for st, outs in edges.items() for n, mv in outs)
    return d if ok else None


lo = -2 * TMAX - 10; hi = TMAX + WP + 10; L = hi - lo; c = -lo
bg0 = np.array([E(x, 0) for x in range(lo, hi)], dtype=np.uint8)
pats = np.arange(1, 1 << WP, dtype=np.int64); NP = len(pats)
X = np.repeat(bg0[None, :], NP, axis=0)
for i in range(WP):
    X[:, c + i] ^= ((pats >> i) & 1).astype(np.uint8)
B = bg0.copy()
R0 = np.array([int(np.flatnonzero((X[k] ^ B))[-1]) for k in range(NP)])
F_at = {}; state_at = {}
F_track = np.zeros((TMAX + 1, NP), dtype=np.int32)


def front(Xc, Bc):
    D = Xc ^ Bc[None, :]
    assert D.any(axis=1).all(), 'a perturbation healed'
    return D.argmax(axis=1), L - 1 - D[:, ::-1].argmax(axis=1)


right_ok = True; right_t = -1
for t in range(TMAX + 1):
    if t > 0:
        Xn = np.zeros_like(X); Xn[:, 1:-1] = X[:, :-2] ^ (X[:, 1:-1] | X[:, 2:]); X = Xn
        Bn = np.zeros_like(B); Bn[1:-1] = B[:-2] ^ (B[1:-1] | B[2:]); B = Bn
    Fi, Ri = front(X, B)
    F_track[t] = Fi - c
    if R0.max() + t < L - t - 2:
        right_ok &= bool((Ri == R0 + t).all()); right_t = t
    if t in CHECK:
        assert Fi.min() - c > lo + t + 1 and (Fi - c + W + 1).max() < hi - t - 1, 'truncation could reach the window'
        assert all(int(B[c + x]) == E(x, t) for x in range(lo + t + 2, hi - t - 2)), 'background row drifted'
        A = Fi - 1
        sts = [(t % q, int((t - (A[k] - c)) % N), tuple(int(v) for v in X[k, A[k] + 1: A[k] + 1 + W])) for k in range(NP)]
        state_at[t] = sts

first_in = np.full(NP, -1)
for t in CHECK:
    for k in range(NP):
        if first_in[k] < 0 and state_at[t][k] in CL:
            first_in[k] = t
print('%s (P,S)=(%d,%d) W=%d alignment (r,s)=(%d,%d); perturbations: all %d nonzero patterns on [0,%d); TMAX=%d' % (
    data['name'], P, S, W, r0, s0, NP, WP, TMAX))
print('rightmost difference equals R0 + t for every pattern and every t <= %d (the exact range): %s' % (right_t, right_ok))
for t in CHECK:
    print('  state in the %d-state closure at t=%d: %d of %d (first entry at t: %d)' % (
        len(CL), t, sum(1 for k in range(NP) if state_at[t][k] in CL), NP, int((first_in == t).sum())))
outside = [k for k in range(NP) if first_in[k] < 0]
print('never in the closure at the checkpoints: %d' % len(outside))
slope = (F_track[TMAX] - F_track[300]) / (TMAX - 300)
print('measured left-front slope (F(%d) - F(300))/%d: min %.4f, max %.4f; theorem -(P-S)/P = %.4f' % (
    TMAX, TMAX - 300, slope.min(), slope.max(), -(P - S) / P))
# exact law check for the certified ones: P(F(t) - F(tc)) + (P-S)(t - tc) stays in psi's range shifted by W
pmin, pmax = min(CL.values()), max(CL.values())
viol = 0
for k in range(NP):
    if first_in[k] < 0:
        continue
    tc = int(first_in[k]); psi_c = CL[state_at[tc][k]]; Ac = F_track[tc, k] - 1
    t = np.arange(tc, TMAX + 1); Fk = F_track[tc:, k]
    # anchor law: P(A - Ac) + (P-S)(t - tc) = psi(now) - psi_c in [pmin - psi_c, pmax - psi_c]; F in (A, A + W]
    lowb = P * (Fk - W - Ac) + (P - S) * (t - tc); upb = P * (Fk - 1 - Ac) + (P - S) * (t - tc)
    viol += int(((upb < pmin - psi_c) | (lowb > pmax - psi_c)).sum())
print('certified perturbations whose simulated front leaves the law band after entry: %d' % viol)
from collections import Counter
for (a, b) in [(TMAX // 4, TMAX // 2), (TMAX // 2, TMAX)]:
    sl = (F_track[b].astype(np.int64) - F_track[a]) / (b - a)
    near = int((np.abs(sl + (P - S) / P) < 0.01).sum())
    hist = Counter(np.round(sl, 2).tolist())
    print('slopes over [%d, %d]: within 0.01 of the theorem %d of %d; clusters (slope, count): %s' % (
        a, b, near, NP, sorted(hist.items(), key=lambda kv: -kv[1])[:12]))
done = {}
for k in outside[:40]:
    st = state_at[1200][k]
    if st in done:
        continue
    res, why = own_closure(st)
    if res is None:
        done[st] = 'no closure (%s)' % why
    else:
        pot = potential(*res)
        done[st] = 'own closure %d states; potential at (P,S): %s' % (len(res[0]), pot is not None)
    print('  outside pattern 0x%x: %s; slope %.4f' % (int(pats[k]), done[st], slope[k]))
if SAVE:
    np.savez_compressed(SAVE, F=F_track, pats=pats)
    print('saved F(t) for every pattern to %s (kept outside git)' % SAVE.rsplit('/', 1)[-1])
print('A4_PERTURBATION_CENSUS_DONE')
