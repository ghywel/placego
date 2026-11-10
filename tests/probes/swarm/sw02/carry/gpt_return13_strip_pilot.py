#!/usr/bin/env python3
"""GC2855: fixed P7 control / P13 strip-SAT feasibility, not a pair-graph census.
Prediction and all limits are in gpt_return13_strip_plan.json; no proof-export claim.
"""
import ast
import hashlib
import itertools
import json
import os
from pathlib import Path
import random
import re
import resource
import time
from pysat.solvers import Cadical195

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(os.environ['CAPPED_OUT'])
KIT = Path(os.environ['K09B_KIT_ROOT'])
PLAN = json.loads((ROOT/'tests/probes/swarm/sw02/carry/gpt_return13_strip_plan.json').read_text())
for name, sha in PLAN['kit_sources_sha256'].items():
    assert hashlib.sha256((KIT/name).read_bytes()).hexdigest() == sha, name
START_CPU = time.process_time()
START_WALL = time.monotonic()
RESULT = {'status': 'RUNNING', 'controls': {}, 'target': {}}

def save():
    RESULT['cpu_s'] = time.process_time()-START_CPU
    RESULT['wall_s'] = time.monotonic()-START_WALL
    (OUT/'strip-pilot.json').write_text(json.dumps(RESULT, indent=2)+'\n')

def stop():
    return (time.process_time()-START_CPU >= 85 or time.monotonic()-START_WALL >= 230)

def six(a,b,c,d):
    return [[-b,a,d],[-b,-a,-d],[-c,a,d],[-c,-a,-d],[b,c,-a,d],[b,c,a,-d]]

# Independent truth-table check of this exact six-clause presentation.
for vals in itertools.product((False,True), repeat=4):
    sat = all(any(vals[abs(l)-1] == (l>0) for l in c) for c in six(1,2,3,4))
    left,center,right,out = vals
    truth = bool((30 >> (4*left+2*center+right)) & 1)
    assert sat == (out == truth), ('TRUTH_TABLE',vals)

def formula(p,q,cols,skip=None):
    var = lambda t,i: q*t+i+1
    cs = [c for t in range(p) for i in range(q-2)
          for c in six(var(t,i),var(t,i+1),var(t,i+2),var(t+1,i))]
    for i in range(cols):
        if i != skip:
            cs += [[-var(p,i),var(0,i)],[var(p,i),-var(0,i)]]
    return cs

def block(word,offset,w):
    return [-(offset+j+1) if (word>>j)&1 else offset+j+1 for j in range(w)]

def validate(model,p,q,cols,skip=None):
    values = {abs(x): x>0 for x in model}
    row = lambda t,i: int(values[q*t+i+1])
    for t in range(p):
        for i in range(q-2):
            want = (30 >> (4*row(t,i)+2*row(t,i+1)+row(t,i+2))) & 1
            assert row(t+1,i) == want, ('BAD_LITERAL_RULE',t,i)
    for i in range(cols):
        if i != skip:
            assert row(p,i) == row(0,i), ('BAD_PERIOD',i)
    return [row(0,i) for i in range(q)]

def solve_projection(p,q,cols,offset,w,limit):
    cs = formula(p,q,cols)
    words=[]
    with Cadical195(bootstrap_with=cs) as solver:
        while True:
            if stop():return words,False,'WORKER_STAGE_STOP'
            solver.conf_budget(500000)
            ans=solver.solve_limited()
            if ans is None:return words,False,'CONFLICT_BUDGET'
            if not ans:return sorted(words),True,'COMPLETE'
            model=solver.get_model();row=validate(model,p,q,cols)
            word=sum(row[offset+j]<<j for j in range(w))
            assert word not in words
            words.append(word);solver.add_clause(block(word,offset,w))
            RESULT['target'].update({'words':words,'seen':len(words)})
            save()
            if len(words)>=limit:return sorted(words),False,'MODEL_COUNT_STOP'

def graph(words,w):
    mask=(1<<(w-1))-1
    edges=[[u for u in words if v//2 == (u&mask)] for v in words]
    degrees=[len(e) for e in edges]
    return {'vertices':len(words),'edges':sum(degrees),'outdegrees':{str(d):degrees.count(d) for d in sorted(set(degrees))},
            'unit_constant_potential':all(d<=1 for d in degrees),
            'base':[1]*len(words),'slope':[0]*len(words) if all(d<=1 for d in degrees) else None}

try:
    control=(KIT/'lean/Ruliology/CellularAutomata/Rule30Certificates/MovingReturn07.lean').read_text()
    expected=ast.literal_eval(re.search(r'def states : List Nat := (\[[^\n]+\])',control)[1])
    words,complete,why=solve_projection(7,35,35,6,6,64)
    assert complete and words==expected, ('P7_CONTROL',complete,why,words)
    RESULT['controls']['p7_exact_words']=words
    # Deleting one block-list entry must expose that omitted genuine control word.
    omitted=expected[len(expected)//2]
    with Cadical195(bootstrap_with=formula(7,35,35)+[block(s,6,6) for s in words if s!=omitted]) as solver:
        assert solver.solve(), 'OMITTED_WORD_NOT_SAT'
        row=validate(solver.get_model(),7,35,35)
        assert sum(row[6+j]<<j for j in range(6))==omitted
    RESULT['controls']['omitted_word_sat']=omitted
    # Fixed chaos intervention: release one randomly selected spatial period equality pair.
    chosen=random.Random(20261110).randrange(35)
    with Cadical195(bootstrap_with=formula(7,35,35,chosen)+[block(s,6,6) for s in words]) as solver:
        solver.conf_budget(500000);answer=solver.solve_limited()
        rec={'removed_column':chosen,'expected':'UNSAT','actual':'UNKNOWN' if answer is None else ('SAT' if answer else 'UNSAT')}
        if answer:
            row=validate(solver.get_model(),7,35,35,chosen)
            rec['new_word']=sum(row[6+j]<<j for j in range(6));rec['row0']=row
        RESULT['controls']['chaos_period_equality']=rec
    RESULT['target']={'p':13,'q':65,'cols':65,'offset':6,'w':16}
    save()
    words,complete,why=solve_projection(13,65,65,6,16,512)
    RESULT['target'].update({'words':words,'complete':complete,'reason':why,'seen':len(words)})
    if complete:
        RESULT['target']['overlap']=graph(words,16)
        final=formula(13,65,65)+[block(s,6,16) for s in words]
        data='p cnf 910 %d\n'%len(final)+''.join(' '.join(map(str,c))+' 0\n' for c in final)
        (OUT/'period13-final.cnf').write_text(data)
        RESULT['target']['final_cnf_sha256']=hashlib.sha256(data.encode()).hexdigest()
        RESULT['target']['proof_exported']=False
    RESULT['status']='COMPLETE' if complete else 'BOUNDED_UNKNOWN'
    save()
    print('RETURN13_STRIP_PILOT_RECORDED')
    print(json.dumps({k:v for k,v in RESULT.items() if k!='target'}))
    print('TARGET',json.dumps({k:v for k,v in RESULT['target'].items() if k!='words'}))
finally:
    save()
