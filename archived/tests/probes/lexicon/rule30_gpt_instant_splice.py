#!/usr/bin/env python3
"""IS1: 784 formal visible-wheel seams, preregistered in GC577 (44f4992).
CPU, standard library, no actual Rule 30 trajectory or hidden-row realization.
Run: python3 tests/probes/lexicon/rule30_gpt_instant_splice.py
"""
import json
import time
from collections import Counter

U = '00010011010001001101000100110100010011010001001101001101'
V = tuple(map(int, U[::2]))
P = len(V)


def main():
    start = time.process_time()
    phi = [0]
    for bit in V:
        phi.append(phi[-1] + 14 * bit - 3)
    assert P == 28 and sum(V) == 6 and phi[-1] == 0
    tables = {name: Counter() for name in ('wheel_gaps', 'broader_gaps')}
    witnesses = {name: {} for name in tables}
    unexpected = []
    checks = 0
    for i in range(P):
        for j in range(P):
            def cell(n):
                return V[((i if n < 0 else j) + n) % P]
            left = next(n for n in range(-1, -P - 1, -1) if cell(n))
            right = next(n for n in range(P) if cell(n))
            gap = right - left - 1
            jump = phi[i] - phi[j]
            # Independent literal charge across complete black-to-black block.
            raw = sum(14 * cell(n) - 3 for n in range(left, right))
            via_endpoints = raw + phi[(i + left) % P] - phi[(j + right) % P]
            assert via_endpoints == jump
            assert raw == 11 - 3 * gap
            if i == j:
                assert jump == 0 and gap in (2, 4)
                assert all(cell(n) == V[(i + n) % P] for n in range(-56, 57))
            old_next = next(n for n in range(P) if V[(i + n) % P])
            new_prev = next(n for n in range(-1, -P - 1, -1) if V[(j + n) % P])
            old_gap = old_next - left - 1
            new_gap = right - new_prev - 1
            record = dict(old_phase=i, new_phase=j, left=left, right=right,
                          crossing_gap=gap, old_gap=old_gap, new_gap=new_gap,
                          jump=jump, raw_charge=raw)
            if gap == 2 and old_gap == new_gap == 4:
                unexpected.append(record)
            for name, allowed in [('wheel_gaps', (2, 4)), ('broader_gaps', (1, 2, 3, 4))]:
                if gap in allowed:
                    tables[name][jump] += 1
                    witnesses[name].setdefault(jump, record)
            checks += 1
    assert checks == 784
    report = {'pairs': checks, 'controls': 'PASS',
              'cpu_seconds': time.process_time() - start,
              'unexpected_short_from_two_long': {'count': len(unexpected),
                                                  'example': unexpected[0] if unexpected else None}}
    for name, counts in tables.items():
        lo, hi = min(counts), max(counts)
        report[name] = {'retained': sum(counts.values()), 'spectrum': dict(sorted(counts.items())),
                        'minimum_witness': witnesses[name][lo], 'maximum_witness': witnesses[name][hi]}
    report['IS_P1'] = any(abs(k) > 6 for k in tables['wheel_gaps'])
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
