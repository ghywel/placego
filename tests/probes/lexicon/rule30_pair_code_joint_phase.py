"""GC1119: the odd phase makes the pending reset observable now.

Missing inference: GC1116 exposes a next-gap choice in odd22. Does
recovering the full paired interface require a new hidden future queue,
or is that choice already observable in the paired22 trace itself?
Use GC1117's conserved C code and the EXISTING interface, not a depth
sweep, a new CUT query or a proposed canonical return.
Record searched: GC1117|left22|odd22|paired.?22 with causal|16.sample|
next.even|past.*state|observable.*edge|one.tick ->2 hits2files,
only the status board and CL295 adoption; GC1116/1117 reused.
P1 BEFORE execution: on the18-state paired-L grammar with arbitrary
k>=1, paired21 and even22 are node functions. Odd22 XOR next-even22
is ALSO a node function K; the two reset/continue edges agree in K.
REFUTED-BY: any node ambiguity in that XOR or in paired21.
P2 BEFORE execution:16 past even22 samples recover the current state.
The present odd22 then predicts next even22 and reconstructs the
paired23 samples without any additional future sample. This is one
causal spatial interface, NOT an invariant under further depths.
REFUTED-BY: a failed state decoder or paired23 literal-truth control.
Counterfactual: present even22 and decoded age alone predict next even.
Must fail at tail15: its reset and continuation have next-even0/1.
Independent controls: original h spelling versus the finite age graph;
literal Rule30 truth-table triangles versus XOR/OR spatial formulas.
Unexpected checks: arbitrarily long S trains and all three pure-S phases
need the no-recent-marker fallback; k=0 has two00 markers in the16-sample
window, so this particular state-decoder guard MUST NOT be widened just
because GC1117's shorter q decoder passes its outside-premise control.
P1/P2 OUTCOME: HELD on56 complete local paths and423 independent
physical samples,198 beyond the recent-marker range;54 pure-S samples
pass. k=0 rejects the16-sample UNIQUE-marker state decoder as predicted.
NEW EVIDENCE before further controls: the (paired21,K) profiles at
ages12,13,14 equal tail15,16,17 exactly. Quotient those three pairs.
P3 BEFORE execution: the resulting15-state/16-edge graph works for ALL
k>=0, with13-past-even state recovery. Reset and continuation are
distinguished by present odd22; no future queue is added.
P4 BEFORE the identified unexpected closure check: at source age11,
paired23 is01 for both choices made at age12, but paired24 is01 after
reset and00 after continuation. Thus the no-new-lookahead property is
specific to22->23 and FAILS at23->24. This closes that causal-kernel
candidate; do not start a depth sweep or extend its future queues.
P3/P4 OUTCOME: HELD;53 complete quotient paths and318 k=0/long-S
samples pass. The age11 counter is in the EXTENDED k>=0 grammar.
Unexpected scope check BEFORE application: that reset has k=0 and is
outside the bare k>=1 grammar. P5 BEFORE its two-cone control: move
to first-L age14; next gap k=1 versus k=2 leaves paired22 and paired23
identical now, but paired24 reads10 versus11. Use h spellings for
(1,1,1) versus(1,2,1), at the SECOND first L, so all physical times
and the13-past decoder are interior. This closes the same causal
candidate on the unrestricted k>=1 macro guard as well.
P5 OUTCOME: HELD at physical52/53, for the k>=1 MACRO alphabet.
Second scope check: those unrestricted macro triples are not whole
GC1113 closed walks. P6 BEFORE publication: use two exact reviewed
generator words, EF_0 EF_0 versus EF_0 FE_0. They agree in q through
119, first differ at120; current first-L age14 has u=115. Paired22
and paired23 agree through physical217, whereas paired24 at216/217
reads10 versus11. This is the counter ON the bare branching model,
and no size of PAST memory of those two columns can distinguish it.
P6 OUTCOME: HELD on EF EF versus EF FE, at216/217; their complete
paired22/23 histories agree through217, paired24 is10/11. The new
future choice reappears; do not enlarge causal memory to repair it.
P7 BEFORE counter-aware check: retaining the EXACT18-state k>=1
guard, next-edge dependence occurs only at current states14 and17,
whose successor is tail15. Both outputs have even24=1, so this new
choice always resets the even-phase WHITE-run counter. In the15-state
quotient, state11->12 can instead reset with k=0 and even24=0. Thus
merging equal present profiles introduces an UNPAID branch and cannot
be used to retain this counter lemma. This is one named spatial
interface and one phase, not an all-depth or both-phase certificate.
OUTCOME P7: HELD. Exactly edges14->15 and17->15 acquire a new
next-edge dependence; both images are{10,11}, so even24 is BLACK.
The15-state quotient introduces the k=0 edge11->12 with even24 WHITE.
No all-depth preservation, both-phase bound or actual lift is claimed.
"""

