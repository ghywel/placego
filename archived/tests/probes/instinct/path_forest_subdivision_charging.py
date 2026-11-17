#!/usr/bin/env python3
"""B116/MI253: complete small free-subdivision charging diagnostic.

1008 labelled seven-point two-chain parents in 0..7; every unequal split
of every occurring gap; four fixed sharp/equal/cross-coordinate controls.
40000 insertion checks,5CPU sec/64MiB. No N5 existence or E28 census.
MI252's infinite lemma remains PROOF-SKETCH, not independently verified.
Preregistration39c400a5. OUTCOME MI254:1008 parents,1112 questions,
24 forced questions,2606 insertion checks pass;0.124796CPU sec,17780736RSS.
Artifact SHA256 e3dc34d3f89026290697606bcce6773cc22ef582ff9dc2f20b364d11d3486b28.
"""
from collections import Counter
from itertools import combinations, product
import json
import resource
import time

import path_forest_partial_padding as validation


def gaps(chain):
    return [v-u for u,v in zip(chain,chain[1:])]


def audit(A,B,h,s,a,b,unequal=True):
    A=list(A);B=list(B);M=2*(h+1);occupied=set(A+B)
    assert A==sorted(A) and B==sorted(B) and not set(A)&set(B)
    assert len(A)+len(B)==7 and len(occupied)==7
    assert 0<=min(occupied)<=max(occupied)<=h
    assert a>0 and b>0 and a+b==s
    if unequal:assert a<b
    else:assert a==b
    parent_gaps=gaps(A)+gaps(B);assert len(parent_gaps)==5
    r=parent_gaps.count(s);assert r
    parent_xs,parent_word=validation.physical(M,A,B)
    assert validation.literal(M,parent_xs)
    assert validation.instrument.literal_geometry(M,set(),parent_xs)
    p=parent_word[0];q=parent_word[len(B)]
    expected=parent_gaps.copy();expected.remove(s);expected.extend((a,b))
    candidates=[];first_free=None;positive_free=0
    choices=(a,b) if unequal else (a,)
    for colour,chain in enumerate((A,B)):
        for j,(v,w) in enumerate(zip(chain,chain[1:])):
            if w-v!=s:continue
            for offset in choices:
                z=v+offset;assert v<z<w and z not in chain
                blocked=z in occupied
                AA=A.copy();BB=B.copy();target=AA if colour==0 else BB
                target.insert(j+1,z)
                assert (AA[0],AA[-1],BB[0],BB[-1])==(A[0],A[-1],B[0],B[-1])
                assert Counter(gaps(AA)+gaps(BB))==Counter(expected)
                xs,word=validation.physical(M,AA,BB)
                assert word[0]==p and word[len(BB)]==q
                assert Counter(word)==Counter((p,q,*(-2*d for d in expected)))
                direct=not set(AA)&set(BB)
                assert direct==(not blocked)
                assert validation.literal(M,xs)==direct
                assert validation.instrument.literal_geometry(M,set(),xs)==direct
                if direct:
                    if first_free is None:first_free=dict(colour=colour,edge=j,index=z,A=AA,B=BB)
                    if min(p,q)>0:
                        validation.validate(M,expected,p,q,AA,BB,0,False)
                        positive_free+=1
                candidates.append(dict(colour=colour,edge=j,index=z,blocked=blocked))
    assert len(candidates)==r*len(choices)
    blocked=[c['index'] for c in candidates if c['blocked']]
    free=[c['index'] for c in candidates if not c['blocked']]
    assert len(blocked)==len(set(blocked))
    assert not {min(occupied),max(occupied)}&set(blocked)
    assert len(blocked)<=5
    forced=unequal and 2*r>5
    if forced:assert free and first_free is not None
    return dict(A=A,B=B,h=h,s=s,a=a,b=b,r=r,p=p,q=q,forced=forced,
                candidates=candidates,blocked=blocked,free=free,first_free=first_free,
                positive_free_checks=positive_free)


def main():
    start=time.process_time();parents=[]
    for occupied in combinations(range(8),7):
        for mask in range(1,(1<<7)-1):
            A=tuple(v for i,v in enumerate(occupied) if mask>>i&1)
            B=tuple(v for i,v in enumerate(occupied) if not mask>>i&1)
            parents.append((A,B))
    assert len(parents)==len(set(parents))==1008
    independent=set()
    for word in product(range(3),repeat=8):
        if word.count(0)!=1 or 1 not in word or 2 not in word:continue
        independent.add((tuple(i for i,c in enumerate(word) if c==1),
                         tuple(i for i,c in enumerate(word) if c==2)))
    assert independent==set(parents)
    rows=[];checks=0
    for A,B in parents:
        for s in sorted(set(gaps(A)+gaps(B))):
            for a in range(1,(s-1)//2+1):
                b=s-a
                row=audit(A,B,7,s,a,b)
                checks+=len(row['candidates']);assert checks<=40000
                rows.append(row)
    assert any(r['forced'] and r['r']==3 for r in rows)
    low=audit([0,3,6],[1,2,4,5],7,3,1,2)
    equal=audit([0,3,5,7],[2,4,6],7,2,1,1,False)
    cross=audit([0,3,6],[1,4,5,7],7,3,1,2)
    balanced=audit([0,3,6,9],[1,4,8],9,3,1,2)
    assert low['r']==2 and len(low['blocked'])==4 and not low['free']
    assert equal['r']==4 and len(equal['candidates'])==4 and not equal['free']
    fake_count=2*equal['r'];assert fake_count>5 and not equal['free']
    assert cross['r']==3 and cross['free']==[2,2]
    assert len(cross['blocked'])==len(set(cross['blocked']))==4
    assert balanced['r']==4 and 1 in balanced['blocked'] and 2 in balanced['free']
    assert balanced['first_free']['A']==[0,2,3,6,9]
    assert balanced['first_free']['B']==[1,4,8]
    assert (balanced['p'],balanced['q'])==(17,15)
    fixed=[low,equal,cross,balanced]
    checks+=sum(len(v['candidates']) for v in fixed);assert checks<=40000
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<5 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',parents=1008,
                         independent_parent_sets_agree=True,questions=len(rows),
                         forced_questions=sum(r['forced'] for r in rows),
                         insertion_checks=checks,
                         positive_free_checks=sum(r['positive_free_checks'] for r in rows+fixed),
                         E28_partitions=0,rows=rows,fixed_controls=fixed,
                         equal_fake_choice_counterfactual=fake_count,
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
