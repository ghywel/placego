#!/usr/bin/env python3
"""B63/MI147 prereg0eee072e:25 primitive wide2+4 profiles, all14 gaps.

Fixed (+a,-b1,-b4,+c,-b2,-b3) order only. Predict350 joint maps nonempty,
independent formula-bitmask/physical-set complete maps agree.42 actual E28
extensions, two literal checkers. Fixed pair0 fails on hand fixture; every
gap7 self-valid root must leave an edge; reflected sign geometry preserved.
Caps25 profiles/350 maps/42 targets/2500 roots/100k pairs/3CPU seconds.
No shape/order/role repair. Hand reduction SKETCH, finite result COMPUTED.
OUTCOME MI148:350/350 complete maps succeed and independently agree;344
core roots/22673 physical pairs. All42 actual targets/checkers/controls PASS.
CPU0.337010s. Artifact SHA256
d71dcdd07867d84a84e82d48d003a39e907f2a3ea1dcf79e6ff6fdfdfcc732fe.
"""
from collections import Counter,defaultdict
from itertools import combinations_with_replacement
import json
import time
from path_forest_six_diameter import EXCEPTIONS,word_points,domain_reference,reference_minimum
from path_forest_cycle_cover import setup,materialize
from path_forest_receiving_chains import certificate_ok
from path_forest_three_surplus_audit import bitset_ok


class Cap(Exception):pass


def primitive(word):
    return not any(sum(word[i] for i in range(6) if mask>>i&1)==0 for mask in range(1,63))


def profiles():
    out=set(EXCEPTIONS)
    counts=Counter()
    for c in range(1,6):
        for b in combinations_with_replacement(range(c+1,8),4):
            if sum(b)==21+c:
                out.add((21,c)+tuple(reversed(b)));counts[c]+=1
    assert [counts[c] for c in range(1,6)]==[8,5,4,2,1]
    out.update(((22,1,6,6,6,5),(22,2,6,6,6,6)))
    ref=set();budget={'states':0}
    for p in domain_reference():
        minimum,is_primitive=reference_minimum(word_points(p)[0],budget)
        if is_primitive and minimum>20:ref.add(p)
    assert out==ref and len(out)==25
    return sorted(out)


def formula_pairs(g):
    out=[]
    for i in range(14):
        for j in range(i+1,14):
            if j-i==g:out.extend(((i,i,j),(27-j,i,j)))
            if i+j==27-g:out.extend(((i,i,j),(j,i,j)))
    return out


