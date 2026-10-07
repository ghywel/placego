#!/usr/bin/env python3
"""GC403: test a hand-derived time4 relation as a sufficient bridge.
Preregistered in CLOUD-LOCAL before run: P1 all antecedent-positive rows
from (0,1-a,0,1,a XOR v,v OR w) land in G209 A or B after4 updates,
confidence0.5. Free columns7..13, supplied alternating wall times4..7.
Counterfactual: the actual anchor retains essential omitted correlations.
Controls: scalar vs packed every step; original4096 rows obey time4 relation.
Unexpected check releases h,k independently; retain any failing row.
OUTCOME: P1 REFUTED:768 relaxed rows,392 antecedent-positive,28 outside A/B.
Releasing h,k gives1024 rows,512 positive,84 outside A/B. All4096 initial
anchor controls PASS. Post hoc (not preregistered): all28 restricted failures
also give white at the final target, so this is a failed implication as well
as a failed pattern cover. Scalar/packed controls cover every evolved row.
This is a small sufficiency test, not a long wheel-preparation certificate.
"""
import itertools
import json


def step(row, wall):
    return [wall] + [row[j-1] ^ (row[j] | row[j+1]) for j in range(1,len(row)-1)]


def evolve(row, start, n):
    for t in range(start,start+n):
        packed=sum(b << j for j,b in enumerate(row))
        bits=((packed << 1) ^ (packed | (packed >> 1)))
        out=step(row,(t+1)%2)
        assert out[1:]==[(bits >> j)&1 for j in range(1,len(row)-1)]
        row=out
    return row


def pattern(r):
    return r[1:8]==[0,1,0,1,1,1,0] or [r[j] for j in (1,2,3,4,6)]==[1,1,1,0,1]


def test(restricted):
    count=pos=bad=final_bad=0; witness=None
    for a,h,k in itertools.product((0,1),repeat=3):
        if restricted and not any(h==(a^v) and k==(v|w) for v,w in itertools.product((0,1),repeat=2)):
            continue
        for tail in itertools.product((0,1),repeat=7):
            row=[0,0,1-a,0,1,h,k]+list(tail)
            end=evolve(row,4,4); count+=1
            if end[6]:
                pos+=1
                if not pattern(end):
                    bad+=1
                    final_bad+=evolve(end,8,4)[5]==0
                    if witness is None: witness={'initial':row,'cut':end}
    return {'rows':count,'antecedent_positive':pos,'violations':bad,'post_hoc_final_violations':final_bad,'witness':witness}


def main():
    controls=0
    for free in range(4096):
        a=free&1
        row=[0,a,1,1,1,0,0]+[(free >> j)&1 for j in range(1,12)]
        r3=evolve(row,0,3); r4=evolve(r3,3,1)
        assert r4[1:7]==[0,1-a,0,1,a^r3[6],r3[6]|r3[7]]
        controls+=1
    out={'original_anchor_controls':controls,'restricted':test(True),'released':test(False)}
    out['P1']='HELD' if out['restricted']['violations']==0 else 'REFUTED'
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
