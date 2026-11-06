# Independent big-integer nu at K = 448, in Python, against left_nu.c, plus merge and F invariance.
import sys,subprocess,collections
exe=sys.argv[1]; K=448; M=(1<<K)-1
def F(y): return (y>>1)^(y|(y<<1))
def L(v): return ((v<<2)^((v<<1)|v))&M
def nu(y):
    W=y.bit_length(); t=0
    while y.bit_length()<K: y=F(y); t+=1
    b=format(y,'b')[:K]; v=int(b[::-1],2)
    s=v
    while True:
        for _ in range(64): v=L(v); t+=1
        if v==s: break
        s=v
    for _ in range((-(t+W))%64): v=L(v)
    return v
rows=list(range(1,1<<9))
out=subprocess.run([exe,str(K),str(K)],input='\n'.join(map(str,rows))+'\n',capture_output=True,text=True).stdout.strip().split('\n')
h={int(l.split()[0]):l.split()[3] for l in out}
py={y:nu(y) for y in rows}
a=collections.defaultdict(set);b=collections.defaultdict(set)
for y in rows: a[py[y]].add(h[y]); b[h[y]].add(py[y])
print('rows',len(rows),'Python nu values',len(a),'C hash values',len(b),'partitions equal',all(len(s)==1 for s in a.values()) and all(len(s)==1 for s in b.values()))
bad=sum(1 for y in rows if py[y]!=nu(F(y)))
print('F invariance violations',bad)
g=collections.defaultdict(list)
for y in rows:
    W=y.bit_length()
    z=y
    for _ in range(512): z=F(z)
    g[(W,z)].append(y)
print('merged groups',sum(1 for v in g.values() if len(v)>1),'with two nu values',sum(1 for v in g.values() if len({py[y] for y in v})>1))
# mutant: forgetting the width term must break F invariance
def bad_nu(y):
    v=nu(y)
    for _ in range(y.bit_length()%64): v=L(v)
    return v
print('mutant without width term, violations',sum(1 for y in rows[:200] if bad_nu(y)!=bad_nu(F(y))))
