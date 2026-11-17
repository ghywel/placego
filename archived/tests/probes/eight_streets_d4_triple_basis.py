#!/usr/bin/env python3
"""MI613 frozen exact basis; ONE bounded run, not an A2 census.

Prediction: all 6423 endpoint-normalized pools, span 7..16, <=4 holes,
at least 8 retained values, omit triple sums only at actual depth <=5.
Record searched: 6423|finite triple; rank.gap; anchored.pair (MI613).
Prior-art/interface: FOUR38--40; elementary pairing and cardinality DP.
Complete literal triple spectra vs independent cardinality bitset DP;
independent weak-composition domain, literal retained witnesses, reflection,
translation and a physically lifted t5 join. The n7 negative MUST fail.
Caps: 20 CPU seconds, 25 internal/30 external wall seconds, 128 MiB RSS,
64 KiB receipt. Stop first confirmed counterexample/control failure/cap.
No retries, source changes or scope widening after execution begins.
OUTCOME MI614: COMPLETE6423 pools, all controls PASS, depth bound5.
Executed source is dfbaf525, SHA256 recorded MI613; only this receipt added.
Universal cutoff remains HAND G341.
"""
import hashlib
import itertools
import json
import math
import resource
import signal
import sys
import time


class InstrumentFailure(Exception):
    pass


class Counterexample(Exception):
    pass


def require(test, detail):
    if not test:
        raise InstrumentFailure(detail)


def dp(pool):
    rows = [1, 0, 0, 0]
    for value in pool:
        for size in (3, 2, 1):
            rows[size] |= rows[size - 1] << value
    return rows[3]


def literal(pool):
    witnesses = {}
    for triple in itertools.combinations(pool, 3):
        witnesses.setdefault(sum(triple), triple)
    mask = sum(1 << target for target in witnesses)
    for target, triple in witnesses.items():
        require(len(set(triple)) == 3 and set(triple) <= set(pool)
                and sum(triple) == target, ['bad witness', pool, target, triple])
    return mask, witnesses


def sums(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def compositions(total, slots):
    if slots == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, slots - 1):
                yield (first,) + rest


def rss_bytes():
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return raw if sys.platform == 'darwin' else raw * 1024


def controls():
    negative = (0, 1, 2, 7, 8, 9, 10)
    mask, _ = literal(negative)
    require(mask == dp(negative), 'negative engines disagree')
    require(not (mask >> 14) & 1 and min(14 - sum(negative[:3]),
            sum(negative[-3:]) - 14) == 11, 'n7 negative not detected')
    # The two consecutive sliding windows, with their ACTUAL fixed tokens.
    pool = tuple(range(9)) + (12,)
    fixed0, middle0 = (0, 1), tuple(range(2, 9)) + (12,)
    fixed1, middle1 = (0, 12), tuple(range(1, 9))
    intervals = []
    for fixed, middle in ((fixed0, middle0), (fixed1, middle1)):
        mask, _ = literal(middle)
        require(mask == dp(middle), 'join engines disagree')
        low, high = sum(middle[:3]) + 6, sum(middle[-3:]) - 6
        require(all((mask >> s) & 1 for s in range(low, high + 1)),
                'join triple interval has hole')
        intervals.append((sum(fixed) + low, sum(fixed) + high))
    require(intervals == [(16, 22), (24, 27)], ['join endpoints', intervals])
    selected = fixed0 + (2, 8, 12)
    require(len(set(selected)) == 5 and set(selected) <= set(pool)
            and sum(selected) == 23, 'join physical lift')
    require(sum(set(pool) - set(selected)) == 25, 'join complement')
    for transform in (lambda x: x + 7, lambda x: 12 - x):
        p = {transform(x) for x in pool}
        a = {transform(x) for x in selected}
        require(len(a) == 5 and a <= p and len(p - a) == 5,
                'transformed physical lift')
        require(sum(a) + sum(p - a) == sum(p), 'transformed conservation')
    return {'n7_missing': 14, 'n7_depth': 11, 'join_sum': 23,
            'join_intervals': intervals, 'join_complement_sum': 25}


