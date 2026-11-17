"""G127 NS0/NS2 PASS; NS1 HELD at n=6 after81fb4fd publication.
Search n=1..7 for a periodic target in Y with no locally-Y precursor block.
Blind prediction held:022000 has six precursors,all containing100.
Independent triple decode and de Bruijn path counts verify the certificate.
Unexpected guard: period-doubling defeats the period-preserving section,
not existence of an image-constrained predecessor.
"""
from collections import Counter
from itertools import product

BAD=('100','101','112','0210','0211','0202')


def label(s):
    return next((w for w in BAD if w in s),None)


def cyclic(s):
    return label((s*4)[:len(s)+3]) is None


def literal(a,b,c):
    if a==1:
        return 2
    if a==2:
        return int(c==2) if b==2 else 2
    if b==0:
        return 0
    if b==1:
        return 1
    return 1-int(c==2)


def decoded(a,b,c):
    A=int(a==2); B=int(b==2); C=int(c==2)
    u=a if a!=2 else 1-B
    v=b if b!=2 else 1-C
    d=v^(u|A)
    return 2 if u else d


def image(s):
    return ''.join(str(literal(*map(int,s[i:i+3]))) for i in range(len(s)-2))


def circ_image(s):
    return image(s+(s*2)[:2])


def path_count(w):
    states=Counter({(a,b):1 for a,b in product(range(3),repeat=2)})
    for d in map(int,w):
        nxt=Counter()
        for (a,b),v in states.items():
            for c in range(3):
                if decoded(a,b,c)==d:
                    nxt[b,c]+=v
        states=nxt
    return sum(states.values())


def main():
    for a,b,c in product(range(3),repeat=3):
        assert literal(a,b,c)==decoded(a,b,c)
    print('NS0 PASS:27 triple cases;literal and binary decoding agree')
    y2={''.join(map(str,w)) for w in product(range(3),repeat=2) if cyclic(''.join(map(str,w)))}
    assert y2=={'00','11','12','21','22'}
    assert {circ_image(s) for s in y2}=={'00','11','22'}
    assert cyclic('0102') and circ_image('0102')=='1212'
    assert not cyclic('01') and circ_image('01')=='12'
    print('NS2 PASS:period2 target12 has period4 predecessor0102 in Y;no period2 predecessor in Y')
    for n in range(1,8):
        precursors={}
        valid=set()
        for word in product(range(3),repeat=n+2):
            s=''.join(map(str,word));t=image(s)
            precursors.setdefault(t,[]).append(s)
            if label(s) is None:
                valid.add(t)
        targets={''.join(map(str,w)) for w in product(range(3),repeat=n) if cyclic(''.join(map(str,w)))}
        assert targets <= precursors.keys(), 'G126 image criterion failed in a periodic target prefix'
        witness=next((s for s in sorted(targets) if s not in valid),None)
        print(f'NS1 n={n}:full inputs={3**(n+2)},locally-Y output prefixes={len(valid)}')
        if witness is not None:
            words=precursors[witness]
            assert len(words)==path_count(witness)
            forbidden=Counter(label(s) for s in words)
            assert None not in forbidden
            print(f'NS1 HELD:witness={witness},periodic target in Y;all {len(words)} full-shift precursor blocks excluded')
            print('Independent path count='+str(path_count(witness))+';exclusion spectrum='+str(dict(sorted(forbidden.items()))))
            return
    print('NS1 REFUTED:blind witness-by7 prediction;no missing periodic target prefix through n=7. No stabilization theorem.')


if __name__=='__main__':
    main()
