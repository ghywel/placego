#!/usr/bin/env python3
"""GC2256 fixed finite controls, not a seed census or a density experiment.

Ten prescribed gate families, eight fixed seeds, twelve bits. Compare literal
truth-table dynamics to bit-parallel ANF, and check the generic Path clauses.
The payload is single-threaded and creates no subprocesses. See the report's
frozen stage specification; never expand or rerun automatically after failure.
"""
import hashlib
import json
import os
import resource
import time
from pathlib import Path

WIDTH = 12
SEEDS = (0, 1, 3, 5, 21, 85, 170, 1113)
TABLES = (8, 7, 2, 13, 4, 11, 14, 1)  # bits indexed by 2*b+s


def literal(x, gates):
    y = 0
    for j, g in enumerate(gates):
        b = (x >> (j - 1)) & 1 if j else 0
        s = (x >> (j - 2)) & 1 if j >= 2 else 0
        y |= (((x >> j) & 1) ^ ((TABLES[g] >> (2*b+s)) & 1)) << j
    return y


def parallel(x, gates):
    alpha = sum(((g >> 2) & 1) << j for j, g in enumerate(gates))
    beta = sum(((g >> 1) & 1) << j for j, g in enumerate(gates))
    gamma = sum((g & 1) << j for j, g in enumerate(gates))
    return (x ^ ((x << 1) & (x << 2)) ^ ((x << 1) & alpha)
            ^ ((x << 2) & beta) ^ gamma) & ((1 << WIDTH)-1)


def order(word, period):
    if not word:
        return period - 1
    mask = (1 << period)-1
    for degree in range(1, period+1):
        word ^= (word >> 1) | ((word & 1) << (period-1))
        word &= mask
        if not word:
            return period-degree
    raise AssertionError('dyadic differences did not vanish')


def qbound(nu, m):
    threshold, q = 1, 0
    while threshold <= m:
        power = nu+threshold+q
        threshold = m+1 if power > m.bit_length() else threshold+(1 << power)
        q += 1
    return q


def profile_word(states, j, period):
    return sum(((states[t % len(states)] >> j) & 1) << t for t in range(period))


def main():
    start = time.process_time()
    assert resource.getrlimit(resource.RLIMIT_CPU) == (60, 60)
    families = [tuple([g]*WIDTH) for g in range(8)]
    families += [tuple(6 if j % 2 else 0 for j in range(WIDTH)),
                 tuple(j % 8 for j in range(WIDTH))]
    records = []
    pair_counts = [0, 0, 0]
    windows = 0
    for family, gates in enumerate(families):
        for seed in SEEDS:
            states, seen, x = [], set(), seed
            while x not in seen:
                assert len(states) < 1 << WIDTH
                seen.add(x)
                states.append(x)
                y = literal(x, gates)
                assert y == parallel(x, gates), ('oracle', family, seed, x)
                x = y
            assert x == seed, ('transient', family, seed)
            periods = []
            for j in range(WIDTH):
                mask = (1 << (j+1))-1
                p = next(t for t in range(1, len(states)+1)
                         if (states[t % len(states)] & mask) == (seed & mask))
                assert p & (p-1) == 0
                old = periods[-1] if j else 1
                parity = 0
                for t in range(old):
                    z = states[t]
                    b = (z >> (j-1)) & 1 if j else 0
                    s = (z >> (j-2)) & 1 if j >= 2 else 0
                    parity ^= (TABLES[gates[j]] >> (2*b+s)) & 1
                assert p == old << parity, ('lift', family, seed, j)
                periods.append(p)
            exponents = [p.bit_length()-1 for p in periods]
            resources = [order(profile_word(states, j, p), p)
                         for j, p in enumerate(periods)]
            for j in range(WIDTH-2):
                w = exponents[j+2]-exponents[j]
                pair_counts[w] += 1
                if w == 2:
                    assert resources[j] == 0, ('reset_before', family, seed, j)
                    assert resources[j+2]+1 == periods[j+2]//2
                if w == 1:
                    assert resources[j] <= resources[j+2]+1, ('countdown', family, seed, j)
            for a in range(WIDTH):
                for n in range(WIDTH-a):
                    m = n//2
                    assert exponents[a+n]-exponents[a] <= (n+1)//2+qbound(exponents[a], m)
                    windows += 1
            records.append({'family': family, 'seed': seed, 'E': exponents,
                            'resources': resources, 'cycle': len(states)})

    # Period-one correction: the uncorrected OR reversal criterion is false.
    assert literal(0, families[6]) == 0
    assert (literal(2, families[6]) >> 2) & 1 == 1
    assert (2 & 1) == 0

    # Known singleton-support AND domino control, with a direct binomial oracle.
    import math
    o = [0, 0]
    for j in range(2, 16):
        o.append(1+(o[-1] | o[-2]))
    for j in range(3, 16):
        q, r = divmod(j, 3)
        u = sum(((q >> k) & 1) << (2*k) for k in range(q.bit_length()))
        v = (q & -q).bit_length()-1
        closed = (6*u-(1 << (2*v+2)), 6*u-(1 << (2*v+1)), 6*u+1)[r]
        assert closed == o[j], ('domino_closed', j)
    x = 3
    for t in range(64):
        for j in range(16):
            assert ((x >> j) & 1) == (math.comb(t, o[j]) & 1 if t >= o[j] else 0)
        x ^= (x << 1) & (x << 2)
        x &= (1 << 16)-1
    result = {'status': 'PASS', 'families': len(families), 'cases': len(records),
              'pair_weights_0_1_2': pair_counts, 'windows': windows,
              'domino_cell_checks': 16*64, 'period_one_mutant_rejected': True,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'cpu_s': time.process_time()-start, 'records': records}
    out = Path(os.environ['CAPPED_OUT']) / 'control.json'
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'records'}))


if __name__ == '__main__':
    main()
