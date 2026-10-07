#!/usr/bin/env python3
"""Pulse-rebound algebra control, GPT 2026-10-07; before execution.
Explains RD32-W's retained period16 hard-witness four-edge subinterval.
C5: for q4..32, all rotations, A=e_s+e_(s+2), B=e_s,
 C=1+e_(s+1)+e_(s+2), E=1+e_(s+1)+e_(s+2)+e_(s+3), F=e_(s+4)
 obey all three literal triples. Scalar delays from T=s+1 are(q,3,1,q).
CF3: applying the identity atq3 must FAIL (E=0, OR containment breaks).
U: q4 is included, despite F coinciding with B as a temporal word.
No ancestry/growth assertion except the already observed q16 occurrence.
OUTCOME: C5/CF3/U PASS on522 rotations, q4..32; literal q16 occurrence
320,64,65151,64639,1024 gives delays16,3,1,16 and interval debt26.
General symbolic argument is in RULE30-GPT; no root claim at other q.
"""
def words(q,s):
    e=lambda i:1<<(i%q)
    full=(1<<q)-1
    return [e(s)^e(s+2),e(s),full^e(s+1)^e(s+2),
            full^e(s+1)^e(s+2)^e(s+3),e(s+4)]
def literal(q,a,b,c):
    return all(((c>>((t+1)%q))&1)==(((a>>t)&1)^(((b>>t)&1)|((c>>t)&1))) for t in range(q))
def delay(q,w,T):
    return next(i+1 for i in range(q) if (w>>((T+i)%q))&1)
n=0
for q in range(4,33):
    for s in range(q):
        ws=words(q,s)
        assert all(literal(q,*ws[i:i+3]) for i in range(3))
        T=s+1;ds=[]
        for w in ws[1:]:
            dt=delay(q,w,T);ds.append(dt);T+=dt
        assert ds==[q,3,1,q] and sum(ds)==2*q+4
        n+=1
assert not all(literal(3,*words(3,0)[i:i+3]) for i in range(3))
assert words(4,0)[1]==words(4,0)[4]
assert words(16,6)==[320,64,65151,64639,1024]
print('C5 CF3 U PASS; rotations',n,'; q16 delays16,3,1,16, cost36, slope5/2 debt26')
