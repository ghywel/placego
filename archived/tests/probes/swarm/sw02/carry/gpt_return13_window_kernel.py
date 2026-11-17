#!/usr/bin/env python3
"""Check the exact window coverage implication with factor exclusions as hypotheses."""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import signal
import sys

from gpt_return13_coverage import native_checks, write_cnf
from gpt_return13_kernel_factor import emit, emit_table, formula_bounds
from gpt_return13_lrat import audit_rup, literal_mask
from gpt_return13_pack_factor import replay
from gpt_return13_prefix_control import write_proof
from gpt_return13_prefix_leaves import OUT, REPORT, guard, pin, read_cnf


STRIP_CLAUSES = 5044
WIDTH = 16


def digest(data):
    return hashlib.sha256(data).hexdigest()


def word_value(word):
    return int(word[::-1], 2)


def signed_blocker(shift, width, value):
    return [(shift + j + 1) * (-1 if value >> j & 1 else 1) for j in range(width)]


def window_literal(literal):
    magnitude = abs(literal)
    if not 7 <= magnitude <= 22:
        raise ValueError('LITERAL_OUTSIDE_WINDOW')
    return (magnitude - 6) * (1 if literal > 0 else -1)


def cut_proof(data, first):
    proof = []
    for expected, row in enumerate(data.decode().splitlines(), first):
        index, *rest = map(int, row.split())
        split = rest.index(0)
        clause, hints = rest[:split], rest[split+1:-1]
        assert index == expected and rest[-1] == 0
        if not 1 <= len(hints) <= 2 or not all(STRIP_CLAUSES < h < index for h in hints):
            raise ValueError('HINT_OUTSIDE_WINDOW_PROOF')
        proof.append((index - STRIP_CLAUSES, [window_literal(lit) for lit in clause],
                      [h - STRIP_CLAUSES for h in hints]))
    assert len(proof) == 2931 and proof[-1][1] == []
    return proof


def require_blockers(clauses, retained, occurrences, factors):
    expected = [signed_blocker(0, WIDTH, value) for value in retained]
    expected.extend(signed_blocker(shift, *factors[index]) for shift, index in occurrences)
    if clauses != expected:
        raise ValueError('WINDOW_BLOCKER_MISMATCH')


def require_rejection(action, reason):
    try:
        action()
    except ValueError as error:
        assert str(error) == reason
    else:
        raise AssertionError(f'NEGATIVE_CONTROL_ACCEPTED: {reason}')


def lean_list(pairs):
    return '[' + ', '.join(f'({a}, {b})' for a, b in pairs) + ']'


