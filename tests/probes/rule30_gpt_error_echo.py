"""G109 EH1-EH2 predictions published throughf9aa008 before execution.
PASS:32 background kernels and128 initial words;16 injections, all source101.
32 single-flip backgrounds; 128 isolated right-race initial words.
Single-flip source1,1-z1,z1 OR z2; injected source signature101.
Independent XOR damage equation; no repeated-race or survival model.
"""
from collections import Counter
from itertools import product


def truth(l,c,r):
    return (30 >> (4*l+2*c+r)) & 1


def sync(row):
    return {i:truth(row[i-1],row[i],row[i+1])
            for i in range(min(row)+1,max(row))}


def paired_step(a,b):
    aa,bb=sync(a),sync(b)
    for i in aa:
        e={j:a[j]^b[j] for j in (i-1,i,i+1)}
        delta=e[i-1]^((a[i]|a[i+1])^((a[i]^e[i])|(a[i+1]^e[i+1])))
        assert delta==aa[i]^bb[i]
    return aa,bb


def main():
    for word in product((0,1),repeat=5):
        a=dict(zip(range(-2,3),word))
        b=dict(a)
        b[0]^=1
        predicted=(1,1-a[1],a[1]|a[2])
        seen=[a[0]^b[0]]
        for _ in range(2):
            a,b=paired_step(a,b)
            seen.append(a[0]^b[0])
        assert tuple(seen)==predicted
    signatures=Counter()
    masks=Counter()
    injections=0
    for word in product((0,1),repeat=7):
        old=dict(zip(range(-3,4),word))
        a=sync(old)
        b=dict(a)
        b[0]=truth(old[-1],old[0],a[1])
        injected=(1-old[0])*(1-old[1])*old[2]
        assert {i for i in a if a[i]^b[i]}==({0} if injected else set())
        signature=[a[0]^b[0]]
        a,b=paired_step(a,b)
        signature.append(a[0]^b[0])
        mask=tuple(i for i in a if a[i]^b[i])
        if injected:
            assert mask==((-1,1) if old[-2]==old[-1] else (1,))
            masks[mask]+=1
            injections+=1
        a,b=paired_step(a,b)
        signature.append(a[0]^b[0])
        assert tuple(signature)==((1,0,1) if injected else (0,0,0))
        signatures[tuple(signature)]+=1
    assert injections==16 and signatures=={(1,0,1):16,(0,0,0):112}
    assert masks=={(1,):8,(-1,1):8}
    print('EH1 PASS:32 arbitrary-background single-flip kernels')
    print('EH2 PASS:128 initial words;16 injections; all source signatures101')
    print('Second-tick damage masks:',dict(masks),'independent damage-equation controls PASS')


if __name__=='__main__':
    main()
