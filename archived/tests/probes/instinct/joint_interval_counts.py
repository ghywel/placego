#!/usr/bin/env python3
"""MI439/B230: seven FIXED count-compatibility fixtures, then reflections.

Predictions and stop rules are committed in GPT-MATH-INSTINCT.md MI439.
No census, sampling, retries, or claim that count admission suffices.
Independent row/column matrix enumeration and formula/literal rank bounds;
independent subset recursion/owner recursion for exact partitions.
10 CPU seconds,20 wall seconds,1,000,000 recursive nodes TOTAL.
Raw JSON goes to stdout, retained outside git. First failure stops.
"""
import itertools
import json
import time


START = time.monotonic()
CPU = time.process_time()
NODES = 0
ROWS = []


class Cap(Exception):
    pass


def tick():
    global NODES
    NODES += 1
    if NODES > 1_000_000 or time.process_time() - CPU > 10 or time.monotonic() - START > 20:
        raise Cap("registered aggregate cap")


def need(condition, message):
    if not condition:
        raise AssertionError(message)


def intervals(pool):
    out = []
    for x in pool:
        if out and x == out[-1][-1] + 1:
            out[-1].append(x)
        else:
            out.append([x])
    return tuple(tuple(a) for a in out)


def compositions(total, caps):
    tick()
    if not caps:
        if total == 0:
            yield ()
        return
    for n in range(max(0, total - sum(caps[1:])), min(total, caps[0]) + 1):
        for tail in compositions(total - n, caps[1:]):
            yield (n,) + tail


def row_matrices(sizes, lengths):
    tick()
    if not sizes:
        if not any(lengths):
            yield ()
        return
    for row in compositions(sizes[0], lengths):
        rest = tuple(a - b for a, b in zip(lengths, row))
        for tail in row_matrices(sizes[1:], rest):
            yield (row,) + tail


def column_matrices(sizes, lengths):
    # Cartesian choices for each interval, then filter row totals. This
    # deliberately does not reuse the recursive row-conservation engine.
    choices = []
    for length in lengths:
        candidates = []
        for column in itertools.product(*(range(c + 1) for c in sizes)):
            tick()
            if sum(column) == length:
                candidates.append(column)
        choices.append(candidates)
    for columns in itertools.product(*choices):
        tick()
        matrix = tuple(tuple(col[i] for col in columns) for i in range(len(sizes)))
        if tuple(map(sum, matrix)) == sizes:
            yield matrix


def formula_ok(matrix, runs, targets):
    for mask in range(1, (1 << len(targets)) - 1):
        tick()
        low = high = target = 0
        for i, value in enumerate(targets):
            if mask >> i & 1:
                target += value
        for j, run in enumerate(runs):
            c = sum(row[j] for i, row in enumerate(matrix) if mask >> i & 1)
            low += run[0] * c + c * (c - 1) // 2
            high += run[-1] * c - c * (c - 1) // 2
        if not low <= target <= high:
            return False
    return True


def literal_ok(matrix, runs, targets):
    for width in range(1, len(targets)):
        for bins in itertools.combinations(range(len(targets)), width):
            tick()
            counts = [sum(matrix[i][j] for i in bins) for j in range(len(runs))]
            lo = sum(sum(run[:c]) for run, c in zip(runs, counts))
            hi = sum(sum(run[len(run) - c:]) for run, c in zip(runs, counts))
            if not lo <= sum(targets[i] for i in bins) <= hi:
                return False
    return True


def subset_partition(pool, sizes, targets):
    tick()
    if not sizes:
        return () if not pool else None
    if len(sizes) == 1:
        return (pool,) if len(pool) == sizes[0] and sum(pool) == targets[0] else None
    for chosen in itertools.combinations(pool, sizes[0]):
        tick()
        if sum(chosen) != targets[0]:
            continue
        chosen_set = set(chosen)
        remaining = tuple(x for x in pool if x not in chosen_set)
        tail = subset_partition(remaining, sizes[1:], targets[1:])
        if tail is not None:
            return (chosen,) + tail
    return None


def owner_partition(pool, sizes, targets):
    parts = [[] for _ in sizes]
    sums = [0] * len(sizes)

    def visit(at):
        tick()
        if at == len(pool):
            if tuple(sums) == targets and tuple(map(len, parts)) == sizes:
                return tuple(tuple(p) for p in parts)
            return None
        remaining = pool[at:]
        for i, size in enumerate(sizes):
            count = size - len(parts[i])
            if count > len(remaining):
                return None
            lo = sum(remaining[:count])
            hi = sum(remaining[len(remaining) - count:])
            if not sums[i] + lo <= targets[i] <= sums[i] + hi:
                return None
        for i, size in enumerate(sizes):
            if len(parts[i]) < size:
                parts[i].append(pool[at])
                sums[i] += pool[at]
                result = visit(at + 1)
                sums[i] -= pool[at]
                parts[i].pop()
                if result is not None:
                    return result
        return None

    return visit(0)


