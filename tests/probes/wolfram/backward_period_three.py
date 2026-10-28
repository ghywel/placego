#!/usr/bin/env python3
"""GC2023: bounded exact period-three root-diagonal compatibility, dual implementations."""
import hashlib
import json
import os
from pathlib import Path
import backward_diagonal_b as primary
from root_past_tails import rays

DEPTH=128
primary.LO=-DEPTH-2
TRUTH=(0,1,1,1,1,0,0,0)
MAX_NODES=20000
nodes=0
checks=0


def key(row):
    return row.win, row.tail


def separate(child):
    global checks
    result=[]
    for rawtail in rays(child.tail):
        tail=primary.least_block(rawtail)
        win={}
        def cell(i):
            return win[i] if i<=0 else tail[(i-1)%len(tail)]
        for i in range(0,primary.LO-1,-1):
            c,r=cell(i+1),cell(i+2)
            answers=[l for l in (0,1) if TRUTH[4*l+2*c+r]==child.at(i+1)]
            assert len(answers)==1
            win[i]=answers[0]
        row=primary.Row([win[i] for i in range(primary.LO,1)],tail)
        for i in range(primary.LO+1,1+3*len(tail)):
            assert TRUTH[4*row.at(i-1)+2*row.at(i)+row.at(i+1)]==child.at(i)
            checks+=1
        result.append(row)
    return result


def parents(child):
    global nodes
    a=primary.parents(child);b=separate(child)
    assert sorted(map(key,a))==sorted(map(key,b))
    nodes+=len(a)
    assert nodes<=MAX_NODES,'total generated nodes'
    return a


def main():
    root=primary.Row([0]*(-primary.LO)+[1],(0,))
    level=[root];counts=[1]
    for _ in range(3):
        level=[r for c in level for r in parents(c)];counts.append(len(level))
    assert counts==[1,2,5,8]
    results=[]
    # Period two is the retained negative control, not a new question.
    for word,limit in [('10',38),('100',DEPTH),('101',DEPTH),('110',DEPTH)]:
        live=[root];levels=[];failure=None;rejected=[]
        for d in range(1,limit+1):
            candidates=[r for c in live for r in parents(c)]
            required=int(word[d%len(word)])
            nxt=[r for r in candidates if r.at(-d)==required]
            levels.append({'depth':d,'parents':len(candidates),'survivors':len(nxt),
                           'required':required,'tail_periods':sorted({len(r.tail) for r in candidates})})
            assert len(nxt)<=2000,'live cap'
            if not nxt:
                failure=d
                rejected=[{'actual':r.at(-d),'tail':list(r.tail),'window_x0':primary.LO,
                           'window':list(r.win)} for r in candidates]
                break
            live=nxt
        if word=='10':assert failure==38
        results.append({'word_backwards_from_root':word,'first_impossible_depth':failure,
                        'levels':levels,'rejected':rejected})
        print(json.dumps({k:v for k,v in results[-1].items() if k not in ('levels','rejected')}),flush=True)
    out={'depth_cap':DEPTH,'generated_nodes':nodes,'independent_truth_checks':checks,
         'primary_truth_checks':primary.checks,'controls':counts,'results':results,
         'source_sha256':{p:hashlib.sha256(Path(__file__).with_name(p).read_bytes()).hexdigest()
                          for p in ['backward_period_three.py','backward_diagonal_b.py','root_past_tails.py']}}
    (Path(os.environ['CAPPED_OUT'])/'result.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
