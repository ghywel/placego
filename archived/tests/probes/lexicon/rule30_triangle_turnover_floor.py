#!/usr/bin/env python3
"""Fixed controls of the turnover floor behind a triangle's rigid fringe.

RUN-ON: cpu, standard-library Python; no solver, census or potential tuning.
COMMAND: python3 tests/probes/lexicon/rule30_triangle_turnover_floor.py

Record searched: triangle/zero-tail with edge-frame/settling ->6hits6files;
compensation/mandatory-source with density/disjoint/turnover ->17hits4files.
GC599/630/631 supply the established moving fringe, GC597/598/632 its
compensation cautions; GC1203/1204/1205 supply the new path source.
The target is a record-conditioned, disjoint nonnegative event floor,
not another fringe theorem or an information-loss estimate.

PREDICTIONS before first execution (2026-10-13):
 T1: d9, both phases, a4/5/9, four fixed six-bit origins and two tails
     (48 cases), have first sources001 for e0,010 for e1. The reference
     inward edge settles Z1=1,Z2=0,Z4=1,Z5=Z6=Z3 by time7; Z3 toggles.
 T2: in the accepted125 fixture's fixed a4..8 block, R=11100, two paths
     have odd turnover past u2; their event anchors are disjoint and
     total turnover >=2 >= max(0,ceil((2N-6)/5)), N5.
 Independent: packed Boolean versus literal Rule30; source parity versus
     signed hole changes, and the already stored actual visible bits.
 Unexpected horizon control: d7,p0,a4,L12, flipping only E+2 changes
     the actual edge cell at time7 but not the first three sources.
     Thus the proof must compare selected cones to a zero-tail reference,
     not assert the full fringe after the finite triangle collapses.
 Counterfactual: distinct events are independent paid seed bits. This
     is not predicted; source overlap/cancellation remains a live guard.
 No larger record or survival scan follows from the lower event bound.

OUTCOME: first harness reached the48 prefix comparisons, then failed
in the d7 horizon control: its origin helper included wall depth0 in
the packed initial row, causing a negative shift. Corrected to retain
only positive depths; the wall remains prescribed, not a seed bit.
Corrected T1/T2 pass:48 fixed prefixes, finite-band counter and216
distinct tail-turnover anchors in the actual five-path block.

T3 ADDENDUM before its execution: subtract source positions j2..5.
For actual visible triple (a,b,c)=(q(k-3),q(k-1),q(k+1)), their values
are c,0,a XOR b XOR c,a XOR b XOR ac, so their parity is ac. The middle
parity (u>=3,j>=6) is b XOR c XOR ac, firing exactly on001 and010.
For the same fixed125 block predict middle parity00011 and210 distinct
middle-turnover anchors. The five-state basic-cut automaton's potentials
O:0,Z1:3,Z2:1,Z3:-1,Z4:-3 certify5*weight-2 >= potential change;
range6 gives ceil((2N-6)/5). Independent finite-boundary counter:
basic-cut word10100001 produces middle weights01000; the stronger
claim of two payments in every five-letter window is false. No real
membership of that formal counterword is asserted.

T4 ADDENDUM before execution, a discriminator audit: GC634 already
proves Z5=Z6=Z3 from time7 and Z7=0 from time10. Thus for a>=6,d>=8,
source u3 is the toggling Z3 phase if e0, and1 if e1. Check only the
already registered T1 cases at a9 (16 cases): e0 source3 equals its
outer input A, while e1 source3 is1. Those ordinary fringe events alone
meet the proposed event floor after the two a4/5 startup losses.
T3/T4 OUTCOME: near-wall subtraction and210 middle anchors match;
the finite potential and boundary counter pass. All16 existing age9
cases match the ordinary u3 contribution. This refutes the inference
that the count floor supplies a new price; no further strip enlargement,
source-count sweep or tuning.
"""
import json
from pathlib import Path
from rule30_zero_triangle_guard_transport import packed, literal
from rule30_zero_triangle_adjacent_charge import path


def origin(d, bits):
    out = {d - 1: 1}
    out.update({d - 2 - i: int(b) for i, b in enumerate(bits) if d - 2 - i > 0})
    return out


