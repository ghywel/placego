"""GC1129: does the single omitted-exit origin have a mature clamped past?

Missing inference: GC1128 narrows second-111 and X exits from recurrent
macro states to P=111010001110111000011. An origin-only ancestry
exclusion would close both beyond a fixed even wall age, without
constructing another strip product or refining its width.
Record searched: GC1096|GC1097|111010001110111000011 AND past|ancestor|
forbid -> nine hits in seven files; the exact complete inverse and
the four-step forbidden-packet proof are read, not reproved.
P1 BEFORE run: P has no four-step clamped past at white wall phase.
Counterfactual: the sole productive recurrent origin is already a
genuine mature row prefix, so its bare prefix is not the missing
admission guard. If present, retain a complete parent and a causal
all-tail cylinder rather than extend an age or width scan.
Controls: independent scalar-forward verification of every backward
edge; actual literal/packed four-tick replay of a retained parent;
the old GC1096 forbidden packet remains absent at four as a negative
instrument control. Unexpected check: the named nearby F packet may
share P's four-step parents after truncation, despite their different
last bits; do not infer impossibility from their graphical similarity.
No CUT, language membership, realization search, new product or width
sweep. A present prefix is not a lifted X/second-111 excursion.
P1 REFUTED: 16 four-step ancestors, levels 4,8,4,16. The bare
origin has a genuine age-four all-tail cylinder. The first comparison
control FAILED: P and F differ at site20, so projecting P ancestors
to F's 24-bit parent length does not target the same output word.
Correct the control to their common first19 bits; no proof relies
on that failed comparison, and no deeper-age scan follows.
P2 BEFORE corrected control: every P/F four-step parent truncated
to 23 bits belongs to the complete common-prefix ancestor set.
P2 HELD; 32 literal/packed arbitrary-tail controls pass. The explicit
25-bit parent is 0101101110111011011101000. This closes the attempted
four-step origin guard only; a longer contextual guard is not ruled out.
"""
from itertools import product
import rule30_black_A_ancestry_guard as p

P=p.bits('111010001110111000011')
F=p.bits('11101000111011100000')


def independent_update(x,wall):
    return tuple((wall if i==0 else x[i-1])^(x[i]|x[i+1])
                 for i in range(len(x)-1))


def parents(word,steps):
    cur={word};counts=[]
    for t in range(steps-1,-1,-1):
        out=set()
        for y in cur:
            for x in p.inverse(y,t&1):
                assert independent_update(x,t&1)==y
                out.add(x)
        cur=out;counts.append(len(cur))
    return cur,counts


def main():
    ancestors,counts=parents(P,4)
    old,oldcounts=parents(p.FORBIDDEN,4)
    assert not old and oldcounts==[4,8,20,0]
    near,nearcounts=parents(F,4)
    print('P_four_step_parents',len(ancestors),'levels',counts,
          'P1_no_mature_P',not ancestors,'F_levels',nearcounts,
          'negative_control_PASS',flush=True)
    if not ancestors:return
    a=min(ancestors)
    assert p.run(a,4)[-1]==P
    controls=0
    for tail in product((0,1),repeat=5):
        rows=p.run(a+tail+(0,)*20,4)
        assert rows[-1][:len(P)]==P
        controls+=1
    # Complete causality: any extension after the 25-bit parent changes
    # no one of the 21 endpoint cells within four ticks.
    assert len(a)==len(P)+4
    common,commoncounts=parents(P[:19],4)
    assert P[:19]==F[:19]
    projected={x[:23] for x in ancestors}
    assert projected<=common
    assert {x[:23] for x in near}<=common
    print('mature_P_parent',''.join(map(str,a)),
          'four_tick_all_tail_cylinder','PASS',
          'literal_packed_controls',controls,
          'common19_parent_levels',commoncounts,
          'common19_truncation_subsets','PASS',flush=True)


if __name__=='__main__':main()
