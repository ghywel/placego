"""GC1104: retain all non-black-A exits from the delayed white SS block.

Missing inference: GC1103 budgets consecutive black11 A returns;
a non-A exit might return later and replenish the exception rank.
Determine the exact exit prefixes in its existing sound20-cell
relation, then test whether each other non-SS exit enters GC1087's
absorbing core. This is a targeted exit composition, not a wider
strip, solver, membership or relaxed-record run.
Record searched: A.exit|non.A|reentr|replenish with core|guard|
GC1087|GC1103 ->27 hits17files; GC1087/1090/1098..1103 read.
P1 BEFORE run: after at least one white SS, all non-black11-A exits
enter the core in at most16 more ticks: either guarded B immediately,
or C/J after S6 or S6-D10. Keep the original A-S-D-H ancestry.
Counterfactual: a fresh white11 A label implies the same admission;
GC1090's actual counter to that shortcut must remain outside C.
Controls: eight scalar six-tick origin flows reproduce the SS exits;
the actual GC1100 A return remains represented; every retained
transition projects to both scalar right-input images.
Unexpected check: exits may be absent in the controlled relaxation,
making a claimed conditional guard vacuous. Report exact exit counts
and prefix types before applying any core implication.
Do not infer global admission or a record bound from this one branch.
P1 HELD in the filtered relation:139 terminal packets,101 black A
and38 white A; no B or010 exit. S returns57 packets; D returns157,
all low010/100 in C. P2 BEFORE proving the unconditional scope:
every retained exit forces S then D even without filtering column5.
Otherwise the first check has silently dropped a real escaping path,
and does not prove admission. Check all intermediate fifth bits.
P3 BEFORE compact shield extraction: the non-GC1090 low branch
(site11 white) has a common sufficient prefix forcing C100 under D.
Counterfactual: the first13 low bits alone give that implication.
Require an explicit causal shield or keep only the finite certificate.
P2 HELD with no fifth-bit filtering at all. The site11-white low
branch has common15-prefix111001001001001. P4 BEFORE causal replay:
this15-prefix alone forces low C100 after D10 for every farther tail,
whereas its first13-prefix alone does not. Retain a literal counter.
P4 causal-prefix replay FAILED: the conservative known-prefix shield
does not retain nine endpoint cells. This is inconclusive for the
15-prefix implication; no longer prefix is silently substituted.
P5 BEFORE independent complete cones: all16 assignments on sites16
through19 after that15-prefix give C100 at D10; at least one of64
assignments after the13-prefix fails C. These are complete causal
cones for the nine claimed endpoint cells, not a longer-time scan.
P5 HELD:16 complete cones give C100, while13-prefix counter
1110010010010000000 fails. P6 BEFORE local closure controls:
the causal prefix at D7 is1101010010 (sites9,10=10). With a,b at
sites11,12, D8 sites10,11=(NOT a,a OR b), whose OR is1. The known
D8 site9=1 then forces D9 site10=0; D9 sites8,9=00 force D10
site9=0. This repairs the prefix shield with a joint OR invariant,
not by adding source cells. Check all four local a,b assignments.
OUTCOME: P1/P2/P3/P5/P6 HELD, P4 prefix-only method failed at eight
known endpoint cells. The repaired hand shield has nine. All other
exits are white A and enter C in16 ticks; no B guard is asserted.
REFUTED-BY: retained fresh white-A counter and insufficient13 low
counter. No actual existence of a white exit is inferred from its
presence in the sound relaxation; admission holds if it occurs.
"""
import rule30_delayed_A_SS_star_rank as r
from rule30_sl_no_refork import bits,run
from rule30_white_SS_exit_guard import certificate
from itertools import product

q=r.q
A9=q.pack(bits('111010001'))
B9=q.pack(bits('111010011'))
C9=q.pack(bits('111010010'))
LOW6=q.pack(bits('111001'))
CORE={q.pack(bits(w)) for w in ('010','011','100')}


def guarded_b(x):
    return x&r.SSMASK==B9 and not((x>>9)&1) and (((x>>10)&1) or not((x>>11)&1))


def core_long(x):
    if x&63!=LOW6:return False
    tri=(x>>6)&7
    if tri in CORE:return True
    if tri!=q.pack(bits('101')):return False
    return (x>>9)&7==q.pack(bits('100')) or (x>>9)&31==q.pack(bits('11110'))


def unfiltered(states,track):
    sizes=[]
    for t,b in enumerate(track):
        assert all((x>>4)&1==b for x in states),(t,b)
        assert all(set(q.successors(x,t))==q.scalar_successors(x,t) for x in states)
        states={y for x in states for y in q.successors(x,t)}
        sizes.append(len(states))
    return states,sizes


