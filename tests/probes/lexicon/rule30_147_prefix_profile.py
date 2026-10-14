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

C4 REVIEW PREDICTION (2026-10-14 01:38 BST, before the fixed-row check):
 the actual X2 left row from its committed 329-bit witness reaches the same entire clamped left row at time11
 as EACH of FIRST and SECOND (two distinct fixture pairs). This would connect the old rejected preludes to
 a genuinely realized record's future state. Counterfactual: matching a long visible suffix alone is enough;
 no general common-continuation or arbitrary-tail statement is claimed. Independent literal/packed updates
 check all cells through width160, beyond the support bound157 at time11. Unexpected controls: FIRST versus
 X2 differs at depth1,time4, and SECOND versus X2 at depth1,time10, preventing premature merger claims.
 Record searched: X2 with merge, real with prelude -> no indexed hit; GC1210, GC1215 and L704 read.
 No membership call, solver, depth sweep or earliest-merger search. The known Y1 membership is adopted.
 C4 OUTCOME: both entire rows equal the real X2 left row at time11 in literal and packed evolution.
 FIRST differs from X2 initially at27 sites, depths5..45; SECOND at26 sites, depths3..57.
 The depth1 countercontrols at times4 and10 pass. These are fixed finite origins, with no arbitrary-tail claim.
"""
import hashlib
from pathlib import Path
import re
import sys
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


def real_review():
    src = Path(__file__).with_name('rule30_exact_cone_cert.py').read_text()
    block = src.split('The witness row, cells -164 .. 164')[1].split('With K14')[0]
    bits = ''.join(re.findall(r'^     ([01]+)$', block, re.M))
    assert len(bits) == 329
    assert hashlib.sha256(bits.encode()).hexdigest() == 'bd2e7ab1aa9cb7628d9348cb7f046fad4acbddf8d15b7d30c51d387b00d07517'
    actual = {j: int(bits[164-j]) for j in range(1, 147)}
    assert actual[146] == 1 and not any(int(bits[164-j]) for j in range(147, 165))
    actual_rows = packed(actual, 0, 11, 160)
    assert actual_rows == literal(actual, 0, 11, 160)
    for name, q, check_time in (('FIRST', FIRST, 4), ('SECOND', SECOND, 10)):
        c = columns(q)
        seed = {j: c[j][0] for j in range(1, 147)}
        rows = packed(seed, 0, 11, 160)
        assert rows == literal(seed, 0, 11, 160)
        assert rows[check_time][1] != actual_rows[check_time][1]
        assert rows[11] == actual_rows[11]
        diff = [j for j in actual if actual[j] != seed[j]]
        print(name, 'and real X2: whole left rows equal at11; earlier depth1 difference at', check_time,
              '| initial differences', len(diff), 'depth range', (min(diff), max(diff)))
    print('C4 PASS: two fixture pairs, independent forward engines and bounded full support')


if __name__ == '__main__':
    if sys.argv[1:] == ['real']:
        real_review()
    else:
        main()
