#!/usr/bin/env python3
"""Check the remaining minimal factors of lengths 9–12 on the fixed P13 strip."""
from collections import Counter
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
    depths = range(9, 13)
    checked = {item['prefix_in_variable_order']: item for item in prior['leaves']
               if item['status'] == 'ABSENT_PREFIX_CHECKED'
               and len(item['prefix_in_variable_order']) in depths}
    assert set(checked) == {'000001010', '0001000011', '00000101101', '010110111110'}
    for factor, item in checked.items():
        assert set(range(17 - len(factor))) <= set(item['shifts']['clause_supported_shifts'])
    representatives = json.loads(pin(os.environ['RETURN13_FACTORS'], plan['factor_representatives_sha256']))
    eligible = {word for word in representatives.values() if len(word) in depths}
    assert set(checked) <= eligible
    factors = plan['factors']
    assert factors == sorted(eligible - checked.keys(), key=lambda word: (len(word), word))
    assert Counter(map(len, factors)) == {9: 33, 10: 26, 11: 10, 12: 3}
    original = pin(os.environ['RETURN13_ORIGINAL_CNF'], plan['original_cnf_sha256'])
    variables, clauses = read_cnf(original)
    assert (variables, len(clauses)) == (910, 5214)
    base = clauses[:5044]
    body = b''.join(original.splitlines(keepends=True)[1:5045])
    (OUT/'strip-base.cnf').write_bytes(b'p cnf 910 5044\n' + body)
    assert read_cnf((OUT/'strip-base.cnf').read_bytes())[1] == base
    for factor in factors:
        check_leaf(f'factor-{factor}', factor, base, body)
    REPORT['status'] = 'DEEP_ROOT_CASES_RECORDED'
    guard.thermal()
    guard.save()
    print('RETURN13_DEEP_ROOTS_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
