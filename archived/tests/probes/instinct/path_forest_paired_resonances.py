#!/usr/bin/env python3
"""B104/MI234 prereg962b5fe0: exact paired-gap canonical obstructions.

Diagnostic s1..3,t2s..2s+3,w t..2t+s-1,h max(6,2t)..2s+2t-1;
all legal positives/capacity masks, complete offset maps and eight repairs.
3000 formulas/40000 offset-order or exception-root cases;2CPU sec/64MiB.
No whole-cycle solver, new actual partitions or general E28 conclusion.
OUTCOME MI235:539 formulas/205 complete offset maps,exactly eight repairs;
0.127142CPU sec/18538496RSS bytes. Artifact SHA256
256cf03e435ab91b34208fbe558b5eb2d61fcd3de331e5ff0679edeb44c7b583.
"""
from collections import Counter
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import resource
import time

import path_forest_partial_padding as validation
import path_forest_forced_short_ownership as forced


EXCEPTIONS = {
    (1,3,3,7,9,13), (1,3,3,7,11,11), (1,3,4,7,11,13),
    (1,4,5,9,13,17), (1,4,5,9,15,15),
    (2,5,7,12,19,23), (2,5,7,12,21,21), (2,5,7,13,17,25),
}


def prefix(x,gaps):
    out=[x]
    for gap in gaps:out.append(out[-1]+gap)
    return out


def capacity(d,h):
    K=sum(d);fits=[];bits=1
    for v in d:bits |= bits<<v
    for mask in range(32):
        load=sum(v for i,v in enumerate(d) if mask>>i&1)
        if load<=h and K-load<=h:fits.append(mask)
    assert bool(fits)==any(bits>>v&1 for v in range(max(0,K-h),h+1))
    return fits


def interval(H,J,alpha):
    if alpha<=min(H,J):return -alpha,alpha
    if H<alpha<=J:return alpha-1-2*H,alpha
    assert J<alpha<=H
    return -alpha,2*J-alpha+1


def bad_offsets(s,t,w,h):
    H=h-2*t;J=h-2*s-w;delta=J-H
    bad={0,delta}
    if w in (t,t+s) and H>=s:bad|={-s,delta+s}
    assert all(-H<=z<=J for z in bad)
    return bad


def shapes(s,w):
    return [[0,s,2*s,2*s+w],[0,s,s+w,2*s+w],[0,w,w+s,w+2*s]]


def finish(s,t,w,h,p,q,preA,preB,c,alpha,kind,**extra):
    first=0 if p>=q else 1;reflected=c==alpha-1
    assert c in (alpha,alpha-1)
    A=preA;B=preB
    if reflected:
        A=[h-v for v in reversed(A)];B=[h-v for v in reversed(B)];first=1-first
    row=validation.validate(2*(h+1),[s,s,t,t,w],p,q,A,B,first,False)
    row.update(s=s,t=t,w=w,h=h,p=p,q=q,kind=kind,alpha=alpha,
               root=c,preA=preA,preB=preB,reflected=reflected,**extra)
    return row


