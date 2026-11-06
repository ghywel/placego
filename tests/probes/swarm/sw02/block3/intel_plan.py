#!/usr/bin/env python3
"""Generate the frozen serial Intel job list for the existing capped stage driver.

Use metal_scope/stage.py as a generic CPU orchestrator, not as a GPU backend.
Each worker execs in CAPPED_OUT; all artifacts share the outer disk envelope.
OMP/BLAS thread counts must be one in the launching environment.
"""
import hashlib
import json
import sys
from pathlib import Path

phase = sys.argv[1]
assert phase in ('smoke', 'main')
B = Path(__file__).resolve().parent
repo = B.parents[4]
jobs = []

def job(name, folder, args, cpu=120, wall=300):
    jobs.append({'name': name, 'cpu': cpu, 'wall': wall,
                 'args': [sys.executable, str(B / 'intel_worker.py'), '{out}/' + folder] + args})

binary = '{out}/lift'
targets = str(B / 'targets.txt')
job('compile', '.', ['cc', '-O2', '-Wall', '-Wextra', '-o', binary, str(B / 'lift.c')], 30, 60)
for w in (19, 20, 21, 22):
    job('base' + str(w), 'base', [binary, '--targets', targets, '--mode', 'pq', '--dense', str(w)])
job('base', 'base', [binary, '--targets', targets, '--mode', 'pq', '--wmax', '22', '--gapn', '0', '--over-max', '0', '--out', '.'])
smoke = phase == 'smoke'
job('r02', 'r02', [binary, '--targets', targets, '--mode', 'xx', '--r02', '--wmax', '22' if smoke else '31', '--gapn', '0', '--over-max', '0', '--out', '.'])
job('rows', 'rows', [binary, '--targets', targets, '--mode', 'xx', '--rows', '14' if smoke else '22', '4400', 'late.txt'], 120 if smoke else 300, 600)
job('xx', 'xx', [binary, '--targets', targets, '--mode', 'xx', '--wmax', '26' if smoke else '40', '--gapn', '16', '--gap-limit', '60000000', '--over-max', '26' if smoke else '36', '--max-nodes', '60000000', '--dump', '--out', '.'], 120 if smoke else 500, 900)
job('xxp', 'xxp', [binary, '--targets', targets, '--mode', 'xx', '--wmax', '28' if smoke else '46', '--wreport', '22' if smoke else '34', '--prune-from', '22' if smoke else '34', '--gapn', '16', '--gap-limit', '60000000', '--over-max', '28' if smoke else '43', '--max-nodes', '60000000', '--out', '.'], 120 if smoke else 500, 900)
job('pq', 'pq', [binary, '--targets', targets, '--mode', 'pq', '--wmax', '24' if smoke else '40', '--gapn', '16', '--gap-limit', '60000000', '--over-max', '24' if smoke else '34', '--max-nodes', '60000000', '--dump', '--out', '.'], 120 if smoke else 400, 900)
for name, mode, width in [('checkxx', 'xx', 22 if smoke else 36), ('checkpq', 'pq', 20 if smoke else 32)]:
    job(name, mode, [sys.executable, str(B / 'check_lift.py'), '--targets', targets, '--mode', mode,
                    '--wmax', str(width), '--scc', '{out}/' + mode + '/scc_' + mode + '.jsonl', '--dumps', '.'], 120 if smoke else 300, 600)
job('tails', 'xx', [sys.executable, str(B / 'tails.py'), str(B / 'control_rows.txt'), str(B.parent), targets, '.', 'xx'], 120 if smoke else 200, 600)
job('reentry', 'rows', [sys.executable, str(B / 'reentry.py'), 'late.txt', str(B.parent), '20' if smoke else '3000'], 120 if smoke else 200, 600)
job('validate', '.', [sys.executable, str(B / 'intel_validate.py'), '{out}', phase], 30, 60)

files = [p for p in B.iterdir() if p.suffix in ('.c', '.py', '.txt')]
files += [repo / 'tests/probes/metal_scope/stage.py', repo / 'tests/probes/wolfram/run_capped.py']
files += [B.parent / 'ref.py']
plan = {'phase': phase, 'worker_stop': 105 if smoke else 1700,
        'input_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}, 'jobs': jobs}
print(json.dumps(plan, indent=2))
