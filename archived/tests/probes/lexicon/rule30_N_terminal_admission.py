"""GC1130: terminal exits of the N ancestry, not another N-return run.
Missing inference: GC1126 bounds white SS residence and keeps AP13 returns,
but does not classify non-AP13 terminal exits. Can these escape and
replenish the typed budget instead of entering the proved C/J core?
Record searched: GC1126|H.low|N.route AND non.AP|white.A|terminal.exit|
non.black -> 3 hits in 2 files; GC1104 and GC1126 read. The old
137-packet exit theorem and the new 62-packet inclusion are reused.
P1 BEFORE run: every non-SS terminal from the N white-SS ancestry
is either black AP13 or white-eleventh A from GC1104's admitted set.
P2 BEFORE run: all terminal exits occur after k=1 or k=2 white SS;
non-AP13 exits then enter C/J within 16 ticks, hence at most 74
from the original A. Check unfiltered fifth bits for this last leg.
Counterfactual (must fail): a non-AP13 terminal is immediately C/J.
Its high A prefix should refute this, so do not erase the 16-tick leg.
Independent controls: scalar full-path replay of one white terminal
at each represented k; full scalar S-D images without track filtering;
exact old 137 and new 62 carrier counts, original labels retained.
Unexpected check: first SS has no black A but might still have
white A exits. Count them; no black return is not a dead branch.
No solver, CUT, exact membership, product, widening or record run.
No claim about H endpoints that never enter this white-SS carrier.
OUTCOME: P1/P2 HELD. k=1 has 40 continuing packets and no terminals;
k=2 has no continuations, 51 AP13 and 29 white-A terminal packets.
The white terminals carry 870 original-origin pairs; 17 have prefix13
1110100011010 and 12 have 1110100011011. All 145 unfiltered S-D
endpoints enter C/J; selected complete k=2 path scalar-replays.
Unexpected check: there are no white terminals at k=1 either. Every
white terminal waits for k=2, then needs the 16-tick admission leg.
Immediate-C/J counterfactual REFUTED on all 29 white-A endpoints.
No failed proof prediction or empty terminal-admission premise.
REFUTED-BY: white terminal 11101000110111100000 at tick 58,
scalar path from 11101000111011100000. Uniform admission by tick 74
uses reviewed GC1104 plus reviewed GC1126 carrier inclusion/rank.
"""
import signal
from collections import Counter
import rule30_111_low_white_return as n
import rule30_delayed_A_exit_admission as a

r=n.r;q=n.q


def main():
    signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('20s cap')))
    signal.alarm(20)
    starts,_,_,_,ent,seen,ends,first,_=n.relation()
    oldstarts,oldent=r.initial();oldseen,_,_,_=r.closure(oldstarts,oldent)
    assert len(seen)==62 and len(oldseen)==137 and set(seen)<=set(oldseen)
    oldout=r.flow(oldseen,q.SS)
    oldterminal={x for x in oldout if x&r.SSMASK not in r.SSPREFIX}
    oldwhite={x for x in oldterminal if x&q.AMASK not in r.AP}
    assert len(oldterminal)==139 and len(oldwhite)==38
    layers={0:ent};terminal={};allwhite=set();counts={}
    for k in (1,2):
        out=r.flow(layers[k-1],q.SS)
        terminal[k]={x:o for x,o in out.items() if x&r.SSMASK not in r.SSPREFIX}
        layers[k]={x:o for x,o in out.items() if x&r.SSMASK in r.SSPREFIX}
        white={x:o for x,o in terminal[k].items() if x&q.AMASK not in r.AP}
        black={x:o for x,o in terminal[k].items() if x&q.AMASK in r.AP}
        assert set(white)<=oldwhite
        assert all(x&((1<<13)-1) in {q.pack(n.bits('1110100011010')),q.pack(n.bits('1110100011011'))} for x in white)
        allwhite.update(white)
        counts[k]={'continuing':len(layers[k]),'black_AP13':len(black),'white_A':len(white),
                   'white_origin_pairs':sum(o.bit_count() for o in white.values())}
        if white:
            z=min(white);i=(white[z]&-white[z]).bit_length()-1
            path,word=n.witness(starts[i],z,k)
            assert len(path)-1==46+6*k
            print('white_terminal_witness',k,''.join(map(str,q.unpack(starts[i]))),
                  ''.join(map(str,q.unpack(z))),'scalar_PASS',flush=True)
    assert not layers[2]
    assert {x for k in terminal for x in terminal[k] if x&q.AMASK in r.AP}==set(ends)
    # Apply GC1104's already proved 16-tick admission theorem. This
    # control verifies its hypotheses on every retained terminal and
    # checks the full scalar images; it does not reprove its OR shield.
    assert allwhite and not any(a.core_long(x) for x in allwhite)
    low,sc=a.unfiltered(allwhite,q.S)
    late,dc=a.unfiltered(low,q.D)
    assert all(a.core_long(x) for x in late)
    print('terminal_layers',counts,'white_union',len(allwhite),
          'white_prefix13',dict(Counter(''.join(map(str,q.unpack(x)[:13])) for x in allwhite)),
          'unfiltered_S_counts',sc,'unfiltered_D_counts',dc,
          'admitted_low_packets',len(late),'last_possible_admission_tick',74,
          'counterfactual_immediate_CJ','REFUTED',flush=True)
    signal.alarm(0)


if __name__=='__main__':main()
