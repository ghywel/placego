#!/usr/bin/env python3
"""CL755 sparse label theorem: exact odd-root cones and original-CNF export."""
import argparse,json
from pathlib import Path
from pysat.solvers import Minisat22
import physical_47 as phys
import physical_ancestry as anc
SIX={2:1,16:1,26:0,30:1,34:1,48:0}
FIVE={2:1,6:1,20:1,34:1,48:0}
WORD=4520

def cone(H,heads):
    W=H+1;off=[1]
    for t in range(H+1):off.append(off[-1]+W-t)
    v=lambda t,p:off[t]+p
    C=[[1]]
    for t in range(H):
        for p in range(1,W-t):
            left=v(t,p-1) if p>1 else (-1 if t%2==0 else 1)
            for cl in phys.gate(left,v(t,p),v(t,p+1),v(t+1,p)):
                cl=list(dict.fromkeys(cl))
                if not any(-x in cl for x in cl):C.append(cl)
    C += [[v(t,1) if b else -v(t,1)] for t,b in sorted(heads.items())]
    return C,off,W

def case(name):
    if name=='short-root':heads={t-2:b for t,b in SIX.items()};H=46;source=26
    else:
        heads=FIVE if name=='five' else SIX if name=='six' else SIX|FIVE
        H=48;source=28
    C,off,W=cone(H,heads)
    G=[(off[source+k]+8)*(1 if WORD>>k&1 else -1) for k in range(14)]
    return C,off,W,G,heads,H,source

def prepare(out):
    out.mkdir(parents=True,exist_ok=True);info={}
    full,fo,fw=phys.generate(359,anc.word_heads(phys.E+phys.A*4+phys.E+phys.A*7+phys.E,1))
    original=phys.dimacs(out/'original.cnf',full,fo[-1])
    assert original['sha256']=='21b425011ebc816994a2dfe221539ca2da6a5900b23d1f7009c9bbe26d70426c'
    base={tuple(cl) for cl in full}
    for name in ('five','six','positive','short-root'):
        C,off,W,G,heads,H,source=case(name)
        D=C if name=='positive' else C+[[-g for g in G]]
        info[name]=phys.dimacs(out/(name+'.cnf'),D,off[-1])|{'height':H,'width':W,'source':source,'heads':heads,'goal':G}
        if name in ('five','six'):
            for delta in (81,247):
                m={1:1}
                for t in range(H+1):
                    for p in range(1,W-t+1):m[off[t]+p]=fo[t+delta]+p
                assert all(tuple(m[abs(x)]*(1 if x>0 else -1) for x in cl) in base for cl in C)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    vals={1:a,2:b,3:c,4:d}
                    assert all(any(vals[abs(x)]==(x>0) for x in cl) for cl in phys.gate(1,2,3,4))==(d==(a^(b|c)))
    (out/'false.cnf').write_text('p cnf 1 1\n1 0\n');(out/'false.lrat').write_text('')
    (out/'prepare.json').write_text(json.dumps({'cases':info,'original':original,'both_embeddings_clause_exact':True,'odd_root':True},indent=2)+'\n')
    print('SPARSE_LABEL_PREPARE_PASS')

def witness(out,name):
    text=(out.parent/(name+'.stdout')).read_text();assert 's SATISFIABLE' in text
    signed=[int(x) for line in text.splitlines() if line.startswith('v ') for x in line[2:].split() if x!='0']
    vals={abs(x):x>0 for x in signed}
    C,off,W,G,heads,H,source=case(name);D=C if name=='positive' else C+[[-g for g in G]]
    assert all(any(vals[abs(x)]==(x>0) for x in cl) for cl in D)
    root=sum(int(vals[off[0]+p])<<(p-1) for p in range(1,W+1));row=root;rows=[row]
    cells=[root>>i&1 for i in range(W+H+3)]
    for t in range(H+1):
        assert row==sum(x<<i for i,x in enumerate(cells))
        assert all(vals[off[t]+p]==bool(row>>(p-1)&1) for p in range(1,W-t+1))
        if t<H:
            row=((row<<1)|(t%2))^(row|(row>>1));rows.append(row)
            cells=[(t%2 if i==0 else cells[i-1])^(cells[i]|(cells[i+1] if i+1<len(cells) else 0)) for i in range(len(cells))]
    label=sum((rows[source+k]>>7&1)<<k for k in range(14))
    assert all(rows[t]&1==b for t,b in heads.items())
    assert (label==WORD)==(name=='positive')
    return {'root':str(root),'label':label,'source_low7':rows[source]&127,'all_CNF_and_scalar_pass':True,'root_relative_T':-28 if name=='positive' else -26,'rows_hex':[hex(x) for x in rows]}

