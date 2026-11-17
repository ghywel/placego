#!/usr/bin/env python3
"""Forced shared seam completion and exact two-launch observation; no solver.

Only generated high-tail states are used. The arbitrary-state space is NOT
claimed reachable. Full original-head acceptance remains a separate guard.
"""
import argparse, hashlib, json
from pathlib import Path
import physical_ancestry as anc

SEAM,CUT,WORD=193,103,4520
MASK=lambda n:(1<<n)-1

def trajectory(root,start,end):
    out=[root]
    for t in range(start,end):out.append(anc.step(out[-1],anc.drive(t)))
    return out

def scalar(root,start,end):
    a=[root>>i&1 for i in range(root.bit_length()+end-start+3)];out=[]
    for t in range(start,end+1):
        out.append(sum(v<<i for i,v in enumerate(a)))
        a=[(anc.drive(t) if i==0 else a[i-1])^(a[i]|(a[i+1] if i+1<len(a) else 0)) for i in range(len(a))]
    return out

def word(rows,start):return sum((rows[start+k]>>7&1)<<k for k in range(14))

def extract(seam,origin,wanted):
    m=SEAM-origin;assert m>=CUT
    near=[0]*m;far=[0]*m;bad_boundary=[];bad_head=[];heads={}
    for j in range(max(seam.bit_length(),m+1),CUT,-1):
        value=seam>>(j-1)&1;cur=[0]*m
        for s in range(m-1,-1,-1):
            pos=j-m+s
            if pos<0:break
            value ^= near[s]|far[s];cur[s]=value;t=origin+s
            if pos==0 and value!=anc.drive(t):bad_boundary.append(t)
            if pos==1:
                heads[t]=value
                if t in wanted and value!=wanted[t]:bad_head.append(t)
        far,near=near,cur
    first=m-CUT
    assert origin+first==90
    return {'near':near[first:],'far':far[first:],
            'band64':(seam>>CUT)&MASK(64),'high':seam>>CUT,
            'prior_bad_boundary':bad_boundary,'prior_bad_head':sorted(bad_head),
            'prior_heads':heads,'origin':origin,'full_root0_ancestry':origin==0,
            'within_original_seam_width':seam.bit_length()<=553}

def complete(state,wanted):
    near=state['near'][:];far=state['far'][:];p=0;heads={};bad=[];label=0;source=0;checks=[]
    for j in range(CUT,0,-1):
        b=SEAM-j;assert len(near)==len(far)==j
        rs=[x|y for x,y in zip(near,far)]
        # Ascending telescoping starts at the required center bit.
        cur=[anc.drive(b)]
        for r in rs:cur.append(cur[-1]^r)
        bit=cur[-1];p|=bit<<(j-1)
        # Independent descending inverse reconstruction with this forced bit.
        v=bit;rev=[0]*j
        for i in range(j-1,-1,-1):v^=rs[i];rev[i]=v
        assert rev==cur[:-1] and v==anc.drive(b)
        t=b+1;heads[t]=cur[1]
        if t in wanted and heads[t]!=wanted[t]:bad.append(t)
        if 79<=j<=92:
            k=92-j;t=109+k
            parity=0
            for r in rs[:8]:parity^=r
            value=anc.drive(101+k)^parity
            assert t-b==8 and value==cur[8]
            label|=value<<k
            checks.append({'k':k,'seam_cell':j,'boundary_time':b,'or_terms':rs[:8],
                           'xor_or':parity,'required_xor_or':(WORD>>k&1)^(k&1),'value':value})
        q=j-84
        if 1<=q<=7:
            assert b==109-q
            source|=cur[q]<<(q-1)
        near,far=cur[1:-1],near[1:]
    assert not near and not far
    return {'prefix103':p,'older_label':label,'older_source7':source,'syndromes':checks,
            'remaining_heads':heads,'remaining_bad_head':bad}

def future(prefix103,band64,fibre):
    small=prefix103
    for k in range(82):small=anc.step(small,anc.drive(193+k))&MASK(102-k)
    # Exactly21 cells remain; independently observe its14-tick input word.
    rows=trajectory(small,275,288);w=word(rows,0)
    assert (small in fibre)==(small&127==64 and w==WORD)
    full=trajectory((band64<<CUT)|prefix103,193,359)
    assert full[82]&MASK(21)==small and word(full,82)==w
    expected=anc.word_heads(anc.A*7+anc.E,193)
    bad=[t for t,b in expected.items() if full[t-193]&1!=b]
    return {'source21':small,'source7':small&127,'label':w,'in_4520_fibre':small in fibre,
            'full_future_bad_heads':bad,'first167':str((band64<<CUT)|prefix103)}

