# Four crossing bins with one singleton count and seven counts at least three

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT324. Four crossing bins with one
singleton count and seven counts at least three (second-read by Cloud, CL448; moved here 2026-10-22)"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Four bins sharing two rows of consecutive numbers, one taking a lone number from the first, all other counts at
least three, reach any totals within the obvious limits.

**What it says.** Two separate rows of consecutive whole numbers are shared out among four bins, each bin taking a
fixed count of numbers from each row; a bin's total is the sum of everything it receives. In the first row one bin
takes a lone number and the others at least three each, and in the second row every bin takes at least three.
Requested whole-number totals can then be met exactly when they keep within the obvious limits: they add up to the
sum of all the numbers in both rows, and each bin, pair of bins and trio of bins asks for no less than it would get
from the lowest numbers of each row and no more than from the highest.

**Why it matters.** A known theorem splits each total between the rows so that each row keeps within its own limits,
but the lone number can still make the first row's split impossible to carry out. A one-unit trade between the lone
number's bin and the bin it blocks, one way in the first row and back in the second, always repairs the split in one
direction or the other. It needs the counts fixed in advance, with no other count below three, so it does not settle
the larger, unsolved problem it was built for, where the rows are the stretches either side of a missing number and
the counts must be chosen.

**An everyday picture.** Lay out tiles numbered 0 to 9 and let a friend take just tile 3: you can no longer pick
three tiles adding up to 4, since 0, 1 and 3 is the only way. So trade one point: your friend takes tile 2 and you
take 0, 1 and 4, while in a second row your friend's tiles add up to one more than planned and yours to one less, so
both grand totals stay the same. Either way round the trade mends the first row, and the second row always accepts
at least one of the two.

## The formal statement and proof

### GPT G324 — Four crossing bins with one singleton count and seven counts at least three (GPT, 2026-10-18; MI449, verified CL448)

*Status:* PROVED in the stated fixed-count scope; independent carrying read by Cloud,
CL448 / 48a1cd79, adopted in MI457 (2026-10-18). Originally filed as a
PROOF-SKETCH at MI449; the proof below is unchanged.
*Where:* GPT-MATH-INSTINCT.md MI448–449; source receipt in PRIOR-ART.md.
*Novelty:* UNASSESSED. Dependencies: known integral discrete separation, PROVED G315 and G316.

**Statement.** On two LABELLED interval copies [0,P-1] and [0,Q-1], prescribe
four-bin counts l=(1,b,c,d), with b,c,d>=3, and k=(k_A,k_B,k_C,k_D),
with every k_i>=3. Thus P=1+b+c+d and Q=sum k_i. Put L(r)=r(r-1)/2
and U_N(r)=r(N-1)-L(r). Integer combined targets v are realizable if and
only if sum v=L(P)+L(Q) and, for every bin group J,

 L(l_J)+L(k_J) <= v_J <= U_P(l_J)+U_Q(k_J).

Each copy is partitioned with its prescribed counts; a bin's target is its
sum across both copies. Independent translations of the copies are allowed
after subtracting their fixed count contributions. This is a fixed-count
theorem, not a count selector for the protected one-hole or five-bin parent.

**1. Obtain an integer rank split (known theorem).** Define
f(J)=U_P(l_J), g(J)=v_J-U_Q(k_J). The first is submodular and the second
supermodular; both are integer valued, vanish at the empty set, and f>=g
is exactly the combined upper bound. Frank's integral discrete separation
theorem gives an integer modular vector s with g(J)<=s_J<=f(J) for all J.
Here f(E)=g(E)=L(P), so sum s=L(P). Set t=v-s. Then sum t=L(Q),
t_J<=U_Q(k_J), and s_J<=U_P(l_J). Complementation supplies the lower
rank bounds for both rows. See Fujishige's primary slides, *Submodularity
and Discrete Convexity* (2012), PDF page 22, theorem “Discrete Separation
Theorem (Frank)” including its integrality clause; precise read scope MI448.
This step works for arbitrary nonnegative fixed counts and any number of bins.
It promises rank-feasible vectors, not physical realizations of those vectors.

**2. Classify the first row's failure.** The singleton A must take x=s_A.
Rank feasibility gives 0<=x<=P-1. For each other bin of size r, the cuts
on that bin and its union with A give precisely the actual scalar bounds
on R=[0,P-1] minus {x}:

 min_R(r)=L(r)+(r-x)_+,
 max_R(r)=min(U_P(r), U_P(r+1)-x).

By FOUR-BIN-PARTITIONS.md Lemma 2 and Theorem A (G315), this row is
realizable unless some other bin hits a scalar omission. Such an omission
has exactly one of the forms

 x=r, s_i=L(r)+1;  or  x=P-1-r, s_i=U_P(r)-1.

All three residual bin sizes are at least three, so G315 applies. If no
omission occurs, G315 realizes this row and G316 realizes the second row,
finishing the proof. Otherwise relabel the offending bin B, of size b.
Reflecting only the first row exchanges the two kinds of omission, so it
suffices to prove the following two-direction repair for the lower one.

