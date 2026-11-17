#!/usr/bin/env python3
"""Reuse checked refutations to export history guards; propagation only, no SAT search."""
import argparse
import hashlib
import json
from pathlib import Path
from pysat.solvers import Minisat22
import e_short_guard as short
import physical_47 as phys
import physical_ancestry as anc


def lines(path):
    for line in path.read_text().splitlines():
        tokens=line.split()
        if not tokens or tokens[0] in ('c','d'):continue
        cl=list(map(int,tokens));assert cl[-1]==0
        yield cl[:-1]


def write(f,cl):f.write(' '.join(map(str,cl))+(' ' if cl else '')+'0\n')
def add(s,f,cl):
    cl=list(dict.fromkeys(cl));ok,_=s.propagate(assumptions=[-v for v in cl])
    assert not ok,('not RUP',cl)
    s.add_clause(cl);write(f,cl)


def main():
    p=argparse.ArgumentParser();p.add_argument('phase');p.add_argument('--out',type=Path,required=True)
    p.add_argument('--old-guard',type=Path);p.add_argument('--past-proof',type=Path);p.add_argument('--full',type=Path)
    p.add_argument('--bad-log',type=Path)
    a=p.parse_args();o=a.out;o.mkdir(parents=True,exist_ok=True)
    if a.phase=='check':
        log=lambda n:(o.parent/(n+'.stdout')).read_text()
        assert 's VERIFIED UNSAT' in log('triple-cake') and 's VERIFIED UNSAT' in log('word-cake')
        prefix=log('full-prefix')
        assert 's DERIVATION' in prefix and 'VERIFIED derivation: all lemmas preserve satisfiability' in prefix
        assert json.loads((o.parent/'full-prefix.receipt.json').read_text())['returncode']==1
        bad=a.bad_log.read_text() if a.bad_log else log('bad-prefix')
        assert 's VERIFIED' not in bad and 's DERIVATION' not in bad
        print('ALL_GUARD_EXPORT_CHECKS_PASS');return
    C,off,W=phys.generate(193,anc.word_heads(phys.E+phys.A*4+phys.E,1));N=off[-1]
    v=lambda t,p:off[t]+p
    av,bv,cv,dv,ev=[v(119,p) for p in range(6,11)];q=v(121,8)
    original={tuple(sorted(set(cl))) for cl in C}
    source,ids,true=short.build('253353',(13,0));mapping={true:1}
    for t,row in enumerate(ids):
        for p_,var in enumerate(row,1):mapping[var]=v(t+108,p_)
    mapped=lambda cl:[mapping[abs(x)]*(1 if x>0 else -1) for x in cl]
    assert all(tuple(sorted(set(mapped(cl)))) in original for cl in source[:-1])
    assert mapped(source[-1])==[-q]
    phys.dimacs(o/'triple.cnf',C+[[-av],[-bv],[-cv]],N)
    with Minisat22(bootstrap_with=C+[[-av],[-bv],[-cv]]) as s,(o/'triple.drup').open('w') as f:
        count=0
        for cl in lines(a.old_guard):add(s,f,mapped(cl)+[q]);count+=1
        add(s,f,[dv,ev])
        core=list(lines(a.past_proof));assert core and core[-1]==[]
        for cl in core:add(s,f,cl)
    # Source row109 low7=64 and its next eleven actual column8 bits=93.
    assumptions=[v(109,p) if 64>>(p-1)&1 else -v(109,p) for p in range(1,8)]
    assumptions += [v(109+i,8) if 93>>i&1 else -v(109+i,8) for i in range(11)]
    phys.dimacs(o/'word.cnf',C+[[x] for x in assumptions],N)
    trunk=[64]
    for t in range(1,11):
        u=93>>(t-1)&1;x=trunk[-1]
        trunk.append((((x<<1)|anc.drive(t))^(x|((x>>1)|(u<<6))))&127)
    assert trunk==[64,96,49,27,104,44,103,57,78,115,28] and 93>>10&1==0
    with Minisat22(bootstrap_with=C+[[x] for x in assumptions]) as s,(o/'word.drup').open('w') as f:
        for unit in (-av,-bv,-cv):add(s,f,[unit])
        for cl in lines(o/'triple.drup'):add(s,f,cl)
    # Discharge the three negative assumptions into a clause of original359.
    F,fo,FW=phys.generate(359,anc.word_heads(phys.E+phys.A*4+phys.E+phys.A*7+phys.E,1))
    info=phys.dimacs(o/'full.cnf',F,fo[-1])
    assert info['sha256']==hashlib.sha256(a.full.read_bytes()).hexdigest()=='21b425011ebc816994a2dfe221539ca2da6a5900b23d1f7009c9bbe26d70426c'
    m={1:1}
    for t in range(194):
        for p_ in range(1,W-t+1):m[v(t,p_)]=fo[t]+p_
    tr=lambda cl:[m[abs(x)]*(1 if x>0 else -1) for x in cl]
    G=tr([av,bv,cv]);fullset={tuple(sorted(set(cl))) for cl in F}
    assert all(tuple(sorted(set(tr(cl)))) in fullset for cl in C)
    with Minisat22(bootstrap_with=F) as s,(o/'full-prefix.drup').open('w') as f:
        assert s.propagate()[0]
        for cl in lines(o/'triple.drup'):add(s,f,tr(cl)+G)
    (o/'bad-prefix.drup').write_text('0\n')
    result={'triple_guard_physical':'x119,6 OR x119,7 OR x119,8',
        'triple_case_cnf':hashlib.sha256((o/'triple.cnf').read_bytes()).hexdigest(),
        'word_case_cnf':hashlib.sha256((o/'word.cnf').read_bytes()).hexdigest(),
        'source_row':109,'source64':True,'forbidden_input_low11':93,'excluded_retained_word':14429,
        'trunk_rows109_to119':trunk,'old_guard_RUP_additions':count,'past_core_RUP_additions':len(core),
        'full_original_clause':G,'full_original_sha256':info['sha256'],
        'proof_method':'Only RUP propagation and existing proof reuse; no solve call',
        'scope':'Necessary conditions; no proof of existence of the whole past or full4,7 witness'}
    (o/'result.json').write_text(json.dumps(result,indent=2)+'\n');print('GUARD_EXPORT_RUP_PASS',result)


if __name__=='__main__':main()
