"""GC1144: CL335 pin13 complete SS-carrier test at existing width20.
Missing inference: white-A exits from pin1110011110100 cannot reenter
GC1141 high111, for every exterior and every SS length.
Record searched:1110011110100|CL335 AND all.tail|carrier|certificate|guard
->2 hits2files; GC1143 next intention and docstring only, no earlier guard.
P1 before run: all non-SS exits are core/guarded B or white-A whose
13th cell is white, or whose14..19 suffix avoids GC1141 high cubes.
P2 before run: complete least fixed point is acyclic, at most5 SS.
The primary white-A guard is tested separately if the stronger P1 fails.
Counterfactual: reachable high-A or badB, or an SS cycle; retain a
shortest relaxation path and stop this carrier candidate, no widening.
Independent controls: scalar successor equality on every reached
intermediate edge, plus complete literal/packed actual pin histories.
Unexpected check: count H-low and black-A exits rather than hide them.
No Local solver, language or record computation; no strip widening.
"""
from collections import Counter,deque
from hashlib import sha256
import rule30_H111_SS_star_B_guard as g
from rule30_sl_no_refork import bits,run
q=g.q
A=q.pack(bits('111010001'))
HIGH={'010001','010010','010011','011010','011011','011100','100001','100100','100101','100110','100111'}

def fmt(x):return ''.join(map(str,q.unpack(x)))
def classify(x):
    s=fmt(x)
    if s[:9]=='111010001':
        if s[10]=='1':return 'black_A'
        if s[12]=='0':return 'white_A_white13'
        if s[13:19] in HIGH:return 'white_A_high111'
        return 'white_A_C16'
    if x&g.MASK9==g.B:return 'bad_B' if g.bad_B(x) else 'guarded_B'
    return s[:9]

def checked_flow(states,track):
    for t,b in enumerate(track):
        out=set()
        for x in states:
            if (x>>4)&1!=b:continue
            ys=set(q.successors(x,t));assert ys==set(q.scalar_successors(x,t))
            out.update(ys)
        states=out
    return states

def main():
    pin=q.pack(bits('1110011110100'))
    starts={pin|(u<<13) for u in range(128)}
    ends=checked_flow(starts,g.H)
    entrances={x for x in ends if x&g.MASK9 in g.SS_TYPES}
    print('starts',len(starts),'Hends',len(ends),'SS_entrances',len(entrances),'HnonSS',dict(Counter(classify(x) for x in ends-entrances)),flush=True)
    pred={x:None for x in entrances};depth={x:0 for x in entrances}
    todo=deque(sorted(entrances));graph={};terminals={};bad=None
    while todo:
        a=todo.popleft();out=checked_flow({a},g.SS)
        graph[a]={z for z in out if z&g.MASK9 in g.SS_TYPES}
        for z in sorted(out):
            if z&g.MASK9 in g.SS_TYPES:
                if z not in pred:pred[z]=a;depth[z]=depth[a]+1;todo.append(z)
            else:
                terminals.setdefault(z,a)
                if classify(z) in ('white_A_high111','bad_B','black_A') and bad is None:bad=(a,z)
    allout=checked_flow(set(graph),g.SS)
    assert {z for z in allout if z&g.MASK9 in g.SS_TYPES}<=set(graph)
    assert allout-set(graph)==set(terminals)
    counts=Counter(classify(z) for z in terminals)
    wa={z for z in terminals if classify(z).startswith('white_A')}
    assert all(fmt(z)[:12]=='111010001101' for z in wa)
    assert all(classify(z)!='white_A_high111' for z in wa)
    assert not any(g.bad_B(z) for z in terminals)
    digest=sha256(''.join(fmt(z)+'\n' for z in sorted(graph)).encode()).hexdigest()
    print('all_length_white_A_guard_and_B_guard_PASS','SS_digest',digest,flush=True)
    print('SSstates',len(graph),'SSedges',sum(map(len,graph.values())),'terminals',len(terminals),'types',dict(counts),'fixed_point_PASS',flush=True)
    # Explicit topological elimination; finite exhaustion is not a depth bound.
    indeg={a:0 for a in graph}
    for out in graph.values():
        for z in out:indeg[z]+=1
    queue=deque(a for a,n in indeg.items() if not n);rank={a:0 for a in queue};removed=[]
    while queue:
        a=queue.popleft();removed.append(a)
        for z in graph[a]:
            rank[z]=max(rank.get(z,0),rank[a]+1);indeg[z]-=1
            if indeg[z]==0:queue.append(z)
    if len(removed)==len(graph):
        assert all(rank[z]>rank[a] for a,out in graph.items() for z in out)
        print('acyclic_rank_PASS','max_SS_through_terminal',1+max(rank.values(),default=-1),flush=True)
    else:print('cyclic_remaining',sum(n>0 for n in indeg.values()),flush=True)
    if bad:
        a,z=bad;macro=[a]
        while pred[macro[-1]] is not None:macro.append(pred[macro[-1]])
        macro.reverse();macro.append(z)
        _,hp=g.flow(starts,g.H,True);v=macro[0];path=[v]
        for row in reversed(hp):path.append(row[path[-1]])
        path.reverse()
        for a,b in zip(macro,macro[1:]):path+=g.path_to(a,b,g.SS)[1:]
        assert all(y in q.scalar_successors(x,t) for t,(x,y) in enumerate(zip(path,path[1:])))
        print('first_counter_type',classify(z),'SS_count',len(macro)-1,'source',fmt(path[0]),'macro',[fmt(x) for x in macro],'scalar_path_PASS',flush=True)
    for pat in ((0,),(1,),(0,1),(1,0)):
        source=bits('1110011110100')+tuple(pat[j%len(pat)] for j in range(57))
        rows=run(source,40)
        assert q.pack(rows[0][:20]) in starts
        assert q.pack(rows[10][:20]) in ends
        for t in range(40):assert q.pack(rows[t+1][:20]) in q.scalar_successors(q.pack(rows[t][:20]),t)
    print('four_actual70cell_projection_controls_PASS',flush=True)
if __name__=='__main__':main()

# OUTCOME: the primary all-length white-A guard HELD: all29
# white-A terminals have canonical prefix111010001101;17 have
# white13 (GC1090),12 black13 with suffix14..19 outside GC1141
# high111. All172 B terminals satisfy the admission dispatch.
# Complete fixed point:87 H-S entrances,519 SS states,1530 SS
# edges,267 terminals (66 blackA,172 B,29 whiteA). Scalar kernel
# equality checked on EVERY reached intermediate edge, and four
# actual70cell literal/packed projection controls PASS.
# Strong P1 fails:66 blackA exits; shortest counter after2 SS
# retained. P2 fails:214 vertices survive topological elimination,
# so no duration bound is inferred. These are relaxation objects,
# not a proof of realized recurrence. Unexpected check fired:
# 74 of161 H endpoints are low111001001. No claim for those exits.
# Fixed-point sorted20bit state digest:
# 09e5e64944f334f13b032a3249bed3e1f96f51d514e8157f8d012aabfb8f89b1
# No widened strip, solver, language census or larger inverse.
