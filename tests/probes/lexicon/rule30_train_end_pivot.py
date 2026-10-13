"""GC1194: first two arrivals from an arbitrary finite departure from S.

PREDICTIONS BEFORE controls, 2026-10-13: at r0/p0/N2/T1, the first
seed discrepancy q from S=1011(0000111)^inf reaches depth1 at q-3.
Even q breaks a black clock; q=1 mod4 creates the certified cut11.
Only q=3 mod4 can pass that first arrival. At q7/11 the next seed
discrepancy must be0, and at q35/39 it must be1 to pass the next black
tick. Counterfactual: the required repair repeats after28; it must
instead flip because the seven-ring contains13 black cells in28 sites.
Controls: seven named q values6/7/8/9/11/35/39, both next-bit
discrepancies and two farther tails,28 fixed formal primitive seeds.
Independent ordinary full-line table versus edge formula, and clamped
Boolean versus lookup evolution. Unexpected: the right repair passes
only this next black condition; neither actual membership nor later
termination is inferred. No period/profile/record/survival census.
Record searched: first.differ|first.mismatch|first.deviation with
train|no11|four|mod4 ->12hits10files; train|two.gap|period7|0110010
withtermin|finite.end|white.band|exit|seed ->222hits66files.
GC1167's PROVED nonlinear one-behind-front identity, G25, GC1193 and
L678 read. This applies the existing identity, not a global affine
explanation or a scan of completed train closing windows.

ADDENDUM BEFORE endpoint-phase table: R4's minimal completions of the
ray at k bits have exactly7 surviving k classes modulo56 after the
first two arrival tests. This follows from seven position classes,
one of four first-arrival phases and opposite repair at k+28. Check
the56 symbolic representatives k56..111, without time evolution or a
closing-window search. Counterfactual: the early tests close the entire
family. Unexpected: retain the seven survivors without calling them
actual records or claiming later survival.
OUTCOME:28 named endpoint controls PASS. The symbolic56-phase table
retains k=10,11,27,30,35,47,50 modulo56. All are kept as unresolved
after these two arrivals; no completed-word closing windows measured.
"""
from rule30_seed_tree_train_ray import finish
from rule30_primitive_seed_language import decode
from rule30_seed_prefix_scope import edge,ordinary,trace

ROWS=('0100110','1111101','0000001','1000011')


def S(j):return int('1011'[j]) if j<4 else int('0000111'[(j-4)%7])


def charge(ell):
    c=ell%2
    for t in range(ell):c ^= int(ROWS[t%4][-(ell-t-1)%7])
    return c


def main():
    count=0
    for q in (6,7,8,9,11,35,39):
        ell=q-2; need=charge(ell)^1^S(q-1)
        if q in (7,11):assert need==0
        if q in (35,39):assert need==1
        for next_diff in (0,1):
            for far in ('00','11'):
                pref=''.join(str(S(i)) for i in range(q))
                pref+=str(1-S(q))+str(S(q+1)^next_diff)+far
                seed=finish(pref);assert decode(seed) is not None
                y=edge(seed);assert y==ordinary(seed)
                row=y[3:ell+4]
                x=trace(row,0,True);assert x==trace(row,0,False)
                ref=[int(t%4!=0) for t in range(len(x))]
                assert x[:ell-1]==ref[:ell-1]
                assert x[ell-1]!=ref[ell-1]
                assert x[ell]^ref[ell]==next_diff^need
                if q%2==0:assert x[ell-1]==0 # first arrival at black tick
                elif q%4==1:
                    assert (1-x[ell-3],1-x[ell-1])==(1,1)
                else:assert (x[ell]==1)==(next_diff==need)
                count+=1
        # Exact background period and odd complete-block charge, not a fit.
        assert charge(ell+28)==1-charge(ell)
        assert charge(ell+56)==charge(ell)
        print('q',q,'first tick',ell-1,'required next seed discrepancy',need)
    assert count==28
    assert sum(r.count('1') for r in ROWS)==13
    print('28 fixed primitive endpoint controls PASS; repair flips after28, repeats after56')
    survivors=[]
    for k in range(56,112):
        seed=finish(''.join(str(S(i)) for i in range(k)))
        q=next(i for i in range(k,len(seed)+7)
               if (int(seed[i]) if i<len(seed) else 0)!=S(i))
        nxt=(int(seed[q+1]) if q+1<len(seed) else 0)^S(q+1)
        if q%4==3 and nxt==(charge(q-2)^1^S(q-1)):
            survivors.append(k%56)
    assert len(survivors)==7
    print('minimal ray completions retain seven end classes modulo56:',sorted(survivors))


if __name__=='__main__':main()
