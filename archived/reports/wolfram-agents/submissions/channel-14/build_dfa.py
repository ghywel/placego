# Port of entropy2.c's BFS (same visiting order, same numbering) for width M; writes sets.
import json, sys, time
M=int(sys.argv[1]); MASK=(1<<M)-1
def nxt(s,tv,u): return (((s<<1)|tv) ^ (s | ((s>>1) | (u<<(M-1))))) & MASK
t0=time.time()
root=tuple(range(1<<M))
index={root:0}; sets=[root]; succ=[]
q=0
while q<len(sets):
    cur=sets[q]; sq=[]
    for bit in (0,1):
        l1=set()
        for s in cur:
            if (s&1)!=bit: continue
            l1.add(nxt(s,0,0)); l1.add(nxt(s,0,1))
        l2=set()
        for t in l1:
            l2.add(nxt(t,1,0)); l2.add(nxt(t,1,1))
        if not l2: sq.append(-1); continue
        key=tuple(sorted(l2))
        if key not in index: index[key]=len(sets); sets.append(key)
        sq.append(index[key])
    succ.append(sq); q+=1
N=len(sets); sizes=[len(s) for s in sets]
print('M',M,'states',N,'mean nonroot size %.1f'%(sum(sizes[1:])/(N-1)),'max',max(sizes[1:]),'min',min(sizes[1:]),'total rows',sum(sizes),'time %.1fs'%(time.time()-t0))
c=json.load(open(f'channel-m{M}.json'))
print('JSON states',c['states'],'successors equal:',c['successors']==succ)
# gaps stats for delta encoding
import statistics
maxd=0; dbits=[0]*17
for s in sets[1:]:
    prev=-1
    for r in s:
        d=r-prev; prev=r; maxd=max(maxd,d); dbits[d.bit_length()]+=1
print('max delta',maxd,'delta bit-length histogram',dbits)
# source size estimates
tot16=sum(len(s)*16 for s in sets[1:]); print('packed 16-bit: %.2f Mbit -> ~%.2f M decimal digits'%(tot16/1e6, tot16*0.30103/1e6))
json.dump({'M':M,'sets':[list(s) for s in sets],'succ':succ}, open(f'dfa-m{M}.json','w'))
# label split: how many rows with bit0=0/1 per state; successor sizes vs image sizes (is T == S_j exactly?)
