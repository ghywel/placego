"""GC1100: test full-strip consistency at white-SS entrance after black A.

Missing inference: can mature black-A S-D101-H enter any white SS?
A universal exclusion would remove the arbitrary-block branch outright.
Record searched: black.A.*SS|SS.*black.A with entrance|age|no.SS
->19hits8files; GC1097/98/99 and CL275 read. New evidence is CL275's
full-row shortcut: sub-row fifth-clamping loses the strip's own past.
P1 BEFORE run: a black-A at even clamped age>=4 cannot enter SS after
S-D101-H. Pull all five white-SS entrance prefixes through the full
row with realized fifth tracks; impose black-A and four earlier ticks.
P2 BEFORE run: if P1 has parents, at least one has an actual black-SS
six-step origin. Cap each complete inverse layer at500000; cap means
UNKNOWN, not absence. Do not extend a capped sub-row ancestry tree.
Counterfactual: white SS is only a boundary-relaxation artifact. The
known fresh low D-H-SS-SS source must remain a full-row positive.
Independent controls: CL275's bad B counts and a positive H parent;
every inverse edge forwardchecked, literal/packed selected full rows.
Unexpected: the fresh low source has real SS and must not be lost by
prematurely asserting the mature black-A premise on every low row.
No solver, CUT, membership or relaxed-record computation.
P1 UNKNOWN: full S frontier hit555392 at S-time2, before the black-A
filter could act. P2 not reached. Stop the complete-frontier attempt.
P3 BEFORE a different existential check: streaming one packet at a
time through the known S/SS shields finds an actual black-SS origin
within250000 inverse nodes. A found source refutes no-entrance; a
visit cap is UNKNOWN and never a universal exclusion.
P3 HELD:110783 visited inverse edges yield ACTUAL below. P4 BEFORE
causal controls: its41 fixed cells force actual black SS, black A at6,
low00100 at12, high101 at22, white SS at32, then its SS fifth trace
through37 for every exterior. P5 predict a second SS entrance at38. REFUTED: black-A returns.
P4 HELD; this all-tail source refutes P1, despite its UNKNOWN frontier.
P6 BEFORE attribution control: unprojected sub-row bad-B high parents
still survive five D ticks, so CL275's gain requires full strip
consistency rather than only restoring the discarded future cells.
P6 HELD: identical112 high packets give five-D sub counts448,588,968,
280,224 versus full164,460,456,96,0. CL275 is independently confirmed.
Alignment check BEFORE the final replay: GC986 bounds4422 in GAP
LENGTHS. Our LLSS has5533, not4422 (S/L have2/4 zeros). The proposed
budget transfer therefore fails; do not spend or infer a4422 event.
OUTCOME:88 causal implications and64 independent histories PASS;
actual black-A delayed restart at6->38, with white SS at32. This
closes no-SS entrance, not eventual admission or the all-depth bound.
The capped complete frontier is retained only as a failure receipt;
default run replays the fixed counter and packet controls. Optional
construct replays the bounded streaming witness derivation.
"""
from rule30_black_A_ancestry_guard import inverse
from rule30_sl_no_refork import bits, run
from rule30_core_short_bridge import S,D
from rule30_black_A_B_admission import BAD_HIGH
from rule30_white_SS_exit_guard import NONVACUOUS,SS,H

WHITE_SS={bits('11101'+w) for w in ('0000','0100','0101','0110','0111')}
BLACK_A=bits('1110100011111')
ACTUAL=bits('11101111111010000001101000000001111001010')
S_SHIELDS=('00011111','10110000','0010100','111011','100010','11011')
SS_SHIELDS=('1111','00000001','10000011','01000110','1110110','00001')


def lift(parents,track,prefix=None,additional=None):
    counts=[]
    for t in range(len(track)-1,-1,-1):
        parents={x for y in parents for x in inverse(y,t%2)
                 if x[4]==track[t]}
        if t==0 and prefix is not None:
            parents={x for x in parents if x[:len(prefix)]==prefix}
        if additional and t in additional:
            p=additional[t]
            parents={x for x in parents if x[:len(p)]==p}
        counts.append(len(parents))
        if len(parents)>500000:
            return None,counts
    return parents,counts


