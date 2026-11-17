#!/usr/bin/env python3
"""One fixed, single-process control of the two-level physical inverse.

Run only under run_capped.py with a separately published freeze. No solver,
adaptive search, child research process, external dependency, or widening.
The oracle evolves literal neighbourhoods forward, independently of inversion.
"""
import argparse
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import re
import resource
import subprocess
import time

p = argparse.ArgumentParser()
p.add_argument('--expected-sha256', required=True)
a = p.parse_args()
out = Path(os.environ['CAPPED_OUT'])
start = time.monotonic()
last_thermal = -10.0
result = {'status': 'RUNNING', 'width_cap': 12, 'controls': {},
          'thermal': [], 'cpu_stop_seconds': 110, 'wall_stop_seconds': 280,
          'outer_supervisor_cpu_included': False, 'research_processes': 1,
          'research_threads': 1, 'source_sha256': a.expected_sha256}


def cpu():
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time() + child.ru_utime + child.ru_stime


def save():
    (out / 'result.json').write_text(json.dumps(result, indent=2) + '\n')


def guard(force_thermal=False):
    global last_thermal
    if cpu() >= 110:
        raise RuntimeError('AGGREGATE_CPU_STOP')
    if time.monotonic() - start >= 280:
        raise RuntimeError('WALL_STOP')
    if force_thermal or time.monotonic() - last_thermal >= 2:
        r = subprocess.run(['pmset', '-g', 'therm'], capture_output=True,
                           text=True, timeout=5)
        text = r.stdout + r.stderr
        limits = re.findall(r'CPU_(?:Speed|Scheduler)_Limit\s*=\s*(\d+)', text)
        okay = (r.returncode == 0 and len(limits) == 2
                and all(int(x) == 100 for x in limits)
                and 'No thermal warning level' in text
                and 'No performance warning level' in text)
        result['thermal'].append({'wall': time.monotonic()-start,
                                  'rc': r.returncode, 'text': text, 'okay': okay})
        last_thermal = time.monotonic()
        if not okay:
            raise RuntimeError('THERMAL_OR_MONITOR_STOP')


def require(okay, label):
    result['controls'][label] = bool(okay)
    if not okay:
        raise RuntimeError('CONTROL_FAILED:' + label)


def words(w):
    if w == 1:
        yield '1'
    else:
        for middle in itertools.product('01', repeat=w-2):
            yield '1' + ''.join(middle) + '1'


def forward(word):
    # Literal Rule30 truth table indexed by (left, centre, right).
    truth = (0, 1, 1, 1, 1, 0, 0, 0)
    row = [0, 0] + [int(x) for x in word] + [0, 0]
    return ''.join(str(truth[4*row[i-1]+2*row[i]+row[i+1]])
                   for i in range(1, len(row)-1))


def pair_step(bit, state):
    a0, b0 = state
    return bit ^ (a0 | b0), a0


def step(bit, state):
    a0, b0, c0, d0 = state
    aa = bit ^ (a0 | b0)
    cc = aa ^ (c0 | d0)
    return aa, a0, cc, c0


def iterate_zero(state, length):
    for _ in range(length):
        state = step(0, state)
    return state


def accepts(word, depth=2, initial=None):
    if not word or '1' not in word:
        return False
    state = initial if initial is not None else (0,) * (2*depth)
    transition = pair_step if depth == 1 else step
    for bit in reversed(word):
        state = transition(int(bit), state)
    return state == (0,) * (2*depth)


def count_one(w, k):
    total = 0
    for r in range(1, k-1):
        residue = k-r-2
        if residue < 0 or residue % 2:
            continue
        h = residue // 2
        if h <= r-1 and w >= 2*r+1+h:
            total += math.comb(r-1, h) * math.comb(w-2-r, r+h-1)
    return total


try:
    source = Path(__file__).read_bytes()
    require(hashlib.sha256(source).hexdigest() == a.expected_sha256, 'source_pin')
    (out / 'source.py').write_bytes(source)
    os.nice(10)
    result['nice'] = os.getpriority(os.PRIO_PROCESS, 0)
    require(result['nice'] >= 10, 'nice_applied')
    guard(True)
    zero = (0, 0, 0, 0)
    states = list(itertools.product((0, 1), repeat=4))
    require(all(iterate_zero(s, m+3) == iterate_zero(s, m)
                for s in states for m in range(2, 11)), 'zero_gap_period_three')
    require(iterate_zero((0, 1, 0, 0), 1) != iterate_zero((0, 1, 0, 0), 4),
            'preperiod_one_countercontrol')
    require([s for s in states if step(0, s) == zero] == [zero], 'zero_unique_predecessor')
    require(accepts('111', 1) and not accepts('111', 2), 'one_past_is_not_two')
    require(accepts('11001', 2), 'literal_grandchild')
    require(not accepts('11', 1) and not accepts('11', 2), 'small_width_boundary')
    require(not accepts('0', 1) and not accepts('0', 2), 'nonzero_domain')
    oracle_one, oracle_two = set(), set()
    for w in range(1, 11):
        guard()
        for x in words(w):
            y = forward(x)
            integer = int(x, 2)
            require(int(y, 2) == integer ^ ((integer << 1) | (integer << 2)),
                    'truth_table_integer_orientation')
            oracle_one.add(y)
            if w <= 8:
                oracle_two.add(forward(y))
    require(len(oracle_one) == 512 and len(oracle_two) == 128, 'oracle_cardinalities')
    groups = []
    seen = one = two = mutant_disagreements = 0
    for w in range(1, 13):
        guard()
        one_by_mass, two_by_mass = {}, {}
        for x in words(w):
            if seen % 128 == 0:
                guard()
            seen += 1
            p1, p2 = accepts(x, 1), accepts(x, 2)
            require(p1 == (x in oracle_one), 'one_level_matches_forward_oracle')
            require(p2 == (x in oracle_two), 'two_level_matches_forward_oracle')
            require(not p2 or x.startswith('110'), 'two_past_prefix')
            one += p1
            two += p2
            k = x.count('1')
            one_by_mass[k] = one_by_mass.get(k, 0) + p1
            two_by_mass[k] = two_by_mass.get(k, 0) + p2
            mutant_disagreements += accepts(x, 2, (0, 0, 0, 1)) != p2
        require(all(one_by_mass.get(k, 0) == count_one(w, k)
                    for k in range(1, w+1)), 'gc2296_mass_formula')
        groups.append({'width': w, 'one_past_by_mass': one_by_mass,
                       'two_past_by_mass': two_by_mass})
    require(seen == 2048 and one == 512 and two == 128, 'complete_fixed_fixture')
    require(mutant_disagreements > 0, 'wrong_right_boundary_detected')
    result.update({'target_words': seen, 'one_past': one, 'two_past': two,
                   'mutant_disagreements': mutant_disagreements, 'groups': groups})
    guard(True)
    result['status'] = 'PASS'
except BaseException as error:
    result['status'] = 'FAILED'
    result['error'] = str(error)
    raise
finally:
    result['aggregate_cpu_final'] = cpu()
    result['wall_seconds'] = time.monotonic()-start
    save()
