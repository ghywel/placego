#!/usr/bin/env python3
"""Map the sparse compact guard to both original E launches; proof reuse only."""
import argparse
import hashlib
import json
from pathlib import Path
from pysat.solvers import Minisat22
import physical_47 as phys
import physical_ancestry as anc


def cnf(path):
    rows=[]
    for line in path.read_text().splitlines():
        if line.startswith(('p','c')) or not line.strip():continue
        v=list(map(int,line.split()));assert v[-1]==0;rows.append(v[:-1])
    return rows


def main():
    p=argparse.ArgumentParser();p.add_argument('phase');p.add_argument('--out',type=Path,required=True)
    p.add_argument('--compact',type=Path);p.add_argument('--columns',default='6,7,8');p.add_argument('--source-case',default='sparse')
    a=p.parse_args();o=a.out;o.mkdir(parents=True,exist_ok=True)
    if a.phase=='check':
        for t in (119,285):
            assert 's VERIFIED UNSAT' in (o.parent/(f'site{t}-cake.stdout')).read_text()
            assert 's VERIFIED' in (o.parent/(f'site{t}-drat.stdout')).read_text()
        text=(o.parent/'prefix.stdout').read_text();rec=json.loads((o.parent/'prefix.receipt.json').read_text())
        assert 's DERIVATION' in text and 'all lemmas preserve satisfiability' in text and rec['returncode']==1
        print('ALL_TWO_SITE_GUARD_CHECKS_PASS');return
    assert a.phase=='build'
    C,off,W=phys.generate(359,anc.word_heads(phys.E+phys.A*4+phys.E+phys.A*7+phys.E,1));N=off[-1]
    info=phys.dimacs(o/'original.cnf',C,N)
    assert info['sha256']=='21b425011ebc816994a2dfe221539ca2da6a5900b23d1f7009c9bbe26d70426c'
    _,so,sw=phys.generate(35,anc.word_heads('25253',1))
    columns=list(map(int,a.columns.split(',')));assert columns in ([6,7],[6,7,8])
    G=[so[23]+p for p in columns]
    source=cnf(a.compact/(a.source_case+'.cnf'));assert source[-len(G):]==[[-v] for v in G]
    proof=cnf(a.compact/(a.source_case+'.drup'));assert proof[-1]==[] and proof[-2]==G;proof=proof[:-1]
    canon=lambda cl:tuple(sorted(set(cl)));original={canon(cl) for cl in C}
    combined=[];sites=[]
    for delta in (96,262):
        def mapping(shift):
            m={1:1}
            for t in range(36):
                for p_ in range(1,sw-t+1):m[so[t]+p_]=off[t+shift]+p_
            return m
        m=mapping(delta);tr=lambda cl:[m[abs(v)]*(1 if v>0 else -1) for v in cl]
        assert all(canon(tr(cl)) in original for cl in source[:-len(G)])
        wrong=mapping(delta+1)
        assert any(canon([wrong[abs(v)]*(1 if v>0 else -1) for v in cl]) not in original for cl in source[:-len(G)])
        goal=tr(G);body=[tr(cl) for cl in proof];tick=delta+23
        phys.dimacs(o/f'site{tick}.cnf',C+[[-v] for v in goal],N)
        with (o/f'site{tick}.drup').open('w') as f:
            for cl in body:f.write(' '.join(map(str,cl))+' 0\n')
            f.write('0\n')
        combined+=body;sites.append({'even_shift':delta,'row':tick,'columns':columns,'clause':goal,'odd_shift_rejected':True,'all_source_clauses_in_original':True})
    with Minisat22(bootstrap_with=C) as s,(o/'combined-prefix.drup').open('w') as f:
        assert s.propagate()[0]
        for cl in combined:
            assert not s.propagate(assumptions=[-v for v in cl])[0]
            s.add_clause(cl);f.write(' '.join(map(str,cl))+' 0\n')
    result={'sites':sites,'RUP_prefix_additions':len(combined),'original':info,
            'source_prefix_additions':len(proof),'no_solve_calls':True,'not_a_full_target_refutation':True,
            'seam193':{'past_scan_indices':[74+p_ for p_ in columns],'future_ticks':92,'future_prefix_cells_sufficient':92+max(columns)}}
    (o/'result.json').write_text(json.dumps(result,indent=2)+'\n');print('TWO_SITE_BUILD_PASS',json.dumps(result))


if __name__=='__main__':main()
