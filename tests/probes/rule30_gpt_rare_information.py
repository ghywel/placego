"""G120 RB0-RB2 preregistered NOT RUN;publish before execution.
Positive64 fair histories,F=(1-X0)*(1-U)*V,observed in first error.
Last error=F*Q;conditional entropy1/8,MI increment7/8.
Negative32 histories hide F;entropy h2(1/8)/2>1/8,increment<7/8.
Unexpected observability guard;REFUTED-BY:RB2 rare-event-probability-only budget.
Independent count entropy spectra;no information-rate existence claim.
"""
from collections import Counter,defaultdict
from itertools import product
from math import log2


def entropy(c):
    n=sum(c.values())
    return -sum((v/n)*log2(v/n) for v in c.values() if v)


def conditional(rows):
    groups=defaultdict(Counter)
    for past,value in rows:
        groups[past][value]+=1
    return sum(sum(c.values())/len(rows)*entropy(c) for c in groups.values())


def mi(pairs,n):
    a=Counter(i[:n] for i,j in pairs);b=Counter(j[:n] for i,j in pairs)
    assert len(a)==len(b)==2**n and set(a.values())==set(b.values())=={len(pairs)//2**n}
    joint=Counter((i[:n],j[:n]) for i,j in pairs)
    return entropy(a)+entropy(b)-entropy(joint)


def main():
    pairs=[];flags=[]
    for x0,x1,x2,u,v,q in product((0,1),repeat=6):
        f=(1-x0)*(1-u)*v
        pairs.append(((x0,x1,x2),(x0,x1^f,x2^(f*q))));flags.append(f)
    assert sum(flags)==8
    revealed=conditional([((i[:2],j[:2]),f) for (i,j),f in zip(pairs,flags)])
    assert abs(revealed)<1e-12
    e=conditional([((i[:2],j[:2]),i[2]^j[2]) for i,j in pairs])
    delta=mi(pairs,3)-mi(pairs,2)
    assert abs(e-1/8)<1e-12 and abs(delta-7/8)<1e-12
    print('RB0-RB1 PASS:64 histories;F revealed,p1/8;error entropy1/8,MI increment7/8')
    pairs=[];flags=[]
    for x0,x1,u,v,q in product((0,1),repeat=5):
        f=(1-x0)*(1-u)*v
        pairs.append(((x0,x1),(x0,x1^(f*q))));flags.append(f)
    assert sum(flags)==4
    hidden=conditional([((i[:1],j[:1]),f) for (i,j),f in zip(pairs,flags)])
    assert hidden>0
    e=conditional([((i[:1],j[:1]),i[1]^j[1]) for i,j in pairs])
    expected=entropy(Counter({0:7,1:1}))/2
    delta=mi(pairs,2)-mi(pairs,1)
    assert abs(e-expected)<1e-12 and e>1/8
    assert abs(delta-(1-e))<1e-12 and delta<7/8
    print(f'RB2 PASS:hidden F,error entropy{e:.12f},MI increment{delta:.12f};scope counterfactual refuted')


if __name__=='__main__':
    main()
