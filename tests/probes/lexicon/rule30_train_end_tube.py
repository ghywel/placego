"""GC1195: finite diagonal difference tube, independent of seed span.

PREDICTIONS BEFORE controls, 2026-10-13: at k11/27/35/47 and R1/2/3,
the tube delta0..deltaR gives the literal clamped endpoint row at the
first arrival and its next R ticks. The packet and relative trace are
unchanged at k+28*2^R. Counterfactual: the period56 one-bit charge does
not lift to a finite triangular packet. Independent control: full
clamped Wolfram lookup at every pre-arrival tick, rather than computing
only the same tube formula. Unexpected: stop the tube at depth1 and
switch to the fixed wall; no free tube is used across the wall.
Also check one28-step abstract block on every R-bit state: a permutation
whose2^R power is identity. This is an algebraic packet check, not a
survival/period/profile census or completed-prefix closing-window run.
Record searched: diagonal.tube|defect.tube|moving.*difference|
difference.*moving withtriangular|permutation|finite|period ->13hits6files;
unitriangular|triangular.*permutation withdefect|diagonal|tube|period28|
2^ ->1 prior tree pointer. GC1167/1193/1194 and Local L679 read.
ADDENDUM BEFORE boundary check: at a white first arrival with x1=1,
x2=0 the four-tick trace must be(1,1,x3,1-x4). Check on the same
four named R3 packets; no new endpoint classes are added.
OUTCOME:12 named endpoint comparisons PASS, including k+M copies. The
28-step abstract block is a permutation and its2^R power is identity
for every tested state at R1/2/3. No closure verdict computed by GPT.
"""
from rule30_train_end_pivot import ROWS,S
from rule30_seed_tree_train_ray import finish
from rule30_seed_prefix_scope import edge,trace

TABLE=(0,1,1,1,1,0,0,0)


def A(t,j):return int(ROWS[t%4][(-j)%7])


def advance(d,t,ell):
    out=[]
    for s,v in enumerate(d):
        a,b=A(t,ell-t-1+s),A(t,ell-t-2+s)
        u=d[s-1] if s>=1 else 0
        w=d[s-2] if s>=2 else 0
        out.append(v ^ ((a^u)|(b^w)) ^ (a|b))
    return out


def child(k,W):
    seed=finish(''.join(str(S(j)) for j in range(k)))
    q=next(j for j in range(k,len(seed)+7)
           if (int(seed[j]) if j<len(seed) else 0)!=S(j))
    y=edge(seed)
    return q,[y[i+2] if i+2<len(y) else 0 for i in range(1,W+1)]


def endpoint(k,R):
    q,row=child(k,k+R+4);ell=q-2
    row=row[:ell+R]
    d=[row[ell+s-1]^A(0,ell+s) for s in range(R+1)]
    assert d[0]==1
    for t in range(ell-1):
        assert d==[row[ell-t+s-1]^A(t,ell-t+s) for s in range(R+1)]
        d=advance(d,t,ell)
        x=[t%2]+row
        row=[TABLE[4*x[j+1]+2*x[j]+x[j-1]] for j in range(1,len(x)-1)]
    packet=[A(ell-1,j)^d[j-1] for j in range(1,R+2)]
    assert row==packet
    # Wall phase at first arrival is (ell-1)%2, not a free tube value.
    rel=trace(packet,(ell-1)%2,True)
    assert rel==trace(packet,(ell-1)%2,False)
    return tuple(packet),tuple(rel)


def block(d,R):
    for t in range(28):d=advance(d,t,9)
    return d


def main():
    for R in (1,2,3):
        M=28*(1<<R)
        images=[]
        for z in range(1<<R):
            d=[1]+[(z>>j)&1 for j in range(R)]
            images.append(tuple(block(d,R)))
            e=d[:]
            for _ in range(1<<R):e=block(e,R)
            assert e==d
        assert len(set(images))==1<<R
        for k in (11,27,35,47):
            a=endpoint(k,R);assert a==endpoint(k+M,R)
            if R==3 and a[0][1]==0:
                assert a[0][0]==1
                assert a[1]==(1,1,a[0][2],1-a[0][3])
        print('R',R,'superperiod',M,'four named endpoint comparisons and block identity PASS')
    print('12 named tube comparisons PASS; clamped endpoint boundary retained; no closure census')


if __name__=='__main__':main()
