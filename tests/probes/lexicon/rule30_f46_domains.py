"""L584: exact-cone unary-domain explanation test, not an UNSAT checker.
Predictions and outcome in RULE30-GPT.md; no SAT or new language census.
"""
from collections import deque
F='0010001000100010100001010100010000101000010101'
TRUTH=(0,1,1,1,1,0,0,0)
def propagate(w):
    last=2*len(w)-2
    dom={(t,i):3 for t in range(last+1) for i in range(last-t+2)}
    for t in range(last+1): dom[t,0]=1<<(t%2)
    for s,b in enumerate(w): dom[2*s,1]=1<<int(b)
    cons=[((t,i-1),(t,i),(t,i+1),(t+1,i)) for t in range(last) for i in range(1,last-t+1)]
    rows=[(l,c,r,TRUTH[4*l+2*c+r]) for l in (0,1) for c in (0,1) for r in (0,1)]
    watch={v:[] for v in dom}
    for j,vs in enumerate(cons):
        for v in vs: watch[v].append(j)
    queue=deque(range(len(cons)));pending=set(queue)
    while queue:
        j=queue.popleft();pending.remove(j);vs=cons[j]
        ok=[r for r in rows if all(dom[v]&(1<<a) for v,a in zip(vs,r))]
        if not ok:return None
        for k,v in enumerate(vs):
            d=sum(1<<b for b in {r[k] for r in ok})
            if d!=dom[v]:
                dom[v]=d
                for n in watch[v]:
                    if n not in pending:pending.add(n);queue.append(n)
    return dom
assert len(F)==46
assert propagate('11') is None
for name,w in [('f',F),('prefix',F[:-1]),('suffix',F[1:])]:
    d=propagate(w)
    print(name,'CONTRADICTION' if d is None else ('OPEN',sum(v==3 for v in d.values()),len(d)))
    if name!='f':assert d is not None
for seed in range(16):
    row={i:int(i<=4 and seed>>(i-1)&1) for i in range(1,20)}
    code=''
    for t in range(9):
        if t%2==0:code+=str(row[1])
        row={i:((t%2 if i==1 else row.get(i-1,0))^(row[i]|row.get(i+1,0))) for i in row}
    assert propagate(code) is not None
print('11, deletion and 16 literal simulation controls PASS')
