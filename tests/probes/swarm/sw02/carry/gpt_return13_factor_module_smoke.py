#!/usr/bin/env python3
"""Check a new factor as a Lean module and import only its public object."""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import signal
import sys

from gpt_return13_kernel_panel import prepare_factor
from gpt_return13_prefix_leaves import OUT, REPORT, guard, pin, read_cnf


def digest(data):
    return hashlib.sha256(data).hexdigest()


def prepare(plan):
    manifest = json.loads(pin(os.environ['RETURN13_SELECTION'], plan['manifest_sha256']))
    variables, clauses = read_cnf(pin(os.environ['RETURN13_ORIGINAL_CNF'], plan['original_cnf_sha256']))
    assert (variables, len(clauses)) == (910, 5214)
    gate_spec = plan['gate_source']
    gate = pin(gate_spec['file'], gate_spec['sha256'])
    factor = plan['factor']
    source, result = prepare_factor(factor, manifest, clauses[:5044], gate)
    assert result['source_sha256'] == factor['source_sha256']
    original = source.read_bytes()
    decl = b'\ntheorem factor_excluded ('
    assert original.startswith(b'import ') and original.count(decl) == 1
    module_source = b'module\n\npublic ' + original.replace(decl, b'\npublic theorem factor_excluded (', 1)
    source.write_bytes(module_source)
    consumer = OUT/'consumer'/'P13PublicImport.lean'
    consumer.parent.mkdir()
    consumer.write_text(f'''module

public import {source.stem}

open Ruliology.CellularAutomata.Rule30MovingStrip
open Ruliology.CellularAutomata.Rule30RingOrbits

public theorem P13PublicImport.excluded (x : Int → Bool) (hx : orbit x 13 = x) (o : Int) :
    ¬ Matches x o {result['lean_width']} {result['lean_value']} :=
  {source.stem}.factor_excluded x hx o

#print axioms P13PublicImport.excluded
''')
    return source, consumer, result


def audit_axioms(output, theorem):
    line = re.fullmatch(rf"'{re.escape(theorem)}' depends on axioms: \[([^]]*)\]", output.strip())
    assert line is not None, output
    axioms = {item.strip() for item in line[1].split(',') if item.strip()}
    assert axioms <= {'propext', 'Classical.choice', 'Quot.sound'}, axioms
    return sorted(axioms)


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
    if sys.argv[2:] == ['--prepare']:
        source, consumer, result = prepare(plan)
        print(json.dumps(dict(result, module_sha256=digest(source.read_bytes()),
                              consumer_sha256=digest(consumer.read_bytes())), indent=2))
        return
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    limits = plan['limits']
    cap = limits['worker_soft_cpu_s']
    resource.setrlimit(resource.RLIMIT_CPU, (cap if soft == resource.RLIM_INFINITY
                                            else min(cap, soft), hard))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    lean = Path(os.environ['RETURN13_LEAN'])
    pin(lean, plan['lean_binary_sha256'])
    kit = Path(os.environ['RETURN13_KIT_OBJECT_ROOT'])
    for name, sha in plan['kit_objects'].items():
        pin(kit/name, sha)
    os.environ['LEAN_PATH'] = str(kit)
    os.environ['LEAN_NUM_THREADS'] = '1'
    _, version = guard.call('lean-version', [str(lean), '--version'], 2, 5, 0)
    assert version.strip() == plan['lean_version']
    source, consumer, result = prepare(plan)
    assert digest(source.read_bytes()) == plan['module_sha256']
    assert digest(consumer.read_bytes()) == plan['consumer_sha256']
    module = source.stem
    public = source.with_suffix('.olean')
    command = [str(lean), '-j1', '-DElab.async=false']
    _, output = guard.call('module-producer', [*command, '-R', str(OUT), '-o', str(public), str(source)],
                           limits['producer_cpu_s'], limits['producer_wall_s'], 0)
    axioms = audit_axioms(output, f'{module}.factor_excluded')
    private = public.with_suffix('.olean.private')
    assert private.stat().st_size > 0 and 0 < public.stat().st_size < private.stat().st_size
    REPORT.update(status='P13_FACTOR_MODULE_PRODUCER_KERNEL_CHECKED', factor=result, axioms=axioms,
                  module_sha256=plan['module_sha256'], consumer_sha256=plan['consumer_sha256'],
                  module_outputs={p.name:{'bytes':p.stat().st_size,'sha256':digest(p.read_bytes())}
                                  for p in sorted(OUT.glob(f'{module}.*'))})
    guard.save()

    public_root = OUT/'public-imports'
    public_root.mkdir()
    exported = public_root/public.name
    exported.write_bytes(public.read_bytes())
    assert list(public_root.iterdir()) == [exported]
    os.environ['LEAN_PATH'] = os.pathsep.join(map(str, (kit, public_root)))
    _, deps = guard.call('public-import-deps', [str(lean), '--deps', '-R', str(consumer.parent),
                                                str(consumer)], 3, 8, 0)
    assert str(exported) in deps.splitlines(), deps
    _, output = guard.call('public-consumer', [*command, '-R', str(consumer.parent), str(consumer)],
                           limits['consumer_cpu_s'], limits['consumer_wall_s'], 0)
    assert audit_axioms(output, 'P13PublicImport.excluded') == axioms
    (OUT/'P13PublicImport.lean').write_bytes(consumer.read_bytes())
    REPORT.update(status='P13_FACTOR_MODULE_PUBLIC_IMPORT_KERNEL_CHECKED')
    guard.thermal()
    print('P13_FACTOR_MODULE_PUBLIC_IMPORT_KERNEL_CHECKED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        if '--prepare' not in sys.argv[2:]:
            guard.save()
