# Independent certificate check of the lower side: for the dumped K at L = f-1, count N(K) = multiples of K
# in the open interval (n, n+f-1) directly; |N(K)| < |K| proves f(n) > f-1 by Hall, without trusting fm.c.
import sys, re
f={}
for line in open('sweep.log'):
    m=re.match(r'n=(\d+) m=\d+ f=(\d+)',line)
    if m: f[int(m.group(1))]=int(m.group(2))
for n in sorted(f):
    L=f[n]-1
    K=[int(x) for x in open('K%d.txt'%n)]
    N=set()
    for k in K:
        x=(n//k+1)*k
        while x<n+L:
            N.add(x); x+=k
    print('n=%d L=f-1=%d |K|=%d |N(K)|=%d  Hall violated: %s'%(n,L,len(K),len(N),len(N)<len(K)))
