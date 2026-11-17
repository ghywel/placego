#!/usr/bin/env python3
"""Rebase the checked guard to a 35-tick physical cone; no SAT search."""
import argparse
import json
import os
from pathlib import Path
from pysat.solvers import Minisat22
import physical_47 as phys
import physical_ancestry as anc


def replay(C,P):
    with Minisat22(bootstrap_with=C) as s:
        assert s.propagate()[0]
        for i,cl in enumerate(P):
            if s.propagate(assumptions=[-v for v in cl])[0]:return False,i
            s.add_clause(cl)
    return True,len(P)


def main():
    p=argparse.ArgumentParser();p.add_argument('phase');p.add_argument('--out',type=Path,required=True)
    p.add_argument('--audit',type=Path);p.add_argument('--case');p.add_argument('--kind');p.add_argument('--binary')
    a=p.parse_args();o=a.out;o.mkdir(parents=True,exist_ok=True)
    if a.phase=='native':
        d=json.loads((o/'result.json').read_text())['cases'][a.case]
        if not d['RUP_pass']:print('NO_EXPORTED_PROOF',a.case);return
        if a.kind=='drat':args=[a.binary,str(o/(a.case+'.cnf')),str(o/(a.case+'.drup')),'-U','-L',str(o/(a.case+'.lrat'))]
        else:args=[a.binary,'--CML_HEAP_SIZE=512','--CML_STACK_SIZE=64',str(o/(a.case+'.cnf')),str(o/(a.case+'.lrat'))]
        os.execv(a.binary,args)
    if a.phase=='check':
        d=json.loads((o/'result.json').read_text());assert d['cases']['word']['RUP_pass']
        for name,rec in d['cases'].items():
            drat=(o.parent/(name+'-drat.stdout')).read_text();cake=(o.parent/(name+'-cake.stdout')).read_text()
            if rec['RUP_pass']:assert 's VERIFIED' in drat and 's VERIFIED UNSAT' in cake
            else:assert 'NO_EXPORTED_PROOF' in drat and 'NO_EXPORTED_PROOF' in cake
        print('ALL_COMPACT_GUARD_CHECKS_PASS');return
    assert a.phase=='build'
    wanted=anc.word_heads('25253',1)
    C,off,W=phys.generate(35,wanted);N=off[-1];G=[off[23]+p for p in (6,7,8)]
    _,oldoff,oldW=phys.generate(193,anc.word_heads(phys.E+phys.A*4+phys.E,1))
    m={1:1}
    for t in range(96,132):
        for x in range(1,W-(t-96)+1):m[oldoff[t]+x]=off[t-96]+x
    P=[]
    for line in (a.audit/'trimmed-prefix.drup').read_text().splitlines():
        cl=list(map(int,line.split()));assert cl[-1]==0
        assert all(abs(v) in m for v in cl[:-1]),'proof variable outside compact cone'
        P.append([m[abs(v)]*(1 if v>0 else -1) for v in cl[:-1]])
    assert P[-1]==G
    # Every supported initial physical clause must be one of this cone's clauses.
    src,_,_=phys.generate(193,anc.word_heads(phys.E+phys.A*4+phys.E,1))
    support=json.loads((a.audit/'support.json').read_text())
    canon=lambda c:tuple(sorted(set(c)))
    cs={canon(c) for c in C}
    for i in support['initial_clause_ids']:
        if i<=len(src):
            cl=src[i-1];assert all(abs(v) in m for v in cl)
            assert canon([m[abs(v)]*(1 if v>0 else -1) for v in cl]) in cs
    core=json.loads((a.audit/'greedy-head-core.json').read_text())['heads']
    sparse={x['t']-96:x['bit'] for x in core}
    S,_,_=phys.generate(35,sparse)
    cases={}
    for name,base in (('word',C),('sparse',S)):
        ok,count=replay(base,P);cases[name]={'RUP_pass':ok,'checked':count,'heads':wanted if name=='word' else sparse}
        phys.dimacs(o/(name+'.cnf'),base+[[-v] for v in G],N)
        if ok:
            with (o/(name+'.drup')).open('w') as f:
                for cl in P:f.write(' '.join(map(str,cl))+' 0\n')
                f.write('0\n')
    assert cases['word']['RUP_pass']
    # Reuse the already checked two-A fixture, shifted from odd1 to even2.
    old_odd=26468218944
    root=anc.step(old_odd,0);rr=anc.rows(root,35)
    assert root.bit_length()<=36 and rr==phys.scalar_rows(root,35,36)
    assert all((rr[t]&1)==bit for t,bit in wanted.items())
    vals={1:True}
    for t in range(36):
        vals.update({off[t]+x:bool(rr[t]>>(x-1)&1) for x in range(1,W-t+1)})
    assert all(any(vals[abs(v)]==(v>0) for v in cl) for cl in C)
    patch=[rr[23]>>(x-1)&1 for x in range(6,11)];assert any(patch[:3])
    result={'shift':96,'height':35,'root_width':36,'word':'25253','goal_time':23,'goal_columns':[6,7,8],
            'goal_variables':G,'cases':cases,'same_52_lemma_prefix':len(P)==52,'no_auxiliary_variables':True,
            'nonvacuity':{'old_odd_fixture':str(old_odd),'root':str(root),'all_word_case_clauses':True,
                          'all_cells_and_scalar':True,'patch_at23':patch,'rows_hex':[hex(x) for x in rr]},
            'not_a_minimal_semantic_premise':True,'no_solve_calls':True}
    (o/'result.json').write_text(json.dumps(result,indent=2)+'\n');print('COMPACT_GUARD_BUILD_PASS',json.dumps({k:v for k,v in result.items() if k!='nonvacuity'}))


if __name__=='__main__':main()
