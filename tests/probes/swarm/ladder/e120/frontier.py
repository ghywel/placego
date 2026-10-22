"""frontier.py: Erdős #120: two elementary checks on where the similarity problem stands after the geometric case.

RUN-ON: cpu, python3 (standard library). COMMAND: python3 tests/probes/swarm/ladder/e120/frontier.py
Why (CL560): an external preprint (OpenAI Math Release, 5 October 2026, unrefereed, not built here) claims every
geometric progression {q^n} is avoided by compact sets of measure > 1 - eta. Two hand facts place the remaining case:
  (a) avoiding an infinite SUBSET of A avoids A (a copy of A contains a copy of the subset); and
  (b) GREEDY LEMMA: if a_n decreases to 0 with a_{n+1} >= c a_n, pick each next term as the first a_m <= a_k / 2;
      then a_m >= c a_{m-1} > c a_k / 2, so the chosen subsequence has every ratio in [c/2, 1/2].
So any extension of the geometric method to ratios confined to [c/2, 1/2] would cover every null sequence with
liminf a_{n+1}/a_n > 0. What remains is the super-exponential regime, where Chlebik's criterion (normalized minimum
gap of m-point subsets e^{-o(m)}) fails even more badly than for geometric sequences.
Record searched: "similarity problem", dyadic, "Green's problem 94": no earlier hit.
PREDICTIONS (before the run): (b) holds on random sequences with ratios in [c, 1) (every chosen ratio in [c/2, 1/2]);
for a_n = 2^{-n^2} the best -log2(normalized min gap)/m over consecutive m-windows grows with m (super-linear decay),
while for 2^{-n} it stays near 1. Counterfactual: a chosen ratio outside [c/2, 1/2] (the lemma is wrong), or a bounded
ratio for 2^{-n^2} (the regime split is wrong).
"""
import math, random
from fractions import Fraction as F

random.seed(5)
ok = True
for trial in range(2000):
    c = F(random.randint(1, 9), 10)
    a = [F(1)]
    for _ in range(400):
        a.append(a[-1] * (c + (1 - c) * F(random.randint(0, 999), 1000)))
    sub, k = [a[0]], 0
    for m in range(1, len(a)):
        if a[m] <= a[k] / 2:
            sub.append(a[m]); k = m
    ok &= all(c / 2 <= sub[i + 1] / sub[i] <= F(1, 2) for i in range(len(sub) - 1))
print('greedy lemma on 2000 random sequences:', 'PASS' if ok else 'FAIL')


def best_rate(exps, m):
    """min over consecutive windows of -log2(min gap / span) / m, for a_n = 2^{-exps[n]} (log-space)."""
    best = math.inf
    for s in range(0, len(exps) - m):
        e = exps[s:s + m]
        # a_i - a_{i+1} >= a_i / 2 here, so min gap ~ a_{m-2}, span ~ a_0: rate ~ (e[m-2] - e[0] + 1) / m
        best = min(best, (e[m - 2] - e[0] + 1) / m)
    return best


for m in (4, 8, 16, 32, 64):
    print(f'm={m:2d}: geometric 2^-n rate {best_rate(list(range(200)), m):.3f}; '
          f'2^-n^2 rate {best_rate([n * n for n in range(1, 200)], m):.3f}')

# OUTCOME (2026-10-22, Cloud, CL560): greedy lemma PASS on 2000 random sequences. Rates: geometric stays near
# (m-1)/m < 1; 2^{-n^2} grows like m (best window at the start). Both predictions held; no counterfactual. The rate
# estimate uses the lower bound a_i - a_{i+1} >= a_i/2, valid for both sequences; it is a placement check, not a proof
# that the routing method fails super-exponentially.