def main():
    control = controls()
    domains = {}
    per_span = []
    digest = hashlib.sha256()
    witness_count = 0
    worst = -1
    worst_example = None
    for span in range(7, 17):
        count = 0
        for hole_count in range(min(4, span - 7) + 1):
            for holes in itertools.combinations(range(1, span), hole_count):
                pool = tuple(x for x in range(span + 1) if x not in holes)
                mask, witnesses = literal(pool)
                require(mask == dp(pool), ['complete spectra mismatch', pool])
                alpha, beta = sum(pool[:3]), sum(pool[-3:])
                for target in range(alpha, beta + 1):
                    if not (mask >> target) & 1:
                        depth = min(target - alpha, beta - target)
                        if depth > worst:
                            worst, worst_example = depth, [pool, target]
                        if depth > 5:
                            # Literal and DP independently confirm the same omission.
                            raise Counterexample([pool, target, alpha, beta, depth])
                reflected = tuple(sorted(span - x for x in pool))
                expected_reflection = sum(1 << (3 * span - s) for s in sums(mask))
                require(dp(reflected) == expected_reflection, ['reflection', pool])
                translated = tuple(x + 7 for x in pool)
                require(dp(translated) == mask << 21, ['translation', pool])
                for target, witness in witnesses.items():
                    require(sum(x + 7 for x in witness) == target + 21
                            and sum(span - x for x in witness) == 3 * span - target,
                            'transformed witness sum')
                require(pool not in domains, 'duplicate primary pool')
                domains[pool] = mask
                digest.update((json.dumps([pool, sorted(witnesses)],
                               separators=(',', ':')) + '\n').encode())
                witness_count += len(witnesses)
                count += 1
                require(rss_bytes() <= 128 * 1024**2, 'RSS cap')
        expected = sum(math.comb(span - 1, h) for h in range(min(4, span - 7) + 1))
        require(count == expected, ['binomial count', span, count, expected])
        per_span.append(count)
    require(per_span == [1, 8, 37, 130, 386, 562, 794, 1093, 1471, 1941]
            and len(domains) == 6423, ['domain total', per_span, len(domains)])
    # Independent domain: available-rank gaps, no deletion combinations.
    secondary = 0
    for size in range(8, 18):
        for holes in range(5):
            if not 7 <= size - 1 + holes <= 16:
                continue
            for gaps in compositions(holes, size - 1):
                pool = [0]
                for extra in gaps:
                    pool.append(pool[-1] + 1 + extra)
                pool = tuple(pool)
                require(pool in domains, ['secondary unexpected/duplicate', pool])
                require(dp(pool) == domains.pop(pool), ['secondary spectrum', pool])
                secondary += 1
    require(not domains and secondary == 6423, ['secondary coverage', len(domains), secondary])
    return {'verdict': 'COMPLETE', 'pools': secondary, 'per_span': per_span,
            'complete_spectrum_sha256': digest.hexdigest(),
            'retained_witnesses': witness_count, 'worst_missing_depth': worst,
            'worst_example': worst_example, 'controls': control}


if __name__ == '__main__':
    wall, cpu = time.monotonic(), time.process_time()
    resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('wall cap')))
    signal.alarm(25)
    try:
        result = main()
    except Counterexample as exc:
        result = {'verdict': 'REFUTED', 'counterexample': exc.args}
    except (InstrumentFailure, TimeoutError) as exc:
        result = {'verdict': 'INSTRUMENT-FAILED' if isinstance(exc, InstrumentFailure)
                  else 'UNKNOWN', 'reason': exc.args}
    result.update(cpu_seconds=time.process_time() - cpu,
                  wall_seconds=time.monotonic() - wall, peak_rss_bytes=rss_bytes())
    output = json.dumps(result, sort_keys=True)
    require(len(output.encode()) < 65536, 'output cap')
    print(output, flush=True)
    sys.exit(0 if result['verdict'] == 'COMPLETE' else 1)
