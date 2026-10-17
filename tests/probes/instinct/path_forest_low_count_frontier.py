#!/usr/bin/env python3
"""B98/MI222 preregea1933cd: frozen N3/N4 admission steering only.

Existing theorem tags plus a derived isolated-largest N4 admission.
<=180 local formula calls/one E28 partition with two zero-move baselines.
2CPU sec/64MiB; no input regeneration or whole-cycle existence solver.
All new general admission tags remain SKETCH.
OUTCOME MI223:156/156 N3,154/180 N4 admitted provisionally;26 remain.
139 formulas/one partition pass;0.023005CPU sec,20500480RSS bytes.
Artifact SHA256 34e2246d5c58a72c4e4a6f5afdabfe7321ed2252961da3d2e24d14bcf3bd5e29.
"""
from collections import Counter
from itertools import combinations,permutations
from pathlib import Path
import hashlib
import json
import resource
import time

import path_forest_partial_padding as validation


def repeat_tags(d):
    N=len(d);counts=Counter(d);tags=[]
    if max(counts.values())>=N-1:tags.append('MI218_SKETCH_one_exception')
    for s in counts:
        if s<2 or counts[s]<N-2:continue
        rest=list(d)
        for _ in range(N-2):rest.remove(s)
        if min(rest)>=s:
            tags.append('MI214_220_SKETCH_two_larger');break
    independent_one=any(len({v for j,v in enumerate(d) if j!=i})==1 for i in range(N))
    independent_two=False
    for i,j in combinations(range(N),2):
        rest=[v for k,v in enumerate(d) if k not in (i,j)]
        if len(set(rest))==1 and rest[0]>=2 and min(d[i],d[j])>=rest[0]:
            independent_two=True
    assert independent_one==('MI218_SKETCH_one_exception' in tags)
    assert independent_two==('MI214_220_SKETCH_two_larger' in tags)
    return tags


def isolatable(d,h=13):
    if len(d)!=4:return False
    B=d[:-1];D=d[-1];S=sum(B);counts=Counter(B)
    return h<sum(d)<=2*h-2 and D<=h and S<=h and len(counts)>1 and counts[1]<2


def prefix(x,steps):
    out=[x]
    for v in steps:out.append(out[-1]+v)
    return out


def construct(d,p,q):
    if not isolatable(d):raise ValueError('outside isolated-largest admission')
    h=13;B=d[:-1];D=d[-1];S=sum(B);H=h-D;J=h-S;T=H+J
    assert p%2 and q%2 and min(p,q)>0 and p+q==2*sum(d) and max(p,q)<=25
    assert not p==q==25 and T>=2
    alpha=(27-max(p,q))//2
    if alpha<=min(H,J):lo,hi=-alpha,alpha
    elif H<alpha<=J:lo,hi=alpha-1-2*H,alpha
    else:
        assert J<alpha<=H;lo,hi=-alpha,2*J-alpha+1
    counts=Counter(B);repeated=None;extra=None
    if len(counts)==2:
        repeated=next(v for v,n in counts.items() if n==2)
        extra=next(v for v in counts if v!=repeated)
        assert repeated>=2
    d0=D-S
    def bad(z):
        return z in (0,d0) or (repeated is not None and D%repeated==extra%repeated
                               and d0<z<0 and z%repeated==0)
    candidates=list(range(lo,min(hi+1,lo+3)))
    assert H==0 or J==0 or len(candidates)==3
    z=next(v for v in candidates if not bad(v))
    c=alpha if z%2==alpha%2 else alpha-1
    x=(c-z)//2;y=(c+z)//2
    assert 0<=x<=H and 0<=y<=J and x+y==c
    preA=[x,x+D];forbidden={v-y for v in preA if y<v<y+S}
    tries=0;chosen=None
    for order in sorted(set(permutations(B))):
        tries+=1
        if not set(prefix(0,order)[1:-1])&forbidden:
            chosen=order;break
    assert chosen is not None and tries<=6
    preB=prefix(y,chosen)
    first=0 if p>=q else 1;reflected=c==alpha-1
    A=preA;Bc=preB
    if reflected:
        A=[h-v for v in reversed(A)];Bc=[h-v for v in reversed(Bc)]
        first=1-first
    row=validation.validate(28,d,p,q,A,Bc,first,False)
    row.update(d=d,p=p,q=q,H=H,J=J,alpha=alpha,c=c,z=z,d0=d0,
               repeated=repeated,exception=extra,local_orders_tried=tries,
               preA=preA,preB=preB,reflected=reflected)
    return row