def main():
    total = 0
    for bits in ('000000', '111111', '101010', '010101'):
        for phase in (0, 1):
            d = 9
            e = 1 ^ ((d + phase) % 2)
            for a in (4, 5, 9):
                k = d + 2 * a + e
                end = k + 3
                for tail in (0, 1):
                    seed = origin(d, bits)
                    seed[end + 1], seed[end + 3] = tail, 1 - tail
                    rows = packed(seed, phase, k + 2, 2 * k + 9)
                    assert rows == literal(seed, phase, k + 2, 2 * k + 9)
                    _, sources = path(rows, phase, d, a, e)
                    assert sources[:3] == ([0, 0, 1] if e == 0 else [0, 1, 0])
                    if a == 9:
                        t, j = a + 4, k - (a + 1) - 3
                        assert sources[3] == (rows[t][j + 2] if e == 0 else 1)
                    total += 1
    d, a, phase, end = 7, 4, 0, 18
    seed = origin(d, '000000')
    rows0 = packed(seed, phase, 17, 40)
    seed[end + 2] = 1
    rows1 = packed(seed, phase, 17, 40)
    assert rows1 == literal(seed, phase, 17, 40)
    assert rows0[7][13] ^ rows1[7][13] == 1
    assert path(rows0, phase, d, a, 0)[1][:3] == path(rows1, phase, d, a, 0)[1][:3] == [0, 0, 1]
    root = Path(__file__).resolve().parents[3]
    records = json.loads((root / 'site/wolframcollatzmahler/data/records.json').read_text())['rows']
    f = next(r for r in records if r['depth'] == 125 and r['phase'] == 1)
    assert f['L'] == 21 and len(f['left']) == 145 and f['left'][123] == '1'
    seed = {j: int(b) for j, b in enumerate(f['left'], 1)}
    rows = packed(seed, 1, 144, 290)
    assert rows == literal(seed, 1, 144, 290)
    events, middle_events, Rs, middle_bits, odd = set(), set(), [], [], 0
    for a in range(4, 9):                 # fixed registered five-path block
        old, sources = path(rows, 1, 125, a, 1)
        assert sources[:3] == [0, 1, 0]
        r = sum(sources[:-1]) % 2
        k, crop, n = 126 + 2 * a, a + 1, 125 + a
        pair = tuple(int(f['visible'][(t - 1) // 2]) for t in (k - 1, k + 1))
        assert rows[k][1] == rows[k + 2][1] == 1
        assert r == (1 - pair[0]) * (1 - pair[1])
        tail = sources[3:-1]
        assert sum(tail) % 2 == 1 ^ r
        abc = tuple(int(f['visible'][(t - 1) // 2]) for t in (k - 3, k - 1, k + 1))
        va, vb, vc = abc
        near = [sources[-j] for j in (2, 3, 4, 5)]
        assert near == [vc, 0, va ^ vb ^ vc, va ^ vb ^ (va * vc)]
        mid = sum(sources[3:-5]) % 2
        assert mid == vb ^ vc ^ (va * vc)
        middle_bits.append(mid)
        odd += sum(tail) % 2
        for u in range(3, n - 1):
            if sources[u]:
                t, j = crop + u, n - u
                newhole = (1 - rows[t + 1][j + 1]) * (1 - rows[t + 1][j])
                assert abs(newhole - old[u]) == 1
                assert (t, j) not in events and t + j == k
                events.add((t, j))
                if j >= 6:
                    assert (t, j) not in middle_events
                    middle_events.add((t, j))
        Rs.append(r)
    assert Rs == [1, 1, 1, 0, 0] and odd == 2
    assert len(events) >= 2 >= max(0, (2 * len(Rs) - 6 + 4) // 5)
    assert middle_bits == [0, 0, 0, 1, 1] and len(middle_events) == 210
    potentials = {'O': 0, 'Z1': 3, 'Z2': 1, 'Z3': -1, 'Z4': -3}
    edges = [('O','Z1',1), ('Z1','O',0), ('Z1','Z2',0), ('Z2','O',1),
             ('Z2','Z3',0), ('Z3','O',1), ('Z3','Z4',0), ('Z4','O',1)]
    assert all(5 * w - 2 >= potentials[v] - potentials[u] for u,v,w in edges)
    assert max(potentials.values()) - min(potentials.values()) == 6
    formal = [int(b) for b in '10100001']
    assert all(not (formal[i] and formal[i+1]) for i in range(len(formal)-1))
    assert '00000' not in ''.join(map(str, formal))
    weights = [formal[i] ^ formal[i+1] ^ (formal[i-1] * formal[i+1]) for i in range(1,6)]
    assert weights == [0,1,0,0,0] and sum(weights) == 1
    print('T1 PASS:', total, 'fixed source prefixes, independent engines.')
    print('Sharp finite-band edge counter PASS: edge flips, prefix001 stays.')
    print('T2 PASS: R11100, two odd compensation paths,', len(events), 'distinct tail-turnover anchors.')
    print('T3 PASS: near-wall subtraction, middle00011,210 distinct anchors, finite potential and boundary counter.')
    print('T4 PASS:16 existing age9 cases; the ordinary fringe already pays the event count. Stop count-only pricing.')


if __name__ == '__main__':
    main()
