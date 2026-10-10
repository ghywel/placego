#!/usr/bin/env python3
"""GC1026 / W283: seven-cell certificate for a universal failed-gate exit packet.

Registered in RULE30-GPT before the full23-cell cone and free-input checks.
All65536 exact cones gave white trace101000100001. Keeping seven cells
and allowing completely independent site8 inputs proves the same packet.
Six retained cells fail at time16 on an exterior stream beginning10.
Finite proof premises only; no claim of permanent synchronization.

Record searched: train + exit/entrance -> GC1017/1019/1023; no packet claim.
Predictions (registered in RULE30-GPT before the corresponding runs):
P1: prefix1001101 forces the white packet through22 for every exact cone.
P2 (after P1): seven cells plus arbitrary site8 suffice, with no width sweep.
Controls: literal Rule30 agrees with packed gates; all exact images match.
Counterfactual: six cells and free site7 suffice. REFUTED-BY: stream1000...
changes the time16 bit but violates site7's own equation at time1.
Unexpected check: restore precisely that missing cell's temporal equation.
OUTCOME: P1/P2 hold;512 local gates and22 complete image steps pass;
65536 exact cones agree; the genuine seven-ring with gate0 keeps the train.
Proof candidate W283, independent review pending. No all-depth bound.
"""
from itertools import product

ROWS = (
 (89,), (79,), (112,), (24,), (45,109), (37,101), (60,124), (6,70),
 (10,74,106), (27,43,91,123), (8,40,72,104), (28,44,92,108,124),
 (7,39,71,103), (9,57,73,105,121), (14,30,46,78,94,126),
 (3,19,35,67,83,99,115), (4,28,52,60,68,92,100,116,124),
 (6,14,22,38,62,70,78,86,102,110),
 (2,10,18,34,50,58,66,74,82,106,114,122),
 (7,11,27,31,43,55,63,71,75,91,95,103,119,123,127),
 (0,8,16,24,32,40,56,64,72,80,88,96,104,120),
 (0,12,28,44,48,56,64,76,88,92,96,108,112,120,124),
 (1,7,13,23,25,39,49,65,71,77,87,89,97,103,119),
)


def packed(r, wall, u, width=7):
    p = r | (u << width)
    return (((p << 1) | wall) ^ (p | (p >> 1))) & ((1 << width)-1)


def literal(r, wall, u):
    p = [wall] + [(r >> j) & 1 for j in range(7)] + [u]
    return sum(((30 >> (4*p[j]+2*p[j+1]+p[j+2])) & 1) << j for j in range(7))


