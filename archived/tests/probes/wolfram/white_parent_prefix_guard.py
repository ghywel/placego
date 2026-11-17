"""Backward deadlines for the one-wheel reset guarantee on the original seed path."""
import hashlib
import json
import os
from pathlib import Path

T, K, CHUNK = 122880, 87867, 512
WIDTH = K+1
MASK = (1 << WIDTH)-1
SIZE = (WIDTH+7)//8
TARGETS = (11999,58287,60550,K)
OUT = Path(os.environ['CAPPED_OUT'])


def step(x):
    return ((x << 2) ^ ((x << 1)|x)) & MASK


def main():
    seed_cycle = Path(os.environ['WHITE_SEED_CYCLE']).read_bytes()
    assert hashlib.sha256(seed_cycle).hexdigest() == '28d6dc60a6157dc39a5d2c9e41bdee6bce00ab562d05ed821ea1c1a724cbae71'
    blocks = [1]
    row = 1
    for t in range(1,T+1):
        row = step(row)
        if t % CHUNK == 0:
            blocks.append(row)
    assert T % CHUNK == 0 and blocks[-1] == int.from_bytes(seed_cycle[:SIZE],'little')
    thresholds = list(TARGETS)
    paths = [bytearray(T) for _ in TARGETS]
    for b in range(len(blocks)-2,-1,-1):
        rows = [blocks[b]]
        for _ in range(CHUNK-1):
            rows.append(step(rows[-1]))
        assert step(rows[-1]) == blocks[b+1]
        for dt in range(CHUNK-1,-1,-1):
            x = rows[dt]
            for i,k in enumerate(thresholds):
                take = int(k > 0 and ((x >> (k-1)) & 1) != 0)
                paths[i][b*CHUNK+dt] = take
                thresholds[i] = k-take

    # Replay the forward guaranteed lower bound from the chosen index and one less.
    need = [v for first in thresholds for v in [first,min(first-1,K)]]
    assert min(need) >= 0
    row = 1
    for t in range(T):
        for i,z in enumerate(need):
            need[i] = min(K,z+((row >> z)&1))
        row = step(row)
    answers = []
    for i,(initial,target) in enumerate(zip(thresholds,TARGETS)):
        assert need[2*i] >= target and need[2*i+1] < target
        assert sum(paths[i]) == target-initial
        name = f'target-{target}.bits'
        payload = bytes(sum(paths[i][q+h] << h for h in range(8)) for q in range(0,T,8))
        (OUT/name).write_bytes(payload)
        answers.append(dict(target=target,initial_last_index=initial,matched_bits=initial+1,
                            endpoint_at_threshold=need[2*i],endpoint_one_less=need[2*i+1],
                            reset_count=sum(paths[i]),certificate=name,sha256=hashlib.sha256(payload).hexdigest()))
    (OUT/'prefix-guards.json').write_text(json.dumps(answers,indent=2)+'\n')
    print('PREFIX_GUARDS_DONE',thresholds)


if __name__ == '__main__':
    main()