def main():
    starts,entrances=r.initial();seen,_,_,_=r.closure(starts,entrances)
    out=r.flow(seen,q.SS)
    # White SS continuations stay inside the known finite inner relation.
    exits={x:o for x,o in out.items() if x&r.SSMASK not in r.SSPREFIX}
    black={x:o for x,o in exits.items() if x&q.AMASK in r.AP}
    other={x:o for x,o in exits.items() if x not in black}
    types={}
    for x in other:types.setdefault(''.join(map(str,q.unpack(x)[:13])),0);types[''.join(map(str,q.unpack(x)[:13]))]+=1
    assert all(x&r.SSMASK in {A9,B9,C9} for x in exits)
    b={x:o for x,o in other.items() if x&r.SSMASK==B9}
    candidates={x:o for x,o in other.items() if x not in b}
    assert (len(exits),len(black),len(other))==(139,101,38)
    assert types=={'1110100011010':26,'1110100011011':12}
    low=r.flow(candidates,q.S)
    immediate={x:o for x,o in low.items() if core_long(x)}
    pending={x:o for x,o in low.items() if not core_long(x)}
    late=r.flow(pending,q.D)
    bad={x:o for x,o in late.items() if not core_long(x)}
    whole_s,s_counts=unfiltered(set(other),q.S)
    whole_d,d_counts=unfiltered(whole_s,q.D)
    assert whole_s==set(low) and whole_d==set(late)
    assert not b and not bad
    assert (len(low),len(late))==(57,157)
    assert all(x&63==LOW6 and (x>>6)&7 in {q.pack(bits('010')),q.pack(bits('100'))} for x in late)
    special={x for x in low if not((x>>10)&1)}
    prefixes={n:sorted({''.join(map(str,q.unpack(x)[:n])) for x in special})
              for n in range(13,18)}
    assert prefixes[15]==['111001001001001']
    assert all((x>>10)&1 or x&((1<<15)-1)==q.pack(bits(prefixes[15][0])) for x in low)
    assert all(x&((1<<11)-1)==q.pack(bits('11100100101')) for x in low if (x>>10)&1)
    shield=bits('111001001001001')
    rows=certificate(shield,10)
    causal_prefix_end=len(rows[-1])
    assert causal_prefix_end<9
    shield_cases=0
    for tail in product((0,1),repeat=4):
        full=run(shield+tail,10)
        assert full[-1][:9]==bits('111001100')
        assert tuple(y[4] for y in full[:10])==q.D
        shield_cases+=1
    complementary_controls=0
    for u,v in product((0,1),repeat=2):
        local=run(rows[7]+(u,v),3,phase=1)
        assert local[1][9:11]==(1-u,u|v)
        assert local[2][7:10]==(0,0,0)
        assert local[3][:9]==bits('111001100')
        complementary_controls+=1
    counters=[]
    for tail in product((0,1),repeat=6):
        origin=shield[:13]+tail
        test=run(origin,10)
        assert tuple(y[4] for y in test[:10])==q.D
        if test[-1][6:9] not in {bits(w) for w in ('010','011','100')}:
            counters.append(origin)
    assert counters
    scalar=0
    for x in sorted(seen)[::max(1,len(seen)//8)][:8]:
        states={x}
        for t,bit in enumerate(q.SS):
            states={y for a in states if (a>>4)&1==bit for y in q.scalar_successors(a,t)}
        assert states==set(r.flow({x:1},q.SS));scalar+=1
    actual=run(r.ACTUAL+(0,)*40,38)
    assert q.pack(actual[38][:20]) in black
    # Known wrong fresh-white-A admission, independently simulated.
    counter=run(bits('11101000110110100010')+(0,)*32,16)
    assert counter[16][6:9]==bits('111')
    print(dict(SS_exit_packets=len(exits),black_A_packets=len(black),
               other_exit_packets=len(other),other_prefix13=types,
               B_packets=len(b),unguarded_B=sum(not guarded_b(x) for x in b),
               immediate_core_packets=len(immediate),pending_low_packets=len(pending),
               late_core_packets=len(late)-len(bad),bad_late_packets=len(bad),
               pending_prefix13=sorted({''.join(map(str,q.unpack(x)[:13])) for x in pending}),
               bad_late_prefix13=sorted({''.join(map(str,q.unpack(x)[:13])) for x in bad}),
               scalar_SS_controls=scalar,actual_A_control='PASS',fresh_white_A_counter='PASS',
               unfiltered_S_counts=s_counts,unfiltered_D_counts=d_counts,
               special_low_prefix15=prefixes[15],
               conservative_prefix_endpoint_cells=causal_prefix_end,
               complete_special_cones=shield_cases,
               complementary_pair_controls=complementary_controls,
               insufficient13_counter=''.join(map(str,counters[0])),
               all_depth_record_bound='OPEN'),flush=True)


if __name__=='__main__':main()
