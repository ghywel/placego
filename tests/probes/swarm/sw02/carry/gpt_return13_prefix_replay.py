#!/usr/bin/env python3
"""Replay the saved P13 exclusions and count factor-minimal proof obligations."""
from collections import Counter
import json
import os
from pathlib import Path

from gpt_return13_prefix_control import read_cnf, rup_hints
from gpt_return13_prefix_leaves import audit_shifts, guard, pin

OUT = guard.OUT
INPUTS = [
    ('depth16', '0000000000000001', '7987734a4cb62e0d7ee9405bf59addcc7fe36767cdc07a56d82411aaf0b25d22'),
    ('depth7', '0000100', '16335b6ee6c2e540637aa59a31da9012bb5147e36ac63b136c4f8e08b67e5f9b'),
]


def read_proof(data, base, prefix):
    proof = []
    database = dict(enumerate(base, 1))
    for line in data.decode().splitlines():
        index, *rest = map(int, line.split())
        zero = rest.index(0)
        clause, hints = rest[:zero], rest[zero + 1:-1]
        assert rest[-1] == 0 and index == len(database) + 1
        assert all(0 < hint < index for hint in hints)
        assert rup_hints(clause, hints, database) == hints
        database[index] = clause
        proof.append((index, clause, hints))
    expected = [(-1 if bit == '1' else 1) * (7 + i) for i, bit in enumerate(prefix)]
    assert proof[-1][1] == expected
    return proof


def factor_reduction(leaves, proofs):
    absent = [leaf['prefix_in_variable_order'] for leaf in leaves if not leaf['retained']]
    absent_set = set(absent)
    minimal = []
    representative = {}
    for word in sorted(absent, key=lambda w: (len(w), w)):
        factors = [word[start:end] for start in range(len(word))
                   for end in range(start + 1, len(word) + 1) if word[start:end] in absent_set]
        best = min(factors, key=lambda w: (len(w), w))
        if best == word:
            minimal.append(word)
        representative[word] = best
    assert set(representative.values()) == set(minimal)
    covered = set()
    for item in proofs:
        prefix = item['prefix']
        offsets = item['support']['clause_supported_shifts']
        matches = [word for word in absent if any(delta >= 0 and word[delta:].startswith(prefix) for delta in offsets)]
        covered.update(matches)
        item['covered_absent_leaves'] = len(matches)
        item['covered_assignments'] = sum(2**(16 - len(word)) for word in matches)
    (OUT/'factor-representatives.json').write_text(json.dumps(representative, indent=2)+'\n')
    return {'absent_leaves': len(absent), 'factor_minimal_count': len(minimal),
            'factor_minimal_by_depth': dict(sorted(Counter(map(len, minimal)).items())),
            'covered_by_two_checked_proofs': len(covered),
            'covered_assignments': sum(2**(16 - len(word)) for word in covered)}


def main():
    source = Path(os.environ['RETURN13_LEAF_STAGE'])
    base_data = pin(source/'strip-base.cnf', '647afe61ca9253daa7c707526f50cbdc94f31fca9eb909c27167c4acab96c457')
    original = pin(os.environ['RETURN13_ORIGINAL_CNF'], 'badadbb38e00fb0c01991563f3fb6664ed2b78c9ab7254a36fa1bd818313fcd0')
    assert base_data == b'p cnf 910 5044\n' + b''.join(original.splitlines(keepends=True)[1:5045])
    _, base = read_cnf(base_data)
    proofs = []
    for label, prefix, sha in INPUTS:
        proof = read_proof(pin(source/f'{label}-discharged.lrat', sha), base, prefix)
        support = audit_shifts(base, proof)
        proofs.append({'prefix': prefix, 'steps': len(proof), 'support': support})
    rejected = proofs[1]['support']['rejected_shifts']
    assert any(x['missing_clause'] == [-65, 64, 129] for x in rejected), 'BOUNDARY_REGRESSION'
    leaves = json.loads(pin(os.environ['RETURN13_PREFIX_LEAVES'], '4fd926b2b495dd046f1b24a5e67700f7823f79208cc219be23b4751992a19884'))
    result = {'proofs': proofs, 'factors': factor_reduction(leaves, proofs)}
    (OUT/'prefix-replay.json').write_text(json.dumps(result, indent=2)+'\n')
    print('RETURN13_PREFIX_REPLAY_RECORDED', flush=True)


if __name__ == '__main__':
    main()
