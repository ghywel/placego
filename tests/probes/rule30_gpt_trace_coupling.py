"""G108 CT1 predictions published through85f0972 before execution.
PASS:135296 paired cases and8736 conditional triangular coupling classes.
135296 paired cases; 8736 conditional classes; causal prefix masks.
Reuse NT1 race evaluator, independent synchronous Boolean evaluator.
Four-input guard E1=1-I0; iid marginals do not imply independent copies.
"""
from collections import defaultdict
from itertools import product
from rule30_gpt_raced_trace import history


def ideal_history(old,t):
    rows=[old]
    for _ in range(t):
        prev=rows[-1]
        rows.append({i:prev[i-1]^(prev[i]|prev[i+1])
                     for i in range(min(prev)+1,max(prev))})
    return rows


def main():
    cases=classes=0
    for t in range(1,4):
        sites=tuple(range(-2*t,t+2))
        paths=[]
        for steps in product((-1,0),repeat=t):
            path=[0]
            for step in steps:
                path.append(path[-1]+step)
            pivots={p-k for k,p in enumerate(path)}
            paths.append((path,[i for i in sites if i not in pivots]))
        for schedule in product((0,1),repeat=t):
            groups=[defaultdict(list) for _ in paths]
            for word in product((0,1),repeat=len(sites)):
                old=dict(zip(sites,word))
                ideal=ideal_history(old,t)
                noisy=history(old,schedule)
                for j,(path,extra) in enumerate(paths):
                    a=tuple(ideal[k][p] for k,p in enumerate(path))
                    b=tuple(noisy[k][p] for k,p in enumerate(path))
                    groups[j][tuple(old[i] for i in extra)].append((a,b))
                    cases+=1
            for by_environment in groups:
                for pairs in by_environment.values():
                    n=2**(t+1)
                    assert len(pairs)==len(set(pairs))==n
                    assert len({a for a,b in pairs})==len({b for a,b in pairs})==n
                    for k in range(t+1):
                        masks=defaultdict(set)
                        for a,b in pairs:
                            masks[a[:k]].add(a[k]^b[k])
                        assert all(len(v)==1 for v in masks.values())
                    assert all(a[0]==b[0] for a,b in pairs)
                    classes+=1
    guard=[]
    for pivot0,pivot1 in product((0,1),repeat=2):
        old={-2:0,-1:pivot1,0:pivot0,1:0,2:1}
        a=ideal_history(old,1)
        b=history(old,(0,))
        b[1][0]=(30 >> (4*old[-1]+2*old[0]+b[1][1])) & 1
        ia=(a[0][0],a[1][0])
        jb=(b[0][0],b[1][0])
        assert ia[1]^jb[1]==1-ia[0]
        guard.append((ia,jb))
    assert len({a for a,b in guard})==len({b for a,b in guard})==4
    assert cases==135296 and classes==8736
    print('CT1 PASS:',cases,'paired cases;',classes,'conditional triangular coupling classes')
    print('Both projections bijective; masks causal; four-input E1=1-I0 guard PASS')


if __name__=='__main__':
    main()
