#!/usr/bin/env python3
"""Join the packed dense factor with the checked arithmetic strip bridge."""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import signal
import sys

from gpt_return13_dense_kernel_factor import dense_inputs
from gpt_return13_kernel_factor import emit, read_inputs
from gpt_return13_prefix_leaves import OUT, REPORT, guard, pin


def join_source(premises, packed, checked_bridge):
    _, compact, compact_packed = dense_inputs(premises, packed)
    core, marker, _ = emit(compact, compact_packed).decode().partition('end P13PackedControl')
    assert marker
    core = core.replace('namespace P13PackedControl', 'namespace P13JoinedControl')
    bridge = checked_bridge.decode()
    formula_lines = lambda text: [line for line in text.splitlines()
                                  if line.startswith(('private def formulaPart', 'def formula :'))]
    assert formula_lines(core) == formula_lines(bridge)
    suffix = bridge[bridge.index('private noncomputable def oldVar0'):bridge.index('end P13BridgeControl')]
    suffix += '''open Ruliology.CellularAutomata.Rule30RingOrbits in
theorem factor_excluded (x : Int → Bool) (hx : orbit x 13 = x) (origin : Int) :
    ¬ Matches x origin 7 6 := factor_excluded_of_unsat unsat x hx origin

end P13JoinedControl

#print axioms P13JoinedControl.factor_excluded
'''
    return (core + suffix).encode()


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
    root = Path(os.environ['RETURN13_BRIDGE_DIR'])
    receipt = json.loads(pin(root/'solve.json', plan['bridge_receipt_sha256']))
    assert receipt['status'] == 'DENSE_FACTOR_KIT_BRIDGE_KERNEL_CHECKED'
    bridge = pin(root/'P13BridgeControl.lean', receipt['generated_source_sha256'])
    source = join_source(*read_inputs(plan), bridge)
    assert hashlib.sha256(source).hexdigest() == plan['generated_source_sha256']
    lean_file, olean = OUT/'P13JoinedControl.lean', OUT/'P13JoinedControl.olean'
    lean_file.write_bytes(source)
    _, diagnostics = guard.call('joined-kernel', [str(lean), '-j1', '-DElab.async=false', '-R', str(OUT),
                                                 '-o', str(olean), str(lean_file)], 75, 150, 0)
    ax = re.fullmatch(r"'P13JoinedControl\.factor_excluded' depends on axioms: \[([^]]*)\]", diagnostics.strip())
    assert ax is not None and olean.stat().st_size > 0, diagnostics
    axioms = {item.strip() for item in ax[1].split(',') if item.strip()}
    assert axioms <= {'propext', 'Classical.choice', 'Quot.sound'}, axioms
    REPORT.update(status='DENSE_WHOLE_LINE_FACTOR_KERNEL_CHECKED', generated_source_sha256=plan['generated_source_sha256'],
                  axioms=sorted(axioms), factor='0110000', olean_sha256=hashlib.sha256(olean.read_bytes()).hexdigest())
    guard.thermal()
    guard.save()
    print('RETURN13_JOINED_KERNEL_FACTOR_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
