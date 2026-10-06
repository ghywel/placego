#!/usr/bin/env python3
"""G12: exact two-hole Boolean interaction audit, not a records search.
COMMAND: PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_hole_interactions.py
RUN-ON: GPT Intel CPU, one process, standard library.
COST: four scalar fibres per period p2..32 through depth3p+2.
PREDICTIONS before first run, 2026-10-06:
 HI0 controls: four scalar evaluations equal a packed four-case truth
     table computed independently by bitwise inverse Rule30.
 HI1 theorem control: flipping the second hole at time p changes no
     depth <=p and always flips depth p+1 (Lemma4, section8.2).
 HI2 theorem control: the mixed coefficient at depth p+2 is exactly
     the first-hole difference at depth p. Derivation in G12.
 HI3 blind: for every p3..32, the two inputs interact by depth2p+2.
 HI4 unexpected check: include p2 and compare its first interaction
     with mostly-black walls; do not infer a monotonicity theorem.
 CF must fail: the two inputs superpose at every depth in every period.
 REFUTED-BY: a control fails; HI3 failing refutes only that finite blind
     threshold. No all-depth LR or universal interaction time is claimed.
 Other hole inputs and non-hole sigma values are zero in this audit.
"""
from rule30_gpt_condrey_holes import forced_columns


def main():
    failed=[];mixed_total=0
    for p in range(2,33):
        depth=3*p+2;n=depth+2
        tau=[int(t%p!=0) for t in range(n)]
        rows=[]
        for a,b in [(0,0),(1,0),(0,1),(1,1)]:
            sigma=[0]*n;sigma[0]=a;sigma[p]=b
            rows.append([c[0] for c in forced_columns(tau,sigma,depth)])
        a=[0]*n;a[0]=10;a[p]=12
        b=[15*t for t in tau];packed=[]
        for _ in range(depth):
            c=[b[t+1] ^ (b[t]|a[t]) for t in range(len(b)-1)]
            packed.append(c[0]);a,b=b,c
        assert packed==[sum(rows[i][j]<<i for i in range(4)) for j in range(depth)]
        for old in range(2):
            assert rows[old][:p]==rows[old+2][:p]
            assert rows[old][p]^rows[old+2][p]==1
        interaction=[j+1 for j in range(depth) if rows[0][j]^rows[1][j]^rows[2][j]^rows[3][j]]
        assert (rows[0][p+1]^rows[1][p+1]^rows[2][p+1]^rows[3][p+1])==(rows[0][p-1]^rows[1][p-1])
        first=interaction[0] if interaction else None
        mixed_total+=len(interaction)
        if p>=3 and (first is None or first>2*p+2):failed.append(p)
        print('p=%d first_mixed=%s mixed_count=%d horizon=%d'%(p,first,len(interaction),depth),flush=True)
    assert mixed_total>0
    print('ALL CONTROLS PASS; CF rejected; HI4 p2 included',flush=True)
    print('HI3 '+('HELD' if not failed else 'REFUTED periods='+str(failed)),flush=True)
    return int(bool(failed))


def shielding():
    import random
    rng=random.Random(2026100612);checks=0
    for p in range(5,65):
        n=2*p+100;tau=[int(t%p!=0) for t in range(n)]
        for _ in range(8):
            sigma=[rng.randrange(2) for _ in range(n)]
            base=forced_columns(tau,sigma,96)
            for t in [0,p]:
                other=sigma[:];other[t]^=1
                flipped=forced_columns(tau,other,96)
                changes=[j+1 for j in range(96) if base[j][t]!=flipped[j][t]]
                assert changes==[1,2,3],(p,t,changes)
                assert base[3][t]==flipped[3][t]==1
                checks+=1
    p=3;n=30;tau=[int(t%p!=0) for t in range(n)]
    a=[0]*n;b=a[:];b[0]=1
    ca=forced_columns(tau,a,20);cb=forced_columns(tau,b,20)
    changes=[j+1 for j in range(20) if ca[j][0]!=cb[j][0]]
    assert any(j>3 for j in changes)
    print('ALL SHIELD CONTROLS PASS: %d comparisons; p3 counterfactual changes=%s'%(checks,changes),flush=True)


if __name__=='__main__':
    import sys
    if len(sys.argv)>1 and sys.argv[1]=='shield':shielding()
    else:raise SystemExit(main())

# ADDENDUM before the shielding check, 2026-10-06 07:17 BST:
# SH0 theorem control: p5..64, eight seeded arbitrary sigma columns,
#     at holes0 andp, flip only sigma(hole). In that hole's row exactly
#     depths1,2,3 change; depths4..96 do not. No arbitrary-time0 claim
#     for a later hole; its earlier inverse cone can still spread.
# SH1 independent control: depth4 is black in both cases; after the
#     two rows agree at depths4 and5, the inverse recurrence makes all
#     later cells equal (their future-time columns already agree).
# CF-SH must fail: p3 first hole is also always confined to three cells.
# This addendum tests a theorem derived after HI3 failed; no revised
# blind prediction and no claim of linear superposition at later holes.
