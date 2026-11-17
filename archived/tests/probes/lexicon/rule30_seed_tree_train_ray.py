"""GC1193: fixed controls for an all-depth obstruction to L676's tree.

PREDICTIONS BEFORE controls, 2026-10-13: at the two named windows10/29,
G25's inverse of the proved clamped1001 train yields compatible left
prefixes A. Lifting A to edge timeT1 gives a seed starting1011; every
prefix extends by1 or11 to GC1191's primitive grammar. The resulting
formal crop survives the named clock window. Counterfactual: the lift
has a different header or terminal completion fails, so it cannot
obstruct this tree. Independent control: ordinary unclamped full-line
lookup evolution of finite A/right1001 against the prescribed clock,
and ordinary seed evolution against the triangular edge formula.
Unexpected: these finite controls certify only their window, not the
clock through the completed seed's deep white band. No real record or
infinite finite-support clock is asserted. No tree or period census.
Record searched: edge|seed.prefix|prefix.tree withinverse.limit|2.adic|
compatible.*resid|coherent.*resid ->16hits11files;1001|GC1020|G282
witheternal|lock|all.tail ->275hits93files. GC1020 and its CL189/L595
reads, GC808, G25, GC1191/1192 read. The known eternal train is used,
not re-proved or resimulated as an experimental long-run claim.
OUTCOME: both named windows PASS, with compatible left prefixes and Q
completions. Finite ordinary clocks hold through their named horizon.
"""
from rule30_extremal_p_corner_read import forced_row,depth1_column
from rule30_primitive_seed_language import decode,seed_from_parent
from rule30_seed_prefix_scope import edge,ordinary

TABLE=(0,1,1,1,1,0,0,0)


def lift(left):
    seed=[1,0,1]
    for v in left:
        seed.append(v ^ (seed[-1] | seed[-2]))
    return ''.join(map(str,seed))


def finish(word):
    a,b=0,0
    for u in word[4:]:a,b=b,int(u) ^ (a|b)
    return word+('11' if (a,b)==(1,0) else '1')


def full_clock(left,W):
    black={-i for i,b in enumerate(left,1) if b}|{1,4}
    for t in range(W+1):
        assert int(0 in black)==t%2
        if t<W:assert int(1 in black)==int(t%4<2)
        if black:
            black={s for s in range(min(black)-1,max(black)+2)
                   if TABLE[4*int(s-1 in black)+2*int(s in black)+int(s+1 in black)]}


def main():
    lefts=[]
    for W in (10,29):
        samples=[1-(i%2) for i in range((W+1)//2)]
        left=forced_row(samples,0)[1:W+1]
        pref=lift(left);assert pref[:4]=='1011'
        seed=finish(pref);d=decode(seed);assert d is not None
        r,gap,typ,beta=d;assert (r,beta)==(0,1)
        assert seed_from_parent(r,gap,typ)==seed
        y=edge(seed);assert y==ordinary(seed)
        assert y[3:W+3]==left
        x=depth1_column([None]+left+[0],0,W-1)
        assert x==[int(t%4!=0) for t in range(W)]
        full_clock(left,W)
        lefts.append(left)
        print('W',W,'seed',seed,'type',typ,'T1 survives; finite ordinary clock0..W PASS')
    assert lefts[0]==lefts[1][:10]
    print('compatible named prefixes and primitive completions PASS; no tree run')


if __name__=='__main__':main()
