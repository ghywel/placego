#!/usr/bin/env python3
"""Check the twenty remaining depth-7 factors in the retained P13 partition."""
import json
import os
from pathlib import Path
import resource
import signal

from gpt_return13_prefix_leaves import OUT, REPORT, check_leaf, guard, pin, read_cnf

FACTORS = (
    '0010111', '0011000', '0011011', '0100011', '0100110', '0101111', '0110000',
    '0110110', '0111101', '1010000', '1010011', '1011001', '1011010', '1011110',
    '1100001', '1101000', '1101100', '1110100', '1111011', '1111101',
)


def main():
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    worker_soft = 12 if soft == resource.RLIM_INFINITY else min(12, soft)
    resource.setrlimit(resource.RLIMIT_CPU, (worker_soft, hard))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    for path, digest in [
        (guard.CADICAL, '7fd73a73259e5494f4e6d638192232e7768b1676f519e91c52c69e145af15a7a'),
        (guard.CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'),
        (guard.LRAT_CHECK, '87429b8c50afdba643e83ea6ab712d36f49d5e4f47f488bd5d9ebc332bd204f1'),
    ]:
        pin(path, digest)
    controls = Path(os.environ['RETURN13_DEPTH7_CONTROLS'])
    first_receipt = json.loads(pin(controls/'first-exact-shifts.json',
        '0c33305551594c04886aa750909383e36c224a29d6fc4057205d1a198876d978'))
    first = next(item for item in first_receipt['proofs'] if item['prefix'] == '0000100')
    joined = json.loads(pin(controls/'joined.json',
        '410393bec6b3c74b855467bf2379e317fc65a15a356ef0110f6eea3126060b64'))['parent']
    assert first['steps'] == 1066 and first['support']['replayed_shifts'] == [-3, 0, 40]
    assert joined['status'] == 'JOINED_FACTOR_CHECKED' and joined['factor'] == '0001111'
    for support in (first['support'], joined['shifts']):
        assert set(range(10)) <= set(support['clause_supported_shifts'])
    representatives = json.loads(pin(os.environ['RETURN13_FACTORS'],
        '449c38d0fad13b88a7ef6c86d3746021c215d7fcb8631afe1f1ae937a041eed7'))
    previous = {first['prefix'], joined['factor']}
    assert tuple(sorted(w for w in set(representatives.values()) - previous if len(w) == 7)) == FACTORS
    original = pin(os.environ['RETURN13_ORIGINAL_CNF'],
        'badadbb38e00fb0c01991563f3fb6664ed2b78c9ab7254a36fa1bd818313fcd0')
    variables, clauses = read_cnf(original)
    assert (variables, len(clauses)) == (910, 5214)
    base = clauses[:5044]
    body = b''.join(original.splitlines(keepends=True)[1:5045])
    (OUT/'strip-base.cnf').write_bytes(b'p cnf 910 5044\n' + body)
    assert read_cnf((OUT/'strip-base.cnf').read_bytes())[1] == base
    for factor in FACTORS:
        check_leaf(f'factor-{factor}', factor, base, body)
    REPORT['status'] = 'DEPTH7_ROOT_CASES_RECORDED'
    guard.thermal()
    guard.save()
    print('RETURN13_DEPTH7_BATCH_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
