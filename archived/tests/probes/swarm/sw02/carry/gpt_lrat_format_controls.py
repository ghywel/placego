#!/usr/bin/env python3
"""GC2864: tiny LRAT format controls and retained-prefix conversion; NO target solve."""
import hashlib
import io
import json
import os
from pathlib import Path
import resource
import signal
import gpt_return13_lrat as guard

OUT = Path(os.environ['CAPPED_OUT'])
guard.REPORT = {'status': 'STARTED', 'commands': []}
REPORT = guard.REPORT


def signed(n):
    v = 2*abs(n)+int(n < 0)
    assert v < 2**64
    out = bytearray()
    while v >= 128:
        out.append((v & 127) | 128); v >>= 7
    out.append(v)
    return bytes(out)


def read_signed(stream):
    value = shift = 0
    while True:
        b = stream.read(1)
        if not b:
            raise ValueError('TRUNCATED_VARINT')
        b = b[0]; value |= (b & 127) << shift
        if not b & 128:
            if value >= 2**64 or value == 1 or (shift and b == 0):
                raise ValueError('NONCANONICAL_OR_OVERSIZED_VARINT')
            n = value >> 1
            return -n if value & 1 else n
        shift += 7
        if shift > 63:
            raise ValueError('OVERSIZED_VARINT')


def read_list(stream):
    result = []
    while True:
        n = read_signed(stream)
        if n == 0:
            return result
        result.append(n)


def decode(stream):
    while True:
        tag = stream.read(1)
        if not tag:
            return
        if tag == b'a':
            cid = read_signed(stream)
            if cid <= 0:
                raise ValueError('NONPOSITIVE_ADDITION_ID')
            yield ('a', cid, read_list(stream), read_list(stream))
        elif tag == b'd':
            ids = read_list(stream)
            if any(n <= 0 for n in ids):
                raise ValueError('NONPOSITIVE_DELETION_ID')
            yield ('d', ids)
        else:
            raise ValueError('INVALID_RECORD_TAG')


def encode_record(record):
    if record[0] == 'a':
        _, cid, clause, hints = record
        return b'a'+signed(cid)+b''.join(map(signed, clause))+b'\0'+b''.join(map(signed, hints))+b'\0'
    assert record[0] == 'd'
    return b'd'+b''.join(map(signed, record[1]))+b'\0'


def encode(records):
    return b''.join(map(encode_record, records))


def ascii_records(records, initial_id):
    latest = initial_id
    for r in records:
        if r[0] == 'd':
            yield str(latest)+' d '+' '.join(map(str, r[1]))+' 0\n'
        else:
            _, latest, clause, hints = r
            yield str(latest)+' '+' '.join(map(str, clause))+' 0 '+' '.join(map(str, hints))+' 0\n'


def record_digest(records):
    digest = hashlib.sha256(); count = 0
    for record in records:
        digest.update(json.dumps(record, separators=(',', ':')).encode()+b'\n')
        count += 1
    return count, digest.hexdigest()


