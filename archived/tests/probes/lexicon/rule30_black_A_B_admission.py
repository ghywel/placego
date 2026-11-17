"""GC1098: black-A past supplies the sparse guard at its first B.

Missing inference: blackA-S-D101-H-B must satisfy B00 implies12white.
Record searched:101.*B|B.*101 withwhite12|site.12|sparse|admission
->88hits28files; black.eleventh|GC1097 withguard|B ->22hits10files.
GC1086/87/1075 read; J ancestry cannot be assumed for a fresh101.
P1: badB0011001 has few H7parents outside010110. HELD:13.
P2: genericH101 has no badB parent. REFUTED:112 high packets;
their first10 cells have three possibilities in HIGH_PREFIXES.
P3 initially appeared to exclude these prefixes already from low100100.
INVALID: hand-copied D shields01111/1100 were wrong. Independent scalar
check gives11111/0000. Corrected transport retains108 low parents;
the false low-only exclusion is withdrawn, not a theorem.
P3b: corrected D then black-A S shields exclude badB. HELD:240 S5
parents, none with S4prefix10001. Uses black-A past, not low alone.
P4: H101 returns a white sixth marker. HELD via H8=11,H9=00.
Unexpected selected Jsource was predicted to give blackB13; FAILED,
also for four immediate exterior variants. Prior generic pair guard
failure remains; this block asserts only sparse B12, never whiteB13.
P5 relax only final A13 filter: FAILED (earlier consequences retained).
P5b weaken all S shields consistently: still FAILED under retainedlow
premise, already at S4. No necessity of A13black is claimed.
P6 actual36-cell B00 cylinder retains12cells at32. HELD:17 cells.
Counterfactual: a fresh high101 always has guardedB. BAD_HIGH refutes
it for every exterior; its needed D-low-S past is excluded.
Independent controls: every inverse edge forward checked; scalar
fresh-right low shields; literal/packed badHigh and actual histories.
Conclusion: conditional first-B admission, not admission after arbitrary
white-marker SS blocks, and not an all-depth record bound.
Second read CL275: CONFIRMED, now PROVED. Its stronger full-strip D-H
exclusion needs neither black-A nor low ancestry; GC1100 replicates
the five-D counts164,460,456,96,0. The original short-past proof above
remains valid, but that past is not necessary for the guard.
"""
from itertools import product
from rule30_black_A_ancestry_guard import inverse
from rule30_core_short_bridge import bits, update, propagate, S, D
from rule30_sl_no_refork import run

H = bits('0101101010')
HIGH_SHIELDS = ('1101', '1001', '0111', '1100', '001', '111', '100')
HIGH_PREFIXES = {bits(s) for s in ('1101101101', '1101101110', '1101110000')}
LOW_SHIELDS = ('100100', '11111', '0000', '000', '10', '0')
BAD_HIGH = bits('11100110110110100000000')
ACTUAL = bits('111011111111000011001000000000000000')


def main():
    parents = {bits('0011001')}
    for t in range(9, 6, -1):
        parents = {x for y in parents for x in inverse(y, H[t])}
    parents = {x for x in parents if x[:2] == bits('01')}
    assert len(parents) == 13
    high_counts = []
    for t in range(6, -1, -1):
        parents = {x for y in parents for x in inverse(y, H[t])
                   if x[:len(HIGH_SHIELDS[t])] == bits(HIGH_SHIELDS[t])}
        high_counts.append(len(parents))
    assert high_counts == [7, 23, 60, 13, 35, 28, 112]
    assert {x[:10] for x in parents} == HIGH_PREFIXES
    for x in parents:
        assert propagate(x, H)[10] == bits('0011001')
    # Verify these prefixes before using them; the original copied
    # phase values were wrong and their empty-set verdict is withdrawn.
    shield_controls = 0
    for t, (old, new) in enumerate(zip(LOW_SHIELDS, LOW_SHIELDS[1:])):
        for far in (0, 1):
            assert update((D[t],)+bits(old)+(far,))[:len(new)] == bits(new)
            shield_controls += 1
    parents = set(HIGH_PREFIXES)
    low_counts = []
    for t in range(9, -1, -1):
        parents = {x for y in parents for x in inverse(y, D[t])}
        if t < len(LOW_SHIELDS):
            parents = {x for x in parents
                       if x[:len(LOW_SHIELDS[t])] == bits(LOW_SHIELDS[t])}
        low_counts.append(len(parents))
    assert low_counts == [12, 20, 29, 14, 24, 25, 23, 64, 228, 108]
    for x in parents:
        assert propagate(x, D)[10] in HIGH_PREFIXES
    # Only two closing S ticks are needed; weaker first-five S4
    # prefix suffices. Black-A's established S4prefix is100010.
    parents = {x for y in parents for x in inverse(y, S[5])
               if x[:5] == bits('11011')}
    assert len(parents) == 240
    parents = {x for y in parents for x in inverse(y, S[4])
               if x[:5] == bits('10001')}
    assert not parents
    # The newly useful white-marker consequence of H8prefix11.
    for a, b in product((0, 1), repeat=2):
        assert update((H[8],)+bits('11')+(a, b))[:2] == bits('00')
        assert update((H[9],)+bits('00')+(a, b))[:1] == bits('0')
    rows = [ACTUAL]
    implications = 0
    for t in range(38):
        old = rows[-1]
        new = update((t % 2,)+old)
        if old[-1]:
            new += (old[-2] ^ 1,)
        for far in (0, 1):
            assert update((t % 2,)+old+(far,))[:len(new)] == new
            implications += 1
        rows.append(new)
    assert rows[6][:13] == bits('1110100011111')
    assert rows[12][:11] == bits('11100100100')
    assert rows[22][:9] == bits('111001101')
    assert rows[32][:12] == bits('111010011000')
    assert rows[38][6:9] == bits('100')
    assert tuple(r[4] for r in rows[:38]) == bits('111010')+S+D+H+S
    actual = bad = 0
    for tail in product((0, 1), repeat=5):
        for far in (0, 1):
            complete = run(ACTUAL+tail+(far,)*32, 38)
            for t, p in enumerate(rows):
                assert complete[t][:len(p)] == p
            actual += 1
            fresh = run(BAD_HIGH+tail+(far,)*16, 10)
            assert fresh[10][:12] == bits('111010011001')
            bad += 1
    unexpected = bits('111001101100000100000')
    for tail in product((0, 1), repeat=2):
        assert run(unexpected+tail+(0,)*20, 10)[10][11:13] == (0, 0)
    print(dict(H_parents=112, low_parents=108, S5_parents=240,
               S4_parents=0, low_shield_controls=shield_controls,
               causal_implications=implications, actual_histories=actual,
               fresh_bad_B_histories=bad, literal_packed='PASS',
               incorrect_D_shields='INVALID verdict retained and corrected',
               first_B_admission='ALL-TAIL SPARSE GUARD',
               H101_marker='WHITE', later_SS_block='OPEN',
               all_depth_bound='OPEN'))


if __name__ == '__main__':
    main()
