#!/usr/bin/env python3
"""B24 / MI058, preregistered 8ed0259e before execution, 2026-10-16.

Nine fixed fixtures only, not a tuple census or burnability decision procedure.
Construct two three-donor walks with signed losses, optionally relay endpoints.
Must-hold: four hand-candidate fixtures and the known balanced control produce
literal certificates. Blind: all four listed irregular fixtures also do so.
Controls: independent certificate checker; dropping a necessary relay preserves
coverage but fails target sums; old reused-pair counterfactual is rejected.
Unexpected: the 96^7,112 fixture has no four-target subset summing to 392.
Caps: 100,000 root configurations/fixture, five process CPU seconds overall.
Any cutoff is UNKNOWN; no witness in this class does not mean unburnable.
Raw output outside git.
OUTCOME (2026-10-16, GPT Intel CPU): 8/9 fixtures WITNESS, including known
control; blind1 NO_WITNESS_IN_CLASS after 80 root configurations, no cutoff.
Must-hold controls pass, blind all-four prediction REFUTED (3/4 pass).
Omitted relay rejected with coverage preserved; reused pair rejected;
four-subset sums {384:35,400:35}. CPU 0.003559 s.
Raw math-instinct-b24-coupled-chains.json stays outside git.
SHA256: 3f650d557b791abcaa5a216dfa31de421a0de1faef92560b24ed82704f519344.

ADDENDUM BEFORE REPAIR CHECK (MI059): no more fixture search. For blind1,
choose receiver targets (68,92) instead of (68,68), roots (13,1), loss
groups ((-10,44,-10),(44,-10,-10)). Predict literal certificate success;
the relay changes receiver sums (80,80) to (68,92). Independent checker
must pass, while omitting this relay must fail target sums. Stop after
this one fixed repair; no cap increase or general role search.
REPAIR OUTCOME (2026-10-16): WITNESS; literal/endpoint/certificate checks
pass, omitted relay rejected. Receiver sums (80,80) -> (68,92).
CPU 0.000177 s; raw math-instinct-b24-repair.json outside git.
SHA256: 545a5ff1d287775d6ed1ccd4f0a7cb4f33528f413272aa1ea402caf7a2faf51a.
Original blind1 NO_WITNESS_IN_CLASS and the refuted prediction are retained.
"""

from collections import Counter
from itertools import combinations, permutations
import json
import sys
import time

from path_forest_receiving_chains import certificate_ok, checked_schedule


FIXTURES = [
    ("k9", [110] * 2 + [94] * 6),
    ("k10", [116] * 2 + [92] * 6),
    ("k11", [122] * 2 + [90] * 6),
    ("coupled", [96] * 7 + [112]),
    ("blind1", [68, 68, 68, 92, 122, 122, 122, 122]),
    ("blind2", [68, 70, 82, 100, 108, 116, 118, 122]),
    ("blind3", [68, 72, 94, 98, 104, 112, 114, 122]),
    ("blind4", [70, 78, 88, 96, 104, 110, 116, 122]),
    ("balanced_control", [98] * 8),
]


def offsets(losses):
    out = [0]
    for loss in losses:
        if loss:
            out.append(out[-1] + loss)
    return out


def possible_roots(walk):
    lo, hi = max(1, 1 - min(walk)), min(55, 55 - max(walk))
    if lo % 2 == 0:
        lo += 1
    return range(lo, hi + 1, 2)


def materialize(roots, loss_groups, relay):
    paths = [[a + s for s in offsets(g)] for a, g in zip(roots, loss_groups)]
    selected = [v for path in paths for v in path]
    if any(v % 2 != 1 or not 1 <= v <= 55 for v in selected):
        return None
    labels = [min(v, 56 - v) for v in selected]
    if len(labels) != len(set(labels)):
        return None
    bins = [{a, 56 - a} for a in roots] + [set() for _ in range(6)]
    moves = []
    for r, (a, group) in enumerate(zip(roots, loss_groups)):
        current = a
        for j, loss in enumerate(group):
            donor = 2 + 3 * r + j
            if loss:
                nxt = current + loss
                bins[donor] = {nxt, 56 - nxt}
                moves.append((r, donor, current, nxt))
                current = nxt
    free = iter(x for x in range(1, 28, 2) if x not in set(labels))
    for donor in range(2, 8):
        while len(bins[donor]) < 4:
            x = next(free)
            bins[donor].update((x, 56 - x))
    assert next(free, None) is None
    assert Counter(v for b in bins for v in b) == Counter(range(1, 56, 2))
    for r, donor, current, nxt in moves:
        assert current in bins[r] and nxt in bins[donor]
        bins[r].remove(current)
        bins[donor].remove(nxt)
        bins[r].add(nxt)
        bins[donor].add(current)
    for r in range(2):
        assert bins[r] == {paths[r][-1], 56 - roots[r]}
    assert list(map(sum, bins[2:])) == [112 - d for g in loss_groups for d in g]
    before = [sorted(b) for b in bins]
    if relay:
        u, v = paths[0][-1], paths[1][-1]
        assert u != v and u in bins[0] and v in bins[1]
        bins[0].remove(u)
        bins[1].remove(v)
        bins[0].add(v)
        bins[1].add(u)
        assert bins[0] == {v, 56 - roots[0]}
        assert bins[1] == {u, 56 - roots[1]}
    return dict(roots=roots, losses=loss_groups, paths=paths, relay=relay,
                bins=[sorted(b) for b in bins], before_relay=before,
                moves=moves)