def prefix_records(path):
    # Discard ONLY the stopped file's incomplete final line, never call this a proof.
    with path.open() as f:
        for line in f:
            if not line.endswith('\n'):
                return
            ns = line.split()
            if ns[1] == 'd':
                assert ns[-1] == '0'
                yield ('d', list(map(int, ns[2:-1])))
            else:
                ns = list(map(int, ns)); z = ns.index(0)
                assert ns[-1] == 0
                yield ('a', ns[0], ns[1:z], ns[z+1:-1])


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (12, 120))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    for path, sha in [(guard.CADICAL, '7fd73a73259e5494f4e6d638192232e7768b1676f519e91c52c69e145af15a7a'),
                      (guard.CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'),
                      (guard.LRAT_CHECK, '87429b8c50afdba643e83ea6ab712d36f49d5e4f47f488bd5d9ebc332bd204f1')]:
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == sha
    # Multi-byte signed literals/IDs and deletions are representation tests only.
    synthetic = [('a', 2**31+129, [205, -205, 1], [1, 2**31+128, -129]), ('d', [129, 205])]
    assert list(decode(io.BytesIO(encode(synthetic)))) == synthetic
    rejected = 0
    for bad in [b'a\x80', b'a\x00\0\0', b'a\x82\x00\0\0', b'?', b'd\x01\0']:
        try:
            list(decode(io.BytesIO(bad)))
        except ValueError:
            rejected += 1
    assert rejected == 5
    # PHP(5 pigeons,4 holes), not the retained period13 CNF.
    var = lambda pigeon, hole: 1+4*pigeon+hole
    clauses = [[var(p, h) for h in range(4)] for p in range(5)]
    clauses += [[-var(p, a), -var(p, b)] for p in range(5) for a in range(4) for b in range(a+1, 4)]
    clauses += [[-var(a, h), -var(b, h)] for h in range(4) for a in range(5) for b in range(a+1, 5)]
    cnf = OUT/'php.cnf'
    cnf.write_text('p cnf 20 %d\n'%len(clauses)+''.join(' '.join(map(str, c))+' 0\n' for c in clauses))
    binary = OUT/'php.clrat'
    guard.call('php-binary', [guard.CADICAL, '-q', '--lrat', '--binary', str(cnf), str(binary)], 2, 5, 20)
    guard.cake('php-binary-cake', cnf, binary, True)
    raw = binary.read_bytes(); records = list(decode(io.BytesIO(raw)))
    assert encode(records) == raw
    assert any(r[0] == 'a' and not r[2] for r in records)
    text = ''.join(ascii_records(records, len(clauses)))
    converted = OUT/'php-decoded.lrat'; converted.write_text(text)
    guard.cake('php-text-cake', cnf, converted, True)
    _, msg = guard.call('php-text-independent', [guard.LRAT_CHECK, str(cnf), str(converted)], 2, 5, 0)
    assert 'c VERIFIED' in msg.splitlines()
    # Unexpected compatibility control: unused CLRAT constant does NOT enable parsing.
    rc, msg = guard.call('php-binary-independent-reject', [guard.LRAT_CHECK, str(cnf), str(binary)], 2, 5)
    assert rc != 0 and 'c NOT VERIFIED' in msg.splitlines()
    unit = OUT/'unit.cnf'; unit.write_text('p cnf 1 2\n1 0\n-1 0\n')
    good = OUT/'unit-good.clrat'; good.write_bytes(encode([('a', 3, [], [1, 2])]))
    bad = OUT/'unit-bad.clrat'; bad.write_bytes(encode([('a', 3, [], [1, 1])]))
    empty = OUT/'empty.clrat'; empty.write_bytes(b'')
    guard.cake('unit-good-binary', unit, good, True)
    guard.cake('unit-bad-binary', unit, bad, False)
    guard.cake('unit-empty-binary', unit, empty, False)
    prefix = Path(os.environ['RETURN13_PARTIAL_ASCII'])
    raw = prefix.read_bytes()
    assert len(raw) == 16777216 and hashlib.sha256(raw).hexdigest() == '9ca317f706d5ae4e689f826eb2cffa7e74c50f6712ee44336e926c1f60e478dd'
    binary_prefix = OUT/'partial-prefix.clrat'
    with binary_prefix.open('wb') as f:
        for record in prefix_records(prefix):
            f.write(encode_record(record))
    before = record_digest(prefix_records(prefix))
    with binary_prefix.open('rb') as f:
        after = record_digest(decode(f))
    assert before == after and before[0] < 100000
    REPORT.update(status='FORMAT_CONTROLS_PASS_NO_TARGET_SOLVE',
        php={'variables': 20, 'clauses': len(clauses), 'binary_bytes': len(records) and binary.stat().st_size,
             'decoded_ascii_bytes': len(text.encode()), 'byte_roundtrip': True},
        malformed_records_rejected=rejected,
        original_partial_prefix={'ascii_input_bytes': len(raw), 'complete_records': before[0],
            'canonical_records_sha256': before[1], 'binary_bytes': binary_prefix.stat().st_size,
            'ratio': binary_prefix.stat().st_size/len(raw), 'is_complete_refutation': False},
        target_solve=False)
    guard.save()
    print('LRAT_FORMAT_CONTROLS_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