**3. BOTH unit directions repair an offending first row.** Suppose
x=b and s_B=L(b)+1. Define s^+=s+e_A-e_B and s^-=s-e_A+e_B.
First both obey every rank cut. It suffices to check lower cuts that decrease.
For s^+, such a group J contains B but not A. If J={B}, its original
lower slack is one. Otherwise its count R_J is at least b+3, and the
original cut J union {A} gives

 s_J-L(R_J) >= R_J-b >= 3.

For s^-, a decreasing group J contains A but not B, with R_J>=1.
The original cut J union {B}, using s_B=L(b)+1, gives

 s_J-L(R_J) >= b*R_J-1 >= b-1 >= 2.

A decrement of one is therefore legal in every affected cut. Totals stay
fixed, so complementary upper cuts hold too.

Next neither repaired row has a scalar omission. A now takes b+1 or b-1,
and B's target is respectively L(b) or L(b)+2, so B has no lower omission.
Nor can it have an upper omission: U_P(b)-L(b)=b(P-b)=b(1+c+d)>=21,
whereas its new target is at most L(b)+2. For another bin, say C, a lower
omission would require its unchanged target to be L(c)+1. But the original
B+C cut forbids this, since L(b)+1+L(c)+1<L(b+c), as bc>=9.
An upper omission for C would require the new hole to be
P-1-c=b+d, which cannot equal b+1 or b-1 when d>=3. The same arguments
apply to D. The scalar bounds still hold by the rank checks just proved.
G315 therefore realizes BOTH s^+ and s^-. Reflecting values z to P-1-z
proves the same two-direction claim for an upper omission, with directions
interchanged. This reflection is only a row lemma, not a claim about
reflection preserving the parent's protected inequalities.

**4. The other row cannot block both compensating directions.** Its upper
rank function F(J)=U_Q(k_J) is strictly submodular on incomparable sets:

 F(X)+F(Y)-F(X union Y)-F(X intersection Y)
 = k_(X minus Y)*k_(Y minus X) > 0.

Consequently two incomparable upper cuts cannot both be tight at t:
modularity gives t_X+t_Y=t_(X union Y)+t_(X intersection Y), at most
the latter two F values, strictly below F(X)+F(Y). If t+e_A-e_B is
illegal, an upper cut containing A but not B must be tight; integrality
of the slacks justifies “tight”. If t-e_A+e_B is illegal, a tight cut
containing B but not A must exist. These cuts are incomparable, a
contradiction. Thus at least one direction is rank-legal. Lower bounds
follow from the fixed total and complements. Pair that legal direction
with the opposite first-row repair from step 3. G316 realizes the repaired
second row because all its counts are at least three. Combined targets
are unchanged. This proves sufficiency; necessity is immediate from ranks.

**Hand adversarial controls and limits.** The rank-feasible first row
(3,4,19,19) on [0,9], counts (1,3,3,3), is impossible: the only triple
summing to 4 is {0,1,3}, which uses A's token 3. Couple it to the second
row (3,12,21,30) on [0,11], counts (3,3,3,3). Decreasing second-row A is
blocked at its minimum. The other sign gives first targets (2,5,19,19)
and second targets (4,11,21,30), realized respectively by

 {2}; {0,1,4}; {3,7,9}; {5,6,8},
 {0,1,3}; {2,4,5}; {6,7,8}; {9,10,11}.

These disjoint lists cover each copy and retain combined targets (6,16,40,49).
An unexpected negative scope check is k_A=0: second-row A is fixed at zero,
so BOTH unit directions can fail, and strictness in step 4 is lost. That
case is excluded; no zero-count extension is inferred. Multiple thin bins,
a size-two first-row bin, count admission, and the full parent remain open.
No computational experiment or new census accompanies this proof candidate.

**Filing comparison.** proof_dupes --near W324: 342 entries, no repeats;
nearest G317 (.24), G315 (.20), W322 (.19), all read in full. G315 is the
one-hole dependency; G317 and G322 concern three bins in special two-hole
pools. This argument concerns four bins across two labelled intervals and
repairs a fixed-count rank split. It does not restate those criteria or
use G322. Similarity is not a novelty verdict.


**Independent review receipt (MI457).** Cloud CL448 / 48a1cd79 re-derived
all four carrying steps: integral discrete separation, the scalar-omission
classification, both physical first-row repairs, and strict-submodular
exclusion of two blocked compensating directions. It explicitly authorizes
PROVED in scope. Independent complete-row enumeration additionally reports
55,711 + 68,348 + 73,072 + 84,760 = 281,891 admitted targets, zero failures,
for the four patterns named in CL448. GPT read the checker source but did
not rerun it; those finite checks support, rather than replace, the hand read.
Cloud's separate SPLIT census was still running and is not claimed complete.
Count selection, multiple thin bins, H2 and the five-bin parent remain OPEN;
novelty remains UNASSESSED.
