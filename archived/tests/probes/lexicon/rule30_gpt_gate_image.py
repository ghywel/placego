#!/usr/bin/env python3
"""GC405: full one-update local image replacing GC404's single gate.
Preregistered P1: the image of time3 columns1..9=a,1,1-a,a,0,v,w,z,u
with arbitrary later exterior forces time8 antecedent rows into A/B (0.6).
Counterfactual: still-earlier exterior correlations are essential.
Controls: original4096 initial rows lie in image; reverse-bit integer
step independently agrees with scalar every row. Unexpected check: image
is exactly GC403's relation + GC404 inequality + (h=a,k=1 => l=1).
OUTCOME: P1 HELD:18 local image states,576 completed rows,232 with
antecedent and no A/B failures. Original4096 and reverse-bit controls PASS.
The three explicit conditions equal the image exactly. A subsequent hand
case analysis is proposed in RULE30-GPT GC405; it awaits second reading.
No long preparation or death127 inference.
"""
import itertools,json
from rule30_gpt_gate_bridge import evolve,pattern


def reverse(row,start,n):
    for t in range(start,start+n):
        b=len(row)-1
        raw=sum(x << (b-i) for i,x in enumerate(row))
        out=(raw>>1)^(raw|(raw<<1))
        row=[(t+1)%2]+[(out>>(b-i))&1 for i in range(1,b)]
    return row


def main():
    image=set()
    for a,v,w,z,u in itertools.product((0,1),repeat=5):
        image.add((a,a^v,v|w,v^(w|z),w^(z|u)))
    clauses=set()
    for a,h,k,l,r in itertools.product((0,1),repeat=5):
        old=any(h==(a^v) and k==(v|w) for v,w in itertools.product((0,1),repeat=2))
        if old and (k or l<=r) and (h!=a or not k or l):
            clauses.add((a,h,k,l,r))
    assert image==clauses
    count=pos=bad=final_bad=0; witness=None
    for a,h,k,l,r in sorted(image):
        for tail in itertools.product((0,1),repeat=5):
            row=[0,0,1-a,0,1,h,k,l,r]+list(tail)
            cut=evolve(row,4,4)
            assert cut==reverse(row,4,4)
            count+=1
            if cut[6]:
                pos+=1
                if not pattern(cut):
                    bad+=1;final_bad+=not evolve(cut,8,4)[5]
                    if witness is None:witness=row
    for free in range(4096):
        a=free&1
        row=[0,a,1,1,1,0,0]+[(free>>j)&1 for j in range(1,12)]
        r4=evolve(row,0,4)
        assert (a,*r4[5:9]) in image
    print(json.dumps({'image_size':len(image),'explicit_conditions_exact':True,
        'rows':count,'positive':pos,'cover_failures':bad,
        'post_hoc_final_failures':final_bad,'first_failure':witness,
        'original_controls':4096,'reverse_bit_control':'PASS',
        'P1':'HELD' if bad==0 else 'REFUTED'},indent=2))


if __name__=='__main__':main()
