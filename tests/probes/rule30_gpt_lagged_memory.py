"""G113 LM1-LM3 preregistered NOT RUN; publish before execution.
Model: infinite fair initial row, isolated source right pulse on tick1,
all other reads synchronous; source to tick6 depends on13 initial bits.
LM1 must:8192 histories; pulse E1=001,E2=0,E3=E1; independent XOR/OR.
LM2 blind: K4,K5 fail to determine next-error law without earlier K3.
Compare exact child/parent cross products, keep a held result if none.
LM3 unexpected must:both seven-sample marginal histograms uniform,
128 words64 times each, even if paired two-step closure fails.
Counterfactual: healing at tick2 prevents next-source error. REFUTED-BY:LM1.
No repeated-race ring, production spectrum or Local job duplicated.
"""
from collections import Counter,defaultdict
from itertools import product
from fractions import Fraction


def truth(l,c,r):
    return (30 >> (4*l+2*c+r)) & 1


def traces(word):
    a=dict(zip(range(-6,7),word));b=dict(a)
    ii,jj=[a[0]],[b[0]]
    for t in range(1,7):
        aa={i:truth(a[i-1],a[i],a[i+1]) for i in range(min(a)+1,max(a))}
        bb={i:truth(b[i-1],b[i],b[i+1]) for i in aa}
        if t==1:
            bb[0]=truth(b[-1],b[0],bb[1])
        for i in aa:
            assert aa[i]==(a[i-1]^(a[i]|a[i+1]))
            right=bb[1] if t==1 and i==0 else b[i+1]
            assert bb[i]==(b[i-1]^(b[i]|right))
        a,b=aa,bb;ii.append(a[0]);jj.append(b[0])
    return tuple(ii),tuple(jj)


def main():
    parent=defaultdict(Counter);child=defaultdict(Counter)
    ih,jh=Counter(),Counter()
    for word in product((0,1),repeat=13):
        i,j=traces(word);e=tuple(x^y for x,y in zip(i,j))
        inject=int(word[6:9]==(0,0,1))
        assert e[1:4]==(inject,0,inject)
        k=tuple(zip(i,e));p=k[4:6];c=(k[3],)+p
        parent[p][e[6]]+=1;child[c][e[6]]+=1
        ih[i]+=1;jh[j]+=1
    assert sum(ih.values())==8192
    print('LM1 PASS:8192 histories; independent updates and source echo')
    splits=[]
    for c,h in sorted(child.items()):
        a=parent[c[1:]];nc,na=sum(h.values()),sum(a.values())
        determinant=h[1]*na-a[1]*nc
        if determinant:
            splits.append((c,h[1],nc,a[1],na))
    print('LM2 '+('HELD split prediction; two-step closure refuted' if splits else 'REFUTED split prediction; finite table held')+
          f':{len(splits)} unequal child-parent refinements;'+
          f'{len(parent)} parents,{len(child)} children')
    for c,sc,nc,sa,na in splits[:3]:
        print(f'witness K3,K4,K5={c}:next-error {sc}/{nc} versus {sa}/{na}; '+
              f'difference {Fraction(sc,nc)-Fraction(sa,na)}')
    assert len(ih)==len(jh)==128
    assert set(ih.values())==set(jh.values())=={64}
    print('LM3 PASS:both seven-sample marginals128 words64 times each')


if __name__=='__main__':
    main()
