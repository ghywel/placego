"""GC385 prescribed column5 words, column6 exact, column7 free.
P:10 survives; CF:col6 alone explains GC384 pairing. Fixed4 graphs<=112nodes.
"""
import json
from collections import deque
import sys
from itertools import product


def closed(root,out):
    prev={root:None};q=deque([root])
    while q:
        u=q.popleft()
        for v in sorted(out[u]):
            if v==root:
                path=[u]
                while path[-1]!=root:path.append(prev[path[-1]])
                return path[::-1]+[root]
            if v not in prev:prev[v]=u;q.append(v)


def local_control():
    # Fixed column4 schedule 0,1,1. Source column5 is h; source6=r,
    # source7=s, and next-row7=z is relaxed free. Literal scalar updates.
    count=0;counter=[]
    for h,r,s,z in product((0,1),repeat=4):
        a=h|r;b=h^(r|s)
        middle=1^(a|b);next6=a^(b|z);d=1^(middle|next6)
        if h==0:assert a==d;count+=1
        elif a!=d:counter.append([h,r,s,z,a,d])
    assert count==8 and counter
    return dict(source_zero_cases=count,relaxed_source_one_counterexamples=counter)


def main():
    control=local_control()
    base=json.load(open(sys.argv[1]));cycle=json.load(open(sys.argv[2]))['0']
    c4=list(map(int,base['forced_columns']['4']))
    c5=[None]*56
    for p,s in cycle['path'][:-1]:c5[p]=(s>>3)&1
    result={}
    for a in (0,1):
        for b in (0,1):
            w=c5.copy();w[12]=a;w[14]=b
            allowed={p:{e for e in (0,1) if w[(p+1)%56]==(c4[p]^(w[p]|e))} for p in range(56)}
            out={(p,e):{((p+1)%56,n) for n in allowed[(p+1)%56] if any(n==(w[p]^(e|f)) for f in (0,1))} for p in range(56) for e in allowed[p]}
            paths=[v for e in sorted(allowed[0]) if (v:=closed((0,e),out)) is not None]
            if not paths:result[str(a)+str(b)]=dict(recurrent=False);continue
            path=min(paths,key=len);ext=[]
            for (p,e),(q,n) in zip(path,path[1:]):
                choices=[f for f in (0,1) if [c4[p]^(w[p]|e),w[p]^(e|f)]==[w[q],n]]
                assert choices;ext.append(choices[0])
            result[str(a)+str(b)]=dict(recurrent=True,length=len(path)-1,column6=[e for p,e in path[:-1]],exterior7=ext,scalar_replay=True)
    assert not result['01']['recurrent']
    assert result['00']['recurrent'] and result['11']['recurrent']
    print(json.dumps(dict(fixed_words=result,local_control=control),indent=2))

if __name__=='__main__':main()
