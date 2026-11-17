"""GC1185: one-tick phase transfer of a canonical white-band birth.

PREDICTIONS BEFORE execution, 2026-10-13:
 For the fixed known real B100101 band d3/L3, advancing one actual tick
 gives S at d4/L1 and increases birth age2 to3. Its canonical formal
 S0w parent has d2/L5 birth age1; a leading0 white advance gives the
 same real B child with age2. Original actual origin is retained; the
 formal S0w ancestor is absent and is not called an actual past.
 Independent: direct Wolfram forward steps versus suffix-root inverse;
 parent padding equalities at n1..5 versus hand formulas for everyn.
 CF: every white leading1 has the same ancestor transfer. The existing
 first bits10 control must fail at the first free ancestor cell.
 Unexpected: shrinking a length2 zero band leaves no interval; the
 same-birth assertion requires L>=3 and cannot be applied to empty bands.
 Record searched: birth|canonical withone.tick|one.step ->36hits18files;
 leading.zero withL7|seven|two.cells ->one GC1181 pointer. GC1170's
 phase images, GC1174's canonical padding andGC1183's closure read.
 First run compared unequal determined prefix lengths in the S image;
fixed to compare the child's shared prefix. The initial padding check
was also corrected to exact equality (both phases and roots coincide).
No mathematical prediction or input changed.
OUTCOME: two phase images, ten padding controls and the fixed age1/2/3
chain PASS. First1 countercontrol fails parent equality as predicted.
No solver, membership, survival/record/profile census or new witness.
"""
from rule30_prefix_realization import inverse
from rule30_canonical_parent_budget import ancestor, forward


def birth(w,p,d,L):
    assert ancestor(w,p,0)[d-1:d+L-1] == [0]*L
    for n in range(1,(d-p)//2+2):
        lo,count = d-n,L+2*n
        segment = ancestor(w,p,n)[lo-1:lo-1+count]
        assert len(segment)==count
        if any(segment):
            return n
    raise AssertionError('checkerboard birth must occur')


def main():
    w = list(map(int,'100101'))
    z = [0]+w
    # S0w is a formal, not real, ancestor of the real B child.
    assert birth(z,0,2,5) == 1
    assert birth(w,1,3,3) == 2
    assert birth(w,0,4,1) == 3
    assert forward(inverse(z,0),0)[:len(inverse(w,1))] == inverse(w,1)
    assert forward(inverse(w,1),1) == inverse(w,0)[:-1]
    for n in range(1,6):
        assert ancestor(w,0,n) == ancestor(w,1,n-1)
        assert ancestor(w,1,n) == ancestor(z,0,n-1)
    # White first1 countercontrol: the canonical parent would be S0u.
    u = w[1:]
    candidate = ancestor(u,1,1)
    old = inverse(w,0)
    assert candidate[:2] != old[:2]
    assert old[3:] == candidate[3:]  # deep erasure does not restore equality
    print('formal S d2/L5 age1 -> real B d3/L3 age2 -> real S d4/L1 age3 PASS')
    print('two direct phase images and ten padding controls PASS')
    print('white first1 parent-equality countercontrol PASS; empty-band guard is hand scope')

if __name__=='__main__':
    main()
