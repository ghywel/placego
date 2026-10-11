"""GC1146: all boundary assignments reject two retained bad-B PATHS.
Missing inference: GC1143 checked only a selected boundary word;
is its counter path (and GC1145's) coherent with ANY column21?
Record searched:boundary|mask|column21 AND
all.assign|compatib|black.mask|violat ->137hits47files;
GC1143/1145 source witnesses read; no all-assignment test surfaced.
Earlier original-A joint-equation attempt yielded no new guard:
existing GC1005/1006/1010/1012 finite-past routes remain closed.
P1 before run: both named paths have empty necessary mask language.
b_(t+1)=x20_t XOR(b_t OR c_t); if b_t=1 the next bit is forced,
otherwise either next bit is possible. If x20_t=0 its own update
fixes b_t, whereas x20_t=1 leaves b_t free. Enumerate only these
2-state obligations on the KNOWN paths, no widened strip graph.
Counterfactual: a compatible assignment exists, so rejecting one
selected boundary assignment does not reject the path itself.
Controls: all8 scalar (x20,b,c) inputs; actual full histories with
actual columns21/22. Unexpected: a coherent path with black middle
can require a nonminimum boundary choice; preserve that freedom.
No realization search, inverse continuation, solver or new carrier.
Outcome: both paths impossible already at H ticks3/4, before SS.
Scope: reject these PATHS; alternate paths to their macro endpoints,
terminal reachability and original-A admission remain undecided.
"""
import rule30_H111_SS_star_B_guard as g
q=g.q
CASES=(
 ('GC1143','11100111100001111110',
  ('11101110111100111000','11101111011111000000',
   '11101011001110010000','11101001100101011000')),
 ('GC1145','11100111111101001000',
  ('11101110111100111001','11101111011111000100',
   '11101011001110011100','11101001100101110000')))

def domains(path):
    out=[]
    for x,y in zip(path,path[1:]):
        old=q.unpack(x);new=q.unpack(y)
        out.append({b for b in (0,1) if new[-1]==old[-2]^(old[-1]|b)})
    assert all(out)
    return out

def compatible(path,allowed=None):
    allowed=domains(path) if allowed is None else allowed
    live=allowed[0];counts=[len(live)]
    for t in range(len(allowed)-1):
        live={bb for b in live for bb in allowed[t+1]
              if b==0 or bb==1-((path[t]>>19)&1)}
        counts.append(len(live))
        if not live:return False,t+1,counts
    return True,None,counts

def main():
    # Every existential right bit is covered by this truth table;
    # this is a necessary condition, not full exterior realization.
    for x in (0,1):
        for b in (0,1):
            image={x^(b|c) for c in (0,1)}
            assert image==({1-x} if b else {0,1})
    for name,source,mac in CASES:
        path=g.path_to(q.pack(g.bits(source)),q.pack(g.bits(mac[0])),g.H)
        for x,y in zip(mac,mac[1:]):
            path+=g.path_to(q.pack(g.bits(x)),q.pack(g.bits(y)),g.SS)[1:]
        assert all(y in q.scalar_successors(x,t) for t,(x,y) in enumerate(zip(path,path[1:])))
        allowed=domains(path);ok,t,counts=compatible(path,allowed)
        assert not ok and t==4
        assert allowed[3]=={1} and allowed[4]=={0}
        assert ((path[3]>>19)&1)==0
        # A two-assignment interval is minimal: neither singleton
        # alone conflicts, and the pair forces 1 -> 0 beside white.
        assert compatible(path[3:6])[0] is False
        print(name,'all_boundary_assignments_REJECTED','first_fail',t,
              'counts',counts,'minimal_interval',(3,4),
              'rows3_4_5_right_pair',[q.unpack(path[j])[-2:] for j in (3,4,5)],flush=True)
    controls=0
    for source in ('1110011110000000001101000000',
                   '1110011110000000000100000000'):
        for pat in ((0,),(1,),(0,1),(1,0)):
            src=g.bits(source)+tuple(pat[j%len(pat)] for j in range(70-len(source)))
            rows=g.run(src,22);path=[q.pack(r[:20]) for r in rows]
            assert compatible(path)[0]
            allowed=domains(path)
            for t in range(22):
                assert rows[t][20] in allowed[t]
                assert rows[t+1][20]==rows[t][19]^(rows[t][20]|rows[t][21])
            controls+=1
    # A chosen minimum boundary word fails although this actual
    # trajectory is coherent: b0=1, b1 ambiguous in the projection.
    rows=g.run((0,)*20+(1,)+(0,)*9,2)
    path=[q.pack(r[:20]) for r in rows];allowed=domains(path)
    assert allowed==[{1},{0,1}]
    assert rows[0][19]==0 and rows[1][19]==1
    assert rows[0][20]==rows[1][20]==1
    assert compatible(path)[0]
    assert not compatible(path,[{min(s)} for s in allowed])[0]
    print('scalar8_truth_table_PASS','actual70cell_controls',controls,
          'unexpected_minimum_boundary_choice_false_rejection_PASS',flush=True)

if __name__=='__main__':main()
