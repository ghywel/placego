#!/usr/bin/env python3
"""One joint-tail sensitivity question at the unary threshold's predecessor."""
import argparse,json
from pathlib import Path
import physical_47 as phys
import physical_ancestry as anc
from image_ancestry_audit import trajectory
from untrapped_prefix import prefix_case
p=argparse.ArgumentParser();p.add_argument('phase',choices=['prepare','audit']);p.add_argument('--image',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
c=json.loads((a.image/'prepare.json').read_text())['controls']['chaos'];original=int(c['original_root'])
C,off,W=prefix_case(original,68,129,{129:0})
if a.phase=='prepare':
    info=phys.dimacs(a.out/'repair68.cnf',C,off[-1]);(a.out/'prepare.json').write_text(json.dumps(info,indent=2)+'\n');print('BOUNDARY_REPAIR_PREPARE_PASS')
else:
    text=(a.out.parent/'repair68.stdout').read_text()
    if 's SATISFIABLE' not in text:r={'status':'UNSAT_UNCHECKED' if 's UNSATISFIABLE' in text else 'UNKNOWN'}
    else:
        vals={abs(int(x)):int(x)>0 for line in text.splitlines() if line.startswith('v ') for x in line[2:].split() if x!='0'}
        assert all(any(vals[abs(x)]==(x>0) for x in cl) for cl in C)
        root=sum(int(vals[off[0]+i])<<(i-1) for i in range(1,W+1));rows=trajectory(root,0,193)
        assert all(vals[off[t]+i]==bool(rows[t]>>(i-1)&1) for t in range(130) for i in range(1,W-t+1))
        assert root&((1<<68)-1)==original&((1<<68)-1) and rows[129]&1==0
        assert all(rows[t]&1==b for t,b in anc.word_heads(anc.E,1).items())
        target=anc.word_heads(anc.E+anc.A*4+anc.E,1)
        r={'status':'SAT_CHECKED','root_tick0':str(root),'first_E_preserved':True,'all_CNF_and_scalar_cells_pass':True,
           'head125':rows[125]&1,'head129':rows[129]&1,'bad_EA4E':[t for t,b in target.items() if rows[t]&1!=b],
           'source109_low7':rows[109]&127,'source109_label':sum((rows[109+k]>>7&1)<<k for k in range(14)),
           'rows_hex':[hex(x) for x in rows],'sharp_contiguous_prefix69_for_head129':True}
    (a.out/'result.json').write_text(json.dumps(r,indent=2)+'\n');print('BOUNDARY_REPAIR_AUDIT_PASS');print(json.dumps({k:v for k,v in r.items() if k!='rows_hex'}))
