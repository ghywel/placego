#!/usr/bin/env python3
"""collatz_demand_unimodal_proof.py: UP, the checks behind Local's proposed hand proof that EVERY actual Collatz
demand law is unimodal, for every horizon T (Q9; DU found it for T <= 1024; L276 carries the proof for reading).
Claimed in CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu (pure Python 3, standard library)
COMMAND:    python3 tests/probes/prizes/collatz_demand_unimodal_proof.py [TMAX=1024]
COST:       to be recorded (expected a few minutes: DU's recursion plus small exhaustive and random lemma checks).

THE PROOF (hand part). Use G219's operators on scaled atom sequences: the critical step C(p) = (p_0, p_0 + p_1,
p_1 + p_2, ..., p_last) and the flat step B(q) = (2 q_0 + q_1, q_1 + q_2, q_2 + q_3, ...), applied backward in time.
(1) C preserves unimodality: it is convolution with (1, 1), which is log-concave, hence strongly unimodal (Keilson and
    Gerber 1971; PRIOR-ART.md).
(2) Flat steps are isolated: ell_(r+2) - ell_r >= 1 because 2 log_3 2 > 1. So every flat step at r < T - 1 acts on a
    law that a critical step produced, and the law at r is B(C(p)) with p the law at r + 2. A flat step at r = T - 1
    acts on the terminal atom and gives a single atom.
(3) Lemma: if p >= 0 is unimodal, so is B(C(p)). Write P = B(C(p)): P_0 = 3 p_0 + p_1 and, for j >= 1,
    P_j = p_(j-1) + 2 p_j + p_(j+1), the (1, 2, 1) convolution read one place on. That tail is unimodal (log-concave
    kernel), so P fails to be unimodal only if P_0 > P_1 and the tail later rises above P_1.
    Case A, p nonincreasing: for j >= 1, P_(j+1) - P_j = (p_j - p_(j-1)) + 2 (p_(j+1) - p_j) + (p_(j+2) - p_(j+1)),
    a sum of differences of p, all <= 0, so the tail never rises from P_1 on. (Corrected 2026-10-08 05:48: this line
    first said j >= 2, which left P_2 - P_1 unstated; the same expansion covers j = 1.)
    Case B, p not nonincreasing: unimodality gives p_0 <= p_1. If p_1 <= p_2 then 2 p_0 <= p_1 + p_2, that is
    P_0 <= P_1, and prepending a value no larger than the first keeps a unimodal sequence unimodal. Otherwise the mode
    is 1, p_1 > p_2 >= p_3 >= ..., the tail is nonincreasing from P_2 on, and a failure needs P_0 > P_1 and P_2 > P_1:
    2 p_0 > p_1 + p_2 and p_2 + p_3 > p_0 + p_1. The first gives p_0 + p_1 > (3 p_1 + p_2)/2, so the second needs
    p_2 / 2 + p_3 > 3 p_1 / 2, impossible since p_2 < p_1 and p_3 <= p_1.
Induction from the terminal law (one atom) then gives unimodality at every time, for every T. G219's valley is C(B(q))
on an input q that is not C of any unimodal law (q = C(p) forces p = (40, 2, 42, ...)), so it cannot occur.

PREDICTIONS (Local's, published before the run):
  UP-P1: on every actual law with T <= TMAX: flat steps are never adjacent; every critical step gives law(r) =
         C(law(r+1)) exactly, and every flat step with r < T - 1 gives law(r) = B(C(law(r+2))) exactly (scaled
         integers, positions measured from ell).
  UP-P2: the lemma holds on every unimodal integer sequence of length 1 .. 6 with entries 0 .. 6, and on 200,000
         random unimodal sequences of length up to 40; C preserves unimodality on the same inputs.
  UP-P3: the case-B inequality pair (2 p_0 > p_1 + p_2 and p_2 + p_3 > p_0 + p_1) never holds for a unimodal p with
         mode exactly 1 in the exhaustive set.
  UP-C0 (control, can say no): C(B(q)) for G219's q = (20, 21, 22, 23, 24) is (61, 104, 88, 92, 71, 24) up to scale,
         not unimodal; and B(C(p)) fails to be unimodal for at least one NON-unimodal p in the exhaustive set.
OUTCOME, 2026-10-08 05:42 (M5, one run at commit 8339ba9; transcript outside Git; a few minutes). UP-P1, P2, P3
HELD and UP-C0 PASS: all 524,800 actual laws to T = 1024 follow C (331,624 critical steps) or B(C) (193,176 flat
steps) exactly and flat steps are never adjacent; the lemma holds on all 16,044 small unimodal inputs and 200,000
random ones; the mode-1 inequality pair never holds; G219's valley is reproduced and 75,797 non-unimodal inputs
give a non-unimodal B(C(p)), so the check can say no. The hand proof above awaits an independent reading.
"""
import random
import sys
from itertools import product

TMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1024


def unimodal(P):
    nz = [j for j, x in enumerate(P) if x]
    if not nz:
        return True
    lo, hi = nz[0], nz[-1]
    if any(P[j] == 0 for j in range(lo, hi + 1)):
        return False
    j = lo
    while j < hi and P[j + 1] >= P[j]:
        j += 1
    while j < hi and P[j + 1] <= P[j]:
        j += 1
    return j == hi


def C(p):
    return [p[0]] + [p[j - 1] + p[j] for j in range(1, len(p))] + [p[-1]]


def B(q):
    q = list(q) + [0]
    return [2 * q[0] + q[1]] + [q[j] + q[j + 1] for j in range(1, len(q) - 1)]


def strip(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def actual():
    ELL, a = [], 0
    for t in range(TMAX + 3):
        while 3 ** a <= 2 ** t:
            a += 1
        ELL.append(a)
    ELL[0] = 0
    adjacent = any(ELL[r + 1] == ELL[r] and ELL[r + 2] == ELL[r + 1] for r in range(TMAX))
    ok, nflat, ncrit = True, 0, 0
    for T in range(1, TMAX + 1):
        top = ELL[T] + 1
        F = [1 if x >= ELL[T] else 0 for x in range(top + 2)]
        laws = {T: strip([1])}
        for r in range(T - 1, -1, -1):
            l = ELL[r]
            G = [0] * (top + 2)
            for x in range(l, top + 1):
                G[x] = F[x] + F[x + 1]
            G[top + 1] = 2 ** (T - r)
            laws[r] = strip([G[l + j] - (G[l + j - 1] if l + j - 1 >= 0 else 0) for j in range(top + 1 - l + 1)])
            if ELL[r + 1] == l + 1:
                ncrit += 1
                ok &= laws[r] == strip(C(laws[r + 1]))
            else:
                nflat += 1
                if r < T - 1:
                    ok &= laws[r] == strip(B(C(laws[r + 2])))
            F = G
    return (not adjacent) and ok, nflat, ncrit


def unimodal_seqs(maxlen, maxv):
    for n in range(1, maxlen + 1):
        for p in product(range(maxv + 1), repeat=n):
            yield list(p)


def random_unimodal(rng):
    n = rng.randint(1, 40)
    m = rng.randint(0, n - 1)
    up = sorted(rng.randint(1, 10 ** 6) for _ in range(m + 1))
    down = sorted((rng.randint(1, up[-1]) for _ in range(n - m - 1)), reverse=True)
    return up + down


def main():
    p1, nflat, ncrit = actual()
    print('UP-P1', 'HELD' if p1 else 'REFUTED', '(%d flat and %d critical steps checked)' % (nflat, ncrit))
    p2 = p3 = True
    nonuni_fail = 0
    n_uni = 0
    for p in unimodal_seqs(6, 6):
        if unimodal(p):
            n_uni += 1
            p2 &= unimodal(B(C(p))) and unimodal(C(p))
            nz = [j for j, x in enumerate(p) if x]
            q = p + [0, 0, 0]
            if len(p) >= 2 and q[0] <= q[1] and q[1] > q[2]:
                p3 &= not (2 * q[0] > q[1] + q[2] and q[2] + q[3] > q[0] + q[1])
        else:
            nonuni_fail += not unimodal(B(C(p)))
    rng = random.Random(20261008)
    for _ in range(200000):
        p = random_unimodal(rng)
        p2 &= unimodal(B(C(p))) and unimodal(C(p))
    g = C(B([20, 21, 22, 23, 24]))
    c0 = g == [x * 1 for x in [61, 104, 88, 92, 71, 24]] and not unimodal(g) and nonuni_fail > 0
    print('UP-P2', 'HELD' if p2 else 'REFUTED', '(%d exhaustive unimodal inputs, 200000 random)' % n_uni)
    print('UP-P3', 'HELD' if p3 else 'REFUTED')
    print('UP-C0', 'PASS' if c0 else 'FAIL', '(G219 row %s; %d non-unimodal inputs give a non-unimodal B(C(p)))'
          % (g, nonuni_fail))


if __name__ == '__main__':
    main()
