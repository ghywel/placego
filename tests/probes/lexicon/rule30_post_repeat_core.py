"""GC1082: repeated high LL forces a sparse guard and core entrance.
Missing inference: can GC1081's post-repeat high renew high LL again?
Record searched: canonical1110011111000 with repeat/renew/inheritance
->17 hits in7 files; canonical prefix,001000 orat-most-two with
core/high/renew/guard/transport ->4 hits in2 files; no core theorem.
P1 BEFORE controls: inherited low B has sites18,19=01. Its high
successor starts1110011111000 and has site15=1, by a two-tick OR
shield. This sparse bit is lost by the contiguous13-bit prefix.
P2: canonical high with site14=0 selects X at its following001;
with site14=1 it returns001000, whose D enters C or101. C is
reviewed closed;101 escapes H-to-S. Thus a continuing mature
ordinary-long run has at most two high LL units, at every length.
P3: ordinary001000 has time5 pair x,y=(NOT C,1), so the reviewed
mid01 guarded map returns C or101, never111.
Counterfactual: the inherited post-repeat high can renew high LL
again through D. The X branch exits the mature S/L0 scope.
Unexpected BEFORE controls: canonical source1110011111000000001000001
with sites14,15=00 really has H-D-H with both high returns L0.
Its finite shield agrees with GC1081 from time3 onward. Dropping
the inherited sparse guard therefore makes the exclusion false.
Controls:16 B-prefix implications,4 local OR bands,32 B histories,96 canonical histories,
128 ordinary001000 histories,40 unexpected one-step shields and32 actual
unexpected histories. Literal against packed; no solver, language
membership or relaxed-record computation. Outcomes in GC1082.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_001_high_return_gate import band
from rule30_inherited_high_repeat import H, D, PREFIXES, update

C = {bits('010'), bits('011'), bits('100')}
CORE_OR_ESCAPE = C | {bits('101')}
X = bits('0101100101')
UNEXPECTED = '1110011111000000001000001'
UPREFIXES = ('11111000000001000001', '10000100000011100011',
             '01001110000110010110') + PREFIXES[3:]
BPREFIXES = ('10010011000001',) + PREFIXES[11:19]


def main():
    local = origins_B = canonical = core = shields = unexpected = b_shields = 0
    for t, (old, new) in enumerate(zip(BPREFIXES, BPREFIXES[1:])):
        for fresh in (0, 1):
            out = update((D[t],) + bits(old) + (fresh,))
            assert out[:len(new)] == bits(new)
            b_shields += 1
    for z, w in product((0, 1), repeat=2):
        rows = band(bits('1101111110') + (z, w) + (0,)*8, 8, 10, D)
        assert rows[10][8:10] == (1-z, 1)
        local += 1
    for tail in product((0, 1), repeat=4):
        for far in (0, 1):
            rows = run(bits('1110010010011000001') + tail + (far,)*35, 30)
            assert tuple(r[4] for r in rows[:10]) == D
            assert rows[8][13:15] == (1, 0)
            assert rows[10][:13] == bits('1110011111000')
            assert rows[10][14] == 1
            origins_B += 1
    for e, f in ((0, 1), (1, 0), (1, 1)):
        for tail in product((0, 1), repeat=4):
            for far in (0, 1):
                rows = run(bits('1110011111000') + (e, f) + tail
                           + (far,)*35, 30)
                assert tuple(r[4] for r in rows[:10]) == H
                assert rows[10][:9] == bits('111001001')
                if e:
                    assert rows[10][:12] == bits('111001001000')
                    assert tuple(r[4] for r in rows[10:20]) == D
                    assert rows[20][6:9] in CORE_OR_ESCAPE
                    assert rows[20][:6] == bits('111001')
                else:
                    assert rows[10][9:11] == (1, 1)
                    assert tuple(r[4] for r in rows[10:20]) == X
                canonical += 1
    for tail in product((0, 1), repeat=6):
        for far in (0, 1):
            rows = run(bits('111001001000') + tail + (far,)*25, 10)
            assert tuple(r[4] for r in rows[:10]) == D
            assert rows[5][8] == 1
            assert rows[10][6:9] in CORE_OR_ESCAPE
            assert rows[10][:6] == bits('111001')
            core += 1
    for t, (old, new) in enumerate(zip(UPREFIXES, UPREFIXES[1:])):
        for fresh in (0, 1):
            out = update(((H+D)[t],) + bits(old) + (fresh,))
            assert out[:len(new)] == bits(new)
            shields += 1
    for tail in product((0, 1), repeat=4):
        for far in (0, 1):
            rows = run(bits(UNEXPECTED) + tail + (far,)*35, 30)
            assert rows[0][13:15] == (0, 0)
            assert tuple(r[4] for r in rows[:30]) == H+D+H
            for t in (10, 20, 30):
                assert rows[t][:6] == bits('111001')
            for t, prefix in enumerate(UPREFIXES):
                assert rows[t][5:5+len(prefix)] == bits(prefix)
            unexpected += 1
    assert (local, origins_B, canonical, core, shields, unexpected) == (
        4, 32, 96, 128, 40, 32)
    assert b_shields == 16
    print({'local_OR_guards': local, 'actual_B': origins_B,
           'canonical_high': canonical, '001000_core': core,
           'B_prefix_shields': b_shields,
           'unexpected_shields': shields, 'unexpected_actual': unexpected,
           'sparse_guard_needed': 'PASS', 'literal_packed': 'PASS'})


if __name__ == '__main__':
    main()
