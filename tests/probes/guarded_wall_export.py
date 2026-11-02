#!/usr/bin/env python3
"""GC2398: export P1024 guarded clauses and ORIGINAL-CNF proof obligations.

No solver and no augmented CNF is produced. See the GC2398 report.
"""
import argparse
import hashlib
import json
from pathlib import Path
import runpy

SE_SHA = 'eeb62a45f0dc278d887b63bed66c1d65f8e25f360431fc05963c601c96928e47'
FILE_LIMIT = 16*1024*1024


def clause(p, cols, k, D, j, t, word):
    if p != 1024 or not 2 <= j <= D-11 or not 0 <= t < p or not 0 <= word < 256:
        raise ValueError('unsupported phase, depth, time or word')

    def mismatch(i):
        var = i*p+t+1
        return -var if (cols[(k-i) % len(cols)] >> t) & 1 else var

    return ([-mismatch(j)] + [mismatch(i) for i in range(2, j)] +
            [(-1 if (word >> (h-1)) & 1 else 1)*mismatch(j+h) for h in range(1, 9)])


def bounded_write(path, lines):
    sha = hashlib.sha256()
    size = 0
    with path.open('xb') as f:
        for line in lines:
            raw = line.encode()
            size += len(raw)
            if size > FILE_LIMIT:
                raise RuntimeError('fixed file limit reached; preserve partial output, no retry')
            f.write(raw)
            sha.update(raw)
    return {'sha256': sha.hexdigest(), 'bytes': size}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--states', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--D', type=int, required=True)
    ap.add_argument('--k', type=int, default=0)
    a = ap.parse_args()
    if not 1 <= a.D <= 64 or not 0 <= a.k < 1024:
        ap.error('frozen implementation supports D1..64 and k0..1023 only')
    raw = a.states.read_bytes()
    if hashlib.sha256(raw).hexdigest() != SE_SHA:
        raise ValueError('state source differs from the independently checked certificate')
    states = sorted((int(c), int(w, 2)) for line in raw.decode().splitlines()
                    if line and not line.startswith('#') for c, w in [line.split()])
    if len(states) != 389 or len(set(states)) != 389 or any(not 0 <= c < 1024 or not 0 <= w < 256 for c,w in states):
        raise ValueError('invalid state table')
    here = Path(__file__).resolve().parent
    source = here/'upward_rigid.py'
    lib = runpy.run_path(str(source), run_name='guarded_export_library')
    p, cols, _ = lib['phases']()['P1024']
    if p != 1024 or any(cols[n] != sum(((cols[0] >> ((t+195*n) % p)) & 1) << t for t in range(p)) for n in range(len(cols))):
        raise ValueError('actual column dictionary is not the carried195 convention')
    nv, base = lib['cnf'](p, cols, a.k, a.D)
    a.out.mkdir(parents=False, exist_ok=False)
    receipt = {'status': 'OBLIGATIONS_ONLY_NOT_CERTIFIED', 'p': p, 'k': a.k, 'D': a.D,
               'base_generator_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
               'state_sha256': SE_SHA, 'variables': nv, 'base_clauses': len(base)}
    receipt['base'] = bounded_write(a.out/'original.cnf',
        iter([f'p cnf {nv} {len(base)}\n'] + [' '.join(map(str,c))+' 0\n' for c in base]))

    def obligations():
        for j in range(2, a.D-10):
            depth = a.D+1-j
            for c, word in states:
                t = (c-195*(a.k-j)) % p
                lits = clause(p, cols, a.k, a.D, j, t, word)
                yield json.dumps({'j': j, 'depth': depth, 'time': t, 'phase': c, 'word': word,
                    'clause': lits, 'negated_clause_units': [[-lit] for lit in lits],
                    'contradiction_horizon': 3*(a.D-depth),
                    'original_sha256': receipt['base']['sha256'],
                    'required_proof': 'original.cnf AND these units is UNSAT; no proof included'})+'\n'
    receipt['obligations'] = bounded_write(a.out/'obligations.jsonl', obligations())
    receipt['obligation_count'] = max(0,a.D-12)*389
    (a.out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__ == '__main__':
    main()
