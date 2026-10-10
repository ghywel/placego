"""GC1076: transport an actual high LL through its long return.
Missing inference: GC1075 pins high-LL origin 111; carry that actual
pin into the following selector rather than choosing a fresh triple.
Record searched: 111001111|high.*LL|LL.*high with transport|return|
site 9|ninth -> 31 hits in 12 files. GC1053 has the general return form,
not the high-origin four-white shield or next selector identity.
P1 BEFORE controls: initial 111001111 has time 4 sites 6..8=000,
time 5 sites 6,7=10. A return to L0 requires time 5 site 8=0 and sites 9
OR 10=1. These imply time 7 sites 6..9=0000 for every farther tail.
P2: writing Q,R,S at time 7 sites 10..12, returned sites 7..9 are
(NOT Q,Q OR R,NOT Q AND(R OR S)). The next long's fifth track is
high iff its returned ninth bit is 1. Its low origin triple is 010 or 100;
its high origin is 101 (forces S) or 111 (needs the joint return read).
Counterfactual: R alone determines the next high track. Q=0,R=0,S=1
is locally high and forces S; Q=1,R=S=1 gives low despite both ones.
Unexpected check: the high-return shield has four whites at time 7,
so its final triple map equals the reviewed low mid01 return map,
despite different fifth tracks during the preceding long.
Controls: 48 two-tick local shields, 8 closing algebra assignments,
64 selected actual origins with both constant farther patterns.
Literal versus packed, exact intermediate identities. No solver,
membership query, mixed-word scan or relaxed-record computation.
RETAINED FAILURE: P1 wrongly replaced time 6 site 8 by sites 9 OR 10
at 5. For time 5 sites 9,10=01 the time 6 prefix is 1101, so time 7
has 0001, not0000. The unconditional four-white shield is REFUTED.
P3 BEFORE rerun: set b=time 5 site 9. Every high LL has time 7
sites 6..9=(0,0,0,NOT b). If b=0, time 5 site 10=1 forces time 7
site 10=0; GC1053 then makes the returned triple 001, hence next low.
If b=1, the four-white shield and P2 closing map hold exactly.
Thus a following high track requires b=1 and Q=0,R OR S=1;
a following high LL requires additionally R=1 by GC1075.
SECOND FAILURE: treating every non-high next track as 0101100000
fails on initial 11100111101101 plus zeros: current high LL returns
triple 001, then fifth track 0101100101, outside a renewed S/L0 run.
GC1046 explicitly requires the next interval to renew; that premise
was missing. This unconditioned low-track inference is CLOSED.
P4 BEFORE rerun: retain H,D,X tracks. H occurs iff b=1 and returned
ninth=1; D renews L0; X exits the synchronized S/L0 collar. Only on
an actual continuing mature run may non-high be identified with D.
Keep the witness and check the exit rather than deleting it.
THIRD FAILURE found by algebra before the extra control: the proposed
complete equality with the mid01 map fails at Q=1,R=S=0. That map
returns011 while this high branch returns010. P5 BEFORE checking:
only Q=0 maps agree; the high branch pins Q=1 to010 regardless R,S.
OUTCOME: 48 local shields and 8 closing identities PASS; 64 selected
origins have 29 current high LL, followed by 23 D and 6 X exits, no H.
That absence of sampled H is evidence, not a new universal exclusion.
The marker-conditioned identity passes literal and packed engines.
No broader search after these local scope corrections.
"""
from itertools import product
from rule30_sl_no_refork import bits, run


def update(row):
    return tuple(row[k-1]^(row[k]|row[k+1]) for k in range(1,len(row)-1))


def main():
    local=closing=origins=long_returns=next_high=next_D=next_X=0
    for b,c in ((0,1),(1,0),(1,1)):
      for d,e,f,g in product((0,1),repeat=4):
        at6=update((0,1,0,0,b,c,d,e,f,g))
        assert at6[:4]==(1,1,b,1)
        at7=update((1,)+at6)
        assert at7[:4]==(0,0,0,1-b)
        if b==0: assert at7[4]==0
        local+=1
    for Q,R,S in product((0,1),repeat=3):
        at8=update((0,)+bits('0000')+(Q,R,S))
        at9=update((1,)+at8)
        at10=update((0,)+at9)
        expected=(1-Q,Q|R,(1-Q)&(R|S))
        assert at10==(1,)+expected
        mid01=(1-Q,Q|R,Q^(R|S))
        if Q==0: assert expected==mid01
        else:
            assert expected==bits('010')
            assert (expected!=mid01)==(R==S==0)
        b,c,d=expected
        U=1-((1-(b|c))|(b^(c|d)))
        assert U==d
        assert expected in (bits('010'),bits('100'),bits('101'),bits('111'))
        closing+=1
    for tail in product((0,1),repeat=5):
      for far in (0,1):
        rows=run(bits('111001111')+tail+(far,)*22,20)
        assert rows[4][5:8]==bits('000')
        assert rows[5][5:7]==bits('10')
        assert tuple(r[4] for r in rows[:10])==bits('0101101010')
        a,b,c=rows[5][7:10]
        is_L=rows[10][:6]==bits('111001')
        assert is_L==(a==0 and bool(b|c))
        if is_L:
            long_returns+=1
            assert rows[7][5:9]==(0,0,0,1-b)
            Q,R,S=rows[7][9:12]
            tri=rows[10][6:9]
            if b==0:
                assert Q==0 and tri==bits('001')
                H=0
            else:
                assert tri==(1-Q,Q|R,(1-Q)&(R|S))
                H=tri[2]
            track=tuple(r[4] for r in rows[10:20])
            assert (track==bits('0101101010'))==bool(H)
            assert track in (bits('0101101010'),bits('0101100000'),bits('0101100101'))
            assert H==(b & tri[2])
            next_D+=track==bits('0101100000')
            next_X+=track==bits('0101100101')
            if tri==bits('101'): assert rows[20][:5]==bits('11101')
            if track==bits('0101100000'): assert rows[20][:6]==bits('111001')
            if track==bits('0101100101'):
                assert rows[20][:5]!=bits('11101')
                assert rows[20][:6]!=bits('111001')
            next_high+=H
        origins+=1
    assert (local,closing,origins)==(48,8,64) and long_returns
    print({'local_marker_shields':local,'closing_identities':closing,
           'selected_origins':origins,'current_high_LL':long_returns,
           'next_high':next_high,'next_D':next_D,'next_X_exits':next_X,
           'literal_packed':'PASS','conditional_selector_transport':'PASS'})


if __name__=='__main__': main()
