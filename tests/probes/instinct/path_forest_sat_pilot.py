#!/usr/bin/env python3
"""B129/MI279: one capped reusable Boolean weighted-sum pilot.

No subset catalogue, anchors, prescribed bin sizes, old witness seeds or
target-specific retained constraints. Cadical195 learns under assumptions.
Primary writes literal partitions and per-call cumulative-stat differences.
Run only through path_forest_sat_check.py after preregistration is pushed.
"""
from itertools import product
from pathlib import Path
import json
import resource
import sys
import time

from pysat.solvers import Cadical195

START = time.process_time()
WALL = time.monotonic()
QUERY_CONFLICTS = 50000
TOTAL_CONFLICTS = 500000


def rss():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r if sys.platform == 'darwin' else r * 1024


def budget():
    if time.process_time() - START > 20 or time.monotonic() - WALL > 40:
        raise RuntimeError('primary CPU/wall cap')
    if rss() > 256 * 1024 * 1024:
        raise RuntimeError('primary RSS cap')


class Model:
    def __init__(self, m, bins):
        self.m, self.k = m, bins
        self.nv = 1
        self.cnf = [[1]]
        self.zero = -1
        self.x = [[self.var() for _ in range(bins)] for _ in range(m)]
        for row in self.x:
            self.cnf.append(row[:])
            for i in range(bins):
                for j in range(i):
                    self.cnf.append([-row[i], -row[j]])
        self.width = (m * m).bit_length()
        self.out = []
        for b in range(bins):
            acc = [self.zero] * self.width
            for j in range(m):
                odd = 2 * j + 1
                word = [self.x[j][b] if (odd >> bit) & 1 else self.zero
                        for bit in range(self.width)]
                carry, result = self.zero, []
                for a, c in zip(acc, word):
                    pair = self.xor(a, c)
                    result.append(self.xor(pair, carry))
                    carry = self.either(self.both(a, c), self.both(pair, carry))
                self.cnf.append([-carry])  # no modular overflow
                acc = result
            self.out.append(acc)
        self.solver = Cadical195(bootstrap_with=self.cnf)

    def var(self):
        self.nv += 1
        return self.nv

    def xor(self, a, b):
        if a == self.zero:
            return b
        if b == self.zero:
            return a
        if a == -self.zero:
            return -b
        if b == -self.zero:
            return -a
        if a == b:
            return self.zero
        if a == -b:
            return -self.zero
        z = self.var()
        self.cnf.extend([[a, b, -z], [-a, -b, -z], [a, -b, z], [-a, b, z]])
        return z

    def both(self, a, b):
        if self.zero in (a, b) or a == -b:
            return self.zero
        if a == -self.zero or a == b:
            return b
        if b == -self.zero:
            return a
        z = self.var()
        self.cnf.extend([[-a, -b, z], [a, -z], [b, -z]])
        return z

    def either(self, a, b):
        return -self.both(-a, -b)

    def assumptions(self, target):
        if len(target) != self.k or any(t < 0 or t >= 1 << self.width for t in target):
            raise ValueError('target outside exact output range')
        return [lit if (t >> bit) & 1 else -lit
                for t, word in zip(target, self.out) for bit, lit in enumerate(word)]

    def solve(self, target, extra=(), limit=QUERY_CONFLICTS):
        budget()
        before = self.solver.accum_stats()
        self.solver.conf_budget(limit)
        cpu = time.process_time()
        ok = self.solver.solve_limited(assumptions=self.assumptions(target) + list(extra))
        elapsed = time.process_time() - cpu
        after = self.solver.accum_stats()
        delta = {k: after[k] - before.get(k, 0) for k in after}
        bins = None
        if ok is True:
            positive = set(v for v in self.solver.get_model() if v > 0)
            bins = [[2*j+1 for j in range(self.m) if self.x[j][b] in positive]
                    for b in range(self.k)]
        return ok, bins, delta, elapsed

    def close(self):
        self.solver.delete()


def emit(stream, row):
    stream.write(json.dumps(row, sort_keys=True, separators=(',', ':')) + '\n')
    stream.flush()


def literal(m, target, bins):
    return (bins is not None and len(bins) == len(target) and
            sorted(v for b in bins for v in b) == list(range(1, 2*m, 2)) and
            [sum(b) for b in bins] == list(target))


