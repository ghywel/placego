# Second-language replay of the exact claim: nu at K = 87868 in Python big integers, W <= 6 classes.
import sys,collections
K=87868; M=(1<<K)-1
def F(y): return (y>>1)^(y|(y<<1))
def L(v): return ((v<<2)^((v<<1)|v))&M
def nu(y):
    W=y.bit_length(); t=0
    while y.bit_length()<K: y=F(y); t+=1
    v=int(format(y,'b')[:K][::-1],2)
    s=v
    while True:
        for _ in range(64): v=L(v); t+=1
        if v==s: break
        s=v
    for _ in range((-(t+W))%64): v=L(v)
    return v
for W in range(1,7):
    reps=[int(l.split()[0]) for l in open(sys.argv[1]+f'/reps{W}.txt')]
    vals={y:nu(y) for y in reps}
    print('W',W,'classes',len(reps),'distinct nu (Python, K=87868)',len(set(vals.values())),flush=True)
