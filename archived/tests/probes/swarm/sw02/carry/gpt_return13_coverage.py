#!/usr/bin/env python3
"""Certify the canonical exclusions and close the exact P13 CNF by trie composition."""
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys

from gpt_return13_implied_retry import add_translated_proof, translated_premises
from gpt_return13_prefix_control import add_step, prefix_partition, rup_hints, write_proof
from gpt_return13_prefix_leaves import OUT, REPORT, guard, pin, read_cnf, shifted
from gpt_return13_prefix_replay import read_proof


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_cnf(path, variables, clauses):
    with path.open('w') as out:
        out.write(f'p cnf {variables} {len(clauses)}\n')
        for clause in clauses:
            out.write(' '.join(map(str, [*clause, 0])) + '\n')


def native_checks(label, cnf, lrat):
    guard.cake(label+'-cake', cnf, lrat, True, 15, 30)
    _, output = guard.call(label+'-independent', [guard.LRAT_CHECK, str(cnf), str(lrat)], 15, 30, 0)
    assert 'c VERIFIED' in output.splitlines()


def canonical_shard(label, base, selected, data, group, source):
    index = {tuple(sorted(c)): i for i, c in enumerate(base, 1)}
    canonical = {}
    for factor in group:
        spec = data['proofs'][factor]
        canonical[factor] = read_proof(pin(source/spec['file'], spec['sha256']), base, factor)
        assert len(canonical[factor]) == spec['steps']
    if '0000100' in canonical:
        try:
            translated_premises(base, index, canonical['0000100'], 41)
        except KeyError as error:
            assert error.args == ((-65, 64, 129),)
        else:
            raise AssertionError('MISSING_TRANSLATED_PREMISE_ACCEPTED')
    translations = []
    for item in selected:
        factor, delta = item['factor'], item['shift']
        if factor in canonical:
            proof = canonical[factor]
            assert 0 <= delta <= 16 - len(factor)
            translated_premises(base, index, proof, delta)
            translations.append({'factor': factor, 'shift': delta,
                                 'clause': [shifted(lit, delta) for lit in proof[-1][1]]})
    selectors = list(range(911, 911 + len(group)))
    trial = base + [selectors]
    disjunct = len(trial)
    implications = {}
    for (factor, proof), selector in zip(canonical.items(), selectors):
        start = len(trial) + 1
        trial.extend([-selector, -lit] for lit in proof[-1][1])
        implications[factor] = list(range(start, len(trial) + 1))
    database = dict(enumerate(trial, 1))
    proof = []
    negatives = []
    for (factor, derivation), selector in zip(canonical.items(), selectors):
        mapping = {i: i for i in range(1, len(base) + 1)}
        conclusion = add_translated_proof(derivation, 0, mapping, database, proof)
        assert database[conclusion] == derivation[-1][1]
        negatives.append(add_step([-selector], [*implications[factor], conclusion], database, proof))
    add_step([], [*negatives, disjunct], database, proof)
    cnf, lrat = OUT/f'{label}.cnf', OUT/f'{label}.lrat'
    write_cnf(cnf, selectors[-1], trial)
    write_proof(lrat, proof)
    native_checks(label, cnf, lrat)
    return {'status': 'CANONICAL_ENTAILMENTS_CHECKED', 'factors': group, 'translations': translations,
            'cnf_sha256': digest(cnf), 'lrat_sha256': digest(lrat), 'steps': len(proof),
            'lrat_bytes': lrat.stat().st_size}


