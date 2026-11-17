"""GC1143: retain H111 past through arbitrary SS, testing B admission.
Missing inference: GC1142 closes only the first following SS-B exit;
a finite carrier excluding badB at every SS length would move Q10.
Record searched:H111|high111|111.diversion|GC1142 AND
B.*guard|SS.star|arbitrary.SS|fixed.point ->31 hits16files.
GC1102/1104/1105/1141/1142 read. Reuse the EXISTING width20
boundary relaxation; no wider strip, Local solver or language run.
P1 BEFORE run: its complete least fixed point from all H111-S
origins has no unguarded B exit at any SS length. Termination uses
the finite state domain, not a k cutoff. Stop on the first violation.
P2 BEFORE run: a first badB occurs no earlier than the second SS,
in agreement with the exact GC1142 first-SS proof. If it occurs on
first SS this relaxation has lost an equation needed by that proof;
retain the path, and do not call the exact theorem refuted.
Counterfactual: badB is reachable after additional SS even though
first-SS B is guarded. An explicit shortest free-boundary path
will identify the ancestry loss and stop this carrier candidate.
Independent controls: scalar one-tick successors on every retained
witness edge and complete run replay on the positive/whitening
GC1142 origins projected into this existing relaxation.
Unexpected check: whitened SS paths can persist while black-marker
paths end; track marker colours rather than discard whitening.
"""
from collections import deque
import rule30_delayed_A_strip_rank as q
from rule30_sl_no_refork import bits,run
from rule30_black_A_white_SS_entrance import WHITE_SS
from rule30_black_A_ancestry_guard import inverse
from rule30_001000_mixed_admission import certificate
from rule30_positive_A_mixed_exit import guarded_B

MASK9=(1<<9)-1
H=bits('0101101010');SS=bits('111010')
B=q.pack(bits('111010011'))
SS_TYPES={q.pack(x) for x in WHITE_SS}|{q.pack(bits(p)) for p in ('111011101','111011110','111011111')}

def flow(states,track,parents=False):
    rows=[]
    for t,b in enumerate(track):
        out={}
        for x in sorted(states):
            if (x>>4)&1!=b:continue
            for y in q.successors(x,t):out.setdefault(y,x)
        states=set(out)
        if parents:rows.append(out)
    return states,rows

def bad_B(x):
    return x&MASK9==B and not((x>>9)&1) and not((x>>10)&1) and ((x>>11)&1)

def path_to(start,target,track):
    ends,parents=flow({start},track,True);assert target in ends
    path=[target]
    for row in reversed(parents):path.append(row[path[-1]])
    return list(reversed(path))

