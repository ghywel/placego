"""GC549.38: fixed whole-row gluing control, horizon 17, two fixtures.

Predictions were stated before execution in the tool request, but the ledger
append failed on a quoting error and execution proceeded. This is a retained
recording failure, not a successfully ledger-preregistered experiment.
P: empty right seed and {1,3,5}, joined to scalar inverse left prefixes,
produce the full 0101 clock through 17 in an unclamped whole-row update.
CF: changing initial depth 17 leaves the last sample unchanged (expect false).
Unexpected: changing either initial site -18 or +18 preserves all samples.
OUTCOME: P held, CF refuted, exterior checks passed on both fixed fixtures.
Codes: 010001010 and 100010100. No record search or longer horizon.
Run: python3 tests/probes/lexicon/rule30_gpt_gluing_control.py
"""
from rule30_gpt_gc549_certificate import scalar_inverse

T = 17


def step(row):
    # Independent decimal rule lookup; no centre overwrite.
    lo, hi = min(row, default=0) - 1, max(row, default=0) + 1
    return {i for i in range(lo, hi + 1)
            if (30 >> (4 * (i - 1 in row) + 2 * (i in row)
                       + (i + 1 in row))) & 1}


def trace(row):
    out = []
    for _ in range(T + 1):
        out.append(int(0 in row))
        row = step(row)
    return out


def main():
    target = [t % 2 for t in range(T + 1)]
    for seed in (set(), {1, 3, 5}):
        right, code = set(seed), []
        for t in range(T):
            if t % 2 == 0:
                code.append(int(1 in right))
            wall = t % 2
            right = {i for i in range(1, T + 3)
                     if (wall if i == 1 else int(i - 1 in right))
                     ^ int(i in right or i + 1 in right)}
        initial = scalar_inverse(code)
        joined = set(seed) | {-j for j in range(1, T + 1) if initial[j]}
        assert trace(joined) == target
        changed = trace(joined ^ {-T})
        assert changed[:T] == target[:T] and changed[T] == 1 - target[T]
        for exterior in (-18, 18):
            assert trace(joined ^ {exterior}) == target
        print(sorted(seed), ''.join(map(str, code)), 'whole-row and controls PASS')


if __name__ == '__main__':
    main()