from collections import defaultdict
import rule30_sl_age_spatial_interface as prior
import rule30_sl_pair_marker_code as code


PREFIX = tuple(map(int, code.BASE[:15]))


def successors(s):
    if s < 15:
        return (s+1,)
    if s == 15:
        return (0, 16)
    return (17,) if s == 16 else (15,)


def qbit(s):
    return int(s in (0, 5, 10, 13, 16))


def cbit(s):
    return PREFIX[s] if s < 15 else int(s != 15)


def paths(path, length=13):
    if len(path) == length:
        yield path
    else:
        for nxt in successors(path[-1]):
            yield from paths(path+(nxt,), length)


def literal(q):
    cols = prior.literal(q)
    a, b = cols[-1], cols[-2]
    out = []
    for t in range(len(a)-1):
        lefts = [x for x in (0, 1)
                 if (30 >> (4*x+2*a[t]+b[t])) & 1 == a[t+1]]
        assert len(lefts) == 1
        out.append(lefts[0])
    return cols+[out]


def decode_state(c, u):
    n = len(c)
    near = [j for j in range(15)
            if c[(u-j-1) % n] == c[(u-j) % n] == 0]
    assert len(near) <= 1
    if near:
        return near[0]
    return {(1, 0): 15, (0, 1): 16, (1, 1): 17}[
        c[(u-1) % n], c[u]]


def small_successors(s):
    if s < 12:
        return (s+1,)
    if s == 12:
        return (0, 13)
    return (14,) if s == 13 else (12,)


def small_q(s):
    return int(s in (0, 5, 10, 13))


def small_c(s):
    return PREFIX[s] if s < 12 else int(s != 12)


def small_paths(path, length=13):
    if len(path) == length:
        yield path
    else:
        for nxt in small_successors(path[-1]):
            yield from small_paths(path+(nxt,), length)


def small_decode(c, u):
    n = len(c)
    near = [j for j in range(12)
            if c[(u-j-1) % n] == c[(u-j) % n] == 0]
    assert len(near) <= 1
    if near:
        return near[0]
    return {(1, 0): 12, (0, 1): 13, (1, 1): 14}[
        c[(u-1) % n], c[u]]


