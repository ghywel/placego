"""GC2626: lag-16 saturation and permanent agreement for the fixed CL721 alignments.

Read only the named seeds, shifts and last observed crossing ticks. The right
cut is exact because the wall-frame update is triangular. No search for a shift.
"""
import hashlib
import json
import os
from array import array
from collections import deque
from pathlib import Path

P, BARRIER, T, ANCHOR = 16, 87867, 122880, 11999
WIDTH = BARRIER + 1
MASK = (1 << WIDTH) - 1
NBYTES = (WIDTH + 7) // 8
OUT = Path(os.environ["CAPPED_OUT"])


def step(row):
    return ((row << 2) ^ ((row << 1) | row)) & MASK


def first(word):
    return (word & -word).bit_length() - 1 if word else WIDTH


def trace(seed, end, snapshots):
    row = seed
    ring = deque(maxlen=P+1)
    edges = array('I')
    retained = {}
    for t in range(end+1):
        ring.append(row)
        if t in snapshots:
            retained[t] = row
        if t >= P:
            edges.append(first(ring[0] ^ row))
        row = step(row)
    return edges, retained


def packed(row):
    return row.to_bytes(NBYTES, 'little')


def main():
    os.nice(10)
    path = Path(__file__).with_name('walk_merge.out')
    cases = []
    for line in path.read_text().splitlines():
        tok = line.split()
        if tok and tok[0].startswith('0x'):
            cases.append((int(tok[0],16), int(tok[2]), int(tok[4])))
    assert len(cases) == 20
    # Each terminal cycle is recorded on the original bias-free clock t=T.
    phases = tuple(range(33))
    seed_B, ref = trace(1, T+32, {32768}|{T+d for d in phases})
    assert seed_B[32768] == 24465 and seed_B[T] == BARRIER
    assert ref[T] == ref[T+32] and ref[T] ^ ref[T+16] == 1 << BARRIER
    assert all(not ((ref[T+h] >> (BARRIER-1)) & 1) for h in range(32))
    assert sum((ref[T+h] >> (BARRIER-2)) & 1 for h in range(16)) == 5
    assert all((ref[T+h]^ref[T+h+16]) == (1<<BARRIER) for h in range(17))
    # A one-time state equality modulo 2^WIDTH certifies its entire future.
    (OUT/'seed-cycle.bin').write_bytes(b''.join(packed(ref[T+h]) for h in phases))
    results = []
    for i,(seed,s,old_last) in enumerate(cases):
        edge, y = trace(seed,T+s+32,{32768+s}|{T+s+d for d in phases})
        lo = max(0,-s)
        assert first(y[32768+s]^ref[32768]) > seed_B[32768]
        train_dis = [t for t in range(lo,32770) if seed_B[t] != edge[t+s]]
        assert max(train_dis,default=-1) == old_last
        extended = [t for t in range(32770,T+1) if seed_B[t] != edge[t+s]]
        lag_delta = y[T+s] ^ y[T+s+16]
        same32 = y[T+s] == y[T+s+32]
        difference = y[T+s] ^ ref[T]
        first_d = first(difference)
        prefix16 = first(lag_delta)
        persistent_parent_white = same32 and first_d > 0 and first_d < WIDTH and all(
            ((y[T+s+h] | ref[T+h]) >> (first_d-1)) & 1 == 0 for h in range(32))
        # An evergreen lag equality is certified if both terminal prefixes
        # repeat and have a visible equal mismatch at every phase of that cycle.
        same_saturated_edges = same32 and all(
            first(y[T+s+h]^y[T+s+h+16]) == BARRIER for h in range(16))
        result = dict(i=i, seed=hex(seed),shift=s,old_last=old_last,
                      extra_edge_disagreements=len(extended), first_extra=next(iter(extended),None),
                      last_extra=max(extended,default=None),
                      prefix32_closed=same32, first_lag16_at_T=prefix16,
                      first_pair_mismatch_at_T=first_d, prefix_equal_at_T=not difference,
                      saturated_edges_equal=same_saturated_edges,
                      first_mismatch_parent_white=persistent_parent_white,
                      equal_after_shift_plus16=y[T+s+16] == ref[T])
        results.append(result)
        # Preserve endpoint bytes (distinct observations even when a seed repeats).
        (OUT/f'case-{i:02}.bin').write_bytes(b''.join(packed(y[T+s+h]) for h in (0,16,32)))
    (OUT/'cases.json').write_text(json.dumps(results,indent=2)+'\n')
    # A real second finite initial row at the same wall origin is the seed
    # advanced by 16 ticks; after saturation J=B exactly. The +16 lift heals it.
    descendant=1
    for _ in range(16):
        descendant=step(descendant)
    control={'descendant':hex(descendant),'J':first(ref[T]^ref[T+16]),
             'lag_edge':seed_B[T],'lag_edge_shifted':seed_B[T+16],
             'same_after_other_lift':ref[T]==ref[T+32],
             'seed_cycle_sha256':hashlib.sha256((OUT/'seed-cycle.bin').read_bytes()).hexdigest(),
             'deduplicated_cases':len(set((seed,s) for seed,s,_ in cases))}
    assert control['J']==control['lag_edge']==control['lag_edge_shifted']==BARRIER
    (OUT/'control.json').write_text(json.dumps(control,indent=2)+'\n')
    print('WHITE_PARENT_FIXED_DONE',len(results))


if __name__ == '__main__':
    main()
