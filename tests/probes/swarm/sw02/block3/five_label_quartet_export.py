#!/usr/bin/env python3
"""Certify/export the quartet suggested by complete five-label causal fibres.

One fixed 57-tick head subcone already present in the original 193/359 cases.
No full-return solve. Native solver/checkers run as separate capped processes.
"""
import argparse,json
from pathlib import Path
from pysat.solvers import Minisat22
import physical_47 as phys
import physical_ancestry as anc


def read_clauses(path):
    out=[]
    for line in path.read_text().splitlines():
        if not line.strip() or line.startswith(('p','c','d')):continue
        vals=list(map(int,line.split()));assert vals[-1]==0;out.append(vals[:-1])
    return out


def prepare(out):
    out.mkdir(parents=True,exist_ok=True)
    heads=anc.word_heads('25253353',1);assert max(heads)==57
    C,off,W=phys.generate(57,heads)
    G=[off[23]+p if bit else -off[23]-p for p,bit in [(6,1),(7,1),(8,0),(9,1)]]
    phys.dimacs(out/'quartet.cnf',C+[[-g for g in G]],off[-1])
    full,fo,fw=phys.generate(359,anc.word_heads(phys.E+phys.A*4+phys.E+phys.A*7+phys.E,1))
    info=phys.dimacs(out/'original.cnf',full,fo[-1]);assert info['sha256']=='21b425011ebc816994a2dfe221539ca2da6a5900b23d1f7009c9bbe26d70426c'
    original={tuple(cl) for cl in full}
    for delta in (96,262):
        m={1:1}
        for t in range(58):
            for p in range(1,W-t+1):m[off[t]+p]=fo[t+delta]+p
        assert all(tuple(m[abs(v)]*(1 if v>0 else -1) for v in cl) in original for cl in C)
    root=anc.rows(2135555,62)[-1]&((1<<58)-1);rr=anc.rows(root,57)
    assert rr==phys.scalar_rows(root,57,58) and all(rr[t]&1==b for t,b in heads.items())
    assert [rr[23]>>(p-1)&1 for p in (6,7,8,9)]==[1,1,0,1]
    vals={1:True}
    for t in range(58):vals.update({off[t]+p:bool(rr[t]>>(p-1)&1) for p in range(1,W-t+1)})
    assert all(any(vals[abs(v)]==(v>0) for v in cl) for cl in C)
    (out/'false.cnf').write_text('p cnf 1 1\n1 0\n');(out/'false.lrat').write_text('')
    (out/'prepare.json').write_text(json.dumps({'height':57,'word':'25253353','goal':G,
      'base_embeds_both_original_sites':True,'original':info,'control_seed':2135555,'control_cut':62,
      'control_root':str(root),'all_base_clauses_and_scalar':True,'no_full_return_witness_claim':True},indent=2)+'\n')
    print('QUARTET_PREPARE_PASS')


def export(out):
    C,off,W=phys.generate(57,anc.word_heads('25253353',1))
    info=json.loads((out/'prepare.json').read_text());G=info['goal'];P=read_clauses(out/'quartet.drat')
    assert P[-1]==[]
    prefix=[]
    with Minisat22(bootstrap_with=C) as s:
        for g in G:
            for cl in P:
                cl=list(dict.fromkeys(cl+[g]))
                if any(-v in cl for v in cl):continue
                assert not s.propagate(assumptions=[-v for v in cl])[0]
                s.add_clause(cl);prefix.append(cl)
            assert prefix[-1]==[g]
    full,fo,fw=phys.generate(359,anc.word_heads(phys.E+phys.A*4+phys.E+phys.A*7+phys.E,1))
    combined=[];units=[]
    with Minisat22(bootstrap_with=full) as s:
        for delta in (96,262):
            m={1:1}
            for t in range(58):
                for p in range(1,W-t+1):m[off[t]+p]=fo[t+delta]+p
            translate=lambda cl:[m[abs(v)]*(1 if v>0 else -1) for v in cl]
            for cl in prefix:
                tr=translate(cl);assert not s.propagate(assumptions=[-v for v in tr])[0]
                s.add_clause(tr);combined.append(tr)
            units+=translate(G)
    with (out/'original-prefix.drup').open('w') as f:
        for cl in combined:f.write(' '.join(map(str,cl))+' 0\n')
    old=[-fo[118]-8,fo[121]+8,-fo[284]-8,fo[287]+8]
    results={};maps={}
    for name,extra in [('original',[]),('old4',old),('quartets',units),('union',old+units)]:
        B=full+[[v] for v in extra];vals,log,bad=phys.propagate(B)
        assert bad is None and phys.replay_units(B,log,bad)==vals
        seam={str(p):int(vals[fo[193]+p]) for p in range(1,fw-193+1) if fo[193]+p in vals}
        maps[name]=vals;results[name]={'root_level_units':len(vals),'seam193':seam,'extra_units':extra}
    results['new_over_old4']={'units':sorted((v if b else -v) for v,b in maps['union'].items() if v not in maps['old4']),
      'seam193':{p:b for p,b in results['union']['seam193'].items() if p not in results['old4']['seam193']}}
    (out/'export.json').write_text(json.dumps({'local_RUP_additions':len(prefix),'original_RUP_additions':len(combined),
       'original_units':units,'target_rows':[119,285],'cells':[6,7,8,9],'bits':[1,1,0,1],
       'propagation':results,'original_CNF_solve_or_refutation_claimed':False},indent=2)+'\n')
    print('QUARTET_EXPORT_AND_REASON_REPLAY_PASS',len(prefix),len(combined),results['new_over_old4'])


def check(out):
    root=out.parent
    assert 's UNSATISFIABLE' in (root/'solve.stdout').read_text()
    assert 's VERIFIED' in (root/'drat.stdout').read_text() and 's VERIFIED UNSAT' in (root/'cake.stdout').read_text()
    assert 's VERIFIED UNSAT' not in (root/'false-cake.stdout').read_text()
    assert 'empty clause not derived at end of proof' in (root/'false-cake.stderr').read_text()
    assert 's DERIVATION' in (root/'prefix.stdout').read_text()
    assert json.loads((root/'prefix.receipt.json').read_text())['returncode']==1
    print('ALL_QUARTET_CERTIFICATES_ORIGINAL_PREFIX_AND_CONTROLS_PASS')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=['prepare','export','check']);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();globals()[a.phase](a.out)
