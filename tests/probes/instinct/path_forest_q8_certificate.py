#!/usr/bin/env python3
"""B124/MI269 independent literal q8 certificate checker and one-run driver.

No import of the normalized solver, its enumeration or earlier probe helpers.
Actual target generator: eight sorted odd integers69..121 summing784.
Independent multiplicity DP counts those tuples. Match EVERY original target
in order; validate first7/other3 bin sizes, all28 odd tokens, exact sums and
fixed canonical seven-set. Positive stream suffices without trusting search.
Stop first negative/UNKNOWN; first complete negative gets a bounded raw-token
reference search, not a repair. All raw output stays local outside git.
Usage: python3 .../path_forest_q8_certificate.py BINARY OUTPUT_PREFIX
One run only. Primary caps100k/profile,50M total,60CPU/90wall/256MiB;
driver timeout95s, own120CPU/180wall/256MiB; first-negative reference200k/10CPU.
Full preregistration, counterfactual and controls are in MI269.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import hashlib
import json
import resource
import subprocess
import sys
import time


class Cap(RuntimeError):
    pass


START=time.process_time()
WALL=time.monotonic()


def rss_bytes():
    n=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return n if sys.platform=='darwin' else n*1024


def budget():
    if time.process_time()-START>120:raise Cap('checker cpu')
    if time.monotonic()-WALL>180:raise Cap('driver wall')
    if rss_bytes()>256*1024*1024:raise Cap('checker rss')


def actual_targets(prefix=(),remaining=784):
    """Literal original coordinates; no minimum/hole normalization."""
    budget()
    n=8-len(prefix)
    if n==0:
        if remaining==0:yield prefix
        return
    lower=prefix[-1] if prefix else 69
    for x in range(lower,122,2):
        if n*x>remaining:break
        if x+121*(n-1)>=remaining:yield from actual_targets(prefix+(x,),remaining-x)


def multiplicity_count():
    """Coin DP: select8 values0..26 with repetition and sum116."""
    ways=[[0]*117 for _ in range(9)];ways[0][0]=1
    for value in range(27):
        for n in range(1,9):
            for s in range(value,117):ways[n][s]+=ways[n-1][s-value]
    return ways[8][116]


def check_literal(target,bins):
    if len(target)!=8 or tuple(sorted(target))!=tuple(target):return False
    if any(x<69 or x>121 or x%2!=1 for x in target) or sum(target)!=784:return False
    if list(map(len,bins))!=[7]+[3]*7:return False
    if any(sum(b)!=t for b,t in zip(bins,target)):return False
    if Counter(x for b in bins for x in b)!=Counter(range(1,56,2)):return False
    # Independent literal reconstruction of the declared fixed seven-set.
    a=target[0]
    fixed=set(range(1,12,2))|{a-36} if a<93 else set(range(1,10,2))|{55,a-80}
    return set(bins[0])==fixed


def match_target(expected,observed):
    if tuple(expected)!=tuple(observed):raise ValueError('missing/duplicate/out-of-order target')


def reference(pool,targets):
    """Independent raw smallest-token recursion, no triple catalogue/normalization."""
    start=time.process_time();nodes=0
    @lru_cache(None)
    def visit(free,left):
        nonlocal nodes
        nodes+=1
        if nodes>200000 or time.process_time()-start>10:raise Cap('negative reference')
        if not nodes%1024:budget()
        if not left:return not free
        x=free[0]
        for y,z in combinations(range(1,len(free)),2):
            s=x+free[y]+free[z]
            if s not in left:continue
            rest=list(left);rest.remove(s)
            nextfree=tuple(v for i,v in enumerate(free) if i not in (0,y,z))
            if visit(nextfree,tuple(rest)):return True
        return False
    answer=visit(tuple(sorted(pool)),tuple(sorted(targets)))
    return answer,nodes


def controls():
    t=(69,69,69,93,121,121,121,121)
    bins=[[1,3,5,7,9,11,33],[13,15,41],[17,21,31],[19,23,51],
          [25,43,53],[27,39,55],[29,45,47],[35,37,49]]
    assert check_literal(t,bins)
    # Swap tokens between equal targets: inventory survives, sums do not.
    bad=[b[:] for b in bins];bad[1][0],bad[2][0]=bad[2][0],bad[1][0]
    assert not check_literal(t,bad)
    bad=[b[:] for b in bins];bad[1][0]=bad[2][0]
    assert not check_literal(t,bad)
    bad=[b[:] for b in bins];bad[0].append(bad[1].pop())
    assert not check_literal(t,bad)
    # Same count and same total still cannot hide wrong coverage/order.
    other=(69,69,69,95,119,121,121,121)
    for fake_stream in ((other,t),(t,t)):
        try:
            for want,observed in zip((t,other),fake_stream):match_target(want,observed)
        except ValueError:pass
        else:raise AssertionError('same-count coverage guard')
    pool=tuple(range(1,16,2))+(101,1001,10001,100001)
    targets=(111,1011,10023,100023)
    assert all(any(sum(c)==s for c in combinations(pool,3)) for s in targets)
    exists,nodes=reference(pool,targets);assert not exists
    fixed=set(bins[0]);pool=tuple(x for x in range(1,56,2) if x not in fixed)
    exists,posnodes=reference(pool,t[1:]);assert exists
    assert multiplicity_count()==258180
    return dict(literal_positive=True,wrong_sums_rejected=True,
                duplicate_token_rejected=True,wrong_cardinalities_rejected=True,
                wrong_target_identity_rejected=True,raw_global_conflict_nodes=nodes,
                raw_positive_nodes=posnodes,independent_dp_count=258180)


def verify_stream(path,complete):
    expected=actual_targets();count=0;by_min=Counter();last=None
    with path.open() as f:
        assert f.readline()=='# B124 original targets followed by seven buffer tokens and seven triples\n'
        for line in f:
            budget();row=list(map(int,line.split()))
            if len(row)!=36:raise ValueError('wrong certificate width')
            target=tuple(row[:8]);want=next(expected)
            match_target(want,target)
            tokens=row[8:];bins=[tokens[:7]]+[tokens[i:i+3] for i in range(7,28,3)]
            if not check_literal(target,bins):raise ValueError('literal certificate rejected')
            count+=1;by_min[target[0]]+=1;last=target
    next_target=next(expected,None)
    if complete:
        if next_target is not None or count!=multiplicity_count():raise ValueError('incomplete coverage')
    return dict(checked=count,by_minimum=dict(sorted(by_min.items())),last_target=last,next_target=next_target)


def main():
    if len(sys.argv)!=3:raise SystemExit(__doc__)
    binary=Path(sys.argv[1]).resolve();prefix=Path(sys.argv[2]);stream=Path(str(prefix)+'.txt')
    primary=Path(str(prefix)+'.primary.json');report=Path(str(prefix)+'.json')
    if any(p.exists() for p in (stream,primary,report)):raise SystemExit('refuse overwrite/restart')
    out={'status':'ERROR'}
    try:
        out['controls']=controls();budget()
        with stream.open('x') as f,primary.open('x') as err:
            proc=subprocess.run([str(binary)],stdout=f,stderr=err,timeout=95,check=False)
        out['primary']=json.loads(primary.read_text());p=out['primary']
        if (proc.returncode==0)!=(p['status']=='COMPLETE'):raise ValueError('primary exit/status disagreement')
        complete=proc.returncode==0 and p['status']=='COMPLETE'
        out['verification']=verify_stream(stream,complete)
        if out['verification']['checked']!=p['count']:raise ValueError('primary/checker count mismatch')
        if p['status']=='FIRST_CANONICAL_NO_WITNESS':
            t=tuple(p['pending_target']);match_target(out['verification']['next_target'],t)
            a=t[0];fixed=set(range(1,12,2))|{a-36} if a<93 else set(range(1,10,2))|{55,a-80}
            exists,nodes=reference(tuple(x for x in range(1,56,2) if x not in fixed),t[1:])
            out['negative_reference']={'exists':exists,'nodes':nodes}
            out['status']='COUNTEREXAMPLE_CANONICAL' if not exists else 'ENGINE_DISAGREEMENT'
        elif complete:out['status']='COMPLETE_LITERAL_CERTIFICATE'
        else:out['status']=p['status']
    except (Cap,subprocess.TimeoutExpired) as e:out.update(status='UNKNOWN_CAP',reason=str(e))
    except Exception as e:out.update(status='ERROR',reason=type(e).__name__+': '+str(e))
    out.update(cpu_seconds=time.process_time()-START,wall_seconds=time.monotonic()-WALL,peak_rss_bytes=rss_bytes())
    for label,path in (('stream',stream),('primary_report',primary)):
        if path.exists():
            # Chunked digest keeps the checker independent of stream size in memory.
            digest=hashlib.sha256();size=0
            with path.open('rb') as f:
                for chunk in iter(lambda:f.read(1024*1024),b''):digest.update(chunk);size+=len(chunk)
            out[label]={'name':path.name,'bytes':size,'sha256':digest.hexdigest()}
    report.write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps(out,sort_keys=True,separators=(',',':')))
    return 0 if out['status']=='COMPLETE_LITERAL_CERTIFICATE' else 2


if __name__=='__main__':raise SystemExit(main())