def proof_clauses(path):
    result=[]
    for line in path.read_text().splitlines():
        if not line or line.startswith(('c','d')):continue
        vals=list(map(int,line.split()));assert vals[-1]==0;result.append(vals[:-1])
    return result

def export(out):
    witnesses={n:witness(out,n) for n in ('positive','short-root')}
    C,off,W,G,_,H,_=case('five');P=proof_clauses(out/'five.drat');assert P[-1]==[]
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
        for delta in (81,247):
            m={1:1}
            for t in range(H+1):
                for p in range(1,W-t+1):m[off[t]+p]=fo[t+delta]+p
            tr=lambda cl:[m[abs(x)]*(1 if x>0 else -1) for x in cl]
            for cl in prefix:
                c=tr(cl);assert not s.propagate(assumptions=[-v for v in c])[0]
                s.add_clause(c);combined.append(c)
            units+=tr(G)
    with (out/'original-prefix.drup').open('w') as f:
        for cl in combined:f.write(' '.join(map(str,cl))+' 0\n')
    assert (out/'original-prefix.drup').stat().st_size<16*1024*1024
    old4=[-fo[118]-8,fo[121]+8,-fo[284]-8,fo[287]+8]
    quartets=[(fo[t]+p)*(1 if b else -1) for t in (119,285) for p,b in ((6,1),(7,1),(8,0),(9,1))]
    prop={};maps={}
    for name,extra in [('original',[]),('previous',old4+quartets),('labels',units),('union',old4+quartets+units)]:
        B=full+[[v] for v in extra];vals,log,bad=phys.propagate(B)
        assert bad is None and phys.replay_units(B,log,bad)==vals;maps[name]=vals
        prop[name]={'unit_count':len(vals),'seam193':{str(p):int(vals[fo[193]+p]) for p in range(1,fw-193+1) if fo[193]+p in vals}}
    prop['new_over_previous']=sorted(v if b else -v for v,b in maps['union'].items() if v not in maps['previous'])
    (out/'result.json').write_text(json.dumps({'witnesses':witnesses,'local_RUP_additions':len(prefix),'original_RUP_additions':len(combined),'original_units':units,'propagation':prop,'full359_solved':False},indent=2)+'\n')
    print('SPARSE_LABEL_EXPORT_PASS')

def check(out):
    for name in ('five','six'):
        assert 's UNSATISFIABLE' in (out.parent/(name+'.stdout')).read_text()
        assert 's VERIFIED' in (out.parent/(name+'-drat.stdout')).read_text()
        assert 's VERIFIED UNSAT' in (out.parent/(name+'-cake.stdout')).read_text()
    assert 's VERIFIED UNSAT' not in (out.parent/'false-cake.stdout').read_text()
    assert 'empty clause not derived at end of proof' in (out.parent/'false-cake.stderr').read_text()
    assert 's DERIVATION' in (out.parent/'prefix.stdout').read_text()
    assert json.loads((out.parent/'prefix.receipt.json').read_text())['returncode']==1
    print('SPARSE_LABEL_ALL_CERTIFICATES_AND_CONTROLS_PASS')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=['prepare','export','check']);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();globals()[a.phase](a.out)
