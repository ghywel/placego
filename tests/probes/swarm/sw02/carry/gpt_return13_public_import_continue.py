#!/usr/bin/env python3
"""Relay an already checked factor using Lean's explicit artifact mapping."""
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys

from gpt_return13_factor_module_smoke import audit_axioms
from gpt_return13_prefix_leaves import OUT, REPORT, guard, pin


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
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
    producer = Path(os.environ['RETURN13_MODULE_PRODUCER_ROOT'])
    receipt = json.loads(pin(producer/'solve.json', plan['producer_receipt_sha256']))
    assert receipt['status'] == 'P13_FACTOR_MODULE_PRODUCER_KERNEL_CHECKED'
    module = plan['module']
    name = f'{module}.olean'
    expected = plan['public_olean_sha256']
    assert receipt['module_outputs'][name]['sha256'] == expected
    public_root = OUT/'public-imports'
    public_root.mkdir()
    exported = public_root/name
    exported.write_bytes(pin(producer/name, expected))
    assert list(public_root.iterdir()) == [exported]
    consumer = OUT/'P13PublicImport.lean'
    consumer.write_bytes(pin(producer/consumer.name, plan['consumer_sha256']))
    setup = OUT/'public-import.setup.json'
    setup.write_text(json.dumps({'name':consumer.stem, 'isModule':True,
                                 'importArts':{module:[[str(exported)]]}}, indent=2)+'\n')
    os.environ['LEAN_PATH'] = str(kit)
    os.environ['LEAN_NUM_THREADS'] = '1'
    _, version = guard.call('lean-version', [str(lean), '--version'], 2, 5, 0)
    assert version.strip() == plan['lean_version']
    _, output = guard.call('explicit-public-consumer', [str(lean), '-j1', '-DElab.async=false',
                                                       f'--setup={setup}', '-R', str(OUT), str(consumer)],
                           plan['limits']['consumer_cpu_s'], plan['limits']['consumer_wall_s'], 0)
    axioms = audit_axioms(output, 'P13PublicImport.excluded')
    assert axioms == receipt['axioms']
    REPORT.update(status='P13_FACTOR_MODULE_EXPLICIT_PUBLIC_IMPORT_KERNEL_CHECKED', axioms=axioms,
                  module=module, public_bytes=exported.stat().st_size, public_sha256=expected,
                  setup_sha256=hashlib.sha256(setup.read_bytes()).hexdigest(),
                  consumer_sha256=plan['consumer_sha256'])
    guard.thermal()
    print('P13_FACTOR_MODULE_EXPLICIT_PUBLIC_IMPORT_KERNEL_CHECKED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
