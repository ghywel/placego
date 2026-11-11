#!/usr/bin/env python3
"""Check index transport and the constant P13 word bound against pinned objects."""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import signal
import sys

from gpt_return13_prefix_leaves import OUT, REPORT, guard, pin


def emit_source(plan, tail):
    lines = [f'import {item["module"]}' for item in plan['imports']]
    lines.extend([
        '',
        'namespace P13OverlapBound',
        '',
        'open P13WindowCoverage',
        'open Ruliology.CellularAutomata.Rule30MovingStrip',
        'open Ruliology.CellularAutomata.Rule30RingOrbits',
        '',
        'set_option maxRecDepth 100000',
        'set_option maxHeartbeats 0',
        '',
        'private def base : List Nat := List.replicate 170 1',
        'private def slope : List Nat := List.replicate 170 0',
        '',
        'private theorem retained_length : retained.length = 170 := by decide +kernel',
    ])
    ranges, checks = [], []
    for start in range(0, 170, 10):
        interval = f"List.range' {start} 10"
        label = f'vertices{start}'
        ranges.append(interval)
        checks.append(label)
        lines.append(f'private theorem {label} :')
        lines.append(f'    ({interval}).all (checkVertex 16 retained base slope) = true := by decide +kernel')
    lines.extend([
        '',
        'private theorem range_split : List.range 170 =',
        '    ' + ' ++ '.join(ranges) + ' := by decide +kernel',
        '',
        'private theorem vertices_ok :',
        '    (List.range retained.length).all (checkVertex 16 retained base slope) = true := by',
        '  rw [retained_length, range_split]',
        '  simp only [List.all_append, Bool.true_and, ' + ', '.join(checks) + ']',
        '',
        'private theorem base_ok :',
        '    sumList ((List.range retained.length).map (baseAt base)) ≤ 170 := by decide +kernel',
        '',
        'private theorem slope_ok :',
        '    sumList ((List.range retained.length).map (slopeAt slope)) ≤ 0 := by decide +kernel',
        '',
        'private theorem potential : checkPotential 16 retained base slope 170 0 = true := by',
        '  have hw : 0 < (16 : Nat) := by decide',
        '  simp only [checkPotential, hw, vertices_ok, base_ok, slope_ok, decide_true, Bool.true_and]',
        '',
        tail.decode(),
    ])
    return '\n'.join(lines).encode()


def audit_axioms(diagnostics):
    expected = {'checked_factor_indices', 'conditional_word_bound'}
    results = {}
    for line in diagnostics.strip().splitlines():
        match = re.fullmatch(r"'P13OverlapBound\.(\w+)' depends on axioms: \[([^]]*)\]", line)
        assert match is not None and match[1] not in results, diagnostics
        axioms = {item.strip() for item in match[2].split(',') if item.strip()}
        assert axioms <= {'propext', 'Classical.choice', 'Quot.sound'}, axioms
        results[match[1]] = sorted(axioms)
    assert results.keys() == expected, diagnostics
    return results


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
    prepare = sys.argv[2:] == ['--prepare']
    if not prepare:
        soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
        cap = plan['limits']['worker_soft_cpu_s']
        resource.setrlimit(resource.RLIMIT_CPU, (cap if soft == resource.RLIM_INFINITY
                                                else min(cap, soft), hard))
        for sig in (signal.SIGTERM, signal.SIGINT):
            signal.signal(sig, lambda s, f: guard.STOP.append(s))
        lean = Path(os.environ['RETURN13_LEAN'])
        pin(lean, plan['lean_binary_sha256'])
        kit = Path(os.environ['RETURN13_KIT_OBJECT_ROOT'])
        for name, sha in plan['kit_objects'].items():
            pin(kit/name, sha)
        imports = [kit]
        for item in plan['imports']:
            root = Path(os.environ[item['directory_env']])
            pin(root/f'{item["module"]}.olean', item['sha256'])
            if root not in imports:
                imports.append(root)
        os.environ['LEAN_PATH'] = os.pathsep.join(map(str, imports))
        os.environ['LEAN_NUM_THREADS'] = '1'
        _, version = guard.call('lean-version', [str(lean), '--version'], 2, 5, 0)
        assert version.strip() == plan['lean_version']
    spec = plan['theorem_source']
    source = emit_source(plan, pin(spec['file'], spec['sha256']))
    source_sha = hashlib.sha256(source).hexdigest()
    lean_file = OUT/'P13OverlapBound.lean'
    lean_file.write_bytes(source)
    if prepare:
        print(source_sha, len(source))
        return
    assert source_sha == plan['generated_source_sha256']
    olean = lean_file.with_suffix('.olean')
    limits = plan['limits']
    _, diagnostics = guard.call(
        'overlap-kernel', [str(lean), '-j1', '-DElab.async=false', '-R', str(OUT),
                           '-o', str(olean), str(lean_file)],
        limits['lean_child_cpu_s'], limits['lean_child_wall_s'], 0,
    )
    results = audit_axioms(diagnostics)
    assert olean.stat().st_size > 0
    REPORT.update(status='P13_CONDITIONAL_OVERLAP_BOUND_KERNEL_CHECKED', axioms=results,
                  source_sha256=source_sha, olean_bytes=olean.stat().st_size,
                  olean_sha256=hashlib.sha256(olean.read_bytes()).hexdigest())
    guard.thermal()
    print('P13_CONDITIONAL_OVERLAP_BOUND_KERNEL_CHECKED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        if '--prepare' not in sys.argv[2:]:
            guard.save()
