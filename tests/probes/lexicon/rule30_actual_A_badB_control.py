"""GC1150: independent actual-wall control of CL346's original-A counter.

Priority switch BEFORE experiment: fetched Cloud commit2bd75079 supplies
an actual original676 entrance, so verify that counter before any mixed
white-gap attempt. No mixed-gap experiment was started.
Record searched: mixed|renewal|S/L AND white.gap|zero.run|zero.window|
record|forced.left|density ->322 hits151files; GC708/709/1007/1008,
1107..1110 read. CL346 and both carrier/lift probes read in full.
P1 BEFORE execution: reconstruct44 initial left cells from the saved
right trace, then evolve the FULL finite row WITHOUT clamping; the wall
alternates through44 and the original-A/H/SS/badB observations hold.
P2: first56 right cells suffice for the admission-relevant certificate:
originA13, high13 at16, SS prefixes9 at26/32/38, site5 track16..43,
and badB12 at44. The saved full20 endpoint needs64 cells instead.
Counterfactual: clamping creates the badB and no finite full-row
configuration has this original-A lineage and alternating wall to44.
Independent engines: literal Wolfram table on the full row and a packed
bit engine; every finite padding boundary is outside all tested cones.
Unexpected: vary57..64 and later tails; the badB12 must persist while
the full20 endpoint may change. Keep the endpoint's cone scope distinct.
No Cloud search, 2^23 image census, width-carrier computation, sampler,
Local solver or continuation-fate work. No eventual-admission refutation.
FIRST OUTCOME: P1/P2 passed every control, but the unexpected assertion
that some full20 endpoint changes FAILED: changed20=0 on all256 complete
assignments57..64. The failure is retained; remove that assertion to
report it. Since the full20 cone ends at64, this complete check also
certifies its constancy from the shorter56-cell prefix. No new search.
"""
from itertools import product

ORIGIN = '1110100011011010010010000100100000000000000000000000000000000000'
TABLE = (0, 1, 1, 1, 1, 0, 0, 0)
MACROS = {
    16: '11100111111101001100',
    26: '11101110111100111001',
    32: '11101111011111000101',
    38: '11101011001110011111',
    44: '11101001100101110101',
}
TRACK = '0101101010'+'111010'*3


def right_trace(source):
    row = list(map(int, source))
    v = []
    for t in range(45):
        v.append(row[0])
        if t < 44:
            row = [TABLE[4*(t % 2 if i == 0 else row[i-1])
                         + 2*row[i]+row[i+1]] for i in range(len(row)-1)]
    return v


def left_prefix(v):
    up = [t % 2 for t in range(len(v))]
    right = v
    out = []
    while len(up) > 1:
        left = [up[t+1] ^ (up[t] | right[t]) for t in range(len(up)-1)]
        out.append(left[0])
        right, up = up, left
    return out


def evolve(source, left, engine):
    # Coordinates -90..150: no outside cell can reach [-1,20] in44.
    wall = 90
    row = [0]*241
    for d, b in enumerate(left, 1):
        row[wall-d] = b
    for i, b in enumerate(map(int, source), 1):
        row[wall+i] = b
    snapshots = []
    for t in range(45):
        snapshots.append(tuple(row[wall-1:wall+21]))
        if engine == 'literal':
            row = [TABLE[4*(row[i-1] if i else 0)+2*row[i]
                         +(row[i+1] if i+1 < len(row) else 0)]
                   for i in range(len(row))]
        else:
            b = sum(x << i for i, x in enumerate(row))
            b = ((b << 1) ^ (b | (b >> 1))) & ((1 << len(row))-1)
            row = [(b >> i) & 1 for i in range(len(row))]
    return snapshots


def main():
    assert len(ORIGIN) == 64
    v = right_trace(ORIGIN)
    left = left_prefix(v)
    assert len(left) == 44
    base = evolve(ORIGIN, left, 'literal')
    assert base == evolve(ORIGIN, left, 'packed')
    assert all(r[1] == t % 2 for t, r in enumerate(base))
    assert ''.join(str(base[t][6]) for t in range(16, 44)) == TRACK
    assert ORIGIN[:13] == '1110100011011'
    assert ORIGIN[13:19] == '010010'
    assert ORIGIN[13:25] == '010010010000'
    for t, word in MACROS.items():
        assert ''.join(map(str, base[t][2:])) == word
    # The predicates' backward cones, stated independently of simulations.
    requirements = [(0, 13), (16, 13), (26, 9), (32, 9), (38, 9), (44, 12)]
    requirements += [(t, 5) for t in range(16, 44)]
    assert max(t+k for t, k in requirements) == 56
    assert max(1+t for t in range(44)) == 44  # wall inverse's right observations
    variants = changed20 = 0
    for bits in product('01', repeat=8):
        # Exhaust57..64, with deterministic later-tail controls.
        tail = ('01'*12 if bits[0] == '1' else '10'*12)
        source = ORIGIN[:56]+''.join(bits)+tail
        rows = evolve(source, left, 'literal')
        assert rows == evolve(source, left, 'packed')
        assert all(r[1] == t % 2 for t, r in enumerate(rows))
        assert ''.join(str(rows[t][6]) for t in range(16, 44)) == TRACK
        for t, k in requirements:
            assert rows[t][2:2+k] == base[t][2:2+k]
        changed20 += rows[44][2:] != base[44][2:]
        variants += 1
    print(dict(original_A_counter='CONFIRMED', full_wall_unclamped='PASS',
               literal_packed='PASS', tail_controls=variants,
               changed_full20_endpoints=changed20, required_right_prefix=56,
               initial_left_prefix=''.join(map(str, left)),
               full20_change_prediction='REFUTED',
               three_SS_B_exit_guard='REFUTED',
               eventual_admission='OPEN', all_depth_R_real='OPEN'))


if __name__ == '__main__':
    main()

# OUTCOME: P1/P2 HELD; actual full finite wall through44, no clamp.
# 256 complete57..64 controls, every literal/packed sample agrees.
# Full20-change prediction REFUTED (0 changes), first assertion retained.
# Locality proves56 right cells suffice for admission predicates; the
# complete finite cone also certifies the full20 endpoint from them.
# No minimal-prefix claim, eventual-admission refutation or fate run.
