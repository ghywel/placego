"""MI561: one fixed balanced-cover threshold diagnostic, not a target census.

Fixed S=[0,12] minus6; counts3333; H6; groups34/124/13/2,
group sizes6/9/6/3. Test a sufficient RELAXATION for their upper-count
sum>=12: whenever endpoint budgets r total<=11, their separate protected
moment ceilings should total<2*sum(S)=144. A failure refutes this relaxed
proof mechanism, not the protected-parent conjecture. No domain extension.

Prediction: maximum ceiling total<144. Counterfactual: >=144 stops the
method here; no after-the-fact target-compatibility filtering in this run.
Engine A uses the row-minimum quadratic and direct budget products.
Engine B enumerates all4096 actual token subsets for scalar high-count
support, then independently maximizes ceilings by budget dynamic programming.
Controls: literal protected parent, known merged-fibre incompatibility,
and an empty count option r1 for size6 (unexpected rounded boundary).
Caps: exactly4096 subset masks, <=2401 direct endpoint allocations,
5CPU seconds, no rerun/enlargement. Standard library only; raw JSON outside git.
"""
import itertools
import json
import time


def main():
    start = time.process_time()
    M, q, H = 12, 6, 6
    pool = tuple(x for x in range(M + 1) if x != q)
    total = sum(pool)
    sizes = (6, 9, 6, 3)
    L = lambda n: n * (n - 1) // 2
    T = lambda n: n * (n + 1) // 2

    def ceiling_a(c, r):
        cap = min(c, H)
        if not max(0, c - q) <= r <= cap:
            return None
        upper = total - T(M - c)
        if r < cap:
            k = r + 1
            upper = min(upper, L(c - k) + (q + 1) * k + L(k) - 1)
        return upper if upper >= T(c) else None

    # Entirely separate scalar oracle: each actual subset gives a sum
    # and its number of high tokens. Store the maximum count at that sum.
    support = {}
    for mask in range(1 << len(pool)):
        chosen = [x for j, x in enumerate(pool) if mask & (1 << j)]
        c, t = len(chosen), sum(chosen)
        key = c, t
        support[key] = max(support.get(key, -1), sum(x > q for x in chosen))

    def ceiling_b(c, r):
        allowed = [t for t in range(T(c), total - T(M - c) + 1)
                   if (c, t) in support and support[c, t] <= r]
        return max(allowed) if allowed else None

    tables = []
    comparisons = 0
    for c in sizes:
        row = {}
        for r in range(max(0, c - q), min(c, H) + 1):
            a, b = ceiling_a(c, r), ceiling_b(c, r)
            comparisons += 1
            assert a == b, (c, r, a, b)
            if a is not None:
                row[r] = a
        tables.append(row)
    assert ceiling_a(6, 1) is None and ceiling_b(6, 1) is None

    checked = 0
    scores = []
    for rs in itertools.product(*(tuple(row) for row in tables)):
        assert checked < 2401
        if sum(rs) > 2 * H - 1:
            continue
        checked += 1
        scores.append((sum(row[r] for row, r in zip(tables, rs)), rs))
    assert scores
    best = max(value for value, _ in scores)
    maximizers = sorted(rs for value, rs in scores if value == best)

    dp = {0: 0}
    for row in tables:
        nxt = {}
        for spent, value in dp.items():
            for r, ceiling in row.items():
                if spent + r <= 2 * H - 1:
                    nxt[spent + r] = max(nxt.get(spent + r, -1), value + ceiling)
        dp = nxt
    assert best == max(dp.values())

    bins = ({0, 1, 5}, {2, 7, 12}, {3, 8, 10}, {4, 9, 11})
    assert sorted(x for block in bins for x in block) == list(pool)
    assert [sum(block) for block in bins] == [6, 21, 21, 24]
    groups = ((2, 3), (0, 1, 3), (0, 2), (1,))
    endpoints = [support[3 * len(J), sum(sum(bins[i]) for i in J)] for J in groups]
    assert sum(endpoints) >= 2 * H
    # Known actual incompatibility: the merged count3 is not inherited
    # by the two child fibres; the independent scalar oracle must retain it.
    assert support[6, 27] == 3
    assert support[3, 6] + support[3, 21] == 2
    elapsed = time.process_time() - start
    assert elapsed < 5, elapsed
    print(json.dumps(dict(fixture=dict(M=M, q=q, counts=[3] * 4, sizes=sizes),
                          subset_masks=1 << len(pool), scalar_comparisons=comparisons,
                          deficit_allocations=checked, tables=tables,
                          maximum=best, required=2 * total, maximizers=maximizers,
                          independent_budget_dp=dp, literal_parent_upper_counts=endpoints,
                          mechanism_pass=(best < 2 * total), controls=3,
                          cpu_seconds=elapsed), sort_keys=True))


if __name__ == '__main__':
    main()
