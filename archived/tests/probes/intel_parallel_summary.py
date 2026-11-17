#!/usr/bin/env python3
"""Summarize a completed frozen Intel benchmark; never rank censored timings.
Usage: intel_parallel_summary.py PLAN OUTPUT_DIRECTORY
Two repeats give descriptive ranges, not statistical confidence intervals.
"""
import json
import statistics
import sys
from pathlib import Path

plan = json.loads(Path(sys.argv[1]).read_text())
out = Path(sys.argv[2])
launcher = json.loads((out / 'launcher.json').read_text())
summary = json.loads((out / 'summary.json').read_text())
assert launcher['exit_reason'] == 'COMPLETED' and launcher['child_rc'] == 0
assert not summary['stop']
assert [r['name'] for r in summary['results']] == [j['name'] for j in plan['jobs']]
groups = {}
for job, result in zip(plan['jobs'], summary['results']):
    stored = json.loads((out / (job['name'] + '.receipt.json')).read_text())
    assert stored == result
    assert result['args'][1] == '--threads=' + str(job['threads'])
    assert result['args'][2] == job['cnf']
    assert result['reason'] == 'EXIT'
    assert result['returncode'] == 20 or (
        result['returncode'] in (-9, -24)
        and result.get('censored') == 'CPU_LIMIT'
        and result['cpu_s'] >= .95 * job['cpu'])
    case = job['name'].rsplit('-r', 1)[0]
    groups.setdefault((case, job['threads']), []).append(result)
rows = []
for (case, threads), rs in sorted(groups.items()):
    solved = [r for r in rs if r['returncode'] == 20]
    row = {'case': case, 'threads': threads, 'runs': len(rs), 'solved': len(solved),
           'wall_s': [r['wall_s'] for r in rs],
           'cpu_s': [r['cpu_s'] for r in rs],
           'maxrss_mib': [r['maxrss_bytes'] / (1 << 20) for r in rs],
           'median_solved_wall_s': statistics.median([r['wall_s'] for r in solved]) if len(solved) == len(rs) else None,
           'median_solved_cpu_s': statistics.median([r['cpu_s'] for r in solved]) if len(solved) == len(rs) else None}
    rows.append(row)
print(json.dumps({'rows': rows, 'worker_cpu_s': summary['worker_cpu_s'],
                  'supervisor_cpu_s': launcher['supervisor_cpu_s'],
                  'host_maxima': launcher['maxima'],
                  'interpretation': 'Descriptive two-repeat ranges only; no ranking of censored wall times.'}, indent=2))
