#!/usr/bin/env python3
"""Check a pinned batch of factor modules and a joint public import."""
import json
import os
from pathlib import Path
import resource
import signal
import sys

from gpt_return13_factor_module_smoke import as_module, audit_axioms, digest
from gpt_return13_kernel_panel import prepare_factor
from gpt_return13_prefix_leaves import OUT, REPORT, guard, pin, read_cnf


def prepare_inputs(plan):
    manifest = json.loads(pin(os.environ['RETURN13_SELECTION'], plan['manifest_sha256']))
    variables, clauses = read_cnf(pin(os.environ['RETURN13_ORIGINAL_CNF'], plan['original_cnf_sha256']))
    assert (variables, len(clauses)) == (910, 5214)
    gate = plan['gate_source']
    return manifest, clauses[:5044], pin(gate['file'], gate['sha256'])


def prepare_module(spec, inputs):
    source, result = prepare_factor(spec, *inputs)
    assert result['source_sha256'] == spec['source_sha256'], result
    generated = as_module(source.read_bytes())
    source.write_bytes(generated)
    result.update(module=source.stem, module_sha256=digest(generated), module_source_bytes=len(generated))
    return source, result


def emit_consumer(results):
    lines = ['module', '']
    lines.extend(f'public import {r["module"]}' for r in results)
    lines.extend(['', 'open Ruliology.CellularAutomata.Rule30MovingStrip',
                  'open Ruliology.CellularAutomata.Rule30RingOrbits', ''])
    for r in results:
        name = f'P13BatchPublic.factor{r["word"]}'
        lines.extend([
            f'public theorem {name} (x : Int → Bool) (hx : orbit x 13 = x) (o : Int) :',
            f'    ¬ Matches x o {r["lean_width"]} {r["lean_value"]} :=',
            f'  {r["module"]}.factor_excluded x hx o',
            '',
            f'#print axioms {name}',
            '',
        ])
    return '\n'.join(lines).encode()


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
    prepare_only = sys.argv[2:] == ['--prepare']
    if not prepare_only:
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
        os.environ['LEAN_PATH'] = str(kit)
        os.environ['LEAN_NUM_THREADS'] = '1'
        _, version = guard.call('lean-version', [str(lean), '--version'], 2, 5, 0)
        assert version.strip() == plan['lean_version']
    inputs = prepare_inputs(plan)
    results = []
    REPORT['factors'] = results
    public_root = OUT/'public-imports'
    public_root.mkdir()
    artifact_map = {}
    for spec in plan['factors']:
        source, result = prepare_module(spec, inputs)
        results.append(result)
        if prepare_only:
            continue
        assert result['module_sha256'] == spec['module_sha256'], result
        module = result['module']
        public = source.with_suffix('.olean')
        limits = plan['limits']
        _, diagnostics = guard.call(
            f'producer-{result["word"]}',
            [str(lean), '-j1', '-DElab.async=false', '-R', str(OUT), '-o', str(public), str(source)],
            limits['producer_cpu_s'], limits['producer_wall_s'], 0,
        )
        result['axioms'] = audit_axioms(diagnostics, f'{module}.factor_excluded')
        result['artifacts'] = {p.name:{'bytes':p.stat().st_size,'sha256':digest(p.read_bytes())}
                               for p in sorted(OUT.glob(f'{module}.*'))}
        assert public.stat().st_size < public.with_suffix('.olean.private').stat().st_size
        exported = public_root/public.name
        exported.write_bytes(public.read_bytes())
        artifact_map[module] = [[str(exported)]]
        result['kernel_checked'] = True
        guard.save()
    consumer = OUT/'P13BatchPublic.lean'
    consumer.write_bytes(emit_consumer(results))
    consumer_sha = digest(consumer.read_bytes())
    REPORT['consumer_sha256'] = consumer_sha
    if prepare_only:
        (OUT/'preflight.json').write_text(json.dumps(REPORT, indent=2)+'\n')
        return
    assert consumer_sha == plan['consumer_sha256']
    assert {p.name for p in public_root.iterdir()} == {r['module']+'.olean' for r in results}
    setup = OUT/'public-import.setup.json'
    setup.write_text(json.dumps({
        'name':consumer.stem, 'isModule':True, 'importArts':artifact_map,
        'dynlibs':[], 'plugins':[], 'options':{},
    }, indent=2)+'\n')
    _, diagnostics = guard.call(
        'joint-public-consumer',
        [str(lean), '-j1', '-DElab.async=false', f'--setup={setup}', '-R', str(OUT),
         '-o', str(consumer.with_suffix('.olean')), str(consumer)],
        plan['limits']['consumer_cpu_s'], plan['limits']['consumer_wall_s'], 0,
    )
    lines = diagnostics.strip().splitlines()
    assert len(lines) == len(results), diagnostics
    for line, result in zip(lines, results):
        assert audit_axioms(line, f'P13BatchPublic.factor{result["word"]}') == result['axioms']
    REPORT.update(status='P13_FACTOR_MODULE_BATCH_KERNEL_CHECKED', joint_consumer_checked=True,
                  public_bytes=sum(r['artifacts'][r['module']+'.olean']['bytes'] for r in results))
    guard.thermal()
    print('P13_FACTOR_MODULE_BATCH_KERNEL_CHECKED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        if '--prepare' not in sys.argv[2:]:
            guard.save()
