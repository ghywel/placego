#!/usr/bin/env python3
"""GC2315 frozen boundary-moment pilot, depths 1/2/3 only.

Compare scalar finite input-cone covariance sums with a separate bit-parallel
whole-row oracle at widths 6*t+2 and 6*t+3. No adaptive extension or search.
Run once under run_capped.py after publishing the source hash and stage freeze.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument('--expected-sha256', required=True)
args = parser.parse_args()
out = Path(os.environ['CAPPED_OUT'])
started = time.monotonic()
last_thermal = -10.0
result = {'status': 'RUNNING', 'controls': {}, 'depths': [], 'thermal': [],
          'research_processes': 1, 'research_threads': 1,
          'cooperative_cpu_stop': 110, 'cooperative_wall_stop': 280,
          'supervisor_cpu_included': False}


def cpu():
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time() + child.ru_utime + child.ru_stime


def guard(force=False):
    global last_thermal
    if cpu() >= 110:
        raise RuntimeError('AGGREGATE_CPU_STOP')
    if time.monotonic() - started >= 280:
        raise RuntimeError('WALL_STOP')
    if force or time.monotonic() - last_thermal >= 2:
        r = subprocess.run(['pmset', '-g', 'therm'], capture_output=True,
                           text=True, timeout=5)
        txt = r.stdout + r.stderr
        limits = re.findall(r'CPU_(?:Speed|Scheduler)_Limit\s*=\s*(\d+)', txt)
        okay = (r.returncode == 0 and len(limits) == 2
                and all(int(x) == 100 for x in limits)
                and 'No thermal warning level' in txt
                and 'No performance warning level' in txt)
        result['thermal'].append({'wall': time.monotonic() - started,
                                  'rc': r.returncode, 'text': txt, 'okay': okay})
        last_thermal = time.monotonic()
        if not okay:
            raise RuntimeError('THERMAL_OR_MONITOR_STOP')


def require(okay, label):
    result['controls'][label] = bool(okay)
    if not okay:
        raise RuntimeError('CONTROL_FAILED:' + label)


def boundary(t):
    # Initial interval [-2*t,4*t]; t literal updates leave outputs [-t,3*t].
    # These are normalized output positions 0..4*t, unaffected by other input.
    count = 1 << (4*t)
    total = square = 0
    zs, szs = [0]*(2*t), [0]*(2*t)
    for mask in range(count):
        if mask % 256 == 0:
            guard()
        row = [0]*(2*t) + [1] + [(mask >> j) & 1 for j in range(4*t)]
        for _ in range(t):
            row = [row[j-1] ^ (row[j] | row[j+1]) for j in range(1, len(row)-1)]
        require(len(row) == 4*t+1 and row[0] == 1, f'cone_endpoints_t{t}')
        s = sum(row[1:2*t+1])
        total += s
        square += s*s
        for j, z in enumerate(row[2*t+1:]):
            zs[j] += z
            szs[j] += s*z
    mu = Q(total, count)
    var = Q(square, count) - mu*mu
    covs = [Q(sz, count)-mu*Q(z, count) for z, sz in zip(zs, szs)]
    require(all(2*z == count for z in zs), f'cone_bulk_fair_t{t}')
    return mu, var, covs, count


def whole(t, width):
    length = width - 2*t
    count = 1 << (length-2)
    seen, histogram = set(), {}
    for seed in range(count):
        if seed % 256 == 0:
            guard()
        row = 1 | (seed << 1) | (1 << (length-1))
        for _ in range(t):
            row = (row << 2) ^ ((row << 1) | row)
        require(row.bit_length() == width and row & 1 == 1,
                f'whole_normalized_t{t}_w{width}')
        seen.add(row)
        k = row.bit_count()
        histogram[k] = histogram.get(k, 0) + 1
    require(len(seen) == count, f'whole_injective_t{t}_w{width}')
    mean = Q(sum(k*v for k, v in histogram.items()), count)
    var = Q(sum(k*k*v for k, v in histogram.items()), count) - mean*mean
    return mean, var, count, histogram


try:
    source = Path(__file__).read_bytes()
    result['source_sha256'] = hashlib.sha256(source).hexdigest()
    require(result['source_sha256'] == args.expected_sha256, 'source_pin')
    (out / 'source.py').write_bytes(source)
    os.nice(10)
    result['nice'] = os.getpriority(os.PRIO_PROCESS, 0)
    require(result['nice'] >= 10, 'nice_applied')
    guard(True)
    for t in (1, 2, 3):
        mu, var, covs, cone_count = boundary(t)
        mean_offset = 1-t+mu
        variance_offset = -Q(t+1, 2)+var+2*sum(covs)
        if t == 1:
            require(mean_offset == Q(5, 4) and variance_offset == -Q(11, 16),
                    'one_past_hand_prediction')
            require(covs == [Q(0), Q(1, 16)], 'one_past_covariances')
        if t == 2:
            require(mean_offset == 1 and variance_offset == -Q(7, 8),
                    'two_past_hand_prediction')
            require(covs == [Q(1, 8), Q(1, 64), Q(0), -Q(1, 64)],
                    'GC2313_covariance_vector')
            require(-Q(t+1, 2)+var != variance_offset,
                    'false_boundary_bulk_independence_detected')
        row = {'t': t, 'cone_assignments': cone_count,
               'boundary_mean': str(mu), 'boundary_variance': str(var),
               'covariances': list(map(str, covs)),
               'mean_offset_from_W_over_2': str(mean_offset),
               'variance_offset_from_W_over_4': str(variance_offset), 'whole': []}
        for width in (6*t+2, 6*t+3):
            mean, variance, count, histogram = whole(t, width)
            require(mean == Q(width, 2)+mean_offset and
                    variance == Q(width, 4)+variance_offset,
                    f'boundary_vs_whole_t{t}_w{width}')
            row['whole'].append({'width': width, 'ancestors': count,
                                 'mean': str(mean), 'variance': str(variance),
                                 'mass_histogram': histogram})
        result['depths'].append(row)
    require(sum(r['cone_assignments'] for r in result['depths']) == 4368,
            'fixed_cone_domain_4368')
    require(sum(w['ancestors'] for r in result['depths'] for w in r['whole']) == 13104,
            'fixed_whole_domain_13104')
    guard(True)
    result['status'] = 'PASS'
except Exception as exc:
    result['status'] = 'FAIL'
    result['error'] = type(exc).__name__ + ': ' + str(exc)
finally:
    result['aggregate_worker_cpu_seconds'] = cpu()
    result['worker_wall_seconds'] = time.monotonic() - started
    (out / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': result['status'], 'controls': len(result['controls']),
                  'depths_completed': len(result['depths'])}))
raise SystemExit(0 if result['status'] == 'PASS' else 1)
