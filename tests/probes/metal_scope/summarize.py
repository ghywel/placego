#!/usr/bin/env python3
"""Summarize complete matched arms while retaining an interrupted stage's status.

Usage: summarize.py STAGE_DIR REPEATS > summary-derived.json
No extrapolation, censored timing, or oracle success inferred from an exit code.
"""
import json
import statistics
import sys
from pathlib import Path


def summarize(root, repeats):
    launcher = json.loads((root / 'launcher.json').read_text())
    stage = json.loads((root / 'summary.json').read_text())
    native = [p for p in root.glob('*.stdout') if p.stem in ('pilot', 'benchmark')]
    assert len(native) == 1, native
    events = [json.loads(line) for line in native[0].read_text().splitlines()]
    cases = []
    samples = [e for e in events if e['event'] == 'sample']
    assert all(e['checked_all_outputs'] for e in samples)
    for case in (e for e in events if e['event'] == 'case'):
        key = tuple(case[k] for k in ('kind', 'n', 'steps'))
        matched = [e for e in samples if tuple(e[k] for k in ('kind', 'n', 'steps')) == key]
        arms = []
        for backend, threads in [('cpu', 1), ('cpu', 2), ('cpu', 4), ('metal', 0)]:
            arm = [e for e in matched if (e['backend'], e['threads']) == (backend, threads) and e['rep'] >= 0]
            ids = sorted(e['rep'] for e in arm)
            assert len(ids) == len(set(ids)), 'duplicate sample'
            record = {'backend': backend, 'threads': threads, 'repeats': ids,
                      'complete': ids == list(range(repeats))}
            if arm:
                for metric in ('wall_ms', 'cpu_ms', 'gpu_command_ms'):
                    values = [e[metric] for e in arm]
                    record[metric] = {'median': statistics.median(values),
                                      'min': min(values), 'max': max(values)}
            arms.append(record)
        cases.append({'case': case, 'complete_matched_case': all(a['complete'] for a in arms), 'arms': arms})
    return {
        'stage_status': launcher['exit_reason'],
        'native_complete': any(e['event'] == 'complete' for e in events),
        'completed_cases': sum(c['complete_matched_case'] for c in cases),
        'cases_started': len(cases), 'samples_checked': len(samples),
        'gpu_samples_checked': sum(e['backend'] == 'metal' for e in samples),
        'worker_cpu_s': stage['worker_cpu_s'],
        'supervisor_cpu_s': launcher['supervisor_cpu_s'],
        'wall_s': launcher['wall_s'], 'maxima': launcher['maxima'],
        'cleanup': launcher['cleanup'],
        'gpu_command_sum_s': sum(e['gpu_command_ms'] for e in samples) / 1000,
        'cases': cases,
    }


if __name__ == '__main__':
    print(json.dumps(summarize(Path(sys.argv[1]), int(sys.argv[2])), indent=2))
