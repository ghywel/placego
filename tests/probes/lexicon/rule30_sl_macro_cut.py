"""Exact cut translation for recurrent S/L words, with a startup scope guard.
None means no occurrence in an S/L bi-infinite word; '' forbids every such word.
"""
from itertools import product

def macro_cut(f):
    assert f and set(f)<=set('01')
    ones=[i for i,b in enumerate(f) if b=='1']
    if not ones:
        return '' if len(f)<=2 else ('L' if len(f)<=4 else None)
    a,b=ones[0],len(f)-1-ones[-1]
    gaps=[j-i for i,j in zip(ones,ones[1:])]
    if max(a,b)>4 or any(d not in (3,5) for d in gaps):return None
    return ('L' if a>=3 else '')+''.join('S' if d==3 else 'L' for d in gaps)+('L' if b>=3 else '')

def cyclic_has(period,f):
    if not f:return True
    s=period*((len(f)+2*len(period)-1)//len(period))
    return any(s[i:i+len(f)]==f for i in range(len(period)))

if __name__=='__main__':
    periods=[''.join(w) for n in range(1,7) for w in product('SL',repeat=n)]
    spell=lambda w:''.join('100' if c=='S' else '10000' for c in w)
    factors={'11','00000','1001','10001','001001','0001000'}
    for w in periods:
        p=spell(w);s=p*((16+2*len(p)-1)//len(p))
        factors.update(s[i:i+n] for i in range(len(p)) for n in range(1,17))
    checks=0
    for f in factors:
        g=macro_cut(f)
        for w in periods:
            assert cyclic_has(spell(w),f)==(g is not None and cyclic_has(w,g)),(f,g,w)
            checks+=1
    assert macro_cut('001001')=='S'
    assert '001001' not in '1001' # Startup: missing preceding gap.
    assert '001001' in '1001001'
    assert macro_cut('0001000')=='LL'
    assert macro_cut('0010001000100010100001010100010000101000010101') is None
    f1='010010010000100001001001000010000100001001'
    f2='001001000010000100001000010010000100001001'
    u,v=f1[1:],f2[2:]
    assert len(f1)==len(f2)==42
    assert macro_cut(f1)=='SSLLSSLLLS'
    assert macro_cut(f2)=='SLLLLSLLS'
    # Logical consequences of Local's absence certificates, not CA membership tests.
    assert not [b for b in '01' if '11' not in b+u and f1 not in b+u]
    assert [''.join(b) for b in product('01',repeat=2)
            if '11' not in ''.join(b)+v and f2 not in ''.join(b)+v]==['10']
    print(checks,'independent cyclic spelling comparisons PASS')
    print('Startup, long-gap and non-S/L f46 controls PASS')