def maps(p,budget):
    word,points=word_points(p);low=min(points);points=tuple(x-low for x in points)
    assert primitive(word) and len(set(points))==6
    span=max(points);blocked={(27-x-y)//2 for x in points for y in points if x<y and (x+y)%2}
    primary={g:set() for g in range(1,15)};ref={g:set() for g in range(1,15)};valid=[]
    for r in range(28-span):
        budget['roots']+=1
        if r in blocked:continue
        mask=sum(1<<min(x+r,27-x-r) for x in points)
        assert mask.bit_count()==6
        for g in primary:
            for x,i,j in formula_pairs(g):
                if not mask&((1<<i)|(1<<j)):primary[g].add((r,x))
    for r in range(28-span):
        budget['roots']+=1
        used={min(x+r,27-x-r) for x in points}
        if len(used)!=6:continue
        valid.append(r)
        for g in ref:
            for x in range(28-g):
                budget['pairs']+=1
                if budget['pairs']>100000 or budget['roots']>2500:raise Cap('GEOMETRY')
                labels={min(x,27-x),min(x+g,27-x-g)}
                if len(labels)==2 and not labels&used:ref[g].add((r,x))
            if g==7:assert any(rr==r for rr,_ in ref[g])
    assert primary==ref
    for g,sols in primary.items():
        if not sols:continue
        r,x=min(sols);coords=[y+r for y in points]+[x,x+g];steps=list(word)+[g,-g]
        assert len({min(y,27-y) for y in coords})==8
        assert Counter(y+e for y,e in zip(coords,steps))==Counter(coords)
        reflected=[27-y for y in coords]
        assert Counter(y-e for y,e in zip(reflected,steps))==Counter(reflected)
        assert [min(y,27-y) for y in coords]==[min(y,27-y) for y in reflected]
    return word,points,primary,valid


def target(p,g):
    a,c,*b=p
    return (56+2*g,56+2*a)+tuple(sorted([112-2*x for x in b]+[112-2*g,112+2*c]))


def reference_targets():
    out=set()
    for a in (21,22):
        for g in (6,7):
            if g>28-a:continue
            for c in range(1,6):
                for negatives in combinations_with_replacement(range(1,29-a),5):
                    if sum(negatives)!=a+g+c or g not in negatives:continue
                    b=list(negatives);b.remove(g)
                    if not primitive((a,c)+tuple(-x for x in b)):continue
                    t=(56+2*g,56+2*a)+tuple(sorted(112-2*x for x in negatives))+(112+2*c,)
                    assert list(t)==sorted(t) and sum(t)==784
                    out.add(t)
    # High/high cancellation would leave either of these NONprimitive cores.
    assert not primitive((21,6,-7,-7,-7,-6))
    assert not primitive((21,7,-7,-7,-7,-7))
    return out


def main():
    start=time.process_time();budget={'roots':0,'pairs':0};rows=[];lookup={};failed=[]
    for p in profiles():
        if time.process_time()-start>3:raise Cap('CPU')
        word,points,placements,valid=maps(p,budget);lookup[p]=(word,points,placements)
        for g,sols in placements.items():
            if not sols:failed.append((p,g))
        rows.append(dict(parameters=p,word=word,points=points,valid_core_roots=valid,
                         complete_placements={str(g):sorted(v) for g,v in placements.items()}))
    fixture=(21,1,7,7,5,3);_,_,solutions=lookup[fixture]
    assert next(r['valid_core_roots'] for r in rows if tuple(r['parameters'])==fixture)==[0,6]
    for g in (6,7):
        assert solutions[g] and not any(x==0 for r,x in solutions[g])
        assert (0,1) in solutions[g]
    domain={}
    for p in lookup:
        if p[0]<21:continue
        for g in ((6,7) if p[0]==21 else (6,)):
            t=target(p,g);assert t==tuple(sorted(t)) and sum(t)==784
            assert t not in domain;domain[t]=(p,g)
    assert len(domain)==42 and set(domain)==reference_targets()
    certificates=[];unresolved=[]
    for t,(p,g) in sorted(domain.items()):
        if time.process_time()-start>3:raise Cap('CPU')
        word,points,solutions=lookup[p]
        if not solutions[g]:unresolved.append(t);continue
        r,x=min(solutions[g]);_,_,e=setup(t);owners=defaultdict(list)
        for i,step in enumerate(e):owners[step].append(i)
        selected={}
        for step,y in zip(word,points):selected[owners[step].pop(0)]=r+y
        selected[owners[g].pop(0)]=x;selected[owners[-g].pop(0)]=x+g
        w=materialize(t,selected)
        assert certificate_ok(w['bins'],t) and bitset_ok(w['bins'],t)
        certificates.append(dict(targets=t,parameters=p,gap=g,selected=selected,bins=w['bins']))
    print(json.dumps(dict(status='COMPLETE_FIXED_CLASS',profiles=len(rows),questions=350,
        failures=failed,results=rows,actual_domain=42,certificates=certificates,
        unresolved_targets=unresolved,budget=budget,controls='PASS',
        cpu_seconds=time.process_time()-start),separators=(',',':')))


if __name__=='__main__':
    try:main()
    except Cap as e:print(json.dumps(dict(status='UNKNOWN_CAP',reason=str(e))))