def refined(table):
    assert all(table[s] == table[s+3] for s in (12, 13, 14))
    table = {s: table[s] for s in range(15)}
    edges, count = {}, 0
    for start in range(15):
        for p in small_paths((start,)):
            cols = literal(tuple(map(small_q, p)))
            s, nxt = p[7:9]
            a, b, k = table[s]
            c, o = cols[22][:2]
            assert tuple(cols[21][:2]) == (a, b)
            assert c == small_c(s)
            assert cols[22][2] == small_c(nxt)
            assert o ^ small_c(nxt) == k
            assert tuple(cols[23][:2]) == (o ^ (c | a), k ^ ((1-o) & b))
            label = (c, o)
            if (s, nxt) in edges:
                assert edges[s, nxt] == label
            edges[s, nxt] = label
            count += 1
    assert len(edges) == 16
    checks = 0
    for ks in ((0, 0, 0), (0, 1, 2), (0, 19, 0), (31, 0, 1)):
        q, firsts = code.source(ks)
        n = len(q)
        expected = [None]*n
        for r, k in zip(firsts, ks):
            for age in range(13+3*k):
                s = age if age < 12 else 12+(age-12) % 3
                expected[(r+age) % n] = s
        c = [small_c(s) for s in expected]
        assert c == code.forced(q)
        for u, s in enumerate(expected):
            assert small_decode(c, u) == s
            cols = literal(tuple(q[(u-7+i) % n] for i in range(13)))
            a, b, k = table[s]
            assert tuple(cols[21][:2]) == (a, b)
            assert cols[22][1] ^ k == c[(u+1) % n]
            checks += 1
    # Only the named two continuations are tested at24, NOT a sweep.
    witnesses = []
    for after in ((0, 1, 2, 3), (13, 14, 12, 13)):
        p = tuple(range(4, 13))+after
        q = tuple(map(small_q, p))
        cols = literal(q)
        a, b = cols[-1], cols[-2]
        left24 = [next(x for x in (0, 1)
                       if (30 >> (4*x+2*a[t]+b[t])) & 1 == a[t+1])
                  for t in range(len(a)-1)]
        assert tuple(cols[23][:2]) == (0, 1)
        witnesses.append((''.join(map(str, q)), tuple(left24[:2])))
    assert witnesses[0][1] == (0, 1) and witnesses[1][1] == (0, 0)
    # The histories are identical through current source age11;
    # the first q difference lies at u+5, outside paired23's cone.
    assert witnesses[0][0][:-1] == witnesses[1][0][:-1]
    print(dict(P3='HELD', P4='HELD causal closure REFUTED',
               states=15, edges=16, complete_local_paths=count,
               k0_and_long_controls=checks, state_history_even_samples=13,
               closure_counter=witnesses, all_depth_invariant=False))
    bare = []
    for ks in ((1, 1, 1), (1, 2, 1)):
        q, firsts = code.source(ks)
        assert firsts[1] == 19
        u = firsts[1]+14
        window = tuple(q[u-7:u+6])
        assert len(window) == 13 and 2*u-14 >= 24
        cols = literal(window)
        a, b = cols[-1], cols[-2]
        left24 = [next(x for x in (0, 1)
                       if (30 >> (4*x+2*a[t]+b[t])) & 1 == a[t+1])
                  for t in range(len(a)-1)]
        assert tuple(cols[22][:2]) == (1, 0)
        assert tuple(cols[23][:2]) == (1, 0)
        bare.append((''.join(map(str, window)), tuple(left24[:2]), q[:u+5]))
    assert bare[0][1] == (1, 0) and bare[1][1] == (1, 1)
    assert bare[0][2] == bare[1][2]
    print(dict(P5='HELD; k>=1 macro causal closure REFUTED',
               macro_guards=((1, 1, 1), (1, 2, 1)),
               physical_target_pair=(52, 53),
               paired22=10, paired23=10,
               macro_counter=[x[:2] for x in bare], all_depth_invariant=False))
    E, F = (1, 2, 2, 3), (3,)
    EF, FE = E+F, F+E
    exact = []
    for ks in (EF+EF, EF+FE):
        q, firsts = code.source(ks)
        assert 101 in firsts
        u = 115
        window = tuple(q[u-7:u+6])
        cols = literal(window)
        a, b = cols[-1], cols[-2]
        left24 = [next(x for x in (0, 1)
                       if (30 >> (4*x+2*a[t]+b[t])) & 1 == a[t+1])
                  for t in range(len(a)-1)]
        assert tuple(cols[22][:2]) == tuple(cols[23][:2]) == (1, 0)
        exact.append((q, tuple(left24[:2])))
    assert exact[0][0][:120] == exact[1][0][:120]
    assert exact[0][0][120] != exact[1][0][120]
    assert exact[0][1] == (1, 0) and exact[1][1] == (1, 1)
    # Independent literal full prefix confirms ALL observed past,
    # not just the state or a fixed-size decoder window.
    prefixes = [literal(tuple(q[:121])) for q, _ in exact]
    assert prefixes[0][22][:218] == prefixes[1][22][:218]
    assert prefixes[0][23][:218] == prefixes[1][23][:218]
    print(dict(P6='HELD; exact bare-walk causal closure REFUTED',
               generator_words=('EF EF', 'EF FE'), common_q_length=120,
               full_past_pair22_pair23_length=218,
               physical_target_pair=(216, 217), paired24=[x[1] for x in exact],
               membership_tested=False))


