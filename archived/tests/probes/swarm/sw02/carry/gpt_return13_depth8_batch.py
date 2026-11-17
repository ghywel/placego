#!/usr/bin/env python3
"""Check the pending minimal length-eight factors of the fixed P13 strip."""
import json
import os
from pathlib import Path
import resource
import signal
import sys

from gpt_return13_prefix_leaves import OUT, REPORT, check_leaf, guard, pin, read_cnf


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
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
    prior = json.loads(pin(os.environ['RETURN13_PANEL_RECEIPT'], plan['panel_receipt_sha256']))
    checked = [item for item in prior['leaves'] if item['status'] == 'ABSENT_PREFIX_CHECKED'
               and len(item['prefix_in_variable_order']) == 8]
    assert [item['prefix_in_variable_order'] for item in checked] == ['00000001']
    assert set(range(9)) <= set(checked[0]['shifts']['clause_supported_shifts'])
    representatives = json.loads(pin(os.environ['RETURN13_FACTORS'], plan['factor_representatives_sha256']))
    all_depth_eight = {word for word in representatives.values() if len(word) == 8}
    factors = plan['factors']
    assert len(factors) == 41 and factors == sorted(all_depth_eight - {'00000001'})
    original = pin(os.environ['RETURN13_ORIGINAL_CNF'], plan['original_cnf_sha256'])
    variables, clauses = read_cnf(original)
    assert (variables, len(clauses)) == (910, 5214)
    base = clauses[:5044]
    body = b''.join(original.splitlines(keepends=True)[1:5045])
    (OUT/'strip-base.cnf').write_bytes(b'p cnf 910 5044\n' + body)
    assert read_cnf((OUT/'strip-base.cnf').read_bytes())[1] == base
    for factor in factors:
        check_leaf(f'factor-{factor}', factor, base, body)
    REPORT['status'] = 'DEPTH8_ROOT_CASES_RECORDED'
    guard.thermal()
    guard.save()
    print('RETURN13_DEPTH8_BATCH_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
