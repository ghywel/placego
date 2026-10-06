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


if __name__=='__main__':raise SystemExit(main())
