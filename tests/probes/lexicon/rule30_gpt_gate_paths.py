#!/usr/bin/env python3
"""GC393: finite column6 histories compatible with GW's reported column4/5 tail.

Prediction (before run): both values at offset -6 remain possible after exact
column6 updates with free column7. Counterfactual: a locally erased input is
necessarily free under all other constraints. Controls: brute-force bit strings
versus forward path construction. Unexpected check: pin both reported endpoints.
OUTCOME: 12 of 16384 strings survive; value at -6 is 0 in eight, 1 in four.
Forward construction equals brute force; the reported GW path is retained.
Pinning the reported endpoints removes no paths (both endpoints already forced).
Exploratory reading: first column6 discrepancy can be -13 or -11, so GW's -13
onset is not necessary in this relaxation. No claim about a real right half.
Only offsets -14..-1, not a global Rule30 witness or a claim about death127.
RUN-ON: CPU, standard library, one process, under a second.
"""
import itertools
import json

WORDS = {
    4: '10111101101011110110101111011010111101101011110011110110',
    5: '10000001011000000101100000010110000001011010101110000101',
    6: '00111111000011111100001111110000111111010110100101111100',
}
DIFFS = {4: {-5, -3, -1}, 5: {-10, -8, -6, -4, -3, -2},
         6: {-13, -11, -9, -7, -6, -3, -2, -1}}
OFFSETS = tuple(range(-14, 0))


def actual(j, k):
    return int(WORDS[j][(12 + k) % 56]) ^ (k in DIFFS[j])


def allowed(k):
    if k == -1:  # No supplied column5 output at the kick itself.
        return (0, 1)
    return tuple(r for r in (0, 1)
                 if actual(4, k) ^ (actual(5, k) | r) == actual(5, k + 1))


def follows(k, b, nxt):
    return any(actual(5, k) ^ (b | r) == nxt for r in (0, 1))


def main():
    brute = {bits for bits in itertools.product((0, 1), repeat=len(OFFSETS))
             if all(b in allowed(k) for k, b in zip(OFFSETS, bits))
             and all(follows(k, bits[i], bits[i + 1])
                     for i, k in enumerate(OFFSETS[:-1]))}
    paths = {(b,) for b in allowed(OFFSETS[0])}
    for k in OFFSETS[1:]:
        paths = {p + (b,) for p in paths for b in allowed(k)
                 if follows(k - 1, p[-1], b)}
    assert paths == brute
    reported = tuple(actual(6, k) for k in OFFSETS)
    assert reported in paths
    i = OFFSETS.index(-6)
    pinned = {p for p in paths if p[0] == reported[0] and p[-1] == reported[-1]}
    result = {
        'brute_candidates': 2 ** len(OFFSETS),
        'surviving_paths': len(paths),
        'values_at_minus6': sorted({p[i] for p in paths}),
        'counts_by_minus6': {str(b): sum(p[i] == b for p in paths) for b in (0, 1)},
        'pinned_paths': len(pinned),
        'first_difference_offsets': sorted({next(k for k, b in zip(OFFSETS, p)
            if b != int(WORDS[6][(12 + k) % 56])) for p in paths}),
        'pinned_values_at_minus6': sorted({p[i] for p in pinned}),
        'controls': 'forward construction equals brute force; reported path retained',
        'examples': {str(b): next((p for p in sorted(paths) if p[i] == b), None)
                     for b in (0, 1)},
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
