"""GC1116: one spatial interface of the paired-L age presentation.

Missing inference: can GC1115's latest-L age carry the FULL paired
left20 trace and close under spatial forcing? Build the exact temporal
grammar M_k=SLLS^k, k=1..3; no CA-membership or Local solver work.
Record searched: GC1115|renewal.*age|latest.*L|age.*quotient with
22.*state|24.*state|odd.*22|branch|closure ->19 hits12 files;
left.?20|GC1115|paired.*trace|image.*language with decorat|iterate|
closed|odd.*track|age ->41 hits15 files. No matching age interface.
P1 BEFORE controls: 22 states (first-L age A0..4, second-L age B0..16)
determine paired cols19/20 at physical time2u-14/2u-13 and paired21.
P2: paired22 fails ONLY in its odd component at B10/B13; keeping
the current edge (24 possibilities) repairs this particular interface.
Counterfactual: current age is spatially closed; the branch successors
have identical current q,b but different q_(u+4), so odd22 refutes it.
Independent controls: literal truth-table inverse triangles against
the paired update, and GC1110 positive-code emissions against b.
Unexpected check: q through u+3 agrees across the undecided resets,
but q at u+4 differs; the exact newest-source coefficient is one.
Refuted by any node ambiguity at19..21, any other ambiguity at22,
or any paired22 ambiguity after retaining the current temporal edge.
OUTCOME: P1/P2 HELD on all44 local paths, covering22 centered states
and24 centered edges. Original physical macro spellings independently
give exactly the same length12 q language. Both branch counters have
q windows001001001000 versus001001001001 and paired22 outputs01
versus00. Age-only spatial closure is REFUTED; the edge lift repairs
cols21/22, with no claim about further depths.
Only this named interface is tested. No nearby-depth sweep, CUT,
records, actual right realization or all-depth closure is inferred.
"""
from collections import defaultdict
from itertools import product


STATES = tuple(('A', i) for i in range(5)) + tuple(('B', i) for i in range(17))


def successors(s):
    kind, i = s
    if kind == 'A':
        return (('A', i + 1),) if i < 4 else (('B', 0),)
    if i == 16:
        return (('A', 0),)
    if i in (10, 13):
        return (('A', 0), ('B', i + 1))
    return (('B', i + 1),)


def qbit(s):
    kind, i = s
    return int(i == 0 if kind == 'A' else i in (0, 5, 8, 11, 14))


def bbit(s):
    kind, i = s
    return int(i not in ((1, 4) if kind == 'A' else (1, 4, 6)))


def paths(path):
    if len(path) == 12:
        yield path
    else:
        for nxt in successors(path[-1]):
            yield from paths(path + (nxt,))


def literal(q):
    columns = [[0, 1] * len(q), [v for x in q for v in (1 - x, 1)]]
    for _ in range(2, 23):
        a, b = columns[-1], columns[-2]
        out = []
        for t in range(len(a) - 1):
            parents = [left for left in (0, 1)
                       if (30 >> (4 * left + 2 * a[t] + b[t])) & 1 == a[t + 1]]
            assert len(parents) == 1
            out.append(parents[0])
        columns.append(out)
    return columns


def main():
    nodes = {d: defaultdict(set) for d in (19, 20, 21, 22)}
    edges = defaultdict(set)
    windows = defaultdict(list)
    graph_words = set()
    count = 0
    for start in STATES:
        for p in paths((start,)):
            q = tuple(map(qbit, p))
            graph_words.add(q)
            cols = literal(q)
            s, nxt = p[7:9]
            for d in nodes:
                nodes[d][s].add(tuple(cols[d][:2]))
            edges[s, nxt].add(tuple(cols[22][:2]))
            windows[s].append((q, tuple(cols[22][:2])))
            assert cols[20][0] == bbit(s)
            e19, o19 = cols[19][:2]
            e20, o20 = cols[20][:2]
            e21, o21 = cols[21][:2]
            assert e21 == o20 ^ (e20 | e19)
            assert o21 == cols[20][2] ^ (o20 | o19)
            assert cols[22][0] == o21 ^ (e21 | e20)
            assert cols[22][1] == cols[21][2] ^ (o21 | o20)
            count += 1
    assert all(len(v) == 1 for d in (19, 20, 21) for v in nodes[d].values())
    bad = {s for s, v in nodes[22].items() if len(v) > 1}
    assert bad == {('B', 10), ('B', 13)}, bad
    assert all(len({x[0] for x in v}) == 1 for v in nodes[22].values())
    assert len(edges) == 24 and all(len(v) == 1 for v in edges.values())
    counters = {}
    for s in sorted(bad):
        counter = next((a, b) for a in windows[s] for b in windows[s]
                       if a[0][:-1] == b[0][:-1] and a[0][-1] != b[0][-1])
        assert counter[0][1][0] == counter[1][1][0]
        assert counter[0][1][1] != counter[1][1][1]
        counters[str(s)] = [(''.join(map(str, q)), out) for q, out in counter]
    # At each branch both successor even20 emissions agree. This is
    # why paired21 is a node function even though the edge is unknown.
    assert all({bbit(n) for n in successors(s)} == {1} for s in bad)
    # Independent original physical macro spelling. Twelve samples span
    # at most two boundaries because every macro is at least16 samples;
    # all cyclic triples therefore cover every such grammar window.
    spelled_words = set()
    for ks in product((1, 2, 3), repeat=3):
        letters = ''.join('SLL' + 'S' * k for k in ks)
        h = ''.join('110100' if a == 'S' else '1101000100' for a in letters)
        q = tuple(map(int, h[::2]))
        for t in range(len(q)):
            spelled_words.add(tuple(q[(t + i) % len(q)] for i in range(12)))
    assert spelled_words == graph_words
    print(dict(P1='HELD', P2='HELD', nodes=22, edges=24,
               local_paths=count, counters=counters,
               age_spatial_closure='REFUTED', all_depth_bound='OPEN'))
    print('state e19o19 e20o20 e21o21 e22o22_by_successor')
    for s in STATES:
        pairs = [''.join(map(str, next(iter(nodes[d][s])))) for d in (19, 20, 21)]
        print(s, *pairs, [(n, next(iter(edges[s, n]))) for n in successors(s)])


if __name__ == '__main__':
    main()
