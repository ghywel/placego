"""G115 IS0-IS2 preregistered NOT RUN;publish before execution.
Same infinite fair isolated-pulse ensemble as G113;8192 initial cone words.
Candidate X5=(F,K4,K5), F=actual injection E1; pulse age fixed and known.
IS0 must:all bins total8192, F=E3=001; unaugmented witness0/896 vs40/1872.
IS1 blind:at least one full-prefix refinement of X5 splits E6 probabilities.
IS2 unexpected blind:K3-only refinement of X5 may hold despite IS1 failure.
Compare integer cross products;retain held/refuted outcomes honestly.
Independent update formulations inherited from traces();no production job.
Counterfactual:omitting F still closes one-lag state. REFUTED-BY:IS0.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import product
from rule30_gpt_lagged_memory import traces


def splits(children,parents,parent_key):
    out=[]
    for c,h in sorted(children.items()):
        p=parent_key(c);a=parents[p]
        nc,na=sum(h.values()),sum(a.values())
        if h[1]*na!=a[1]*nc:
            out.append((c,p,h[1],nc,a[1],na))
    return out


def main():
    parents=defaultdict(Counter);full=defaultdict(Counter);shallow=defaultdict(Counter)
    raw=Counter();zero=Counter();examples={}
    for word in product((0,1),repeat=13):
        i,j=traces(word);k=tuple((x,x^y) for x,y in zip(i,j))
        f=k[1][1];s=k[6][1]
        assert f==k[3][1]==int(word[6:9]==(0,0,1))
        p=(f,k[4],k[5]);c=k[:6]
        parents[p][s]+=1;full[c][s]+=1;shallow[(k[3],p)][s]+=1
        examples.setdefault((c,s),word)
        if k[4:6]==((0,0),(0,0)):
            raw[s]+=1
            if k[3]==(0,0):
                zero[s]+=1
    assert raw==Counter({0:1832,1:40}) and zero==Counter({0:896})
    assert sum(map(lambda h:sum(h.values()),parents.values()))==8192
    assert sum(map(lambda h:sum(h.values()),full.values()))==8192
    print('IS0 PASS:8192 words, injection identity and unaugmented witness')
    deep=splits(full,parents,lambda c:(c[1][1],c[4],c[5]))
    near=splits(shallow,parents,lambda c:c[1])
    print(f'IS1 '+('HELD split prediction' if deep else 'REFUTED split prediction; finite table held')+
          f':{len(deep)} unequal full-prefix refinements;{len(parents)} parents,{len(full)} histories')
    for c,p,sc,nc,sa,na in deep[:2]:
        print(f'parent F,K4,K5={p}; history={c}; next-error {sc}/{nc} vs {sa}/{na}; difference {Fraction(sc,nc)-Fraction(sa,na)}')
        for s in (0,1):
            if (c,s) in examples:
                print(f'initial[-6..6]={"".join(map(str,examples[c,s]))}; E6={s}')
    print('IS2 '+('HELD shallow-equality prediction' if not near else 'REFUTED shallow-equality prediction')+
          f':{len(near)} unequal K3-only refinements')


if __name__=='__main__':
    main()
