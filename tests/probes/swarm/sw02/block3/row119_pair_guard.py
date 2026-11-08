#!/usr/bin/env python3
"""Discharge only the two negative goals actually used by the checked LRAT DAG."""
import argparse,json
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
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);p.add_argument('--audit',type=Path,required=True)
    p.add_argument('--lrat',type=Path,required=True);p.add_argument('--compact',type=Path,required=True);a=p.parse_args();o=a.out;o.mkdir(parents=True,exist_ok=True)
    support=json.loads((a.audit/'support.json').read_text())
    assert [i for i in (112425,112426,112427) if i in support['initial_clause_ids']]==[112425,112426]
    C,off,W=phys.generate(35,anc.word_heads('25253',1));N=off[-1];G=[off[23]+p for p in (6,7)]
    _,oo,ow=phys.generate(193,anc.word_heads(phys.E+phys.A*4+phys.E,1));m={1:1}
    for t in range(96,132):
        for p_ in range(1,W-(t-96)+1):m[oo[t]+p_]=off[t-96]+p_
    keep=set(support['lemma_ids']);P=[]
    for line in a.lrat.read_text().splitlines():
        words=line.split()
        if not words or words[0]=='c' or words[1]=='d' or int(words[0]) not in keep:continue
        v=list(map(int,words));z=v.index(0,1);cl=v[1:z]
        assert all(abs(x) in m for x in cl)
        P.append(list(dict.fromkeys([m[abs(x)]*(1 if x>0 else -1) for x in cl]+G)))
    assert len(P)==52 and P[-1]==G
    sparse={x['t']-96:x['bit'] for x in json.loads((a.audit/'greedy-head-core.json').read_text())['heads']}
    S,_,_=phys.generate(35,sparse);cases={}
    for name,base in (('word',C),('sparse',S)):
        ok,count=replay(base,P);cases[name]={'RUP_pass':ok,'checked':count}
        phys.dimacs(o/(name+'.cnf'),base+[[-v] for v in G],N)
        if ok:
            with (o/(name+'.drup')).open('w') as f:
                for cl in P:f.write(' '.join(map(str,cl))+' 0\n')
                f.write('0\n')
    assert cases['word']['RUP_pass']
    # The already carried ten-step trunk suffices; no eleventh input unit.
    assumptions=[off[13]+p_ if 64>>(p_-1)&1 else -off[13]-p_ for p_ in range(1,8)]
    assumptions += [off[13+k]+8 if 93>>k&1 else -off[13+k]-8 for k in range(10)]
    base=C+[[v] for v in assumptions];Q=[]
    with Minisat22(bootstrap_with=base) as s:
        for v in G:
            assert not s.propagate(assumptions=[v])[0]
            s.add_clause([-v]);Q.append([-v])
        for cl in P:
            assert not s.propagate(assumptions=[-v for v in cl])[0]
            s.add_clause(cl);Q.append(cl)
        assert not s.propagate()[0]
    phys.dimacs(o/'input10.cnf',base,N)
    with (o/'input10.drup').open('w') as f:
        for cl in Q:f.write(' '.join(map(str,cl))+' 0\n')
        f.write('0\n')
    cases['input10']={'RUP_pass':True,'source_row':13,'source64':True,'actual_input_count':10,'input_value':93}
    prior=json.loads((a.compact/'result.json').read_text())['nonvacuity'];root=int(prior['root']);rr=anc.rows(root,35)
    assert rr==[int(h,16) for h in prior['rows_hex']] and (rr[23]>>5&3)!=0
    result={'cases':cases,'goal_columns':[6,7],'goal_time':23,'goal_variables':G,'source64_row':13,
            'forbidden_input_low10':93,'unused_original_negative_goal':112427,'prefix_additions':len(P),
            'nonvacuity_root':str(root),'nonvacuity_patch':prior['patch_at23'],'lookahead_ticks':12,
            'not_a_minimal_semantic_premise':True,'no_solve_calls':True}
    (o/'result.json').write_text(json.dumps(result,indent=2)+'\n');print('PAIR_GUARD_BUILD_PASS',json.dumps(result))


if __name__=='__main__':main()
