#!/usr/bin/env python3
"""B118/MI256: complementary small-terminal forced-window diagnostic.

42 fixed profiles,69 forced formulas,two supplied-parent children;
7056 capacity-mask cases,168 full fixed-layout offsets,69 root maps.
Predict33 broad/36 thin,21 negative offsets,15 reflections,nine T1 refusals.
3CPU sec/64MiB,100 formulas/10000 cases;no N5 existence/E28 census.
MI255/MI252 remain PROOF-SKETCH,not independently verified here.
"""
from collections import Counter
from itertools import product
import json
import resource
import time

import path_forest_partial_padding as validation


def chains(m,s,a,b,x,y):
    return ([x+i*s for i in range(m+1)]+[x+m*s+b],
            [y+i*s for i in range(m+1)]+[y+m*s+a])


def construct(m,s,a,h,p,q):
    b=s-a;d=[s]*(2*m)+[a,b];K=(2*m+1)*s
    assert m>=1 and 0<a<b and m*s+b<=h<(m+1)*s
    assert min(p,q)>0 and p%2 and q%2 and p+q==2*K and max(p,q)<=2*h-1
    if p==q==2*h-1:raise ValueError('doubled maximum')
    H=h-m*s-b;delta=b-a;J=H+delta;T=2*h-K
    assert 0<=H<a and J<b and T>=2
    alpha=(2*h+1-max(p,q))//2
    assert 1<=alpha<=H+(delta+1)//2
    if alpha<=2*H:
        branch='broad';c=alpha if alpha%2 else alpha-1
        if delta==1:assert a>=2
        z=-1 if delta==1 else 1
        x=(c-z)//2;y=(c+z)//2
    else:
        branch='thin';assert delta>=2
        c=alpha;x=H;y=alpha-H;z=alpha-2*H
        assert 0<z<delta<s
    assert 0<=x<=H and 0<=y<=J and -a<z<b and z%s and z!=delta
    preA,preB=chains(m,s,a,b,x,y)
    first=0 if p>=q else 1;reflected=c==alpha-1
    A=preA;B=preB
    if reflected:
        A=[h-v for v in reversed(A)];B=[h-v for v in reversed(B)];first=1-first
    row=validation.validate(2*(h+1),d,p,q,A,B,first,False)
    row.update(m=m,s=s,a=a,b=b,h=h,p=p,q=q,H=H,J=J,T=T,delta=delta,
               alpha=alpha,c=c,z=z,x=x,y=y,branch=branch,
               preA=preA,preB=preB,reflected=reflected)
    return row


def capacity_control(m,s,a,h):
    b=s-a;d=[s]*(2*m)+[a,b];K=sum(d);loads=[];fits=[];bits=1
    for v in d:bits |= bits<<v
    for mask in range(1<<len(d)):
        load=sum(v for i,v in enumerate(d) if mask>>i&1);loads.append(load)
        if load<=h and K-load<=h:
            assert sum(bool(mask>>i&1) for i in range(2*m))==m
            assert bool(mask>>(2*m)&1)!=bool(mask>>(2*m+1)&1)
            fits.append(mask)
    assert fits and set(loads)=={v for v in range(K+1) if bits>>v&1}
    assert min(max(v,K-v) for v in loads)==m*s+b
    parent_loads=[s*mask.bit_count() for mask in range(1<<(2*m+1))]
    assert min(max(v,K-v) for v in parent_loads)==(m+1)*s
    assert not any(v<=h and K-v<=h for v in parent_loads)
    return dict(m=m,s=s,a=a,b=b,h=h,minimum=m*s+b,parent_minimum=(m+1)*s,
                target_masks=len(loads),parent_masks=len(parent_loads),fitting_masks=fits)


def offset_control(m,s,a,h):
    b=s-a;H=h-m*s-b;J=h-m*s-a;delta=b-a;M=2*(h+1)
    bad=[];cases=0
    for z in range(-H,J+1):
        x=max(0,-z);y=x+z
        assert 0<=x<=H and 0<=y<=J
        A,B=chains(m,s,a,b,x,y);direct=not set(A)&set(B)
        xs,word=validation.physical(M,A,B)
        assert validation.literal(M,xs)==direct
        assert validation.instrument.literal_geometry(M,set(),xs)==direct
        assert direct==(z not in (0,delta))
        if not direct:bad.append(z)
        cases+=1
    assert bad==[0,delta]
    return dict(m=m,s=s,a=a,h=h,bad=bad,cases=cases)


