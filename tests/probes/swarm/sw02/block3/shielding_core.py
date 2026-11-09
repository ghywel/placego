#!/usr/bin/env python3
"""Propagation-only shielding explanation and original-CNF blocker export."""
import argparse,json
from pathlib import Path
import physical_47 as phys
import physical_ancestry as anc
from untrapped_prefix import prefix_case,abstract


def prepare(out,image,prefix):
    out.mkdir(parents=True,exist_ok=True)
    c=json.loads((image/'prepare.json').read_text())['controls']['chaos']
    a=json.loads((prefix/'prepare.json').read_text());root=int(c['original_root']);rows=[int(x,16) for x in c['baseline_rows_hex']]
    C,off,W=prefix_case(root,70,193,{})
    vals,log,bad=phys.propagate(C);assert bad is None and phys.replay_units(C,log,bad)==vals
    reason={abs(v):i for v,i in log};todo=[off[129]+1];seen=set();leaf=set()
    while todo:
        v=todo.pop()
        if v in seen:continue
        seen.add(v);cl=C[reason[v]]
        if len(cl)==1:
            if v!=1:assert 2<=v<=71;leaf.add(v)
        else:todo.extend(abs(z) for z in cl if abs(z)!=v)
    literals=[v if vals[v] else -v for v in sorted(leaf)]
    core,co,cw=phys.generate(129,{129:0});core += [[v] for v in literals]
    vv,ll,bb=phys.propagate(core);assert bb is not None;phys.replay_units(core,ll,bb)
    phys.dimacs(out/'core.cnf',core,co[-1]);(out/'core.drup').write_text('0\n')
    clause=[-v for v in literals]
    for H,word in [(193,anc.E+anc.A*4+anc.E),(359,anc.E+anc.A*4+anc.E+anc.A*7+anc.E)]:
        cnf,fo,fw=phys.generate(H,anc.word_heads(word,1))
        info=phys.dimacs(out/f'original{H}.cnf',cnf,fo[-1])
        if H==359:assert info['sha256']=='21b425011ebc816994a2dfe221539ca2da6a5900b23d1f7009c9bbe26d70426c'
        vv,ll,bb=phys.propagate(cnf+[[x] for x in literals]);assert bb is not None;phys.replay_units(cnf+[[x] for x in literals],ll,bb)
        (out/f'blocker{H}.drup').write_text(' '.join(map(str,clause))+' 0\n')
    # Minimal-prefix threshold within unary-domain propagation, NOT semantic minimality.
    th=list(range(1,195));thresholds=[th]
    for t in range(193):
        new=[]
        for i in range(len(th)-1):
            l=0 if i==0 else th[i-1]
            b=(rows[t]>>i)&1;d=(rows[t]>>(i+1))&1
            o=min(v for bit,v in ((b,th[i]),(d,th[i+1])) if bit) if b|d else max(th[i],th[i+1])
            new.append(max(l,o))
        th=new;thresholds.append(th)
    assert all((thresholds[t][p]<=70)==(m!=3) for t,row in enumerate(a['abstract_rows']) for p,m in enumerate(row))
    Eheads=anc.word_heads(anc.E,1);ke=max(thresholds[t][0] for t in Eheads);kh=thresholds[129][0]
    for K in sorted({ke-1,ke,kh-1,kh}):
        masks=abstract(root,K,193)
        assert all((thresholds[t][p]<=K)==(m!=3) for t,row in enumerate(masks) for p,m in enumerate(row))
    # The compact certainty-front recurrence is independent of CNF bookkeeping.
    K=70;front=[]
    for t in range(194):
        width=194-t;K=min(K,width);front.append(K)
        assert K==next((i for i,m in enumerate(a['abstract_rows'][t]) if m==3),len(a['abstract_rows'][t]))
        if t<193 and K:K-=int((rows[t]>>(K-1)&1)==0)
    inputs={}
    for st in (67,81,95,109):
        w=sum((rows[st+i]>>7&1)<<i for i in range(14));assert w==808
        assert all(a['abstract_rows'][st+i][7]!=3 for i in range(14));inputs[st]=w
    trunks={}
    for w in (808,4520):
        q=64;rr=[q]
        for k in range(14):
            q=anc.step(q|((w>>k&1)<<7),anc.drive(109+k))&127;rr.append(q)
        trunks[w]=rr
    assert trunks[808]==[r&127 for r in rows[109:124]]
    result={'root_core_cells':[abs(x)-1 for x in literals],'root_core_literals':literals,'root_core_size':len(literals),
      'blocker_clause':clause,'reason_nodes':len(seen),'minimality_claim':False,
      'threshold_kind':'Exact minimum fixed-prefix length within unary-domain propagation only',
      'first_E_prefix_threshold':ke,'head129_prefix_threshold':kh,
      'prefix_thresholds_sampled_heads':{str(t):thresholds[t][0] for t in range(1,194,2)},
      'certainty_front':front,'four_A_inputs':inputs,'source109_trunks':trunks,
      'input_difference_times':[109+k for k in range(14) if (808^4520)>>k&1],
      'original359_CNF_hash_unchanged':True,'original193_and359_blockers_RUP':True,
      'native_certificates_pending':True}
    (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print('SHIELDING_CORE_PREPARE_PASS');print(json.dumps({k:v for k,v in result.items() if k not in ('certainty_front','prefix_thresholds_sampled_heads','source109_trunks')}))


def check(out):
    for name in ('oldcontrol','repair129','core'):
        assert 's VERIFIED' in (out.parent/(name+'-drat.stdout')).read_text()
        assert 's VERIFIED UNSAT' in (out.parent/(name+'-cake.stdout')).read_text()
    assert 's VERIFIED UNSAT' not in (out.parent/'false-cake.stdout').read_text()
    assert 'empty clause not derived at end of proof' in (out.parent/'false-cake.stderr').read_text()
    for H in (193,359):
        assert 's DERIVATION' in (out.parent/f'blocker{H}.stdout').read_text()
        assert json.loads((out.parent/f'blocker{H}.receipt.json').read_text())['returncode']==1
    print('SHIELDING_NATIVE_CERTIFICATES_PASS')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=['prepare','check']);p.add_argument('--out',type=Path,required=True);p.add_argument('--image',type=Path);p.add_argument('--prefix',type=Path);a=p.parse_args()
    if a.phase=='prepare':prepare(a.out,a.image,a.prefix)
    else:check(a.out)
