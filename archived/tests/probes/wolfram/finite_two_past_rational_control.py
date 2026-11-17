#!/usr/bin/env python3
"""One frozen exact-algebra check of the seven-state two-past rational series.

Uses retained GC2300 oracle counts; never evolves new rows or expands the machine.
Only standard-library integer polynomials, one thread and serial thermal reads.
Run under run_capped.py after publishing exact source and a separate stage freeze.
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
p.add_argument('--fixture', required=True)
a = p.parse_args()
out = Path(os.environ['CAPPED_OUT'])
start = time.monotonic()
last_thermal = -10.0
result = {'status': 'RUNNING', 'retained_width_cap': 12, 'controls': {},
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


# Sparse exact integer polynomials in (z,u); every operation is bounded here.
def mono(z=0, u=0, coefficient=1):
    return {(z, u): coefficient} if coefficient else {}

def add(*terms):
    ans = {}
    for term in terms:
        for key, value in term.items():
            ans[key] = ans.get(key, 0) + value
    return {k: v for k, v in ans.items() if v}

def neg(poly):
    return {k: -v for k, v in poly.items()}

def mul(*terms):
    ans = mono()
    for term in terms:
        new = {}
        for (a, b), x in ans.items():
            for (c, d), y in term.items():
                new[a+c, b+d] = new.get((a+c, b+d), 0) + x*y
        ans = {k: v for k, v in new.items() if v}
        guard()
    return ans

def series(numer, denom):
    require(denom.get((0, 0)) == 1 and all(w > 0 for w, k in denom if (w, k) != (0, 0)),
            'well_founded_series')
    coeffs = {}
    for w in range(13):
        guard()
        for k in range(13):
            coeffs[w, k] = numer.get((w, k), 0) - sum(
                value * coeffs.get((w-dw, k-dk), 0)
                for (dw, dk), value in denom.items() if (dw, dk) != (0, 0))
    return coeffs

def at_one(poly):
    ans = {}
    for (w, k), value in poly.items():
        ans[w, 0] = ans.get((w, 0), 0) + value
    return {key: value for key, value in ans.items() if value}

def encoded(poly):
    return [[w, k, v] for (w, k), v in sorted(poly.items())]

try:
    source = Path(__file__).read_bytes()
    require(hashlib.sha256(source).hexdigest() == a.expected_sha256, 'source_pin')
    (out / 'source.py').write_bytes(source)
    fixture_data = Path(a.fixture).read_bytes()
    require(hashlib.sha256(fixture_data).hexdigest() ==
            'f80ccf5a1f798b428c5d28cd73f06d4271c947d6923d9b10a353bdb533b17895', 'retained_fixture_pin')
    (out / 'fixture.json').write_bytes(fixture_data)
    fixture = json.loads(fixture_data)
    require(fixture['status'] == 'PASS' and fixture['width_cap'] == 12, 'retained_fixture_scope')
    os.nice(10)
    result['nice'] = os.getpriority(os.PRIO_PROCESS, 0)
    require(result['nice'] >= 10, 'nice_applied')
    guard(True)
    classes = {'A': [0], 'B': [3], 'C': [9, 13], 'D': [10, 14],
               'E': [4], 'F': [6, 7], 'G': [12]}
    transition = {'A': ('A', 'D'), 'B': ('B', 'C'), 'C': ('G', 'F'),
                  'D': ('C', 'F'), 'E': ('D', 'A'), 'F': ('C', 'B'), 'G': ('D', 'E')}
    owner = {s: label for label, states in classes.items() for s in states}
    edges = 0
    for label, states in classes.items():
        for state in states:
            aa, bb, cc, dd = ((state >> i) & 1 for i in (3, 2, 1, 0))
            for e in (0, 1):
                A = e ^ (aa | bb)
                C = A ^ (cc | dd)
                target = (A << 3) | (aa << 2) | (C << 1) | cc
                require(owner.get(target) == transition[label][e], 'complete_quotient_table')
                edges += 1
    require(edges == 20, 'all_twenty_transition_checks')
    one, z, u = mono(), mono(1), mono(0, 1)
    P = add(one, neg(z))
    R = add(P, mono(1, 2))
    S = add(P, mul(z, u, R))
    T = add(P, neg(mul(mono(2, 1), R)))
    V = add(T, neg(mul(mono(3), add(one, mono(1, 1)), S)))
    denominator = add(mul(P, P), neg(mul(mono(2, 1), P, R)), neg(mul(mono(3), S, S)))
    numerator = mul(P, mono(5, 3), S)
    suffix = {'A': V, 'B': mono(4, 3), 'C': mul(mono(3, 2), P),
              'D': mul(mono(4, 2), S), 'E': mul(mono(1, 1), add(T, neg(mul(mono(3), S)))),
              'F': mul(mono(4, 2), R), 'G': mul(mono(2, 2), T)}
    for label, (q0, q1) in transition.items():
        residual = add(suffix[label], neg(mul(z, suffix[q0])),
                       neg(mul(z, u, suffix[q1])), neg(denominator) if label == 'A' else {})
        require(not residual, 'exact_suffix_identity_' + label)
    require(not add(mul(P, P, V), neg(mul(P, denominator)), neg(numerator)),
            'exact_zero_padding_removal')
    require(at_one(S) == one and at_one(denominator) == add(one, mono(1, 0, -2)),
            'known_all_width_specialization')
    require(at_one(numerator) == mul(mono(5), P), 'known_all_width_numerator')
    actual = series(numerator, denominator)
    expected = {(g['width'], k): g['two_past_by_mass'].get(str(k), 0)
                for g in fixture['groups'] for k in range(g['width']+1)}
    require(len(expected) == 90 and all(actual[key] == val for key, val in expected.items()),
            'all_ninety_retained_width_mass_coefficients')
    require(sum(actual[key] for key in expected) == 128, 'retained_total_128')
    require(actual[0, 0] == 0 and all(actual[w, 0] == 0 for w in range(13)), 'exclude_empty_and_all_white')
    short = series(mul(mono(5, 3), S), denominator)
    sign = series(numerator, add(mul(P, P), neg(mul(mono(2, 1), P, R)), mul(mono(3), S, S)))
    mutant_padding = sum(short[key] != val for key, val in expected.items())
    mutant_sign = sum(sign[key] != val for key, val in expected.items())
    require(mutant_padding > 0, 'missing_padding_factor_detected')
    require(mutant_sign > 0, 'wrong_denominator_sign_detected')
    result.update(transition_checks=edges, suffix_identities=7, retained_coefficient_checks=90,
                  mutant_padding_disagreements=mutant_padding, mutant_sign_disagreements=mutant_sign,
                  numerator=encoded(numerator), denominator=encoded(denominator),
                  coefficient_table=[[w, k, actual[w, k]] for w, k in sorted(expected)],
                  fixture_sha256=hashlib.sha256(fixture_data).hexdigest(), new_dynamics_cases=0)
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
