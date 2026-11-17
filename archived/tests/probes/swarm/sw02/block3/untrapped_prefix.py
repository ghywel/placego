#!/usr/bin/env python3
"""Follow the single chaos draw: universal shielding and one shorter launch cone."""
import argparse,itertools,json
from pathlib import Path
import physical_47 as phys
import physical_ancestry as anc
from image_ancestry_audit import scan, PAIRS, trajectory


def abstract_gate(a,b,c):
    out=0
    for l,m,r in itertools.product(range(2),repeat=3):
        if a>>l&1 and b>>m&1 and c>>r&1:out|=1<<(l^(m|r))
    return out


def abstract(root,K,H):
    row=[1<<(root>>i&1) if i<K else 3 for i in range(H+1)];out=[row]
    for t in range(H):
        row=[abstract_gate((1<<anc.drive(t)) if i==0 else row[i-1],row[i],row[i+1]) for i in range(len(row)-1)]
        out.append(row)
    return out


def prefix_case(root,K,H,heads):
    C,off,W=phys.generate(H,heads)
    C += [[(off[0]+p)*(1 if root>>(p-1)&1 else -1)] for p in range(1,K+1)]
    return C,off,W


def prepare(out,prior):
    out.mkdir(parents=True,exist_ok=True);a=json.loads((prior/'prepare.json').read_text());r=json.loads((prior/'result.json').read_text())
    control=a['controls']['chaos'];root=int(control['original_root']);K=70;H=193
    masks=abstract(root,K,H)
    # Independently compare interval image with all concrete completions in small cones.
    for known in range(8):
        tab=abstract(known,3,8)
        for hi in range(64):
            rr=trajectory(known|(hi<<3),0,8)
            for t in range(9):
                assert all(mask>>(rr[t]>>i&1)&1 for i,mask in enumerate(tab[t]))
    cases={};C,off,W=prefix_case(root,K,129,{129:0})
    cases['repair129']=phys.dimacs(out/'repair129.cnf',C,off[-1])|{'H':129,'W':W,'fixed_low70':str(root&((1<<70)-1)),'wanted_head129':0}
    # UP as a separate exact-CNF realization of all abstract forced cells.
    base,bo,bw=prefix_case(root,K,H,{})
    vals,log,bad=phys.propagate(base);assert bad is None and phys.replay_units(base,log,bad)==vals
    for t in range(H+1):
        for p,m in enumerate(masks[t],1):
            if m!=3:assert bo[t]+p in vals and int(vals[bo[t]+p])==(m==2)
    corrupt=[x[:] for x in log];corrupt[0][0]*=-1
    try:phys.replay_units(base,corrupt,bad)
    except AssertionError:pass
    else:raise AssertionError('corrupt reason log accepted')
    wanted=anc.word_heads(anc.E+anc.A*4+'3353',1)
    C,off,W=phys.generate(153,wanted)
    cases['launch153']=phys.dimacs(out/'launch153.cnf',C,off[-1])|{'H':153,'W':W,'word':'E A4 3353'}
    # Four explicit higher tails distinguish prefix image from whole-row image.
    tails={}
    fixtures={n:(int(v['root_tick1']),v['width']) for n,v in r.items() if v['status']=='SAT_CHECKED'}
    fixtures['known_E']=(int(a['controls']['known_E_tick1_prefix']),69)
    for name,(y,width) in fixtures.items():
        accepted=[]
        for tail in range(4):
            full=y|(tail<<width);p=anc.inverse(full,1)
            if p is not None:assert anc.step(p,1)==full;accepted.append(tail)
        assert len(accepted)==len(PAIRS[scan(y,width)[-1]])
        tails[name]={'accepted_two_cell_tails':accepted,'state':scan(y,width)[-1]}
    mids=r['e_mid']['prefix_parent_roots'];new_root=int(next(iter(mids.values())));rr=trajectory(new_root,0,193)
    assert all(rr[t]&1==b for t,b in anc.word_heads(anc.E,1).items())
    target=anc.word_heads(anc.E+anc.A*4+anc.E,1)
    result={'cases':cases,'all_small_concrete_in_abstract':True,'four_tails':tails,
      'abstract_heads':{str(t):masks[t][0] for t in range(1,194,2)},
      'first_unknown_sample':next((t for t in range(1,194,2) if masks[t][0]==3),None),
      'first_fixed_wrong_EA4E_sample':next((t for t,b in target.items() if masks[t][0]!=3 and (masks[t][0]==2)!=bool(b)),None),
      'UP_units':len(vals),'all_abstract_constants_in_UP':True,'corrupt_log_rejected':True,
      'new_anchored_E_root':str(new_root),'new_anchored_E_bad_EA4E':[t for t,b in target.items() if rr[t]&1!=b],
      'new_anchored_E_rows_hex':[hex(x) for x in rr],
      'abstract_rows':masks,'UP_log':log}
    (out/'prepare.json').write_text(json.dumps(result,indent=2)+'\n')
    print('UNTRAPPED_PREFIX_PREPARE_PASS')
    print(json.dumps({k:result[k] for k in ('first_unknown_sample','first_fixed_wrong_EA4E_sample','four_tails','new_anchored_E_bad_EA4E')}))


def audit(out,prior):
    aa=json.loads((prior/'prepare.json').read_text());root=int(aa['controls']['chaos']['original_root']);ans={}
    for name in ('repair129','launch153'):
        text=(out.parent/(name+'.stdout')).read_text()
        if 's SATISFIABLE' not in text:
            ans[name]={'status':'UNSAT_UNCHECKED' if 's UNSATISFIABLE' in text else 'UNKNOWN'};continue
        if name=='repair129':C,off,W=prefix_case(root,70,129,{129:0});H=129
        else:C,off,W=phys.generate(153,anc.word_heads(anc.E+anc.A*4+'3353',1));H=153
        vals={abs(int(x)):int(x)>0 for line in text.splitlines() if line.startswith('v ') for x in line[2:].split() if x!='0'}
        assert all(any(vals[abs(x)]==(x>0) for x in cl) for cl in C)
        x=sum(int(vals[off[0]+p])<<(p-1) for p in range(1,W+1));rr=trajectory(x,0,193)
        assert all(vals[off[t]+p]==bool(rr[t]>>(p-1)&1) for t in range(H+1) for p in range(1,W-t+1))
        target=anc.word_heads(anc.E+anc.A*4+anc.E,1)
        ans[name]={'status':'SAT_CHECKED','root_tick0':str(x),'W':W,'H':H,
          'bad_EA4E':[t for t,b in target.items() if rr[t]&1!=b],
          'actual_source109_low7':rr[109]&127,'actual_label109':sum((rr[109+k]>>7&1)<<k for k in range(14)),
          'rows_hex':[hex(z) for z in rr],'all_original_CNF_and_scalar_cells_pass':True}
    (out/'result.json').write_text(json.dumps(ans,indent=2)+'\n')
    print('UNTRAPPED_PREFIX_MODEL_AUDIT_PASS');print(json.dumps({n:{k:v for k,v in r.items() if k!='rows_hex'} for n,r in ans.items()}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=['prepare','audit']);p.add_argument('--out',type=Path,required=True);p.add_argument('--prior',type=Path,required=True);a=p.parse_args();globals()[a.phase](a.out,a.prior)
