#!/usr/bin/env python3
"""GC2569: fixed root-to-(19,10) forcing trace, not a solver/census.
Only sound one-step masking and the carried a10 two-step identity are used.
Inputs: existing background JSON and saved path JSON (root only is read).
Artifacts go to CAPPED_OUT; no subprocess or symbolic-algebra engine.
"""
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource
import sys

H, TARGET = 19, 10
BG_SHA = '528b5760a6d9c4b9d709512b6ba1e45ffecfe57a3ea987cc447ca69c9a94075b'
ROOT_SHA = '30dee77c511774708e64873b7272df4a4a31a8408ed53b110a8eab0cb81b2ece'


def inside(t, x):
    return 0 <= t <= H and abs(x - TARGET) <= H - t


def derive(initial, two_step):
    facts = {(0, x): {'value': v, 'rule': 'initial', 'parents': []}
             for x, v in initial.items()}
    def add(t, x, value, rule, parents):
        assert inside(t, x)
        n = {'value': value, 'rule': rule, 'parents': parents}
        if (t, x) in facts:
            assert facts[t, x]['value'] == value, 'CONTRADICTORY_DERIVATIONS'
        else:
            facts[t, x] = n
    for t in range(H):
        row = {x: n['value'] for (tt, x), n in facts.items() if tt == t}
        for x in range(TARGET - H + t + 1, TARGET + H - t):
            if x - 1 in row:
                a = row[x - 1]
                if row.get(x) == 1:
                    add(t+1,x,1-a,'gate',[(t,x-1),(t,x)])
                elif row.get(x+1) == 1:
                    add(t+1,x,1-a,'gate',[(t,x-1),(t,x+1)])
                elif row.get(x) == 0 and row.get(x+1) == 0:
                    add(t+1,x,a,'gate',[(t,x-1),(t,x),(t,x+1)])
        if two_step and t+2 <= H:
            for x in range(TARGET-H+t+2,TARGET+H-t-1):
                if x-2 in row and row.get(x-1) == 1 and row.get(x) == 0:
                    add(t+2,x,row[x-2],'a10',[(t,x-2),(t,x-1),(t,x)])
    return facts


def closure(facts, key):
    needed = set()
    def visit(k):
        if k in needed:
            return
        needed.add(k)
        for p in facts[k]['parents']:
            visit(p)
    if key in facts:
        visit(key)
    return [{'t':t,'x':x,**facts[t,x]} for t,x in sorted(needed)]


def verify(nodes, initial):
    """Independent local truth-table checker, recomputing any unused parents.
    No reliance on the extractor's masking or a10 formulas.
    """
    checked = {}
    table = (0,1,1,1,1,0,0,0)
    def step3(a,b,c):
        return table[4*a+2*b+c]
    for n in nodes:
        t,x,v = n['t'],n['x'],n['value']
        assert inside(t,x) and (t,x) not in checked and v in (0,1)
        parents = [tuple(p) for p in n['parents']]
        assert all(p in checked for p in parents)
        if n['rule'] == 'initial':
            assert t == 0 and not parents and initial[x] == v
        elif n['rule'] in ('gate','a10'):
            dt = 1 if n['rule'] == 'gate' else 2
            positions = list(range(x-dt,x+dt+1))
            assert all(pt == t-dt and px in positions for pt,px in parents)
            fixed = {px:checked[pt,px] for pt,px in parents}
            missing = [px for px in positions if px not in fixed]
            values = set()
            for bits in itertools.product((0,1),repeat=len(missing)):
                row = {**fixed,**dict(zip(missing,bits))}
                for _ in range(dt):
                    row = {j:step3(row[j-1],row[j],row[j+1])
                           for j in range(min(row)+1,max(row))}
                values.add(row[x])
            assert values == {v}, ('BAD_LOCAL_IMPLICATION',t,x,values,v)
        else:
            raise AssertionError('UNKNOWN_RULE')
        checked[t,x] = v
    return checked


def main():
    os.nice(10)
    resource.setrlimit(resource.RLIMIT_CPU,(3,3))
    out=Path(os.environ['CAPPED_OUT'])
    paths=list(map(Path,sys.argv[1:]));assert len(paths)==2
    for p,want in zip(paths,(BG_SHA,ROOT_SHA)):
        assert hashlib.sha256(p.read_bytes()).hexdigest()==want
    data,root=(json.loads(p.read_text()) for p in paths)
    assert root['start']==[39,0,'0011011100111010']
    assert data['N']==7 and data['r']==0 and data['s']==4 and len(data['orb'])==63
    strip=list(map(int,root['start'][2]))
    initial={x:(data['orb'][43][(-x)%7] if x<=0 else strip[x-1])
             for x in range(TARGET-H,17)}
    basic=derive(initial,False);extended=derive(initial,True)
    nodes=closure(extended,(H,TARGET))
    checked=verify(nodes,initial)
    assert not derive({},True), 'EMPTY_ROOT_CONTROL'
    mutation='not applicable: target not derived'
    if nodes:
        bad=[dict(n) for n in nodes];bad[-1]['value']^=1
        try:
            verify(bad,initial)
        except AssertionError:
            mutation='rejected'
        else:
            raise AssertionError('MUTATED_CONCLUSION_ACCEPTED')
    result={'status':'COMPLETED','question':[H,TARGET],'initial':initial,
            'ordinary_target':basic.get((H,TARGET)),
            'a10_target':extended.get((H,TARGET)),
            'prediction_target_black':checked.get((H,TARGET))==1,
            'known_cells_ordinary':len(basic),'known_cells_with_a10':len(extended),
            'proof_nodes':len(nodes),'a10_proof_nodes':sum(n['rule']=='a10' for n in nodes),
            'mutation_control':mutation,'empty_root_control':'PASS',
            'cpu_self_s':resource.getrusage(resource.RUSAGE_SELF).ru_utime+resource.getrusage(resource.RUSAGE_SELF).ru_stime,
            'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    (out/'trace.json').write_text(json.dumps(nodes,indent=2)+'\n')
    (out/'known.json').write_text(json.dumps([{'t':t,'x':x,**n} for (t,x),n in sorted(extended.items())],indent=2)+'\n')
    (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
