"""GC1099: one white SS after D-H cannot produce unguarded B.

Missing inference: admit the first SL after arbitrarily many white SS.
Concrete result: a seven-cell necessary high packet has no four-white
past; hence D-H-SS-B00 forces B12white, independently of black-A origin.
Record searched: white.SS|white.marker with admission|A11|eleventh
->5hits4files; GC1056/1087/1089/1090/1098 sources read. Further
100100|00100 with SS|short.block ->310hits116files (broad); narrowed
100100 with SS ->148hits66files; relevant named ancestry sources read.
Predictions were registered before each adaptive transport:
P1/P2 white SS cannot prepare black-A00011111 or bad B0011001.
REFUTED:182 and195 realized white SS parents respectively.
Initial full replay assertion FAILED: prescribing the fifth wall does
not guarantee its realization. Added the explicit realized-SS filter;
212 relaxed A parents reduce to182, all195 B parents remain.
P3 high101 H past excludes both after one SS. REFUTED:19120 A and
22724 B parents; selected full-source counters below retain the failure.
P4 first-ten-cell projection followed by low D and black-A S past is
empty. REFUTED for A:11200 parents, six distinct first13 prefixes;
HELD for B: D inverse counts32,24,24,0, before any low restriction.
P5 those projected A parents all have the forbidden five-white suffix.
REFUTED: six prefixes, not only0001111100000. Do not infer restart.
P6 low100100-D101-H cannot enter SS. INCONCLUSIVE under ten-cell
projection (1472 parents); full entrance calculation retains17376.
P7 at least one full SS entrance has actual black-SS past. UNKNOWN:
full D counts992,1176,2144,1888,3008,3648,2976,4576,16000,17376;
S counts51840,43072,109824,161184,150528,220160; preceding SS first
inverse reached606208, above preregistered500000 cap. STOP that tree;
no actual-black-SS counter or absence claimed.
P8 bad-B high parents' first10 are1101001 plus every three-bit word;
this seven-cell prefix has no four-step white-fifth past. HELD.
P9 least full low entrance realizes D-H-SS. HELD by NONVACUOUS.
P10 BEFORE causal controls: NONVACUOUS alone forces two white SS,
by retaining first9 at time26, not merely by its padded zero-tail run.
Counterfactual: white marker alone or fresh H101 supplies admission.
Four fixed all-tail counter-cylinders below refute those shortcuts.
Unexpected check: known111010000 white SS remains a positive; the
selected D-H entrance may continue SS rather than instantly admit.
Independent controls: every inverse edge forwardchecked; every high
packet's joint seven-bit prefix; fresh-right causal implications and
literal/packed arbitrary-exterior replays. No solver, CUT, record run,
longer-word census or extrapolation to arbitrary SS block length.
OUTCOME: P8/P9/P10 HELD;140 causal implications and320 independent
histories PASS. One-SS B guard is a proof sketch pending second read.
Arbitrary white-SS admission and the all-depth bound remain OPEN.
"""
from itertools import product
from rule30_black_A_ancestry_guard import inverse
from rule30_core_short_bridge import bits, update, propagate, D
from rule30_sl_no_refork import run
from rule30_black_A_B_admission import HIGH_SHIELDS, LOW_SHIELDS

SS=bits('111010')
H=bits('0101101010')
COUNTERS=(
    ('11101'+'00001101101000',6,'1110100011111'),
    ('11101'+'0000000000010',6,'111010011001'),
    ('11100'+'110100111010001000000000',16,'1110100011111'),
    ('11100'+'11010010000000100000000',16,'111010011001'),
)
NONVACUOUS=bits('11100100100010000110100000000')


def lift(parents,track,shields=()):
    counts=[]
    for t in range(len(track)-1,-1,-1):
        parents={x for y in parents for x in inverse(y,track[t])
                 if t>=len(shields) or x[:len(shields[t])]==bits(shields[t])}
        counts.append(len(parents))
    return parents,counts


