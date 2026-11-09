#!/usr/bin/env python3
"""Exact black-center predecessor-prefix automaton and fixed E ancestry tests."""
import argparse, hashlib, itertools, json, random
from pathlib import Path
import physical_47 as phys
import physical_ancestry as anc
from sparse_label_certificate import cone

PAIRS=({(0,0)},{(0,1)},{(1,0),(1,1)},{(0,1),(1,0),(1,1)},
       {(0,0),(1,0),(1,1)},{(0,0),(0,1)},set(itertools.product((0,1),repeat=2)),set())
TRANS=((0,1),(7,2),(3,0),(3,4),(6,5),(0,3),(6,6),(7,7))
NAMES=('a','b','c','d','e','f','U','empty')
CASES={'opening_mid':('3353',tuple(range(6))),
       'e_bad':(anc.E,(7,)), 'e_mid':(anc.E,tuple(range(6)))}
SEED='GC2776-chaos-one-root-tail'


def scan(y,W):
    assert y&1
    q=0;path=[q]
    for i in range(1,W):q=TRANS[q][y>>i&1];path.append(q)
    return path


def parent(y,W):
    # Independent forward nondeterministic reconstruction, retaining full roots.
    paths={(0,0):0}
    for i in range(2,W+1):
        new={}
        for (a,b),x in paths.items():
            for c in (0,1):
                if a^(b|c)==y>>(i-1)&1:new[(b,c)]=x|(c<<i)
        paths=new
    return paths


def encode(word,allowed):
    heads={t-1:b for t,b in anc.word_heads(word,1).items()};H=max(heads)
    C,off,W=cone(H,heads);base=off[-1]
    v=lambda i,q:base+8*(i-1)+q+1
    for i in range(1,W+1):
        vs=[v(i,q) for q in range(8)];C.append(vs)
        C += [[-x,-y] for x,y in itertools.combinations(vs,2)]
    C.append([v(1,0)])
    for i in range(2,W+1):
        bit=off[0]+i
        for q in range(8):
            C.append([-v(i-1,q),bit,v(i,TRANS[q][0])])
            C.append([-v(i-1,q),-bit,v(i,TRANS[q][1])])
    C.append([v(W,q) for q in allowed])
    return C,off,W,heads,base+8*W


def trajectory(x,start,H):
    rr=[x];cells=[x>>i&1 for i in range(x.bit_length()+H+4)]
    for t in range(start,start+H):
        x=anc.step(x,anc.drive(t));rr.append(x)
        cells=[(anc.drive(t) if i==0 else cells[i-1])^(cells[i]|(cells[i+1] if i+1<len(cells) else 0)) for i in range(len(cells))]
        assert x==sum(v<<i for i,v in enumerate(cells))
    return rr


def controls():
    for q,S in enumerate(PAIRS):
        for bit in (0,1):
            image={(b,c) for a,b in S for c in (0,1) if a^(b|c)==bit}
            assert image==PAIRS[TRANS[q][bit]]
    count=0
    for W in range(1,11):
        lookup={}
        for x in range(1<<(W+1)):
            y=anc.step(x,1)&((1<<W)-1)
            if y&1:lookup.setdefault(y,set()).add((x>>(W-1)&1,x>>W&1))
        for y in range(1,1<<W,2):
            st=scan(y,W)[-1]
            assert PAIRS[st]==lookup.get(y,set())
            assert set(parent(y,W))==PAIRS[st]
            assert (anc.inverse(y,1) is not None)==((0,0) in PAIRS[st])
            count+=1
    gap={}
    for y in range(1,128,2):
        rr=trajectory(y,1,6)
        if [rr[t]&1 for t in (0,2,4,6)]==[1,0,0,1]:gap[y]=NAMES[scan(y,7)[-1]]
        assert ([rr[t]&1 for t in (0,2,4,6)]==[1,0,0,1])==((y&7)==7 and bool(y&24))
    rr=trajectory(639,1,12)
    assert all(rr[t-1]&1==b for t,b in anc.word_heads('33',1).items())
    assert scan(639,13)[-1]==7
    # Known full physical E: keep original seed ancestry, then shift an even90 ticks.
    original=trajectory(2135555,0,90)[-1]
    rows=trajectory(original,0,193)
    assert all(rows[t]&1==b for t,b in anc.word_heads(anc.E,1).items())
    first=rows[1]&((1<<69)-1)
    assert scan(first,69)[-1]==6
    # Owner-requested one-shot chaos: modify only original root cells71..194.
    bits=random.Random(SEED).getrandbits(124)
    changed=(original&((1<<70)-1))|(bits<<70)
    mutant=trajectory(changed,0,193)
    assert all((rows[t]&1)==(mutant[t]&1) for t in range(70))
    differing=[t for t in range(1,194,2) if rows[t]&1!=mutant[t]&1]
    wanted=anc.word_heads(anc.E+anc.A*4+anc.E,1)
    chaos={'seed':SEED,'original_root':str(original),'changed_root':str(changed),
      'frozen_low70':str(original&((1<<70)-1)),'random_high124':str(bits),
      'first_different_sample':differing[0] if differing else None,
      'all_different_samples':differing,'prediction_changed_by125':any(t<=125 for t in differing),
      'original_bad_EA4E':[t for t,b in wanted.items() if rows[t]&1!=b],
      'changed_bad_EA4E':[t for t,b in wanted.items() if mutant[t]&1!=b],
      'rows_hex':[hex(x) for x in mutant],'baseline_rows_hex':[hex(x) for x in rows],
      'firstE_preserved':True,'root0_ancestry_preserved':True,
      'no_seam_splice':True,'one_draw_only':True}
    return {'DFA_exhaustive_prefix_cases':count,'transition_truth_table':True,
      'gap3_states':gap,'free33_nonimage639':True,'known_E_universal_state':True,
      'known_E_tick1_prefix':str(first),'chaos':chaos}


