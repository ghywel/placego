#!/usr/bin/env python3
"""GC2437: one exact remaining gap, alignment(5,1), cut43/T148/Q-11.

Encoder-only stage. Predict gate/model/entry controls and byte limits pass.
No solver, other gap, cut scan, horizon extension or random tail.
"""
import hashlib
import importlib.util
import json
import os
import re
from pathlib import Path


def load(name, path, expected):
    p = Path(path)
    assert hashlib.sha256(p.read_bytes()).hexdigest() == expected
    spec = importlib.util.spec_from_file_location(name, p)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    out = Path(os.environ['CAPPED_OUT'])
    m = load('encoder', 'tests/probes/ether_tail_cnf.py',
             '0a0ab05fab78bfd99941e5574c7488f30e212ecdae36afb088a527a03ff18425')
    base = load('base', 'tests/probes/ether_adaptive_shield.py',
                'f1fccc493af4fe3538a89b3dcc8d12d7f56f9279b5074afb5b197afa210ee85a')
    raw = Path('tests/probes/lean/EtherEdgeZero.lean').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == base.ENTRY_HASH
    assert re.search(r'theorem entry_5_1 : checkEntry 5 1 148 \(-24\) = true', raw.decode())
    eraw = Path(os.environ['ETHER_KIT_SOURCE']).read_bytes()
    assert hashlib.sha256(eraw).hexdigest() == base.ETHER_HASH
    walls = set()
    text = eraw.decode().split('def wallStates :', 1)[1].split('theorem', 1)[0]
    for phase, values in re.findall(r'\((\d), \[([a-z, ]+)\]\)', text):
        walls.add((int(phase), tuple(int(v.strip() == 'true') for v in values.split(','))))
    assert len(walls) == 109
    initial = lambda x: base.TABLE[(x+5)%7][1] if x < 0 else int(x == 0)
    cone = m.Cone(-252, 137, 148, 43, initial)
    assert (cone.nv, len(cone.fixed), len(cone.target), cone.count()) == (36058, 296, 94, 214305)
    original = out/'gap43.cnf'
    report = {'status': 'STARTED', 'solver_run': False, 'entry': [5, 1, 148, -24, -11],
              'original': cone.write(original), 'controls': {}}
    def save():
        (out/'gap-encoder.json').write_text(json.dumps(report, indent=2)+'\n')
    save()
    # Protected control is exactly original body plus18 fixed-input units.
    units = b''.join(f'-{cone.var(0,x)} 0\n'.encode() for x in range(44, 62))
    header = f'p cnf {cone.nv} {cone.count()+18}\n'.encode()
    protected = out/'gap61.cnf'
    with original.open('rb') as f:
        original_header = f.readline()
        body = f.read()
    data = header+body+units
    assert len(data) < 16 << 20
    protected.write_bytes(data)
    assert protected.read_bytes().split(b'\n', 1)[1] == original.read_bytes().split(b'\n', 1)[1]+units
    report['protected'] = {'variables': cone.nv, 'clauses': cone.count()+18,
                            'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
    # Exact baseline entry in the known cone; the infinite-left part uses carried A1.
    ref = cone.reference
    phi = (148+1) % 4
    wall = tuple(ref[cone.var(148, x)] for x in range(-23, -10))
    assert (phi, wall) in walls
    assert all(ref[cone.var(148, x)] == base.TABLE[(x+5)%7][phi] for x in range(-104, -23))
    assert wall != tuple(base.TABLE[(x+5)%7][phi] for x in range(-23, -10))
    cone.packed_control(ref)
    assert m.disk_unsatisfied(original, ref) == [cone.count()]
    assert m.disk_unsatisfied(protected, ref) == [cone.count()]
    (out/'baseline.bits').write_bytes(ref)
    report['controls']['baseline_only_goal_fails'] = True
    # Named lower witness: valid under cut42, deliberately NOT under original cut43.
    lower = cone.scalar_model({43: 1})
    cone.packed_control(lower)
    changed = [x for x in range(-104, -10) if lower[cone.var(148,x)] != ref[cone.var(148,x)]]
    assert changed
    assert m.disk_unsatisfied(original, lower) == [cone.count()-1]
    assert m.disk_unsatisfied(protected, lower) == [cone.count()-1]
    (out/'flip43-under-cut42.bits').write_bytes(lower)
    report['controls']['lower_witness'] = {'flip': 43, 'initial_agreement_through': 42,
        'changed_targets': changed, 'only_original_input43_unit_fails': True,
        'sha256': hashlib.sha256(lower).hexdigest()}
    bad = ref[:]
    bad[cone.var(1, -251)] ^= 1
    assert any(k <= 6*(cone.nv-cone.widths[0]) for k in m.disk_unsatisfied(original,bad))
    report['controls']['corrupt_gate_rejected'] = True
    inp = Path(os.environ['TAIL_REFERENCE_INPUT'])
    for name, expected in [('010.cnf', 'ad4f2afcfaad0c7d46f277c3d46dff23184ef504d84f968b294e77d519c0ae4e'),
                           ('110-gap.cnf', 'e78928354d3e7d5fd4f013404867a2dcbe69e730616201c85a9ab6a21ef60250')]:
        data = (inp/name).read_bytes()
        assert hashlib.sha256(data).hexdigest() == expected
        (out/name).write_bytes(data)
    report['controls']['known_micro_cnfs_byte_exact'] = True
    report['status'] = 'GAP_ENCODER_CONTROLS_PASS'
    save()
    print(json.dumps(report))


if __name__ == '__main__':
    main()
