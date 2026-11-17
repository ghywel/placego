#!/usr/bin/env python3
"""Exact local interface fibres and same-row label observer; no SAT or free seam.

The 23 input cells are the causal support of the existing four-register /
actual-top interface, not an enlarged window search. All histories below are
explicitly scoped: local cone, saved whole E, or actual seed (no target claim).
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import numpy as np
import physical_ancestry as anc
import a_block_history as hist

LABELS=(4482,4498,4520,4521,4522)
LAUNCH=(3357,4482,4498,4520,4521,4522,8797,9618,9640,9641,9642,14429,14941)


def encode(bits):return sum(int(b)<<i for i,b in enumerate(bits))


def local_fibres():
    roots=(np.arange(1<<16,dtype=np.uint64)<<np.uint64(7))|np.uint64(64)
    rr=[roots]
    for t in range(22):
        x=rr[-1];rr.append(((x<<np.uint64(1))|np.uint64(t&1))^(x|(x>>np.uint64(1))))
    # Independent scalar-cell representation, for every assignment and tick.
    cells=((roots[:,None]>>np.arange(47,dtype=np.uint64))&np.uint64(1)).astype(bool)
    for t in range(23):
        packed=np.pad(np.packbits(cells,axis=1,bitorder='little'),((0,0),(0,2)))
        assert np.array_equal(packed.copy().view('<u8').reshape(-1),rr[t])
        if t<22:
            left=np.empty_like(cells);right=np.empty_like(cells)
            left[:,0]=bool(t&1);left[:,1:]=cells[:,:-1]
            right[:,-1]=False;right[:,:-1]=cells[:,1:]
            cells=left^(cells|right)
    word=np.zeros(1<<16,dtype=np.uint64)
    for k in range(14):word|=((rr[k]>>np.uint64(7))&np.uint64(1))<<np.uint64(k)
    good=np.ones(1<<16,dtype=bool)
    for t in range(2,23,2):good &= (rr[t]&np.uint64(1))==int(t in (2,6,16,22))
    assert set(map(int,np.unique(word[good])))==set(LAUNCH)
    wrong_first=((roots<<np.uint64(1))|np.uint64(1))^(roots|(roots>>np.uint64(1)))
    assert np.all((wrong_first&1)!=(rr[1]&1))
    at=lambda t,p:(rr[t]>>np.uint64(p-1))&np.uint64(1)
    patch=sum(at(10,p)<<np.uint64(p-6) for p in range(6,11))
    state=[at(10,10),at(10,11),at(11,11),at(11,12)]
    top=[at(12,p) for p in (11,10,9,8)]
    code=sum(x<<np.uint64(i) for i,x in enumerate(state+top))
    later_input=at(12,8)
    out={};sets={};examples={}
    for w in LABELS+(14429,):
        mask=good&(word==w);assert mask.any()
        pats=sorted(map(int,np.unique(patch[mask])))
        codes,counts=np.unique(code[mask],return_counts=True);sets[w]=set(map(int,codes))
        inds=np.flatnonzero(mask)
        examples[w]={int(c):int(roots[inds[np.flatnonzero(code[inds]==c)[0]]]) for c in codes}
        for n in inds:
            # The five-cell two-tick law checks every retained local model.
            a,b,c,d,e=[int(patch[n])>>k&1 for k in range(5)]
            assert int(later_input[n])==a^(int(b==c)&(d|e))
        if w in LABELS:
            assert all(p&15==11 for p in pats) # physical cells6..9 = 1,1,0,1
        else:assert all(p&7==0 for p in pats)
        trunk=hist.trunk(64,w)
        assert np.all((rr[10][mask]&127)==trunk[10])
        out[str(w)]={'local_models':int(mask.sum()),'patch_codes_low_bit_cell6':pats,
                     'interface_codes_state_then_top':list(map(int,codes)),
                     'interface_counts':list(map(int,counts)),
                     'trunk0_to14':trunk,'full_E_realizability_of_each_model_claimed':False}
    collisions=[]
    for a,b in itertools.combinations(LABELS,2):
        shared=sorted(sets[a]&sets[b])
        item={'labels':[a,b],'common_codes':shared}
        if shared:
            c=shared[0];item['local_roots']=[str(examples[a][c]),str(examples[b][c])]
        collisions.append(item)
    suffix={w>>6 for w in LABELS};assert suffix=={70}
    return {'assignments':1<<16,'root_cells':23,'free_initial_bits':16,
            'max_observation_dependency':23,'all23_time_rows_scalar_checked':True,
            'wrong_phase_rejected':True,'A_then3_local_models':int(good.sum()),
            'common_input_bits6_to13_low_bit_first':[70>>k&1 for k in range(8)],
            'fibres':out,'local_interface_collisions':collisions,
            'not_a_whole_past_or_full_return_classification':True}


def observe(seam,depth,origin):
    near=[0]*depth;far=[0]*depth;rs=[0]*depth+[seam]
    events=[];snap={};word=0;candidates=set(LABELS);boundary=[]
    for j in range(max(seam.bit_length(),depth+1),0,-1):
        value=seam>>(j-1)&1;current=[0]*depth
        for s in range(depth-1,-1,-1):
            pos=j-depth+s
            if pos<0:break
            value ^= near[s]|far[s];current[s]=value
            if pos==0:
                if value!=anc.drive(origin+s):boundary.append(origin+s)
            else:rs[s]|=value<<(pos-1)
            k=origin+s-109
            if pos==8 and 0<=k<14:
                assert j==92-k
                word|=value<<k;candidates={w for w in candidates if w>>k&1==value}
                events.append({'seam_cell':j,'global_time':origin+s,'input_bit':k,'value':value,
                               'candidates_after_read':sorted(candidates)})
        far,near=near,current
        if j in (103,80,79):
            first=max(0,depth-j+1)
            snap[str(j)]={'first_global_live':origin+first,'pair_bits':2*(depth-first),
                          'near':''.join(map(str,near[first:])), 'far':''.join(map(str,far[first:]))}
    assert not boundary
    return {'word':word,'events':events,'snapshots_after_cell':snap,'rows':rs,
            'boundary_interval_checked':[origin,origin+depth-1],
            'not_a_prescribed_earlier_past_acceptance_claim':True}


def saved_scans(path):
    cases=json.loads(path.read_text());out=[];full_interfaces={}
    for case in cases:
        if case['answer'] is not True or case['word'] not in LABELS+(14429,):continue
        w=case['word'];root=int(case['witness']['root']);rr=anc.rows(root,85)
        assert rr==[int(x,16) for x in case['witness']['rows_hex']]
        got=observe(rr[-1],85,108);assert got.pop('rows')==rr and got['word']==w
        ref=anc.diagonal(rr[-1],85);assert ref['accepted'] and ref['rows']==rr
        assert [e['input_bit'] for e in got['events']]==list(range(14))
        state=[rr[11]>>9&1,rr[11]>>10&1,rr[12]>>10&1,rr[12]>>11&1]
        top=[rr[13]>>(p-1)&1 for p in (11,10,9,8)]
        code=encode(state+top);full_interfaces[w]=code
        got.update({'label':w,'source_frame_root':str(root),'seam193_if_origin108':str(rr[-1]),
                    'state4':state,'actual_top4':top,'interface_code':code,
                    'scope':'Saved whole-E history108..193, no earlier E/A4 ancestry',
                    'full_earlier_past_claimed':False})
        if w in LABELS:
            assert got['events'][-1]['candidates_after_read']==[w]
            first=next(e for e in got['events'] if e['candidates_after_read']==[w])
            got['first_unique_among_five_cell']=first['seam_cell']
        else:assert not got['events'][-1]['candidates_after_read']
        out.append(got)
    assert len(out)==6
    root=2135555;rr=anc.rows(root,193);actual=observe(rr[-1],193,0)
    assert actual.pop('rows')==rr
    actual['actual_seed_root']=root;actual['scope']='Actual seed control; target E/A4/E heads not asserted'
    actual['source_low7']=rr[109]&127
    assert actual['snapshots_after_cell']['103']['pair_bits']==204
    assert actual['snapshots_after_cell']['80']['pair_bits']==158
    assert actual['snapshots_after_cell']['79']['pair_bits']==156
    return {'saved_whole_E':out,'actual193_seed_control':actual,
            'full_E_selected_witness_interface_collisions':[
                [a,b,full_interfaces[a]] for a,b in itertools.combinations(LABELS,2)
                if full_interfaces[a]==full_interfaces[b]],
            'five_label_recognizer_completed_at_seam_cell':79,
            'old_band_end':80,'one_more_actual_seam_bit_needed_for_full_word_read':True}


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True)
    p.add_argument('--histories',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    result={'local':local_fibres(),'shared_row':saved_scans(a.histories),
            'histories_sha256':hashlib.sha256(a.histories.read_bytes()).hexdigest(),
            'no_SAT_or_independent_seam_selection':True}
    (a.out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print('FIVE_LABEL_LOCAL_FIBRES_AND_SAME_ROW_OBSERVER_PASS')
    print('Fibre models/patches',[(w,d['local_models'],d['patch_codes_low_bit_cell6']) for w,d in result['local']['fibres'].items()])
    print('Selected full-E collisions',result['shared_row']['full_E_selected_witness_interface_collisions'])


if __name__=='__main__':main()
