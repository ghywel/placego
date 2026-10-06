"""G118 JI0-JI2 preregistered NOT RUN;publish before execution.
2048 words,both six-sample marginals64 traces32 each.
Joint112 pairs,count histogram32:32,24:32,8:16,5:16,3:16.
Hjoint=6+h2(1/4)/2+h2(3/8)/16;MI=12-Hjoint.
Unexpected:injection depends on initial observed bit,not independent.
REFUTED-BY:JI2 unconditional injection entropy substitution.
Independent literal-table/XOR-OR;no production or entropy-rate claim.
"""
from collections import Counter,defaultdict
from itertools import product
from math import log2


def h(p):
    return -p*log2(p)-(1-p)*log2(1-p) if 0<p<1 else 0.0


def entropy(counts):
    n=sum(counts.values())
    return -sum((c/n)*log2(c/n) for c in counts.values() if c)


def main():
    ideal,noisy,joint=Counter(),Counter(),Counter();flag=defaultdict(Counter)
    def truth(l,c,r):
        return (30>>(4*l+2*c+r))&1
    for word in product((0,1),repeat=11):
        a=dict(zip(range(-5,6),word));b=dict(a)
        ii,jj=[a[0]],[b[0]]
        for t in range(1,6):
            aa={i:truth(a[i-1],a[i],a[i+1]) for i in range(min(a)+1,max(a))}
            bb={i:truth(b[i-1],b[i],b[i+1]) for i in aa}
            if t==1:
                bb[0]=truth(b[-1],b[0],bb[1])
            for i in aa:
                r=bb[1] if t==1 and i==0 else b[i+1]
                assert aa[i]==(a[i-1]^(a[i]|a[i+1]))
                assert bb[i]==(b[i-1]^(b[i]|r))
            a,b=aa,bb;ii.append(a[0]);jj.append(b[0])
        i,j=tuple(ii),tuple(jj);F=i[1]^j[1]
        ideal[i]+=1;noisy[j]+=1;joint[i,j]+=1;flag[i][F]+=1
    assert len(ideal)==len(noisy)==64 and set(ideal.values())==set(noisy.values())=={32}
    assert len(joint)==112 and Counter(joint.values())==Counter({32:32,24:32,8:16,5:16,3:16})
    print('JI0 PASS:2048 words;uniform marginal traces;112 predicted joint pairs')
    H=entropy(joint);pred=6+h(1/4)/2+h(3/8)/16
    mi=entropy(ideal)+entropy(noisy)-H
    assert abs(H-pred)<1e-12 and abs(mi-(6-h(1/4)/2-h(3/8)/16))<1e-12
    print(f'JI1 PASS:Hjoint={H:.12f},MI={mi:.12f} bits')
    for i,c in flag.items():
        assert c==(Counter({0:24,1:8}) if i[0]==0 else Counter({0:32}))
    conditional=sum((sum(c.values())/2048)*entropy(c) for c in flag.values())
    assert abs(conditional-h(1/4)/2)<1e-12
    assert 6+h(1/8)+h(3/8)/16>H+0.1
    print('JI2 PASS:conditional injection entropy;independence counterfactual refuted')


if __name__=='__main__':
    main()
