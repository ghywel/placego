#!/usr/bin/env python3
"""Fixed source64 implication in the existing 35-tick cone, with actual history.

No horizon increase, census, adaptive budget or restarted exterior. Native
solver/checker jobs are separate supervised processes in the frozen plan.
"""
import argparse
import hashlib
import json
import runpy
from pathlib import Path
from pysat.solvers import Minisat22
import physical_47 as phys
import physical_ancestry as anc


def build(out, replay):
    out.mkdir(parents=True,exist_ok=True)
    heads=anc.word_heads('25253',1)
    cases={}
    for name,wanted in [('compact',heads),('laterA',{t:b for t,b in heads.items() if t>=15})]:
        C,off,W=phys.generate(35,wanted)
        correct=[off[13]+p if p==7 else -off[13]-p for p in range(1,8)]
        goal=[-v for v in correct] # At least one of the seven source bits differs.
        info=phys.dimacs(out/(name+'.cnf'),C+[goal],off[-1])
        rup=[]
        with Minisat22(bootstrap_with=C) as s:
            assert s.propagate()[0]
            for v in correct:
                ok=not s.propagate(assumptions=[-v])[0]
                rup.append(ok)
                if ok:s.add_clause([v])
        cases[name]={'heads':wanted,'source_time':13,'source_low7':64,
                     'negated_conjunction_clause':goal,'cnf':info,'unit_RUP_flags':rup}
    root=49101737184
    rr=anc.rows(root,35)
    assert rr==phys.scalar_rows(root,35,36)
    assert all((rr[t]&1)==b for t,b in heads.items()) and rr[13]&127==64
    actual=sum((rr[13+k]>>7&1)<<k for k in range(14))
    assert actual==4482
    removed=anc.rows(0,35)
    assert removed[13]&127!=64
    cases['controls']={'nonvacuity_root':str(root),'source':rr[13]&127,
                       'actual_column8_word14':actual,'scalar_all_cells':True,
                       'heads_removed_root':'0','heads_removed_source':removed[13]&127}
    phys.dimacs(out/'true.cnf',[[1],[-1]],1)
    (out/'true.drup').write_text('0\n')
    phys.dimacs(out/'false.cnf',[[1]],1)
    (out/'false.drup').write_text('0\n')
    (out/'false.lrat').write_text('2 0 1 0\n')
    # Numerical replay of Local's S14 worked cell, plus a cell-array oracle
    # for every graph edge at both release widths. No Wolfram evaluation.
    data=runpy.run_path(str(replay))
    edges=0
    for word,B,R,forb,ctrl in data['CASES']:
        n=1<<B
        for ph in range(3):
            for row in range(n):
                for x in (0,1):
                    bits=[int(word[ph])]+[(row>>i)&1 for i in range(B)]+[x]
                    scalar=sum((bits[i] ^ (bits[i+1]|bits[i+2]))<<i for i in range(B))
                    e=row|(x<<B)
                    assert scalar==((((e<<1)|int(word[ph]))^(e|(e>>1)))&(n-1))
                    edges+=1
    result={'cases':cases,'source64_lookahead_ticks':22,'S14_graph_edge_scalar_checks':edges,
            'S14_worked_output':data['out'],'S14_replay_sha256':hashlib.sha256(replay.read_bytes()).hexdigest(),
            'no_solver_search_in_builder':True,'no_autonomous_seven_bit_claim':True}
    (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print('SOURCE64_BUILD_PASS',json.dumps(result))


def check(out):
    logs=out.parent
    for name in ('compact','laterA','true'):
        assert 's VERIFIED' in (logs/(name+'-drat.stdout')).read_text()
        assert 's VERIFIED UNSAT' in (logs/(name+'-cake.stdout')).read_text()
    for name in ('compact','laterA'):
        assert 's UNSATISFIABLE' in (logs/(name+'-solve.stdout')).read_text()
    assert 's VERIFIED' not in (logs/'false-drat.stdout').read_text()
    assert 's VERIFIED UNSAT' not in (logs/'false-cake.stdout').read_text()
    assert json.loads((logs/'false-drat.receipt.json').read_text())['returncode']!=0
    assert json.loads((logs/'false-cake.receipt.json').read_text())['returncode']!=0
    print('ALL_SOURCE64_CERTIFICATES_AND_CONTROLS_PASS')


def main():
    p=argparse.ArgumentParser();p.add_argument('phase',choices=['build','check'])
    p.add_argument('--out',type=Path,required=True);p.add_argument('--replay',type=Path)
    a=p.parse_args()
    if a.phase=='build':build(a.out,a.replay)
    else:check(a.out)


if __name__=='__main__':main()
