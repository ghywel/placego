# Independent checks of the hand steps in GC2706 and GC2709 (Cloud carrying read, CL753). No inputs.
import random
random.seed(1)
# ---- GC2706: the clock ----
c = lambda n: 34 + 7*n           # sampled steps per return E + n copies of A=25 (E = 3+3+5+3+5+5+5+5 = 34, A = 2+5 = 7)
assert sum([3,3,5,3,5,5,5,5]) == 34 and 2+5 == 7
# grammar at 39-41: R: 4->S, n>=6 -> R ; S: n>=7 -> R
h = {'R': 0.0, 'S': -10.5}
edges = [('R',4,'S')] + [('R',n,'R') for n in range(6,40)] + [('S',n,'R') for n in range(7,40)]
viol = [(q,n,q2) for (q,n,q2) in edges if not (c(n) - 72.5 >= h[q2]-h[q] - 1e-12)]
print("potential inequality violations:", viol)
# exact min cost over k returns from R via the recurrence and by brute force over paths
INF = float('inf')
r, s = 0, INF
rec = []
for k in range(1, 12):
    r, s = min(r+76, s+83), r+62
    rec.append((k, r, s, min(r, s)))
# brute force DP over the same grammar with n up to 12 (larger n only costs more)
import functools
def best(k):
    # min cost of k returns starting at R, ending anywhere
    dp = {'R':0, 'S':INF}
    for _ in range(k):
        nd = {'R':INF,'S':INF}
        for q,v in dp.items():
            if v==INF: continue
            for (a,n,b) in edges:
                if a==q: nd[b] = min(nd[b], v + c(n))
        dp = nd
    return min(dp.values()), dp
ok = True
for (k, r_, s_, m) in rec:
    b, dp = best(k)
    claim = (145*(k//2) + 62) if k%2==1 else (145*(k//2) - 7)
    ok &= (b == m == claim) and dp['R']==r_ and dp['S']==s_
print("recurrence/brute-force/closed form agree for k=1..11:", ok, rec[:4])
print("mean of the 4,7 cycle:", (c(4)+c(7))/2, "; R->R with 6:", c(6), "; W38 cycle 4,6:", (c(4)+c(6))/2)
# ---- GC2709: D, B_b, E_m identities ----
def Bb(X,b): return ((X<<1)|b) ^ (X | (X>>1))
def D(X): return X ^ ((X>>1) | (X>>2))
bad = [(X,b) for X in range(1<<12) for b in (0,1) if (Bb(X,b)>>1) != D(X)]
print("B_b(X)>>1 == D(X) for X<2^12:", not bad)
print("D commutes with >>1 for X<2^12:", all(D(X>>1) == (D(X)>>1) for X in range(1<<12)))
def Em(X, drive):
    for b in drive: X = Bb(X,b)
    return X
def Dm(X,m):
    for _ in range(m): X = D(X)
    return X
okE = all(Em(X,drive)>>len(drive) == Dm(X,len(drive)) for X in random.sample(range(1<<20), 300) for drive in [[random.randint(0,1) for _ in range(random.randint(1,9))]])
print("E_m(X)>>m == D^m(X) on 300 random X<2^20, drives of length 1..9:", okE)
# D bijective on w-bit words, width-preserving
for w in range(1,13):
    img = sorted(D(X) for X in range(1<<w))
    assert img == list(range(1<<w)), w
    assert all(D(X).bit_length()==X.bit_length() for X in range(1<<w))
print("D is a width-preserving permutation of w-bit words, w<=12: True")
# inverse by top-down descent
def Dinv(Y, w):
    x = [0]*(w+2)
    for i in range(w-1, -1, -1):
        x[i] = ((Y>>i)&1) ^ (x[i+1] | x[i+2])
    return sum(x[i]<<i for i in range(w))
print("top-down descent inverts D (w=12):", all(D(Dinv(Y,12))==Y for Y in range(1<<12)))
# tail completion: given drive (fixed) and q = E_m(X0)>>m, X0 = D^-m(q) and the low m bits of E_m(X0) are determined
m=5; drive=[1,0,1,0,1]
ok_tc = True
for X0 in range(1<<10):
    M = Em(X0, drive); q = M>>m
    Y = q
    for _ in range(m): Y = Dinv(Y, 10)
    ok_tc &= (Y == X0) and (Em(Y,drive) == M)
print("tail completion: q determines X0 and all of M (w=10, m=5):", ok_tc)
# predecessor uniqueness for finite rows under a prescribed drive bit
for b in (0,1):
    pre = {}
    for X in range(1<<13):
        pre.setdefault(Bb(X,b), []).append(X)
    mult = [Y for Y,xs in pre.items() if len(xs)>1]
    widths_ok = all(Bb(X,b).bit_length()==X.bit_length()+1 for X in range(1,1<<13))
    print(f"drive b={b}: Y with >1 finite predecessor among X<2^13: {len(mult)}; width grows by exactly 1 for X!=0: {widths_ok}; predecessor of Y=0: {pre.get(0)}, of Y=1: {pre.get(1)}")
# corridor law: F = B_1 o B_0 (white then black centre); F(R)_1 = NOT(x1|x2|x3)
okc = all(((Bb(Bb(R,0),1))&1) == (1 - ((R|(R>>1)|(R>>2))&1)) for R in range(1<<10))
print("corridor law F(R)_1 = NOT(x1 or x2 or x3) for R<2^10:", okc)
# seam arithmetic
E_s, A_s = 34, 7
tot = E_s + 4*A_s + E_s + 7*A_s + E_s
print("sampled steps E A^4 E A^7 E:", tot, "-> ticks", 2*tot, "+1 =", 2*tot+1)
print("seams: 1 +", 2*E_s, "=", 1+2*E_s, "; +", 2*(4*A_s+E_s), "=", 1+2*E_s+2*(4*A_s+E_s), "; cone widths 360-t:", 360-69, 360-193, "; A^7 E ticks:", 2*(7*A_s+E_s), "; width of M at 193:", 360+193)
