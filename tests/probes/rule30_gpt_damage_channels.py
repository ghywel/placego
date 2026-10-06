"""G114 DP0-DP2 preregistered NOT RUN;publish before execution.
DP0:64 local triples obey expanded XOR error equation versus literal table.
DP1:known13-bit pulse word yields declared shrinking rows at ticks3..5,
with incoming errors(1,1) then(1,0), and source error return at tick6.
DP2 unexpected:shared black centre blocks right damage; Rule90 predicts1.
REFUTED-BY:DP2 autonomous-Rule90 damage counterfactual.
OUTCOME 2026-10-06 21:16 BST after9e09890:DP0-DP2 PASS.
64 identities;incoming(1,1) cancels,(1,0) returns;black-centre guard passes.
"""
from itertools import product


def truth(a,b,c):
    return (30>>(4*a+2*b+c))&1


def damage(b,c,p,q,r):
    return p^((1-c)*q)^((1-b)*r)^(q*r)


def main():
    for a,b,c,p,q,r in product((0,1),repeat=6):
        actual=truth(a,b,c)^truth(a^p,b^q,c^r)
        assert actual==damage(b,c,p,q,r)
        if q==0:
            assert actual==(p^((1-b)*r))
    print('DP0 PASS:64 exact local damage identities')
    word=tuple(map(int,'0011110010000'))
    a=dict(zip(range(-6,7),word));b=dict(a)
    expected={3:('1010101','1111011'),4:('01010','00001'),5:('101','001')}
    for t in range(1,7):
        aa={i:truth(a[i-1],a[i],a[i+1]) for i in range(min(a)+1,max(a))}
        bb={i:truth(b[i-1],b[i],b[i+1]) for i in aa}
        if t==1:
            bb[0]=truth(b[-1],b[0],bb[1])
        else:
            for i in aa:
                p,q,r=(a[j]^b[j] for j in (i-1,i,i+1))
                assert (aa[i]^bb[i])==damage(a[i],a[i+1],p,q,r)
        a,b=aa,bb
        if t in expected:
            assert (''.join(map(str,a.values())),''.join(map(str,b.values())))==expected[t]
        if t in (4,5):
            assert a[0]==b[0]==0
            incoming=(a[-1]^b[-1],a[1]^b[1])
            assert incoming==((1,1) if t==4 else (1,0))
            print(f'DP1 tick{t}:white source, incoming{incoming}, predicted next error{incoming[0]^incoming[1]}')
        if t==6:
            assert a[0]^b[0]==1
    print('DP1 PASS:hand-derived cone rows and cancellation/return mechanism')
    assert damage(1,0,0,0,1)==0 and (0^1)==1
    print('DP2 PASS:autonomous-Rule90 damage counterfactual refuted')


if __name__=='__main__':
    main()
