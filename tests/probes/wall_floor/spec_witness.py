#!/usr/bin/env python3
"""spec_witness.py (Local, L1552): the witness's route of (phase, depth) against the third lock's strip, by the same metric as the chain, and the corridor's common word against the witness, phase by phase."""
import json,re,collections
ref=[l.strip()[::-1] for l in open('ref6.txt') if l.strip()]
def agree(r):
    best=(0,0)
    for p,x in enumerate(ref):
        k=0
        while k<len(r) and k<len(x) and (x[k]=='?' or x[k]==r[k]): k+=1
        if k>best[1]: best=(p,k)
    return best
d=json.load(open('witness_break_175_56.json'))
y=d['y0_by_offset']
row=[1]+[0]*8+y[::-1]
N=1300
b=row[-1]
while len(row)<N: b^=1; row.append(b)
x=sum(1<<i for i,c in enumerate(row) if c)
MASK=(1<<N)-1
fw=lambda v:(v^((v<<1)|(v<<2)))&MASK
def inv(yv):
    o=yv&1;p1=1;p2=0
    for j in range(1,N):
        c=((yv>>j)&1)^(p1|p2)
        o|=c<<j;p2=p1;p1=c
    return o
rows={0:x}
for k in range(1,112): rows[k]=fw(rows[k-1])
c=x
for k in range(-1,-41,-1):
    c=inv(c); rows[k]=c
def top(v,k,n=256):
    hi=569-3*k
    return ''.join('#' if (v>>(hi-i))&1 else '.' for i in range(min(n,hi+1)))
route=[(k,)+agree(top(rows[k],k)) for k in range(110,-41,-1)]
print('witness route, backward time, tick:phase:depth')
print(' '.join(f'{k}:{p}:{D}' for k,p,D in route))
W={k:top(rows[k],k) for k in rows}
json.dump({str(k):v for k,v in W.items()},open('witness_tops.json','w'))
# corridor
S=[];cur=None
for l in open('spec_run/out.txt'):
    if l.startswith('SPEC'):
        cur=[];S.append(cur);continue
    m=re.match(r'(-?\d+) (\d+) (\d+) ([#.]+)$',l)
    if m and cur is not None: cur.append((int(m[1]),int(m[2]),int(m[3]),m[4]))
S=[s for s in S if len(s)==96]
s0=S[0]
def lcp(a,b):
    k=0
    while k<min(len(a),len(b)) and a[k]==b[k]: k+=1
    return k
print('corridor rows against witness rows: for each corridor tick, the witness tick with the deepest common word')
for i in range(-20,12):
    r=next(q for q in s0 if q[0]==i)
    best=max(W,key=lambda k:lcp(r[3],W[k]))
    print(i,'phase',r[2],'lock depth',r[1],'best witness tick',best,'common depth',lcp(r[3],W[best]))
