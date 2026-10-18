#!/usr/bin/env python3
"""B241 / MI461: first-negative test of strict two-token H2 matching escape.
Fixed counts233/234, all internal holes; 20s/50k states; no repair/retry.
Independent subset maps, neighbour generation, matching, physical reflection.
"""
from itertools import combinations
from collections import defaultdict
import json
import time

START = time.monotonic()
L = lambda r: r*(r-1)//2

def fibres(pool, size):
    primary=defaultdict(set)
    for b in combinations(pool,size): primary[sum(b)].add(b)
    other=defaultdict(set)
    for mask in range(1<<len(pool)):
        if mask.bit_count()==size:
            b=tuple(x for i,x in enumerate(pool) if mask>>i&1)
            other[sum(b)].add(b)
    assert dict(primary)==dict(other)
    return primary

def edges(pool,u):
    p=set(pool)
    a=tuple((x,y) for x,y in combinations(pool,2) if x+y==u)
    b=tuple((x,u-x) for x in pool if x<u-x and u-x in p)
    assert a==b
    return a

def touched(b,ee):
    b=set(b)
    return sum(bool(b.intersection(edge)) for edge in ee)

def neighbours(pool,b,fibre):
    bs=set(b); out=set()
    for rem in combinations(b,2):
        for add in combinations(tuple(x for x in pool if x not in bs),2):
            if sum(rem)==sum(add):
                c=tuple(sorted(bs-set(rem)|set(add)))
                assert len(c)==len(b) and sum(c)==sum(b)
                out.add(c)
    reference={c for c in fibre if len(bs.symmetric_difference(c))==4}
    assert out==reference
    return out

def check_state(pool,u,b,fibre):
    ee=edges(pool,u)
    nn=neighbours(pool,b,fibre)
    m=max(pool)
    rp=tuple(sorted(m-x for x in pool)); rb=tuple(sorted(m-x for x in b))
    rf={tuple(sorted(m-x for x in c)) for c in fibre}
    rn=neighbours(rp,rb,rf); re=edges(rp,2*m-u)
    assert rn=={tuple(sorted(m-x for x in c)) for c in nn}
    assert touched(b,ee)==touched(rb,re)
    assert all(touched(c,ee)==touched(tuple(sorted(m-x for x in c)),re) for c in nn)
    good=sorted(c for c in nn if touched(c,ee)<len(ee))
    return ee,nn,good

def protected(target,counts):
    for mask in range(1,7):
        r=sum(c for i,c in enumerate(counts) if mask>>i&1)
        if sum(t for i,t in enumerate(target) if mask>>i&1)<L(r)+r:return False
    return True

def main():
    pool=tuple(x for x in range(9) if x!=3); ff=fibres(pool,3)
    ee,nn,good=check_state(pool,8,(0,1,6),ff[7])
    assert touched((0,1,6),ee)==len(ee) and (0,2,5) in good
    pool=(0,1,2,3,4,6); ff=fibres(pool,2)
    ee,nn,good=check_state(pool,2,(0,6),ff[6])
    assert touched((0,6),ee)==len(ee) and not good
    assert not protected((2,6,8),(2,2,2))
    print(json.dumps({'controls':'positive, negative, whole fibre maps, neighbour maps, matching and physical reflection PASS'}),flush=True)
    seen=bad=0
    for counts in ((2,3,3),(2,3,4)):
        m=sum(counts)
        for q in range(1,m):
            pool=tuple(x for x in range(m+1) if x!=q); total=sum(pool)
            ff=fibres(pool,counts[1])
            for u in range(3,2*m-q):
                ee=edges(pool,u)
                for v in sorted(ff):
                    target=(u,v,total-u-v)
                    if not protected(target,counts):continue
                    for b in sorted(ff[v]):
                        seen+=1
                        assert seen<=50000 and time.monotonic()-START<20,'cap'
                        if touched(b,ee)!=len(ee):continue
                        bad+=1
                        ee,nn,good=check_state(pool,u,b,ff[v])
                        if not good:
                            print(json.dumps({'result':'FIRST NEGATIVE','counts':counts,'q':q,'M':m,'target':target,'B':b,'pairs':ee,'neighbours':sorted(nn),'fibre':sorted(ff[v]),'fibre_good':sorted(c for c in ff[v] if touched(c,ee)<len(ee)),'states_seen':seen,'blocking_seen':bad,'seconds':time.monotonic()-START}),flush=True)
                            return
    print(json.dumps({'result':'FIXED DOMAIN PASS','states_seen':seen,'blocking_seen':bad,'seconds':time.monotonic()-START}),flush=True)

if __name__=='__main__':main()
