"""g342_check.py: Cloud's carrying-read checks for GPT's G342 (Erdős #132, cocircular-plus-one family; CL552).

RUN-ON: cpu, python3 (sympy optional). COMMAND: python3 tests/probes/cloud_reads/g342_check.py
Checks (1) the algebra: t = 1 + d/h and h((t+1)^2 + 2t) = 6h + d^2 give d = 6h/(h-1), t = (h+5)/(h-1), and
d - (1+sqrt t)^2 = 4 - 2 sqrt t > 0 for h > 3; (2) the moment identities sum_z |p-z|^2 = h(t+1) and
sum_z |p-z|^4 = h((t+1)^2 + 2t) for any p and any Y on the unit circle with S = 0 and T = (h/2) I (regular h-gons);
(3) unexpected check: on random configurations (regular h-gon or random cocircular points, h = 6..12, plus a random
or special extra point), count distances with multiplicity in [1, n]; the theorem predicts at least 2 every time.
PREDICTIONS (before the run): all three pass; (3) never finds fewer than 2 rare distances.
"""
import math, random, itertools
from fractions import Fraction
# (1) algebra, exact for h = 4..40
for h in range(4, 41):
    d = Fraction(6 * h, h - 1); t = 1 + d / h
    assert t == Fraction(h + 5, h - 1)
    assert h * ((t + 1) ** 2 + 2 * t) == 6 * h + d * d
    assert d - (1 + math.sqrt(t)) ** 2 > 1e-12 and abs((d - (1 + math.sqrt(t)) ** 2) - (4 - 2 * math.sqrt(t))) < 1e-9
print('(1) algebra: d = 6h/(h-1), t = (h+5)/(h-1), gap 4 - 2 sqrt(t) > 0 for h = 4..40: PASS')
# (2) identities on regular h-gons
rnd = random.Random(342)
for h in range(6, 13):
    Y = [(math.cos(2 * math.pi * k / h), math.sin(2 * math.pi * k / h)) for k in range(h)]
    for _ in range(20):
        p = (rnd.uniform(-3, 3), rnd.uniform(-3, 3)); t = p[0] ** 2 + p[1] ** 2
        s2 = sum((p[0] - x) ** 2 + (p[1] - y) ** 2 for x, y in Y)
        s4 = sum(((p[0] - x) ** 2 + (p[1] - y) ** 2) ** 2 for x, y in Y)
        assert abs(s2 - h * (t + 1)) < 1e-9 and abs(s4 - h * ((t + 1) ** 2 + 2 * t)) < 1e-7
print('(2) moment identities on regular h-gons, h = 6..12: PASS')
# (3) rare-distance counts
def rare(points):
    from collections import Counter
    c = Counter(round(math.dist(a, b), 9) for a, b in itertools.combinations(points, 2))
    n = len(points); return sum(1 for v in c.values() if 1 <= v <= n)
worst = 99
for h in range(6, 13):
    for trial in range(60):
        if trial % 2: Y = [(math.cos(2 * math.pi * k / h), math.sin(2 * math.pi * k / h)) for k in range(h)]
        else:
            ang = sorted(rnd.uniform(0, 2 * math.pi) for _ in range(h)); Y = [(math.cos(a), math.sin(a)) for a in ang]
        cands = [(0.0, 0.0), (rnd.uniform(-2, 2), rnd.uniform(-2, 2)), (2.0, 0.0), (0.5, 0.0)]
        for p in cands:
            worst = min(worst, rare(Y + [p]))
print('(3) fewest rare distances found:', worst, '(theorem: >= 2)')
# OUTCOME (2026-10-22 15:31 BST, Cloud, CL552): (1) PASS; (2) PASS; (3) fewest rare distances = 2, never fewer. Predictions held.
