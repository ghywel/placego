#!/usr/bin/env python3
"""Emit and kernel-check one exact packed factor against the pinned core kit."""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import signal
import sys

from gpt_return13_prefix_leaves import OUT, REPORT, guard, pin


def branch_table(entries, first=0):
    if len(entries) == 1:
        return entries[0]
    middle = len(entries) // 2
    left = branch_table(entries[:middle], first)
    right = branch_table(entries[middle:], first + middle)
    return f'(branch (nat_lit {first + middle - 1}) {left} {right})'


def emit_table(name, values, chunk):
    groups = []
    for start in range(0, len(values), chunk):
        leaves = [f'(fun _ => nat_lit {value})' for value in values[start:start+chunk]]
        groups.append(f'{name}{len(groups)}')
        yield f'private noncomputable def {groups[-1]} : Nat → Nat := {branch_table(leaves, start)}'
    def group_table(labels, first):
        if len(labels) == 1:
            return labels[0]
        middle = len(labels) // 2
        return (f'(branch (nat_lit {(first+middle)*chunk-1}) '
                f'{group_table(labels[:middle], first)} {group_table(labels[middle:], first+middle)})')
    yield f'private noncomputable def {name} : Nat → Nat := {group_table(groups, 0)}'


def emit(premises, packed):
    initial = [[2*(abs(literal)-1)+int(literal > 0) for literal in clause]
               for clause in premises['initial_clauses']]
    masks, steps = packed['masks_hex'], packed['steps_hex']
    assert len(initial) == 1395 and len(masks) == 3582 and len(steps) == 2187
    assert int(masks[-1], 16) == 0
    lines = ['import Ruliology.CellularAutomata.Rule30MovingStrip', '',
             'namespace P13PackedControl', '', 'open Ruliology.CellularAutomata.Rule30MovingStrip',
             'set_option maxRecDepth 1000000', 'set_option maxHeartbeats 0', '']
    lines.extend(emit_table('getClause', masks, 32))
    lines.extend(emit_table('getStep', steps, 32))
    formulas = []
    for start in range(0, len(initial), 32):
        label = f'formulaPart{len(formulas)}'
        formulas.append(label)
        lines.append(f'private def {label} : List (List Nat) := {initial[start:start+32]}')
        lines.append(f'private theorem {label}_ok : checkFormula getClause {label} {start} = true := by decide +kernel')
    lines.append('def formula : List (List Nat) := ' + ' ++ '.join(formulas))
    lines.append('private theorem formula_ok : checkFormula getClause formula 0 = true := by')
    lines.append('  unfold formula')
    lines.extend(f'  apply checkFormula_append_ok {label}_ok' for label in formulas[:-1])
    lines.append(f'  exact {formulas[-1]}_ok')
    lines.append('private theorem formula_length : formula.length = 1395 := by decide +kernel')
    chunks = []
    for start in range(0, len(steps), 32):
        n = min(32, len(steps)-start)
        idx = len(initial) + start
        label = f'rup{len(chunks)}'
        chunks.append((label, n, idx, start))
        lines.append(f'private theorem {label} : replayPackedN getClause getStep {n} {idx} {start} = true := by decide +kernel')
    lines.append(f'private theorem nil_ok : Nat.beq (getClause {len(masks)-1}) 0 = true := by decide +kernel')
    lines.extend(['theorem unsat : ∀ a : Nat → Bool, ¬ (∀ c ∈ formula, Models a c) := by',
                  '  intro a ha',
                  '  have hk0 : Known getClause a 1395 := by',
                  '    rw [← formula_length]',
                  '    exact initial_known formula_ok ha'])
    for j, (label, n, idx, pos) in enumerate(chunks):
        lines.append(f'  have hk{j+1} : Known getClause a {idx+n} := replayPackedN_sound {n} {idx} {pos} hk{j} {label}')
    lines.extend([f'  exact unsat_of_known_nil nil_ok hk{len(chunks)}', '', 'end P13PackedControl',
                  '', '#print axioms P13PackedControl.unsat', ''])
    return '\n'.join(lines).encode()


def read_inputs(plan):
    source = Path(os.environ['RETURN13_PACKED_DIR'])
    files = [json.loads(pin(source/spec['file'], spec['sha256'])) for spec in plan['packed_inputs']]
    return files


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (12 if soft == resource.RLIM_INFINITY else min(12, soft), hard))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    lean = Path(os.environ['RETURN13_LEAN'])
    pin(lean, plan['lean_binary_sha256'])
    kit = Path(os.environ['RETURN13_KIT_ROOT'])/'lean'
    source_root, lib_root = OUT/'src', OUT/'lib'
    os.environ['LEAN_PATH'] = str(lib_root)
    os.environ['LEAN_NUM_THREADS'] = '1'
    _, version = guard.call('lean-version', [str(lean), '--version'], 2, 5, 0)
    assert version.strip() == plan['lean_version']
    source = emit(*read_inputs(plan))
    assert hashlib.sha256(source).hexdigest() == plan['generated_source_sha256']
    source_root.mkdir(exist_ok=True)
    packed_source = source_root/'P13PackedControl.lean'
    packed_source.write_bytes(source)
    for name, sha in plan['kit_sources'].items():
        relative = Path('Ruliology/CellularAutomata')/f'{name}.lean'
        local = source_root/relative
        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_bytes(pin(kit/relative, sha))
        olean = lib_root/relative.with_suffix('.olean')
        olean.parent.mkdir(parents=True, exist_ok=True)
        _, diagnostics = guard.call(name, [str(lean), '-j1', '-DElab.async=false', '-R', str(source_root),
                                           '-o', str(olean), str(local)], 20, 40, 0)
        assert not diagnostics.strip() and olean.stat().st_size > 0, diagnostics
    _, diagnostics = guard.call('packed-kernel', [str(lean), '-j1', '-DElab.async=false', '-R', str(source_root),
                                                  str(packed_source)], 75, 180, 0)
    statement = re.fullmatch(r"'P13PackedControl\.unsat' depends on axioms: \[([^]]*)\]", diagnostics.strip())
    assert statement is not None, diagnostics
    axioms = {item.strip() for item in statement[1].split(',') if item.strip()}
    assert axioms <= {'propext', 'Classical.choice', 'Quot.sound'}, axioms
    REPORT.update(status='EXACT_COMPACT_FACTOR_KERNEL_CHECKED', generated_source_sha256=plan['generated_source_sha256'],
                  axioms=sorted(axioms), kit_commit=plan['kit_commit'], factor='0110000')
    guard.thermal()
    guard.save()
    print('RETURN13_KERNEL_FACTOR_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