def root_control(row):
    H,J,alpha=row['H'],row['J'],row['alpha']
    direct={y-x for x,y in product(range(H+1),range(J+1))
            if x+y in (alpha,alpha-1)}
    lo=-alpha if alpha<=H else alpha-1-2*H
    assert direct==set(range(lo,alpha+1))
    for z in direct:
        c=alpha if z%2==alpha%2 else alpha-1
        x=(c-z)//2;y=(c+z)//2
        assert 0<=x<=H and 0<=y<=J and x+y==c and y-x==z
    return dict(m=row['m'],s=row['s'],a=row['a'],h=row['h'],
                p=row['p'],q=row['q'],offsets=sorted(direct),cases=(H+1)*(J+1))


def supplied_parent(m,s,a,h,p,q,A,B,z):
    b=s-a;M=2*(h+1)
    parent=validation.validate(M,[s]*(2*m+1),p,q,A,B,0,False)
    assert z not in A+B
    AA=sorted(A+[z]);child=validation.validate(M,[s]*(2*m)+[a,b],p,q,AA,B,0,False)
    child.update(m=m,s=s,a=a,b=b,h=h,p=p,q=q,inserted=z,parent=parent,
                 branch='supplied_parent',reflected=False)
    return child


def main():
    start=time.process_time();rows=[];caps=[];maps=[];refused=[]
    for m in range(1,4):
        for s in range(3,8):
            for a in range(1,(s-1)//2+1):
                b=s-a;K=(2*m+1)*s
                for h in range(m*s+b,(m+1)*s):
                    caps.append(capacity_control(m,s,a,h));maps.append(offset_control(m,s,a,h))
                    local=[]
                    for p in range(1,K+1,2):
                        q=2*K-p
                        if q>2*h-1 or p==q==2*h-1:continue
                        local.append(construct(m,s,a,h,p,q))
                    rows.extend(local)
                    if 2*h-K==1:
                        assert not local and K==2*h-1
                        try:construct(m,s,a,h,K,K)
                        except ValueError as e:assert str(e)=='doubled maximum'
                        else:raise AssertionError('missing doubled-maximum refusal')
                        refused.append(dict(m=m,s=s,a=a,h=h,p=K,q=K))
    assert len(caps)==len(maps)==42 and len(rows)==69 and len(refused)==9
    assert Counter(r['branch'] for r in rows)=={'broad':33,'thin':36}
    assert sum(r['z']<0 for r in rows)==21 and sum(r['reflected'] for r in rows)==15
    assert sum(c['target_masks'] for c in caps)==4704
    assert sum(c['parent_masks'] for c in caps)==2352
    assert sum(v['cases'] for v in maps)==168
    roots=[root_control(r) for r in rows]
    assert sum(r['cases'] for r in roots)==468
    parents=[supplied_parent(2,3,1,9,17,13,[0,3,6,9],[1,4,7],2),
             supplied_parent(3,4,1,16,31,25,[0,4,8,12,16],[1,5,9,13],3)]
    assert len(rows)+len(parents)==71 and all(r['bins'] is None for r in rows+parents)
    wrong=next(r for r in rows if (r['m'],r['s'],r['a'],r['h'],r['p'],r['q'])==(2,5,2,14,25,25))
    xs,word=validation.physical(30,wrong['preA'],wrong['preB'])
    assert validation.literal(30,xs) and validation.instrument.literal_geometry(30,set(),xs)
    assert word[0]==27 and word[len(wrong['preB'])]==23
    assert Counter(word)!=Counter((25,25,*(-2*v for v in [5]*4+[2,3])))
    cases=7056+168+468;assert cases==7692 and cases<=10000
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<3 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',profiles=42,
                         forced_formulas=69,child_formulas=71,E28_partitions=0,
                         capacity_cases=7056,offset_cases=168,root_cases=468,total_cases=cases,
                         rows=rows,capacity=caps,offset_maps=maps,root_maps=roots,
                         parent_children=parents,doubled_maximum_refusals=refused,
                         omitted_reflection=dict(A=wrong['preA'],B=wrong['preB'],word=word,
                                                 geometry_valid=True,original_bag_valid=False),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
