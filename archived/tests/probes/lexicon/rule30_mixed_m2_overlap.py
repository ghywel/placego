"""GC1112: which M2-only cuts can touch the reviewed mixed output?

Missing inference: GC1111's reported 120-factor cuts the pure M2
cycle, but could it also destroy GC1106's mixed FE/EF branching?
Resolve this for the explicit reviewed witness language, at every
word length; do not run CA membership, a solver or a wider strip.
Record searched: M2|M_2|LLSSS with longest.*factor|common.*factor|
cut.*FE|FE.*cut|matching.*factor ->9 hits6files; relevant GC1103,
GC1106, GC1111 and the existing exact macro-cut translation read.
P1 BEFORE execution: no M2 factor of length105 occurs in any
concatenation of FE/EF, even across the two-word boundaries.
Hand reason: five complete LL marker triples force four consecutive
19-sample LL spacings; the grammar has at most three k=2 macros.
REFUTED-BY: a matching path of 105 bits in the complete pair graph.
P2 BEFORE execution: the sharp maximum common factor is87 bits.
This is informed by the three k=2 macros between k=1 and k=3:
five matching samples before them, 57 inside, 25 after them.
Counterfactual: a 120-symbol pure-M2 cut destroys this branching.
REFUTED-BY: an all-length avoidance certificate for both generators.
Controls: independent gap-marker and even-physical-h spellings;
complete pair-graph longest path, with a locally verified falling
integer rank on every matching edge; independent cyclic EF witness
attains the maximum. No finite scan is extrapolated to all lengths.
Unexpected check: include occurrences crossing an FE/EF choice
boundary, arbitrary bit phase, and partially visible LL triples.
Negative control: M2 matched with itself must have a directed cycle.
OUTCOME: P1/P2 HELD. The 2,718 matching states form a DAG with
maximum verified rank87. An independent EF cyclic spelling attains
87, and the direct k=1,2,2,2,3 window has nearest mismatches at
T-6 and T+82. The self-period graph cycles as required. Thus every
M2-only cut of length>=88 leaves the reviewed mixed generators
unchanged; a shorter minimized cut could still hit them. This is
an all-length result for the explicit model language, not CA
membership or a realized-record bound. All-depth transport OPEN.
"""

from collections import deque


def spell(ks):
    gaps = [g for k in ks for g in [3, 5, 5] + [3] * k]
    marks, cursor = set(), 0
    for gap in gaps:
        marks.add(cursor)
        cursor += gap
    q = ''.join('1' if i in marks else '0' for i in range(cursor))
    h = {'S': '110100', 'L': '1101000100'}
    physical = ''.join(h['SLL'[i] if i < 3 else 'S']
                       for k in ks for i in range(3+k))
    assert physical[::2] == q
    return q


def pair_graph(words, period):
    # A state records the current generator, its current sample and
    # the M2 sample. The edge consumes the state's matching bit.
    # Every factor of the full concatenation language starts in one
    # of these states; at generator ends both successors are allowed.
    nodes = {(w, i, p) for w, word in enumerate(words)
             for i, bit in enumerate(word) for p, b in enumerate(period)
             if bit == b}
    edges = {}
    for w, i, p in nodes:
        successors = ([(w, i+1)] if i+1 < len(words[w])
                      else [(v, 0) for v in range(len(words))])
        edges[w, i, p] = {(v, j, (p+1) % len(period))
                           for v, j in successors
                           if (v, j, (p+1) % len(period)) in nodes}
    return edges


def rank_certificate(edges):
    indegree = {x: 0 for x in edges}
    for ys in edges.values():
        for y in ys:
            indegree[y] += 1
    ready = deque(x for x, n in indegree.items() if n == 0)
    order = []
    while ready:
        x = ready.popleft()
        order.append(x)
        for y in edges[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                ready.append(y)
    if len(order) != len(edges):
        return None
    rank = {}
    for x in reversed(order):
        rank[x] = 1 + max((rank[y] for y in edges[x]), default=0)
    # Independent local verification is the all-length certificate:
    # a factor of n matching samples entails a path of n states.
    assert all(1 <= r <= 104 for r in rank.values())
    assert all(rank[x] >= 1+rank[y] for x, ys in edges.items() for y in ys)
    return rank


def cyclic_overlap(word, period):
    # A separate literal witness search; not the all-length proof.
    best = 0
    for i in range(len(word)):
        for p in range(len(period)):
            n = 0
            while n < 120 and word[(i+n) % len(word)] == period[(p+n) % len(period)]:
                n += 1
            best = max(best, n)
    return best


def main():
    e, f = (1, 2, 2, 2, 3), (3,)
    words = [spell(f+e), spell(e+f)]
    m2 = spell((2,))
    assert [len(w) for w in words] == [117, 117] and len(m2) == 19
    assert words[0] != words[1]
    edges = pair_graph(words, m2)
    rank = rank_certificate(edges)
    assert rank is not None
    sharp = max(rank.values())
    assert sharp == 87
    # Direct marker proof of sharpness and the two nearest mismatches.
    # T=16 is the first M2 macro after k=1; k=3 starts at T+57.
    local = spell((1, 2, 2, 2, 3, 1))
    reference = ''.join(m2[(i-16) % 19] for i in range(len(local)))
    assert local[11:98] == reference[11:98]
    assert local[10] != reference[10] and local[98] != reference[98]
    assert cyclic_overlap(words[1], m2) == sharp
    assert rank_certificate(pair_graph([m2], m2)) is None
    print(dict(P1='HELD', P2='HELD', matching_states=len(edges),
               longest_matching_factor=sharp, falling_rank='PASS',
               root_boundary_and_bit_phases='included',
               self_period_cycle_control='PASS',
               scope='mixed model language; no actual-language membership'))


if __name__ == '__main__':
    main()
