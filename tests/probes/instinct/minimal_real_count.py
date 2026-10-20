"""MI567: one fixed minimal-domain count-admission diagnostic, not partitions.

Domain M12, counts3333, EVERY internal q1..11, sorted integer targets
with conservation and all proper baseline group cuts. No M13 extension.
Prediction: every such count region is REAL feasible and integer feasible.
Can fail: first real-empty target refutes real count admission HERE;
real-feasible/integer-empty target challenges G334 or the implementation.
Stop at first failure, mismatch, cap, or completed domain. No retry.
Engine A: analytic scalar intervals and exact doubled-coordinate projection.
Engine B: actual scalar subsets and independent integer count enumeration.
Controls: three protected literal positives; size2 real/integer gap;
size2 real-empty shortage. The gap must remain, not be 'fixed' by the test.
Unexpected: both q5 and q7 retained, since protection is not reflection
invariant. All11 holes are tested separately. No physical partition claim.
Caps:45568 scalar masks;25000 canonical targets;15CPU seconds.
Standard library; raw JSON stays outside git. Known elimination, MI558.
"""
import itertools
import json
import time


T = lambda n: n * (n + 1) // 2
L = lambda n: n * (n - 1) // 2
MASKS = tuple(range(1, 15))


def main():
    start = time.process_time()
    scalar_masks = cases = scalar_comparisons = 0
    cache = {}

    def limits():
        assert scalar_masks <= 45568
        assert cases <= 25000
        assert time.process_time() - start < 15

    def oracle(M, q):
        nonlocal scalar_masks
        if (M, q) in cache:
            return cache[M, q]
        pool = tuple(v for v in range(M + 1) if v != q)
        out = {}
        for mask in range(1 << len(pool)):
            picked = [v for j, v in enumerate(pool) if mask & (1 << j)]
            key = len(picked), sum(picked)
            out.setdefault(key, set()).add(sum(v > q for v in picked))
            scalar_masks += 1
        limits()
        cache[M, q] = out
        return out

    def analytic(M, q, c, t):
        H = M - q
        ks = []
        for k in range(max(0, c - q), min(c, H) + 1):
            lo = L(c - k) + (q + 1) * k + L(k)
            hi = (c - k) * (q - 1) - L(c - k) + M * k - L(k)
            if lo <= t <= hi:
                ks.append(k)
        return (min(ks), max(ks)) if ks else None

    def real_projection(H, intervals):
        if any(v is None for v in intervals.values()):
            return False, None
        A, B = zip(*(intervals[1 << i] for i in range(4)))
        P, Q = zip(*(intervals[1 | (1 << j)] for j in range(1, 4)))
        for j in range(3):
            other = [h for h in range(3) if h != j]
            if not (P[j] + sum(A[h + 1] for h in other) <= H
                    <= Q[j] + sum(B[h + 1] for h in other)):
                return False, None
        lows = [2 * A[0], 2 * (H - sum(B[1:])), sum(P) - H]
        highs = [2 * B[0], 2 * (H - sum(A[1:])), sum(Q) - H]
        for j in range(3):
            lows.append(2 * (P[j] - B[j + 1]))
            highs.append(2 * (Q[j] - A[j + 1]))
        for j, h in itertools.combinations(range(3), 2):
            l = 3 - j - h
            lows.append(2 * (P[j] + P[h] + A[l + 1] - H))
            highs.append(2 * (Q[j] + Q[h] + B[l + 1] - H))
        bounds = max(lows), min(highs)
        return bounds[0] <= bounds[1], bounds

    def evaluate(M, q, cs, ts):
        nonlocal scalar_comparisons
        assert sum(cs) == M and sum(ts) == T(M) - q
        support = oracle(M, q)
        group_sizes = {m: sum(cs[i] for i in range(4) if m >> i & 1)
                       for m in MASKS}
        group_sums = {m: sum(ts[i] for i in range(4) if m >> i & 1)
                      for m in MASKS}
        intervals = {}
        for m in MASKS:
            c, t = group_sizes[m], group_sums[m]
            a = analytic(M, q, c, t)
            ks = support.get((c, t), set())
            b = (min(ks), max(ks)) if ks else None
            assert a == b, (M, q, cs, ts, m, a, b)
            if ks:
                assert ks == set(range(b[0], b[1] + 1))
            intervals[m] = a
            scalar_comparisons += 1
        for m in MASKS:
            if intervals[m] is not None:
                lo, hi = intervals[m]
                assert intervals[15 ^ m] == (M - q - hi, M - q - lo)
        real, projection = real_projection(M - q, intervals)
        witness = None
        for v in itertools.product(*(range(c + 1) for c in cs)):
            if sum(v) != M - q:
                continue
            if all(sum(v[i] for i in range(4) if m >> i & 1)
                   in support.get((group_sizes[m], group_sums[m]), set())
                   for m in MASKS):
                witness = v
                break
        limits()
        return real, witness, projection

    controls = [
        (12, 1, (3,) * 4, (6, 21, 24, 26), True, True),
        (12, 7, (3,) * 4, (6, 16, 24, 25), True, True),
        (12, 5, (3,) * 4, (25, 25, 10, 13), True, True),
        (8, 4, (2,) * 4, (5, 5, 11, 11), True, False),
        (8, 5, (2,) * 4, (11, 11, 4, 5), False, False),
    ]
    control_output = []
    for M, q, cs, ts, expected_real, expected_integer in controls:
        a, w, p = evaluate(M, q, cs, ts)
        assert (a, w is not None) == (expected_real, expected_integer)
        if a and w is None:
            assert p[0] == p[1] and p[0] % 2 == 1
        control_output.append(dict(M=M, q=q, real=a, integer=w is not None))

    by_hole = {}
    cs = (3,) * 4
    for q in range(1, 12):
        S = T(12) - q
        count = 0
        for first in itertools.combinations_with_replacement(range(6, S - 44), 3):
            ts = first + (S - sum(first),)
            if not first[-1] <= ts[-1] <= S - 45:
                continue
            if not all(sum(ts[i] for i in range(4) if m >> i & 1)
                       >= T(3 * m.bit_count()) for m in MASKS):
                continue
            cases += 1
            count += 1
            a, w, p = evaluate(12, q, cs, ts)
            if not a or w is None:
                print(json.dumps(dict(verdict="first_failure", q=q, targets=ts,
                                      real=a, witness=w, projection=p,
                                      cases=cases, scalar_masks=scalar_masks)))
                return
        by_hole[q] = count
    assert scalar_masks == 45568
    print(json.dumps(dict(verdict="completed", M=12, counts=cs, holes=11,
                          cases=cases, by_hole=by_hole, scalar_masks=scalar_masks,
                          scalar_comparisons=scalar_comparisons,
                          controls=control_output, cpu_seconds=time.process_time()-start),
                     sort_keys=True))


if __name__ == "__main__":
    main()
