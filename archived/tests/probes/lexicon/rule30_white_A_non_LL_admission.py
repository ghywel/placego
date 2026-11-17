"""GC1141: white-A origins outside the high-LL selector.
Missing inference: GC1139/40 discharge only the28 A25 high-LL
cylinders; non-LL high111 or unguarded101 may still replenish SS/A.
Record searched: white.A|white.eleventh AND non.high|outside|admission|001001
->67 hits25files. GC1090,1104,1136..1140 read. The low01
shield closes white13; delayed-SS ancestry is not assumed here.
P1 BEFORE run: every source25 beginning white-A13 with u=1
outside the28 selector cylinders gives C at16. Complete source25
cones fix all9 endpoint cells, so this is a finite causal proof if
true. If false retain the first actual exceptional source and its
H26 classification, instead of treating non-LL as absorption.
Counterfactual: a high111 whose H ends S survives this restriction,
and may replenish SS. Controls: literal/packed on complete cones;
white13 GC1090 branch as independent positive control; four actual
far-exterior patterns on the counter. Unexpected: non-LL need not
mean non-high; keep both H-low and H-short explicitly separate.
No solver, CUT, membership, record or graph computation.
"""
from collections import Counter
from itertools import product
from rule30_sl_no_refork import bits,run
from rule30_white_A_high_LL_guard import selector,primes
from rule30_low_core_closure import CORE
from rule30_001000_mixed_admission import certificate
from rule30_positive_A_mixed_exit import guarded_B,mixed_long
from rule30_core_short_bridge import propagate
from rule30_001_high_return_gate import H


