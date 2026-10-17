#!/usr/bin/env python3
"""B114/MI250 prereg32a24c24: general-window rich-four six-gap diagnostic.

Eight fixed geometry calls, seven complete offset maps, eight root maps,
two complete canonical-trap maps under both parity roles. No E28 partitions.
Predict 2742+5004=7746 cases and 120 original candidates/zero witnesses.
3CPU sec/64MiB; no wider profile census or whole-cycle allocation solver.
The infinite statement remains SKETCH, conditional on MI246.
OUTCOME MI251:8 formulas/7 offset maps/8 root maps/7746 cases pass;
0.151986CPU sec,15978496RSS bytes. Artifact SHA256
42b1b0fcaeecf1f967b8f37b815910280791fed081e74b0688e20199b2df9b3a.
"""
from collections import Counter
from itertools import permutations, product
import json
import resource
import time

import path_forest_partial_padding as validation


def prefix(x,gaps):
    out=[x]
    for gap in gaps:out.append(out[-1]+gap)
    return out


def orders(gaps):
    return sorted(set(permutations(gaps)))


def endpoint_bad(b,D,E):
    S=sum(b);L=D+E;bad={-S,0,L-S,L}
    if D==E:bad.update((D,D-S))
    elif E-D==S:bad.add(D)
    return bad


def bounds(H,J,alpha):
    assert J>=H and 1<=alpha<=(H+J+1)//2
    if alpha<=H:return -alpha,alpha
    assert alpha<=J
    return alpha-1-2*H,alpha


def construct(h,b,D,E,p,q):
    b=tuple(b);S=sum(b);L=D+E;K=L+S;M=2*(h+1)
    assert h>=7 and len(b)==4 and b==tuple(sorted(b))
    assert 1<=min(b) and max(Counter(b).values())<=2
    assert max(b)<=D<=E and S<=L<=h
    assert min(p,q)>0 and p%2 and q%2 and p+q==2*K
    assert max(p,q)<=2*h-1 and not p==q==2*h-1
    H=h-L;J=h-S;alpha=(2*h+1-max(p,q))//2
    assert H+J>=2
    lo,hi=bounds(H,J,alpha);bad=endpoint_bad(b,D,E)
    good=set(range(lo,hi+1))-bad;reflected=False;first=0 if p>=q else 1
    if not good:
        assert D==E==S+1 and h==2*D and alpha==1
        assert sorted((p,q))==[2*D-1,4*D-1]
        A=[0,D];B=prefix(1,(D,)+b)
        preA=A;preB=B;c=1;z=None;tried=0;kind='thin_repair'
    else:
        z=min(good,key=lambda v:(abs(v),v))
        c=alpha if z%2==alpha%2 else alpha-1
        x=(c-z)//2;y=(c+z)//2
        assert 0<=x<=H and 0<=y<=J
        ao=next(o for o in orders((D,E)) if not set(prefix(x,o))&{y,y+S})
        preA=prefix(x,ao);preB=None;tried=0
        for bo in orders(b):
            tried+=1
            candidate=prefix(y,bo)
            if not set(preA)&set(candidate):preB=candidate;break
        assert preB is not None and tried<=24
        A=preA;B=preB;reflected=(c==alpha-1);kind='canonical'
        if reflected:
            A=[h-v for v in reversed(A)];B=[h-v for v in reversed(B)]
            first=1-first
    row=validation.validate(M,list(b)+[D,E],p,q,A,B,first,False)
    row.update(h=h,b=b,D=D,E=E,p=p,q=q,H=H,J=J,alpha=alpha,
               interval=[lo,hi],bad=sorted(bad),kind=kind,z=z,c=c,
               preA=preA,preB=preB,reflected=reflected,local_orders=tried)
    return row


def root_control(row):
    H,J,alpha=row['H'],row['J'],row['alpha']
    direct={y-x for x,y in product(range(H+1),range(J+1))
            if x+y in (alpha,alpha-1)}
    lo,hi=row['interval'];assert direct==set(range(lo,hi+1))
    for z in direct:
        c=alpha if z%2==alpha%2 else alpha-1
        x=(c-z)//2;y=(c+z)//2
        assert 0<=x<=H and 0<=y<=J and x+y==c and y-x==z
    return dict(h=row['h'],b=row['b'],D=row['D'],E=row['E'],
                p=row['p'],q=row['q'],offsets=sorted(direct))


