"""GC1135: does white SS alone supply the delayed-exit admission guard?
Missing inference: GC1104 keeps A-S-D-H ancestry; GC1134 excluded
only one fresh counter. Test the broader, specific white-SS premise.
Record searched: white.A|white-SS AND mature|entrance|guard ->66 hits,
23 files; 111001001001100|111001001001111 AND guard|shield|return
->8 hits,5 files. GC1104,1080..82,1131 and1134 read. The B decoder
is established and is not recomputed as a research result.
P1 BEFORE run: every white-SS to white-A exit has GC1104's low
admission guard after S, without the older black-A ancestry.
Counterfactual: white SS suffices to import GC1104. A complete
finite cone reaching high111 rather than C/J refutes this shortcut.
P2 BEFORE run: a found full cone has a two-tick clamped past,
so the counter is not just the excluded fresh GC1090 diagnostic.
If P2 fails, retain that failure; do not scan ages or widen strips.
Construct white-A13's complete six-tick past with the SS track,
then the eight missing causal bits of its S-to-low15 guard. Stop
at the first guard failure; test its sixteen completions for the
nine endpoint bits of S-D. No absence claim from this search.
Controls: every inverse edge scalar checked; literal versus packed
complete cone, every farther tail masked outside that cone;
GC1104's fifteen-cell admitted low shield remains positive.
Unexpected check: retain a full two-tick predecessor, including
its SS marker and phase, rather than testing only an output prefix.
This is a finite local causal counter to one admission premise,
not a solver, CUT, membership, graph, record or age census.
"""
from itertools import product
from rule30_black_A_ancestry_guard import inverse
from rule30_sl_no_refork import bits,run
from rule30_core_short_bridge import S,D
from rule30_001_high_return_gate import H,gate

SS=bits('111010')
GUARD=bits('111001001001001')
CORE={bits(x) for x in ('010','011','100')}

def parents():
    states={bits('111010001101'+b) for b in '01'}
    sizes=[]
    for t in range(5,-1,-1):
        states={x for y in states for x in inverse(y,t%2) if x[4]==SS[t]}
        sizes.append(len(states))
        assert len(states)<=20000, 'frontier cap, UNKNOWN'
    states={x for x in states if x[:5]==bits('11101') and x[5]==0}
    for x in states:
        rows=run(x,6)
        assert tuple(y[4] for y in rows[:6])==SS
        assert rows[6][:12]==bits('111010001101')
    return sorted(states),sizes

def main():
    starts,sizes=parents();checked=0;first=None
    for x in starts:
        for tail in product((0,1),repeat=8):
            src=x+tail;rows=run(src,12);low=rows[12]
            assert tuple(y[4] for y in rows[:12])==SS+S
            checked+=1
            guard=low[10] or low[:15]==GUARD
            if not guard:
                first=src;break
        if first:break
    print('SS_inverse_sizes',sizes,'SS_sources19',len(starts),
          'guard_cones_checked',checked,'P1_guard',not first,flush=True)
    found=None
    if first:
        for tail in product((0,1),repeat=4):
            src=first+tail;rows=run(src,22)
            assert tuple(y[4] for y in rows[:22])==SS+S+D
            if rows[22][6:9] not in CORE:
                found=src;break
    assert found is not None,'no counter retained; do not claim universal absence'
    rows=run(found,22)
    # Structural composition BEFORE controls: the retained low19 is
    # exactly GC1080 case B. Its reviewed all-tail gate supplies H
    # returning L0; no bare-age or longer-time census is needed.
    low=rows[12]
    assert low[:17]==bits('11100100100110000')
    assert low[17]|low[18]
    assert gate(low[9:19])
    past={x for y in inverse(found,1) for x in inverse(y,0)}
    print('source31',''.join(map(str,found)),
          'whiteA6',''.join(map(str,rows[6])),
          'low12',''.join(map(str,rows[12])),
          'endpoint22',''.join(map(str,rows[22])),
          'two_tick_past',len(past),'P2_mature',bool(past),flush=True)
    if past:
        p=min(past)
        complete=run(p,24)
        assert complete[2]==found
        assert complete[24][:9]==rows[22][:9]
        print('predecessor33',''.join(map(str,p)),flush=True)
    # Complete endpoint cone: its first nine bits use exactly 31 source
    # cells through 22 ticks. Exterior controls verify the bound explicitly.
    for tail in product((0,1),repeat=4):
        ext=run(found+tail,22)
        assert all(ext[t][:len(y)]==y for t,y in enumerate(rows))
        extended=run(found+tail+(0,)*16,32)
        assert tuple(y[4] for y in extended[:32])==SS+S+D+H
        assert extended[22][:13]==bits('1110011111000')
        assert extended[32][:6]==bits('111001')
    for tail in product((0,1),repeat=4):
        assert run(GUARD+tail,10)[10][:9]==bits('111001100')
    print('causal_exterior_controls16 positive_shield16 H_LL_composition16 scalar_packed_PASS',flush=True)

if __name__=='__main__':main()

# OUTCOME: P1 REFUTED; P2 HELD. 116 SS source19 packets; first
# failed guard after 9473 complete cones. Source31 and predecessor33
# retained by main. Their low19 is GC1080 case B, so H returns L0
# at32 for every exterior. Neither eventual admission nor any bound
# on repeated untyped visits follows. No age scan is authorized.
