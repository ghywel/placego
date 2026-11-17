#!/usr/bin/env python3
"""MI443/B232: ONE minimal one-sided count pattern, not a census.

Predictions/controls/stop rules: GPT-MATH-INSTINCT.md MI443, published
before this source. Labelled copies 0..5, counts (3,1,1,1)/(0,2,2,2).
Blind prediction: the complete integer rank-target set is attainable.
Independent row-combination and whole-token-owner engines; full sets,
literal witnesses, reflection, translation, positive and negative controls.
The negative control uses the explicitly different MI441 count pattern.
One invocation; 10 CPU / 20 wall seconds / 1,000,000 checked states.
First failed control or negative stops. Raw output remains outside git.
"""
import hashlib
import itertools
import json
import time

START = time.monotonic()
CPU = time.process_time()
NODES = 0
OUT = {"status": "RUNNING", "controls": []}


class Stop(Exception):
    pass


def tick():
    global NODES
    NODES += 1
    if NODES > 1_000_000 or time.process_time() - CPU > 10 or time.monotonic() - START > 20:
        OUT["status"] = "CAPPED"
        raise Stop("registered aggregate cap")


def need(ok, message):
    if not ok:
        OUT["status"] = "CONTROL_FAILURE"
        raise Stop(message)


def row_allocations(tokens, counts):
    tick()
    if not counts:
        if not tokens:
            yield ()
        return
    for selected in itertools.combinations(tokens, counts[0]):
        rest = tuple(x for x in tokens if x not in selected)
        for tail in row_allocations(rest, counts[1:]):
            yield (selected,) + tail


def row_engine(counts):
    left = list(row_allocations(tuple(range(6)), counts[0]))
    right = list(row_allocations(tuple(range(6)), counts[1]))
    out = {}
    for lo, hi in itertools.product(left, right):
        tick()
        sums = tuple(sum(lo[i]) + sum(hi[i]) for i in range(4))
        out.setdefault(sums, (lo, hi))
    return out, (len(left), len(right))


def owner_engine(counts):
    # Assign each labelled token to a bin; no subset-generation helper.
    remaining = [list(row) for row in counts]
    sums = [0] * 4
    out = set()
    leaves = 0

    def visit(t):
        nonlocal leaves
        tick()
        if t == 12:
            need(not any(remaining[0] + remaining[1]), "owner counts at leaf")
            out.add(tuple(sums))
            leaves += 1
            return
        row, value = divmod(t, 6)
        for owner in range(4):
            if remaining[row][owner]:
                remaining[row][owner] -= 1
                sums[owner] += value
                visit(t + 1)
                sums[owner] -= value
                remaining[row][owner] += 1

    visit(0)
    return out, leaves


def rank_formula(v, counts):
    if sum(v) != 30:
        return False
    for mask in range(1, 15):
        tick()
        lo = hi = 0
        for row in counts:
            n = sum(row[i] for i in range(4) if mask >> i & 1)
            lo += n * (n - 1) // 2
            hi += 5 * n - n * (n - 1) // 2
        value = sum(v[i] for i in range(4) if mask >> i & 1)
        if not lo <= value <= hi:
            return False
    return True


def rank_literal(v, counts):
    if sum(v) != 30:
        return False
    for width in range(1, 4):
        for group in itertools.combinations(range(4), width):
            tick()
            lo = hi = 0
            for row in counts:
                n = sum(row[i] for i in group)
                lo += sum(list(range(6))[:n])
                hi += sum(list(range(6))[6-n:])
            if not lo <= sum(v[i] for i in group) <= hi:
                return False
    return True


def validate(v, witness, counts):
    tick()
    for row, sizes in zip(witness, counts):
        need(tuple(map(len, row)) == sizes, "witness counts")
        need(sorted(x for group in row for x in group) == list(range(6)), "witness row cover")
    need(tuple(sum(witness[0][i]) + sum(witness[1][i]) for i in range(4)) == v,
         "witness sums")
    physical = [tuple(witness[0][i]) + tuple(x + 7 for x in witness[1][i]) for i in range(4)]
    need(sorted(x for group in physical for x in group) == [x for x in range(13) if x != 6],
         "translated pool cover")
    need(tuple(map(sum, physical)) == tuple(v[i] + 7 * counts[1][i] for i in range(4)),
         "translated sums")


