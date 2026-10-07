#!/usr/bin/env python3
"""GC395: complete GC393's 14-row tail through its finite backward cone.
Prediction before run: all12 relaxed column6 paths have a finite completion
(P1, confidence0.5); both values at s-6 persist (P2, confidence0.7).
Counterfactual: exact exterior dynamics eliminate a locally allowed path.
Controls: list-cell versus integer-bit simulation on every candidate; recorded
GW column6 path must occur under the full left-strip comparison.
Unexpected check: compare targets4/5 alone versus the full1..5 target.
8192 initial assignments to7..19;1..6 fixed at s-14; supplied wall0 alternates.
OUTCOME: P1 and P2 REFUTED. Exactly672 initial assignments produce the tail;
only one of the12 relaxed column6 paths occurs, the reported GW path, with0 at-6.
Targets4/5 and1..5 give identical counts; both controls PASS. The eleven other
relaxed paths fail finite exterior consistency, not merely long preparation.
Finite right-half evolution only; no126-step preparation or two-sided wall claim.
RUN-ON: CPU, Python standard library, one process, seconds.
"""
import itertools
import json
from rule30_gpt_gate_paths import WORDS, DIFFS, OFFSETS, actual, allowed, follows

U = '00010011010001001101000100110100010011010001001101001101'
EXTRA = {2: '01110010110111001011011100101101110010110111001011001011',
         3: '11000110101100011010110001101011000110101100011000011010'}
EXTRA_DIFFS = {1: set(), 2: {-1}, 3: {-4, -2}}


def target(j, k):
    if j >= 4:
        return actual(j, k)
    word = U if j == 1 else EXTRA[j]
    return int(word[(12 + k) % 56]) ^ (k in EXTRA_DIFFS[j])


def main():
    relaxed = {p for p in itertools.product((0, 1), repeat=14)
               if all(b in allowed(k) for k, b in zip(OFFSETS, p))
               and all(follows(k, p[i], p[i + 1]) for i, k in enumerate(OFFSETS[:-1]))}
    assert len(relaxed) == 12
    counts = {'tail45': 0, 'tail15': 0}
    paths = {name: set() for name in counts}
    examples = {}
    for seed in range(8192):
        row = [0] + [target(j, -14) for j in range(1, 7)]
        row += [(seed >> i) & 1 for i in range(13)]
        packed = sum(b << j for j, b in enumerate(row))
        ok45 = ok15 = True
        path = []
        for k in OFFSETS:
            assert row == [(packed >> j) & 1 for j in range(len(row))]
            ok45 &= all(row[j] == target(j, k) for j in (4, 5))
            ok15 &= all(row[j] == target(j, k) for j in range(1, 6))
            path.append(row[6])
            if k != -1:
                n = len(row) - 1
                row = [(k + 1) % 2] + [row[j-1] ^ (row[j] | row[j+1])
                                      for j in range(1, n)]
                packed = ((packed << 1) ^ (packed | (packed >> 1))) & ((1 << n) - 1)
                packed = (packed & ~1) | ((k + 1) % 2)
        p = tuple(path)
        for name, ok in (('tail45', ok45), ('tail15', ok15)):
            if ok:
                counts[name] += 1
                paths[name].add(p)
                assert p in relaxed
                examples.setdefault((name, p), seed)
    reported = tuple(actual(6, k) for k in OFFSETS)
    assert reported in paths['tail15']
    result = {
        'initial_candidates': 8192,
        'completion_counts': counts,
        'distinct_paths': {name: len(p) for name, p in paths.items()},
        'values_at_minus6': {name: sorted({p[8] for p in ps}) for name, ps in paths.items()},
        'missing_relaxed_paths': {name: len(relaxed - ps) for name, ps in paths.items()},
        'controls': 'all candidate rows agree between scalar and packed simulation; GW path retained',
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