def main():
    for r, wall, u in product(range(128), range(2), range(2)):
        assert literal(r, wall, u) == packed(r, wall, u)
    for t in range(22):
        assert {literal(r, t % 2, u) for r in ROWS[t] for u in (0,1)} == set(ROWS[t+1])
    assert all(len({r & 1 for r in row}) == 1 for row in ROWS)
    full = ''.join(str(row[0] & 1) for row in ROWS)
    assert full[::2] == '101000100001'
    for tail in range(1 << 16):
        r, out = 89 | (tail << 7), []
        for t in range(23):
            out.append(str(r & 1))
            r = ((r << 1) | (t % 2)) ^ (r | (r >> 1))
        assert ''.join(out) == full
    # Six-cell relaxation: arbitrary site7 loses its own temporal equation.
    r, out = 25, []
    for t in range(17):
        out.append(r & 1)
        r = packed(r, t % 2, int(t == 0), 6)
    assert out[16] != int(full[16])
    # This stream asks site7 to change1->0 with site6=0, impossible for either site8.
    assert {0 ^ (1 | v) for v in (0,1)} == {1}
    ring = ('0100110','1111101','0000001','1000011')
    for t in range(4):
        r = tuple(map(int,ring[t]))
        assert tuple(r[(i-1)%7] ^ (r[i] | r[(i+1)%7]) for i in range(7)) == tuple(map(int,ring[(t+1)%4]))
    control = ''.join(ring[t%4][1] for t in range(0,23,2))
    assert control == '10'*6 and control != full[::2]
    # GC1027: preannounced endpoint audit on Cloud's retained CL193 model.
    seed = ('011111100111010100110001100011001001011110110010011010001010'
            '01111011100010100110111010000000000000000')
    r = list(map(int, seed))
    history = []
    for t in range(101):
        history.append(r)
        p = [t % 2] + r + [0]
        r = [(30 >> (4*p[j]+2*p[j+1]+p[j+2])) & 1 for j in range(len(r))]
    q, v = '000010001010000', '0010000101'
    assert ''.join(str(history[t][0]) for t in range(0,101,2)) == q+'10'*13+v
    for n in range(5,14):
        for j in range(1,n-1):
            assert history[30+4*j][:6] == [1,0,0,1,1,0]
        for j in range(1,n-2):
            assert history[30+4*j][6] == 0
        assert history[30+4*n][0] == 1 ^ history[30+4*(n-2)][6]
    assert history[70][6] == 0 and history[74][6] == 1
    assert history[78][:6] != [1,0,0,1,1,0]  # old last-car interface fails
    assert ''.join(str(history[t][0]) for t in range(82,97,2)) == '00100001'
    # GC1029: next white0 is automatic; final exit1 has three hidden targets.
    targets = set()
    for r in ROWS[22]:
        outcomes = set()
        for exterior in range(16):
            state = r
            for t in range(4):
                state = literal(state,t%2,(exterior>>t)&1)
                if t == 1:
                    assert state & 1 == 0
            outcomes.add(state & 1)
        assert outcomes == {int((r & 6) == 0 and (r & 24) != 0)}
        if outcomes == {1}:
            targets.add(r)
    assert targets == {25,49,89}
    # GC1029 backward separator, preregistered in RULE30-GPT.
    # P: a unique successful intermediate row exists after branching.
    # Control: exact forward image table above; unexpected may/must distinction.
    # OUTCOME: at offset7 only row6 can reach the final1; row6 is not sufficient.
    may = [set() for _ in ROWS]
    must = [set() for _ in ROWS]
    may[22] = must[22] = {25,49,89}
    for t in range(21,-1,-1):
        for r in ROWS[t]:
            nxt = {literal(r,t%2,u) for u in (0,1)}
            if nxt & may[t+1]:
                may[t].add(r)
            if nxt <= must[t+1]:
                must[t].add(r)
    assert may[7] == {6} and must[7] == set()
    assert [len(may[t]) for t in range(8,23)] == [2,2,2,2,2,3,3,3,3,4,4,3,3,3,3]
    # Independent forward weighted propagation uses the packed formula.
    counts_at_target = []
    for initial in (6,70):
        counts = {initial:1}
        for t in range(7,22):
            nxt = {}
            for r,n in counts.items():
                for u in (0,1):
                    v = packed(r,t%2,u)
                    nxt[v] = nxt.get(v,0)+n
            counts = nxt
        assert sum(counts.values()) == 32768
        counts_at_target.append(sum(counts.get(r,0) for r in (25,49,89)))
    assert counts_at_target == [11904,0]
    assert history[81][:7] == [0,1,1,0,0,0,0]  # actual positive failed gate74
    print('PASS: backward separator row6 at7; forward continuation counts11904,0')
    # GC1030 exact13-tick transport, preregistered in RULE30-GPT.
    # Wrong-phase countercontrol failed: both phases obey the identity.
    # Repaired negative control: site7=1 erases the first exterior bit.
    ends = {(0,0):{27,37,43,47,79,91,101,111,123},
            (0,1):{6,14,22,38,62,70,78,86,102,110},
            (1,0):{7,25,39,45,89,103,109},
            (1,1):{4,24,28,40,52,60,68,88,92,100,104,116,120,124}}
    for phase in (0,1):
        for first in (0,1):
            states = {literal(9,phase,first)}
            for t in range(1,13):
                states = {literal(r,(phase+t)%2,u) for r in states for u in (0,1)}
            assert states == ends[phase,first]
            assert {r&1 for r in states} == {1-first}
        for stream in range(8192):
            r = 9
            for t in range(13):
                r = packed(r,(phase+t)%2,(stream>>t)&1)
            assert (r&1) == 1-(stream&1)
        for tail in range(128):
            row = [(9>>j)&1 for j in range(7)]+[(tail>>j)&1 for j in range(7)]
            for t in range(13):
                p = [(phase+t)%2]+row
                row = [(30>>(4*p[j]+2*p[j+1]+p[j+2]))&1 for j in range(len(row)-1)]
            assert row == [1-(tail&1)]
        bad = []
        for stream in (0,1):
            r = 73
            for t in range(13):
                r = literal(r,(phase+t)%2,(stream>>t)&1)
            bad.append(r&1)
        assert bad == [1,1]  # first1 violates claimed complement after site7 flip
    print('PASS GC1030: both phases, 16384 streams, 256 cones; site7 masking control')
    print('PASS: GC1029 240 continuations; final exit1 iff state22 in25,49,89')
    print('PASS: GC1027 endpoint identities on retained CL193 model, n=5..13')
    print('PASS: 512 literal gates, 22 exact image transitions, 65536 cones and countercontrols')
    print('full trace:',full,'; white trace:',full[::2])


if __name__ == '__main__':
    main()
