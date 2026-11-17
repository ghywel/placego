#!/usr/bin/env python3
"""gate_state.py (Local, L1552): exact sweep analysis at the gates of the witness's route. A backward tick is a sweep up the row, with a state of two cells. Rows that share the witness row above offset c enter the shared part with one of four states. For each state, where does the new row first differ from the witness's next row? Also: where the 145 corridor and the witness part."""
import json,re
W={int(k):v for k,v in json.load(open('witness_tops.json')).items()}
ref=[l.strip()[::-1] for l in open('ref6.txt') if l.strip()]
def sweep_up(row_top,c,a,b):
    """row_top: offsets from the wall, top first. Sweep from offset c-1 up to offset 0 of the row, with new cells a=new(c+?)..: returns new cells by old index j (old offset j -> new offset j+3)."""
    out={}
    p1,p2=a,b           # p1 nearest new cell below, p2 next
    for j in range(c-1,-1,-1):
        v=1 if row_top[j]=='#' else 0
        z=v^(p1|p2)
        out[j]=z
        p2=p1;p1=z
    return out
def first_diff(k,c,a,b):
    """y shares witness row k above offset c; state (a,b) at the boundary. New row in the frame of tick k-1: old offset j -> new offset j+3-? """
    new=sweep_up(W[k],c,a,b)
    # old offset j sits at new offset j-? : frame rises 3 cells, so new offset = j - 0 ... determined by matching the witness itself
    return new
# calibrate: the witness's own state at offset c reproduces its next row
def calibrate(k):
    w0=W[k]; w1=W[k-1]
    for sh in range(-6,7):
        ok=0;tot=0
        for c in (150,):
            for a in (0,1):
                for b in (0,1):
                    new=sweep_up(w0,c,a,b)
                    m=sum(1 for j in range(0,c) if 0<=j+sh<len(w1) and (w1[j+sh]=='#')==bool(new[j]))
                    ok=max(ok,m)
        if ok>=c-2: return sh
    return None
for k in (27,26,20,19,18,17,14,13,12):
    print('tick',k,'shift',calibrate(k))

print()
D={int(l.split()[0]):int(l.split()[1]) for l in open('witness_tops2.txt')}
def table(k,cs):
    w1=W[k-1]
    print(f'gate tick {k} -> {k-1}: D {D[k]} -> {D[k-1]}. For rows sharing the witness above offset c: first difference from the next witness row, by state (new c+3, new c+4); * the witness state')
    for c in cs:
        res=[]
        ws=(1 if w1[c+3]=='#' else 0, 1 if w1[c+4]=='#' else 0)
        for a in (0,1):
            for b in (0,1):
                new=sweep_up(W[k],c,a,b)
                # first difference: smallest new offset j+3 where it differs; search from the top
                fd=None
                for j in range(0,c):
                    if (w1[j+3]=='#')!=bool(new[j]): fd=j+3; break
                if fd is None: fd=c+3
                res.append(f"{a}{b}{'*' if (a,b)==ws else ''}:{fd}")
        print('  c',c,' '.join(res))
table(27,range(94,104))
table(19,range(120,136,2))
table(18,range(124,142,2))
table(13,range(141,148))
print()
# corridor against witness
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
print('corridor tick i against witness tick k, same phase: common depth, and how far past the shallower of the two first differences from the lock')
best=[]
for q in s0:
    i,dep,ph,row=q
    p=(2+i)%6
    for k in range(7,60):
        if (1-k)%6!=p: continue
        c=lcp(row,W[k]); dw=D.get(k,0)
        # corridor's depth in its own phase
        x=ref[p];dc=0
        while dc<len(x) and (x[dc]=='?' or x[dc]==row[dc]): dc+=1
        ex=c-min(dc,dw)
        if ex>0: best.append((ex,i,k,c,dc,dw))
best.sort(reverse=True)
print(best[:14])

best=[]
for s in S[:12]:
  for q in s:
    i,dep,ph,row=q
    p=(2+i)%6
    x=ref[p];dc=0
    while dc<len(x) and (x[dc]=='?' or x[dc]==row[dc]): dc+=1
    for k in range(7,57):
        if (1-k)%6!=p: continue
        c=lcp(row,W[k]); dw=D[k]
        ex=c-min(dc,dw)
        if ex>0: best.append((i,k,c,dc,dw))
agg={}
for i,k,c,dc,dw in best:
    agg.setdefault((i,k),[]).append((c,dc,dw))
print('corridor ticks that share a deviation with a witness row: (corridor tick, witness tick): common, corridor depth, witness depth; from tick -14 on')
for (i,k),v in sorted(agg.items()):
    if -14<=i<=4: print((i,k),len(v),max(v))
print('deepest shares overall',sorted(((max(x[0] for x in v),i,k,len(v)) for (i,k),v in agg.items()),reverse=True)[:10])