def prepare(out):
    out.mkdir(parents=True,exist_ok=True)
    result={'controls':controls(),'cases':{}}
    for name,(word,allowed) in CASES.items():
        C,off,W,heads,N=encode(word,allowed)
        result['cases'][name]=phys.dimacs(out/(name+'.cnf'),C,N)|{'W':W,'H':max(heads),'allowed':[NAMES[q] for q in allowed],'word':word}
    # Small independent nontrivial UNSAT and empty-proof rejection controls.
    C=[[1,2],[1,-2],[-1,2],[-1,-2]]
    phys.dimacs(out/'control.cnf',C,2)
    (out/'false.cnf').write_text('p cnf 1 1\n1 0\n');(out/'false.lrat').write_text('')
    (out/'prepare.json').write_text(json.dumps(result,indent=2)+'\n')
    print('IMAGE_ANCESTRY_PREPARE_PASS')


def audit(out):
    ans={}
    for name,(word,allowed) in CASES.items():
        text=(out.parent/(name+'.stdout')).read_text()
        if 's SATISFIABLE' not in text:
            ans[name]={'status':'UNSAT_UNCHECKED' if 's UNSATISFIABLE' in text else 'UNKNOWN'};continue
        vals={abs(int(x)):int(x)>0 for line in text.splitlines() if line.startswith('v ') for x in line[2:].split() if x!='0'}
        C,off,W,heads,N=encode(word,allowed)
        assert all(any(vals[abs(x)]==(x>0) for x in cl) for cl in C)
        root=sum(int(vals[off[0]+i])<<(i-1) for i in range(1,W+1))
        rr=trajectory(root,1,max(heads));path=scan(root,W)
        assert path[-1] in allowed
        assert all(rr[t]&1==b for t,b in heads.items())
        assert all(vals[off[t]+p]==bool(rr[t]>>(p-1)&1) for t in range(max(heads)+1) for p in range(1,W-t+1))
        pp=parent(root,W);assert set(pp)==PAIRS[path[-1]]
        for x in pp.values():assert anc.step(x,1)&((1<<W)-1)==root
        ans[name]={'status':'SAT_CHECKED','root_tick1':str(root),'width':W,
          'state':NAMES[path[-1]],'state_path':[NAMES[q] for q in path],
          'first_dead_cell':next((i+1 for i,q in enumerate(path) if q==7),None),
          'whole_white_tail_has_parent':anc.inverse(root,1) is not None,
          'prefix_parent_roots':{str(p):str(x) for p,x in pp.items()},
          'all_CNF_scalar_and_integer_cells_pass':True,'rows_hex':[hex(x) for x in rr]}
    (out/'result.json').write_text(json.dumps(ans,indent=2)+'\n')
    print('IMAGE_ANCESTRY_MODEL_AUDIT_PASS');print(json.dumps({n:{k:v for k,v in r.items() if k in ('status','root_tick1','state','first_dead_cell')} for n,r in ans.items()}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=['prepare','audit']);p.add_argument('--out',type=Path,required=True);a=p.parse_args();globals()[a.phase](a.out)