def emit_window(clauses, packed, retained, occurrences, factors, lemmas):
    source, marker, _ = emit({'initial_clauses': clauses}, packed).decode().partition('end P13PackedControl')
    assert marker
    lines = [source.replace('namespace P13PackedControl', 'namespace P13WindowCoverage')]
    for name, values in zip(('factorWidth', 'factorValue'), zip(*factors)):
        table = list(emit_table(name, values, 32))
        lines.extend(table[:-1])
        lines.append(table[-1].removeprefix('private '))
    lines.append(lemmas.decode())
    retained_parts, occurrence_parts, bridges, bounds = [], [], [], []
    for i, (start, end) in enumerate(formula_bounds(len(clauses))):
        words = retained[start:end]
        entries = occurrences[max(0, start-len(retained)):max(0, end-len(retained))]
        sides = []
        if words:
            label = f'retained{i}'
            retained_parts.append(label)
            lines.append(f'private def {label} : List Nat := {words}')
            sides.append(f'{label}.map (blocker 0 16)')
        if entries:
            label = f'occurrences{i}'
            occurrence_parts.append(label)
            lines.append(f'private def {label} : List (Nat × Nat) := {lean_list(entries)}')
            sides.append(f'{label}.map occurrenceBlocker')
            bound = f'indices{i}'
            bounds.append(bound)
            lines.append(f'private theorem {bound} : {label}.all (fun e => decide (e.2 < {len(factors)})) = true := by decide +kernel')
        bridge = f'bridge{i}'
        bridges.append(bridge)
        lines.append(f'private theorem {bridge} : formulaPart{i} = {" ++ ".join(sides)} := by decide +kernel')
    lines.extend([
        'def retained : List Nat := ' + ' ++ '.join(retained_parts),
        'private def occurrences : List (Nat × Nat) := ' + ' ++ '.join(occurrence_parts),
        'private theorem formula_bridge :',
        '    formula = retained.map (blocker 0 16) ++ occurrences.map occurrenceBlocker := by',
        '  simp only [formula, retained, occurrences, List.map_append, List.append_assoc,',
        '    ' + ', '.join(bridges) + ']',
        f'private theorem indices_ok : occurrences.all (fun e => decide (e.2 < {len(factors)})) = true := by',
        '  simp only [occurrences, List.all_append, Bool.true_and, ' + ', '.join(bounds) + ']',
        '',
        'theorem window_coverage (x : Int → Bool) (origin : Int)',
        f'    (hexclude : ∀ i < {len(factors)}, ∀ o : Int, ¬ Matches x o (factorWidth i) (factorValue i)) :',
        '    ∃ s ∈ retained, Matches x origin 16 s := by',
        '  classical',
        '  apply Classical.byContradiction',
        '  intro hnot',
        '  apply unsat (fun j => x (origin + (j : Int)))',
        '  intro c hc',
        '  rw [formula_bridge] at hc',
        '  rcases List.mem_append.mp hc with hret | hocc',
        '  · rcases List.mem_map.mp hret with ⟨s, hs, rfl⟩',
        '    have hmiss : ¬ Matches x origin 16 s := fun hm => hnot ⟨s, hs, hm⟩',
        '    exact blocker_models x origin (by simpa using hmiss)',
        '  · rcases List.mem_map.mp hocc with ⟨e, he, rfl⟩',
        '    have hi := of_decide_eq_true (List.all_eq_true.mp indices_ok e he)',
        '    exact blocker_models x origin (hexclude e.2 hi (origin + (e.1 : Int)))',
        '',
        'end P13WindowCoverage',
        '',
        '#print axioms P13WindowCoverage.window_coverage',
        '',
    ])
    return '\n'.join(lines).encode()