def main():
    rows, kvals, edges = defaultdict(set), defaultdict(set), {}
    count = 0
    for start in range(18):
        for p in paths((start,)):
            cols = literal(tuple(map(qbit, p)))
            s, nxt = p[7:9]
            a, b = cols[21][:2]
            c, o = cols[22][:2]
            assert c == cbit(s) and cols[22][2] == cbit(nxt)
            rows[s].add((a, b))
            kvals[s].add(o ^ cbit(nxt))
            value = (c, o)
            if (s, nxt) in edges:
                assert edges[s, nxt] == value
            edges[s, nxt] = value
            # Independent literal23 must agree with the no-lookahead map.
            k = o ^ cbit(nxt)
            predicted = (o ^ (c | a), k ^ ((1-o) & b))
            assert tuple(cols[23][:2]) == predicted
            count += 1
    assert set(rows) == set(kvals) == set(range(18))
    assert all(len(v) == 1 for v in rows.values())
    assert all(len(v) == 1 for v in kvals.values())
    assert len(edges) == 19
    table = {s: (*next(iter(rows[s])), next(iter(kvals[s])))
             for s in range(18)}
    assert cbit(0) == 0 and cbit(16) == 1
    assert edges[15, 0][1] != edges[15, 16][1]
    checks = fallback = 0
    for ks in ((1, 2, 3), (2, 2, 2), (3, 3, 3),
               (1, 19, 2), (31, 1, 1)):
        q, firsts = code.source(ks)
        n = len(q)
        expected = [None]*n
        for r, k in zip(firsts, ks):
            for age in range(13+3*k):
                state = age if age < 15 else 15+(age-15) % 3
                expected[(r+age) % n] = state
        c = [cbit(s) for s in expected]
        for u, s in enumerate(expected):
            assert decode_state(c, u) == s
            local = tuple(q[(u-7+i) % n] for i in range(13))
            cols = literal(local)
            a, b, k = table[s]
            o = cols[22][1]
            assert tuple(cols[21][:2]) == (a, b)
            assert cols[22][0] == c[u]
            assert o ^ k == c[(u+1) % n]
            predicted = (o ^ (c[u] | a), k ^ ((1-o) & b))
            assert tuple(cols[23][:2]) == predicted
            checks += 1
            fallback += s >= 15
    pure = 0
    for phase in range(3):
        q = tuple(int((u+phase) % 3 == 0) for u in range(18))
        c = code.forced(q)
        for u in range(len(q)):
            s = decode_state(c, u)
            assert s in (15, 16, 17)
            cols = literal(tuple(q[(u-7+i) % len(q)] for i in range(13)))
            a, b, k = table[s]
            assert tuple(cols[21][:2]) == (a, b)
            assert cols[22][1] ^ k == c[(u+1) % len(q)]
            pure += 1
    q0, _ = code.source((0, 0, 0))
    c0 = code.forced(q0)
    try:
        decode_state(c0, 3)
    except AssertionError:
        pass
    else:
        raise AssertionError('outside-premise double-marker guard did not fail')
    print(dict(P1='HELD', P2='HELD', states=18, edges=19,
               local_paths=count, physical_controls=checks,
               no_recent_marker_controls=fallback, pure_phase_controls=pure,
               state_history_even_samples=16,
               future_even_from_present_odd=True,
               even_only_prediction='REFUTED', k0_guard='fails as predicted',
               all_depth_invariant=False))
    refined(table)
    def image23(s, nxt):
        a, b, k = table[s]
        c = cbit(s)
        o = k ^ cbit(nxt)
        return (o ^ (c | a), k ^ ((1-o) & b)), (c, o)
    images24 = {}
    for s in range(18):
        for nxt in successors(s):
            (e, o), (c, right_o) = image23(s, nxt)
            values = set()
            for after in successors(nxt):
                (next_e, _), _ = image23(nxt, after)
                left_e, left_o = o ^ (e | c), next_e ^ (o | right_o)
                assert (30 >> (4*left_e+2*e+c)) & 1 == o
                assert (30 >> (4*left_o+2*o+right_o)) & 1 == next_e
                values.add((left_e, left_o))
            images24[s, nxt] = values
    ambiguous = {edge: values for edge, values in images24.items()
                 if len(values) > 1}
    assert set(ambiguous) == {(14, 15), (17, 15)}
    assert all(values == {(1, 0), (1, 1)} for values in ambiguous.values())
    assert all(len(values) == 1 for values in images24.values()
               if any(e == 0 for e, _ in values))
    print(dict(P7='HELD; new future branch pays an even-phase black reset',
               ambiguous_edges=sorted(ambiguous),
               unpaid_quotient_branch='state11 -> tail12, k=0',
               both_phase_certificate=False, all_depth_certificate=False))


if __name__ == '__main__':
    main()
