#!/usr/bin/env python3
"""All16 completions just outside one saved past head cone; no seed search."""
import argparse,json,hashlib
from pathlib import Path
import physical_ancestry as anc

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--prior',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    prior=json.loads(a.prior.read_text());base=next(c for c in prior['cases'] if c['name']=='sparse_positive_past')
    assert base['origin']==81 and base['all_past_heads_match'] and base['completion']['older_label']==4520
    root=int(base['root']);assert root.bit_length()<=113
    wanted={t:b for t,b in anc.word_heads(anc.E+anc.A*4+anc.E,1).items() if t>=81};cases=[]
    for tail4 in range(16):
        x=root|(tail4<<113);rr=[x]
        cells=[x>>i&1 for i in range(235)]
        for t in range(81,198):
            assert rr[-1]==sum(v<<i for i,v in enumerate(cells))
            if t==197:break
            rr.append(anc.step(rr[-1],anc.drive(t)))
            cells=[(anc.drive(t) if i==0 else cells[i-1])^(cells[i]|(cells[i+1] if i+1<len(cells) else 0)) for i in range(len(cells))]
        label=sum((rr[28+k]>>7&1)<<k for k in range(14))
        assert label==4520 and all(rr[t-81]&1==b for t,b in wanted.items())
        low5=rr[112]&31;head197=rr[116]&1
        # Carried GC2711/GC2714 image-black gap2 criterion.
        assert head197==int(low5 in (17,25))
        cases.append({'tail4':tail4,'root':str(x),'seam_low5':low5,'head197':head197,
                      'older_label':label,'all_past_heads81_to193':True})
    good=[x['tail4'] for x in cases if x['head197']==1]
    result={'input_sha256':hashlib.sha256(a.prior.read_bytes()).hexdigest(),'fixed_first113':str(root),'origin':81,
            'free_root_cells':[114,115,116,117],'query':'repair first future A head197 with all past heads81..193 unchanged',
            'cases':cases,'repairs':good,'count':len(good),'causal_support_cells':117,
            'arbitrary_higher_tail_irrelevant_to_head197':True,'original_pre81_ancestry_claimed':False,
            'full_future_or_full_target_claimed':False,'both_exact_representations_pass':True}
    (a.out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print('JOINT4520_TAIL_GUARD_TABLE_PASS')
    print(json.dumps({'repair_count':len(good),'tail4':good,'seam_low5_values':sorted({c['seam_low5'] for c in cases})}))

if __name__=='__main__':main()
