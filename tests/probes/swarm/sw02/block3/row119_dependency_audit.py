#!/usr/bin/env python3
"""Audit a checked proof's dependencies, never invoking a SAT search."""
import argparse
import hashlib
import json
from pathlib import Path
from pysat.solvers import Minisat22
import physical_47 as phys
import physical_ancestry as anc


def save(path,x):path.write_text(json.dumps(x,indent=2)+'\n')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def read_cnf(path):
    n=None;C=[]
    for line in path.read_text().splitlines():
        if line.startswith('p '):n=int(line.split()[2]);continue
        if not line.strip() or line.startswith('c'):continue
        v=list(map(int,line.split()));assert v[-1]==0;C.append(v[:-1])
    return n,C


def replay(C,proof):
    with Minisat22(bootstrap_with=C) as s:
        consistent=s.propagate()[0]
        for i,cl in enumerate(proof):
            ok,_=s.propagate(assumptions=[-x for x in cl])
            if ok:return {'passed':False,'checked':i,'first_failed':i+1,'base_UP_consistent':consistent}
            s.add_clause(cl)
    return {'passed':True,'checked':len(proof),'base_UP_consistent':consistent}


def audit(a):
    o=a.out;o.mkdir(parents=True,exist_ok=True)
    wanted=anc.word_heads(phys.E+phys.A*4+phys.E,1)
    C,off,W=phys.generate(193,wanted);N=off[-1]
    G=[off[119]+p for p in (6,7,8)];neg=[[-x] for x in G]
    _,old=read_cnf(a.case);assert old==C+neg
    # Label each original clause without changing any original ID.
    meta={1:{'kind':'constant'}};ix=1
    for t in range(193):
        for p in range(1,W-t):
            for slot in range(6):
                ix+=1;meta[ix]={'kind':'gate','t':t,'p':p,'slot':slot}
    heads={}
    for t,b in sorted(wanted.items()):
        ix+=1;assert C[ix-1]==[off[t]+1 if b else -off[t]-1]
        meta[ix]={'kind':'head','t':t,'bit':int(b)};heads[t]=ix
    assert ix==len(C)
    for i,cl in enumerate(neg,len(C)+1):meta[i]={'kind':'negative_goal','clause':cl}
    nodes={};order=[];last=None
    for line in a.lrat.read_text().splitlines():
        words=line.split()
        if not words or words[0]=='c' or words[1]=='d':continue
        v=list(map(int,words));z=v.index(0,1);cid=v[0]
        assert cid>len(old) and cid not in nodes
        nodes[cid]=(v[1:z],v[z+1:-1]);order.append(cid)
        if not v[1:z]:last=cid
    assert last is not None
    used=set();todo=[last]
    while todo:
        cid=todo.pop()
        if cid in used:continue
        used.add(cid)
        if cid>len(old):
            cl,hints=nodes[cid];assert all(x>0 for x in hints),'non-RUP dependency'
            todo.extend(hints)
    initial=sorted(x for x in used if x<=len(old))
    kept=[i for i in order if i in used]
    proof=[list(dict.fromkeys(nodes[i][0]+G)) for i in kept]
    assert proof[-1]==G
    with (o/'trimmed-prefix.drup').open('w') as f:
        for cl in proof:f.write(' '.join(map(str,cl))+' 0\n')
    baseline=replay(C,proof);assert baseline['passed'] and baseline['base_UP_consistent']
    assert not replay(C,[[]])['passed'],'malformed empty proof accepted'
    hs=[meta[i] for i in initial if meta[i]['kind']=='head']
    gs=[meta[i] for i in initial if meta[i]['kind']=='gate']
    support={'initial_clause_ids':initial,'lemma_ids':kept,'heads':hs,
             'gate_clauses':len(gs),'gate_cells':len({(x['t'],x['p']) for x in gs}),
             'input_time_bounds':[min(x['t'] for x in gs),max(x['t'] for x in gs)],
             'boundary_input_times':sorted({x['t'] for x in gs if x['p']==1}),
             'lemma_count':len(proof),'original_case_sha256':sha(a.case),'source_lrat_sha256':sha(a.lrat)}
    save(o/'support.json',support)
    # Single removals refer to this fixed pruned derivation, not logical necessity.
    singles=[]
    for t,cid in heads.items():singles.append({'removed_head':t,'bit':wanted[t],**replay([cl for i,cl in enumerate(C,1) if i!=cid],proof)})
    save(o/'single-head-deletions.json',singles)
    physics=[cl for i,cl in enumerate(C,1) if meta[i]['kind']!='head']
    current={x['t'] for x in hs};assert replay(physics+[C[heads[t]-1] for t in sorted(current)],proof)['passed']
    greedy=[]
    for t in sorted(current.copy()):
        candidate=current-{t};rr=replay(physics+[C[heads[u]-1] for u in sorted(candidate)],proof)
        greedy.append({'attempted_remove':t,**rr})
        if rr['passed']:current=candidate
    save(o/'greedy-head-core.json',{'heads':[{'t':t,'bit':wanted[t]} for t in sorted(current)],'attempts':greedy,'scope':'inclusion-minimal for this fixed RUP derivation and chronological removal order'})
    group=[]
    for cut in (69,97,111):group.append({'drop_heads_before':cut,**replay([cl for i,cl in enumerate(C,1) if meta[i]['kind']!='head' or meta[i]['t']>=cut],proof)})
    cuts=[];cut_formulas={}
    for cut in (0,68,82,96,108):
        cc=[cl for i,cl in enumerate(C,1) if meta[i]['kind']=='constant' or meta[i]['t']>=cut]
        cut_formulas[cut]=cc;cuts.append({'start_tick':cut,**replay(cc,proof)})
    # Existing physical suffix is a genuine countermodel to the cut108 goal.
    history=next(x['witness'] for x in json.loads(a.histories.read_text()) if x.get('word')==14429)
    rr=anc.rows(int(history['root']),85)
    assert rr==[int(x,16) for x in history['rows_hex']]
    assert rr==phys.scalar_rows(int(history['root']),85,86)
    values={1:True}
    for t in range(108,194):
        for p in range(1,W-t+1):values[off[t]+p]=bool(rr[t-108]>>(p-1)&1)
    assert all(any(values[abs(l)]==(l>0) for l in cl) for cl in cut_formulas[108]+neg)
    assert not cuts[-1]['passed'],'proof accepted despite checked actual cut108 countermodel'
    boundaries=[]
    for lo,hi in ((0,67),(68,81),(82,95),(96,107),(108,118),(119,192)):
        cc=[cl for i,cl in enumerate(C,1) if not(meta[i]['kind']=='gate' and meta[i]['p']==1 and lo<=meta[i]['t']<=hi)]
        boundaries.append({'free_drive_input_times':[lo,hi],**replay(cc,proof)})
    save(o/'group-and-time-deletions.json',{'head_groups':group,'time_cuts':cuts,'boundary_groups':boundaries,'cut108_actual_countermodel':'old full-E14429','failed_replay_is_not_logical_necessity':True})
    best=max(x['start_tick'] for x in cuts if x['passed'])
    cases={'headcore':physics+[C[heads[t]-1] for t in sorted(current)],
           'late':cut_formulas[best],
           'kernel':[old[i-1] for i in initial if i<=len(C)]}
    for name,base in cases.items():
        assert replay(base,proof)['passed']
        phys.dimacs(o/(name+'.cnf'),base+neg,N)
        with (o/(name+'.drup')).open('w') as f:
            for cl in proof:f.write(' '.join(map(str,cl))+' 0\n')
            f.write('0\n')
    result={'goal_193_variables':G,'baseline':baseline,'support_heads':hs,
            'greedy_head_core':[{'t':t,'bit':wanted[t]} for t in sorted(current)],
            'single_head_deletions_breaking_this_proof':[x['removed_head'] for x in singles if not x['passed']],
            'latest_checked_sufficient_start':best,'time_cuts':cuts,'boundary_groups':boundaries,
            'three_native_cases':list(cases),'cut108_actual_countermodel_verified':True,
            'no_solve_calls':True,'existence_of_full_past_not_proved':True}
    save(o/'result.json',result)
    print('DEPENDENCY_AUDIT_PASS',json.dumps(result))


def main():
    p=argparse.ArgumentParser();p.add_argument('phase');p.add_argument('--out',type=Path,required=True)
    p.add_argument('--case',type=Path);p.add_argument('--lrat',type=Path);p.add_argument('--histories',type=Path)
    a=p.parse_args()
    if a.phase=='audit':audit(a)
    elif a.phase=='check':
        for name in ('headcore','late','kernel'):
            assert 's VERIFIED UNSAT' in (a.out.parent/(name+'-cake.stdout')).read_text()
            assert 's VERIFIED' in (a.out.parent/(name+'-drat.stdout')).read_text()
        print('ALL_NATIVE_DEPENDENCY_CASES_PASS')
    else:raise ValueError(a.phase)


if __name__=='__main__':main()
