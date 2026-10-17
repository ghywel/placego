#!/usr/bin/env python3
"""B102/MI230 prereg6a94b44e: forced short ownership after capacity failure.

Ten formulas/six E28 partitions;32 labelled capacity masks, whole fixed-
order root rectangles and original-positive maps;endpoint and scope controls.
2CPU sec/64MiB. No grid regeneration or whole-cycle solver. Theorem SKETCH.
OUTCOME MI231:10 formulas/6 E28 partitions/320 capacity masks/112 root-
orientation entries pass;0.019583CPU sec/20312064RSS bytes. Artifact SHA256
fc8c416ea48c44f6b09084c646fb09daf244d14e328ca364ce78c57ca1c7481b.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import resource
import time

import path_forest_partial_padding as validation
from path_forest_two_unit_triangle import partition


def prefix(x,gaps):
    out=[x]
    for gap in gaps:out.append(out[-1]+gap)
    return out


def ownerships(M,d):
    a,b,u,v,w=d;h=M//2-1;out=[]
    for r,s,owner in ((b,a,1),(a,b,0)):
        if w+r<=h and u+v+s<=h and (r,s) not in [(z['r'],z['s']) for z in out]:
            out.append(dict(r=r,s=s,r_owner=owner,X=h-w-r,Y=h-u-v-s))
    return out


def construct(M,d,p,q):
    assert M%2==0 and len(d)==5 and list(d)==sorted(d) and min(d)>0
    a,b,u,v,w=d;h=M//2-1;C=a+b;L=u+v;K=sum(d)
    if u<C or C+L<=h or w+C<=h:raise ValueError('outside forced short-ownership scope')
    fits=ownerships(M,d)
    if not fits:raise ValueError('no ordinary two-bin capacity')
    assert p>0 and q>0 and p%2 and q%2 and p+q==2*K
    assert max(p,q)<=M-3 and not p==q==M-3
    own=fits[0];r=own['r'];s=own['s'];X=own['X'];Y=own['Y'];T=X+Y;d0=Y-X
    assert X<s and Y<r and 2<=T<=C-2 and h>=9
    alpha=(M-1-max(p,q))//2;assert 1<=alpha< T and alpha<=(T+1)//2
    if alpha<=min(X,Y):lo,hi=-alpha,alpha
    elif X<alpha<=Y:lo,hi=alpha-1-2*X,alpha
    else:
        assert Y<alpha<=X;lo,hi=-alpha,2*Y-alpha+1
    if X==0:z=alpha
    elif Y==0:z=-alpha
    else:z=next(z for z in range(lo,lo+3) if z not in (0,d0))
    assert lo<=z<=hi and z not in (0,d0)
    root=alpha if z%2==alpha%2 else alpha-1
    x=(root-z)//2;y=(root+z)//2
    assert 0<=x<=X and 0<=y<=Y and x+y==root
    preA=prefix(x,(r,w));preB=prefix(y,(u,s,v))
    assert preB[0]<preA[1]<preB[1]<preB[2]<preA[2]
    assert not set(preA)&set(preB)
    first=0 if p>=q else 1;reflected=root==alpha-1;A=preA;B=preB
    if reflected:
        A=[h-z for z in reversed(A)];B=[h-z for z in reversed(B)];first=1-first
    row=validation.validate(M,d,p,q,A,B,first,False)
    row.update(M=M,d=d,p=p,q=q,C=C,L=L,X=X,Y=Y,T=T,d0=d0,
               alpha=alpha,root=root,z=z,ownership=own,fitting_ownerships=fits,
               preA=preA,preB=preB,reflected=reflected)
    return row


def independent_controls(row):
    M=row['M'];h=M//2-1;d=row['d'];a,b,u,v,w=d;K=sum(d);p=row['p'];q=row['q']
    masks=[];normalized=set()
    for mask in range(32):
        load=sum(value for i,value in enumerate(d) if (mask>>i)&1)
        if load<=h and K-load<=h:
            oriented=mask if mask&16 else mask^31
            assert not oriented&12 and (bool(oriented&1)+bool(oriented&2))==1
            normalized.add(oriented);masks.append(dict(mask=mask,loads=[load,K-load]))
    assert masks
    labelled_owns={(d[0],d[1]) if mask&1 else (d[1],d[0]) for mask in normalized}
    assert labelled_owns=={(v['r'],v['s']) for v in ownerships(M,d)}
    rectangles=[];selected_seen=False;checks=0
    for r,s in sorted(labelled_owns):
        X=h-w-r;Y=h-u-v-s;d0=Y-X;entries=[]
        for x in range(X+1):
            for y in range(Y+1):
                for reverse in (False,True):
                    A=prefix(x,(w,r) if reverse else (r,w))
                    B=prefix(y,(v,s,u) if reverse else (u,s,v))
                    xs,word=validation.physical(M,A,B);direct=not set(A)&set(B);checks+=1
                    assert direct==((y-x) not in (0,d0))
                    assert validation.literal(M,xs)==direct
                    assert validation.instrument.literal_geometry(M,set(),xs)==direct
                    original_bag=Counter(word)==Counter((p,q,*(-2*z for z in d)))
                    if A==row['A'] and B==row['B']:
                        assert original_bag and direct;selected_seen=True
                    entries.append(dict(x=x,y=y,reverse=reverse,A=A,B=B,valid=direct,
                                        original_bag=original_bag))
        rectangles.append(dict(r=r,s=s,X=X,Y=Y,entries=entries))
    assert selected_seen
    return dict(capacity_masks=masks,rectangles=rectangles,root_orientation_checks=checks)


def main():
    start=time.process_time();raw=Path('/tmp/math-instinct-b87-admission-synthesis.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    assert digest=='3b53cad88d8f0930397f545953dbad8b3a2a38adc7e37242bd90641a9ad885d0'
    prior=json.loads(raw);chosen=[]
    for rec in prior['records']:
        if rec['N']!=5:continue
        a,b,u,v,w=rec['d'];C=a+b;L=u+v
        if u>=C and C+L>13 and w+C>13:chosen.append(rec)
    explicit={(1,3,4,6,10),(1,3,5,5,10),(2,2,4,6,10),(2,2,5,5,10),
              (1,4,5,5,9),(2,3,5,5,9)}
    assert {tuple(v['d']) for v in chosen}==explicit and len(chosen)==6
    assert all(v['positive_pairs']==[[23,25]] for v in chosen)
    rows=[];partitions=[];controls=[]
    for rec in chosen:
        row=construct(28,rec['d'],23,25);rows.append(row)
        partitions.append(partition(row));controls.append(independent_controls(row))
    fixtures=[(30,[2,3,5,5,10],25,25),(36,[2,4,6,6,14],31,33),
              (40,[2,3,8,8,15],35,37),(30,[1,4,5,5,11],25,27)]
    generic=[]
    for args in fixtures:
        row=construct(*args);generic.append(dict(row=row,controls=independent_controls(row)))
    assert generic[0]['row']['reflected'] and generic[0]['row']['ownership']['r']==3
    assert generic[1]['row']['ownership']['r']==2 and len(generic[1]['row']['fitting_ownerships'])==1
    assert generic[3]['row']['ownership']['r']==1 and generic[3]['row']['Y']==0
    A=[1,4,14];B=[1,6,8,13];xs,word=validation.physical(30,A,B)
    assert Counter(word)==Counter((25,25,-4,-6,-10,-10,-20))
    assert set(A)&set(B)=={1} and len(set(xs))==7 and all(0<=x<30 for x in xs)
    assert not validation.literal(30,xs) and not validation.instrument.literal_geometry(30,set(),xs)
    refused=[]
    for name,args in [('u_below_C',(20,[2,2,3,3,6],15,17)),
                      ('largest_isolatable',(32,[2,3,5,5,12],25,29))]:
        try:construct(*args)
        except ValueError:refused.append(name)
        else:raise AssertionError('scope refusal missing '+name)
    lowA=[1,3,9];lowB=[0,3,5,8];lowxs,lowword=validation.physical(20,lowA,lowB)
    assert Counter(lowword)==Counter((15,17,-4,-4,-6,-6,-12))
    assert set(lowA)&set(lowB)=={3} and not validation.literal(20,lowxs)
    assert not validation.instrument.literal_geometry(20,set(),lowxs)
    alternate_low=validation.validate(20,[2,2,3,3,6],15,17,[0,2,8],[1,4,6,9],1,False)
    alternate_isolated=validation.validate(32,[2,3,5,5,12],25,29,[1,13],[0,2,5,10,15],1,False)
    assert sum((2,3,5,5))==15 and 12<=15
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<2 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='6a94b44e',
                         input_sha256=digest,frozen_profiles=6,frozen_questions=6,
                         formula_calls=10,E28_partitions=6,rows=rows,partitions=partitions,
                         controls=controls,generic=generic,scope_refusals=refused,
                         endpoint_collision=dict(A=A,B=B,positions=xs,word=word,original_bag_valid=True),
                         outside_u_internal_collision=dict(A=lowA,B=lowB,positions=lowxs,word=lowword),
                         outside_u_alternate=alternate_low,outside_nonisolation_alternate=alternate_isolated,
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
