#!/usr/bin/env python3
"""B97/MI220 prereg335b0e2f: forced shared exceptions via capacity carry.

Nine forced formula calls/one baseline-extended E28 partition; capacity
masks/root rectangles and three collision controls; one prior separate call.
1CPU sec/64MiB, no cycle-order or general existence census. Uniform SKETCH.
OUTCOME MI221:9+1 calls/one E28 partition pass;0.002198CPU sec,17068032RSS.
Artifact SHA256 c24437d9baea43b36f2dd37d1982ad5a755545e37ee1967c6dce660fcc01b33c.
"""
from collections import Counter
import json
import resource
import time

import path_forest_partial_padding as validation
import path_forest_unequal_ladders as separate


def prefix(x,steps):
    out=[x]
    for v in steps:out.append(out[-1]+v)
    return out


def partition_with_baseline(row,M,d,p,q,first):
    assert M==28 and len(d)==5
    e=[p,q]+[-2*v for v in d]+[0]*(6-len(d))
    h=[1,1]+[2]*6;t=[56*v+2*w for v,w in zip(h,e)]
    assert len(t)==8 and min(t)>=68 and max(t)<=122 and sum(t)==784
    pool={v:[i+2 for i,w in enumerate(d) if w==v] for v in set(d)}
    selected={}
    for j,move in enumerate(row['word']):
        owner=first if j==0 else 1-first if j==len(row['B']) else pool[-move//2].pop(0)
        assert e[owner]==move;selected[owner]=row['positions'][j]
    assert all(not v for v in pool.values())
    assert set(selected)=={i for i,v in enumerate(e) if v}
    bins=validation.instrument.materialize(M,set(),[0]*8,h,e,selected,t)
    assert validation.instrument.literal_ok(M,bins,t,h)
    assert validation.instrument.independent_ok(M,bins,t)
    assert e[-1]==0 and t[-1]==112 and 7 not in selected
    row.update(targets=t,bins=bins,selected=selected,owner_moves=e,baseline_owners=[7])


def construct(M,s,m,a,b,p,q,partition=False):
    assert M%2==0 and m>=1 and 2<=s<=a<=b
    h=M//2-1;K=m*s+a+b;d=[s]*m+[a,b]
    assert min(p,q)>0 and p%2 and q%2 and p+q==2*K
    assert max(p,q)<=2*h-1 and not p==q==2*h-1
    fsep=(h-a)//s+(h-b)//s;ftog=(h-a-b)//s+h//s
    if fsep>=m:raise ValueError('exceptions need not share a bin')
    assert h>=a+b and ftog>=m
    qb,r=divmod(h,s);Aq,u=divmod(a,s);Bq,v=divmod(b,s)
    assert ftog==m==2*qb-Aq-Bq-1 and fsep==m-1
    assert u>r and v>r and u+v<=r+s
    k=m-qb;assert k>=0
    L=a+b+k*s;S=qb*s;H=h-L;J=h-S;T=H+J
    assert H==r+s-u-v and J==r and 2<=T<=s-2
    alpha=(2*h+1-max(p,q))//2;assert 1<=alpha<=(T+1)//2
    if alpha<=min(H,J):lo,hi=-alpha,alpha
    elif H<alpha<=J:lo,hi=alpha-1-2*H,alpha
    else:
        assert J<alpha<=H;lo,hi=-alpha,2*J-alpha+1
    I=set(range(lo,hi+1));bad={0,u+v-s}
    if H==0:z=alpha
    elif J==0:z=-alpha
    else:
        assert hi-lo+1>=3
        z=next(vv for vv in range(lo,lo+3) if vv not in bad)
    assert z in I and z not in bad
    c=alpha if z%2==alpha%2 else alpha-1
    x=(c-z)//2;y=(c+z)//2
    assert 0<=x<=H and 0<=y<=J and x+y==c
    ag=[a]+[s]*k+[b];bg=[s]*qb
    # Independent direct start rectangle and literal chain intersections.
    direct=set();collisions={}
    for xx in range(H+1):
        for yy in range(J+1):
            if xx+yy not in (alpha,alpha-1):continue
            zz=yy-xx;direct.add(zz)
            shared=set(prefix(xx,ag))&set(prefix(yy,bg))
            assert bool(shared)==(zz in bad)
            collisions.setdefault(zz,[]).append(sorted(shared))
    assert direct==I
    preA=prefix(x,ag);preB=prefix(y,bg)
    first=0 if p>=q else 1;reflected=c==alpha-1
    Ac=preA;Bc=preB
    if reflected:
        Ac=[h-vv for vv in reversed(Ac)];Bc=[h-vv for vv in reversed(Bc)]
        first=1-first
    row=validation.validate(M,d,p,q,Ac,Bc,first,False)
    if partition:partition_with_baseline(row,M,d,p,q,first)
    # Independent labelled-item capacity enumeration, no cycle oracle.
    together=apart=0
    for mask in range(1<<len(d)):
        left=sum(vv for i,vv in enumerate(d) if mask>>i&1)
        if left>h or K-left>h:continue
        if ((mask>>m)&1)==((mask>>(m+1))&1):together+=1
        else:apart+=1
    assert together>0 and apart==0
    row.update(M=M,s=s,m=m,a=a,b=b,p=p,q=q,d=d,F_sep=fsep,F_tog=ftog,
               quotient=qb,remainder=r,u=u,v=v,k=k,L=L,S=S,H=H,J=J,
               T=T,alpha=alpha,offset_interval=sorted(I),bad_offsets=sorted(bad),
               collisions=collisions,c=c,z=z,preA=preA,preB=preB,reflected=reflected,
               capacity_masks=1<<len(d),together_splits=together,separate_splits=apart)
    return row


def negative(M,d,p,q,A,B,shared):
    xs,word=validation.physical(M,A,B)
    assert Counter(word)==Counter((p,q,*(-2*v for v in d)))
    assert all(0<=x<M for x in xs) and len(set(xs))==len(d)+2
    assert set(A)&set(B)==set(shared)
    assert not validation.literal(M,xs) and not validation.instrument.literal_geometry(M,set(),xs)
    return dict(M=M,A=A,B=B,positions=xs,word=word,shared_indices=shared,
                bag_valid=True,folded_geometry_valid=False)


def main():
    start=time.process_time()
    fixtures=[(28,4,3,6,6,23,25),(36,5,3,8,8,31,31),
              (32,5,3,6,6,27,27),(38,5,3,9,9,33,33),
              (46,7,3,9,10,43,37),(46,7,3,9,10,41,39),
              (56,5,7,8,8,51,51),(34,4,4,5,9,31,29),
              (56,8,3,12,15,51,51)]
    rows=[construct(*f,partition=i==0) for i,f in enumerate(fixtures)]
    assert len(rows)==9 and sum(v['bins'] is not None for v in rows)==1
    assert rows[0]['baseline_owners']==[7] and len(rows[0]['selected'])==7
    assert rows[1]['reflected'] and rows[5]['reflected']
    assert rows[2]['J']==0 and rows[3]['H']==0 and rows[8]['H']==0
    assert rows[6]['k']==2
    controls=[negative(36,[5,5,5,8,8],31,31,[1,9,17],[1,6,11,16],[1]),
              negative(46,[7,7,7,9,10],41,39,[2,11,21],[0,7,14,21],[21])]
    try:construct(22,3,3,4,4,17,17)
    except ValueError:pass
    else:raise AssertionError('missing forced-case premise refusal')
    controls.append(negative(22,[3,3,3,4,4],17,17,[2,6,10],[0,3,6,9],[6]))
    outside=separate.construct(22,3,3,4,4,17,17)
    assert outside['bins'] is None
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='335b0e2f',
                         forced_formula_calls=9,existing_formula_calls=1,E28_partitions=1,
                         rows=rows,negative_controls=controls,separate_positive_control=outside,
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
