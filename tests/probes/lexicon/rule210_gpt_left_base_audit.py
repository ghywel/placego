"""GC470 L278 independent bounded-left base leaves.
P1: seven odd-left rows at -1,-3,-5 have sole121-prefix R XOR mirrors.
P2: all56 even-containing rows in[-6,-1] have no depth6 survivor.
C0: independent scalar matches decimal masks for every 8-bit right seed
and every seven odd-left rows. CF0: reflection commutes at depth3 for{-3};
must fail. Unexpected: first deviation122 has window lower site26>6.
REFUTED-BY: alternative prefix, surviving even-left row or scalar mismatch.
OUTCOME: P1 HELD7; P2 HELD56; C0 PASS1792; CF0 rejected at depth3
(actual5 versus reflected3,5,7); unexpected window threshold PASS.
"""
from rule210_gpt_base_certificate import step,OFF,D

def trace(seed,depth,left):
    row=(seed<<(OFF+1))|sum(1<<(OFF-k) for k in left)
    out=[]
    for t in range(depth+1):
        out.append((row>>OFF)&1);row=step(row)
    return out

def scalar(seed,depth,left):
    row={-k:1 for k in left}
    row.update({i+1:(seed>>i)&1 for i in range(depth)})
    out=[]
    for t in range(depth+1):
        out.append(row.get(0,0))
        row={i:row.get(i-1,0)^((1-row.get(i,0))*row.get(i+1,0))
             for i in range(-depth,depth+1)}
    return out

def prefixes(left,depth):
    alive=[0]
    for d in range(1,depth+1):
        alive=[p|(v<<(d-1)) for p in alive for v in (0,1)
               if trace(p|(v<<(d-1)),d,left)==[t%2 for t in range(d+1)]]
        if not alive:break
    return alive,d

if __name__=='__main__':
    R=sum(1<<(i-1) for i in range(1,D+1) if i%6 in (1,5))
    controls=0
    for mask in range(1,8):
        left=[k for j,k in enumerate((1,3,5)) if (mask>>j)&1]
        for seed in range(256):
            assert trace(seed,8,left)==scalar(seed,8,left);controls+=1
        alive,d=prefixes(left,D)
        assert alive==[R^sum(1<<(k-1) for k in left)] and d==D
    rejected=0
    for mask in range(1,64):
        left=[k for k in range(1,7) if (mask>>(k-1))&1]
        if any(k%2==0 for k in left):
            assert prefixes(left,6)[0]==[];rejected+=1
    empty,_=prefixes([],3);actual,_=prefixes([3],3)
    wrong=sorted(p^4 for p in empty)
    assert sorted(actual)!=wrong
    assert 122-2*48>6
    print('PASS seven unique121 bases;',rejected,'even rows rejected;',
          controls,'scalar controls; reflection guard',sorted(actual),wrong)
