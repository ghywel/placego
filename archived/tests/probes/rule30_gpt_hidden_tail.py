"""G117 FT0-FT2 preregistered NOT RUN;publish before execution.
2048 initial words,tick5 isolated-pulse model.256 injections,152 fifth errors.
Exact latent bit D=x3 AND(x4 OR x5);compare hand kernel vs literal updates.
Injected prefix16 cases16 each,D1 six,D0 ten;error-count histogram0:2,16:6,6:6,10:2.
Unexpected guard:identical complete observed history can have different E5
without new flags.REFUTED-BY:FT2 deterministic-next-error counterfactual.
Independent XOR/OR controls;no repeated-race job or entropy-rate claim.
OUTCOME 2026-10-06 21:30 BST after6c4792e:FT0-FT2 PASS.
2048 words,256 injections,152 fifth errors;16 exact conditional kernels.
Identical observed histories from00110001000 and00110001101 have different E5.
"""
from collections import Counter,defaultdict
from itertools import product


def truth(l,c,r):
    return (30>>(4*l+2*c+r))&1


def kernel(a,b,c,d,D):
    H=a^b^c
    L=1^((1-b)*(d^(c|(1^a^b))))
    R=b^D
    C=c^((1^a^b)|(1^a^D))
    return L^((1-C)*H)^((1-d)*R)^(H*R)


def main():
    counts=defaultdict(Counter);tails=defaultdict(Counter);witness={}
    injected=errors=0
    for word in product((0,1),repeat=11):
        old=dict(zip(range(-5,6),word));a=dict(old);b=dict(a)
        ii=[a[0]];ee=[0]
        for t in range(1,6):
            aa={i:truth(a[i-1],a[i],a[i+1]) for i in range(min(a)+1,max(a))}
            bb={i:truth(b[i-1],b[i],b[i+1]) for i in aa}
            if t==1:
                bb[0]=truth(b[-1],b[0],bb[1])
            for i in aa:
                right=bb[1] if t==1 and i==0 else b[i+1]
                assert aa[i]==(a[i-1]^(a[i]|a[i+1]))
                assert bb[i]==(b[i-1]^(b[i]|right))
            a,b=aa,bb;ii.append(a[0]);ee.append(a[0]^b[0])
        f=int((old[0],old[1],old[2])==(0,0,1))
        D=old[3]*(old[4]|old[5]);q=tuple(ii[1:5])
        assert ee[1:4]==[f,0,f]
        assert ee[4]==f*(ii[1]^ii[2]^ii[3])
        assert ee[5]==f*kernel(*q,D)
        injected+=f;errors+=ee[5]
        if f:
            counts[q][ee[5]]+=1;tails[q][D]+=1
            if q==(0,0,0,0):
                assert ee[5]==D
                witness.setdefault(D,(word,tuple(zip(ii[:5],ee[:5]))))
    assert (injected,errors)==(256,152)
    assert len(counts)==16 and all(sum(h.values())==16 for h in counts.values())
    assert all(h==Counter({0:10,1:6}) for h in tails.values())
    assert Counter(h[1] for h in counts.values())==Counter({0:2,16:6,6:6,10:2})
    assert set(witness)=={0,1} and witness[0][1]==witness[1][1]
    print('FT0 PASS:2048 words;echo and fourth parity;independent updates')
    print('FT1 PASS:256 injections,152 fifth errors;16 prefix kernels and tail independence')
    for D,(word,history) in sorted(witness.items()):
        print(f'FT2 D={D},initial[-5..5]={"".join(map(str,word))},history={history},E5={D}')
    print('FT2 PASS:identical observed past,different next error;no-fresh-noise guard')


if __name__=='__main__':
    main()
