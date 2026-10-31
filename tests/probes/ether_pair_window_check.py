#!/usr/bin/env python3
"""GC2327 finite self-check. Fixed horizons; only bounded thermal-check children."""
import itertools
import json
import os
import re
import resource
import subprocess
import time

START = time.monotonic()
THERMAL = []


def cpu_used():
    children = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time() + children.ru_utime + children.ru_stime


def guard():
    # No live child exists during research: Python has one thread and the
    # two thermal checks run synchronously before/after it. All reaped child
    # CPU is included; outer run_capped/time overhead is reported separately.
    if cpu_used() >= 110:
        raise RuntimeError('AGGREGATE_WORKER_CPU_STOP')
    if time.monotonic()-START >= 280:
        raise RuntimeError('DRIVER_WALL_STOP')


def thermal():
    guard()
    result = subprocess.run(['pmset', '-g', 'therm'], capture_output=True, text=True, timeout=5)
    message = result.stdout+result.stderr
    limits = re.findall(r'CPU_(?:Speed|Scheduler)_Limit\s*=\s*(\d+)', message)
    okay = (result.returncode == 0 and len(limits) == 2 and
            all(int(v) == 100 for v in limits) and
            'No thermal warning level' in message and 'No performance warning level' in message)
    THERMAL.append({'okay': okay, 'text': message})
    if not okay:
        raise RuntimeError('THERMAL_OR_MONITOR_STOP')
    guard()


def good(r, u, v):
    return ((not u and v), u, (not u and not v), u,
            (not u and not v), u == (not v), (u and not v), u)[r % 8]


OFFSETS = ((0, 1), (0, 1), (0, 1), (-1, 0),
           (0, 1), (0, 1), (0, 1, 2), (0, 1))
POTENTIAL = (0, 5, 2, -1, 4, 1, 6, 3)


def local_check():
    # Arrays cover times -1,0,1,2. Only recurrence implications required by
    # the published local_descent are assumed. No actual-orbit restriction.
    premises = [0] * 8
    for bits in itertools.product((False, True), repeat=11):
        guard()
        u, v, w = bits[:4], bits[4:8], bits[8:]
        if not all((u[t] != u[t+1]) == (v[t] or w[t]) for t in range(3)):
            continue
        if not all(not w[t] or v[t] != v[t+1] for t in range(3)):
            continue
        for h, ds in enumerate(OFFSETS):
            if all(good(h+2+d, u[1+d], v[1+d]) for d in ds):
                premises[h] += 1
                assert good(h, v[1], w[1]), (h, bits)
    assert all(premises), premises
    edges = []
    for h, ds in enumerate(OFFSETS):
        for d in ds:
            target = (h+2+d) % 8
            slack = POTENTIAL[h]-POTENTIAL[target]-(3*d-2)
            assert slack >= 0
            assert slack == (8 if (h, d) in ((1, 0), (6, 0)) else 0)
            edges.append([h, d, target, slack])
    assert len(edges) == 17
    return premises, edges


def edge_step(x):
    return [x[0]] + [x[j] != (x[j-1] or (j > 1 and x[j-2]))
                     for j in range(1, len(x))]


def physical_step(black):
    # Literal Wolfram Rule 30 truth table, different representation/oracle.
    if not black:
        return set()
    out = set()
    for j in range(min(black)-1, max(black)+2):
        index = 4*(j-1 in black)+2*(j in black)+(j+1 in black)
        if (30 >> index) & 1:
            out.add(j)
    return out


def finite_check():
    counts = []
    oracle_cells = 0
    for k in range(9):
        bound = (2*k)//3 + 5
        longest = -1
        witness = None
        cases = 0
        for tail in itertools.product((False, True), repeat=k+1):
            guard()
            initial = [True, *tail]
            x = initial[:]
            physical = {-j for j, bit in enumerate(initial) if bit}
            pairs = []
            for t in range(bound):
                for j, bit in enumerate(x):
                    assert bit == (t-j in physical), (k, tail, t, j)
                    oracle_cells += 1
                pairs.append((x[k+1], x[k]))
                x = edge_step(x)
                physical = physical_step(physical)
            for phase in range(8):
                run = next((t for t, (u, v) in enumerate(pairs)
                            if not good(t+phase, u, v)), bound)
                assert run < bound, (k, initial, phase)
                if run > longest:
                    longest = run
                    witness = {'initial': ''.join(str(int(b)) for b in initial),
                               'phase': phase}
                cases += 1
        counts.append({'k': k, 'bound': bound, 'cases': cases,
                       'maximum_initial_good_run': longest, 'witness': witness})
    assert counts[0]['maximum_initial_good_run'] == 3
    return counts, oracle_cells


def controls():
    # The positive ether is infinite in both spatial directions; modulo 4
    # is explicit. It is NOT a black-edge code.
    words = (43, 202, 178, 172)
    bit = lambda i, t: bool((words[i % 4] >> (t % 8)) & 1)
    for i in range(4):
        for t in range(8):
            assert bit(i, t+1) == (bit(i, t) != (bit(i-1, t) or bit(i-2, t)))
            assert good(t+2*i, bit(i+1, t), bit(i, t))
    assert all(good(7+t, bool(1-t % 2), True) for t in range(3))
    assert not good(10, False, True)
    # Unexpected guard: the only past dependency is reachable only at an
    # odd offset from an even target phase; it cannot cross the start time.
    for start in (2, 4, 6):
        frontier = {(start, 0)}
        for _ in range(12):
            frontier = {((h+2+d) % 8, off+d)
                        for h, off in frontier for d in OFFSETS[h]}
            assert all(off >= 0 and h % 2 == off % 2 for h, off in frontier)


if __name__ == '__main__':
    record = {'status': 'RUNNING', 'status_limit': 'finite self-check, not independent carrying read'}
    try:
        priority = os.getpriority(os.PRIO_PROCESS, 0)
        if priority < 10:
            os.nice(10-priority)
        assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
        thermal()
        premises, edges = local_check()
        record.update(local_premise_counts=premises, potential_edges=edges)
        controls()
        counts, oracle_cells = finite_check()
        record.update(depth_checks=counts, physical_oracle_cell_comparisons=oracle_cells)
        thermal()
        record['status'] = 'PASS'
    except BaseException as exc:
        record.update(status='FAILED', error=repr(exc))
        raise
    finally:
        record.update(aggregate_worker_cpu_s=cpu_used(), wall_seconds=time.monotonic()-START,
                      outer_supervisor_cpu_included=False, thermal=THERMAL)
        print(json.dumps(record, indent=2))