def digest(values):
    return hashlib.sha256(json.dumps(sorted(values), separators=(",", ":")).encode()).hexdigest()


def checked_maps(counts, expected_counts):
    actual, sizes = row_engine(counts)
    other, leaves = owner_engine(counts)
    need(sizes == expected_counts, "row assignment counts")
    need(leaves == sizes[0] * sizes[1], "owner leaf count")
    need(set(actual) == other, "complete target maps disagree")
    for v, witness in actual.items():
        validate(v, witness, counts)
        need(rank_formula(v, counts) and rank_literal(v, counts), "actual target fails necessary bounds")
        reflected = tuple(5 * (counts[0][i] + counts[1][i]) - v[i] for i in range(4))
        need(reflected in actual, "actual whole-map reflection")
        rw = tuple(tuple(tuple(5-x for x in group) for group in row) for row in witness)
        validate(reflected, rw, counts)
    return actual, {"row_assignments": sizes, "owner_leaves": leaves,
                    "distinct_targets": len(actual), "target_sha256": digest(actual)}


def main():
    # Run the registered negative control before the blind comparison.
    nc = ((3, 1, 2, 0), (0, 2, 1, 3))
    negative, info = checked_maps(nc, (60, 60))
    v = (4, 4, 11, 11)
    need(rank_formula(v, nc) and rank_literal(v, nc), "negative rank admission")
    need(v not in negative, "negative wrongly attained")
    for target, hi in [((4, 3, 12, 11), ((), (0, 1), (3,), (2, 4, 5))),
                       ((4, 5, 10, 11), ((), (0, 3), (1,), (2, 4, 5)))]:
        witness = (((0, 1, 3), (2,), (4, 5), ()), hi)
        validate(target, witness, nc)
        need(target in negative, "midpoint endpoint absent")
    OUT["negative_control"] = info
    OUT["controls"].append("negative admission/nonexistence and two midpoint endpoints")

    counts = ((3, 1, 1, 1), (0, 2, 2, 2))
    actual, info = checked_maps(counts, (120, 90))
    supplied = (((0, 1, 2), (3,), (4,), (5,)), ((), (0, 5), (1, 4), (2, 3)))
    validate((3, 8, 9, 10), supplied, counts)
    need((3, 8, 9, 10) in actual, "positive control absent")
    OUT["primary"] = info
    OUT["controls"].append("independent complete actual maps; all witnesses/reflections/translations; positive")
    rank = set()
    tested = 0
    for a, b, c in itertools.product(range(3, 13), range(1, 15), range(1, 15)):
        tick()
        v = (a, b, c, 30-a-b-c)
        tested += 1
        formula, literal = rank_formula(v, counts), rank_literal(v, counts)
        need(formula == literal, "rank engines disagree")
        if formula:
            rank.add(v)
            if v not in actual:
                OUT.update(status="PREDICTION_REFUTED", first_negative=v,
                           rank_candidates_tested=tested, admitted_before_stop=len(rank))
                raise Stop("first rank-admitted unattainable target; no continuation")
    need(rank == set(actual), "rank/actual map mismatch beyond blind comparison")
    need({tuple(15-x for x in v) for v in rank} == rank, "rank whole-map reflection")
    OUT.update(status="PASS", rank_candidates_tested=tested, rank_targets=len(rank),
               rank_sha256=digest(rank), witnesses=[{"target": v, "rows": actual[v]} for v in sorted(actual)])
    OUT["controls"].append("complete rank map; formula/literal bounds; rank reflection")


if __name__ == "__main__":
    try:
        main()
    except Stop as error:
        OUT["error"] = str(error)
    except Exception as error:
        OUT.update(status="INSTRUMENT_ERROR", error=repr(error))
    OUT.update(nodes=NODES, cpu_seconds=time.process_time()-CPU, wall_seconds=time.monotonic()-START)
    print(json.dumps(OUT, indent=2))
    raise SystemExit(0 if OUT["status"] == "PASS" else 1)
