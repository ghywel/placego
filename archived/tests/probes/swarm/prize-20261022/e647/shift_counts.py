# Numeric companion to the addendum theorem: N_r(x) = #{n <= x : tau(n-k) <= k+C for k=1..r}, C=2 and C=6,
# against the shape x (loglog x)^{rJ} / (log x)^r (upper bound, constants unknown). Time-limited (x = 1e7).
import numpy as np, math, time
t0 = time.time(); X = 10**7
tau = np.zeros(X+1, dtype=np.int32)
for d in range(1, X+1):
    tau[d::d] += 1
print('sieve', round(time.time()-t0, 1), 's')
for C in (2, 6):
    ok = np.ones(X+1, dtype=bool); ok[:20] = False
    for r in range(1, 7):
        cond = np.zeros(X+1, dtype=bool); cond[r+1:] = tau[1:X+1-r] <= r + C   # n-r = m
        ok &= cond
        for x in (10**5, 10**6, 10**7):
            Nr = int(ok[:x+1].sum()); J = int(math.log2(r + C))
            shape = x * math.log(math.log(x))**(r*J) / math.log(x)**r
            print(f"C={C} r={r} x={x:.0e} N_r={Nr} ratio N_r/shape={Nr/shape:.3g}")
