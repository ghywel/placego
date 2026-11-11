#!/usr/bin/env python3
"""Check a dense P13 certificate with its whole-line Rule 30 interpretation."""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import signal
import sys

from gpt_return13_kernel_factor import emit, emit_table, read_inputs
from gpt_return13_pack_factor import replay
from gpt_return13_prefix_leaves import OUT, REPORT, guard, pin


def rename_mask(mask, variables):
    result = 0
    while mask:
        bit = mask & -mask
        literal = bit.bit_length() - 1
        result |= 1 << (2 * variables[literal // 2] + literal % 2)
        mask ^= bit
    return result


def rename_step(word, variables):
    result = word & 0xffffff
    count = (word >> 14) & 0x3ff
    for j in range(count):
        offset = 24 + 25*j
        hint = (word >> offset) & 0x3fff
        literal = (word >> (offset + 14)) & 0x7ff
        result |= (hint | ((2*variables[literal//2] + literal%2) << 14)) << offset
    assert word >> (24 + 25*count) == 0
    return result


def dense_inputs(premises, packed):
    masks = [int(value, 16) for value in packed['masks_hex']]
    steps = [int(value, 16) for value in packed['steps_hex']]
    used = 0
    for mask in masks:
        used |= mask
    old = [v for v in range((used.bit_length()+1)//2) if used >> (2*v) & 3]
    new = {v: j for j, v in enumerate(old)}
    assert 0 < len(old) <= 2**10
    dense_masks = [rename_mask(mask, new) for mask in masks]
    dense_steps = [rename_step(step, new) for step in steps]
    assert [rename_mask(mask, old) for mask in dense_masks] == masks
    assert [rename_step(step, old) for step in dense_steps] == steps
    assert replay(dense_masks, dense_steps, len(premises['initial_clauses']))
    dense_clauses = [[(new[abs(literal)-1] + 1) * (1 if literal>0 else -1) for literal in clause]
                     for clause in premises['initial_clauses']]
    assert [[(old[abs(literal)-1] + 1) * (1 if literal>0 else -1) for literal in clause]
            for clause in dense_clauses] == premises['initial_clauses']
    return old, {'initial_clauses': dense_clauses}, {
        'masks_hex': [hex(mask) for mask in dense_masks], 'steps_hex': [hex(step) for step in dense_steps]}


def bridge(old, ids, factor='0110000'):
    width = len(factor)
    value = int(factor[::-1], 2)
    lines = [*emit_table('oldVar', old, 32),
             'open Ruliology.CellularAutomata.Rule30RingOrbits',
             'private def restoreLit (l : Nat) : Nat := 2 * oldVar (l / 2) + l % 2',
             'private def stripBase : List (List Nat) := transitionFormula 13 65 ++ periodFormula 13 65 65',
             'private def baseArray : Array (List Nat) := stripBase.toArray',
             'private def selectBase (i : Nat) : List Nat := (baseArray[i]?).getD []',
             'private def cube : List (List Nat) :=',
             f'  (List.range {width}).map (fun i => [mkLit (vid 65 0 (6+i)) (({value} : Nat).testBit i)])']
    parts, checks = [], []
    for start in range(0, len(ids), 32):
        label = f'indices{len(parts)}'
        part = f'formulaPart{len(parts)}'
        check = f'liftPart{len(parts)}'
        parts.append(label)
        checks.append(check)
        rhs = f'{label}.map selectBase' + (' ++ cube' if start+32 >= len(ids) else '')
        lines.extend([f'private def {label} : List Nat := {ids[start:start+32]}',
                      f'private theorem {check} : {part}.map (List.map restoreLit) = {rhs} := by decide +kernel'])
    lines.extend(['private def supportIds : List Nat := ' + ' ++ '.join(parts),
                  'private theorem formula_bridge :',
                  '    formula.map (List.map restoreLit) = supportIds.map selectBase ++ cube := by',
                  '  simp only [formula, supportIds, List.map_append, List.append_assoc,',
                  '    ' + ', '.join(checks) + ']'])
    proof = '''private theorem stripLength : stripBase.length = 5044 := by decide +kernel
private theorem indices_ok : supportIds.all (fun i => decide (i < 5044)) = true := by decide +kernel

private theorem selectBase_mem {i : Nat} (hi : i < 5044) : selectBase i ∈ stripBase := by
  have hib : i < stripBase.length := by simpa only [stripLength] using hi
  have hget : stripBase[i]? = some stripBase[i] := getElem?_eq_getElem hib
  apply List.mem_of_getElem? (i := i)
  simp only [selectBase, baseArray, List.getElem?_toArray, hget, Option.getD_some]

private theorem models_pullback (a : Nat → Bool) (c : List Nat)
    (h : Models a (c.map restoreLit)) : Models (fun v => a (oldVar v)) c := by
  rcases h with ⟨l', hl', hv⟩
  rcases List.mem_map.mp hl' with ⟨l, hl, rfl⟩
  refine ⟨l, hl, ?_⟩
  have hd : (2 * oldVar (l/2) + l%2) / 2 = oldVar (l/2) := by omega
  have hm : (2 * oldVar (l/2) + l%2) % 2 = l%2 := by omega
  simpa only [Lit, restoreLit, hd, hm] using hv

private theorem cube_models (x : Int → Bool) (origin : Int) (h : Matches x origin WIDTH VALUE) :
    ∀ c ∈ cube, Models (assignment 65 x (origin-6)) c := by
  intro c hc
  rcases List.mem_map.mp hc with ⟨j, hj, rfl⟩
  have hj7 : j < WIDTH := List.mem_range.mp hj
  refine ⟨_, List.mem_cons_self, (lit_mk _ _ _).mpr ?_⟩
  rw [assignment_variable (by decide) x (origin-6) 0 (6+j) (by omega)]
  have he : origin - 6 + ((6+j : Nat) : Int) = origin + j := by omega
  simpa only [orbit, he] using h j hj7

theorem factor_excluded (x : Int → Bool) (hx : orbit x 13 = x) (origin : Int) :
    ¬ Matches x origin WIDTH VALUE := by
  intro hm
  let a := assignment 65 x (origin-6)
  apply unsat (fun v => a (oldVar v))
  intro c hc
  apply models_pullback
  have hmem : c.map restoreLit ∈ supportIds.map selectBase ++ cube := by
    rw [← formula_bridge]
    exact List.mem_map.mpr ⟨c, hc, rfl⟩
  rcases List.mem_append.mp hmem with hbase | hcube
  · rcases List.mem_map.mp hbase with ⟨i, hi, he⟩
    rw [← he]
    have hib : i < 5044 := of_decide_eq_true (List.all_eq_true.mp indices_ok i hi)
    have hs := selectBase_mem hib
    rcases List.mem_append.mp hs with ht | hp
    · exact transition_models (by decide) x (origin-6) _ ht
    · exact period_models (by decide) (by decide) x hx (origin-6) _ hp
  · exact cube_models x origin hm _ hcube
'''
    lines.extend(proof.replace('WIDTH', str(width)).replace('VALUE', str(value)).splitlines())
    return '\n'.join(lines)


def emit_dense(premises, packed):
    old, compact_premises, compact_packed = dense_inputs(premises, packed)
    base_source = emit(compact_premises, compact_packed).decode()
    base_source, _, _ = base_source.partition('end P13PackedControl')
    base_source = base_source.replace('namespace P13PackedControl', 'namespace P13DenseControl')
    assert premises['factor'] == '0110000' and len(premises['base_clause_ids']) == 1388 and len(old) == 338
    source = base_source + bridge(old, [i-1 for i in premises['base_clause_ids']]) + '\n'
    source += '\nend P13DenseControl\n\n#print axioms P13DenseControl.factor_excluded\n'
    return source.encode(), compact_packed


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
    source, packed = emit_dense(*read_inputs(plan))
    assert hashlib.sha256(source).hexdigest() == plan['generated_source_sha256']
    lean_file = OUT/'P13DenseControl.lean'
    lean_file.write_bytes(source)
    _, diagnostics = guard.call('dense-kernel', [str(lean), '-j1', '-DElab.async=false', '-R', str(OUT),
                                                 str(lean_file)], 85, 180, 0)
    statement = re.fullmatch(r"'P13DenseControl\.factor_excluded' depends on axioms: \[([^]]*)\]", diagnostics.strip())
    assert statement is not None, diagnostics
    axioms = {item.strip() for item in statement[1].split(',') if item.strip()}
    assert axioms <= {'propext', 'Classical.choice', 'Quot.sound'}, axioms
    REPORT.update(status='DENSE_WHOLE_LINE_FACTOR_KERNEL_CHECKED', generated_source_sha256=plan['generated_source_sha256'],
                  axioms=sorted(axioms), factor='0110000', distinct_variables=338,
                  mask_characters=sum(map(len, packed['masks_hex'])))
    guard.thermal()
    guard.save()
    print('RETURN13_DENSE_KERNEL_FACTOR_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
