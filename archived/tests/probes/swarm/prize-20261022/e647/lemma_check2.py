# Non-vacuous kill test of the lemma's first steps: for 84 < n <= X, tau(n-k) <= k+2 for k=1..4 should force
# 120 | n, n-1 prime, (n-2)/2, (n-3)/3, (n-4)/4 prime. Adding k=6: also 7 | n? (needs k=5 too) -> test 2520|n with k=1..6.
import numpy as np
X = 3_000_000
tau = np.zeros(X+1, dtype=np.int32)
for d in range(1, X+1):
    tau[d::d] += 1
P = (tau == 2)
B4 = [n for n in range(85, X+1) if all(tau[n-k] <= k+2 for k in (1,2,3,4))]
v4 = [n for n in B4 if n % 120 or not (P[n-1] and P[(n-2)//2] and P[(n-3)//3] and P[(n-4)//4])]
B6 = [n for n in B4 if tau[n-5] <= 7 and tau[n-6] <= 8]
v6 = [n for n in B6 if n % 2520 or not P[(n-6)//6]]
print('k<=4: #B4 =', len(B4), 'violations', v4[:10], '| first', B4[:8])
print('k<=6: #B6 =', len(B6), 'violations', v6[:10], '| members', B6[:10])
