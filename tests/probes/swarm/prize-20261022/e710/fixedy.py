# Fixed-y limit probe: restricted problem R_y(n,L): left = y-smooth k in [ceil((n+L)/q), n], right = y-smooth m in
# (n, n+L), edge k -> k*i (i < q). f_y(n) = least L with a left-perfect matching; Lemma A gives L_A (count bound).
# Question: does (n+f_y)/(n+L_A) stay bounded as n -> infinity at fixed y?  Exact big-integer arithmetic.
import sys, time, bisect
sys.setrecursionlimit(100000)
t0=time.time()
y=int(sys.argv[1]); PR=[p for p in range(2,y+1) if all(p%d for d in range(2,int(p**.5)+1))]
q=y+1
while any(q%d==0 for d in range(2,int(q**.5)+1)): q+=1
def smooth_upto(X):
    out=[1]
    for p in PR:
        new=[]
        for v in out:
            w=v
            while w<=X: new.append(w); w*=p
        out=new
    out.sort(); return out
def matchable(S,n,L):
    lo=-(-(n+L)//q)
    left=S[bisect.bisect_left(S,lo):bisect.bisect_right(S,n)]
    rset=set(S[bisect.bisect_right(S,n):bisect.bisect_left(S,n+L)])
    if len(left)>len(rset): return False
    adj=[[k*i for i in range(2,q) if n<k*i<n+L and (k*i) in rset] for k in left]
    match={}
    # greedy init then Kuhn with iterative DFS
    ml=[None]*len(left)
    for a in range(len(left)):
        for x in adj[a]:
            if x not in match: match[x]=a; ml[a]=x; break
    for a in range(len(left)):
        if ml[a] is not None: continue
        # BFS augment
        prev={}; frontier=[a]; seen={a}; found=None
        while frontier and found is None:
            nf=[]
            for u in frontier:
                for x in adj[u]:
                    if x in prev: continue
                    prev[x]=u
                    if x not in match: found=x; break
                    w=match[x]
                    if w not in seen: seen.add(w); nf.append(w)
                if found is not None: break
            frontier=nf
        if found is None: return False
        x=found
        while True:
            u=prev[x]; px=ml[u]; match[x]=u; ml[u]=x
            if px is None: break
            x=px
    return True
def countA(S,n,L):
    lo=-(-(n+L)//q)
    A=bisect.bisect_right(S,n)-bisect.bisect_left(S,lo)
    B=bisect.bisect_left(S,n+L)-bisect.bisect_right(S,n)
    return A>B
for e in [int(a) for a in sys.argv[2:]]:
    n=10**e
    S=smooth_upto(n*q+1)
    # Lemma A bound
    lo,hi=0,(q-1)*n
    while hi-lo>1:
        mid=(lo+hi)//2
        if countA(S,n,mid): lo=mid
        else: hi=mid
    LA=lo+1
    lo,hi=LA-1,(q-1)*n   # lo fails (Lemma A violation), find least matchable L
    while hi-lo>1:
        mid=(lo+hi)//2
        if matchable(S,n,mid): hi=mid
        else: lo=mid
    fy=hi
    print('y=%d q=%d n=10^%d |S|=%d  W_A=%.4f  W_f=%.4f  ratio=%.4f  sqrt(q)=%.3f  secs=%.0f'%(y,q,e,len(S),(n+LA)/n,(n+fy)/n,(n+fy)/(n+LA),q**.5,time.time()-t0),flush=True)
    if time.time()-t0>300: break