def materialize_two_baselines(row):
    d=row['d'];p=row['p'];q=row['q'];first=row['first_owner']
    assert len(d)==4 and min(p,q)>=7
    e=[p,q]+[-2*v for v in d]+[0,0];h=[1,1]+[2]*6
    targets=[56*s+2*v for s,v in zip(h,e)]
    pool={v:[i+2 for i,w in enumerate(d) if w==v] for v in set(d)};selected={}
    for j,move in enumerate(row['word']):
        owner=first if j==0 else 1-first if j==len(row['B']) else pool[-move//2].pop(0)
        assert e[owner]==move;selected[owner]=row['positions'][j]
    assert set(selected)==set(range(6)) and all(not v for v in pool.values())
    assert min(targets)>=68 and sum(targets)==784
    bins=validation.instrument.materialize(28,set(),[0]*8,h,e,selected,targets)
    assert validation.instrument.literal_ok(28,bins,targets,h)
    assert validation.instrument.independent_ok(28,bins,targets)
    return dict(targets=targets,bins=bins,selected=selected,owner_moves=e,baseline_owners=[6,7])


def main():
    start=time.process_time();raw=Path('/tmp/math-instinct-b87-admission-synthesis.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    assert digest=='3b53cad88d8f0930397f545953dbad8b3a2a38adc7e37242bd90641a9ad885d0'
    prior=json.loads(raw);source=[v for v in prior['residual'] if v['N'] in (3,4)]
    assert sum(v['questions'] for v in source if v['N']==3)==156
    assert sum(v['questions'] for v in source if v['N']==4)==180
    records=[];first_before=None
    for r in source:
        d=r['d'];assert not r['admissions'] and len(d)==r['N']
        sums={0}
        for v in d:sums|={s+v for s in sums}
        assert any(sum(d)-13<=s<=13 for s in sums)
        tags=repeat_tags(d)
        if len(d)==3:tags.append('MI201_SKETCH_five_vertex')
        if len(d)==4 and not tags and first_before is None:first_before=r
        if isolatable(d):tags.append('MI222_SKETCH_isolated_largest')
        records.append(dict(d=d,N=r['N'],K=r['K'],positive_pairs=r['positive_pairs'],
                            questions=r['questions'],new_SKETCH_admissions=tags))
    remaining=[v for v in records if not v['new_SKETCH_admissions']]
    preliminary=dict(records=records,first_before_isolation=first_before,remaining=remaining)
    Path('/tmp/math-instinct-b98-audit-before-formulas.json').write_text(json.dumps(preliminary))
    assert first_before['d']==[1,4,4,5] and first_before['positive_pairs']==[[3,25],[5,23],[7,21],[9,19],[11,17],[13,15]]
    assert remaining and remaining[0]['d']==[1,4,9,9]
    assert remaining[0]['positive_pairs']==[[21,25],[23,23]]
    assert not any(v['N']==3 for v in remaining)
    overlap=next(v for v in prior['records'] if v['d']==[4,4,4,5])
    assert set(repeat_tags(overlap['d']))=={'MI218_SKETCH_one_exception','MI214_220_SKETCH_two_larger'}
    formulas=[]
    for r in records:
        if 'MI222_SKETCH_isolated_largest' in r['new_SKETCH_admissions']:
            formulas.extend(construct(r['d'],p,q) for p,q in r['positive_pairs'])
    assert len(formulas)<=180
    actual=next(v for v in formulas if v['d']==[1,4,4,5] and (v['p'],v['q'])==(7,21))
    partition=materialize_two_baselines(actual)
    try:construct([1,4,9,9],21,25)
    except ValueError:pass
    else:raise AssertionError('missing isolated-capacity refusal')
    assert 1+9<=13 and 4+9<=13
    A=[1,6];B=[2,6,10,11];xs,word=validation.physical(28,A,B)
    assert Counter(word)==Counter((21,7,-2,-8,-8,-10))
    assert len(set(xs))==6 and all(0<=v<28 for v in xs) and set(A)&set(B)=={6}
    assert not validation.literal(28,xs) and not validation.instrument.literal_geometry(28,set(),xs)
    byN={str(N):dict(old_questions=sum(v['questions'] for v in records if v['N']==N),
                    SKETCH_admitted=sum(v['questions'] for v in records if v['N']==N and v['new_SKETCH_admissions']),
                    remaining=sum(v['questions'] for v in remaining if v['N']==N)) for N in (3,4)}
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<2 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='ea1933cd',
                         input_sha256=digest,scope='frozen B87 residual N3/N4 only; tags SKETCH',
                         byN=byN,records=records,remaining=remaining,formula_calls=len(formulas),
                         formulas=formulas,E28_partitions=1,actual_partition=partition,
                         overlap_control=overlap['d'],first_remaining=remaining[0],
                         negative_order_control=dict(A=A,B=B,positions=xs,word=word,bag_valid=True,folded_geometry_valid=False),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