def construct(high):
    nodes=0
    def stream(y,track,prefix,shields=(),t=None):
        nonlocal nodes
        if t is None:t=len(track)-1
        if t<0:
            yield y;return
        for x in sorted(inverse(y,t%2)):
            nodes+=1
            if nodes>250000:raise RuntimeError('visit cap')
            if x[4]!=track[t]:continue
            if t<len(shields) and x[5:5+len(shields[t])]!=bits(shields[t]):continue
            if t==0 and x[:len(prefix)]!=prefix:continue
            yield from stream(x,track,prefix,shields,t-1)
    try:
        for h in sorted(high):
            for low in stream(h,D,bits('11100100100')):
                for a in stream(low,S,BLACK_A,S_SHIELDS):
                    for source in stream(a,SS,bits('111011111'),SS_SHIELDS):
                        rows=run(source,32)
                        assert rows[6][:13]==BLACK_A
                        assert rows[32] in WHITE_SS
                        assert tuple(r[4] for r in rows[:32])==SS+S+D+H
                        print('constructed actual black SS',nodes,''.join(map(str,source)),flush=True)
                        return source
    except RuntimeError as e:
        print('P3 UNKNOWN',str(e),nodes,flush=True)
        return None
    print('P3 no source in this shielded search',nodes,flush=True)
    return None


def main():
    from itertools import product
    from rule30_white_SS_exit_guard import certificate
    from rule30_black_A_B_admission import HIGH_SHIELDS,ACTUAL as GOOD_SOURCE
    bad,hb=lift({bits('111010011001')},H,bits('111001101'))
    assert hb==[3,5,13,46,79,60,152,420,104,112]
    assert BAD_HIGH[:22] in bad
    sub={bits('0011001')}
    for t in range(9,-1,-1):
        sub={x for y in sub for x in inverse(y,H[t])
             if t>=7 or x[:len(HIGH_SHIELDS[t])]==bits(HIGH_SHIELDS[t])}
    assert sub=={x[5:] for x in bad}
    sub_counts=[]
    for t in range(9,4,-1):
        sub={x for y in sub for x in inverse(y,D[t])}
        sub_counts.append(len(sub))
    assert sub_counts==[448,588,968,280,224]
    bad,db=lift(bad,D)
    assert db[:5]==[164,460,456,96,0] and not bad
    # The actual good B's known full-row path is accepted at every edge.
    good=run(GOOD_SOURCE+(0,)*8,32)
    assert good[32]==bits('111010011000')
    for t in range(31,11,-1):
        assert good[t] in inverse(good[t+1],t%2)
        assert good[t][4]==(H[t-22] if t>=22 else D[t-12])
    rows=certificate(ACTUAL,44)
    expected={0:'111011111',6:'1110100011111',12:'11100100100',
              22:'111001101',32:'111010000',38:'1110100011111',
              44:'11100100100'}
    for t,p in expected.items():assert rows[t][:len(p)]==bits(p)
    assert tuple(r[4] for r in rows[:44])==SS+S+D+H+SS+S
    q=''.join(str(rows[t][0]) for t in range(0,45,2))
    assert q=='10010010000100001001001'
    ones=[i for i,b in enumerate(q) if b=='1']
    assert tuple(b-a for a,b in zip(ones,ones[1:]))==(3,3,5,5,3,3)
    assert q[6:]=='10000100001001001'
    assert '1000100010101' not in q[6:] # GC986's4422 budget is different.
    histories=0
    for tail in product((0,1),repeat=5):
        for far in (0,1):
            full=run(ACTUAL+tail+(far,)*40,44)
            for t,p in enumerate(rows):assert full[t][:len(p)]==p
            histories+=1
    # Replay the discovered path in reverse without a frontier census.
    for t in range(31,-1,-1):
        end=9+32-(t+1)
        assert rows[t][:end+1] in inverse(rows[t+1][:end],t%2)
    print(dict(actual_origin_cells=len(ACTUAL),black_A_times=[6,38],
               white_SS_time=32,macro='SS-S-D-H-SS-S',
               visible_gaps=[3,3,5,5,3,3],causal_implications=88,
               literal_packed_histories=histories,
               bad_B_full_five_D=db[:5],bad_B_sub_five_D=sub_counts,
               no_SS_entrance='REFUTED all-tail',
               second_SS_prediction='REFUTED: black-A instead',
               arbitrary_block_admission='OPEN',all_depth_bound='OPEN'))


if __name__=='__main__':
    import sys
    if sys.argv[1:]==['construct']:
        high,c=lift(WHITE_SS,H,bits('111001101'))
        assert c==[5,15,49,44,88,56,144,560,360,248]
        assert construct(high)==ACTUAL
    else:
        assert not sys.argv[1:]
        main()
