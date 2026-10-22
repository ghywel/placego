"""bounded_ratio_check.py: Erdős #120: numerical replay of the three q-dependent estimates of the geometric-case
preprint (OpenAI, 5 October 2026) for a NON-geometric sequence with ratios in [kappa, lam].

RUN-ON: cpu, python3 (standard library, exact Fractions). COMMAND: python3 tests/probes/swarm/ladder/e120/bounded_ratio_check.py
Why (CL561): reading sections 2-5 of the preprint, q enters only through (i) the grid N_b = 2^ceil(log2(c q^-b)),
c = 4/(1-q); (ii) the stability density 4 c q^{g+1}; (iii) the separation lemma; (iv) the scale count 1 + 2 c q^{-2r}.
Replacing q^b by a_b and c by 4/(1-lam): (ii) becomes <= 4c lam^{g+1}, (iii) needs only a_{n+1} <= lam a_n,
(iv) becomes <= 1 + 2c kappa^{-2r}, and the branching condition becomes p(M-1)/2 > 2 log(1/kappa).
Record searched: CL560, PRIOR-ART #120.
PREDICTIONS (before the run): on random sequences with ratios in [0.3, 0.5]: (iii) every window's points have
distinct keys J_b at b = window end, for random centers and scales; (ii) the exact stability density per window is
<= 4c lam^{g+1}; (iv) the exact boundary count 1 + floor(a_n N_{b*}) is <= 1 + 2c kappa^{-(b*-a_e)}.
Counterfactual: any violation, which would mean the substitution misses a hidden use of q.
"""
import math, random
from fractions import Fraction as F

random.seed(11)
kappa, lam = F(3, 10), F(1, 2)
c = 4 / (1 - lam)
viol = 0
for trial in range(300):
    a = [F(1, 16)]
    for _ in range(60):
        a.append(a[-1] * (kappa + (lam - kappa) * F(random.randint(0, 1000), 1000)))
    N = [2 ** math.ceil(math.log2(c / x)) for x in a]
    assert all(N[i] <= N[i + 1] for i in range(len(N) - 1))
    # a window [s, e] with s >= 1 and a gap g before it from previous end bp = s - g - 1
    g = random.randint(1, 4); s = random.randint(g + 2, 30); e = s + random.randint(1, 8)
    bp = s - g - 1
    # (ii) stability density of [gamma - 2 a_s, gamma), gamma in N_bp^{-1} Z, per unit period
    dens = N[bp] * 2 * a[s]
    viol += dens > 4 * c * lam ** (g + 1)
    # (iii) separation at resolution b = e for random x, t
    for _ in range(20):
        x = F(random.randint(0, 10 ** 6), 10 ** 6); t = 1 + F(random.randint(0, 1000), 1000)
        pts = [x] + [x + t * a[n] for n in range(s, e + 1)]
        keys = [math.floor(N[e] * (z - math.floor(z))) for z in pts]
        viol += len(set(keys)) != len(keys)
    # (iv) boundary crossings of y_n(t) = x + t a_n, t in [1, 2], on the grid of b* (take b* = e + random extra)
    bstar = e + random.randint(0, e - s + 1)
    if bstar < len(a):
        for n in range(s, e + 1):
            viol += 1 + math.floor(a[n] * N[bstar]) > 1 + 2 * c * kappa ** (-(bstar - s))
print('violations:', viol)

# OUTCOME (2026-10-22, Cloud, CL561): violations 0 over 300 random sequences (ratios in [0.3, 0.5]) and 6,000 random
# (center, scale) separation tests. Prediction held; no hidden use of q appeared in these three estimates. A numerical
# replay of inequalities only: the routing, no-default and density lemmas (sections 4-5) do not involve q and were read,
# not replayed; the whole argument stays the preprint's, unrefereed.
