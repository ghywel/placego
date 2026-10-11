"""GC1094: classify the third-image intersection, retaining both origins.

Missing inference: GC1093 cannot be iterated by assuming images commute
with intersection. Record searched: parity.image|phase.intersection|
white.parity with later|third|intersection|merger ->5 hits in3 files,
GC1093 source and unrelated parity references; no third-image theorem.
Predictions before graph: P1 third intersection exactly zero/one; P2
even if P1 fails, all its bi-infinite outputs die within2 ticks. Both
HELD. Every intercomponent bridge was included in the unexpected check;
none survives. Dropping either origin permits fixed checkerboard.
Adaptive finite prediction: white parity on[a-3,b+3], odd-q-periodic
third image on[a,b], b-a>=q+16 imply F^4 white on[a+2,b-q-14].
64-state rank certificate, literal/packed packets and exterior controls
verify it. No solver, visible-period census or record computation.
No all-time intersection identity or all-depth prize bound follows.
"""
from itertools import product

from rule30_forced_odd_period_bridge import evolve
from rule30_two_step_parity_bridge import TABLE, word


CYCLES = (
    ('000000',),
    ('011101', '110011', '101110'),
    ('011110', '110101', '101011'),
    ('011011', '110110', '101101'),
)
# A certificate for the graph after deleting its ten cycle edges.
# Every other edge strictly decreases this height, including departures.
HEIGHTS = (
    '000000 000001 000111 001001 001010 001011 001100 001101 '
    '001110 001111 010001 010111 011000 011001 011111 100011 '
    '100101 101000 101001 101111 110001 110110 110111 111001 '
    '111010 111011 111100 111101 111110 111111',
    '000010 000011 000101 000110 001000 010000 010110 011011 '
    '011110 100000 100100 110011 110100 111000',
    '000100 010010 010100 011010 100001 100010 100111 101011 101100',
    '010101 100110 110000 110010',
    '010011 011100 011101 101110',
    '101010 101101',
    '110101',
)


def build(depth):
    states = list(product((0, 1), repeat=2*depth))
    edges = []
    for state in states:
        z, u = state[:depth], state[depth:]
        for g, h in product((0, 1), repeat=2):
            first = tuple(v for bit in z+(g,) for v in (bit, 0))
            second = tuple(v for bit in u+(h,) for v in (0, bit))
            if depth % 2 == 0:
                first = tuple(v for bit in z+(g,) for v in (0, bit))
                second = tuple(v for bit in u+(h,) for v in (bit, 0))
            a = evolve(first, depth)[depth]
            b = evolve(second, depth)[depth]
            if depth == 3:
                A, B, C = z
                D, E, F = u
                assert a == (A ^ B ^ ((1-C) & g), B | C | g)
                assert b == (D | E | F, D ^ E ^ ((1-F) & h))
            if a == b:
                target = z[1:]+(g,)+u[1:]+(h,)
                edges.append((word(state), word(target), word(a)))
    return [word(s) for s in states], edges


def verify_certificate():
    states2, edges2 = build(2)
    assert {s: tuple(sorted((t, out) for a, t, out in edges2 if a == s))
            for s in states2} == TABLE
    states, edges = build(3)
    heights = {s: height for height, group in enumerate(HEIGHTS)
               for s in group.split()}
    assert len(heights) == sum(len(group.split()) for group in HEIGHTS) == 64
    assert set(heights) == set(states)
    recurrent = {(cycle[i], cycle[(i+1) % len(cycle)])
                 for cycle in CYCLES for i in range(len(cycle))}
    recurrent_states = {s for s, _ in recurrent}
    assert len(edges) == 64 and len(recurrent) == 10
    assert recurrent <= {(s, t) for s, t, _ in edges}
    for s, t, out in edges:
        if (s, t) in recurrent:
            assert out == ('00' if s == '000000' else '11')
        else:
            assert heights[t] < heights[s]
            assert t not in recurrent_states
    s, chain = '110101', ['110101']
    while heights[s]:
        t = next(t for a, t, _ in edges if a == s
                 and (a, t) not in recurrent and heights[t] == heights[s]-1)
        chain.append(t)
        s = t
    assert len(chain) == 7
    # This explicit certificate includes every edge between components;
    # such an edge cannot continue forever or reenter a cycle.
    paths = 0
    outgoing = {s: [(t, out) for a, t, out in edges if a == s]
                for s in states}

    def walk(s, left, first=None):
        nonlocal paths
        if not left:
            assert first in recurrent
            paths += 1
            return
        for t, _ in outgoing[s]:
            walk(t, left-1, first if first is not None else (s, t))

    for s in states:
        walk(s, 7)
    # Both constant outputs occur with both origin parities.
    ancestor = (0, 0, 1, 0, 1, 0)*8
    assert all(evolve(ancestor, 3)[3])
    assert all(evolve(ancestor[3:]+ancestor[:3], 3)[3])
    assert not any(evolve((0,)*48, 3)[3])
    return paths


def finite_controls():
    fixtures = rejected = 0
    for q in (1, 3, 5, 7, 9):
        a, b = 10, 10+q+24
        width = b+14
        for white in (0, 1):
            for z in product((0, 1), repeat=3):
                for exterior in product((0, 1), repeat=4):
                    x = tuple(0 if i % 2 == white else z[(i//2) % 3]
                              for i in range(width))
                    x = exterior + x[4:-4] + tuple(1-v for v in exterior)
                    rows = evolve(x, 4)
                    w = rows[3]
                    if not all(w[i-3] == w[i+q-3]
                               for i in range(a, b-q+1)):
                        rejected += 1
                        continue
                    assert all(x[i] == 0 for i in range(a-3, b+4)
                               if i % 2 == white)
                    assert all(rows[4][i-4] == 0
                               for i in range(a+2, b-q-13))
                    fixtures += 1
    assert evolve((1, 0)*32, 4)[4] == (1, 0)*28
    return fixtures, rejected


def main():
    paths = verify_certificate()
    fixtures, rejected = finite_controls()
    print(dict(third_image_packets=256, hidden_states=64,
               graph_edges=64, recurrent_edges=10, maximum_exit=6,
               seven_edge_paths=paths, finite_fixtures=fixtures,
               rejected_premises=rejected, even_q_counterexample='PASS',
               third_intersection='ZERO AND ONE PROOF-SKETCH',
               finite_odd_q_bridge='ALL q PROOF-SKETCH',
               all_time_iteration='OPEN', prize_bound='OPEN'))


if __name__ == '__main__':
    main()
