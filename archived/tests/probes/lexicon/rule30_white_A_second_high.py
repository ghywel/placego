"""GC1138: compose the white-A entrance with the next high-renewal gate.
Missing inference: GC1137's sixteen negative entrances might still retain
an A-lineage guard excluding a second high LL. Test that named guard,
not older ages or wider strips. Record searched: white.A|GC1136|GC1137
AND second|repeat|renewal ->53 hits31 files; GC1081/82,1135/36/37 read.
P1 BEFORE run: the sixteen A25 cylinders force the time21 band to miss
GC1081's necessary repeat pattern at sites14..20 =0001111.
Counterfactual: an A entrance may realise a second high LL on the same
actual trajectory, even though a third remains barred by GC1082.
First use fresh-right prefix implications. If unresolved, extend a
specific negative cylinder, stopping at the first complete all-tail
repeat certificate or 4096 attempted prefixes (UNKNOWN at the cap).
Controls: every retained-prefix step checked for both fresh right bits;
an independent complete source35 cone checks the new time21 bit;
GC1135's mature SS is the identified unexpected same-history check.
No solver, CUT, language, record, strip or ancestry-age census.
"""
from itertools import product
from rule30_white_A_high_LL_guard import bits, run, selector, S, D, H
from rule30_white_A_high_sparse_guard import fixed_prefix
from rule30_inherited_high_repeat import inherited_gate


def text(row):
    return ''.join(map(str,row))


def misses(row):
    # At time21, the eight-cell band10001100 followed by0001111
    # is necessary before the reviewed eleven-bit repeat gate applies.
    required=bits('100011000001111')
    return any(x!=required[j] for j,x in enumerate(row[5:20]))


def main():
    origins=[bits('1110100011011')+p for p in product((0,1),repeat=12)
             if selector(p)]
    origins=[p for p in origins if run(p,6)[6][17:19]==(1,1)]
    blocked=[];open_origins=[]
    for p in origins:
        q=fixed_prefix(p,21)[21]
        (blocked if misses(q) else open_origins).append(p)
    print('initial_fixed_gate',len(blocked),'blocked',len(open_origins),'open',flush=True)
    attempts=0;found=None
    leaves=[];unfinished=False
    for seed in open_origins:
        stack=[seed]
        while stack and attempts<4096:
            p=stack.pop();attempts+=1
            q=fixed_prefix(p,21)[21]
            if misses(q):
                leaves.append((p,q));continue
            if len(q)>=24:
                if inherited_gate(q[13:24]):found=p;break
                continue
            stack.extend([p+(1,),p+(0,)])
        unfinished=bool(stack)
        if found or unfinished:break
    print('attempts',attempts,'P1_lineage_exclusion',not bool(found),
          'search_status','COUNTER' if found else ('UNKNOWN' if unfinished else 'COVERED'),flush=True)
    for p in blocked:
        q=fixed_prefix(p,21)[21]
        assert q[:14]==bits('01100100011001')
        required=bits('100011000001111')
        j=next(j for j,x in enumerate(q[5:20]) if x!=required[j])
        print('initial_block',text(p[13:]),'site',j+6,'actual',q[j+5],flush=True)
    for p,q in leaves:
        assert q[:14]==bits('01100100011001')
        print('split_leaf',text(p),'gate21',text(q),flush=True)
    if not found and not unfinished:
        # Prefix-free leaves cover each unresolved source cylinder.
        for root in open_origins:
            descendants=[p for p,q in leaves if p[:25]==root]
            n=max(map(len,descendants))
            assert sum(1<<(n-len(p)) for p in descendants)==1<<(n-25)
        # Complete independent cones fix the bit even on the two
        # source25 cylinders where contiguous induction lost it.
        cones=0
        for root in origins:
            for far in product((0,1),repeat=10):
                r=run(root+far,21)
                assert r[21][:14]==bits('01100100011001')
                cones+=1
        print('complete_source35_cones',cones,'literal_packed_PASS',flush=True)
        # Tick21 is black-wall phase. The common14 prefix alone
        # discharges into ordinary001000 at tick26 for every tail.
        for far in product((0,1),repeat=3):
            r=run(bits('01100100011001')+far,5,phase=1)
            assert r[5][:12]==bits('111001001000')
        print('black_phase_low12_cones8_PASS',flush=True)
        # Unexpected control: retain GC1135's mature origin with its
        # real two-tick past, rather than a newly assigned high tail.
        mature=bits('000111011001010010000000000000000')
        r=run(mature+(0,)*32,54)
        a=r[8][:25];assert a in origins
        assert r[24][:15]==bits('111001111100000')
        assert r[29][:14]==bits('01100100011001')
        assert r[34][:12]==bits('111001001000')
        assert misses(fixed_prefix(a,21)[21]) or any(
            r[8][:len(p)]==p for p,q in leaves)
        for far in product((0,1),repeat=4):
            ext=run(mature+(0,)*32+far,54)
            assert all(ext[t][:len(y)]==y for t,y in enumerate(r))
        print('mature_same_history_control_exteriors16_PASS',flush=True)
    if found:
        rows=fixed_prefix(found,46)
        print('repeat_source',text(found),'length',len(found),flush=True)
        print('gate21',text(rows[21]),flush=True)
        # Full source cone, not fixed-prefix shrinkage, validates track.
        full=found+(0,)*max(0,52-len(found))
        r=run(full,46)
        assert tuple(y[4] for y in r[:46])==S+D+H+D+H
        assert r[16][:15]==bits('111001111100000')
        assert r[36][:13]==bits('1110011111000')
        assert r[46][:6]==bits('111001')
        print('high16',text(r[16][:15]),'low26',text(r[26][:19]),
              'high36',text(r[36][:15]),'low46',text(r[46][:6]),flush=True)
        for far in product((0,1),repeat=4):
            ext=run(full+far,46)
            assert all(ext[t][:len(y)]==y for t,y in enumerate(r))
        print('literal_packed_exteriors16_PASS',flush=True)


if __name__=='__main__':main()

# OUTCOME: P1 HELD, proved by a prefix-free all-tail certificate.
# Fourteen source25 prefixes fix01100100011001 at21 directly.
# The other two fix it after either value of source26 (four leaves).
# Source35's16384 cones and eight black-phase low12 cones agree.
# Therefore all16 negative entrances return ordinary001000 at26;
# GC1082's reviewed guard then discharges to C/101, with no further
# high LL in the same ordinary-long run. The12 positive entrances
# already have GC1137's stopping bit: all28 allow at most one high
# LL per continuing ordinary-long run. A later S may reset it;
# no bound on mixed runs, untyped residence or R_real is claimed.
