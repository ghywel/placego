#!/usr/bin/env python3
"""One deterministic follow-up to the chaos shielding threshold, no sweep."""
import argparse,json
from pathlib import Path
import physical_ancestry as anc
from image_ancestry_audit import trajectory
from untrapped_prefix import abstract

p=argparse.ArgumentParser();p.add_argument('--image',type=Path,required=True);p.add_argument('--core',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
c=json.loads((a.image/'prepare.json').read_text())['controls']['chaos'];d=json.loads((a.core/'result.json').read_text())
assert d['first_E_prefix_threshold']==35 and d['head129_prefix_threshold']==69
original=int(c['original_root']);root=original^(1<<68)
rows=trajectory(root,0,193);baseline=[int(x,16) for x in c['baseline_rows_hex']]
assert root&((1<<35)-1)==original&((1<<35)-1)
assert all(rows[t]&1==b for t,b in anc.word_heads(anc.E,1).items())
target=anc.word_heads(anc.E+anc.A*4+anc.E,1)
word=lambda rr,st:sum((rr[st+k]>>7&1)<<k for k in range(14))
masks=abstract(original,35,193)
assert all(masks[t][0]!=3 and int(masks[t][0]==2)==b for t,b in anc.word_heads(anc.E,1).items())
front=[]
for t,(x,y) in enumerate(zip(baseline,rows)):
 z=x^y;front.append(None if not z else (z&-z).bit_length())
result={'root_tick0':str(root),'original_root':str(original),'changed_cell':69,
 'first_E_preserved':True,'full_ancestry_preserved':True,'firstE_forced_by_low35':True,
 'head129_before':baseline[129]&1,'head129_after':rows[129]&1,
 'prediction_head129_flips':bool((baseline[129]^rows[129])&1),
 'first_different_sample':next((t for t in range(1,194,2) if (baseline[t]^rows[t])&1),None),
 'all_different_samples':[t for t in range(1,194,2) if (baseline[t]^rows[t])&1],
 'first_target_failure':next((t for t,b in target.items() if rows[t]&1!=b),None),
 'bad_EA4E':[t for t,b in target.items() if rows[t]&1!=b],
 'source_inputs_before':{str(t):word(baseline,t) for t in (67,81,95,109)},
 'source_inputs_after':{str(t):word(rows,t) for t in (67,81,95,109)},
 'source109_low7_after':rows[109]&127,'row125_low7_after':rows[125]&127,
 'first_damage_cell_each_tick':front,'rows_hex':[hex(x) for x in rows],
 'scope':'One exact root mutation, original ancestry and full firstE preserved. No uniform influence or fullE4 existence inferred.'}
(a.out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
print('THRESHOLD_FLIP_FIXED_TEST_PASS');print(json.dumps({k:v for k,v in result.items() if k not in ('rows_hex','first_damage_cell_each_tick')}))
