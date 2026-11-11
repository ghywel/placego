#!/usr/bin/env python3
"""Kernel-check only the P13 premise bridge, using arithmetic gate lookup."""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import signal
import sys

from gpt_return13_dense_kernel_factor import bridge, dense_inputs
from gpt_return13_kernel_factor import formula_bounds, read_inputs
from gpt_return13_prefix_leaves import OUT, REPORT, guard, pin


def emit_bridge(premises, packed, gate_source):
    old, compact, _ = dense_inputs(premises, packed)
    factor = premises['factor']
    initial = [[2*(abs(literal)-1)+int(literal > 0) for literal in clause]
               for clause in compact['initial_clauses']]
    ranges = formula_bounds(len(initial), len(factor))
    labels = [f'formulaPart{i}' for i in range(len(ranges))]
    header = ['import Ruliology.CellularAutomata.Rule30MovingStrip', '',
              'namespace P13BridgeControl', '', 'open Ruliology.CellularAutomata.Rule30MovingStrip',
              'set_option maxRecDepth 1000000', 'set_option maxHeartbeats 0', '']
    for label, (start, end) in zip(labels, ranges):
        header.append(f'private def {label} : List (List Nat) := {initial[start:end]}')
    header.append('def formula : List (List Nat) := ' + ' ++ '.join(labels))
    body = bridge(old, [i-1 for i in premises['base_clause_ids']], factor)
    left = body.index('private def stripBase')
    right = body.index('private def cube')
    body = body[:left] + gate_source.decode() + '\n' + body[right:]
    left = body.index('private theorem stripLength')
    bounds = body.index('private theorem indices_ok', left)
    end = body.index('\n', bounds)
    right = body.index('private theorem models_pullback', end)
    body = body[:left] + body[bounds:end] + '\n\n' + body[right:]
    body = body.replace('private def restoreLit', 'private noncomputable def restoreLit')
    body = body.replace('  simpa only [Lit, restoreLit, hd, hm] using hv',
                        '  unfold Lit at hv ⊢\n  unfold restoreLit at hv\n  rw [hd, hm] at hv\n  exact hv')
    body = body.replace('theorem factor_excluded (x : Int → Bool)',
                        'theorem factor_excluded_of_unsat\n'
                        '    (hu : ∀ a : Nat → Bool, ¬ (∀ c ∈ formula, Models a c))\n'
                        '    (x : Int → Bool)')
    body = body.replace('apply unsat (fun v => a (oldVar v))', 'apply hu (fun v => a (oldVar v))')
    return ('\n'.join(header) + '\n' + body + '\n\nend P13BridgeControl\n\n'
            '#print axioms P13BridgeControl.factor_excluded_of_unsat\n').encode()


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (12 if soft == resource.RLIM_INFINITY else min(12, soft), hard))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    lean = Path(os.environ['RETURN13_LEAN'])
    pin(lean, plan['lean_binary_sha256'])
    kit_build = Path(os.environ['RETURN13_KIT_OBJECT_ROOT'])
    for name, sha in plan['kit_objects'].items():
        pin(kit_build/name, sha)
    os.environ['LEAN_PATH'] = str(kit_build)
    os.environ['LEAN_NUM_THREADS'] = '1'
    _, version = guard.call('lean-version', [str(lean), '--version'], 2, 5, 0)
    assert version.strip() == plan['lean_version']
    gate = plan['gate_source']
    source = emit_bridge(*read_inputs(plan), pin(gate['file'], gate['sha256']))
    assert hashlib.sha256(source).hexdigest() == plan['generated_source_sha256']
    lean_file = OUT/'P13BridgeControl.lean'
    lean_file.write_bytes(source)
    _, diagnostics = guard.call('bridge-kernel', [str(lean), '-j1', '-DElab.async=false', '-R', str(OUT),
                                                  str(lean_file)], 60, 125, 0)
    ax = re.fullmatch(r"'P13BridgeControl\.factor_excluded_of_unsat' depends on axioms: \[([^]]*)\]",
                      diagnostics.strip())
    assert ax is not None, diagnostics
    axioms = {item.strip() for item in ax[1].split(',') if item.strip()}
    assert axioms <= {'propext', 'Classical.choice', 'Quot.sound'}, axioms
    REPORT.update(status='DENSE_FACTOR_KIT_BRIDGE_KERNEL_CHECKED', generated_source_sha256=plan['generated_source_sha256'],
                  axioms=sorted(axioms), factor='0110000')
    guard.thermal()
    guard.save()
    print('RETURN13_BRIDGE_ONLY_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
