#!/usr/bin/env python3
"""Freeze exact serial Lean batches for the remaining P13 factors."""
import json
import os
from pathlib import Path
import resource
import signal
import sys
from tempfile import TemporaryDirectory

from gpt_return13_module_batch import digest, emit_consumer, prepare_inputs, prepare_module
from gpt_return13_prefix_leaves import OUT, REPORT, guard, pin


def partition(rows, byte_limit, count_limit):
    groups = []
    batch = []
    size = 0
    for row in rows:
        assert row['source_bytes'] <= byte_limit
        if len(batch) == count_limit or size + row['source_bytes'] > byte_limit:
            groups.append(batch)
            batch, size = [], 0
        batch.append(row)
        size += row['source_bytes']
    if batch:
        groups.append(batch)
    return groups


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    cap = plan['limits']['worker_soft_cpu_s']
    resource.setrlimit(resource.RLIMIT_CPU, (cap if soft == resource.RLIM_INFINITY
                                            else min(cap, soft), hard))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    template = plan['batch_template']
    matrix = json.loads(pin(template['file'], template['sha256']))
    inputs = prepare_inputs(matrix)
    inventory = json.loads(pin(os.environ['RETURN13_EXPORT_INVENTORY'], plan['inventory_sha256']))
    rows = {row['word']:row for row in inventory['exports']}
    assert len(rows) == len(inventory['exports']) == 138
    completed = set(plan['completed_inventory_words'])
    assert len(completed) == len(plan['completed_inventory_words']) == 23
    assert completed <= rows.keys()
    checked_words = []
    source_root = Path(os.environ['RETURN13_SOURCE_ROOT'])
    for name, sha in plan['completed_receipt_sha256'].items():
        receipt = json.loads(pin(source_root/name/'solve.json', sha))
        assert receipt['status'] in {
            'P13_FACTOR_PANEL_KERNEL_CHECKED',
            'P13_FACTOR_MODULE_PRODUCER_KERNEL_CHECKED',
            'P13_FACTOR_MODULE_BATCH_KERNEL_CHECKED',
        }
        checked = receipt['factors'] if 'factors' in receipt else [receipt['factor']]
        checked_words.extend(row['word'] for row in checked)
    assert len(checked_words) == len(completed) and set(checked_words) == completed
    remaining = [rows[word] for word in sorted(rows.keys() - completed)]
    groups = partition(remaining, plan['source_byte_limit'], plan['factor_count_limit'])
    assert len(remaining) == 115
    assert [[row['word'] for row in group] for group in groups] == plan['expected_cohorts']
    batches = {}
    REPORT['batches'] = batches
    for i, group in enumerate(groups, 1):
        results = []
        specs = []
        for row in group:
            if guard.STOP or guard.cpu() >= plan['limits']['inner_aggregate_stop_cpu_s']:
                raise RuntimeError('MATRIX_STOP')
            spec = {key:row[key] for key in ('word', 'source_sha256', 'source_bytes', 'lrup_additions')}
            with TemporaryDirectory(dir=OUT) as work:
                _, result = prepare_module(spec, inputs, Path(work))
            assert all(result[key] == spec[key] for key in spec)
            spec['module_sha256'] = result['module_sha256']
            specs.append(spec)
            results.append(result)
        batches[f'{i:02d}'] = {
            'factors': specs,
            'source_bytes': sum(row['source_bytes'] for row in specs),
            'consumer_sha256': digest(emit_consumer(results)),
        }
        guard.thermal()
        guard.save()
    del matrix['factors'], matrix['consumer_sha256']
    matrix['input_sha256'].update(plan['matrix_input_updates'])
    matrix['jobs'][0].update(
        name='module-matrix-batch',
        args=['python3', plan['module_worker'], '--matrix'],
    )
    matrix['prediction'] = {
        'producer': 'Each selected cohort gives the pinned whole-line factor exclusions with standard axioms.',
        'consumer': 'The joint consumer relays each theorem via its explicitly mapped public object.',
    }
    matrix['batches'] = batches
    output = OUT/'module-matrix.json'
    output.write_text(json.dumps(matrix, indent=2)+'\n')
    REPORT.update(status='P13_MODULE_MATRIX_FROZEN', factor_count=len(remaining),
                  batch_count=len(groups), matrix_sha256=digest(output.read_bytes()))
    guard.thermal()
    print('P13_MODULE_MATRIX_FROZEN', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