def white_ss_parents(target):
    parents,counts=lift({bits(target)},SS)
    parents={x for x in parents if x[0]==0}
    counts[-1]=len(parents)
    realized=set()
    for x in parents:
        assert propagate(x,SS)[6]==bits(target)
        rows=run(bits('11101')+x,6)
        if tuple(r[4] for r in rows[:6])==SS:
            assert rows[6][5:]==bits(target)
            realized.add(x)
    return realized,counts


def certificate(source,steps):
    rows=[source]
    for t in range(steps):
        old=rows[-1]
        new=update((t%2,)+old)
        if old[-1]:
            new+=(old[-2]^1,)
        for far in (0,1):
            assert update((t%2,)+old+(far,))[:len(new)]==new
        rows.append(new)
    return rows


def main():
    a,counts=white_ss_parents('00011111')
    assert counts==[2,8,20,62,188,212] and len(a)==182
    b,counts=white_ss_parents('0011001')
    assert counts==[3,5,13,46,105,195] and len(b)==195
    high,h_counts=lift(b,H,HIGH_SHIELDS)
    assert h_counts==[438,1351,4545,1595,1452,4487,8473,5590,14120,22724]
    assert {x[:7] for x in high}=={bits('1101001')}
    assert {x[:10] for x in high}=={bits('1101001')+q for q in product((0,1),repeat=3)}
    # Four white fifth cells immediately precede any D-to-H101 origin.
    parents={bits('1101001')}
    expected=(
        ('01011010','01011011','01011100','01100001'),
        ('001111010','001111011','001111100'),
        ('0001001101','0001001110','0001001111'),
        (),
    )
    for layer in expected:
        parents={x for y in parents for x in inverse(y,0)}
        assert parents=={bits(w) for w in layer}
    # Reconstruct the full nonvacuous low packet independently.
    ss_prefixes={bits(w) for w in ('0000','0100','0101','0110','0111')}
    entrance,e_counts=lift(ss_prefixes,H,HIGH_SHIELDS)
    assert e_counts==[5,15,49,20,28,56,72,88,216,248]
    low,l_counts=lift(entrance,D,LOW_SHIELDS)
    assert l_counts==[992,1176,2144,1888,3008,3648,2976,4576,16000,17376]
    assert bits('11100')+min(low)==NONVACUOUS
    controls=implications=0
    for word,steps,target in COUNTERS:
        rows=certificate(bits(word),steps)
        assert rows[-1][:len(target)]==bits(target)
        expected_track=SS if steps==6 else H+SS
        assert tuple(r[4] for r in rows[:steps])==expected_track
        implications+=2*steps
        for tail in product((0,1),repeat=5):
            for far in (0,1):
                full=run(bits(word)+tail+(far,)*24,steps)
                for t,p in enumerate(rows):
                    assert full[t][:len(p)]==p
                controls+=1
    rows=certificate(NONVACUOUS,26)
    assert rows[10][:9]==bits('111001101')
    assert rows[20][:9]==bits('111010000')
    assert rows[26][:9]==bits('111010000')
    assert tuple(r[4] for r in rows[:26])==D+H+SS
    implications+=52
    for tail in product((0,1),repeat=5):
        for far in (0,1):
            full=run(NONVACUOUS+tail+(far,)*32,32)
            for t,p in enumerate(rows):
                assert full[t][:len(p)]==p
            assert tuple(r[4] for r in full[:32])==D+H+SS+SS
            controls+=1
    # Known positive, unrelated to the low-origin cylinder.
    source=bits('0000')+(0,)*10
    target=propagate(source,SS)[6]
    known,_=white_ss_parents(''.join(map(str,target)))
    assert source in known
    print(dict(white_SS_A=182,white_SS_bad_B=195,high_bad_B=22724,
               high_guard='1101001',four_white_parents=[4,3,3,0],
               complete_low_entrance=17376,causal_implications=implications,
               literal_packed_histories=controls,known_SS='PASS',
               D_H_SS_B00_implies_white12='ALL-TAIL',
               actual_black_SS_entrance='UNKNOWN cap retained',
               arbitrary_SS_blocks='OPEN',all_depth_bound='OPEN'))


if __name__=='__main__':
    main()