def geometry(M,A,B):
    direct=not set(A)&set(B)
    xs,word=validation.physical(M,A,B)
    assert validation.literal(M,xs)==direct
    assert validation.instrument.literal_geometry(M,set(),xs)==direct
    return direct,word


def offset_control(h,b,D,E):
    S=sum(b);L=D+E;H=h-L;J=h-S;M=2*(h+1)
    ashapes=[prefix(0,o) for o in orders((D,E))]
    bshapes=[prefix(0,o) for o in orders(b)]
    diffs=[{a-v for a in A for v in B} for A,B in product(ashapes,bshapes)]
    independent=set.intersection(*diffs)&set(range(-H,J+1))
    predicted=endpoint_bad(b,D,E)&set(range(-H,J+1))
    assert independent==predicted
    observed=[];cases=0
    for z in range(-H,J+1):
        x=max(0,-z);y=x+z
        assert 0<=x<=H and 0<=y<=J
        any_valid=False
        for aa,bb in product(ashapes,bshapes):
            A=[x+v for v in aa];B=[y+v for v in bb]
            direct,word=geometry(M,A,B);cases+=1
            assert Counter(word)==Counter((word[0],word[len(B)],
                                            *(-2*v for v in tuple(b)+(D,E))))
            any_valid |= direct
        if not any_valid:observed.append(z)
    assert set(observed)==predicted
    return dict(h=h,b=b,D=D,E=E,bad=sorted(predicted),cases=cases)


def trap_control(row):
    h,b,D,E,p,q=(row[k] for k in ('h','b','D','E','p','q'))
    M=2*(h+1);wanted=Counter((p,q,*(-2*v for v in tuple(b)+(D,E))))
    roles=[]
    for ag,bg in (((D,E),b),(b,(D,E))):
        cases=candidates=valid=0
        for x,y in product(range(h-sum(ag)+1),range(h-sum(bg)+1)):
            for ao,bo in product(orders(ag),orders(bg)):
                A=prefix(x,ao);B=prefix(y,bo)
                direct,word=geometry(M,A,B);cases+=1
                if Counter(word)==wanted:
                    candidates+=1;valid+=direct
        assert candidates and not valid
        roles.append(dict(cases=cases,candidates=candidates,valid=valid))
    return dict(h=h,b=b,D=D,E=E,p=p,q=q,roles=roles)


def main():
    start=time.process_time()
    fixtures=[(8,(1,1,2,2),3,3,13,11),(8,(1,1,2,2),4,4,15,13),
              (12,(1,1,2,2),6,6,23,13),(14,(1,1,2,2),7,7,27,13),
              (16,(1,1,2,2),8,8,31,13),(12,(1,1,2,2),3,9,19,17),
              (200,(1,2,3,93),100,100,399,199),(14,(1,1,2,2),7,7,25,15)]
    rows=[construct(*f) for f in fixtures]
    assert len(rows)==8 and sum(r['kind']=='thin_repair' for r in rows)==2
    assert [i for i,r in enumerate(rows) if r['reflected']]==[0,5]
    assert all(r['bins'] is None for r in rows)
    roots=[root_control(r) for r in rows]
    profiles=list(dict.fromkeys(f[:4] for f in fixtures))
    maps=[offset_control(*f) for f in profiles]
    assert len(maps)==7 and sum(v['cases'] for v in maps)==2742
    traps=[trap_control(rows[i]) for i in (3,6)]
    assert [sum(v['cases'] for v in t['roles']) for t in traps]==[108,4896]
    assert [sum(v['candidates'] for v in t['roles']) for t in traps]==[24,96]
    assert all(v['valid']==0 for t in traps for v in t['roles'])
    assert sum(v['cases'] for v in maps)+sum(v['cases'] for t in traps for v in t['roles'])==7746
    first=rows[0];A=first['preA'];B=first['preB'];direct,word=geometry(18,A,B)
    assert direct and word[0]==15 and word[len(B)]==9
    assert Counter(word)!=Counter((13,11,*(-2*v for v in (1,1,2,2,3,3))))
    assert rows[-1]['kind']=='canonical' and rows[-1]['alpha']==2 and rows[-1]['z']==2
    assert rows[-1]['A']==[0,7,14] and rows[-1]['B']==[2,3,4,6,8]
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<3 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='32a24c24',
                         formula_calls=8,E28_partitions=0,rows=rows,root_maps=roots,
                         offset_maps=maps,trap_maps=traps,offset_and_failure_cases=7746,
                         omitted_reflection=dict(A=A,B=B,word=word,geometry_valid=True,
                                                 original_bag_valid=False),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
