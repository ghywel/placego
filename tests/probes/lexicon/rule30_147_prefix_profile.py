#!/usr/bin/env python3
"""One fixed origin-profile comparison for the two committed147 codes.

RUN-ON: cpu, Python standard library. No solver or membership replay.
COMMAND: python3 tests/probes/lexicon/rule30_147_prefix_profile.py

Record searched: early.prefix|prefix.edit|common.continuation|spatial.tail
with merge|pair.image|finite.edit|tail.equival ->GC994 only. First-bit
merger search located GC1057's local merger, so it is not re-proved.
GC1159's first-visible-bit quotient, GC1005/06 and GC1208 read.

PREDICTIONS before execution (2026-10-13):
 C1 blind(.5): the two82-bit codes committed in rule30_cadical_lift.py
     have identical physical P0 words at d147,p0,e0,k147. Both have
     inner black146 and zeros147..164, by their checked relaxed models.
 C2 blind(.5): early times0..11 in both forced columns16 and17 agree.
     If so, since the right codes agree from white12 onward, these two
     entire columns agree for every common continuation after white28;
     inverse induction gives all farther columns identical. This is a
     finite certificate of a specific all-tail merger, not a cutoff fit.
     If C2 fails, no deeper merger search or extra code follows.
 Independent: inverse literal Wolfram-table solve versus GC971's XOR/OR
     image at every used depth. C1 compares all147 path letters.
 Unexpected: unused terminal right164 and arbitrary black-time raw
     right bits leave the profile unchanged; flipping visible146
     necessarily changes its penultimate first coordinate.
 Counterfactual: a shared visible tail alone determines P0 or guarantees
     early real admission. Both codes are certified non-real; left-side
     origin reconstruction is not a real record or membership claim.

FIRST OUTCOME: C1 HELD (all147 profile letters equal); C2 REFUTED
at both fixed columns, with a difference at depth16,time0. Both
reconstructed rows have black146 and whites147..164. All controls pass.
No deeper merger search or additional code was run.

C3 ADDENDUM before execution: for these two FIXED finite rows, set all
depths beyond146 to0 and compare their whole clamped left rows at
time11. Predict equality there; time10 depth1 must still differ, since
the final code edit is at white10. Thus11 is the earliest merger if
the check passes. This is justified by C1 and the proved exact word
update: future adjacent traces from146 agree; the stored codes give
agreement from11 to145. Inverse induction then forces the entire row
at11 to agree. Independent direct forward literal/packed controls
will check the new carrying inference, with full support width160.
This does not assert universal merger for arbitrary q continuations
or left tails; the stronger C2 failed.

C3 OUTCOME: the entire rows merge at11 (support bound157,width160);
time10 depth1 differs. Initial rows differ at33 sites, depths3..57.
Literal/packed forward controls pass. This fixed-row equality extends
by determinism, without converting failed C2 into an all-tail theorem.
"""
from rule30_rrl_transducer import literal_image
from rule30_zero_triangle_guard_transport import packed, literal

FIRST = '0000100001010101000100001001001000010000100100100001000010000100001001000010010000'
SECOND = '0100010001010101000100001001001000010000100100100001000010000100001001000010010000'


def root(q, terminal=0, odd=0):
    return tuple(2*(t % 2)+(int(q[t//2]) if t % 2 == 0 and t < 164
                           else (terminal if t == 164 else odd)) for t in range(165))


def table_image(word):
    out = []
    for prev, nxt in zip(word, word[1:]):
        c, r = divmod(prev, 2)
        y = nxt//2
        left = next(l for l in (0, 1) if ((30 >> (4*l+2*c+r)) & 1) == y)
        out.append(2*left+c)
    return tuple(out)


def columns(q, terminal=0, odd=0):
    words = [root(q, terminal, odd)]
    for _ in range(164):
        new = literal_image(words[-1])
        assert new == table_image(words[-1])
        words.append(new)
    return [tuple(x//2 for x in w) for w in words]


def profile(cols):
    # c1,n146,k147, with actual black wall included at the last letter.
    return [(cols[146-u][1+u], cols[147-u][1+u]) for u in range(147)]


def main():
    assert len(FIRST) == len(SECOND) == 82
    assert [i for i, (a, b) in enumerate(zip(FIRST, SECOND)) if a != b] == [1, 4, 5]
    c0, c1 = columns(FIRST), columns(SECOND)
    w0, w1 = profile(c0), profile(c1)
    for c in (c0, c1):
        assert c[146][0] == 1 and all(c[j][0] == 0 for j in range(147, 165))
    assert w0[0] == w1[0] == (1, 1)
    assert w0[-1] == w1[-1] == (1, 1)
    early = [c0[j][:12] == c1[j][:12] for j in (16, 17)]
    print('C1 P0 equality', w0 == w1, 'differing letters',
          sum(a != b for a, b in zip(w0, w1)))
    print('C2 fixed columns16/17, times0..11', early)
    print('C2 first fixed-window difference',
          next(((j,t) for j in (16,17) for t in range(12) if c0[j][t] != c1[j][t]), None))
    seeds = [{j: c[j][0] for j in range(1,147)} for c in (c0,c1)]
    forward = [packed(s,0,11,160) for s in seeds]
    assert all(rows == literal(s,0,11,160) for rows,s in zip(forward,seeds))
    assert forward[0][10][1] ^ forward[1][10][1] == 1
    assert forward[0][11] == forward[1][11]
    differences = [j for j in range(1,147) if seeds[0][j] != seeds[1][j]]
    print('C3 whole left rows merge at11; at10 depth1 differs; initial differences',
          len(differences), 'range', (min(differences),max(differences)))
    for q in (FIRST, SECOND):
        assert profile(columns(q, terminal=1, odd=1)) == profile(columns(q))
        changed = q[:73]+str(1-int(q[73]))+q[74:]
        assert profile(columns(changed))[-2][0] ^ profile(columns(q))[-2][0] == 1
    print('PASS: inverse-table controls, both retained bands, mask/terminal and visible146 controls')


if __name__ == '__main__':
    main()
