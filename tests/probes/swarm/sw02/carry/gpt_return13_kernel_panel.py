#!/usr/bin/env python3
"""Build exact whole-line exclusions from pinned canonical P13 discharges."""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import signal
import sys

from gpt_return13_bridge_only import emit_bridge
from gpt_return13_coverage import write_cnf
from gpt_return13_join_kernel_factor import join_source
from gpt_return13_lrat import audit_rup, literal_mask
from gpt_return13_pack_factor import compact_factor, replay
from gpt_return13_prefix_control import write_proof
from gpt_return13_prefix_leaves import OUT, REPORT, guard, pin, read_cnf
from gpt_return13_prefix_replay import read_proof


def digest(data):
    return hashlib.sha256(data).hexdigest()


def prepare_factor(spec, manifest, base, gate):
    factor = spec['word']
    width = len(factor)
    value = sum((bit == '1') << i for i, bit in enumerate(factor))
    source = manifest['proofs'][factor]
    data = pin(Path(os.environ['RETURN13_SOURCE_ROOT'])/source['file'], source['sha256'])
    derivation = read_proof(data, base, factor)
    assert len(derivation) == source['steps']
    supported, initial, proof = compact_factor(base, derivation, factor)
    assert initial[:len(supported)] == [base[index - 1] for index in supported]
    units = [[(i + 7) * (1 if (value >> i) & 1 else -1)] for i in range(width)]
    assert initial[len(supported):] == units
    assert derivation[-1][1] == [-unit[0] for unit in units]

    work = OUT/f'packing-{factor}'
    work.mkdir()
    cnf, lrat, packed_path = (work/file for file in ('factor.cnf', 'factor.lrat', 'packed.json'))
    write_cnf(cnf, 910, initial)
    write_proof(lrat, proof)
    audit = audit_rup(cnf, lrat, packed_path)
    assert audit['packable'] and audit['used_additions'] == len(derivation) + 1, audit
    packed = json.loads(packed_path.read_bytes())
    masks = [int(mask, 16) for mask in packed['masks_hex']]
    steps = [int(step, 16) for step in packed['steps_hex']]
    assert masks[:len(initial)] == [literal_mask(clause) for clause in initial]
    assert replay(masks, steps, len(initial))
    bad_conflict = len(masks) - 1
    assert bad_conflict < 2**14
    assert not replay(masks, [*steps[:-1], (steps[-1] & ~0x3fff) | bad_conflict], len(initial))
    assert not replay([*masks[:-1], 1], steps, len(initial))

    premises = {'factor': factor, 'base_clause_ids': supported, 'initial_clauses': initial}
    bridge = emit_bridge(premises, packed, gate)
    namespace = f'P13Factor{factor}'
    generated = join_source(premises, packed, bridge, namespace)
    assert f'¬ Matches x origin {width} {value} :='.encode() in generated
    assert f'(List.range {width}).map (fun i => [mkLit (vid 65 0 (6+i)) (({value} : Nat).testBit i)])'.encode() in generated
    lean_file = OUT/f'{namespace}.lean'
    lean_file.write_bytes(generated)
    result = {
        'word': factor, 'lean_width': width, 'lean_value': value, 'base_clauses': len(supported),
        'lrup_additions': audit['used_additions'], 'source_bytes': len(generated),
        'source_sha256': digest(generated), 'negative_controls': ['forward conflict hint', 'nonempty goal'],
    }
    return lean_file, result


def check_factor(plan, spec, lean, lean_file, result):
    assert result['source_sha256'] == spec['source_sha256'], result
    namespace = lean_file.stem
    olean = lean_file.with_suffix('.olean')
    limits = plan['limits']
    _, diagnostics = guard.call(
        namespace, [str(lean), '-j1', '-DElab.async=false', '-R', str(OUT),
                    '-o', str(olean), str(lean_file)],
        limits['lean_child_cpu_s'], limits['lean_child_wall_s'], 0,
    )
    axiom_line = re.fullmatch(rf"'{namespace}\.factor_excluded' depends on axioms: \[([^]]*)\]",
                             diagnostics.strip())
    assert axiom_line is not None and olean.stat().st_size > 0, diagnostics
    axioms = {item.strip() for item in axiom_line[1].split(',') if item.strip()}
    assert axioms <= {'propext', 'Classical.choice', 'Quot.sound'}, axioms
    result.update(axioms=sorted(axioms), olean_sha256=digest(olean.read_bytes()),
                  olean_bytes=olean.stat().st_size)
    guard.thermal()


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
    prepare_only = sys.argv[2:] == ['--prepare']
    if not prepare_only:
        soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
        worker_cap = plan['limits']['worker_soft_cpu_s']
        resource.setrlimit(resource.RLIMIT_CPU, (worker_cap if soft == resource.RLIM_INFINITY
                                                else min(worker_cap, soft), hard))
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
    manifest = json.loads(pin(os.environ['RETURN13_SELECTION'], plan['manifest_sha256']))
    variables, clauses = read_cnf(pin(os.environ['RETURN13_ORIGINAL_CNF'], plan['original_cnf_sha256']))
    assert (variables, len(clauses)) == (910, 5214)
    gate_spec = plan['gate_source']
    gate = pin(gate_spec['file'], gate_spec['sha256'])
    results = []
    REPORT['factors'] = results
    for spec in plan['factors']:
        lean_file, result = prepare_factor(spec, manifest, clauses[:5044], gate)
        results.append(result)
        if not prepare_only:
            check_factor(plan, spec, lean, lean_file, result)
            guard.save()
    REPORT['status'] = 'PREPARED' if prepare_only else 'P13_FACTOR_PANEL_KERNEL_CHECKED'
    if prepare_only:
        (OUT/'solve.json').write_text(json.dumps(REPORT, indent=2)+'\n')
    else:
        print('P13_FACTOR_PANEL_KERNEL_CHECKED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        if '--prepare' not in sys.argv[2:]:
            guard.save()