def construct(s,t,w,h,p,q):
    if h<6:raise ValueError('seven vertices require seven folded labels')
    assert s>=1 and t>=2*s and w>=t and h<2*s+2*t
    d=[s,s,t,t,w];K=sum(d)
    assert p>0 and q>0 and p%2 and q%2 and p+q==2*K
    assert max(p,q)<=2*h-1 and not p==q==2*h-1
    assert capacity(d,h)
    alpha=(2*h+1-max(p,q))//2
    if w+2*s>h:
        row=forced.construct(2*(h+1),d,p,q)
        row.update(s=s,t=t,w=w,h=h,kind='forced_capacity')
        return row
    H=h-2*t;J=h-2*s-w;T=H+J
    assert H>=0 and J>=0 and T>=2 and 1<=alpha<=((T+1)//2)<T
    lo,hi=interval(H,J,alpha);bad=bad_offsets(s,t,w,h)
    z=next((v for v in range(lo,min(hi,lo+4)+1) if v not in bad),None)
    if z is None:
        assert (s,t,w,h,min(p,q),max(p,q)) in EXCEPTIONS
        c=min(alpha,s);preA=[c,c+s,c+s+w];preB=[0,t,t+s,2*t+s]
        return finish(s,t,w,h,p,q,preA,preB,c,alpha,'finite_repair',bad=sorted(bad),I=[lo,hi])
    c=alpha if z%2==alpha%2 else alpha-1
    x=(c-z)//2;y=(c+z)//2
    assert 0<=x<=H and 0<=y<=J
    preA=[x,x+t,x+2*t]
    preB=next([y+v for v in shape] for shape in shapes(s,w)
              if not set(preA)&{y+v for v in shape})
    return finish(s,t,w,h,p,q,preA,preB,c,alpha,'canonical',z=z,bad=sorted(bad),I=[lo,hi])


def offset_control(s,t,w,h):
    H=h-2*t;J=h-2*s-w;aa=[0,t,2*t];bs=shapes(s,w)
    assert [prefix(0,g) for g in sorted(set(permutations((s,s,w))))]==bs
    difference_sets=[{a-b for a in aa for b in shape} for shape in bs]
    intersection=set.intersection(*difference_sets)&set(range(-H,J+1))
    assert intersection==bad_offsets(s,t,w,h)
    measured_bad=[];checks=0
    for z in range(-H,J+1):
        x=max(0,-z);y=x+z;A=[x+v for v in aa];answers=[]
        assert 0<=x<=H and 0<=y<=J
        for shape in bs:
            B=[y+v for v in shape];direct=not set(A)&set(B)
            xs,word=validation.physical(2*(h+1),A,B)
            assert validation.literal(2*(h+1),xs)==direct
            assert validation.instrument.literal_geometry(2*(h+1),set(),xs)==direct
            assert Counter(word)==Counter((word[0],word[len(B)],-2*s,-2*s,-2*t,-2*t,-2*w))
            answers.append(direct);checks+=1
        if not any(answers):measured_bad.append(z)
    assert set(measured_bad)==intersection
    return dict(s=s,t=t,w=w,h=h,H=H,J=J,bad=measured_bad,checks=checks)


def complete_exception(key):
    s,t,w,h,p,q=key;M=2*(h+1);counts=[];checks=0
    for ag,bg in [((t,t),(s,s,w)),((s,s,w),(t,t))]:
        candidates=valid=0
        for x,y in product(range(h-sum(ag)+1),range(h-sum(bg)+1)):
            for ao,bo in product(sorted(set(permutations(ag))),sorted(set(permutations(bg)))):
                A=prefix(x,ao);B=prefix(y,bo);xs,word=validation.physical(M,A,B)
                direct=not set(A)&set(B);checks+=1
                assert validation.literal(M,xs)==direct
                assert validation.instrument.literal_geometry(M,set(),xs)==direct
                if Counter(word)==Counter((p,q,-2*s,-2*s,-2*t,-2*t,-2*w)):
                    candidates+=1;valid+=direct
        assert candidates and valid==0
        counts.append(dict(candidates=candidates,valid=valid))
    return dict(key=key,parity_roles=counts,checks=checks)


def main():
    start=time.process_time();rows=[];offsets=[];profile_count=capacity_checks=0
    counts=Counter();exceptions=[];checked=0
    for s in range(1,4):
        for t in range(2*s,2*s+4):
            for w in range(t,2*t+s):
                for h in range(max(6,2*t),2*s+2*t):
                    profile_count+=1;d=[s,s,t,t,w];fits=capacity(d,h);capacity_checks+=32
                    if not fits:continue
                    if w+2*s<=h:
                        rec=offset_control(s,t,w,h);offsets.append(rec);checked+=rec['checks']
                    K=sum(d)
                    for p in range(1,K+1,2):
                        q=2*K-p
                        if q>2*h-1 or p==q==2*h-1:continue
                        row=construct(s,t,w,h,p,q);rows.append(row);counts[row['kind']]+=1
                        if row['kind']=='finite_repair':exceptions.append((s,t,w,h,p,q))
                        assert len(rows)<=3000 and checked<=40000
    assert set(exceptions)==EXCEPTIONS and len(exceptions)==8
    exception_maps=[complete_exception(key) for key in sorted(EXCEPTIONS)]
    checked+=sum(v['checks'] for v in exception_maps)
    assert checked<=40000 and counts['forced_capacity']>0
    named=next(v for v in rows if (v['s'],v['t'],v['w'],v['h'],v['p'],v['q'])==(2,4,8,11,19,21))
    assert named['kind']=='forced_capacity'
    # The false endpoint-only rule accepts a genuinely universally bad offset.
    assert -1 not in {0,6-5} and -1 in bad_offsets(1,3,3,7)
    assert next(v for v in offsets if (v['s'],v['t'],v['w'],v['h'])==(1,3,3,7))['bad']==[-1,0,1,2]
    try:construct(1,2,2,5,7,9)
    except ValueError:label_refused=True
    else:raise AssertionError('seven-label countercontrol not refused')
    assert capacity([1,1,2,2,2],5) and 7+9==2*8 and max(7,9)==2*5-1
    scaled=construct(4,10,14,26,33,51);assert scaled['kind']=='canonical'
    raw=Path('/tmp/math-instinct-b103-canonical-obstruction.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    assert digest=='c2d4738c551cc2426a0d1d73c378dcaa5d4d30d37a3f4864d9ec13c9d8be81ed'
    old=json.loads(raw)['alternative_rows'][0]
    current=next(v for v in rows if (v['s'],v['t'],v['w'],v['h'],v['p'],v['q'])==(2,5,7,13,17,25))
    assert old['A']==current['A'] and old['B']==current['B'] and old['word']==current['word']
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert len(rows)+1<=3000 and elapsed<2 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='962b5fe0',
                         grid_profiles=profile_count,capacity_mask_checks=capacity_checks,
                         formula_calls=len(rows)+1,grid_formula_calls=len(rows),branches=dict(counts),
                         canonical_profile_maps=offsets,offset_and_exception_cases=checked,
                         exception_maps=exception_maps,rows=rows,scaled=scaled,
                         label_control_refused=label_refused,B103_input_sha256=digest,
                         reused_E28_certificate=True,new_E28_partitions=0,
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
