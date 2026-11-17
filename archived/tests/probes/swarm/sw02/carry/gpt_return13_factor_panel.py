#!/usr/bin/env python3
"""Measure six preselected factor exclusions on the retained P13 strip."""
import json
import os
from pathlib import Path
import resource
import signal

from gpt_return13_prefix_leaves import OUT, REPORT, check_leaf, guard, pin, read_cnf

FACTORS = ('0001111', '00000001', '000001010', '0001000011', '00000101101', '010110111110')


def saved_unknown(stage):
    receipt = json.loads(pin(stage/'solve.json',
        '6d8ab7403c4ada4f8843204c6cb08888166cd8e0880f522affd012a80faf5a06'))
    assert len(receipt['leaves']) == len(receipt['commands']) == 1
    entry = receipt['leaves'][0]
    command = receipt['commands'][0]
    assert entry['prefix_in_variable_order'] == FACTORS[0]
    assert (command['name'], command['returncode'], command['reason']) == ('depth7-solve', 0, 'EXIT')
    assert (stage/'depth7-solve.stdout').read_text() == 'c UNKNOWN\n'
    assert not (stage/'depth7-solve.stderr').read_bytes()
    assert entry['cnf_sha256'] == '2af8b3f8556518b240def9da4248592c36a5a318e4a750c9f786614df1e5fed2'
    pin(stage/'depth7.cnf', entry['cnf_sha256'])
    trace = pin(stage/'depth7.clrat',
        '765db3cc02b7b7b6b97256344dfe35575a76afec4659291c6499cb73045772a7')
    return {**entry, 'status': 'CONFLICT_LIMIT_UNKNOWN', 'binary_bytes': len(trace),
            'source_stage': 'GC2877'}


def main():
    _, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (12, hard))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    for path, digest in [
        (guard.CADICAL, '7fd73a73259e5494f4e6d638192232e7768b1676f519e91c52c69e145af15a7a'),
        (guard.CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'),
        (guard.LRAT_CHECK, '87429b8c50afdba643e83ea6ab712d36f49d5e4f47f488bd5d9ebc332bd204f1'),
    ]:
        pin(path, digest)
    representatives = json.loads(pin(os.environ['RETURN13_FACTORS'],
        '449c38d0fad13b88a7ef6c86d3746021c215d7fcb8631afe1f1ae937a041eed7'))
    unproved = set(representatives.values()) - {'0000100', '0000000000000001'}
    assert tuple(min(word for word in unproved if len(word) == depth) for depth in range(7, 13)) == FACTORS
    original = pin(os.environ['RETURN13_ORIGINAL_CNF'],
        'badadbb38e00fb0c01991563f3fb6664ed2b78c9ab7254a36fa1bd818313fcd0')
    variables, clauses = read_cnf(original)
    assert (variables, len(clauses)) == (910, 5214)
    base = clauses[:5044]
    body = b''.join(original.splitlines(keepends=True)[1:5045])
    (OUT/'strip-base.cnf').write_bytes(b'p cnf 910 5044\n' + body)
    assert read_cnf((OUT/'strip-base.cnf').read_bytes())[1] == base
    prior = os.environ.get('RETURN13_PRIOR_FACTOR_STAGE')
    pending = FACTORS
    if prior:
        REPORT['leaves'].append(saved_unknown(Path(prior)))
        pending = FACTORS[1:]
        guard.save()
    for factor in pending:
        check_leaf(f'depth{len(factor)}', factor, base, body)
    REPORT['status'] = 'SIX_FIXED_FACTORS_RECORDED'
    guard.thermal()
    guard.save()
    print('RETURN13_FACTOR_PANEL_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