def find(targets, deadline):
    targets = sorted(targets)
    assert len(targets) == 8 and sum(targets) == 784
    assert all(t % 2 == 0 and 68 <= t <= 122 for t in targets)
    A, B = targets[:2]
    losses = [112 - t for t in targets[2:]]
    count = 0
    for perm in sorted(set(permutations(losses))):
        if time.process_time() >= deadline:
            return dict(status="UNKNOWN_CPU", configurations=count)
        groups = (perm[:3], perm[3:])
        walks = tuple(offsets(g) for g in groups)
        if any(len(w) != len(set(w)) for w in walks):
            continue
        D1, D2 = map(sum, groups)
        assert D1 + D2 == A + B - 112
        relay = not (D1 == A - 56 and D2 == B - 56)
        for a in possible_roots(walks[0]):
            bs = (a + A - 56 - D2,) if relay else possible_roots(walks[1])
            for b in bs:
                if count >= 100000:
                    return dict(status="UNKNOWN_CAP", configurations=count)
                if time.process_time() >= deadline:
                    return dict(status="UNKNOWN_CPU", configurations=count)
                count += 1
                witness = materialize((a, b), groups, relay)
                if witness is None:
                    continue
                assert certificate_ok(witness['bins'], targets)
                return dict(status="WITNESS", configurations=count,
                            targets=targets, witness=witness)
    return dict(status="NO_WITNESS_IN_CLASS", configurations=count,
                targets=targets)


def main():
    start = time.process_time()
    deadline = start + 5
    results = []
    for name, targets in FIXTURES:
        result = find(targets, deadline)
        result['name'] = name
        results.append(result)
    special = [96] * 7 + [112]
    subset_sums = Counter(sum(special[i] for i in inds)
                          for inds in combinations(range(8), 4))
    assert subset_sums == {384: 35, 400: 35} and 392 not in subset_sums
    coupled = next(r for r in results if r['name'] == 'coupled')
    assert coupled['status'] == 'WITNESS'
    witness = coupled['witness']
    assert witness['relay']
    before = witness['before_relay']
    assert Counter(v for b in before for v in b) == Counter(range(1, 56, 2))
    assert not certificate_ok(before, special)
    try:
        checked_schedule(5, (1, 3))
    except ValueError:
        pair_control = 'REJECTED'
    else:
        raise AssertionError('reused-pair counterfactual accepted')
    print(json.dumps(dict(results=results, subset_sums=dict(subset_sums),
                          omitted_relay='REJECTED_TARGETS_COVERAGE_PRESERVED',
                          reused_pair=pair_control,
                          cpu_seconds=time.process_time() - start), indent=2))


def repair_boundary():
    start = time.process_time()
    target = [68, 68, 68, 92, 122, 122, 122, 122]
    witness = materialize((13, 1), ((-10, 44, -10), (44, -10, -10)), True)
    assert witness is not None
    assert list(map(sum, witness['before_relay'][:2])) == [80, 80]
    assert list(map(sum, witness['bins'][:2])) == [68, 92]
    assert certificate_ok(witness['bins'], target)
    assert not certificate_ok(witness['before_relay'], target)
    print(json.dumps(dict(targets=target, witness=witness,
                          status='WITNESS', omitted_relay='REJECTED',
                          cpu_seconds=time.process_time() - start), indent=2))


if __name__ == '__main__':
    if sys.argv[1:] == ['--repair-boundary']:
        repair_boundary()
    elif not sys.argv[1:]:
        main()
    else:
        raise SystemExit('Only the preregistered fixed modes are available')