def validate(witness, pool, sizes, targets):
    need(tuple(sorted(x for part in witness for x in part)) == pool, "literal union")
    need(tuple(map(len, witness)) == sizes, "literal sizes")
    need(tuple(map(sum, witness)) == targets, "literal sums")


def witness_matrix(witness, runs):
    return tuple(tuple(sum(x in run for x in part) for run in runs) for part in witness)


def fixture(label, pool, sizes, targets, expect_admit, expect_partition, supplied=None):
    runs = intervals(pool)
    lengths = tuple(map(len, runs))
    need(len(pool) == sum(sizes) and sum(pool) == sum(targets), "fixture total")
    matrices_a = set(row_matrices(sizes, lengths))
    matrices_b = set(column_matrices(sizes, lengths))
    need(matrices_a == matrices_b, "whole transportation-matrix maps disagree")
    admitted_a = {m for m in matrices_a if formula_ok(m, runs, targets)}
    admitted_b = {m for m in matrices_b if literal_ok(m, runs, targets)}
    need(admitted_a == admitted_b, "whole admitted-matrix maps disagree")
    first = subset_partition(pool, sizes, targets)
    second = owner_partition(pool, sizes, targets)
    need((first is None) == (second is None), "partition oracles disagree")
    for witness in (first, second, supplied):
        if witness is not None:
            validate(witness, pool, sizes, targets)
            need(witness_matrix(witness, runs) in admitted_a, "positive lost by necessary condition")
    row = dict(label=label, pool=pool, sizes=sizes, targets=targets,
               matrices=len(matrices_a), admitted=len(admitted_a),
               partition=first, supplied=supplied, nodes_so_far=NODES)
    ROWS.append(row)
    need(bool(admitted_a) == expect_admit, "admission prediction: " + label)
    need((first is not None) == expect_partition, "partition prediction: " + label)
    return admitted_a


def main():
    fixtures = [
        ("cloud_three", tuple(x for x in range(12) if x not in (4, 5, 6)), (3, 3, 3), (17, 17, 17), False, False, None),
        ("cloud_four", tuple(x for x in range(15) if x not in (6, 7, 8)), (3, 3, 3, 3), (21, 21, 21, 21), False, False, None),
        ("bad_child", tuple(x for x in range(11) if x not in (4, 6)), (3, 3, 3), (7, 15, 23), False, False, None),
        ("parent_q4", tuple(x for x in range(13) if x != 4), (3, 3, 3, 3), (29, 23, 15, 7), True, True,
         ((7, 10, 12), (3, 9, 11), (1, 6, 8), (0, 2, 5))),
        ("parent_q6", tuple(x for x in range(13) if x != 6), (3, 3, 3, 3), (27, 23, 15, 7), True, True,
         ((5, 10, 12), (3, 9, 11), (0, 7, 8), (1, 2, 4))),
        ("positive_rows", (0, 1, 2, 10, 11, 12), (2, 2, 2), (12, 12, 12), True, True,
         ((0, 12), (1, 11), (2, 10))),
        ("not_sufficient", (0, 1, 2, 3), (1, 1, 1, 1), (1, 1, 2, 2), True, False, None),
    ]
    for args in fixtures:
        admitted = fixture(*args)
        label, pool, sizes, targets, ea, ep, supplied = args
        top = max(pool)
        mirrored = tuple(sorted(top - x for x in pool))
        new_targets = tuple(top * c - u for c, u in zip(sizes, targets))
        new_supplied = None if supplied is None else tuple(tuple(sorted(top - x for x in part)) for part in supplied)
        other = fixture(label + "_reflected", mirrored, sizes, new_targets, ea, ep, new_supplied)
        expected = {tuple(tuple(reversed(row)) for row in m) for m in admitted}
        need(other == expected, "whole reflection matrix map")


if __name__ == "__main__":
    status, error = "PASS", None
    try:
        main()
    except Cap as exc:
        status, error = "CAPPED", str(exc)
    except Exception as exc:
        status, error = "FAILED", repr(exc)
    print(json.dumps(dict(status=status, error=error, rows=ROWS, nodes=NODES,
                         cpu_seconds=time.process_time() - CPU,
                         wall_seconds=time.monotonic() - START), indent=2))
    raise SystemExit(0 if status == "PASS" else 1)
