"""GC371: sound arc-consistency forcing beside a prescribed wheel.
No singleton conclusion is inferred from unresolved domains; no SAT completeness claim.
"""
from collections import deque
import json
from pathlib import Path
import re


def propagate(N, m, trace, phase=0):
    width = m + 2
    domains = [3] * ((N + 1) * width)
    ix = lambda t, x: t * width + x
    for t in range(N + 1):
        domains[ix(t, 0)] = 1 << (t % 2)
        if t < N:
            domains[ix(t, 1)] = 1 << trace[(t - phase) % len(trace)]
    tuples = [(l, c, r, l ^ (c | r)) for l in (0, 1)
              for c in (0, 1) for r in (0, 1)]
    constraints = [(ix(t, x-1), ix(t, x), ix(t, x+1), ix(t+1, x))
                   for t in range(N) for x in range(1, m+1)]
    watchers = [[] for _ in domains]
    for j, variables in enumerate(constraints):
        for v in variables:
            watchers[v].append(j)
    queue = deque(range(len(constraints)))
    pending = set(queue)
    while queue:
        j = queue.popleft(); pending.remove(j)
        variables = constraints[j]
        allowed = [row for row in tuples if all(domains[v] & (1 << a)
                    for v, a in zip(variables, row))]
        if not allowed:
            return None
        for k, v in enumerate(variables):
            supported = 0
            for row in allowed:
                supported |= 1 << row[k]
            if supported != domains[v]:
                domains[v] = supported
                for neighbor in watchers[v]:
                    if neighbor not in pending:
                        pending.add(neighbor); queue.append(neighbor)
    return [[domains[ix(t,x)] for x in range(width)] for t in range(N+1)]


def main():
    src = Path('tests/probes/lexicon/rule30_wheel_left.py').read_text()
    U = [int(c) for c in re.search(r'^U = "([01]+)"', src, re.M).group(1)]
    assert len(U) == 56
    # Literal incompatible wall=01 and companion=11 must be rejected, GC313.
    assert propagate(4, 2, [1]) is None
    report = []
    for N in (56, 112, 168):
        rows = propagate(N, 40, U)
        assert rows is not None
        counts = [sum(rows[t][x] != 3 for t in range(N)) for x in range(1, 41)]
        lo, hi = N//3, 2*N//3
        complete = [x for x in range(2, 41) if all(rows[t][x] != 3 for t in range(lo, hi))]
        periodic_conflicts = [(x,t) for x in range(2,41) for t in range(N-56)
                              if rows[t][x] != 3 and rows[t+56][x] != 3
                              and rows[t][x] != rows[t+56][x]]
        report.append(dict(N=N, singleton_counts=counts,
                           complete_middle_columns=complete,
                           known_period56_conflicts=len(periodic_conflicts)))
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
