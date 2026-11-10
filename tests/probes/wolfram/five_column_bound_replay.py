#!/usr/bin/env python3
"""S09 worked cell. Prediction: [True,128,70,8,3,16], already independently
checked in GC2810. No trajectory census. Local replays for the notebook.
Counterfactual: mismatch blocks the numerical cell. Record searched: GC2810,
P2-3.1, ColumnTransfer and PR253. Does not carry the all-time Lean proof.
"""
from itertools import product
rule=lambda a,b,c:a^(b|c)
H=lambda u:max(0,2-sum(u[1:]))
def damaged(u):return 0 if not any(u) else H(u)
slacks=[];mirror=damage=linear=0
for w in product((0,1),repeat=7):
    u=w[1:6];v=tuple(rule(*w[i:i+3]) for i in range(5))
    k=sum(u)-3;slacks.append(H(v)-H(u)-k)
    mirror+=H(v[::-1])-H(u[::-1])<k
    damage+=damaged(v)-damaged(u)<k
    linear+=H(tuple(w[i]^w[i+1]^w[i+2] for i in range(5)))-H(u)<k
out=[all(s>=0 for s in slacks),len(slacks),slacks.count(0),mirror,damage,linear]
assert out==[True,128,70,8,3,16]
print('{True, 128, 70, 8, 3, 16}')