def controls(stream):
    count, fixed = 0, 0
    for m in range(1, 7):
        model = Model(m, 3)
        oracle = set()
        for labels in product(range(3), repeat=m):
            sums = [sum(2*j+1 for j, label in enumerate(labels) if label == b) for b in range(3)]
            if min(sums) > 0:
                oracle.add(tuple(sorted(sums)))
        for a in range(1, m*m//3 + 1):
            for b in range(a, (m*m-a)//2 + 1):
                t = (a, b, m*m-a-b)
                ok, bins, _, _ = model.solve(t)
                assert ok is not None and ok == (t in oracle)
                if ok:
                    assert literal(m, t, bins)
                count += 1
        model.close()
        model = Model(m, 2)
        for labels in product(range(2), repeat=m):
            t = tuple(sum(2*j+1 for j, label in enumerate(labels) if label == b) for b in range(2))
            extra = [v if labels[j] == b else -v for j, row in enumerate(model.x) for b, v in enumerate(row)]
            ok, bins, _, _ = model.solve(t, extra)
            assert ok is True and literal(m, t, bins)
            wrong = list(t)
            wrong[0] ^= 1  # exact fixed-assignment output, not just total preservation
            assert model.solve(wrong, extra)[0] is False
            fixed += 1
        model.close()
    assert count == 189 and fixed == 126
    model = Model(3, 3)
    # Incremental A -> impossible B -> A must not retain B's target assumptions.
    sequence = []
    for t in ((1, 3, 5), (3, 3, 3), (1, 3, 5)):
        ok, bins, _, _ = model.solve(t)
        sequence.append(ok)
        if ok:
            assert literal(3, t, bins)
    assert sequence == [True, False, True]
    assert model.solve((1, 3, 5), [model.x[0][0], model.x[0][1]])[0] is False
    assert model.solve((1, 3, 5), [-v for v in model.x[0]])[0] is False
    model.close()
    model = Model(28, 8)  # a disposable full-width control; never reused by pilot
    t = (69,69,69,93,121,121,121,121)
    fixture = [[1,3,5,7,9,11,33],[13,15,41],[17,21,31],[19,23,51],
               [25,43,53],[27,39,55],[29,45,47],[35,37,49]]
    def pin(bins):
        owner = {v:b for b, row in enumerate(bins) for v in row}
        return [v if owner[2*j+1] == b else -v
                for j, row in enumerate(model.x) for b, v in enumerate(row)]
    assert model.solve(t, pin(fixture))[0] is True
    fixture[0].remove(1)
    fixture[-1].append(1)
    mixed = (68,69,69,93,121,121,121,122)
    ok, bins, _, _ = model.solve(mixed, pin(fixture))
    assert ok is True and literal(28, mixed, bins)
    fixture[0][0], fixture[1][0] = fixture[1][0], fixture[0][0]
    assert model.solve(mixed, pin(fixture))[0] is False
    model.close()
    emit(stream, dict(kind='controls', oracle_questions=count, fixed_assignments=fixed,
                      wrong_bit_negatives=fixed, assumption_sequence=sequence,
                      duplicate_and_missing_assignment_rejected=True,
                      full_width_fixed_positives=2, full_width_wrong_sum_rejected=True))


def main():
    if len(sys.argv) != 3:
        raise SystemExit('usage: PRIMARY INPUT_TXT STREAM_JSONL')
    # Hard OS CPU fallback; normal budget is checked before/after limited calls.
    resource.setrlimit(resource.RLIMIT_CPU, (25, 26))
    target_rows = [tuple(map(int, line.split())) for line in Path(sys.argv[1]).read_text().splitlines()]
    assert len(target_rows) == 2000
    status = 'ERROR'
    with Path(sys.argv[2]).open('x') as stream:
        try:
            controls(stream)
            model = Model(28, 8)
            emit(stream, dict(kind='model', variables=model.nv, clauses=len(model.cnf),
                              assignment_variables=224, width=model.width, solver='Cadical195'))
            total_conflicts, completed = 0, 0
            for i, target in enumerate(target_rows):
                budget()
                emit(stream, dict(kind='start', index=i, target=target))
                limit = min(QUERY_CONFLICTS, TOTAL_CONFLICTS - total_conflicts)
                if limit <= 0:
                    status = 'UNKNOWN_TOTAL_CONFLICT_CAP'
                    break
                ok, bins, stats, cpu = model.solve(target, limit=limit)
                total_conflicts += stats['conflicts']
                emit(stream, dict(kind='result', index=i, target=target, sat=ok, bins=bins,
                                  stats=stats, cpu_seconds=cpu, total_conflicts=total_conflicts))
                if ok is None:
                    status = 'UNKNOWN_CONFLICT_CAP'
                    break
                if ok is False:
                    status = 'PRIMARY_UNSAT_NOT_CERTIFIED'
                    break
                assert literal(28, target, bins)
                completed += 1
                budget()  # retain the just-finished call's work before testing caps
            else:
                status = 'COMPLETE_SAME_2000'
            model.close()
            emit(stream, dict(kind='end', status=status, completed=completed,
                              total_conflicts=total_conflicts, primary_cpu_seconds=time.process_time()-START,
                              primary_wall_seconds=time.monotonic()-WALL, peak_rss_bytes=rss()))
        except Exception as e:
            emit(stream, dict(kind='end', status='ERROR_OR_CAP', reason=type(e).__name__ + ': ' + str(e),
                              primary_cpu_seconds=time.process_time()-START, peak_rss_bytes=rss()))
    return 0 if status == 'COMPLETE_SAME_2000' else 2


if __name__ == '__main__':
    raise SystemExit(main())
