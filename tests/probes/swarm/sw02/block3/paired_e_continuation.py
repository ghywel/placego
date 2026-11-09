#!/usr/bin/env python3
"""Fixed actual-history comparison after GC2773; no witness search or census."""
import argparse, json
from pathlib import Path
import joint_4520_state as joint
import physical_ancestry as anc
from transient_audit_controls import run as audit


def scan_trace(state):
    near,far=state['near'][:],state['far'][:];out=[];prefix=0
    for j in range(103,0,-1):
        b=193-j;ors=[a|c for a,c in zip(near,far)];v=anc.drive(b);cur=[v]
        for r in ors:v^=r;cur.append(v)
        out.append({'j':j,'b':b,'near':near,'far':far,'ors':ors,'forced':cur[-1]})
        prefix|=cur[-1]<<(j-1)
        near,far=cur[1:-1],near[1:]
    assert prefix==joint.complete(state,{})['prefix103']
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--prior',type=Path,required=True)
    ap.add_argument('--cloud-json',type=Path,required=True);ap.add_argument('--trap-lean',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    cloud=audit(a.cloud_json,a.trap_lean)
    (a.out/'cloud-audit.json').write_text(json.dumps(cloud,indent=2)+'\n')
    prior=json.loads(a.prior.read_text());old=next(x for x in prior['cases'] if x['name']=='sparse_positive_past')
    r=joint.trajectory(2135555,0,496)[-1]&joint.MASK(360)
    rows=joint.trajectory(r,0,359);assert rows==joint.scalar(r,0,359)
    wanted=anc.word_heads(anc.E+anc.A*4+anc.E,1)
    st=joint.extract(rows[193],0,wanted);co=joint.complete(st,wanted)
    assert not st['prior_bad_boundary'] and co['prefix103']==rows[193]&joint.MASK(103)
    assert co['older_label']==joint.word(rows,109)==4520
    earlier_bad=[t for t,b in wanted.items() if rows[t]&1!=b]
    assert earlier_bad==sorted(st['prior_bad_head']+co['remaining_bad_head'])
    common=anc.word_heads(anc.E+anc.A*4+anc.E,1)
    assert all(rows[t]&1==b for t,b in common.items() if t>=81)
    assert earlier_bad and max(earlier_bad)<81
    histories=[{'name':'sparse_positive','root':old['root'],'origin':81,'seam':old['seam'],
                'state':old['state'],'completion':old['completion']},
               {'name':'real_second_E','root':str(r),'origin':0,'seam':str(rows[193]),'state':st,'completion':co}]
    traced=[scan_trace(x['state']) for x in histories]
    for x,tr in zip(histories,traced):
        x['scan']=tr;x['low7']=int(x['seam'])&127;x['low5']=int(x['seam'])&31
        future=joint.trajectory(int(x['seam']),193,207)
        x['next_A_heads']={str(t):future[t-193]&1 for t in range(193,208,2)}
        x['first_A_matches']=all(future[t-193]&1==b for t,b in anc.word_heads(anc.A,193).items())
        x['tail_rows_189_193']=[hex(y) for y in joint.trajectory(int(x['root']),x['origin'],193)[189-x['origin']:]]
    comparison=[]
    for left,right in zip(*traced):
        assert left['j']==right['j']
        comparison.append({'j':left['j'],'b':left['b'],'different_or_rows':[left['b']+i for i,(x,y) in enumerate(zip(left['ors'],right['ors'])) if x!=y],
                           'different_pair_rows':[left['b']+i for i,(x,y,z,w) in enumerate(zip(left['near'],right['near'],left['far'],right['far'])) if (x,z)!=(y,w)],
                           'forced':[left['forced'],right['forced']]})
    assert histories[0]['low5']==23 and histories[1]['low5']==17
    assert not histories[0]['first_A_matches'] and histories[1]['first_A_matches']
    assert all(x['completion']['older_label']==4520 for x in histories)
    result={'histories':histories,'comparison':comparison,'real_earlier_original_head_failures':earlier_bad,
            'same_prescribed_heads_81_193':True,'full_EA4E_witness':False,
            'scope':'Fixed histories only. First case has origin81, second has true root0 ancestry but fails earlier original heads. No arbitrary-state graft or reachability inference.'}
    (a.out/'paired-state.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PAIRED_E_CONTINUATION_AND_CLOUD_AUDIT_PASS')
    print(json.dumps({'low5':[x['low5'] for x in histories],'first_A':[x['first_A_matches'] for x in histories],
                      'last_five':comparison[-5:],'earlier_bad':earlier_bad}))

if __name__=='__main__':main()
