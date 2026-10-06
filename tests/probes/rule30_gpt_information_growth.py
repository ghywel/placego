"""G119 GF0-GF2 preregistered NOT RUN;publish before execution.
Positive32 fair histories,shared fresh pivots,biased hidden R=U*V.
MI prefixes1,2-h2(1/4),3-h2(1/4);error entropies0,h2(1/4),0.
Negative8 fair triples:I=(X,Y,Z),J=(X,Z,Y),both iid,MI1,1,3.
Unexpected cross-copy reuse;REFUTED-BY:GF2 marginal-iid-only extension.
Independent joint/marginal and conditional-error entropy spectra;no rate claim.
OUTCOME 2026-10-06 21:40 BST after439744b:GF0-GF2 PASS.
32 shared-fresh histories obey identity;8 reused-bit histories refute extension.
"""
from collections import Counter,defaultdict
from itertools import product
from math import log2


def entropy(counts):
    n=sum(counts.values())
    return -sum((c/n)*log2(c/n) for c in counts.values() if c)


def audit(pairs):
    mi=[];errors=[]
    n=len(pairs)
    for t in range(3):
        ic,jc,joint=Counter(),Counter(),Counter();groups=defaultdict(Counter)
        for i,j in pairs:
            ic[i[:t+1]]+=1;jc[j[:t+1]]+=1;joint[i[:t+1],j[:t+1]]+=1
            groups[i[:t],j[:t]][i[t]^j[t]]+=1
        assert len(ic)==len(jc)==2**(t+1)
        assert set(ic.values())==set(jc.values())=={n//2**(t+1)}
        mi.append(entropy(ic)+entropy(jc)-entropy(joint))
        errors.append(sum((sum(h.values())/n)*entropy(h) for h in groups.values()))
    return mi,errors


def main():
    h=entropy(Counter({0:3,1:1}))
    pairs=[]
    for x0,x1,x2,u,v in product((0,1),repeat=5):
        r=u*v;pairs.append(((x0,x1,x2),(x0,x1^r,x2^(r*x0))))
    mi,e=audit(pairs)
    assert all(abs(a-b)<1e-12 for a,b in zip(mi,(1,2-h,3-h)))
    assert all(abs(a-b)<1e-12 for a,b in zip(e,(0,h,0)))
    previous=0
    for a,b in zip(mi,e):
        assert abs((a-previous)-(1-b))<1e-12;previous=a
    print('GF0-GF1 PASS:32 histories;uniform marginals,conditional-error increment identity')
    mi,e=audit([((x,y,z),(x,z,y)) for x,y,z in product((0,1),repeat=3)])
    assert all(abs(a-b)<1e-12 for a,b in zip(mi,(1,1,3)))
    assert abs(e[2])<1e-12 and abs((mi[2]-mi[1])-(1-e[2]))>0.9
    print('GF2 PASS:8 histories;MI increments end at2,error uncertainty0;scope counterfactual refuted')


if __name__=='__main__':
    main()