def main():
    high=q.pack(bits('111001111'));starts={high|(x<<9) for x in range(1<<(q.WIDTH-9))}
    ends,_=flow(starts,H);entrances={x for x in ends if x&MASK9 in SS_TYPES}
    assert entrances and all((x>>5)&1 for x in entrances)
    frontier=entrances;seen=set();pred={x:None for x in entrances};depth={x:0 for x in entrances}
    rounds=[];bad=None;terminals=set();white_seen=set()
    while frontier:
        seen|=frontier;nxt=set()
        for a in sorted(frontier):
            out,_=flow({a},SS)
            for z in sorted(out):
                if bad_B(z):bad=(a,z,depth[a]+1);break
                if z&MASK9 in SS_TYPES:
                    if not((z>>5)&1):white_seen.add(z)
                    if z not in seen and z not in nxt:
                        pred[z]=a;depth[z]=depth[a]+1;nxt.add(z)
                else:terminals.add(z)
            if bad is not None:break
        rounds.append((len(frontier),len(nxt)))
        if bad is not None:break
        frontier=nxt
        assert len(seen)<=len(SS_TYPES)*(1<<(q.WIDTH-9))
    print('H111_source20',len(starts),'H_end20',len(ends),'black_SS_entrances',len(entrances),
          'rounds',rounds,'reachable_SS',len(seen),'white_SS_seen',len(white_seen),
          'P1_all_k_badB_absent',bad is None,flush=True)
    if bad is not None:
        a,z,k=bad;macro=[a]
        while pred[macro[-1]] is not None:macro.append(pred[macro[-1]])
        macro.reverse();macro.append(z)
        # Reconstruct one complete H-origin for the earliest entrance.
        hends,hparents=flow(starts,H,True);v=macro[0];hp=[v]
        for row in reversed(hparents):hp.append(row[hp[-1]])
        hp.reverse();path=hp
        for a,b in zip(macro,macro[1:]):path+=path_to(a,b,SS)[1:]
        track=H+SS*k
        assert len(path)==len(track)+1 and k==len(macro)-1
        boundary=[]
        for t,(x,y) in enumerate(zip(path,path[1:])):
            assert y in q.scalar_successors(x,t)
            old=q.unpack(x);nextrow=q.unpack(y)
            choices=[]
            for right in (0,1):
                image=tuple(((t&1) if j==0 else old[j-1])^(old[j]|(old[j+1] if j+1<q.WIDTH else right)) for j in range(q.WIDTH))
                if image==nextrow:choices.append(right)
            assert choices;boundary.append(choices[0])
        fmt=lambda x:''.join(map(str,q.unpack(x)))
        violations=[t for t in range(len(boundary)-1) if boundary[t] and boundary[t+1]!=1-((path[t]>>19)&1)]
        print('first_badB_SS_count',k,'P2_later_than_first',k>=2,
              'source20',fmt(path[0]),'macro_endpoints',[fmt(x) for x in macro],
              'boundary',''.join(map(str,boundary)),
              'boundary21_black_mask_violations',violations,
              'all_scalar_edges_PASS',flush=True)
        # P3 BEFORE exact counter lift: the retained bad-B20 packet
        # has an actual H111-SS^3 ancestor, despite this selected
        # boundary path's violations. Complete inverse cap200000
        # at each layer; a cap is UNKNOWN and stops this tree.
        # A found prefix is checked by an all-tail certificate and
        # four independent80-cell literal/packed histories.
        assert k==3
        exact={q.unpack(z)[5:]};layers=[]
        for t in range(len(track)-1,-1,-1):
            exact={x for y in exact for x in inverse(y,track[t])}
            if t in (10,16,22):exact={x for x in exact if q.pack(bits('11101')+x[:4]) in SS_TYPES}
            shields={0:bits('1111'),1:bits('1000'),4:bits('000'),5:bits('10')}
            if t in shields:exact={x for x in exact if x[:len(shields[t])]==shields[t]}
            layers.append(len(exact))
            if len(exact)>200000:
                print('P3_actual_counter_lift_UNKNOWN_cap','time',t,'layers',layers,flush=True);break
            if not exact:
                print('P3_named_terminal_no_exact_ancestor','time',t,'layers',layers,flush=True);break
        else:
            src=bits('11100')+min(exact);cert=certificate(src,len(track))
            assert cert[-1][:20]==q.unpack(z) and not guarded_B(cert[-1])
            assert tuple(x[4] for x in cert[:-1])==track
            for pattern in ((0,),(1,),(0,1),(1,0)):
                far=tuple(pattern[j%len(pattern)] for j in range(80-len(src)))
                full=run(src+far,len(track))
                assert full[-1][:20]==q.unpack(z)
                assert all(full[t][:len(y)]==y for t,y in enumerate(cert))
            print('P3_actual_H111_SS3_badB_source',''.join(map(str,src)),
                  'source_len',len(src),'layers',layers,'four_complete80cell_controls_PASS',flush=True)

    else:
        allout,_=flow(seen,SS)
        assert not any(bad_B(x) for x in allout)
        assert {x for x in allout if x&MASK9 in SS_TYPES}<=seen
        print('fixed_point_closure_and_all_B_guard_PASS',flush=True)
    for source in ('1110011110000000001101000000','1110011110000000000100000000'):
        full=run(bits(source)+(0,)*42,22)
        assert q.pack(full[10][:20]) in entrances
        for t in range(22):assert q.pack(full[t+1][:20]) in q.scalar_successors(q.pack(full[t][:20]),t)
    print('two_actual_GC1142_projection_controls_PASS',flush=True)

if __name__=='__main__':main()

# OUTCOME: P1 REFUTED in the existing width20 relaxation:599
# H111 black-S entrances reach badB first after3 SS (P2 HELD).
# 1306 SS states seen before the counter, including341 white ones.
# Explicit28-tick scalar path and selected boundary assignment
# retained; that assignment violates column21's black-mask equation
# at3,5,9,13,18. This does not rule out alternate boundary choices
# or actual lifts. P3 exact named-terminal inverse stopped UNKNOWN
# at time12:282752 nodes exceeded the registered200000 cap.
# No continuation or larger cap. Two independent complete actual
# GC1142 histories project into the relaxation. Final probe PASS.
# Close this generic finite-carrier guard; GC1142 first-SS theorem
# remains intact. Next use new CL335 pin13 evidence to test a
# narrower all-tail X-return admission guard, not widen this strip.
