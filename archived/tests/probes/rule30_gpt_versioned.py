"""G99 VP1 preregistered through827e006; PASS 2026-10-06. Publish before execution.
All initial words, N1..4: two ready-node schedules equal synchronous
triangle at every node. Mixed-generation projection must differ.
"""
from itertools import product


def truth(l,c,r):
    return (30 >> (4*l+2*c+r)) & 1


def synchronous(word,n):
    row=dict(zip(range(-n,n+1),word))
    result={(i,0):bit for i,bit in row.items()}
    for k in range(1,n+1):
        row={i:truth(row[i-1],row[i],row[i+1])
             for i in range(-n+k,n-k+1)}
        result.update({(i,k):bit for i,bit in row.items()})
    return result


def schedule(word,n,spatial):
    values={(i,0):bit for i,bit in zip(range(-n,n+1),word)}
    pending={(i,k) for k in range(1,n+1) for i in range(-n+k,n-k+1)}
    while pending:
        ready=[(i,k) for i,k in pending if all((i+d,k-1) in values for d in (-1,0,1))]
        assert ready
        i,k=(max(ready,key=lambda q:(q[0],q[1])) if spatial
             else min(ready,key=lambda q:(q[1],q[0])))
        values[i,k]=truth(*(values[i+d,k-1] for d in (-1,0,1)))
        pending.remove((i,k))
    return values


def main():
    cases=0
    for n in range(1,5):
        for word in product((0,1),repeat=2*n+1):
            expected=synchronous(word,n)
            assert schedule(word,n,False)==expected
            assert schedule(word,n,True)==expected
            assert len(expected)==(n+1)**2
            cases+=1
    # Complete seed-one frame versus a projection after only node(0,1).
    seed={1}
    mixed=seed|{0}
    frame={i for i in range(-2,4)
           if truth(int(i-1 in seed),int(i in seed),int(i+1 in seed))}
    assert mixed=={0,1} and frame=={0,1,2} and mixed!=frame
    print('VP1 PASS:',cases,'initial words; both schedules equal every synchronous node')
    print('Mixed-generation guard PASS: {0,1} differs from full frame {0,1,2}')


if __name__=='__main__':
    main()
