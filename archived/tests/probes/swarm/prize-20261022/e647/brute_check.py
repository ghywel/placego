# Independent brute-force control: tau by divisor-sieve, D(n) by running max, compare with dscan log (D<=12), n<=1e6.
import numpy as np, sys
N = 10**6
tau = np.zeros(N+1, dtype=np.int64)
for d in range(1, N+1):
    tau[d::d] += 1
R = 0; bad = 0; mine = {}
for n in range(2, N+2):
    m = n-1
    v = m + int(tau[m])
    if v > R: R = v
    D = R - n
    if D <= 12: mine[n] = D
theirs = {}
for line in open('log_1e6.txt'):
    a, b = line.split(); theirs[int(a)] = int(b)
print('entries brute', len(mine), 'dscan', len(theirs), 'identical', mine == theirs)
print('max tau <=1e6:', tau[1:].max(), 'at', int(tau[1:].argmax())+1)
