"""G107 NT1 predictions published throughe779bd0 before execution.
PASS:135296 word/path/schedule cases and8736 conditional bijection classes.
T1..3, all left/stay paths, all global-row race-switch schedules.
Conditional pivot-bit bijection, uniform sample/flip laws, exact moments.
Finite synchronous terminal; no finite-ring or selected-seed inference.
Unexpected guard: at zero flags ideal/noisy copies are equal, not independent.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import product


def truth(l,c,r):
    return (30 >> (4*l+2*c+r)) & 1


def history(old,schedule):
    rows=[old]
    for race in schedule:
        prev=rows[-1]
        lo=min(prev)+1
        hi=max(prev)-1
        new={}
        for i in range(hi,lo-1,-1):
            r=new[i+1] if race and i<hi else prev[i+1]
            new[i]=truth(prev[i-1],prev[i],r)
        rows.append(new)
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
            groups=[defaultdict(Counter) for _ in paths]
            flips=[Counter() for _ in paths]
            for word in product((0,1),repeat=len(sites)):
                old=dict(zip(sites,word))
                rows=history(old,schedule)
                if not any(schedule):
                    ideal=[old]
                    for _ in range(t):
                        prev=ideal[-1]
                        ideal.append({i:prev[i-1]^(prev[i]|prev[i+1])
                                      for i in range(min(prev)+1,max(prev))})
                    assert rows==ideal
                for j,(path,extra) in enumerate(paths):
                    samples=tuple(rows[k][p] for k,p in enumerate(path))
                    groups[j][tuple(old[i] for i in extra)][samples]+=1
                    flips[j][tuple(a^b for a,b in zip(samples,samples[1:]))]+=1
                    cases+=1
            for j in range(len(paths)):
                for counts in groups[j].values():
                    assert len(counts)==2**(t+1) and set(counts.values())=={1}
                    classes+=1
                f=flips[j]
                assert len(f)==2**t and set(f.values())=={2**(2*t+2)}
                total=2**len(sites)
                mean=sum(Fraction(c*sum(v),total) for v,c in f.items())
                var=sum(Fraction(c,total)*(sum(v)-mean)**2 for v,c in f.items())
                assert mean==Fraction(t,2) and var==Fraction(t,4)
    assert cases==135296 and classes==8736
    print('NT1 PASS:',cases,'word-path-schedule cases;',classes,'conditional bijection classes')
    print('Uniform samples and flips; mean T/2 and variance T/4; identical-copy guard PASS')


if __name__=='__main__':
    main()
