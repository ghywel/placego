"""routing_obstruction.py: Erdős #120: can the geometric-case routing (OpenAI preprint, 5 October 2026) reach a
super-exponential sequence such as a_n = 2^{-n^2} by any choice of branching M, window lengths and gaps?

RUN-ON: cpu, python3 (standard library). COMMAND: python3 tests/probes/swarm/ladder/e120/routing_obstruction.py
Why (CL562): at the first default vertex U (height h), the preprint's union bound needs, for the scale representatives
of the LAST child edge e = (U, M-1),
    (M-1) * r_h * p/2  >  log D,   D >= a_{a_e} * N_{b*_e} >= a_{a_e} / a_{b*_e}   (N_b >= c / a_b, c >= 4),
with r_h >= g + sigma_{h-1} (the window covers the following child subtree), so b*_e - a_e = r_h + g + sigma_{h-1} - 1.
The sibling windows and subtrees of children 1..M-2 come first, so a_e >= n_0 + (M-2)(r_h + g + sigma_{h-1}).
For a_n = 2^{-n^2}: log(a_{a_e}/a_{b*_e}) = ((b*)^2 - a_e^2) ln 2 >= 2 a_e (b* - a_e) ln 2, which grows with M.
Record searched: CL560-561, PRIOR-ART #120.
PREDICTIONS (before the run): for every M in 3..400, r_1 in 1..30, g in 1..6 and n_0 = 1, the p required at a
height-2 vertex exceeds 1 (impossible, since p is a density), with the smallest required p well above 1.
Counterfactual: some parameters with required p < 1 (the obstruction is only an artefact of my bound).
For contrast, a geometric sequence (ell_n = log 2) and the bounded-ratio class need p of order 1/M (feasible).
"""
import math


def sigma(h, M, r1, g):
    """span of all windows (with gaps) in a subtree of height h, and r_h, per the preprint's recursion."""
    r, s = r1, M * r1 + (M - 1) * g
    for _ in range(2, h + 1):
        r = max(r1, g + s)
        s = M * (r + g + s) + (M - 1) * g
    return r, s


def required_p(ell_sum, M, h, r1, g, n0=1):
    r_h, _ = sigma(h, M, r1, g)
    s_prev = sigma(h - 1, M, r1, g)[1] if h >= 2 else 0
    block = r_h + g + (s_prev if h >= 2 else 0)
    a_e = n0 + (M - 2) * (block + g)
    b_star = a_e + (block if h >= 2 else r_h) - 1
    logD = max(0.0, ell_sum(a_e, b_star))
    return 2 * logD / ((M - 1) * r_h)


sq = lambda a, b: (b * b - a * a) * math.log(2)     # a_n = 2^{-n^2}
geo = lambda a, b: (b - a) * math.log(2)            # a_n = 2^{-n}
best_sq, best_geo = math.inf, math.inf
for M in range(3, 401):
    for r1 in range(1, 31):
        for g in range(1, 7):
            best_sq = min(best_sq, required_p(sq, M, 2, r1, g))
            best_geo = min(best_geo, required_p(geo, M, 2, r1, g))
print(f'height-2 vertex, smallest required p: 2^(-n^2) {best_sq:.3f};  2^(-n) {best_geo:.4f}')
# the same at height 1 (children are leaves, b* = window end): position-dependent too
best1 = min(required_p(sq, M, 1, r1, g) for M in range(3, 401) for r1 in range(2, 31) for g in range(1, 7))
print(f'height-1 vertex with r >= 2, smallest required p for 2^(-n^2): {best1:.3f}')

# OUTCOME (2026-10-22 18:12 BST, Cloud, CL562): smallest required p at a height-2 vertex is 49.56 for 2^{-n^2} over
# M in 3..400, r_1 in 1..30, g in 1..6 (impossible: p is a density), against 0.0069 for 2^{-n}. Height-1 vertices with
# r >= 2 need p >= 3.81; only r = 1 at height 1 escapes, and defaults there carry probability about 2^{1-M}, while
# d must be about 2^M log(1/p) levels deep. Prediction held; no counterfactual. Scope: this obstructs the preprint's
# mechanism AS WRITTEN (sequential sibling windows, scale count at the subtree's finest grid). The required p is a lower
# bound, since D's extra factors were dropped. It is not a theorem about every construction.
