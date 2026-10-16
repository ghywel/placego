#!/usr/bin/env python3
"""B76/MI173 prereg6ed48def: parity-class shifts change odd-jump imbalance.

Only26 positive geometry fixtures,18 exact range failures, two essential-
assumption countercontrols and four labelled E28 partitions.1CPU sec/64MiB.
No enlarged grid/search/target coverage inference. Hand construction SKETCH.
OUTCOME:26 geometry fixtures/18 predicted range failures/4 labelled partitions
pass; uniform-translation and odd-M failures retained.0.001388CPU sec,
15179776bytes RSS. Raw SHA256
f6aa1aefe9cd343bdf26e3668bdeeb235c23b169cee907eceea5c068245fc54d.
"""
import json
import resource
import time

import path_forest_balanced_bridge as instrument
import path_forest_split_anchor_pilot as pilot


def raw_shift(xs,z,t):
    # Original colours, before z: odd z swaps current colours but not ownership.
    return [x+z+(t if x%2==0 else -t) for x in xs]


def bounds(M,xs,z):
    E=[x for x in xs if x%2==0];O=[x for x in xs if x%2]
    assert E and O
    return (max(-min(E)-z,max(O)+z-(M-1)),
            min(M-1-max(E)-z,min(O)+z))


def direct_word(word,root):
    xs=[root]
    for step in word:xs.append(xs[-1]+step)
    assert xs[-1]==root
    return xs[:-1]


def source(r):
    return [0,6*r+3,4*r+3,2*r+1,1,6*r+4,4*r+2,2*r+2]


def main():
    start=time.process_time();rows=[];negatives=[];base_count=0
    for r in (2,3,4,10,100):
        a,b,c=6*r+3,2*r,2*r+2;xs=source(r)
        base_word=(a,-b,-c,-b,a,-c,-b,-c)
        assert xs==direct_word(base_word,0)
        E=[x for x in xs if x%2==0];O=[x for x in xs if x%2]
        cross={u+v for u in E for v in O}
        for M in sorted({6*r+8,8*r+4}):
            base_count+=1;Z=(M-6*r-8)//2
            assert instrument.literal_geometry(M,set(),xs)
            assert M-1-2*Z==6*r+7 and 6*r+7 not in cross
            assert bounds(M,xs,Z)==(-Z,Z+1)
            for t in sorted({-Z,0,1,Z+1}):
                image=raw_shift(xs,Z,t)
                word=(a-2*t,-b,-c,-b,a+2*t,-c,-b,-c)
                assert min(a-2*t,a+2*t)>0
                assert image==direct_word(word,Z+t)
                assert {u+v+2*Z for u in E for v in O}=={
                    image[i]+image[j] for i,x in enumerate(xs) if x%2==0
                    for j,y in enumerate(xs) if y%2}
                assert len(set(min(x,M-1-x) for x in image))==8
                assert instrument.literal_geometry(M,set(),image)
                for i,e in enumerate(base_word):
                    changed=word[i]-e
                    expected=0 if e%2==0 else (-2*t if xs[i]%2==0 else 2*t)
                    assert changed==expected
                rows.append(dict(r=r,M=M,z=Z,t=t,source=xs,positions=image,word=word))
            for t in (-Z-1,Z+2):
                image=raw_shift(xs,Z,t)
                assert min(image)==-1 and not instrument.literal_geometry(M,set(),image)
                negatives.append(dict(r=r,M=M,z=Z,t=t,positions=image,reason='MINIMUM_MINUS_ONE'))
    assert base_count==9 and len(rows)==26 and len(negatives)==18
    base=source(3);uniform=[x+2 for x in base]
    assert 3 in uniform and 24 in uniform and not instrument.literal_geometry(28,set(),uniform)
    odd_source=[0,3,6];odd_image=raw_shift(odd_source,0,1)
    assert instrument.literal_geometry(9,set(),odd_source)
    assert odd_image==[1,2,7] and not instrument.literal_geometry(9,set(),odd_image)
    owners=(0,2,3,4,1,5,6,7);partitions=[];distinct=set()
    for row in rows:
        if row['r']!=3 or row['M']!=28:continue
        t=row['t'];e=[21-2*t,21+2*t,-6,-8,-6,-8,-6,-8]
        h=[1,1,2,2,2,2,2,2];targets=[56*s+2*v for s,v in zip(h,e)]
        selected=dict(zip(owners,row['positions']))
        bins=instrument.materialize(28,set(),[0]*8,h,e,selected,targets)
        assert pilot.literal_ok(bins,targets,h) and pilot.independent_ok(bins,targets)
        assert all(68<=v<=122 for v in targets)
        distinct.add(tuple(sorted(targets)))
        partitions.append(dict(t=t,targets=targets,slots=h,moves=e,selected=selected,bins=bins))
    assert len(partitions)==4 and len(distinct)==3
    far=next(row for row in rows if row['r']==3 and row['M']==28 and row['t']==2)
    assert far['positions']==[3,20,14,6,0,25,17,11]
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='6ed48def',
                         bases=base_count,positive_geometries=len(rows),range_failures=len(negatives),
                         rows=rows,range_counterexamples=negatives,partitions=partitions,
                         distinct_sorted_E28=sorted(distinct),
                         assumption_controls=dict(uniform_translation=uniform,odd_M=odd_image),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
