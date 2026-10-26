#!/usr/bin/env python3
"""Frozen bounded verification of the staircase hand lemma; see report.

Not a discovery census or a proof of endless alternation. The input argument
is the private reconstruction JSON. No image is read or edited here.
"""
import json
import resource
import signal
import sys
import time
from collections import Counter


def bit(n,i): return (n>>i)&1


def scalar(row):
    return [(30>>(4*a+2*b+c))&1 for a,b,c in zip(row,row[1:],row[2:])]


def cone(n,w,steps):
    rows=[n]
    for _ in range(steps):
        n=(n^((n>>1)|(n>>2))) & ((1<<(w-2))-1)
        w-=2
        rows.append(n)
    return rows


def check(left,z,y):
    h=len(left)
    assert all(v==1 for v in left)
    assert len(z)>=h+1 and len(y)>=h+2
    assert all(not(z[t]==z[t+1]==1) for t in range(h))
    s=next((t for t in range(h) if z[t]==z[t+1]==0),None)
    if s is None:
        assert all(z[t]!=z[t+1] for t in range(h))
        return 'alternates', None
    assert all(v==0 for v in z[s:h+1])
    assert all(v==1 for v in y[s:h+2])
    return 'successor',s


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(60,60))
    resource.setrlimit(resource.RLIMIT_FSIZE,(2*1024**2,2*1024**2))
    signal.alarm(75)
    start=time.monotonic()
    totals=[]; controls=0; cf2=None
    for h in range(1,7):
        w=2*h+5;j=h+1
        counts=Counter(); delays=Counter()
        for n in range(1<<w):
            rows=cone(n,w,h+1)
            if w<=9 or n%256==0:
                rr=[bit(n,i) for i in range(w)]
                for t in range(h+2):
                    assert rr==[bit(rows[t],i) for i in range(w-2*t)]
                    if t<h+1:rr=scalar(rr)
                controls+=1
            left=[bit(rows[t],j-t) for t in range(h)]
            z=[bit(rows[t],j+1-t) for t in range(h+2)]
            y=[bit(rows[t],j+2-t) for t in range(h+2)]
            if all(left):
                kind,s=check(left,z,y);counts[kind]+=1
                if s is not None:delays[s]+=1
            elif cf2 is None and left[0] and z[0]==z[1]==0 and any(z[2:h+1]):
                cf2=dict(h=h,word=''.join(str(bit(n,i)) for i in range(w)),left=left,z=z,y=y)
        assert counts['alternates'] and counts['successor'], 'Both branches must be exercised'
        rec=dict(h=h,total_cones=1<<w,counts=dict(counts),first00=dict(delays))
        totals.append(rec); print(json.dumps({'cone_complete':rec}),flush=True)
        assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 128*1024**2
    assert cf2 is not None, 'Missing-hypothesis mutant must fail'
    # Counterfactual externally chosen y=1,0 yields z=0,0,1; genuine y1=1.
    fake_z=[0]
    for y0 in [1,0]:fake_z.append(1^(fake_z[-1]|y0))
    assert fake_z==[0,0,1]
    assert all((0^(1|r))==1 for r in [0,1])
    T=256;N=2*T+1;grid=[bytearray(N)];grid[0][T]=1
    for t in range(T):
        row=grid[-1];nxt=bytearray(N)
        # Zero exterior; at t<T no active cell beyond the allocated boundary.
        for i in range(N):
            l=row[i-1] if i else 0
            r=row[i+1] if i+1<N else 0
            nxt[i]=(30>>(4*l+2*row[i]+r))&1
        grid.append(nxt)
    observed=Counter();heights=Counter()
    for c in range(N-2):
        a=0
        while a<=T:
            if not grid[a][c]:a+=1;continue
            b=a
            while b<T and grid[b+1][c]:b+=1
            if b-a+1>=3 and b+2<=T:
                kind,s=check([grid[t][c] for t in range(a,b+1)],
                             [grid[t][c+1] for t in range(a,b+2)],
                             [grid[t][c+2] for t in range(a,b+3)])
                observed[kind]+=1;heights[b-a+1]+=1
            a=b+1
    recovered=json.load(open(sys.argv[1]))['grid']
    assert len(recovered)==32 and all(len(r)==32 and set(r)<={'0','1'} for r in recovered)
    matches=[]
    for t0 in range(T-30):
        x0=t0-10
        if all(int(recovered[r][c])==grid[t0+r][T+x0+c] for r in range(32) for c in range(32)):
            matches.append(dict(time=t0,x=x0))
    assert ''.join(recovered[t][21] for t in range(19,28))=='101010101'
    assert recovered[27][21]==recovered[28][21]=='1'
    image_steps=[]
    for c,a,b in [(12,13,18),(14,14,20),(16,14,22),(18,17,24),(20,19,26)]:
        kind,s=check([int(recovered[t][c]) for t in range(a,b+1)],
                     [int(recovered[t][c+1]) for t in range(a,b+2)],
                     [int(recovered[t][c+2]) for t in range(a,b+3)])
        image_steps.append(dict(column=c,start=a,end=b,kind=kind,first00=None if s is None else a+s))
    result=dict(status='ALL CHECKS PASS',cones=sum(v['total_cones'] for v in totals),
                independent_engine_inputs=controls,missing_left_counterexample=cf2,
                actual_single_seed_maximal_bars=dict(observed),heights=dict(heights),
                image_matches=matches,image_steps=image_steps,
                elapsed_seconds=time.monotonic()-start,
                peak_rss_host_units=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
