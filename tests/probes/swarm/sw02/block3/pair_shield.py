#!/usr/bin/env python3
"""One order-two relational shielding test; no width or prefix sweep."""
import argparse,itertools,json
from pathlib import Path
import physical_ancestry as anc
from image_ancestry_audit import trajectory
from untrapped_prefix import abstract
PAIRS=list(itertools.product((0,1),repeat=2));QUADS=list(itertools.product((0,1),repeat=4))

def prune(S):
    F=[{0,1}]
    for edge in S:F.append({b for a,b in edge if a in F[-1]})
    B=[set() for _ in F];B[-1]={0,1}
    for i in range(len(S)-1,-1,-1):B[i]={a for a,b in S[i] if b in B[i+1]}
    return [{(a,b) for a,b in e if a in F[i] and b in B[i+1]} for i,e in enumerate(S)]

def evolve(S,t):
    N=[]
    for i in range(len(S)-1):
        if i==0:
            N.append({(anc.drive(t+1),a^(b|c)) for a,b in S[0] for bb,c in S[1] if b==bb})
        else:
            N.append({(a^(b|c),b^(c|d)) for a,b,c,d in QUADS if (a,b) in S[i-1] and (b,c) in S[i] and (c,d) in S[i+1]})
    return prune(N)

def run(root,K,H):
    W=H+1;dom=[{anc.drive(0)}]+[{root>>i&1} if i<K else {0,1} for i in range(W)]
    S=[set(itertools.product(dom[i],dom[i+1])) for i in range(W)];rr=[S]
    for t in range(H):S=evolve(S,t);assert all(S);rr.append(S)
    return rr

p=argparse.ArgumentParser();p.add_argument('--image',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
root=int(json.loads((a.image/'prepare.json').read_text())['controls']['chaos']['original_root'])
# Every concrete completion in fixed small cones remains in the abstract relation.
for low in range(8):
    rr=run(low,3,9)
    for tail in range(128):
        rows=trajectory(low|(tail<<3),0,9)
        for t,S in enumerate(rr):
            cell=[anc.drive(t)]+[rows[t]>>i&1 for i in range(10-t)]
            assert all((cell[i],cell[i+1]) in edge for i,edge in enumerate(S))
rr=run(root,68,129);uu=abstract(root,68,129)
heads={t:sorted({b for _,b in S[0]}) for t,S in enumerate(rr)}
# Pair projection must refine the unary-domain overapproximation.
for t,S in enumerate(rr):
    for i,edge in enumerate(S):assert all(uu[t][i]>>b&1 for _,b in edge)
baseline=trajectory(root,0,129)
assert all((anc.drive(t),baseline[t]&1) in rr[t][0] for t in range(130))
encoded=[[[2*x+y for x,y in sorted(e)] for e in S] for S in rr]
result={'fixed_prefix':68,'horizon':129,'small_concrete_controls':1024,
 'head129_values':heads[129],'prediction_pair_proves_black129':heads[129]==[1],
 'unary_head129_mask':uu[129][0],'first_unknown_sample':next((t for t in range(1,130,2) if len(heads[t])>1),None),
 'heads':heads,'pair_rows':encoded,'refines_unary':True,
 'scope':'Sound adjacent-pair overapproximation with same root ancestry; unknown projections do not prove dependence.'}
(a.out/'result.json').write_text(json.dumps(result,indent=2)+'\n');print('PAIR_SHIELD_FIXED_AUDIT_PASS');print(json.dumps({k:v for k,v in result.items() if k not in ('heads','pair_rows')}))
