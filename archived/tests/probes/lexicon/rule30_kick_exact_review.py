"""GC379 entry27 semantic guards, no SAT solver or DRAT rerun.
Preregistered: phase inverse, selector restriction, scalar gate CNF, duration cut.
"""
import itertools,json
import rule30_kick_alphabet_exact as kx


def satisfied(cs,values):
    return all(any(values[abs(l)] if l>0 else not values[abs(l)] for l in c) for c in cs)


def main():
    count=0
    # Independently enumerate KK's OR and XOR gate clauses against literal rule.
    cs=[[-4,2,3],[4,-2],[4,-3],[-5,1,4],[-5,-1,-4],[5,-1,4],[5,1,-4]]
    for a,b,c in itertools.product((0,1),repeat=3):
        accepted=[]
        for o,y in itertools.product((0,1),repeat=2):
            if satisfied(cs,{1:a,2:b,3:c,4:o,5:y}):accepted.append((o,y))
        assert accepted==[(b|c,a^(b|c))];count+=1
    phases=0
    for d in range(0,56,2):
        for k in range(-14,14):
            dn=(d-10*k)%56  # inverse of17 modulo28 is5
            assert kx.kick_of(dn-d)==k
            assert sum(kx.kick_of(q-d)==k for q in range(0,56,2))==1
            phases+=1
    # Eligibility failure is not a checked DRAT refutation.
    assert kx.U[52]==kx.U[6]==1
    assert all(kx.instance_sized(t,d,52,1) is None for t in (0,1) for d in range(0,56,2))
    cases=[]
    for a,k in ((32,2),(42,5),(52,-6),(32,7),(52,1)):
        # Exactly140 event occurs at t0=0, old phase(140-a) modulo56.
        d=(140-a)%56
        inst=kx.instance_sized(0,d,a,k)
        if inst is not None:
            nv,cs,row,s,E,keep=inst
            assert s==140 and E-s+1==21
            assert keep==[(d-10*k)%56]
            assert len(cs[-1])==1
        cases.append(dict(a=a,k=k,eligible=inst is not None))
    # Unexpected rounding guard; direct N140 does not always mean length140.
    _,_,_,s,E=kx.kk.instance(0,0,32,140)
    assert s==144
    tau=s-140;assert tau%2==0
    d2=(-tau)%56;dn2=(6-tau)%56
    assert kx.kick_of(dn2-d2)==kx.kick_of(6)
    print(json.dumps(dict(gate_triples=count,phase_kick_pairs=phases,
                         exact140_selector_cases=cases,rounded_case_length=s,
                         normalized_length=s-tau),indent=2))

if __name__=='__main__':main()
