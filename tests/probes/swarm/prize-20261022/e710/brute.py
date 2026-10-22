# Independent control: exhaustive backtracking (no matching theory) for f(n), n <= 14
import sys, time
t0=time.time()
def feasible(n,L):
    used=set()
    order=list(range(n,0,-1))
    def bt(i):
        if i==len(order): return True
        k=order[i]
        x=(n//k+1)*k
        while x<n+L:
            if x not in used:
                used.add(x)
                if bt(i+1): return True
                used.discard(x)
            x+=k
        return False
    return bt(0)
res=[]
for n in range(1,15):
    L=n+1
    while not feasible(n,L): L+=1
    res.append(L)
    if time.time()-t0>120: break
print('brute f(1..%d):'%len(res), res)
