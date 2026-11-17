"""Shortest worst-case observation gap from each anchored phase at wheel 87867.

Reconstruct three lawful period-16 prefix cycles. Flip just the last bit to
realize every temporary lag collision, as a genuine finite row at observation start.
"""
import hashlib
import json
import os
from pathlib import Path
import struct

P, LOW, K = 16, 11998, 87867
SIZE = (K + 8) // 8
MASK = (1 << (K+1)) - 1
LEAVES = {
    0:'28c4a4cedc03b34a827efc87342e76bbaecdfc5b5127d68f40a42300075c4d40',
    2:'781b5c9eedac7413ec838ff3ab1f309def40be09513db1d26cf8a4952525ae15',
    3:'0326baea5f28b89ff8229b914149fc78bdab47c0ff024e078d8df692a8b0690a',
}


def step(x):
    return ((x << 2) ^ ((x << 1) | x)) & MASK


def main():
    tree = Path(os.environ['WHITE_TREE_DIR'])
    out = Path(os.environ['CAPPED_OUT'])
    raw = Path(os.environ['WHITE_SEED_CYCLE']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == '28d6dc60a6157dc39a5d2c9e41bdee6bce00ab562d05ed821ea1c1a724cbae71'
    results, witness_blob = {}, bytearray()
    anchor_mask = (1 << (LOW+2)) - 1
    seed = [int.from_bytes(raw[i*SIZE:(i+1)*SIZE],'little') for i in range(33)]
    assert len({x & anchor_mask for x in seed[:P]}) == P
    for leaf_index, digest in LEAVES.items():
        blob = (tree/f'leaf-{leaf_index}.u16le').read_bytes()
        assert hashlib.sha256(blob).hexdigest() == digest
        words = [v for v, in struct.iter_unpack('<H',blob)]
        assert len(words) == K-LOW+1 and words[-2] != 0
        # Assemble phase zero once. Check all sixteen physical iterates against
        # the certified clock and the two terminal driving words.
        base = bytearray(seed[0].to_bytes(SIZE,'little'))
        for j, word in enumerate(words,LOW):
            mask = 1 << (j%8)
            base[j//8] = (base[j//8] & ~mask) | ((word & 1) << (j%8))
        row = int.from_bytes(base,'little')
        cycle = []
        for r in range(P):
            cycle.append(row)
            assert (row & anchor_mask) == (seed[r] & anchor_mask)
            for j in (K-2,K-1,K):
                assert ((row >> j)&1) == ((words[j-LOW] >> r)&1)
            row = step(row)
        assert row == cycle[0]
        delays = []
        for r, x in enumerate(cycle):
            delay = 1 + next(h for h in range(P) if (words[-2] >> ((r+h) % P)) & 1)
            trial = x ^ (1 << K)
            witness_blob.extend(trial.to_bytes(SIZE,'little'))
            trace = [trial]
            for _ in range(2*P):
                trace.append(step(trace[-1]))
            for i in range(P+1):
                lag = trace[i] ^ trace[i+P]
                assert lag == ((1 << K) if i < delay else 0)
            delays.append(delay)
        results[leaf_index] = dict(near=words[-2],far=words[-3],delays=delays)
    # Permanent positive control has its observed lag edge at K for every phase.
    assert all(seed[r]^seed[r+P] == 1 << K for r in range(P+1))
    assert seed[0]==seed[2*P]
    gate = [max(data['delays'][r] for data in results.values()) for r in range(P)]
    witness = [next(i for i,d in results.items() if d['delays'][r]==gate[r]) for r in range(P)]
    (out/'finite-starts.bin').write_bytes(witness_blob)
    result = dict(phase_zero=122880,indices=list(LEAVES),results=results,gate=gate,
                  attaining_leaf=witness,starts_sha256=hashlib.sha256(witness_blob).hexdigest())
    (out/'short-gate.json').write_text(json.dumps(result,indent=2)+'\n')
    print('SHORT_GATE_DONE',gate)


if __name__ == '__main__':
    main()
