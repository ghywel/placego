"""GC485 fixed late-interval audit, not an onset/horizon search.
P1 BLIND: radius1/phase2 remains inconsistent after each burn16,64,128.
C0 MUST: literal-set and integer Rule30 agree at all257 rows.
C1 MUST: a fitted potential satisfies every retained equation; zero rewards feasible.
CF: shorter consistent data prove an eventual infinite identity; reject that inference
    using an explicit synthetic graph with a later conflicting edge.
Unexpected: track loss of constraints when enlarging windows or dropping early times;
           finite feasibility is recorded as undecided, never as a balance proof.
Fixed scope: radius0..3, phase2/4/8, end256, burns16/64/128; no adaptive reruns.
REFUTED-BY: control mismatch or radius1/phase2 feasible on a declared late interval.
"""
from rule30_gpt_selected_potential import consistent,decimal_set_step
if __name__=='__main__':
    assert consistent([(0,1,0,0)])[0]
    assert not consistent([(0,1,0,0),(0,1,1,2)])[0]
    T=256;off=T+5;mask=(1<<(2*off+1))-1;row=1<<off;a={0};rows=[]
    for t in range(T+1):
        assert {i-off for i in range(2*off+1) if (row>>i)&1}==a
        rows.append(row)
        if t<T:row=((row<<1)^(row|(row>>1)))&mask;a=decimal_set_step(a)
    for burn in (16,64,128):
        for r in range(4):
            for phase in (2,4,8):
                def state(t):return ((rows[t]>>(off-r))&((1<<(2*r+1))-1),t%phase)
                edges=[]
                for t in range(burn,T,2):
                    c=(rows[t]>>off)&1;cn=(rows[t+1]>>off)&1;g=(1-2*c)*int(c==cn)
                    edges.append((state(t),state(t+2),g,t))
                ok,w=consistent(edges)
                assert consistent([(u,v,0,t) for u,v,g,t in edges])[0]
                if r==1 and phase==2:assert not ok
                print('burn',burn,'r',r,'phase',phase,'feasible',ok,'witness',w)
    print('PASS:257 independent rows,36 zero-reward controls; fixed late radius1 prediction HELD')
