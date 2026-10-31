#!/usr/bin/env python3
"""GC2332: one bounded replay of Local's front certificate, plus a rejected potential mutation."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import resource
import subprocess
import time

START = time.monotonic()
SOURCE = Path(__file__).with_name('ether_front_potential_certificate.py')
EXPECTED = '544d14c71a64c5ee1f2c77ea9aed813e65fbabc6374409f7200bc6ebb0f58ee5'
THERMAL = []


def cpu():
    a = resource.getrusage(resource.RUSAGE_SELF)
    b = resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime + a.ru_stime + b.ru_utime + b.ru_stime


def guard():
    if cpu() > 15 or time.monotonic() - START > 25:
        raise RuntimeError('REVIEW_BUDGET_STOP')


def thermal():
    guard()
    r = subprocess.run(['pmset', '-g', 'therm'], capture_output=True, text=True, timeout=5)
    msg = r.stdout + r.stderr
    limits = re.findall(r'CPU_(?:Speed|Scheduler)_Limit\s*=\s*(\d+)', msg)
    ok = (r.returncode == 0 and len(limits) == 2 and all(x == '100' for x in limits)
          and 'No thermal warning level' in msg and 'No performance warning level' in msg)
    THERMAL.append({'okay': ok, 'text': msg})
    if not ok:
        raise RuntimeError('THERMAL_OR_MONITOR_STOP')
    guard()


def main():
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != EXPECTED:
        raise RuntimeError('SOURCE_CHANGED')
    thermal()
    spec = importlib.util.spec_from_file_location('reviewed_front', SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.main()
    guard()
    original = module.G2
    module.G2 = (original[0] + 2,) + original[1:]
    rejected = False
    try:
        module.part2_lemmaA_B()
    except SystemExit as exc:
        rejected = 'A2: Phi invariant' in str(exc)
    finally:
        module.G2 = original
    if not rejected:
        raise RuntimeError('MUTATED_POTENTIAL_NOT_REJECTED')
    print('CONTROL: altered potential rejected by literal front transition check')
    thermal()
    print(json.dumps({'worker_aggregate_cpu_s': cpu(), 'wall_s': time.monotonic()-START,
                      'thermal': THERMAL, 'source_sha256': EXPECTED}))
    print('GPT_FRONT_REVIEW_PASS')


if __name__ == '__main__':
    main()
