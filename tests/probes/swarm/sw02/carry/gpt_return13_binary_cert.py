#!/usr/bin/env python3
"""One original P13 binary LRAT export and checked positive dependency cone."""
import hashlib
import os
from pathlib import Path
import resource
import signal
import gpt_lrat_format_controls as codec

guard = codec.guard
OUT = guard.OUT
guard.REPORT = {'status': 'STARTED', 'commands': []}
REPORT = guard.REPORT


def pin(path, sha):
    data = Path(path).read_bytes()
    assert hashlib.sha256(data).hexdigest() == sha, Path(path).name
    return data


def budget():
    if guard.STOP or guard.cpu() >= 95:
        raise RuntimeError('DEPENDENCY_AUDIT_AGGREGATE_STOP')


def compact(cnf, binary, text):
    """Retain the final empty clause's positive hints; keep the ORIGINAL formula."""
    with cnf.open() as f:
        header = f.readline().split()
    assert header[:2] == ['p', 'cnf'] and len(header) == 4
    original = int(header[-1])
    offsets = {}; empty = None; deletions = 0
    with binary.open('rb') as f:
        records = codec.decode(f)
        while True:
            at = f.tell()
            r = next(records, None)
            if r is None:
                break
            if r[0] == 'd':
                deletions += 1
            else:
                _, cid, clause, _ = r
                assert cid > original and cid not in offsets
                offsets[cid] = at
                if not clause:
                    empty = cid
                if len(offsets) % 2048 == 0:
                    budget()
        assert empty is not None
        used = {}; todo = [empty]
        while todo:
            cid = todo.pop()
            if cid <= original or cid in used:
                continue
            f.seek(offsets[cid]); r = next(codec.decode(f))
            assert r[0] == 'a' and r[1] == cid
            _, _, clause, hints = r
            if any(h <= 0 for h in hints):
                return {'status': 'USED_RAT', 'raw_additions': len(offsets),
                        'deletion_records': deletions, 'first_seen_rat_id': cid}
            assert all(h <= original or (h in offsets and offsets[h] < offsets[cid]) for h in hints)
            used[cid] = (clause, hints)
            todo.extend(hints)
            if len(used) % 2048 == 0:
                budget()
    order = sorted(used, key=offsets.__getitem__)
    assert order[-1] == empty and used[empty][0] == []
    ids = {cid: original+i+1 for i, cid in enumerate(order)}
    with text.open('w') as f:
        for i, cid in enumerate(order):
            clause, hints = used[cid]
            newh = [h if h <= original else ids[h] for h in hints]
            assert all(0 < h < ids[cid] for h in newh)
            f.write(' '.join(map(str, [ids[cid], *clause, 0, *newh, 0]))+'\n')
            if i % 2048 == 0:
                budget()
    return {'status': 'POSITIVE_CONE', 'raw_additions': len(offsets),
            'deletion_records': deletions, 'used_additions': len(order),
            'original_clauses': original, 'text_bytes': text.stat().st_size}


def c_check(name, cnf, proof, expect=True):
    rc, msg = guard.call(name, [guard.LRAT_CHECK, str(cnf), str(proof)], 10 if name=='target-cone-check' else 2,
                         30 if name=='target-cone-check' else 5)
    assert (rc == 0 and 'c VERIFIED' in msg.splitlines()) == expect
    if not expect:
        assert 'c NOT VERIFIED' in msg.splitlines()


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (12, 120))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    for path, sha in [(guard.CADICAL, '7fd73a73259e5494f4e6d638192232e7768b1676f519e91c52c69e145af15a7a'),
                      (guard.CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'),
                      (guard.LRAT_CHECK, '87429b8c50afdba643e83ea6ab712d36f49d5e4f47f488bd5d9ebc332bd204f1')]:
        pin(path, sha)
    controls = Path(os.environ['LRAT_FORMAT_CONTROL_DIR'])
    php = OUT/'php.cnf'; php_bin = OUT/'php.clrat'; php_trim = OUT/'php-cone.lrat'
    php.write_bytes(pin(controls/'php.cnf', '4fa2e5d8b36454ba6b01e1a92161e90e46cd16b0f19b41cdf148e49a87c741a1'))
    php_bin.write_bytes(pin(controls/'php.clrat', '40d411cde559bd11e5c14b31f0d2a3f835dec4bb070766c753ef6b9f37726aa3'))
    guard.cake('retained-php-binary', php, php_bin, True)
    ctl = compact(php, php_bin, php_trim)
    assert ctl['status'] == 'POSITIVE_CONE'
    c_check('php-cone-check', php, php_trim)
    bad = OUT/'php-cone-without-empty.lrat'
    ls = php_trim.read_bytes().splitlines(keepends=True)
    assert ls[-1].split()[1] == b'0'
    bad.write_bytes(b''.join(ls[:-1]))
    c_check('php-cone-reject', php, bad, False)
    REPORT['control'] = ctl; guard.save()
    cnf = OUT/'original.cnf'; binary = OUT/'original.clrat'; text = OUT/'needed-cone.lrat'
    cnf.write_bytes(pin(os.environ['RETURN13_ORIGINAL_CNF'], 'badadbb38e00fb0c01991563f3fb6664ed2b78c9ab7254a36fa1bd818313fcd0'))
    guard.call('target-binary-solve', [guard.CADICAL, '-q', '--lrat', '--binary', str(cnf), str(binary)], 45, 100, 20)
    guard.cake('target-binary-cake', cnf, binary, True, 15, 40)
    REPORT['finite_cnf'] = 'ORIGINAL_CNF_BINARY_LRAT_CAKE_VERIFIED'
    REPORT['binary_sha256'] = hashlib.sha256(binary.read_bytes()).hexdigest()
    REPORT['binary_bytes'] = binary.stat().st_size
    guard.save()
    REPORT['cone'] = compact(cnf, binary, text)
    if REPORT['cone']['status'] == 'POSITIVE_CONE':
        c_check('target-cone-check', cnf, text)
        REPORT['finite_cnf'] = 'ORIGINAL_CNF_CAKE_AND_INDEPENDENT_CONE_VERIFIED'
        REPORT['cone_sha256'] = hashlib.sha256(text.read_bytes()).hexdigest()
        guard.save()
        REPORT['rup_audit'] = guard.audit_rup(cnf, text)
    REPORT['status'] = 'FINITE_CNF_VERIFIED_FORMAT_AUDITED'
    guard.thermal(); guard.save()
    print('RETURN13_BINARY_STAGE_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
