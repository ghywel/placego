"""GC1072: a finite moving-front test of the missing fastest zero lane.
Record searched: collar|front with zero.lane|fastest|halfwidth|seven.cell
->22 hits in10 files. GC1071's three-cell shield is not universal;
no three-site all-length zero-lane exclusion found.
Missing inference: for W=K+4, released1 first differs at future K+1.
Only its fastest leftward path can affect the halfwidth last observation.
P1 BLIND before run: for the four (p,phase) origins with retained
prefix p0(01)^(K/2), at least one of the first THREE propagation
centres is black, for every even K>=10. A seven-bit moving frame
started at future2 covers these centres, with period dividing128.
P2 control: the finite front at all relevant dependency points agrees
with literal actual cones. Check K10..136 even, covering every residue.
Counterfactual: the first TWO centres suffice; the zero initial front
at K=0mod32 is predicted to defeat it.
Unexpected check: include the third centre even though its time-zero
frame origin lies left of the wall. Initialize at future2 instead;
an unconstrained imaginary initial left tail must not substitute for it.
These are finite invariant controls, not a trace/membership census.
Retained control failure: first initialization used interior sites1..7,
one site too far right. K10,p=phase=0 gave predicted001, actual100.
Correct future2 front uses sites0..6: wall phase followed by six cells.
P1 unchanged before rerun; the failed alignment is not proof evidence.
OUTCOME first aligned run: P1 REFUTED,32 of256 contexts have000.
P2 PASS; counterfactual REFUTED (64 first-two failures). No fourth-
centre search follows. The proposed universal three-centre shield closes.
ADDENDUM before run: P3 the four rooted seven-bit states return after32
steps, so these failures are recurrent at arbitrary collar length.
P4: p=phase=1,K=12+32n gives000 for all n>=0. A finite32-step cycle
certificate plus the dependency triangle proves this, not a length scan.
Counterfactual: period16 suffices for all seven bits; expect failure.
OUTCOME addendum: four32-step cycles PASS; all four16-step returns
fail as predicted. The rooted state0101101 has states1001111,0111000,
1100110 after11,12,13 steps, certifying the000 negative family.
256 independent literal/packed front controls PASS;32 three-centre
and64 two-centre failures. No fourth-centre or language census run.
"""
from itertools import product
from rule30_sl_no_refork import bits, run


def advance(z):
    return (1-z[0], z[1]^z[0]) + tuple(
        z[r]^(z[r-1]|z[r-2]) for r in range(2,len(z)))


def main():
    failures=[]
    two_failures=[]
    checks=0
    for p,phase in product((0,1),repeat=2):
        origin=(p,0)+bits('01')*5+bits('0000000')+(0,)*150
        initial=((phase,)+run(origin,4,phase)[4][:6])[::-1]
        states=[initial]
        for t in range(32): states.append(advance(states[-1]))
        assert states[32]==states[0]
        assert states[16]!=states[0]
        for K in range(10,138,2):
            W=K+4
            actual=run((p,0)+bits('01')*(K//2)+bits('0000000')+(0,)*150,K+5,phase)
            assert ((phase,)+actual[4][:6])[::-1]==initial
            centres=tuple(states[(K+r-2)%32][2*r] for r in (1,2,3))
            literal=tuple(actual[K+r+2][W-r-1] for r in (1,2,3))
            assert centres==literal,(p,phase,K,centres,literal)
            if not any(centres): failures.append((p,phase,K,centres))
            if not any(centres[:2]): two_failures.append((p,phase,K))
            checks+=1
        if p==phase==1:
            assert tuple(states[(12+r-2)%32][2*r] for r in (1,2,3))==(0,0,0)
    print({'front_controls':checks,'three_centre_failures':len(failures),
           'two_centre_failures':len(two_failures),'finite_period32':'PASS',
           'all_length_negative_family':'p=phase=1,K=12+32n',
           'literal_front':'PASS'})


if __name__=='__main__': main()
