#!/usr/bin/env python3
"""B244/MI474: isolated adjacent -1,+1 cycle on the SAME119 k8 profiles.
One invocation, first negative,20wall seconds/1M independent states.
Input: retained MI472 JSONL, SHA256 frozen in the notebook.
"""
from itertools import permutations
from functools import lru_cache
from pathlib import Path
import hashlib,json,sys,time
from pair_sum_group_capacity import profile_stream
START=time.monotonic();NODES=0

def guard():
    assert time.monotonic()-START<20,'wall cap'

def profile(p):return tuple(sorted(15+i-p[i] for i in range(8)))

def swap(p):return any(p[a]==a+1 and p[a+1]==a for a in range(7))

def inverse(p):return tuple(p.index(i) for i in range(8))

def independent(q):
    global NODES
    for a in range(7):
        demand=list(q);demand.remove(14);demand.remove(16)
        @lru_cache(None)
        def visit(slot,rows,cols):
            global NODES
            NODES+=1;guard();assert NODES<=1000000,'state cap'
            if slot==6:return ()
            d=demand[slot]-15
            for i in range(8):
                j=i-d
                if not 0<=j<8 or rows>>i&1 or cols>>j&1:continue
                tail=visit(slot+1,rows|1<<i,cols|1<<j)
                if tail is not None:return ((i,j),)+tail
            return None
        used=(1<<a)|(1<<(a+1))
        out=visit(0,used,used)
        if out is not None:
            edges=((a,a+1),(a+1,a))+out
            p=tuple(dict(edges)[i] for i in range(8))
            assert sorted(p)==list(range(8)) and profile(p)==q and swap(p)
            return p
    return None

def main():
    raw=Path(sys.argv[1]).read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='ad13bd33660740444f97146a741245c03920415301b33651307478293d0bb612'
    qs=set()
    for row in map(json.loads,raw.splitlines()):
        if 'certificate' not in row:continue
        q=tuple(row['certificate']);h=row['highs']
        assert sorted(h)==list(range(8,16))
        assert tuple(sorted(i+x for i,x in enumerate(h)))==q
        qs.add(q)
    assert len(qs)==119
    assert qs=={q for q in profile_stream(8) if {14,15,16,17}.issubset(q)}
    good={};allmap={};count=0
    for p in permutations(range(8)):
        guard();q=profile(p);allmap.setdefault(q,p);count+=1
        inv=inverse(p)
        assert profile(inv)==tuple(sorted(30-x for x in q))
        assert swap(inv)==swap(p)
        if swap(p):good.setdefault(q,p)
    assert count==40320 and len(allmap)==5270
    pos=(1,0,2,3,4,5,6,7);pq=profile(pos)
    assert swap(pos) and pq in good and independent(pq) is not None
    assert (15,)*8 in allmap and (15,)*8 not in good
    # Its absence is hand-forced: every displacement0 requires p_i=i.
    print(json.dumps({'controls':'retained digest/literal witnesses; independent full target domain; inverse whole map; adjacent swap positive; identity negative PASS','profiles':119}),flush=True)
    for index,q in enumerate(sorted(qs),1):
        other=independent(q)
        assert (other is not None)==(q in good),'independent property mismatch'
        if q not in good:
            print(json.dumps({'result':'FIRST CONSTRUCTION-STEP FAILURE','q':q,'index':index,'unrestricted_p':allmap[q],'states':NODES,'seconds':time.monotonic()-START}),flush=True)
            return
        print(json.dumps({'certificate':q,'p':good[q]}),flush=True)
    print(json.dumps({'result':'FIXED DOMAIN PROPERTY PASS','profiles':119,'states':NODES,'seconds':time.monotonic()-START}),flush=True)

if __name__=='__main__':main()
