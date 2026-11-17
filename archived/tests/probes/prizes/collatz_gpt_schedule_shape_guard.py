"""GC468 bounded schedule-only guard for L275, not actual Collatz census.
Blind P1: every terminal-generated law under words without NN, length<=14,
is unimodal. CF0: generic N preserves unimodality; must fail on10,13,16,18.
Unexpected C0: both folds exactly double total mass, with zero padded edge.
REFUTED-BY: first nonunimodal law; retain word and integer atoms.
OUTCOME: P1 HELD2581 laws; CF0 rejects33,29,34,18; C0 PASS all folds.
"""
def fold(p,kind):
    q=p+[0]
    return ([2*q[0]+q[1]]+[q[j]+q[j+1] for j in range(1,len(p))]
            if kind=='N' else [q[0]]+[q[j-1]+q[j] for j in range(1,len(p)+1)])
def unimodal(p):
    falling=False
    for a,b in zip(p,p[1:]):
        if b<a:falling=True
        if falling and b>a:return False
    return True
if __name__=='__main__':
    guard=[10,13,16,18]
    assert unimodal(guard) and not unimodal(fold(guard,'N'))
    frontier=[('',[1])];tested=0;bad=[]
    for n in range(1,15):
        nxt=[]
        for w,p in frontier:
            for k in 'CN':
                if k=='N' and w.endswith('N'):continue
                q=fold(p,k)
                assert sum(q)==2*sum(p)==2**n
                tested+=1
                if not unimodal(q):bad.append((w+k,q))
                nxt.append((w+k,q))
        frontier=nxt
    print('tested',tested,'nonunimodal',len(bad),'first',bad[:1])
    print('generic fold guard',fold(guard,'N'))