def check_case(name,root,origin,fibre):
    rr=trajectory(root,origin,359);assert rr==scalar(root,origin,359)
    M=rr[193-origin];wanted={t:b for t,b in anc.word_heads(anc.E+anc.A*4+anc.E,1).items() if t>=origin}
    state=extract(M,origin,wanted);assert not state['prior_bad_boundary']
    got=complete(state,wanted);assert got['prefix103']==M&MASK(CUT)
    assert got['older_label']==word(rr,109-origin)
    assert got['older_source7']==rr[109-origin]&127
    for t,b in state['prior_heads'].items():assert b==rr[t-origin]&1
    for t,b in got['remaining_heads'].items():assert b==rr[t-origin]&1
    f=future(got['prefix103'],state['band64'],fibre)
    assert f['source21']==rr[275-origin]&MASK(21) and f['label']==word(rr,275-origin)
    actual_bad=[t for t,b in wanted.items() if rr[t-origin]&1!=b]
    assert sorted(state['prior_bad_head']+got['remaining_bad_head'])==actual_bad
    # A changed low bit cannot change the incoming state. Its full ancestry
    # must fail, and completion restores the unique original low prefix.
    mutant=M^(1<<91);ms=extract(mutant,origin,wanted);assert ms==state
    back=mutant;failed=None
    for t in range(192,origin-1,-1):
        back=anc.inverse(back,anc.drive(t))
        if back is None:failed=t;break
    assert failed is not None
    if origin==0:
        reference=anc.diagonal(M,193,wanted,cut=CUT)
        assert reference['rows']==rr[:194] and reference['accepted']==(not actual_bad)
        assert root.bit_length()<=360 if state['within_original_seam_width'] else True
    return {'name':name,'root':str(root),'origin':origin,'seam':str(M),'seam_width':M.bit_length(),
            'state':state,'completion':got,'future':f,
            'all_clause_free_scalar_inverse_controls':True,'mutant_first_bad_boundary':failed,
            'all_past_heads_match':not actual_bad,
            'original_full_target':origin==0 and state['within_original_seam_width'] and not actual_bad and not f['full_future_bad_heads']}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--fibres',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    saved=json.loads(a.fibres.read_text());fibre={x for row in saved if row['word']==WORD for x in row['roots']}
    # Directly replay the saved singleton fibre, not a new window census.
    assert len(fibre)==256
    for r in sorted(fibre):assert r&127==64 and word(trajectory(r,109,122),0)==WORD
    (a.out/'fibre4520.json').write_text(json.dumps(sorted(fibre))+'\n')
    seed=2135555;shifted=trajectory(seed,0,330)[-1]
    positive=422256424234816
    fixtures=[('seed0',seed,0),('root19',19,0),('known_second_E_future',shifted,0),
              ('sparse_positive_past',positive,81),('one_outside_support_bit',positive^(1<<49),81)]
    results=[check_case(n,r,o,fibre) for n,r,o in fixtures]
    assert results[2]['future']['label']==WORD
    assert results[3]['completion']['older_label']==results[4]['completion']['older_label']==WORD
    diff={'old_label_unchanged':True,'changed_root_cell':50,'future_labels':[r['future']['label'] for r in results[3:]],
          'future_label_changed':results[3]['future']['label']!=results[4]['future']['label'],
          'scope':'actual histories from81, no earlier0..80 ancestry or full target claimed'}
    # Check all remaining boundary-forced cells on the saved source relation.
    outcome={'fibre_count':len(fibre),'fibre_sha256':hashlib.sha256((a.out/'fibre4520.json').read_bytes()).hexdigest(),
             'input_sha256':hashlib.sha256(a.fibres.read_bytes()).hexdigest(),'cases':results,'fixed_bit50_control':diff,
             'interface':{'generated_pair_bits':206,'actual_high_band_bits':64,'prior_acceptance_required':True,
                          'arbitrary_state_reachability_claimed':False,'full_167_future_retained':True},'no_solver_or_new_census':True}
    (a.out/'result.json').write_text(json.dumps(outcome,indent=2)+'\n')
    print('JOINT4520_FORCED_COMPLETION_AND_PARITY_PASS')
    print(json.dumps({'labels':[(r['name'],r['completion']['older_label'],r['future']['label']) for r in results],'bit50':diff}))

if __name__=='__main__':main()