def main():
    counts=Counter();exception=None;white13=Counter();high_sources=set()
    for far in product((0,1),repeat=12):
        src=bits('1110100011011')+far
        if run(src,16)[16][6:9]==bits('111'):
            high_sources.add(sum(b<<j for j,b in enumerate(far)))
        if not selector(far):
            end=run(src,16)[16];counts[end[6:9]]+=1
            if end[6:9] not in CORE and exception is None:exception=src
        q=run(bits('1110100011010')+far,16)[16]
        assert q[6:9] in CORE;white13[q[6:9]]+=1
    print('P1_nonLL_core16',exception is None,'complete25_counts',dict(counts),
          'white13_positive4096',dict(white13),flush=True)
    if exception is None:return
    r=run(exception+(0,)*55,52)
    print('first_actual_nonLL_source25',''.join(map(str,exception)),
          'L16',''.join(map(str,r[16][:20])),
          'H26',''.join(map(str,r[26][:20])),
          'tick32',''.join(map(str,r[32][:20])),flush=True)
    for pattern in ((0,),(1,),(0,1),(1,0)):
        far=tuple(pattern[j%len(pattern)] for j in range(80-len(exception)))
        full=run(exception+far,52)
        assert full[16][:9]==r[16][:9]
        print('counter_exterior_pattern',pattern,'guardedB26',guarded_B(full[26]),
              'mixed32',mixed_long(full[32]),
              'H26_prefix13',''.join(map(str,full[26][:13])),flush=True)
    # P2 BEFORE an actual reset check: this first non-LL source,
    # with55 displayed white cells, replenishes black-eleventh A
    # by44 through at most three SS after H26. If false retain
    # that exact failure; do not scan ages or add more SS counts.
    # This tests a fixed declared witness, not all tails of source25.
    black_A=None
    for t in (26,32,38,44):
        if r[t][:12]==bits('111010001110'):
            black_A=t;break
    print('P2_actual_black_A_by44',black_A,
          'SS_endpoints',[(t,''.join(map(str,r[t][:14]))) for t in (26,32,38,44)],flush=True)
    if black_A is not None:
        src=exception+(0,)*55
        cert=certificate(src,black_A)
        assert cert[-1][:12]==bits('111010001110')
        print('black_A_all_tail_source80_certificate_PASS','tick',black_A,flush=True)
    # P3 BEFORE guard extraction: the D111 decision ignores A24/25
    # and has at most12 prime cubes. This concerns the first D
    # return, not the already-reviewed high-LL selector. Check the
    # full704 set independently against the cubes and their free bits.
    ps=primes(high_sources,12)
    support=[j+14 for j in range(12) if any(
        (x in high_sources)!=((x^(1<<j)) in high_sources) for x in range(4096))]
    for x in range(4096):assert (x in high_sources)==any((x&m)==v for v,m in ps)
    print('P3_D111_selector','count',len(high_sources),'support',support,
          'cubes',len(ps),'prediction',all(j<=23 for j in support) and len(ps)<=12,flush=True)
    for v,m in ps:
        print('D111_cube',''.join(str((v>>j)&1) if (m>>j)&1 else '-' for j in range(12)),flush=True)
    # P4 BEFORE finite-witness compression: this same displayed
    # source admits guarded B44 using at most45 original cells.
    # Retain a fresh-bit induction, not four sample exteriors.
    witness=exception+(0,)*55
    lengths=[n for n in range(25,81) if guarded_B(certificate(witness[:n],44)[44])]
    assert lengths
    n=min(lengths);src=witness[:n];cert=certificate(src,44)
    assert guarded_B(cert[44])
    for pattern in ((0,),(1,),(0,1),(1,0)):
        far=tuple(pattern[j%len(pattern)] for j in range(100-len(src)))
        full=run(src+far,50)
        assert guarded_B(full[44]) and mixed_long(full[50])
        assert all(full[t][:len(y)]==y for t,y in enumerate(cert))
    print('P4_all_tail_guarded_B44_source',''.join(map(str,src)),'length',n,
          'prediction',n<=45,'B44',''.join(map(str,cert[44])),
          'independent_source100_controls4_PASS',flush=True)
    # P5 BEFORE the local structural check: every111 high has
    # returned site6=1, on H-short as well as H-low, using only
    # GC1076's reviewed time5 sites6,7=10. This explains the676
    # black-marker SS entrances without assuming the black-A past
    # of GC1105's narrower computed set. Record searched:111|high
    # AND black.marker|black.sixth|site6.*1|sixth.*black ->39 hits14files;
    # GC1076,1089,1105 read; the generic time5 implication is new.
    for a,b,c,d in product((0,1),repeat=4):
        mid=bits('10')+(a,b,c,d)
        rows=propagate(mid,H[5:])
        assert rows[2][:2]==(0,0)  # time7 sites6,7.
        assert rows[3][1]==(a or not(b or c)) # time8 site7.
        assert rows[4][0]==1-rows[3][1] # time9 site6.
        assert rows[5][0]==1 # time10 site6.
    negative=run(bits('111001101100')+(0,)*16,10)[10]
    assert negative[:9]==bits('111010011') and negative[5]==0
    words=sorted({''.join(str((x>>j)&1) for j in range(6)) for x in high_sources})
    assert len(words)==11
    print('D111_source19_suffixes',words,
          'generic_high111_black6_local16_PASS',
          'unexpected_high101_white6_PASS',flush=True)


if __name__=='__main__':main()

# OUTCOME: P1 REFUTED:4068 non-LL A25 cylinders partition into
# 3392 immediate C (2624 C010,768 C100) and676 high111, with no
# unguarded101 outcome. White13 control4096 all C010. P2 fixed
# counter's black-A-by44 prediction REFUTED; it reaches guarded
# B44 instead. P3 HELD, strengthened: D111 depends only on A14..19,
# five prime cubes/eleven full source19 suffixes. P4 HELD: the
# source39 prefix proves B44 for every tail, then C/J50; four
# independent100-cell trajectories agree. P5 HELD by the local
# complementary pair at time9: every111 H return has black6, so
# the676 non-LL cases enter black-marker SS at26. The fresh101
# negative control retains white6. The remaining676 admission is
# OPEN; this one39-cell cylinder is not a universal deadline.
