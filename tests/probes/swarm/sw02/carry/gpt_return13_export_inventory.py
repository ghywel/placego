#!/usr/bin/env python3
"""Measure exact proof export sizes for the remaining P13 canonical factors."""
import json
import os
from pathlib import Path
import resource
import signal
import sys
from tempfile import TemporaryDirectory

from gpt_return13_kernel_panel import prepare_factor
from gpt_return13_prefix_leaves import OUT, REPORT, guard, pin, read_cnf


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    cap = plan['limits']['worker_soft_cpu_s']
    resource.setrlimit(resource.RLIMIT_CPU, (cap if soft == resource.RLIM_INFINITY
                                            else min(cap, soft), hard))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    manifest = json.loads(pin(os.environ['RETURN13_SELECTION'], plan['manifest_sha256']))
    variables, clauses = read_cnf(pin(os.environ['RETURN13_ORIGINAL_CNF'], plan['original_cnf_sha256']))
    assert (variables, len(clauses)) == (910, 5214)
    base = clauses[:5044]
    gate_spec = plan['gate_source']
    gate = pin(gate_spec['file'], gate_spec['sha256'])
    checked = set(plan['already_kernel_checked'])
    assert checked <= manifest['proofs'].keys() and len(checked) == 3
    remaining = sorted(manifest['proofs'].keys() - checked)
    assert len(remaining) == plan['remaining_count']
    rows = []
    REPORT['exports'] = rows
    for word in remaining:
        if guard.STOP or guard.cpu() >= plan['limits']['inner_aggregate_stop_cpu_s']:
            raise RuntimeError('INVENTORY_STOP')
        REPORT['current_factor'] = word
        with TemporaryDirectory(dir=OUT) as work:
            _, result = prepare_factor({'word': word}, manifest, base, gate, Path(work))
            rows.append(result)
        if len(rows) % 16 == 0:
            guard.thermal()
            guard.save()
    del REPORT['current_factor']
    REPORT.update(status='P13_CANONICAL_EXPORT_INVENTORY_CHECKED',
                  source_bytes_total=sum(row['source_bytes'] for row in rows),
                  source_bytes_max=max(row['source_bytes'] for row in rows),
                  proof_additions_total=sum(row['lrup_additions'] for row in rows))
    guard.thermal()
    print('P13_CANONICAL_EXPORT_INVENTORY_CHECKED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
