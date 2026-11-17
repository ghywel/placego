#!/usr/bin/env python3
"""B227 / MI434: frozen smallest strict-triple child diagnostic.

COMMAND: python3 tests/probes/instinct/ss3_triple_child.py OUTDIR
RUN-ON: CPU, standard library. Raw data outside git.
Prediction: all admitted children in the twenty listed two-hole pools partition.
Counterfactuals: MI350 and its reflection fail; weak-cut fixture fails but
is excluded by the strict gate. Complete combination/owner maps, literal
witnesses, reflection and original 14/30-cut lift controls are compulsory.
Stop at first missing admitted child, any control failure, 20 wall seconds,
10 CPU seconds or 2 million recursion nodes. No retry or automatic expansion.
"""
import hashlib
import itertools as it
import json
from pathlib import Path
import sys
import time

START=time.monotonic(); CPU=time.process_time()
COUNTS=dict(nodes=0,combination_leaves=0,owner_leaves=0,pools=0,
            targets=0,oriented_lifts=0,reflection_maps=0)

def guard():
    if time.monotonic()-START>20 or time.process_time()-CPU>10 or COUNTS['nodes']>2000000:
        raise TimeoutError('fixed time/node cap')

def L(r): return r*(r-1)//2

def combinations_map(pool):
    out={}; count=0
    for A in it.combinations(pool,3):
        rest=tuple(x for x in pool if x not in A)
        for B in it.combinations(rest,3):
            C=tuple(x for x in rest if x not in B)
            witness=(A,B,C); key=tuple(map(sum,witness))
            assert sorted(x for block in witness for x in block)==list(pool)
            assert all(len(block)==3 for block in witness)
            out.setdefault(key,witness); count+=1
        guard()
    assert count==1680
    COUNTS['combination_leaves']+=count
    return out

def owner_map(pool):
    out=set(); bins=[[],[],[]]; sums=[0,0,0]; count=0
    def visit(i):
        nonlocal count
        COUNTS['nodes']+=1
        if COUNTS['nodes']%4096==0: guard()
        if i==len(pool):
            assert all(len(b)==3 for b in bins)
            out.add(tuple(sums)); count+=1; return
        for j in range(3):
            if len(bins[j])<3:
                bins[j].append(pool[i]); sums[j]+=pool[i]
                visit(i+1)
                sums[j]-=pool[i]; bins[j].pop()
    visit(0)
    assert count==1680
    COUNTS['owner_leaves']+=count
    return out

def checked(pool):
    pool=tuple(sorted(pool)); cm=combinations_map(pool)
    assert set(cm)==owner_map(pool),('whole maps disagree',pool)
    return cm

def parent_gate(H,Q,v):
    # a=3,m=9,n=12; original missing q=10-Q.
    q=10-Q; h=H+Q-10
    u=(33-H,)+tuple(30-x for x in v)
    assert sum(u)==78-q
    deltas={mask:sum(u[i] for i in range(4) if mask>>i&1)-L(3*mask.bit_count())-3*mask.bit_count()
            for mask in range(1,15)}
    assert deltas[14]==h
    assert all(value>h for mask,value in deltas.items() if mask!=14),(H,Q,v,deltas)
    assert min(deltas.values())>=0
    # Actual full-five-bin lift, l=2,k=0, first bin {0,1,q+2}.
    full=(q+3,)+tuple(x+6 for x in u)
    assert sum(full)==105
    slacks=[sum(full[i] for i in range(5) if mask>>i&1)-L(3*mask.bit_count())
            for mask in range(1,31)]
    assert min(slacks)==q and slacks[0]==q
    COUNTS['oriented_lifts']+=1
    return q,u,full

def parent_witness(q,u):
    pool=tuple(x for x in range(13) if x!=q)
    for A in it.combinations(pool,3):
        if sum(A)!=u[0]: continue
        rest=tuple(x for x in pool if x not in A)
        cm=combinations_map(rest)
        if u[1:] in cm:
            witness=(A,)+cm[u[1:]]
            assert tuple(map(sum,witness))==u
            assert sorted(x for b in witness for x in b)==list(pool)
            return witness
    return None

def main(outdir):
    outdir.mkdir(parents=True,exist_ok=False)
    rows=[]; result='COMPLETE-PASS'; negative=None
    try:
        # Known impossible individually feasible target; reflection independent.
        for holes,target in [((1,4),(12,12,26)),((6,9),(18,18,4)),((2,8),(6,15,24))]:
            pool=tuple(x for x in range(11) if x not in holes)
            cm=checked(pool)
            assert target not in cm,('negative became positive',holes,target)
            assert all(t in {sum(A) for A in it.combinations(pool,3)} for t in target)
        # The weak-margin negative is outside the strict gate, not a new failure.
        assert min(6,15,24)<7 and 6+15<22
        assert (7,19,19) in checked(x for x in range(11) if x not in (1,9))
        # Full interval control: reviewed three-bin rank sufficiency.
        cm=checked(range(9))
        for x in range(3,22):
            for y in range(3,22):
                z=36-x-y
                if 3<=z<=21 and min(x+y,x+z,y+z)>=15:
                    assert (x,y,z) in cm
        pools=[(H,Q) for H,Q in it.combinations(range(1,10),2) if H+Q>=10]
        assert len(pools)==20
        for H,Q in pools:
            pool=tuple(x for x in range(11) if x not in (H,Q)); cm=checked(pool)
            reflected=combinations_map(tuple(sorted(10-x for x in pool)))
            assert {tuple(30-v for v in key) for key in cm}==set(reflected)
            COUNTS['reflection_maps']+=1; COUNTS['pools']+=1
            total=sum(pool)
            for x in range(7,total//3+1):
                for y in range(x,(total-x)//2+1):
                    z=total-x-y
                    if x+y<22: continue
                    v=(x,y,z); COUNTS['targets']+=1
                    gates=[parent_gate(H,Q,v),parent_gate(Q,H,v)]
                    if v not in cm:
                        result='CHILD-CONJECTURE-REFUTED'
                        negative=dict(holes=(H,Q),targets=v,parents=[])
                        for q,u,full in gates:
                            witness=parent_witness(q,u)
                            negative['parents'].append(dict(hole=q,targets=u,full_targets=full,
                                witness=witness,status='POSITIVE' if witness else 'ONE-ENGINE-NEGATIVE-UNVERIFIED'))
                        raise StopIteration
                    rows.append(dict(holes=(H,Q),targets=v,witness=cm[v]))
                    guard()
    except StopIteration:
        pass
    except TimeoutError as e:
        result='PARTIAL-CAP'; negative=dict(error=str(e))
    except AssertionError as e:
        result='INSTRUMENT-FAILED'; negative=dict(error=repr(e))
    raw=json.dumps(rows,sort_keys=True,separators=(',',':')).encode()
    (outdir/'witnesses.json').write_bytes(raw)
    summary=dict(status=result,counts=COUNTS,negative=negative,
        raw_sha256=hashlib.sha256(raw).hexdigest(),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        wall_seconds=time.monotonic()-START,cpu_seconds=time.process_time()-CPU)
    (outdir/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main(Path(sys.argv[1]))