def prepare(plan):
    source = Path(os.environ['RETURN13_COVERAGE_ROOT'])
    original = pin(source/'coverage.cnf', plan['coverage_cnf_sha256'])
    raw_proof = pin(source/'coverage.lrat', plan['coverage_lrat_sha256'])
    variables, clauses = read_cnf(original)
    assert (variables, len(clauses)) == (910, 6260)
    clauses = [[window_literal(lit) for lit in clause] for clause in clauses[STRIP_CLAUSES:]]
    manifest = json.loads(pin(os.environ['RETURN13_SELECTION'], plan['manifest_sha256']))
    projection = json.loads(pin(os.environ['RETURN13_PROJECTION'], plan['projection_sha256']))
    retained = projection['target']['words']
    words = sorted(manifest['proofs'])
    factors = [(len(word), word_value(word)) for word in words]
    indices = {word: i for i, word in enumerate(words)}
    occurrences = [(entry['shift'], indices[entry['factor']]) for entry in manifest['selected']]
    assert (len(retained), len(occurrences), len(factors)) == (170, 1046, 141)
    assert all(shift + factors[index][0] <= WIDTH for shift, index in occurrences)
    require_blockers(clauses, retained, occurrences, factors)
    wrong_shift = [(occurrences[0][0] + 1, occurrences[0][1]), *occurrences[1:]]
    require_rejection(lambda: require_blockers(clauses, retained, wrong_shift, factors),
                      'WINDOW_BLOCKER_MISMATCH')
    first = STRIP_CLAUSES + len(clauses) + 1
    proof = cut_proof(raw_proof, first)
    row, rest = raw_proof.split(b'\n', 1)
    prefix, hints = row.split(b' 0 ', 1)
    mutated = prefix + b' 0 5044 ' + hints.split(b' ', 1)[1] + b'\n' + rest
    require_rejection(lambda: cut_proof(mutated, first), 'HINT_OUTSIDE_WINDOW_PROOF')
    assert {h for _, _, hints in proof for h in hints if h <= len(clauses)} == set(range(1, len(clauses)+1))
    cnf, lrat = OUT/'window-cut.cnf', OUT/'window-cut.lrat'
    write_cnf(cnf, WIDTH, clauses)
    write_proof(lrat, proof)
    audit = audit_rup(cnf, lrat)
    assert audit['packable'] and audit['used_additions'] == len(proof), audit
    packed = json.loads((OUT/'packed-rup.json').read_bytes())
    masks = [int(mask, 16) for mask in packed['masks_hex']]
    steps = [int(step, 16) for step in packed['steps_hex']]
    assert masks[:len(clauses)] == [literal_mask(clause) for clause in clauses]
    assert replay(masks, steps, len(clauses))
    assert not replay(masks, [*steps[:-1], (steps[-1] & ~0x3fff) | (len(masks)-1)], len(clauses))
    lemma = plan['lemma_source']
    generated = emit_window(clauses, packed, retained, occurrences, factors,
                            pin(lemma['file'], lemma['sha256']))
    lean_file = OUT/'P13WindowCoverage.lean'
    lean_file.write_bytes(generated)
    REPORT.update(variables=WIDTH, retained=len(retained), occurrences=len(occurrences), factors=len(factors),
                  audit=audit, cnf_sha256=digest(cnf.read_bytes()), lrat_sha256=digest(lrat.read_bytes()),
                  source_sha256=digest(generated), source_bytes=len(generated),
                  controls=['strip hint', 'shifted blocker', 'forward conflict'])
    return cnf, lrat, lean_file


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
    if sys.argv[2:] == ['--prepare']:
        prepare(plan)
        (OUT/'solve.json').write_text(json.dumps(REPORT, indent=2)+'\n')
        return
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    cap = plan['limits']['worker_soft_cpu_s']
    resource.setrlimit(resource.RLIMIT_CPU, (cap if soft == resource.RLIM_INFINITY else min(cap, soft), hard))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    for path, sha in plan['native_checker_sha256'].items():
        pin(path, sha)
    lean = Path(os.environ['RETURN13_LEAN'])
    pin(lean, plan['lean_binary_sha256'])
    kit = Path(os.environ['RETURN13_KIT_OBJECT_ROOT'])
    for name, sha in plan['kit_objects'].items():
        pin(kit/name, sha)
    os.environ['LEAN_PATH'] = str(kit)
    os.environ['LEAN_NUM_THREADS'] = '1'
    _, version = guard.call('lean-version', [str(lean), '--version'], 2, 5, 0)
    assert version.strip() == plan['lean_version']
    cnf, lrat, lean_file = prepare(plan)
    for k in ('cnf_sha256', 'lrat_sha256', 'source_sha256'):
        assert REPORT[k] == plan['expected'][k], k
    native_checks('window-cut', cnf, lrat)
    olean = lean_file.with_suffix('.olean')
    limits = plan['limits']
    _, diagnostics = guard.call('coverage-kernel', [str(lean), '-j1', '-DElab.async=false', '-R', str(OUT),
                                                   '-o', str(olean), str(lean_file)],
                                limits['lean_child_cpu_s'], limits['lean_child_wall_s'], 0)
    line = re.fullmatch(r"'P13WindowCoverage\.window_coverage' depends on axioms: \[([^]]*)\]",
                        diagnostics.strip())
    assert line is not None and olean.stat().st_size > 0, diagnostics
    axioms = {item.strip() for item in line[1].split(',') if item.strip()}
    assert axioms <= {'propext', 'Classical.choice', 'Quot.sound'}, axioms
    REPORT.update(status='P13_CONDITIONAL_WINDOW_COVERAGE_KERNEL_CHECKED', axioms=sorted(axioms),
                  olean_bytes=olean.stat().st_size, olean_sha256=digest(olean.read_bytes()))
    guard.thermal()
    print('P13_CONDITIONAL_WINDOW_COVERAGE_KERNEL_CHECKED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        if '--prepare' not in sys.argv[2:]:
            guard.save()