def close_trie(original, clauses, selected, data, source, plan):
    originals = len(clauses)
    results = {}
    for group_number, group in enumerate(data['shards']):
        label = f'canonical-{group_number}'
        receipt = json.loads((OUT/f'{label}-coverage.json').read_bytes())
        assert receipt['status'] == 'CANONICAL_ENTAILMENTS_CHECKED' and receipt['factors'] == group
        assert receipt['cnf_sha256'] == digest(OUT/f'{label}.cnf')
        assert receipt['lrat_sha256'] == digest(OUT/f'{label}.lrat')
        assert 's VERIFIED UNSAT' in (OUT/f'{label}-cake.stdout').read_text().splitlines()
        assert 'c VERIFIED' in (OUT/f'{label}-independent.stdout').read_text().splitlines()
        for row in receipt['translations']:
            key = row['factor'], row['shift']
            assert key not in results and key[0] in group
            results[key] = row['clause']
    lemma_ids, leaf_lemmas, additions = {}, {}, []
    for item in selected:
        factor, delta = key = item['factor'], item['shift']
        assert key not in lemma_ids and key in results
        lemma = [(-1 if bit == '1' else 1) * (7 + delta + j) for j, bit in enumerate(factor)]
        assert lemma == results[key]
        additions.append(lemma)
        lemma_ids[key] = originals + len(additions)
        for word in item['leaves']:
            assert word not in leaf_lemmas and word[delta:delta+len(factor)] == factor
            leaf_lemmas[word] = lemma_ids[key]
    assert results.keys() == lemma_ids.keys()
    projection = plan['projection']
    words = json.loads(pin(source/projection['file'], projection['sha256']))['target']['words']
    assert len(set(words)) == len(words) == 170
    blockers = [[(7 + j) * (-1 if word & (1 << j) else 1) for j in range(16)] for word in words]
    assert clauses[5044:] == blockers
    blocker_ids = {word: 5045 + i for i, word in enumerate(words)}
    leaves = list(prefix_partition(words, 16))
    partition = plan['partition']
    expected = json.loads(pin(source/partition['file'], partition['sha256']))
    assert leaves == [(item['prefix_in_variable_order'], item['retained']) for item in expected]
    assert {word for word, retained in leaves if not retained} == leaf_lemmas.keys()
    assert sum(1 << (16 - len(word)) for word in leaf_lemmas) == 65366
    database = dict(enumerate(clauses + additions, 1))
    proof, trie = [], {}
    internal = set()
    for word, retained in leaves:
        if retained:
            trie[word] = blocker_ids[int(word[::-1], 2)]
        else:
            leaf_clause = [(7 + j) * (-1 if bit == '1' else 1) for j, bit in enumerate(word)]
            trie[word] = add_step(leaf_clause, [leaf_lemmas[word]], database, proof)
        internal.update(word[:j] for j in range(len(word)))
    for word in sorted(internal, key=lambda w: (-len(w), w)):
        prefix_clause = [(7 + j) * (-1 if bit == '1' else 1) for j, bit in enumerate(word)]
        trie[word] = add_step(prefix_clause, [trie[word+'0'], trie[word+'1']], database, proof)
    assert len(trie) == 3101 and proof[-1][1] == []
    try:
        rup_hints([], [trie['0']], database)
    except ValueError as error:
        assert str(error) == 'NO_RUP_CONFLICT'
    else:
        raise AssertionError('ONE_ROOT_CHILD_ACCEPTED')
    cnf, lrat = OUT/'coverage.cnf', OUT/'coverage.lrat'
    header, original_body = original.split(b'\n', 1)
    assert header == b'p cnf 910 5214'
    suffix = ''.join(' '.join(map(str, [*clause, 0]))+'\n' for clause in additions).encode()
    cnf.write_bytes(f'p cnf 910 {originals + len(additions)}\n'.encode() + original_body + suffix)
    assert read_cnf(cnf.read_bytes()) == (910, clauses + additions)
    write_proof(lrat, proof)
    native_checks('coverage', cnf, lrat)
    return {'status': 'COMPOSITE_ORIGINAL_CNF_COVERAGE_CHECKED', 'original_sha256': hashlib.sha256(original).hexdigest(),
            'original_clauses': originals, 'retained_words': len(blockers), 'absent_leaves': len(leaf_lemmas),
            'translated_entailments': len(lemma_ids), 'trie_steps': len(proof), 'cnf_sha256': digest(cnf),
            'lrat_sha256': digest(lrat), 'lrat_bytes': lrat.stat().st_size}


def main():
    plan_path, mode = sys.argv[1:]
    plan = json.loads(Path(plan_path).read_bytes())
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (12 if soft == resource.RLIM_INFINITY else min(12, soft), hard))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    for path, sha in plan['tool_sha256'].items():
        pin(path, sha)
    source = Path(os.environ['RETURN13_SOURCE_ROOT'])
    original = pin(os.environ['RETURN13_ORIGINAL_CNF'], plan['original_cnf_sha256'])
    variables, clauses = read_cnf(original)
    assert (variables, len(clauses)) == (910, 5214)
    selection = plan['selection']
    data = json.loads(pin(source/selection['file'], selection['sha256']))
    selected = data['selected']
    all_factors = [factor for group in data['shards'] for factor in group]
    assert len(selected) == 1046 and len(set(all_factors)) == len(all_factors) == 141
    assert set(all_factors) == data['proofs'].keys()
    if mode == 'trie':
        receipt = close_trie(original, clauses, selected, data, source, plan)
        label = 'trie'
    else:
        group = int(mode)
        label = f'canonical-{group}'
        receipt = canonical_shard(label, clauses[:5044], selected, data, data['shards'][group], source)
    (OUT/f'{label}-coverage.json').write_text(json.dumps(receipt, indent=2)+'\n')
    REPORT['status'] = receipt['status']
    guard.thermal()
    guard.save()
    print('RETURN13_COVERAGE_STEP_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
