"""GC383 replacement recurrent witnesses, fixed width13, no width sweep.
Prediction: both column5 phase12 bits lie on cycles. CF: one is bridge-only.
Controls full scalar cyclic strip; source column5 flip rejects via column6.
Unexpected: shortest returns need not be56; old skeleton projections must change.
"""
import json,re,sys
from collections import deque
from pathlib import Path
from rule30_locked_core import core
from rule30_locked_lift import lift


def returning(root,out):
    parents={root:None};queue=deque([root])
    while queue:
        n=queue.popleft()
        for v in sorted(out[n]):
            if v==root:
                path=[n]
                while path[-1]!=root:path.append(parents[path[-1]])
                return list(reversed(path))+[root]
            if v not in parents:parents[v]=n;queue.append(v)
    return None


def replay(path,U,mutate=False):
    rows=[[p%2,U[p]]+[(s>>i)&1 for i in range(12)] for p,s in path[:-1]]
    exterior=[]
    for i,row in enumerate(rows):
        source=row.copy()
        if mutate and i==0:source[5]^=1
        good=[f for f in (0,1) if [source[x-1]^(source[x]|(source+[f])[x+1]) for x in range(1,14)]==rows[(i+1)%len(rows)][1:]]
        if not good:return None
        exterior.append(good[0])
    return exterior


def main():
    U=list(map(int,re.search(r'^U = "([01]+)"',Path('tests/probes/lexicon/rule30_wheel_left.py').read_text(),re.M).group(1)))
    _,a,o=core(12,U,details=True);b,bo,_=lift(12,U,a,o)
    assert len(b)==836
    old=json.load(open(sys.argv[1]))['closed_walk_choices'];result={}
    for bit in (0,1):
        roots=sorted(n for n in b if n[0]==12 and ((n[1]>>3)&1)==bit)
        choices=[p for n in roots if (p:=returning(n,bo)) is not None]
        if not choices:result[bit]=dict(recurrent=False,roots=len(roots));continue
        path=min(choices,key=lambda p:(len(p),p));ext=replay(path,U)
        assert ext is not None and replay(path,U,True) is None
        oldstates=dict(old[str(bit)]['path'][:-1])
        different=sum((s&2047)!=oldstates[p] for p,s in path[:-1]);assert different
        result[bit]=dict(recurrent=True,length=len(path)-1,path=path,exterior14=ext,scalar_replay=True,mutation_rejected=True,changed_projection_rows=different,column5=''.join(str((s>>3)&1) for p,s in path[:-1]))
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
