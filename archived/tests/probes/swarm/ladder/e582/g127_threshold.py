"""g127_threshold.py: Erdős #582: where between 60 and 80 vertices do G127's induced subgraphs turn hard to colour?

RUN-ON: cpu, python3 with python-sat. COMMAND: python3 tests/probes/swarm/ladder/e582/g127_threshold.py
Why (CL550): g127_subgraphs.py found every random induced subgraph SAT at once at m = 60 and every one at m >= 80 a
5-second TIMEOUT, against the prediction. A longer budget separates "hard but colourable" from a candidate.
PREDICTIONS (before the run): the change is sharp, between m = 64 and 76; with 25 s, the m = 80 samples are found SAT
(hard, not arrowing). Counterfactual: an m = 80 sample still TIMEOUT at 25 s stays a lead for a long run and a proof.
"""
import random, sys
sys.path.insert(0, 'tests/probes/swarm/ladder/e582')
from g127_subgraphs_lib import colour
rnd = random.Random(1270)
for m, budget in ((64, 10), (68, 10), (72, 10), (76, 10), (80, 25)):
    rows = [colour(rnd.sample(range(127), m), budget) for _ in range(3)]
    print(f'm={m}: ' + ', '.join(f'{r} {d:.1f}s' for r, d, _ in rows), flush=True)
# OUTCOME (2026-10-22 15:03 BST, Cloud, CL550): m = 64, 68, 72: all SAT at once; m = 76: SAT in 0.2 to 0.7 s; m = 80: SAT 0.1 s,
# SAT 4.4 s, TIMEOUT 25 s. A sharp hardness threshold near 76 to 80 with a heavy tail: hard but (so far) colourable.
# Not evidence of arrowing; the m = 80 sample that timed out is the next run's lead (longer budget, then a proof).
