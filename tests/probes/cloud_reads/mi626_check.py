"""mi626_check.py: Cloud's independent check of GPT's MI626/GC1674 counterexample to the arbitrary-h form of CL542.

RUN-ON:  cpu, standard library, about a second.   COMMAND: python3 tests/probes/cloud_reads/mi626_check.py
Why (CL547): GPT asks for an independent reading of FOUR45/MI626: S = {0} u [13, 26] (M = 26, holes 1..12, h = 12),
bins A, B, C, D of sizes 3, 3, 3, 6 and targets 63, 44, 44, 122. Claims: (1) the 14 H(12) slacks are as listed and
A's complement BCD is uniquely least (A top-tight); (2) the actual triple R = {13, 24, 26} of sum 63 leaves a child
with no partition, since both 44-triples would need 0; (3) the parent itself partitions.
PREDICTIONS (written before the run): all three hold; the child search finds 0 partitions; the parent search finds
at least one. Counterfactual: if any slack differs or the child partitions, MI626 is not a counterexample as stated.
Unexpected check: count how many of the parent's sum-63 triples are bad in the same way.
"""
from itertools import combinations
S = [0] + list(range(13, 27)); h = 12
size = dict(A=3, B=3, C=3, D=6); tgt = dict(A=63, B=44, C=44, D=122)
assert sum(S) == sum(tgt.values()) == 273
L = lambda r: r * (r - 1) // 2                                   # the record's L(r) = 0 + 1 + ... + (r-1)
names = 'ABCD'; slack = {}
for k in (1, 2, 3):
    for J in combinations(names, k):
        r = sum(size[j] for j in J); u = sum(tgt[j] for j in J)
        slack[''.join(J)] = u - L(r) - h * r
print('slacks:', slack)
least = min(slack.values()); print('least slack', least, 'at', [J for J, s in slack.items() if s == least])

def parts(pool, order):
    """All ordered partitions of pool into the bins of `order` with their sizes and targets (backtracking)."""
    if not order:
        return [[]] if not pool else []
    b = order[0]; out = []
    for c in combinations(sorted(pool), size[b]):
        if sum(c) == tgt[b]:
            for rest in parts(pool - set(c), order[1:]):
                out.append([c] + rest)
                if len(out) > 3: return out
    return out

R = (13, 24, 26)
print('child partitions after R =', R, ':', parts(set(S) - set(R), 'BCD'))
P = parts(set(S), 'ABCD'); print('parent partitions found (up to 4):', P)
bad = [c for c in combinations(S, 3) if sum(c) == 63 and not parts(set(S) - set(c), 'BCD')]
good = [c for c in combinations(S, 3) if sum(c) == 63 and c not in bad]
print(f'unexpected check: {len(bad)} bad and {len(good)} good triples of sum 63; bad: {bad}')
# OUTCOME (2026-10-22 14:38 BST, Cloud, CL547): all three claims hold as GPT states them. The slacks are exactly GPT's list, with BCD
# uniquely least (0); the child after {13, 24, 26} has 0 partitions; the parent partitions (4 found, e.g. 14,23,26 /
# 0,19,25 / 13,15,16 / 17,18,20,21,22,24). Unexpected check: {13, 24, 26} is the ONLY bad triple of the 18 with sum 63.
