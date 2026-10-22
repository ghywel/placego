# Unexpected check: is the right endpoint m* = n + f(n) - 1 (the last integer of the optimal interval) always
# a smooth number? Prediction: P(m*) <= 23 for every n <= 10^4 (the deficient sets are 23-smooth with small multipliers).
import collections
def P(k):
    best=1; p=2
    while p*p<=k:
        while k%p==0: best=p; k//=p
        p+=1
    return max(best,k) if k>1 else best
rows=[tuple(map(int,l.split())) for l in open('allf.txt') if l.strip() and l[0].isdigit()]
print('n range', rows[0][0], rows[-1][0], 'count', len(rows))
c=collections.Counter(); worst=[]
for n,f in rows:
    m=n+f-1; p=P(m); c[p]+=1
    if p>23: worst.append((n,f,m,p))
print('P(n+f(n)-1) histogram:', sorted(c.items()))
print('n with P>23:', len(worst), worst[:20])
# also: does R(n)=n+f(n) never decrease (provable: f(n) <= f(n+1)+1)?
R=[n+f for n,f in rows]; print('R nondecreasing:', all(R[i]<=R[i+1] for i in range(len(R)-1)))
print('distinct endpoints:', len(set(R)))
