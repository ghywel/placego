#!/usr/bin/env python3
"""Export one checked P13 factor proof in the kit's packed RUP format."""
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys

from gpt_return13_coverage import native_checks, write_cnf
from gpt_return13_lrat import audit_rup, literal_mask
from gpt_return13_prefix_control import add_step, write_proof
from gpt_return13_prefix_leaves import OUT, REPORT, guard, pin, read_cnf
from gpt_return13_prefix_replay import read_proof


def replay(masks, packed, initial):
    if len(masks) != initial + len(packed) or masks[-1] != 0:
        return False
    for bound, word in enumerate(packed, initial):
        conflict = word & 0x3fff
        count = (word >> 14) & 0x3ff
        trail = word >> 24
        known_false = masks[bound]
        for _ in range(count):
            hint = trail & 0x3fff
            unit = (trail >> 14) & 0x7ff
            if hint >= bound or masks[hint] & ~(known_false | (1 << unit)):
                return False
            known_false |= 1 << (unit ^ 1)
            trail >>= 25
        if trail or conflict >= bound or masks[conflict] & ~known_false:
            return False
    return True


def compact_factor(base, derivation, factor):
    supported = sorted({hint for _, _, hints in derivation for hint in hints if hint <= len(base)})
    units = [[(7 + j) * (1 if bit == '1' else -1)] for j, bit in enumerate(factor)]
    initial = [base[index - 1] for index in supported] + units
    database = dict(enumerate(initial, 1))
    proof = []
    mapping = {source: target for target, source in enumerate(supported, 1)}
    for index, clause, hints in derivation:
        mapping[index] = add_step(clause, [mapping[h] for h in hints], database, proof)
    conclusion = proof[-1][0]
    assert database[conclusion] == [-unit[0] for unit in units]
    add_step([], [*range(len(supported) + 1, len(initial) + 1), conclusion], database, proof)
    return supported, initial, proof


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (12 if soft == resource.RLIM_INFINITY else min(12, soft), hard))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    for path, digest in plan['tool_sha256'].items():
        pin(path, digest)
    pin(Path(os.environ['RETURN13_KIT_ROOT'])/plan['kit_replayer']['file'], plan['kit_replayer']['sha256'])
    source = Path(os.environ['RETURN13_SOURCE_ROOT'])
    original = pin(os.environ['RETURN13_ORIGINAL_CNF'], plan['original_cnf_sha256'])
    variables, clauses = read_cnf(original)
    assert (variables, len(clauses)) == (910, 5214)
    base = clauses[:5044]
    spec = plan['discharged_proof']
    factor = spec['factor']
    derivation = read_proof(pin(source/spec['file'], spec['sha256']), base, factor)
    assert len(derivation) == spec['steps']
    supported, initial, proof = compact_factor(base, derivation, factor)
    cnf, lrat = OUT/'compact-factor.cnf', OUT/'compact-factor.lrat'
    write_cnf(cnf, variables, initial)
    write_proof(lrat, proof)
    native_checks('compact-factor', cnf, lrat)
    audit = audit_rup(cnf, lrat)
    assert audit['packable'], audit
    packed_path = OUT/'packed-rup.json'
    packed_raw = packed_path.read_bytes()
    packed = json.loads(packed_raw)
    masks = [int(x, 16) for x in packed['masks_hex']]
    words = [int(x, 16) for x in packed['steps_hex']]
    assert masks[:len(initial)] == [literal_mask(clause) for clause in initial]
    assert replay(masks, words, len(initial))
    wrong_conflict = len(initial) + len(words) - 1
    assert wrong_conflict < 2**14
    assert not replay(masks, [*words[:-1], (words[-1] & ~0x3fff) | wrong_conflict], len(initial))
    assert not replay([*masks[:-1], 1], words, len(initial))
    (OUT/'factor-premises.json').write_text(json.dumps({'factor': factor, 'base_clause_ids': supported,
                                                        'initial_clauses': initial}, indent=2)+'\n')
    REPORT.update(status='KIT_PACKED_FORMAT_CONTROL_PASS', factor=factor, audit=audit,
                  exact_support_count=len(supported), cube_units=len(initial)-len(supported),
                  packed_sha256=hashlib.sha256(packed_raw).hexdigest(), packed_bytes=len(packed_raw),
                  bad_hint_rejected=True, nonempty_goal_rejected=True)
    guard.thermal()
    guard.save()
    print('RETURN13_PACKED_FACTOR_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
