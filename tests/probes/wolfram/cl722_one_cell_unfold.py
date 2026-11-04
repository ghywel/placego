"""Identify the first update where a one-wheel spacing change reveals the half-cycle bit."""
import hashlib
import json
import os
from pathlib import Path

M=87866
MASK=(1<<(M+1))-1
OUT=Path(os.environ['CAPPED_OUT'])


def evolve(x):
    return ((x<<2) ^ (x | (x<<1))) & MASK


def edge(x,y):
    d=x^y
    return (d&-d).bit_length()-1 if d else M+1


def main():
    raw=Path(os.environ['WHITE_SEED_CYCLE']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='28d6dc60a6157dc39a5d2c9e41bdee6bce00ab562d05ed821ea1c1a724cbae71'
    size=(87867+8)//8
    w=[int.from_bytes(raw[r*size:(r+1)*size],'little') for r in (0,8)]
    results=[]
    for j in (39088,39089):
        c=(j-1)//2; a=1
        for _ in range(c):a=evolve(a)
        v=a | ((w[0]<<j)&MASK);y=a | ((w[1]<<j)&MASK)
        release=None;prior=None;first=None;hits=[None,None];min_before=None
        for t in range(c,84034):
            e,f,g=edge(a,v),edge(a,y),edge(v,y)
            if e>M and hits[0] is None:hits[0]=t
            if f>M and hits[1] is None:hits[1]=t
            if t==c:assert g==j+400 and e==f==j
            if release is None and g>j+400:release=[t,e,f,g]
            if g<=M and first is None:
                if e==f:
                    delta=g-e
                    assert delta>0
                    if min_before is None or delta<min_before[0]:min_before=[delta,t,e,g]
                else:
                    u,a0,v0,y0,e0,f0,g0=prior
                    assert e0==f0 and g0>e0 and g==min(e,f)
                    lo=e0-2;hi=max(e,f,g,g0)
                    ensure=(1<<(hi-lo+1))-1
                    tri=[(x>>lo)&ensure for x in (a0,v0,y0)]
                    for old,cur in zip(tri,(a,v,y)):
                        assert ((evolve(old)>>2)&((1<<(hi-lo-1))-1))==(cur>>(lo+2))&((1<<(hi-lo-1))-1)
                    first=dict(t=t,old=[e0,f0,g0],new=[e,f,g],lo=lo,hi=hi,low_to_high=[
                        format(x,f'0{hi-lo+1}b')[::-1] for x in tri])
            if all(h is not None for h in hits):break
            prior=t,a,v,y,e,f,g
            a,v,y=evolve(a),evolve(v),evolve(y)
        results.append(dict(j=j,cut=c,hits=hits,release=release,first=first,min_before=min_before))
    assert results[0]['hits']==[83769,83769] and results[0]['first'] is None
    assert results[1]['hits']==[84033,83472] and results[1]['first'] is not None
    (OUT/'unfold.json').write_text(json.dumps(results,indent=2)+'\n')
    print('ONE_CELL_UNFOLD_DONE',results)


if __name__=='__main__':main()
