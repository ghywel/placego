# GPT-MATH-INSTINCT, volume 4: MI373 to MI492; G325 (2026-10-18 to 2026-10-20)

*A frozen volume of [GPT-MATH-INSTINCT.md](../../GPT-MATH-INSTINCT.md), rotated out of it unchanged on 2026-10-22 in the documentation spring clean. New entries go in the live file; the list of volumes is at its top.*

### MI373 — B190: exact protected six-element exceptions by hand (2026-10-18 09:58 BST)

**HAND ARGUMENT,UNREVIEWED.** With at most three holes and six
available values,two bin sizes>=3 must both be3. Under the protected
lower margins and total condition,the only failures are

 S={0,2,3,5,6,8} or S={0,1,2,6,7,8}, with targets12,12.

This statement uses the ambient[0,M] normalization of H(h).
Endpoint holes trim as in MI371;the trimmed h<=2 case is covered
there,conditional on the h<=2 part of W318. The new h3,n6 case
below is independent of W318 and of any finite computation.

If all three holes remain after trimming,then M=8,0 and8 are
present,H is a three-subset of{1,...,7},and w=sum(H)>=6.
Put u<=v. From u>=12 and 2u<=u+v=36-w<=30,we need only
u=12,13,14,15. These four values are handled as follows.

- u12. The COMPLETE list of triples summing12 in[0,8] is
  048,057,138,147,156,237,246,345.
  Because0 and8 survive,blocking048 forces4 into H;
  blocking138 forces1 or3;blocking057 forces5 or7.
  Since there are exactly three holes,only four covers remain:
  {1,4,5},{1,4,7},{3,4,5},{3,4,7}.
  The first leaves237;the last leaves156. Each of the middle
  two meets all eight triples. They both have w12,so the other
  target is also12. These are exactly the two displayed failures.
- u13 requires w<=10. At least one of058 and067 survives:
  killing both requires hole5 and one of6,7,whose sum with
  the third positive hole is at least12,contradiction.
- u14 requires w<=8,hence max(H)<=w-3<=5;068 survives.
- u15 requires w<=6,hence H={1,2,3};078 survives.

Complementation supplies v and uses every remaining value exactly
once. This proves the claimed exception list without enumerating
pools. It does not classify the full spectrum outside protected
targets. The existing Cloud finite report is consistent support,
not a step in the argument. MI371 plus this result now gives the
full two-bin protected criterion for h<=3,r,t>=3,with precisely
these two exceptional instances at n6. The larger-n part still
has W318 as an unreviewed dependency.


### MI374 — B190: the actual two-pivot geometry repairs both terminal failures (2026-10-18 09:59 BST)

**HAND CONDITIONAL COMPLETION,UNREVIEWED.** This is a further
consequence in the actual three-bin remainder,not a proof that
the required selected realization always exists.

Let S=[0,M] minus H have three internal holes of either actual
missing-pivot repair shape

 H={p,p+1,M-1}, or H={1,p,p+1}.

There are three bins,all sizes>=3,and all proper groups satisfy
u_J>=L(r_J)+mu*r_J for mu>=3. Suppose A,size a,is a globally
least margin-adjusted-slack singleton,and SOME realization of A
leaves a normalized remainder with at most three holes.
Then the two remaining targets can be completed,conditional on
MI371/W318;the two exceptional n6 cases of MI373 are repaired
explicitly below. This implication does not assert the existence
of such a singleton or realization. Both are still selector issues.

MI368 supplies the remaining protected margins. If there are at
least7 values left,MI371 applies. If6 remain,the other two bin
sizes are3;MI373 applies unless the normalized pool is one of
its two exceptions and both shifted targets equal12.

Write b=min(remainder),c=max(remainder),h'=3 in that exceptional
case. MI368 gives

 mu'=h'+(mu-3)+(M-c)>=3.

The target12 of a triple also forces12>=3+3*mu',so equality
holds:mu'=mu=3 and c=M. Since mu'=a+mu-b,we obtain b=a.
The remainder has span8,so M=a+8 and the two original targets
are BOTH3a+12. If w=sum(H),the removed target is therefore

 u_A=L(a+9)-w-2(3a+12)=L(a)+3a+12-w.

Its own protected lower bound forces w<=12. Thus positive excess
margin already excludes the exceptional case,as does any top trim.
The exact equalities,not a guess about the shape,locate the repair.

For H={p,p+1,M-1},all holes internal means p>=1. Hence
w=2p+M>=a+10>=13,contradiction. This high-end shape never
produces a bad protected terminal pool from such an A.

For H={1,p,p+1},we have2p+2=w<=12,so2<=p<=5.
The original holes must avoid the actual remainder

 a+{0,2,3,5,6,8}, or a+{0,1,2,6,7,8}.

Above a,the missing positions are respectively a+{1,4,7}
or a+{3,4,5}. The adjacent original holes p,p+1 cannot lie
in the first three-position set. To lie in the second would
require p>=a+3>=6,contrary to p<=5. They cannot straddle a,
which is present in the remainder. Thus ALL original holes lie
below a,and the whole nine-value block[a,a+8] is available.

The current A contains exactly the three omitted positions of
that block;in either exception their sum is3a+12. Keep A's
values below a,and repartition the block into

 {a,a+4,a+8}, {a+1,a+5,a+6}, {a+2,a+3,a+7}.

All three triples sum3a+12. Give the first to A and the other
two to the remaining bins. Sizes and targets are unchanged,
all values are distinct and available,and the full pool is used.
This is the standard nine-value equal-sum construction applied
locally,not a new assertion about magic arrays. It completes
both terminal cases under the stated structured hypothesis.

**An actual lifted control.** In P=[0,14] minus5,the four-bin
sizes(3,5,3,3),targets(6,34,30,30) satisfy P_0. Their adjusted
slacks at margin1,in order A,B,C,D,are

 singles:0,19,24,24;
 pairs AB,AC,AD,BC,BD,CD:4,15,15,28,28,39;
 triples ABC,ABD,ACD,BCD:4,4,21,28.

Removing the uniquely least singleton {0,2,4},then shifting by-1,
gives S=[0,13] minus{1,3,4},sizes(5,3,3),targets(29,27,27).
Its single slacks at margin3 are4,15,15,and pair slacks4,4,21;
the size5 bin is a global least singleton,with ties retained.
Choose it initially as{0,2,6,9,12}. Its remainder is exactly
5+{0,2,3,5,6,8},so the two targets27,27 FAIL on that fixed
remainder. The local repair instead gives

 {0,2,5,9,13} / {6,10,11} / {7,8,12},

with sums29,27,27. Every value of S is used exactly once.
The original P instance itself lifts by MI362 to full[0,16],
first bin{0,1,7},sizes(3,3,5,3,3),targets(8,12,44,36,36).
Its gate has l2,k0,m14,q5;42>=10 and every residual size r>=3
has max(r,5-2r)=r. Hence this repair occurs inside the intended
five-bin reduction,not only in an unrelated three-hole example.

**Check that the shape hypothesis is used.** For the generic
pool[0,11] minus{1,4,7},targets(12,21,21),all sizes3,margin3,
the least singleton A={0,2,10} leaves the other bad pool
3+{0,2,3,5,6,8}. Its top nine-value block is NOT full.
The cut slacks are singles0,9,9 and pairs0,0,9,so slack alone
does not justify the nine-value repair. The whole target is
nevertheless positive:{0,3,9}/{2,8,11}/{5,6,10}. This control
limits the proof's inference;it does not refute general H(3).

Niggle sweep:all triples for12 listed;endpoints available before
covering arguments;smaller target chosen by bin interchange,not
pool reflection;total preserved;both exact equalities from the
bad terminal forced;high and low actual shapes kept distinct;
all original holes below a proved before using the full block;
the local equal-sum change keeps A's lower part;fixture slacks
and the original five-bin lift checked by hand. No machine result
or independent verification is claimed. No new PROOFS entry or
separate carrying request is opened at this intermediate step.

Gut:the interest is in the equality forcing a full block where a
local repair becomes possible. The initial easy induction failed,
but this is a specific structural simplification rather than more
hole bookkeeping. Reasoned:the exact two-bin base is now known
conditionally,including its terminal exceptions;the actual three-
hole two-pivot branch can repair those exceptions whenever its
least singleton has a realization leaving at most3 holes. Still
OPEN:obtaining that realization and treating a pair-minimum
branch. The actual two-hole legal-pivot branch is also separate.
Next cheap test:in the zero-excess low-end two-pivot shape,does choosing the
least adjusted singleton allow an endpoint-containing realization
with bounded residual holes? First derive its sum range and test
whether an endpoint is feasible;do not assume the root can be
assigned or generate another generic hole catalogue. W318 review
remains pending;13-minute heartbeat continues without a routine halt.


### MI375 — B191: endpoint feasibility versus the residual hole budget (2026-10-18 10:08 BST)

Question:in S=[0,M] minus{1,p,p+1},zero excess margin mu=3,
three sizes a,b,c>=3,does a globally least adjusted-slack singleton
have a realization containing0 and leaving at most3 normalized holes?
These are separate statements. The endpoint calculation was begun
by hand before this entry;no experiment has been run or is claimed
as preregistered. A bounded hand block will decide both statements
or identify the exact gap.

Record searched:record_find least.*singleton with containing.?0|
endpoint|hole.bound ->7 hits/4 files;read FOUR-BIN-PARTITIONS
sections3/6 and MI368/374. The two-hole scalar localization is
already in reviewed G315;the protected terminal completion remains
conditional on W318. This is an internal selector test,not a new
literature novelty claim. No repeat of the parked generic hole tree.

Pull:the least-slack bound appears to place the rooted sum safely
inside the scalar spectrum. Unease:using that existence to claim
a controlled complement would repeat the earlier false induction.
Kill test:find a genuine protected target for which EVERY realization
of the selected bin leaves more than3 holes,not merely a failed
canonical recipe. Independent hand controls:enumerate every subset
of a small selected target;verify all six adjusted slacks;give a
positive whole partition;check the exact five-bin lift separately.
Unexpected check:try to lift a selector failure all the way back to
a unique least-singleton choice on a full interval. Stop after the
endpoint proof and one decisive geometry verdict;no automatic census
or escalation to a four-hole catalogue.


### MI376 — B191 outcome: zero is feasible, but the three-hole selector fails on an actual lift (2026-10-18 10:12 BST)

**Verdict.** In MI375's zero-excess low shape,the globally least
adjusted-slack singleton CAN contain0. But there need not be ANY
realization of that singleton leaving at most3 normalized holes.
The counterexample below lies inside the actual five-bin reduction,
and its complete partition is positive. Thus the obstruction is to
the proposed induction,not to five-bin existence. All reasoning in
this entry is by hand and not independently reviewed;no experiment
or larger census has been run. No W318 assumption is used here.

**1. Endpoint feasibility.** Write m=b+c>=6,n=a+m=M-2,
L(r)=r(r-1)/2 and w=1+p+(p+1)=2p+2. The pool is
S=[0,M] minus{1,p,p+1},2<=p<=M-2. Suppose all proper
cuts satisfy u_J>=L(r_J)+3r_J and A is globally least for
adjusted slack delta_J=u_J-L(r_J)-3r_J. Comparing A
with its complementary pair gives

```text
L(a)+3a <= u_A <= L(a)+3a+am/2+1/2-p.             (1)
```

Indeed sum(S)=L(n)+3n+3-w,so delta_BC>=delta_A is
exactly twice the upper inequality. This uses the complementary
pair's slack,not the unsupported assertion that a least singleton
always exists. The statement is conditional on that choice.

A containing0 is equivalent to an (a-1)-subset of
Q=[2,M] minus{p,p+1} with sum u_A. Put r=a-1. Its least
sum alpha satisfies

```text
alpha <= L(r)+4r = L(a)+3a-3.
```

Its greatest sum is exactly

```text
beta = r*M-L(r)-2*(p-m-2)_+.
```

The unpunctured top r values start at m+4;the pair of holes
is below them when p<=m+2,and otherwise its two replacements
cost 2*(p-m-2). Subtracting the upper bound in (1) from beta
leaves

```text
D = (a-2)*m/2+p-7/2-2*(p-m-2)_+.
```

If p<=m+2 and a>=4,then D>=9/2. If p>m+2,then
D=m*(a+2)/2-p+1/2 >= a*(m/2-1)+1/2,using p<=a+m.
Thus for a>=4,u_A is at least3 above alpha and at least3
below beta. Q is a translated two-hole interval with subset
size r>=3 and complementary size m>=6. Reviewed G315's
scalar localization (FOUR-BIN-PARTITIONS section3) leaves
possible omissions only at distances1/2 from the actual extrema.
It therefore supplies the required rooted realization.

For a=3,the selected pair is too small to invoke that lemma.
Use the following direct check instead. In the full interval[2,M],
each sum s in[9,2M-5] has at least3 pairwise disjoint pairs:
the smaller member runs from max(2,s-M) through floor((s-1)/2),
which gives at least3 choices throughout this interval. Two removed
values cannot meet all of them. Here u_A>=12. If u_A<=2M-5,
this proves the assertion. Otherwise u_A>=2m+6 because M=m+5;
(1) forces p<=13/2-m/2<=7/2,hence p<=3. The displayed D
is positive also for a3 (at least3/2 in its first branch),so
u_A<=beta<2M. The pair{M,u_A-M} has second member at least
m+1>=7 and below M;it misses p,p+1 and belongs to Q. This
completes the endpoint argument,including the size boundary.

**2. A complete failure of the hole budget.** Take

```text
S=[0,15] minus{1,10,11},
(a,b,c)=(3,5,5), (u_A,u_B,u_C)=(12,43,43), mu=3.
```

Total sum is98. The six proper adjusted slacks are

```text
A,B,C:       0,18,18;
AB,AC,BC:    3, 3,11.
```

Thus A is the UNIQUE global least cut,not just a tied singleton.
Every three-set with sum12 is one of

```text
{0,3,9}, {0,4,8}, {0,5,7},
{2,3,7}, {2,4,6}, {3,4,5}.
```

This list is exhaustive by choosing the smallest value0,2 or3;
smallest>=4 would already give4+5+6>12. In the first row,the
remainder has minimum2 and maximum15. Removing three values from
a three-hole pool and trimming two bottom positions leaves exactly
4 normalized holes. In the second row,the remainder retains0 and15
and has exactly6 holes. None of the six possibilities leaves<=3.
In particular,endpoint feasibility does not repair the geometry.

This is NOT a counterexample to protected three-bin completion:

```text
{0,3,9} / {2,4,8,14,15} / {5,6,7,12,13}
```

has the required sizes and sums12,43,43. The theorem sought may
still hold even though this induction invariant is false.

**3. Unexpected check:the obstruction is on the actual route.**
Start from the full interval[0,18],five sizes(3,3,3,5,5),targets

```text
(E,D,A,B,C)=(15,19,21,58,58).
```

They total171. All proper full-interval lower-cut slacks are>=12,
and E has slack12. A compact independent arithmetic check groups
cuts by the number j of the two five-bins and number k of the
three three-bins. For each (j,k),take the smallest k of15,19,21:

```text
j=0, k=1,2,3:      12,19,19;
j=1, k=0,1,2,3:    48,45,37,22;
j=2, k=0,1,2:      71,53,30.
```

The empty and full cuts are excluded. Other choices only increase
the sum at the same cardinality. E is therefore the unique least
proper cut. Its canonical realization{0,1,14} leaves,after subtracting2,

```text
P=[0,16] minus12,
(D,A,B,C) sizes(3,3,5,5), targets(13,15,48,48), mu=1.
```

The proper adjusted slacks on P are

```text
singles D,A,B,C:              7,9,33,33;
pairs DA,DB,DC,AB,AC,BC:      7,25,25,27,27,41;
triples DAB,DAC,DBC,ABC:      10,10,18,20.
```

Hence D is a globally least adjusted-slack singleton. Its missing-
pivot recipe is the formal{0,1,12};the actual low repair is{0,2,11},
with the same sum13. Deleting it and subtracting1 gives EXACTLY
S above and targets12,43,43. The inherited margin is
3+1-1=3,so this is the zero-excess actual low two-pivot geometry,
not an arbitrary three-hole control. No inference from P_0 back to
a full-interval instance is assumed:the lift and every cut were
checked explicitly here.

**What changes.** The proposed route "remove a least singleton,
keep at most3 holes,then apply MI371/374" is REFUTED even on
actual lifted instances. MI374 remains a valid conditional argument;
its selector hypothesis cannot be supplied universally. W318's
central lemma and the established G315/G316/G317 are untouched.
The unique least singleton in the counterexample also means that
tie-breaking cannot cure this failure. Pair-minimum cases remain
separate,but are not responsible for this obstruction.

Niggle sweep:used actual values instead of ranks;treated a3 without
misapplying the minsize3 localization;proved D's two branches;
kept mu exactly3;checked both scalar extrema and pair distinctness;
enumerated every selected three-set;normalized by the actual survivor
endpoints;provided a whole positive partition;verified both earlier
least-cut choices and the exact missing-pivot repair;did not confuse
failure of an invariant with failure of a partition theorem. No new
PROOFS entry or routine carrying-review request is warranted here.

Gut:disappointment that the clean bounded-hole induction fails,but
relief that a decisive small example answers the niggle. The pull
is now toward the two surviving intervals,not another hole count.
Reasoned:zero can be assigned under the stated hypothesis;this is
not enough for recursive geometry. Do not extend the generic tree
to four holes. Next cheap test:after assigning0,the original low
shape becomes TWO full intervals separated by two missing values.
Keep that two-block representation and examine whether choices of
low/high counts for the three bins permit separate full-interval
partitions. First derive the coupled count/sum constraints and test
them against this exact positive fixture;do not assume that individual
sum intervals imply joint feasibility. This changes representation
at the failed inference instead of raising a census cap. Five-bin,
P_0,E28/L8 remain OPEN;13-minute heartbeat remains ACTIVE.

Loop check for B191:MI368's one-extra-hole step and MI376's fixed-three-
hole selector have both failed on actual inputs. This is enough evidence
to stop patching that induction,without waiting for the90-minute clock.
Fresh choice:the concrete two-interval allocation question still attracts
attention;the prospect of cataloguing successive hole patterns does not.
The next block changes representation and retains this counterexample
as its first control. No routine review halt.


### MI377 — B192: replace hole growth by two-interval count allocation (2026-10-18 10:18 BST)

Question:after assigning0 in the low shape,can the three bins be
constructed separately inside the two full intervals? Derive the
coupled counts and sums exactly;test the actual MI376 obstruction
and check whether singleton allocations invalidate any sufficiency
claim. This is a bounded hand block,no experiment. Some algebra
was explored before this entry;it is not a preregistered measurement.

Record searched:record_find two.block|two.interval|low.high with
partition|count|joint ->25 hits/10 files,mostly unrelated older work.
Read FOUR-BIN-PARTITIONS section2's exact one-hole spectrum,section5's
reviewed full-interval three-bin lemma,and PRIOR-ART's MI342 source
scope. The ingredients are already in the record;no external novelty
claim or new theorem review is proposed. The last counterexample,
rather than an enlarged census,is the first control.

Pull:the two intact intervals preserve far more structure than a
hole count. Concrete concern:partitions with a singleton can fail
individual rank bounds even on a full interval. Kill test for an
overstrong claim:force the rooted bin to take one token from each
interval under the actual protected cuts. Unexpected check:verify
that a simpler fixed-count criterion follows without even solving
a separate sum-splitting optimization. Stop after the exact regular-
count reduction and the singleton boundary;no generic hole catalogue.


### MI378 — B192 outcome: compatible count allocations and a shared-singleton repair (2026-10-18 10:25 BST)

**Status.** Hand reduction/application of the reviewed full-interval
three-bin theorem,plus an unreviewed shared-singleton repair. No
novelty claim,no experiment and no W318 dependency. It supplies a
constructive branch for the actual low shape;it does not yet prove
that every protected target has an allocation in this branch.

After assigning0 to A,write

```text
I=[2,p-1], P=p-2; J=[p+2,M], Q=M-p-1;
(r_A,r_B,r_C)=(a-1,b,c).
```

Let k_i be the number of J values assigned to bin i,and l_i=r_i-k_i.
Thus sum(k)=Q,sum(l)=P. Normalize the two full intervals separately
by subtracting2 and p+2. If x_i,y_i are their normalized bin sums,
then

```text
v_i = u_i-2*r_i-p*k_i = x_i+y_i,
sum(x)=L(P), sum(y)=L(Q), L(t)=t(t-1)/2.
```

For fixed counts set

```text
alpha_i=L(l_i), beta_i=l_i*(P-1)-L(l_i),
gamma_i=L(k_i), eta_i=k_i*(Q-1)-L(k_i).
```

A count row is called regular HERE if at most two counts are positive,
or if all three are at least2. This is just a local definition. A
regular full-interval row is jointly realizable exactly when its
three sums total the interval sum and satisfy their individual rank
bounds:use the reviewed three-bin theorem when all counts>=2,and
the elementary complete subset-sum interval for at most two bins.

**1. If both count rows are regular,only the individual combined
bounds need checking.** Precisely,the count allocation succeeds iff

```text
alpha_i+gamma_i <= v_i <= beta_i+eta_i, for each i.     (R)
```

Necessity is immediate. For sufficiency,seek integer low sums in

```text
max(alpha_i,v_i-eta_i) <= x_i <= min(beta_i,v_i-gamma_i),
sum(x)=L(P).                                         (S)
```

(R) makes each interval nonempty. The sum of the three lower
endpoints is at most L(P):expand a choice of either alpha_i or
v_i-eta_i for each i. Choosing none of the latter uses sum(alpha)
<=L(P);choosing all uses sum(v)=L(P)+L(Q) and sum(eta)>=L(Q).
For exactly one index i,use v_i-eta_i<=beta_i and
beta_i+alpha_j+alpha_k<=L(P). For exactly two indices i,j,
use v_k>=alpha_k+gamma_k and
eta_i+eta_j+gamma_k>=L(Q). These two auxiliary inequalities
are simply L(s+t)=L(s)+L(t)+s*t. Every choice therefore has
sum<=L(P),which proves the lower-endpoint claim. Reflecting BOTH
normalized interval summands gives the upper-endpoint claim
sum min(beta_i,v_i-gamma_i)>=L(P). This is an algebraic reflection
inside this fixed-count calculation,not an assertion that the original
protected cuts are invariant under reflecting S.

Integer intervals contain every sum between their endpoint sums,
so choose x with (S) and put y=v-x. Both regular rows can now be
partitioned independently;combining corresponding bins gives the
required original partition. Thus joint compatibility has not been
assumed from individual subset feasibility:it follows from this
three-coordinate sum-splitting argument and the reviewed row theorem.

**2. Both rows may instead have the SAME singleton bin.** The same
criterion (R) is sufficient if the counts are

```text
low:  (1,l,c),  high: (1,k,d),  with l,c,k,d>=2.
```

This case matters when a=3 and A must take one value from each
interval. First obtain a rank-feasible split (S),without asserting
that either row is already an actual partition. Let A's low/high
singleton values be x,y. Since their sums and the two other row
sums satisfy all individual full-interval rank bounds,each remaining
B target lies between the ACTUAL extrema after removing x or y.
For example in the low row,

```text
min_B = L(l)+(l-x)_+,
max_B = l*(P-1)-L(l)-(x-c)_+.
```

The first follows by taking the maximum of B's own lower bound
and the bound from C's upper sum;the second similarly follows from
B's upper bound and C's lower sum. The high row has the identical
form with k,d,y. The one-hole spectrum lemma now applies because
both remaining counts on each side are>=2.

Each of these two spectra is its full actual interval except possibly
minimum+1 and maximum-1. If the removed value is an endpoint,the
spectrum is full with width at least l*c>=4 (or k*d>=4). If the
removed value is internal,its width is at least l*c+1>=5. This
follows directly by subtracting the two displayed extrema:the loss
from l*(c+1) is at most l-1 for an internal x.

Their sum spectrum therefore contains the entire combined interval
except possibly its minimum+1 and maximum-1. To see the central
coverage when both widths U,V>=5,translate both minima to0.
Each spectrum contains{0,U} union[2,U-2],or the analogous V set.
The two central intervals add to[4,U+V-4];adding0 or an endpoint
covers the lower/upper tails[2,U+V-2],with adjacent or overlapping
joins since U,V>=5. Combined minimum+1 is missing only when BOTH
individual minimum+1 values are missing;the same holds at the top.
If one spectrum is full of width>=4,its translates overlap across
the other's at-most-one-point gaps and the entire sum interval fills.

By the exact one-hole lemma,a simultaneous lower omission requires
x=l,y=k and B's combined normalized target L(l)+L(k)+1. Move
A's values to x'=l+1,y'=k-1,keeping x'+y'=x+y. Give B the low
values0..l-1 and high values0..k-2 together with k. Their sum is
exactly L(l)+L(k)+1;they avoid A and have the prescribed counts.
C receives the complements. All values exist because l,c,k,d>=2.
For a simultaneous upper omission,x=c,y=d. Move A to c-1,d+1;
give B the top l low values,and the top k high values with d+1
replaced by d. Their sum is the previous combined maximum minus1.
Again C is the complement. These explicit slides fill the ONLY two
remaining possible gaps. No unchanged-root assumption is used:the
sum of A's two values stays fixed while their positions change.

Small adversarial control:take both normalized intervals[0,4] and
both count rows(1,2,2),combined targets(A,B,C)=(4,3,13). Freezing
A at2 on each side leaves pair spectra{1,3,4,5,7};their sum misses3.
The slide gives A=(3;1), B=({0,1};{0,2}), C=({2,4};{3,4}),
with combined sums4,3,13. The reflected target4,13,3 is repaired
by A=(1;3),B=({3,4};{2,4}),C=({0,2};{0,1}). These are
local repair controls,not claimed to satisfy the original protected
margin hypotheses.

**3. What the count choice now asks.** Each bin's legal k lies in
[max(0,r-P),min(r,Q)]. Its fixed-count scalar extrema are

```text
f_i(k)=2*r+p*k+L(r-k)+L(k),
g_i(k)=(p-1)*(r-k)-L(r-k)+M*k-L(k).
```

Both increase strictly with k on the legal range. Thus the counts
with f_i(k)<=u_i<=g_i(k) form an integer interval K_i,possibly
empty. Ignoring row types,an allocation of high counts exists iff
all K_i are nonempty and sum min(K_i)<=Q<=sum max(K_i).
This is only a count condition. The sufficiency proved above applies
when a choice summing to Q has two regular rows,or the shared-
singleton shape in section2. Establishing an admitted count choice
from the protected cuts is still OPEN;uncovered thin rows cannot
be silently discarded.

**4. Actual controls and the remaining boundary.**

- MI376's S=[0,15] minus{1,10,11},sizes(3,5,5),targets12,43,43
  has P8,Q4 and counts low(2,3,3),high(0,2,2),both regular.
  The normalized combined targets are8,13,13. The low-sum intervals
  in (S) are[8,8],[8,12],[8,12],whose sums include L(8)=28.
  For example low sums8,8,12 and high sums0,5,1 reproduce MI376's
  whole partition. No hole-bound invariant is required.
- S=[0,13] minus{1,7,8},sizes(3,4,4),targets12,31,32 has
  proper adjusted slacks0,13,14 / 1,2,11. The rooted A pair
  cannot lie wholly in[2,6] (maximum11) or[9,13] (minimum19).
  Both rows(1,2,2) are therefore a useful shared-singleton choice.
  An explicit partition is{0,2,10}/{3,4,11,13}/{5,6,9,12}.
- The remaining thin boundary is REAL under the protected cuts:
  S=[0,12] minus{1,6,7},sizes(3,3,4),targets12,21,31 has
  adjusted slacks0,9,13 / 0,1,10. With P4,Q5,A must split1/1.
  The high-count intervals are K_A={1},K_B={1,2},K_C={2,3}.
  Their only choices summing to5 are(1,1,3) and(1,2,2).
  Neither has two regular rows or section2's shared singleton with
  all four other counts>=2. Yet{0,4,8}/{2,9,10}/{3,5,11,12}
  is a partition. This is the next missing boundary,not a negative
  example to the protected theorem.

Niggle sweep:count sums imposed before normalizing targets;empty
rows/zero counts included;integer rather than fractional sum splitting;
all subset choices in the three-coordinate endpoint argument covered;
actual one-hole bounds derived from BOTH other-bin constraints;
width4 endpoint cases treated separately;root slides preserve its
sum and avoid duplicate values;minimum/maximum gap conditions taken
from the exact reviewed lemma;all three positive controls hand checked.
A full interval with counts(1,2,2),sums(2,2,6) remains a negative
control to applying the regular-row theorem indiscriminately:the
singleton2 removes every pair of sum2. No such assumption is used.

Gut:the useful surprise is that the two interval rows can compensate
for each other's isolated gaps by moving the shared singleton. This
is a concrete mechanism that was invisible to hole counting. Reasoned:
the new branch handles MI376 and a forced-split protected example;
it still needs count selection and thin rows. Next cheap test is the
crossed-singleton boundary just displayed:derive its distinct-value
constraints and ask whether a one-step slide or choice of the other
count allocation resolves them uniformly. Keep W318's separate review
pending;no new census or per-lemma review queue. P_0,five-bin,E28/L8
remain OPEN;13-minute heartbeat ACTIVE.


### MI379 — B193: the additional-singleton boundary (2026-10-18 10:33 BST)

Question:extend MI378 to low counts(1,1,c),high(1,k,d),c,k,d>=2,
and test whether the same combined-rank criterion might cover ALL
positive count rows. Hand reasoning already indicates a repair for
one additional singleton;it is not a measurement prediction.

Record searched:record_find singleton with two.interval|count.row|crossed
->4 hits/2 files;MI378 is the current result. The exact one-hole
spectrum and full-interval three-bin theorem are the existing reviewed
ingredients. No new literature theorem is assumed or novelty claimed.
Pull:the root can move without changing its total,and the other
singleton may trade places with it. Concern:if both interval rows
have two singletons,the two collision constraints could trap each other.

**Preregistration before the small diagnostic.** Predict that for
P,Q=3..6 and ALL ordered positive three-count compositions on each
side,the actual sum of the two partition-sum sets equals the complete
integer region given by the combined individual rank bounds and total.
This is a finite prediction,not a theorem or an automatic extension
beyond6. Counterfactual:any missing target satisfying these bounds
refutes the proposed all-positive-row extension;retain its exact
counts and target and stop trying to prove that general assertion.
The one-additional-singleton hand argument has its own scope.

Construct each row map by literal choices of two disjoint subsets;
independently build all row maps by sequential value-assignment DP.
Require complete equality before testing row sums. Check the resulting
sum maps against simultaneous reflection of both intervals. Independent
negative control:one interval[0,6] with counts(1,3,3),other[0,0]
with counts(1,0,0),combined targets(3,4,14),passes combined rank
bounds but has no partition (singleton3 removes the only route to
three-set sum4). Unexpected check:run that zero-count control even
though the main prediction requires all counts positive;do not silently
promote positivity to an irrelevant hypothesis. Positive controls:
MI378's regular-count fixture and the two shared-singleton edge repairs.

Stop after P,Q3..6,at most400 ordered count-row pairs,or10 CPU seconds,
or any control failure. No cap increase,no automatic rerun. Raw output
outside git;record the exact result and proof/measurement distinction.


### MI380 — B193 result: one additional singleton can be repaired (2026-10-18 10:37 BST)

**Status.** Hand PROOF-SKETCH,not independently reviewed. The fixed
finite diagnostic is separately COMPUTED below. No novelty claim,
W318 dependency,or five-bin theorem is asserted.

Let the two normalized intervals be[0,P-1] and[0,Q-1],with fixed
three-bin count rows

```text
low: (1,1,c), high: (1,k,d),  c,k,d>=2;
P=c+2, Q=k+d+1; L(n)=n(n-1)/2.
```

Then the combined individual rank bounds (R) of MI378 and total
conservation suffice for a joint partition. Interval exchange and
bin relabelling give the corresponding symmetric cases. This closes
the actual12/21/31 boundary named in MI378,not uniform count selection.

**Rank split and its only obstructions.** The interval-splitting
part of MI378 produces integer row sums satisfying each row's
individual rank bounds and total;that algebra does not require
regular counts. Write the two singleton low sums x,z and the high
A singleton y and B sum w. Thus the combined A,B targets are
x+y,z+w. Put U=k*(Q-1)-L(k). The low row is realizable precisely
when x!=z. Its C rank bounds say

```text
1<=x+z<=2*P-3.
```

Consequently a collision x=z=t has1<=t<=P-2. In the high row,
B's own bounds and C's complementary bounds place w between the
actual k-subset extrema after deleting y. The reviewed one-hole
spectrum lemma says the only nonrealizable possibilities are

```text
lower gap: y=k, w=L(k)+1;
upper gap: y=d, w=U-1.
```

At fixed D=y+w,at most one gap can occur:the two exceptional D
values are L(k+1)+1 and U_(k+1)-1,whose difference is
(k+1)*d-2>=4. Here U_(k+1) is the maximum(k+1)-subset sum
in[0,Q-1]. This distinguishes a rank-feasible split from a partition.

**1. Remove a low collision.** Suppose x=z=t. Try either

```text
plus:  low(A,B)=(t+1,t-1), high(A,B sums)=(y-1,w+1);
minus: low(A,B)=(t-1,t+1), high(A,B sums)=(y+1,w-1).
```

Both low rows are actual;both preserve C's low sum. High C's sum
also stays fixed. Plus fails high rank bounds only if y=0 or w=U;
minus fails only if y=Q-1 or w=L(k). Both cannot fail:the only
compatible simultaneous endpoint possibilities would be
(y,w)=(0,L(k)) or(Q-1,U),and each violates the complementary
rank bound for A union B (minimum L(k+1),maximum U_(k+1)).

If both moves obey high rank bounds,at most one meets a high gap
by the fixed-D observation,so choose the other. If just one obeys
rank bounds but hits a gap,there are only two genuine boundary cases:

- Plus hits the lower gap:the original y=k+1,w=L(k).
  Keep A at low t/high k+1;give low B the value t-1 and high B
  the k values0..k-2 together with k. Their high sum is L(k)+1.
- Minus hits the upper gap:the original y=d-1,w=U.
  Keep A at low t/high d-1;give low B the value t+1 and high B
  the top k values with d+1 replaced by d. Their high sum is U-1.

Each displayed construction preserves both combined targets,uses
distinct legal values,and lets C take the complements. Plus hitting
the upper gap cannot be the sole rank-legal move:its original values
are y=d+1,w=U-2,so minus is legal as k>=2 and U-L(k)=k*(d+1)>=6.
Similarly minus hitting the lower gap has original y=k-1,w=L(k)+2,
and plus is legal. This exhausts low collisions,including simultaneous
obstructions in the two rows.

**2. Repair a high gap when the low row is already actual.** Suppose
x!=z and the high row is at its lower gap y=k,w=L(k)+1. Change y
to k-1 or k+1,compensating x to x+1 or x-1,and keep z,w fixed.
For either high singleton,the explicit B set0..k-2 together with k
has sum L(k)+1 and avoids A. Thus only a low endpoint or a new
low collision could block the move. If both directions are blocked,
the two possibilities are exactly x=0,z=1 or x=P-1,z=P-2:

- At x=0,z=1,swap low A,B to1,0. Give high A the value k-1
  and high B the values0..k-2 together with k+1 (sum L(k)+2).
- At x=P-1,z=P-2,swap low A,B to P-2,P-1. Give high A k+1
  and high B0..k-1 (sum L(k)).

All combined sums and counts are preserved. The high upper gap is
obtained by reflecting BOTH normalized intervals;the rank region,
counts and partition property are invariant under this bijection.
This reflection is internal to the fixed-count theorem,not an
assumption about invariance of the original protected-margin cuts.
Cases1 and2 now produce actual partitions from every rank split.

**Actual boundary reached.** On S=[0,12] minus{1,6,7},targets
12,21,31 with sizes3,3,4,put0 in A. The intervals[2,5] and[8,12]
have the permitted count rows(1,1,2)/(1,2,2) and normalized combined
targets(2,3,11). The theorem applies. The literal partition
{0,4,8}/{2,9,10}/{3,5,11,12} checks counts,sums and disjoint coverage.
Thus the additional singleton was a repairable obstruction in the
construction,not a negative example to the protected theorem.

**Finite diagnostic (MI379 preregistration).** The new probe
`tests/probes/instinct/two_interval_count_smoothing.py` completed its
fixed P,Q=3..6 domain:400 ordered pairs of positive count rows,
44656 combined rank targets,NO missing target. All complete row maps
for lengths1,3,4,5,6,7,8 agreed between literal disjoint-subset
enumeration and sequential assignment DP. Four positive controls,
whole-map simultaneous reflection,and the zero-count negative control
passed. CPU0.256752 seconds on GPT's host;no timing comparison is
claimed. Raw JSON is outside git;no rerun or domain expansion.
The fourth positive control is this block's thin boundary,in addition
to the three explicitly listed in MI379. The all-positive-row
extension remains a CONJECTURE beyond the hand cases above/MI378;
this finite equality is not its proof. The negative control shows
that dropping positivity is not justified by these observations.

Niggle sweep:the initial row split is only rank-feasible;all actual
realizations enter through explicit disjoint sets or the reviewed
scalar lemma. Collision moves keep C's row sums fixed until an
explicit construction takes over;the latter automatically preserves
C's combined sum by conservation. The sole-legal-move exceptions use
k,d>=2,including their equality cases;no nonexistent endpoint is used.
Both endpoint swaps preserve each bin's combined sum. No original
protected-cut reflection,unproved general smoothing,or W318 claim is
used. Probe maps are independently constructed and the negative
control fails exactly where required;finite coverage is kept finite.

Gut:the attraction is specific rather than inherited warmth:the two
intervals absorb each other's single-value exclusions,and the thin
case now has a short repair. Reasoned:that mechanism advances the
chosen representation and reaches an actual protected example. The
next cheap question is whether TWO thin rows can always avoid their
two simultaneous collisions. For example low(1,l,1),high(1,1,d)
leaves a two-dimensional integer rank region with two forbidden
lines. Analyse that geometry by hand before enlarging any census.
Uniform selection of the counts from protected cuts is separately
OPEN. W318 remains the existing carrying request;no new per-lemma
review queue. P_0,five-bin,E28/L8 OPEN;13-minute heartbeat ACTIVE.


### MI381 — B194: simultaneous thin rows (2026-10-18 10:46 BST)

Question:do MI378's combined rank bounds suffice when BOTH interval
rows have at least two singleton bins? Choose the actual distinct-value
constraints,not a hole-count surrogate. Record searched:record_find
with two.thin|two.interval|collision.lines -> MI378-380 and prior
count-allocation entries;irrelevant old project hits discarded.
The reviewed scalar ingredients and MI378's rank splitting are the
current starting points;no external theorem or novelty claim is needed.

Pull:the forbidden-line description may be overcomplicating this.
At a collision the low singleton is necessarily internal,so either
unit adjustment stays inside its interval. This might let the other
interval choose which direction is safe. Kill test by hand:force the
other singleton to an endpoint beside its partner,where only one
ordinary move is possible. If those endpoint traps have no repair,
retain them and narrow the statement. No experiment or enlarged run.


### MI382 — B194: all positive two-interval count rows (2026-10-18 10:49 BST)

**Status: complete hand PROOF-SKETCH,independent verification pending;
novelty UNASSESSED.** The two-thin-row question admits a short repair.
Following that mechanism also closes the remaining positive row types.
This is a theorem about FIXED counts,not a proof that the original
protected target admits such counts. No new computation is run.

**Statement.** Take two labelled copies of the integer intervals
[0,P-1],[0,Q-1]. Let l_i,k_i>=1 be integers for i=A,B,C,sum(l)=P,sum(k)=Q.
For integer targets v_i,there are partitions with these counts and combined bin sums v_i
if and only if sum(v)=L(P)+L(Q) and,for each i,

```text
L(l_i)+L(k_i)<=v_i<=l_i*(P-1)-L(l_i)+k_i*(Q-1)-L(k_i).
```

Here L(n)=n(n-1)/2. Translating either interval adds its fixed
count times the translation to each target,so the statement applies
to the original separated intervals. Copies are labelled;equal
normalized values in DIFFERENT copies are not a collision.

**A. Rank splitting and a fibre bound.** MI378 section1's integer
interval argument first splits v into low and high row sums meeting
each row's rank bounds and total. That argument uses no regularity
hypothesis until the final realization step. We now repair the split.
For any full interval of length n=a+b+c,hold its B sum z fixed.
The possible A sums within the rank region form the integer interval

```text
max(L(a),L(n)-z-U_c) <= s <= min(U_a,L(n)-z-L(c)),
U_j=j*(n-1)-L(j).
```

Its width is at least a*c. Indeed each of the four upper-minus-lower
endpoint differences is at least a*c:two are U_a-L(a)=a*(b+c)
and U_c-L(c)=c*(a+b);the others follow by substituting z=U_b
or z=L(b),respectively,and equal a*c at those extremes. Thus if
all three counts are positive,the fibre has at least two integers.
If the whole row has all counts>=2,it is realizable by the reviewed
full-interval three-bin theorem MI295,throughout this rank region.

**B. Both rows have at least two singleton bins.** Call such a row
thin. A thin row is actual exactly when its chosen singleton values
are distinct;its remaining bin takes the complement. Rank bounds
force their sum to lie between1 and2P-3. A collision x=z=t therefore
has1<=t<=P-2. If neither row collides there is nothing to do. Choose
a colliding row as low;the other row may itself collide.

If the singleton bin pairs coincide,call them A,B. Write the high
singletons y,w. Some one-coordinate unit move of (y,w),within
[0,Q-1]^2,makes them distinct:try a neighbour of y different from w;
if none exists,y is an endpoint and w its adjacent value,so move w
one step away from y (Q>=3). Compensate by the opposite move of
the matching low singleton t. It stays in range and differs from
the unchanged t. Both rows are now actual;C takes the complements.
The combined sum in each bin is unchanged.

If the pairs differ,relabel so low has A,C singleton and high has
A,B singleton. Low A=C=t,high A=y,B=w. Try changing low C to t+e
and high B to w+e,e=+1 or-1,keeping low A and high A fixed.
Both remaining-bin sums change by-e,so all combined targets stay
fixed. Choose a legal neighbour w+e different from y. This succeeds
unless (w,y)=(0,1) or(Q-1,Q-2). In the first exception instead
change low A to t+1 and swap high A,B from(1,0) to(0,1).
In the second change low A to t-1 and swap high A,B from(Q-2,Q-1)
to(Q-1,Q-2). Low C stays t. All values are legal and distinct;
complements give the correct remaining sums. This covers all thin
pairs,including rows(1,1,1),without a lattice-point counting argument.

**C. A regular positive row absorbs any other row's defect.** Here
regular means all three counts>=2. If the other row is also regular,
MI295 realizes both. If it is thin and collides at t,t,move either
one of its singleton values by one step and compensate in the same
bin of the regular row,keeping another bin's sum fixed. Both signs
are legal in the thin row;by partA at least one sign is rank-legal
in the regular row. Both resulting rows are actual.

Otherwise the other row has exactly one singleton,say low A= x,
with counts(1,b,c),b,c>=2. The reviewed one-hole lemma says a
rank-feasible row can fail only at x=b,B sum L(b)+1,or its reflected
upper case. In the lower case either x=b-1 or x=b+1 allows the
explicit B set{0,...,b-2,b},keeping B's sum fixed. Compensate in
high A while holding high B fixed. PartA again supplies a rank-legal
sign,and the regular row is actual. Reflect BOTH intervals for the
upper case. All targets transform and recover bijectively.

**D. Different singleton owners.** It remains useful to prove a
slightly broader repair:low counts(1,b,c),b,c>=2;high counts(a,1,d),
a,d>=1. Low A is singleton;high B is singleton. Here we repair a low-row
gap. PartE handles the orientations where only the high row fails.

Suppose the low row fails at its LOWER gap:low A=b,B sum L(b)+1.
Let high B=y,high A sum z. At fixed y,the high A rank fibre equals
its actual extreme interval after deleting y. Its possible omissions
have these three properties:

(i) Two values z-1,z+1 in that interval cannot both be missing.
(ii) If the minimum plus1 is missing,then y=a and the minimum is L(a).
(iii) If the maximum minus1 is missing,the width is at least2 and
      the maximum minus2 is present.

For a,d>=2 these follow from the reviewed one-hole spectrum lemma:
only extreme-distance1 omissions are possible;an internal deletion
has width>=a*d+1>=5,while endpoint deletions have none. If a=1,
the spectrum is simply[0,Q-1] minus y. If d=1,it is its reflected
complement spectrum L(Q)-y-([0,Q-1] minus y). These explicit sets
prove(i)-(iii) also when a or d equals1,including a=d=1,Q=3.
For clarity,in the d=1 case an internal y gives minimum
L(Q)-y-(Q-1);minimum+1 is missing exactly when y=Q-2=a,
and that minimum is L(a). Endpoint deletions give full intervals.

Try low A=b-1 or b+1,low B unchanged;high A becomes z+1 or z-1,
high B unchanged. Low B is realized by{0,...,b-2,b} for either
choice. The high fibre has width>=a*d>=1 by partA,so at least
one neighbour is rank-legal. If both are legal,(i) gives an actual
choice. If only one is legal and it is missing:

- The legal neighbour is z+1:then z is the fibre minimum and(ii)
  gives y=a,z=L(a). Keep low A=b and high A sum L(a),increase
  high B from a to a+1,and decrease low B sum from L(b)+1 to L(b).
  Use low B={0,...,b-1},high A={0,...,a-1};both avoid their
  respective singleton. High B=a+1 is legal since d>=1.
- The legal neighbour is z-1:then z is the fibre maximum. Instead
  put low A=b+2 and high A sum z-2,keeping B unchanged.
  Low A exists since c>=2 and avoids the same displayed low B set;
  (iii) supplies an actual high A set disjoint from high B=y.

Complements give C;every modification preserves all combined sums.
Reflection of both intervals handles a low upper gap. Thus ANY
low-row gap is repairable with this high singleton owner,whether
or not the original high row was actual.

**E. Exhaustion of row types.** PartB handles two thin rows and
partC handles any regular row. Remaining rows each have a singleton,
and at least one has exactly one. Choose such a row as low,with
singleton A. If high has a singleton in another bin,rename that bin
B and use partD whenever low is nonactual. If low is actual but high
is nonactual:

- If high also has exactly one singleton,swap the two rows and
  relabel its singleton A;the old low singleton is a different bin,
  so partD applies.
- If high has exactly two singleton bins sharing low's singleton,
  use MI380 with interval/bin relabelling. Its other two counts
  are the two >=2 counts of the old low row. Otherwise choose
  high's singleton pair B,C,disjoint from low's singleton A;this
  includes high(1,1,1).
  A high collision at t,t forces t internal. Change high B,C to
  t+e,t-e,for e=+1 or-1,and compensate low B,C sums by-e,+e,
  holding low A fixed. Both high pairs are legal and distinct.
  The low one-hole fibre has width>=b*c>=4;at least one neighbour
  is rank-legal,and two legal neighbours cannot both be missing.
  If the sole legal neighbour is missing,the original low B sum
  is its minimum or maximum. In the lower case the one-hole lemma
  forces low A=b,low B sum L(b). Instead increase low A to b+1
  and high C from t to t+1,keeping low B and high B unchanged.
  Low B={0,...,b-1} avoids its new singleton;high B,C are distinct.
  The low C sum falls1 and the high A sum falls1,so all combined
  targets are preserved. At the upper extreme low A=c,low B is
  the top b-set;decrease low A to c-1 and high C to t-1 instead.
  Again complements finish the construction. This argument also
  handles high(1,1,1):choose its B,C singleton pair,disjoint from
  the low A singleton,even though it has a third singleton.

For high thin rows with exactly two singletons SHARING low's A,
MI380 applies because the high remaining count is>=2 and low's
other two counts are>=2. The preceding disjoint-pair argument
handles every other thin row. Finally,if high has no singleton
except A,both rows have that same sole singleton and MI378 section2
supplies the shared-singleton spectrum/slide construction. Thus all
positive row pairs are covered. All unreviewed dependencies are
explicit:MI378's rank split/shared-singleton repair and MI380's
shared additional-singleton repair. Reviewed ingredients are MI295
and the one-hole scalar lemma;W318 is not used.

**Adversarial hand controls and niggle sweep.** At P=Q=3 and all
counts1,the rank split(1,1,1)+(1,1,1) has two colliding rows;
partB can replace it by(0,1,2)+(2,1,0),giving(2,2,2). This is
also the smallest case where the ordinary no-two-neighbour-gaps
argument needs its singleton-spectrum qualification.
For partD take low(1,2,2),high(1,1,1). The failed low sums
(2,2,6) plus high(0,1,2) give targets(2,3,8);the lower-end repair
uses low A2,B{0,1},C{3,4},high A0,B2,C1. For high(2,1,0)
instead,the targets(4,3,6) require the other endpoint repair:
low A4,B{0,2},C{1,3},high A0,B1,C2. The two-step low move
uses c=2 exactly;it is not silently treated as an interior move.
For partE's disjoint singleton pair,take low counts(1,2,2),sums
(2,1,7),and high counts(2,1,1),sums(4,1,1). Moving high B,C
oppositely meets the low missing sum2. The alternate construction
low A3,B{0,1},C{2,4};high A{0,3},B1,C2 realizes the same
combined targets(6,2,8). These are literal controls,not new runs.

Every use of a neighbouring target checks the fixed-row rank fibre
before invoking realization;the width assertion is algebraic. Thin
rows are actual by distinct singleton values and their complements,
not by rank alone. The d=1/a=1 spectra are handled explicitly,
including width2. The upper-gap reflections act on both interval
copies and transformed targets. Row-type exhaustion includes
all-ones rows and the disjoint singleton-pair orientation that a
quick shared-root argument would miss. Existing zero-count negative
control from MI379 prevents weakening positivity. MI380 is cited
with its exact c,k,d>=2 scope. No finite census closes an infinite
quantifier here;MI380's 400-row diagnostic is supporting evidence only.

Literature check:two targeted primary-literature searches found Gao,
Hwang,Li,Rothblum(1999),*Partition polytopes over 1-dimensional
points*,DOI10.1007/s10107990019a. The institutional abstract describes
convex-hull inequalities for prescribed counts;the attempted full
text opened a login page. No integer saturation theorem from it is
being imported,and the abstract is insufficient to settle novelty.
The source pointer/read limitation is filed in PRIOR-ART.md.

Gut:the surprise is that endpoint traps have forced identities,
which make explicit swaps possible. This earns continued interest:
it replaces several separate count restrictions by one criterion.
Reasoned:the full positive-count compatibility statement now has a
complete hand candidate,subject to independent review and unknown
novelty. Next return to the actual protected target:can its scalar
count intervals be chosen with every low/high count positive and
with the required total? Zero-count rows must be handled separately;
this theorem does not erase them. Five-bin/P_0/E28/L8 remain OPEN.
This is a useful combined-proof review milestone,not a reason to
halt the independent count-selection work.13-minute heartbeat ACTIVE.


### MI383 — B195: the zero-count boundary and the remaining count capacity (2026-10-18 11:05 BST)

**Question and status.** Continue the actual protected low shape of
MI376 after assigning0 to its globally least adjusted-slack singleton
A. Does allowing zero interval counts introduce a further joint
obstruction beyond scalar count admission? Hand work begun09:56 UTC;
this is its retrospective work record,not an experimental preregistration.
No experiment was run. Record searched:record_find with the combined
terms count.admission,zero.count,least.adjusted returned no hits;
the directly read notebook MI376/378/380/382 supplies the actual prior
work. Reviewed ingredients remain MI295 and the one/two-hole scalar
lemmas. G319 and MI376 are unreviewed dependencies;W318 is not used.

Pull:the explicit two-interval exchanges remain interesting because
count0 may have a short structural classification. Unease:positivity
in G319 cannot simply be dropped. The hand test below isolates its
failure shape,then checks the actual protected inequalities. A second
niggle is whether separate feasible count intervals automatically
have the correct total;they do not in general. Keep that step open.

Use S=[0,M] minus{1,p,p+1},a,b,c>=3,a+b+c=M-2,
u_A+u_B+u_C=sum(S),and every proper cut
u_J>=L(s_J)+3s_J. A is globally least among all singleton/pair
adjusted slacks delta_J=u_J-L(s_J)-3s_J. In particular

```text
delta_AB=delta_A+delta_B-ab, hence delta_B>=ab;
delta_AC=delta_A+delta_C-ac, hence delta_C>=ac.       (1)
```

This stronger consequence of the pair comparisons is essential below.
After assigning0 to A,put r=(a-1,b,c),P=p-2,Q=M-p-1,
I=[2,p-1],J=[p+2,M]. All remaining bin sizes are>=2.

**1. Zero counts: the only possible failure shape.** Fix legal
counts l_i+k_i=r_i,sum(l)=P,sum(k)=Q and assume the combined
individual rank bounds and total. MI378 supplies integer low/high
row targets obeying each row's rank bounds,even with zeros.
If both rows are positive,G319 supplies joint partitions. If both
have at most two positive counts,each is regular and MI378 applies.
Suppose high has exactly two positive bins B,C;low A=r_A>=2.
If the low row is not regular,it has one or two singleton bins:

- Sole singleton B:low counts(alpha,1,gamma),alpha,gamma>=2.
  A nonactual low row has B=alpha and A sum L(alpha)+1,
  or the reflected upper gap,by the one-hole scalar lemma.
  Replacing B by alpha-1 or alpha+1 while keeping the A sum
  fixes the lower gap:use A={0,...,alpha-2,alpha}.
  Compensate the low B change by the opposite high B change,
  and high C by the reverse change. The binary high B interval
  has width k_B*k_C>=1,so at least one neighbour is legal.
  Reflection handles the upper gap. Singleton C is symmetric.
- Two low singleton bins B,C:the only failure is a collision t,t.
  Rank feasibility forces 1<=t<=P-2. Replace the two values
  by t+1,t-1 or t-1,t+1 and compensate in the binary high row.
  Again its interval of width>=1 allows one direction.

If high has just one positive bin H,all high values belong to H.
The other two low bin counts are their full r_i>=2. If low H is0
or>=2,the low row is regular. Thus the ONLY unresolved fixed-count
shape is:one interval wholly belongs to H,and H takes exactly ONE
value of the other interval. In that other interval the remaining
two counts are>=2,and the only possible failure is a one-hole
minimum-plus1 gap for one of those bins (a maximum-minus1 gap
for one is a minimum-plus1 gap for its complement).
Swapping the two rows gives the other orientation. An empty interval
leaves one full row with all r_i>=2,covered by MI295.

**2. The actual hypotheses exclude that exceptional failure.**
If H owns the whole high interval and one low value,the other two
bins are low-only. A failure gives one of them its low minimum+1.
For a nonroot size s this is L(s)+2s+1<L(s)+3s. For root A it
is L(a-1)+2(a-1)+1=L(a)+a<L(a)+3a. Both violate protection.

Now let H own the whole low interval and one high value. Write
that high value as p+2+y;sum(I)=L(p)-1.
If H=A,then a=p. A failure for nonroot B forces y=b and
u_B=L(b)+(p+2)b+1. Thus delta_B=(p-1)b+1<ab,
contradicting(1),since b>=3. The same holds for C.

If H is nonroot,rename it C. Then c=p-1>=3,so p>=4.
The other high counts are a-1,b;Q=a+b. There are two failures:

- Root A is at its high minimum+1. Then y=a-1 and
  delta_A=(p-2)a-p,delta_C=a-p+2.
  The required delta_C>=delta_A would give (p-3)a<=2,
  impossible for p>=4,a>=3.
- B is at its high minimum+1. Then y=b and
  delta_C=b-p+3. A is the complementary high maximum-minus1,
  giving delta_A=(a-1)(p+b)-a-3.
  Thus delta_C>=delta_A would require
  (a-2)b+ap-a-6<=0,also impossible for a,b>=3,p>=4.

These formulas use original sizes/slacks:the removed0 changes A's
cardinality but not its target. They exhaust the two possible
one-hole omissions;there is no reflection assumption about the
protected inequalities. Consequently ANY scalar-admitted count
allocation completes jointly in this actual least-singleton case,
conditional on G319 for the positive rows.

**3. Exact remaining scalar question.** For each bin of remaining
size r define its legal k range max(0,r-P)<=k<=min(r,Q),and

```text
f_r(k)=2r+pk+L(r-k)+L(k),
g_r(k)=(p-1)(r-k)-L(r-k)+Mk-L(k),
K_i={legal integer k:f_(r_i)(k)<=u_i<=g_(r_i)(k)}.
```

Both f and g strictly increase on the legal range:their forward
differences are p+k-(r-k)+1 and Q+1+(r-k)-k respectively.
The first is positive since r-k<=P=p-2;the second since k<=Q.
Thus K_i is an integer interval,possibly empty. A selection with
sum(k)=Q exists exactly when all K_i are nonempty and

```text
sum min(K_i) <= Q <= sum max(K_i).                  (2)
```

There is no extra restriction that counts be positive.
In fact each K_i is nonempty under our hypotheses. A follows from
MI376. For B,let alpha,beta be its actual extrema in
[2,M] minus{p,p+1}. The b smallest values give alpha<=L(b)+4b.
By(1),u_B>=L(b)+(a+3)b>=alpha+6. The complementary size
is a+c-1. Its minimum is at most
L(a+c-1)+4(a+c-1)=L(a+c)+3(a+c)-3.
The protected AC cut therefore gives u_B<=beta-3.
Both subset/complement sizes are>=3,so the reviewed two-hole
scalar lemma realizes u_B. Same for C. Every actual subset has
some high count,which proves K_B,K_C nonempty.

What is NOT yet proved is(2). This is now the exact remaining
rooted count-admission step,conditional on the hand reductions above.
The first algebraic foothold is(1);using only separate subset
feasibility would lose the global least-slack information.

**Controls and niggle sweep.** The existing protected12/43/43
fixture of MI376 forces k_A=0 and has regular rows;it prevents
mistaking positivity for necessity. The earlier zero-row negative
control of MI379 is consistent with section1's exceptional shape.
As an unexpected hand control for section3,take the same type of
pool S=[0,11] minus{1,6,7},sizes3,3,3,targets14,26,12.
With0 assigned to A,individual counts are feasible but their maxima
are1,2,0,whose sum3 is below Q=4. The full target is nevertheless
partitionable with0 in C:{2,3,9}/{5,10,11}/{0,4,8}.
This is NOT a protected counterexample:its AC target26 is below
L(6)+18=33,and A is not globally least. It serves only to disprove
the generic implication from nonempty K_i to a feasible count total.
Do not reuse it as a protected wrong-root example.

For the zero-row repairs,all moved singleton values are legal;
collision t=0 or P-1 is excluded by the complementary rank bound.
A binary row has a complete sum interval,so no hidden singleton
spectrum assumption is needed there. Empty rows and original A size3
are covered explicitly. Exceptional-shape exclusions use actual
protected/least inequalities,not an arbitrary rank-relaxed surrogate.
No finite check upgrades G319 or this reduction to independently
verified status. No new PROOFS entry or carrying request is opened.

Gut:the interest has a new reason today:the joint zero-count geometry
has collapsed to a scalar capacity question. The unfinished inequalities
are a real obstacle,not just another renamed hole case. Reasoned:
conditional exact reduction and individual nonemptiness established
by hand;the two aggregate capacity inequalities remain OPEN. Next
cheap step:derive a contradiction from a deficit in the maximum
counts using(1),then separately examine minimum counts without
assuming reflection preserves protection. Five-bin/P_0/E28/L8 OPEN.
13-minute heartbeat remains ACTIVE;no routine review halt.


### MI384 — B196: both count-capacity inequalities in the protected low shape (2026-10-18 11:16 BST)

**Question/status.** Prove the two aggregate inequalities left by
MI383 for S=[0,M] minus{1,p,p+1},a,b,c>=3,all proper protected
cuts,and a globally least adjusted-slack singleton A. This entry is
a COMPLETE hand argument for count capacity. Together with MI383
and pending G319,it gives a conditional rooted partition of this
specific low shape. It does not cover arbitrary three-hole pools,
a pair-minimum branch,or the full five-bin problem. No experiment
or new census. The work is not independently reviewed.

Record searched:record_find capacity.deficit with count returned no
hits;MI376/378/382/383 were read directly. The proof uses their exact
count endpoints and original slacks. No external theorem or novelty
claim is added. The nearby partition-polytope prior art remains
abstract-read only,as recorded in MI382/PRIOR-ART.

Initial pull:the pair comparisons delta_B>=ab,delta_C>=ac are
stronger than the separate feasibility used so far. Test a shortage
of high counts against those comparisons. Unease:reflecting the pool
will NOT preserve the protected hypotheses verbatim. The unexpected
hand check is to translate the reflected inequalities from scratch;
retain a separate proof for the opposite capacity bound. Stop at
this exact scalar question,not a new hole-case catalogue.

Keep MI383's notation:r=(a-1,b,c),P=p-2,Q=M-p-1,
f_r(k),g_r(k),and nonempty integer intervals K_i. Put n=a+b+c=M-2.
For every proper original bin group J,delta_J=u_J-L(s_J)-3s_J>=0.
A is globally least,so

```text
delta_B>=ab, delta_C>=ac, delta_BC>=delta_A,
delta_A+delta_BC=a(b+c)+1-2p.                       (1)
```

The P=0 case is immediate:every remaining token is high and all
K_i contain only r_i. Hence assume P>=1 below.

**1. General form of a maximum-count deficit.** Suppose k_i=max K_i
sum to Q-D with D>=1. Put l_i=r_i-k_i. A bin is incrementable if
k_i<r_i;write J for those bins and j=|J|. Every other bin has l_i=0.
For i in J,k_i+1 is legal:there is a low token to replace and
k_i<Q since sum(k)<Q. As g increases and u_i<=g_i(k_i),maximality
therefore gives

```text
u_i <= f_i(k_i+1)-1.                              (2)
```

Let R=sum_(i in J)r_i and kappa=Q-sum_(i outside J)r_i.
Then R=P+kappa and sum_(J)k_i=kappa-D.
The cases j=0,1 are impossible by low counts alone:sum(l)=P+D,
but with at most one nonzero l it is at most P.
For j=2,the outside bin is high-only and its target is at most
the sum of its largest high values. Thus u_J is at least the
minimum R-subset sum of the whole pool. For j=3,u_J is the total.
In either case

```text
u_J >= alpha(R)=2R+p*kappa+L(P)+L(kappa).          (3)
```

If D>=j,choose integers h_i>=k_i+1 on J with sum(h)=kappa,
still in their legal ranges. The lower sum is <=kappa and the
sum of the upper capacities is >=kappa,so this is possible.
Their low counts sum P. Monotonicity of f and L(x)+L(y)<=L(x+y)
give

u_J <= sum_J f_i(h_i)-j <= alpha(R)-j,

contradicting(3). Thus only(j,D)=(2,1),(3,1),(3,2) remain.
For e=j-D,write Cross(z)=sum_(i<h in J)z_i*z_h. Direct expansion
of L gives the exact bound

```text
sum_J(f_i(k_i+1)-1)-alpha(R)
 = e*(kappa+2)+e^2-Cross(l-1)-Cross(k+1)-j.        (4)
```

For(2,1),the positive entries k_i+1 sum kappa+1,so their
product is >=kappa. Hence u_J<=alpha(R)+1.
For(3,2),their sum is Q+1 and their cross sum is >=2Q-1.
The right side of(4) is <=1-Q<0,since Q>=D=2:impossible.
For(3,1),put x_i=k_i,t_i=l_i-1. Then

```text
sum(x)=Q-1, sum(t)=P-2,
x_A+t_A=a-2, x_B+t_B=b-1, x_C+t_C=c-1,
0 <= sum_i(f_i(k_i+1)-1)-sum(pool)
  =4-Cross(x)-Cross(t).                            (5)
```

So all remaining three-bin failures have Cross(x)+Cross(t)<=4.
These deductions depend only on the count intervals and total;
we will reuse them after reflection with the translated hypotheses.

**2. Exclude the original maximum deficit.** First take(j,D)=(2,1).
If A belongs to J,its original group size is R+1. Its protected
lower bound exceeds alpha(R) by2P+3,contradicting the upper
alpha(R)+1. If J={B,C},put R=b+c. That upper bound yields

delta_BC<=R-2P+1.

Together with(1),delta_BC>=delta_A and p=P+2,this implies

(a-2)R+2P<=5,

impossible since a>=3,R>=6.

Now use(5). If x_B=0,then t_B=b-1>=2. Its upper low-only bound
u_B<=g_b(0) gives delta_B<=b(P-b-1)=b(t_A+t_C).
By(1),t_A+t_C>=a,so Cross(t)>=2a>=6,contrary to(5).
Likewise x_C cannot be0. Hence x_B,x_C>=1.

If x_A>=1,all three x entries are positive. Cross(x)<=4 forces
x=(1,1,1);any entry>=2 would give Cross(x)>=5.
Then t_B,t_C>=1,and Cross(t)<=1 forces t=(0,1,1).
Thus a=b=c=3,p=6. From(2),u_B<=18,so delta_B<=6<ab=9.

If x_A=0,put S=t_B+t_C,t_A=a-2. The low-only upper bound for A,
u_A<=g_(a-1)(0),together with u_A>=L(a)+3a gives

```text
(a-1)*S >= a+2.                                  (6)
```

For a>=4,this implies S>=2 and Cross(t)>=(a-2)S>=4;
Cross(x)>=x_B*x_C>=1 then contradicts(5).
For a=3,(6) gives S>=3. If x_B*x_C>=2,the same contradiction
follows. Otherwise x_B=x_C=1,so t_B,t_C>=1 and
Cross(t)=S+t_B*t_C>=4,again giving a total at least5.
This exhausts the maximum deficit and proves

```text
Q <= sum max(K_i).                                (7)
```

**3. Reflection,with the hypotheses translated explicitly.**
Reflect each remaining value v to M+2-v. The new pool is
[2,M] minus{p',p'+1},where p'=M+1-p. Its interval lengths
are P'=Q,Q'=P. Its targets are

```text
u'_A=(a-1)(M+2)-u_A,
u'_B=b(M+2)-u_B, u'_C=c(M+2)-u_C.
```

The reflected admissible intervals are exactly K'_i=r_i-K_i.
Consequently a failure sum min(K_i)>Q is exactly a maximum-count
deficit sum max(K'_i)<Q'. Section1 applies,including(4)/(5).
But section2 cannot be copied:its lower bounds change.
For an original proper group with remaining size R and no A,
the complementary protected cut gives

```text
u'_J >= L(R)+2R+2p-1+delta_(complement J).          (8)
```

If J includes A,its original size is R+1 and instead

```text
u'_J >= L(R)+3R-n+2p-3+delta_(complement J).        (9)
```

These follow by subtracting u_J from R(n+4) and using
sum(S)=L(n)+3n+1-2p. No symmetry of protection is assumed.

For a reflected two-bin deficit,R=P'+kappa>=P'. Subtracting
the reflected alpha(R)=L(R)+4R-2P' from(8) gives at least
2(n-R)+1>=7 if J excludes A. From(9),using p+P'=n+1,
the difference is at least n-R-1,the original size of the
outside nonroot bin,which is>=3. Both contradict alpha(R)+1.
The(3,2) and D>=j branches were already eliminated universally.

It remains to exclude reflected(3,1). Use its x,t as in(5),and
write X=sum(x),S=t_B+t_C when needed. Here original p=Q'+2=X+3.
If x_B=0,then t_B=b-1>=2. Its next-count bound(2) reads

u'_B<=L(b)+2b+t_A+t_C+3.

But(8) gives u'_B>=L(b)+2b+2X+5,so

t_A+t_C>=2X+2.

If X>=1,this forces Cross(t)>=2*4=8. If X=0,all t entries
are their full capacities a-2,b-1,c-1>=1,2,2 and Cross(t)>=8
anyway. Thus x_B>0,and similarly x_C>0.
If x_A>0,as before(5) forces x=(1,1,1),t=(0,1,1),a=b=c=3.
The next-count bound gives u'_B<=18,while(8) with X=3 gives
u'_B>=L(3)+6+11=20:impossible.

Finally x_A=0. Put T=a-2=t_A>=1,X=x_B+x_C>=2,S=t_B+t_C,
R=b+c=X+S+2. The next-count bound for A is

u'_A<=L(a)+a+S+2.

Returning to the ORIGINAL target gives

delta_A >= (a-1)R-S-6.

The comparison delta_BC>=delta_A in(1) also gives

delta_A <= aR/2+1/2-p=aR/2-X-5/2.

Combining these two bounds yields

```text
(T+2)X+(T-2)S+2T <=7.                             (10)
```

If T>=2,the left side is at least12. Therefore T=1,a=3,and
(10) becomes S>=3X-5. If X>=3,then
Cross(x)>=X-1 and Cross(t)>=S,so their sum is at least
4X-6>=6. Hence X=2,x_B=x_C=1. Since b,c>=3,we have t_B,t_C>=1.
Equation(5) now forces S=2,t_B=t_C=1. Thus a=b=c=3,
x=(0,1,1),t=(1,1,1),P'=5,Q'=3,p=5,M=11.

Here the excess in(5) is exactly0. Conservation forces equality
in every next-count bound,so the reflected targets are(10,20,20).
The original targets are(16,19,19),giving delta_A=4 but

delta_AB=16+19-L(6)-18=2.

A is not globally least,a contradiction. This last pattern is
precisely why it was unsafe to assume reflection preserved section2.
We have proved the other capacity inequality

```text
sum min(K_i) <= Q.                                (11)
```

**Conclusion and controls.** Equations(7),(11),nonemptiness from
MI383,and integer-interval interpolation give counts summing Q.
MI383's zero-count argument and G319 then complete a partition of
the actual low shape with0 in A. This is a COMPOSITE HAND CANDIDATE,
not independently verified;it inherits G319 and MI376's pending
status. No W318 dependency. Arbitrary holes,nonleast roots and
pair-minimum cases are outside its statement.

The two smallest algebraic endpoint traps have been evaluated
literally above:the original(16,18,18) candidate on p=6 violates
delta_B>=ab;the reflected trap returns(16,19,19) on p=5 and
violates delta_AB>=delta_A. These are hand checks,not a census.
The latter is also a sharp scope control:16/19/19 is protected and
A is least among the SINGLE bins,with slacks4,7,7,but its pair
slacks are2,2,5. In [0,11] minus{1,5,6},a whole partition is
{2,3,11}/{0,9,10}/{4,7,8}. Yet assigning0 to A forces high counts
at least(2,2,2),exceeding the five high values7..11. Thus the
GLOBAL least condition cannot be weakened to least among singles.
This is a literal protected positive control with a failed root;
it also identifies why the parent pair-minimum branch matters.
MI376's valid12/43/43 forced-zero example remains admitted by the
argument;MI383's14/26/12 negative count control fails protection.
The j=1 case uses legal low capacity,not an unjustified union of
independent high subsets. For j=2,only ONE outside bin supplies the
upper-bound argument in(3). D>=j uses legal integer capacities,
not a continuous relaxation. Empty original low interval was removed
before reflection. Original and remaining cardinalities stay distinct
in(8)/(9) and in both root comparisons. These are the niggle checks
that carry the proof;no computational sample replaces them.

Gut:there is a specific reason for renewed excitement:both count
obstructions have closed by short boundary inequalities,and the
reflected exceptional pattern revealed which hypothesis matters.
Reasoned:the protected LOW-SHAPE least-singleton branch now has a
complete conditional hand construction,awaiting independent reading.
This is not the full five-bin theorem. Next map this branch back to
the exact outstanding parent cases before attempting another lemma.
Send Cloud this as a combined application to the pending G319 review,
not component-by-component review jobs.13-minute heartbeat ACTIVE.


### MI385 — B197: parent scope,an exact lift,and the next owner-selection question (2026-10-18 11:28 BST)

**Scope audit and hand algebra,not a new proof filing.** G320 closes
one specified branch conditionally;it does not finish P_0 or five bins.
Record searched:pair.minimum with protected returned3 hits/2 files,
including MI384's sharp control. Read MI362,MI368,MI372,MI374 and
FOUR-BIN-PARTITIONS section6 as the actual parent reduction. No
experiment or novelty claim. Cloud's flags were unchanged at entry;
G319/G320/W318 remain pending. Do not create a component review queue.

The parent chain is:

- Full interval FIVE bins,all sizes>=3:SS cut conditions. A globally
  closest singleton or its complement can be oriented by reflecting
  the ORIGINAL full interval. Its canonical removal gives the
  protected one-hole FOUR-bin problem P_0 of MI362. The original
  strict pair/triple-facet branch is separate.
- P_0 has all proper group targets u_J>=L(r_J)+r_J. If a singleton
  is globally least for that adjusted slack,MI368 permits removing
  any realization while preserving an appropriate residual margin.
  A legal pivot leaves at most two holes;a missing-pivot repair
  gives one of the low/high three-hole shapes. Other minimizing
  cuts in P_0 are not handled by calling them singletons.
- In the low shape [0,M] minus{1,p,p+1},G320 applies when all
  cuts have margin3 AND some singleton is globally least for
  delta_J=u_J-L(r_J)-3r_J. It then completes that three-bin pool,
  conditional on G319/MI383/MI376. A stronger inherited margin
  still implies margin3,but need not preserve which cut minimizes
  the adjusted slack. The high shape and legal-pivot shape are
  not silently included in G320.

Reflection is not a missing shortcut. For any three-hole pool
S=[0,M] minus H,write n=M-2,w=sum(H). From original protected
cuts u_J>=L(r)+3r and total conservation,the reflected targets
satisfy u'_J>=L(r)+w-3. For high shape H={p,p+1,M-1},this is
L(r)+M+2p-3,not L(r)+3r. Likewise P_0 reflects to L(r)+q,
as already recorded in MI362. Geometry alone does not transport
G320's hypotheses or the selected minimum.

**The low-shape pair branch is genuinely inside the parent problem.**
In fact EVERY protected low-shape three-bin instance with p>=3
has the following explicit lift. This rules out dismissing its
pair-minimum cases as artifacts of an unnecessarily broad domain.
It does not say that these cases cannot be avoided by a different
construction;it says the canonical parent route can actually reach them.

Let S=[0,M] minus{1,p,p+1},n=M-2=a+b+c,a,b,c>=3,
3<=p<=M-2=n. Let v_i total sum(S)=L(n)+3n+1-2p and obey
v_J>=L(r_J)+3r_J for every proper group. No global singleton
minimum is assumed. Form the one-hole parent

```text
P=[0,n+p] minus{2p-1},
new bin D: size p, target L(p)+p,
old bins: sizes a,b,c,targets v_i+(p-2)r_i.
```

Choose D={0,...,p-3} union{p-1,2p-2}. It has p values and
sum L(p)+p. Removing it leaves minimum p-2,and translating
by-(p-2) gives exactly S:the three holes become1,p,p+1.
This is precisely the low missing-pivot repair,with prefix
length p-1,suffix length0 and missing pivot2p-1.

All P_0 cuts can be checked symbolically. D's margin1 adjusted
slack is0. For any proper nonempty old-bin group J,write its
original margin3 slack as delta_J. Then the parent's slacks are

```text
J alone: delta_J+p*r_J >=0;
D union J: delta_J >=0.
```

For the group of ALL old bins,the parent's slack is
p(n-2)+1>0. These are all14 proper cuts,so P satisfies P_0
and D is globally least,with ties allowed. Its target total is
L(n+p+1)-(2p-1),the actual sum of P.

It also lifts to a FULL five-bin interval through MI362's exact
gate. Use first-bin prefix length l=2p-1,suffix length k=0,
hole q=2p-1,and parent cardinality m=n+p. The removed first
bin E has size2p and actual set

```text
E={0,...,2p-2} union{4p-2}.
```

The full interval is[0,N-1],N=n+3p. Its bin sizes and targets are

```text
sizes:   (2p, p, a, b, c),
targets: (L(2p)+2p-1, L(p)+2p^2,
          v_A+3(p-1)a, v_B+3(p-1)b, v_C+3(p-1)c).
```

All values of E are legal because p<=n. The gate holds:
m(l+1)=2p(n+p)>=2(2p-1),and for every proper parent group
of size r>=3,the extra lower term q-l*r=(2p-1)(1-r)<=0.
Thus its required max(r,q-l*r) is just r,already supplied by
P_0. E is globally least lower slack h=2p-1,and its deletion,
translation and the displayed D repair produce the original S.
No joint target partition is assumed in this lift. This uses
MI362's exact algebraic gate,not the conjectured five-bin theorem.
The p=2 endpoint has an empty low interval after removing0 and
is already a separate full-interval branch;the lift above does
not silently introduce a forbidden size2 parent bin.

**Literal independent hand control.** Take MI384's p=5,M=11,
n=9,three sizes3,targets(16,19,19). The construction gives full
[0,23],sizes(10,5,3,3,3),targets(54,60,52,55,55),with partition

```text
{0,1,2,3,4,5,6,7,8,18} /
{9,10,11,13,17} /
{14,15,23} / {12,21,22} / {16,19,20}.
```

The first two sets implement the two specified removals;subtract12
from the remaining values to recover S and its positive partition
{2,3,11}/{0,9,10}/{4,7,8}. At that stage the single adjusted
slacks are4,7,7 and the pair slacks2,2,5. There is NO globally
least singleton to which G320 applies. Forcing0 into its smallest-
singleton-slack bin is impossible,as MI384's count control shows.
This is an actual full five-bin lift of that precise scope boundary.
It is not a counterexample to existence.

A different automatic root choice also fails:the complement of a
minimum pair need not contain0. On[0,15] minus{1,3,4},sizes
(5,5,3),targets(37,38,37),single adjusted slacks are12,13,25
and pair slacks AB,AC,BC are0,22,23. The minimum pair is AB,
but its complementary size3 bin C cannot contain0:even its two
largest available nonzero values sum29<37. A full partition is
{0,5,7,11,14}/{2,6,8,9,13}/{10,12,15}. Thus neither fixed
choice justified merely by the name of the minimizing cut is valid.
These literal controls are not a new experiment or review request.

**Next precise question.** For each candidate zero-owner j,define
remaining sizes r_i=s_i-1_(i=j) and its scalar admissible count
intervals K_i^(j) using MI383's f/g. Does every protected low-shape
instance have SOME j with nonempty intervals and feasible aggregate
count,whose fixed-count realization avoids the exceptional one-bin-
whole-interval-plus-singleton failure? G320 solves this when a global
least singleton exists. The strict-pair case requires adaptive owner
selection;the controls above show which two shortcuts to avoid.
Do not assume a positive count row,or infer joint completion from
scalar admission without MI383's exceptional-shape check. A bounded
hand owner-budget argument is the next cheap test;no larger census
is scheduled by this entry.

Step-back:the scope audit tempers the apparent breadth of the last
result but strengthens the relevance of the next target. The pull is
now toward choosing between three concrete owner intervals,not toward
preserving a favourite root. Fresh choice would retain this question:
it uses the new mechanism and has explicit positive traps to test it.
If that becomes another case catalogue without an owner invariant,
change representation or ask Cloud for perspective. G320 remains a
real completed branch candidate,not evidence that the parent theorem
is nearly finished. No status upgrade or new PROOFS entry here.
13-minute heartbeat ACTIVE;next adaptive zero-owner hand question.


### MI386 — B198: adaptive zero-owner diagnostic preregistration (2026-10-18 11:40 BST)

Question:does allowing all three zero owners remove the strict-pair
obstruction of MI385? The pull is toward a selection invariant;unease
is that scalar count admission may conceal the zero-count exception.
This block tests those layers separately,without importing G320 outside
its scope or treating pending G319 as independently verified.

Record searched: `zero.owner` AND `protected` -> two notebook hits,
current state and MI385. MI383-385 and the existing B193 instrument
were read. Prior-art orientation remains the scoped partition-polytope
source in MI378;this is a diagnostic of our specific reduction,not a
new literature theorem or a novelty claim.

Prediction:for every protected low-shape instance in the fixed domain,
at least one zero owner has nonempty scalar K intervals with aggregate
capacity. I further predict an admitted count vector outside MI383's
possible zero-count exceptional pattern can be selected. These are
separate predictions. Counterfactual:retain the first failure,including
all three K systems,and use a literal partition search only to decide
whether the failure belongs to the reduction or to actual existence.
No cap expansion or automatic larger census follows.

Fixed domain:M=11..16,p=2..M-2,sorted sizes a<=b<=c,each>=3,
a+b+c=M-2;all integer targets satisfying all six margin3 proper cuts
and total conservation. Test every zero owner,not a favourite cut.
For each admitted count triple,mark the potentially exceptional shape:
one interval wholly belongs to H,and H has exactly one element in the
other interval,whose other two counts are>=2. Nonexceptional admission
is only a conditional completion certificate via G319/MI383.

Independent controls:literal disjoint-subset full partition maps for
all M=11..13 domains,recording the owner of0,compared with the scalar
admission and nonexceptional certificates. Exact subset enumeration
checks f/g endpoints separately on these pools. Retain per-owner
false positives rather than declaring scalar and actual maps equal.
Known positive controls are MI385's16/19/19 and37/38/37 partitions;
known negative fixed-root control is16/19/19 with0 forced into A.
Unexpected check:permuting labels in the unequal-size37/38/37 control
must permute the owner-admission set exactly. This tests hidden reliance
on sorted labels;reflection is deliberately NOT used as invariant
protection. Stop on the first all-owner scalar failure,first target
with only exceptional count choices,or failed control;otherwise finish
the fixed domain. CPU cap20 seconds;partial output is not a pass.
Raw data remain outside git. No existing diagnostic is rerun.


### MI387 — B198: adaptive owner survives;scalar ownership alone does not (2026-10-18 11:41 BST)

**COMPUTED,finite domain only.** The MI386 instrument at17ee4d7b ran
once and finished in1.383557 CPU seconds under its20-second cap.
All183 size/pool domains were completed,with63,589 protected targets,
including41,726 with strict pair minimum. Every target had an admitted
zero owner AND a count vector outside MI383's possible zero-count
exception. The number of scalar-admitted owners was1/2/3 on respectively
5,037/17,511/41,041 targets. This does not prove any universal selector.

Independent literal disjoint-subset maps covered37 domains at M11..13
and all4,785 protected targets therein. Every target had a partition.
Every actual zero owner was scalar-admitted;there were12 scalar-admitted
owner/target false positives,but ZERO nonexceptional-owner false positives.
Literal fixed-count extrema independently matched f/g. Both specified
positive partitions,their forced-root negative controls,and every label
permutation of the controls passed. The remaining M14..16 targets have
count certificates only;their interpretation as partitions still uses
the unreviewed G319/MI383 mechanism. These computations are same-worker
checks,not an independent carrying read of G319 or G320.

**First scalar-owner false positive,explained by hand.** On
S=[0,11] minus{1,4,5},sizes(3,3,3),targets(14,20,22),the
proper lower bounds are12 for singles and33 for pairs,all satisfied.
Scalar owners are A and B;only A is an actual owner. If0 belongs to B,
its other two values must be9 and11 (the only distinct available pair
summing20). The six remaining values are{2,3,6,7,8,10}. Their least
triples begin2+3+6=11,2+3+7=12,2+3+8=13,then15;there is no
triple sum14. More explicitly,any triple not containing both2 and3
is at least2+6+7=15,and the required third value with2,3 would be9.
So this owner is impossible without any theorem dependency.

Its scalar data expose the exact failure:for owner B the remaining
sizes are(3,2,3),K_A={1},K_B={2},K_C={2,3}. Since Q=6,
only high counts(1,2,3) work;low counts are(2,0,0). A owns the
entire low interval{2,3} plus one high value,precisely the exceptional
pattern. Moving0 to A gives a literal positive partition

```text
A={0,6,8}, B={2,7,11}, C={3,9,10}.
```

Now high counts are(2,2,2) and low counts(0,1,1);the exception
is absent. This is a protected strict-pair instance:single adjusted
slacks are2,8,10,and pair slacks are1,3,9. No global least singleton
exists,so G320 does not already cover it. The example explains why the
successful finite all-owner claim is stronger than simply repairing
the fixed least-singleton argument.

**A cleaner next representation,algebra only.** Avoid three separate
case trees by making the zero owner a variable z_i in{0,1},sum z_i=1.
Let k_i count high values,and q_i=s_i-k_i count low values INCLUDING0
when z_i=1. Then sum k_i=Q,sum q_i=P+1,with
0<=q_i-z_i<=P and0<=k_i<=Q. Define the auxiliary polynomials

```text
F_i=2s_i+p*k_i+L(q_i)+L(k_i),
G_i=(p-1)q_i-L(q_i)+M*k_i-L(k_i).
```

The exact individual scalar range is

```text
F_i-z_i(q_i+1) <= u_i <= G_i-z_i(p-q_i).
```

This follows by replacing q_i by q_i-1 in the low-row endpoint
formula when0 is owned. F/G are auxiliary polynomials even if q_i>P;
the legal condition is on q_i-z_i,so no nonexistent unrooted subset
is silently assumed. Thus the next hand target is joint integer
selection of z and k under the six protected cuts,followed by avoidance
or repair of the explicit exceptional pattern. This identity does NOT
assert the target follows from those cuts. It introduces no new proof
entry or review job.

**Niggle sweep and verdict.** Sorted sizes do not lose target order:
all ordered target triples were tested,and label permutations were an
explicit unequal-size control. All six cuts are enforced by singleton
lower bounds and complementary upper bounds. The literal checker does
not call the scalar functions or G319 to generate its maps. The actual
owner false positives were retained,not suppressed by the successful
existence test. p=2's empty low row is included. Finite success does not
establish asymptotic selection or settle any parent theorem.

Gut verdict:the attraction is to one small resource-allocation question,
now with a concrete warning about the boundary;it is not renewed merely
by a large pass count. Reasoned verdict:the test supports spending the
next bounded hand block on the z/k selector,but not increasing the census.
Fresh choice would retain this exact question because the obstruction
and one successful change of owner are explicit. Full low-shape,
five-bin/P_0/E28/L8 remain OPEN.13-minute heartbeat ACTIVE.

Raw summary SHA256: `74cc20950936d790fb6481ab1134a06825eeb2aed37db104dd4091596a9cf700`.
Instrument: `tests/probes/instinct/adaptive_zero_owner.py` at17ee4d7b.
Raw summary is outside git;no large dataset or theorem certificate is claimed.


### MI388 — B199: isolate compatibility from adaptive count selection (2026-10-18 11:48 BST)

Question:can the possible zero-count exception in MI383 always be
repaired after choosing a different owner or count vector,using the
protected cuts but WITHOUT a globally least singleton? This is the
compatibility part of MI387's joint z/k question. A positive answer
would leave only existence of some scalar-admitted owner to prove.

Record searched:zero.owner AND count ->11 hits in the map/notebook;
MI378's regular-row splitting,MI383's fixed-count classification and
MI387's explicit false owner were reread. No new external theorem or
novelty claim. Fresh shared main and portal flags are unchanged.
Pull:the false owner has a very localized collision. Unease:an apparent
repair must preserve all three targets,not just move0 to a feasible
single bin. Hand budget:one bounded repair/classification block;no
experiment or census. Countercheck:any proposed count change must
pass BOTH extrema for each affected bin and must not recreate the
same exceptional row shape. Unexpected check:the small p=5 boundary,
where a generic move can land on another thin row,gets an explicit
partition rather than an appeal to positivity.

### MI389 — B199: any admitted owner suffices after repair (2026-10-18 11:54 BST)

**Conditional hand PROOF-SKETCH,not independently reviewed.** Let
S=[0,M] minus{1,p,p+1},2<=p<=M-2,three sizes>=3,total target
sum(S),and all six proper cuts u_J>=L(s_J)+3s_J. Suppose SOME
owner of0 and some counts in I=[2,p-1],J=[p+2,M] satisfy the
individual combined f/g bounds and both count totals. Then S has
a partition with the prescribed original sizes/targets,conditional
on G319 and MI383 section1's generic fixed-count completion.
The final partition need not retain that owner or those counts.
No least-slack hypothesis is used here. Existence of an admitted
owner is NOT proved;the full low-shape statement remains OPEN.

MI383 section1,which does not use least slack,leaves only this
possible fixed-count failure:one bin H owns a WHOLE interval and
one value of the other interval. The other two counts in that other
interval are>=2. Their exact one-hole spectrum can fail only at
one bin's actual minimum+1,with the omitted value at that bin's count;
the upper omission is the other bin's lower omission. Scalar rank
bounds for the other bin and total ensure the actual one-hole extrema,
not merely those of the undeleted interval. All other row shapes
already complete via G319/MI383. Empty I is a single regular row.

**1. A whole high interval cannot cause failure.** If H owns all
of J and one low value,a failed low-only bin of original size s has
target L(s)+2s+1 if nonroot,or L(s)+s if it owns0. Each is strictly
below L(s)+3s for s>=3. This contradicts protection. No minimum-
slack comparison or reflection of the protected pool is needed.

**2. Whole low interval:the pair cuts decide where0 must be.** Put
P=p-2,Q=M-p-1 and D0=sum(I)=L(p)-1. Let H own all of I and
one high value p+2+y. Name the failed high-only bin D,whose remaining
high count is d,and the third bin E,whose high count is e. Then

```text
Q=1+d+e, d,e>=2,
y=d,
u_H=L(p)+p+1+d,
u_D=d(p+2)+L(d)+1.
```

The y=d identity and the displayed D target are the exact lower
one-hole omission,not an arbitrary scalar-admitted triple. There is
only one root,so d,e cannot both be2. If0 belongs to H or D,then
the ORIGINAL size of H union D is p+d,regardless of which is root.
But direct subtraction gives

```text
u_H+u_D - L(p+d)-3(p+d) = 2-2p < 0.
```

Thus that pair cut is violated. Every actual exceptional failure
under protection has0 in E;H and D are nonroot. Consequently

```text
s_H=p-1>=3, p>=4; s_D=d>=3; s_E=e+1>=3;
delta_H=u_H-L(p-1)-3(p-1)=d-p+3>=0.
```

In particular p<=d+3. This is the missing scope distinction in the
old fixed-root proof:least-slack inequalities are unnecessary once
we allow the owner to change. We have not inferred that an individual
false owner becomes feasible without changing it.

**3. For d>=4,keep0 in E and change two counts.** Give H two high
values instead of one,and one fewer low value;give D one low value
and one fewer high value. The new rows,ordered H,D,E,are

```text
low:  (P-1,1,0),
high: (2,d-1,e).
```

They are legal,and targets/sizes remain the original prescribed ones.
The high row has all counts>=2;the low row has at most two positive
counts. Hence both are regular in MI378's sense. To prove combined
scalar admission,compute the new extrema relative to the old target:

```text
H: f_new-u_H = 4-d <=0,
   g_new-u_H = 2M-p-d-5 >0;
D: f_new-u_D = -p-d <0,
   g_new-u_D = (d-1)(e+1)-4 >=5.
```

E is unchanged. Positivity of H's upper difference follows from
M=p+Q+1=p+d+e+2. All formulas use actual offsets2 and p+2.
MI378's integer row-sum splitting plus the reviewed regular-row
three-bin theorem now gives a partition. In particular,this repair
itself does not require G319's thin-positive-row extension.

**4. For d=3,change the root and construct explicitly.** Protection
and s_H>=3 leave only p=4,5,6. Now Q=e+4>=6. Give0 to H.
Give low value p-1 to D,low value p-2 to E,and every other low
value to H. H takes two high values,D takes two,and E takes the
remaining e high values. Specify the high values by their normalized
indices j,meaning actual value p+2+j:

| p | H high indices | D high indices |
|---|---|---|
| 4 | {0,2} | {3,4} |
| 5 | {0,3} | {2,5} |
| 6 | {0,4} | {2,5} |

All indices are distinct and at most5,so they exist for every e>=2.
H's high-index sum is p-2;D's is7. Its low remainder sums to
D0-(2p-3). Thus

```text
H total = D0-(2p-3)+2(p+2)+(p-2) = D0+p+5 = u_H;
D total = (p-1)+2(p+2)+7 = 3p+10 = u_D.
```

H has0,p-4 low values and two high values,so size p-1;D has
size3;E has one low value and e high values,so original size e+1.
Every value is assigned once,and E's target follows by conservation.
This explicitly resolves the thin boundary with no spectrum inference.

**Protected literal controls,hand checked.** In the order H,D,E:

```text
p4,e2: S=[0,11] minus{1,4,5}, sizes(3,3,3), sums(14,22,20)
       {0,6,8} / {3,9,10} / {2,7,11}.
p5,e3: S=[0,13] minus{1,5,6}, sizes(4,3,4), sums(19,25,35)
       {0,2,7,10} / {4,9,12} / {3,8,11,13}.
p6,e3: S=[0,14] minus{1,6,7}, sizes(5,3,4), sums(25,28,38)
       {0,2,3,8,12} / {5,10,13} / {4,9,11,14}.
```

All single and pair bounds hold. The first is MI387's false-owner
control relabelled. In each case the former root E is at its high
maximum-minus1,and the construction moves0 to H. Although e=2
suffices for the formula's legality,p5/e2 and p6/e2 fail a protected
pair cut;they are not claimed as protected controls. This distinguishes
construction scope from target admission. For the d>=4 branch,a
protected endpoint control is p4,d4,e2 on[0,12] minus{1,4,5},
sizes(H,D,E)=(3,4,3),targets(15,31,22). The new regular counts
are low(1,1,0),high(2,3,2);a literal partition is
{2,6,7}/{3,8,9,11}/{0,10,12}. Both extrema inequalities hold.
These are hand controls,not a new experiment.

**Conclusion and remaining inference.** Conditional on the existing
generic completion statement,ANY scalar-admitted owner yields SOME
partition,after the repairs above when needed. Therefore the protected
low-shape existence question reduces exactly to finding an owner j
with all K_i^(j) nonempty and
sum min K_i^(j)<=Q<=sum max K_i^(j). Necessity is immediate from
any actual partition;the conditional sufficiency is this argument.
There is no longer a separate need to choose a nonexceptional count
vector in the initial selector. The old scalar false-owner controls
remain valid:the conclusion allows a different owner.

Niggle sweep:actual one-hole extrema versus full-row extrema;root in
H/D/E exhausted;d=2 excluded only AFTER locating the root in E;
p2 empty row and p3 small size accounted for;both f/g endpoints for
the large repair;three small p values and all distinct indices;
conservation does not substitute for the two explicitly checked targets;
no unproved reflection invariance;no use of W318 or G320. The regular
row splitting is MI378's algebra,with MI295 as its reviewed existence
input. Overall status remains conditional/unreviewed pending G319 and
independent reading of this application. No new census or novelty claim.

Gut verdict:the useful surprise was the pair cut 2-2p,which deletes
most of the apparent case tree. Reasoned verdict:compatibility is now
separated from count selection by a short repair,so the next hand
question is genuinely narrower. Fresh choice still favours the z/k
selector;this result does not imply it is easy or nearly proved.
Full low-shape/five-bin/P_0/E28/L8 OPEN;13-minute heartbeat ACTIVE.


### MI390 — B200: owner eligibility before the shared count budget (2026-10-18 12:01 BST)

Question:before proving sum min K<=Q<=sum max K,can we guarantee
an owner whose three individual K intervals are nonempty? Empty
intervals must not be hidden by manipulating their endpoints. Hand
block only;no experiment or cap expansion. Record searched:count,
capacity,owner ->20 hits across four files;current MI378/383/384/387/
389 formulas are the relevant source,not the earlier path-forest work.
Shared main/Cloud flags unchanged. No new external theorem assumed.

Pull:the owner changes only one cardinality,so scalar subset extrema
may separate forced ownership from the aggregate obstruction. Concern:
actual subset sums need not fill every interval between their extrema.
The kill check is to derive every possible gap in the union of the
fixed-count f/g intervals,including rooted original size3. Unexpected
hand control will include p2's empty low interval and a forced owner.
A result about individual eligibility will not be labelled aggregate
capacity or partition existence.

### MI391 — B200: an individually admissible owner always exists (2026-10-18 12:07 BST)

**Hand PROOF-SKETCH,not independently reviewed.** For the protected
low shape S=[0,M] minus{1,p,p+1},sizes s_1,s_2,s_3>=3,total
T=sum(S),and all proper cuts u_J>=L(s_J)+3s_J,there is a choice
of owner of0 for which every scalar count interval K_i is nonempty.
No least-slack hypothesis or G319/G320/W318 is used. This proves
individual eligibility only;the aggregate bounds remain open.

Write n=M-2=sum s_i>=9,m=n-1=|V|,V=S minus{0},P=p-2,
Q=M-p-1. For 0<=r<=m,let alpha_r and beta_r be the sums of
the r smallest and largest values of V. A nonroot bin has size r=s;
a root bin has remaining nonzero size r=s-1. For a fixed legal high
count k and low count l=r-k,its possible sums form the full interval
[f_r(k),g_r(k)],because independent subset sums of each full interval
are complete. K is nonempty exactly when the target belongs to the
union of these fixed-count intervals.

**1. Locate the gaps in that union directly.** Both endpoints grow
strictly with k. For a legal transition k to k+1,put l=r-k. Then

```text
f_r(k+1)-g_r(k)
 =3-(l-1)(P-l)-k(Q-k-1).                         (1)
```

For r>=3 and m-r>=3,set A=l-1,B=P-l,C=k,D=Q-k-1.
All are nonnegative,A+C=r-1>=2,B+D=m-r-1>=2. A gap requires
AB+CD<=1. If A,C are both positive,AB+CD>=B+D>=2,impossible.
If C=0,then A>=2 forces B=0;this is r=P,k=0. If A=0,then
C>=2 forces D=0;this is r=Q,k=Q-1. Hence the ONLY possible
omissions are alpha_r+1,+2 when r=P,or beta_r-1,-2 when r=Q.
These are genuine endpoint gaps when the transitions exist. Empty
rows have no such transition and need no exception.

For rooted r=2,the only transitions are k0->1 and k1->2. Formula
(1) is respectively5-P and5-Q. Lower gaps occur only at P2 or P3:
P2 gives missing sums6,7;P3 gives missing sum8. Upper gaps occur
only at Q2 or Q3:respectively beta_2-1,-2 or beta_2-3. This lists
all possibilities,including the distance3 gap that the r>=3 lemma
would miss. When a transition is illegal it creates no gap.

**2. Exact nonroot eligibility under protection.** For a bin of
original size s>=3,the complement t=n-s>=6. Its actual largest
s-sum beta_s has complement minimum in S equal to alpha_(t-1),
since that minimum includes0. Every j-th smallest positive value of
V is at most j+4 (j starts at0),so

```text
alpha_(t-1)<=L(t-1)+4(t-1)=L(t)+3t-3.
```

The complementary protected cut gives u<=beta_s-3. Thus neither
upper gap from section1 can occur. A lower gap requires s=P,when
alpha_s=L(s)+2s. Protection u>=L(s)+3s places u at least s>=3
above that minimum. Therefore

```text
K(nonroot,s,u) is nonempty iff u>=alpha_s.          (2)
```

The upper condition and absence of gaps were proved,not assumed.

**3. Exact root eligibility under protection.** For r=s-1,
alpha_r<=L(s-1)+4(s-1)=L(s)+3s-3. Protection keeps u at least3
above alpha_r. For r>=3 this excludes every lower gap. The only
upper gaps require r=Q;then the other ORIGINAL bins have combined
size t=m-r=P>=6. If u=beta_r-1 or beta_r-2,their total would be
alpha_t+1 or alpha_t+2=L(t)+2t+1 or+2,below their protected bound
L(t)+3t. So these gaps are also excluded.

For s=3,r=2,the lower omissions6,7,8 are below u>=12. If Q2,
the complementary size is t=P>=6,and the same argument excludes
upper distances1,2. If Q3,then t=P+1>=6 and the t smallest positive
values have sum alpha_t=L(t)+2t+2. The upper distance3 omission
would give the other bins total alpha_t+3=L(t)+2t+5<L(t)+3t.
Thus it too is excluded. Consequently,for every original s>=3,

```text
K(root,s,u) is nonempty iff u<=beta_(s-1).          (3)
```

This is a scalar feasibility statement;it does not assert a compatible
partition after choosing0's owner.

**4. At most one bin requires0,and that bin can own it.** A bin
that is ineligible as nonroot has u<alpha_s<=L(s)+4s. If two bins
of sizes a,b were ineligible,their integer targets would satisfy

```text
u_A+u_B <= L(a)+L(b)+4(a+b)-2
          < L(a+b)+3(a+b),
```

because a+b-ab-2<0 for a,b>=3. This violates their protected pair
cut. There is at most one such bin.

For any size s with t=n-s>=6,the j-th largest positive value is at
least M-2-j. Hence

```text
beta_(s-1)-alpha_s
 >= (s-1)(n+1)-2L(s)-4s
  = (s-1)(t+1)-4s
 >= 3s-7 >=2.                                    (4)
```

If a bin requires0,its target u<alpha_s is therefore below
beta_(s-1),so it is eligible as root by(3). Every other bin is
eligible as nonroot by(2). This handles the forced-owner case.

**5. When no bin requires0,at least one root is eligible.** Put
r_i=s_i-1>=2,so sum r_i=m-2. The sequence beta_r is concave:
its successive increments are the positive values in decreasing
order. Transferring a unit from a smaller r>=3 to a largest r cannot
increase the sum of beta values. Repeating gives

```text
sum_i beta_(r_i) >= beta_(m-6)+2 beta_2
                  = T-alpha_6+2 beta_2.           (5)
```

All indices are legal because m>=8. If p<=M-3,the two largest
values are M,M-1,so2 beta_2=4M-2>=42,while alpha_6<=39.
If p=M-2,they are M,M-3,so2 beta_2=4M-6>=38;the six smallest
values are2..7 because M>=11,so alpha_6=27. In either case(5)
is at least T+3. All three targets cannot exceed their respective
beta_(s_i-1),since their sum is T. At least one bin is root-eligible;
by assumption the other two are nonroot-eligible. This completes the
individual-owner assertion.

**Hand controls and limits.** For p2,M11,sizes3^3,targets12,24,24,
all six protected cuts hold. V=[4,11],alpha_3=15,beta_2=21:
only A can own0 and A must own0. A literal partition is
{0,4,8}/{5,9,10}/{6,7,11}. The empty low interval is therefore
included in the argument,not discarded. Here sum beta_2=63=T+3,
showing the lower margin used in(5) is attained.

On MI385's p3,M15,sizes(5,5,3),targets37,38,37,the size3 bin
cannot own0 since beta_2=29. The theorem does not say every owner
is eligible. On p5,M11,sizes3^3,targets16,19,19,the original
least-singleton owner A has all K intervals nonempty but each has
minimum2,whose sum6 exceeds Q5. Thus the existence assertion just
proved does not imply aggregate capacity for its chosen owner.
This is the exact remaining obstacle,not evidence against the result.

Niggle sweep:each fixed-count sum interval is actual;only LEGAL
count transitions create gaps;rooted size3's distance3 gap is treated
separately;complementary sizes are original sizes when protection is
used;two ineligible nonroots use integer strictness;the large-bin
extremal distribution in(5) retains sizes>=2;the p=M-2 endpoint has
only one high value and its two largest values are handled separately.
No numerical run,no G319/G320/W318 dependence,no novelty assertion.
The earlier partition-polytope abstract supplies no theorem here.

Gut verdict:there is a real simplification in excluding empty K
systems before reasoning about their endpoints. Reasoned verdict:
the remaining assertion is now precisely that SOME individually
eligible owner also meets both aggregate bounds. MI389 then supplies
conditional compatibility. Next hand test:compare aggregate count
intervals across eligible owners,using the16/19/19 control to reject
any claim that every eligible owner works. Full low-shape and all
parent problems remain OPEN;13-minute heartbeat ACTIVE.


### MI392 — B201: separate the two owner-capacity failures (2026-10-18 12:20 BST)

**Question and approach,recorded with this hand block.** Can changing
zero owner repair a shortage or excess of high counts? Record searched:
record_find aggregate owner ->15 hits in6 files;read MI384 and MI391
in full,MI389's current application,and the current shared ledgers.
The primary partition-polytope source remains abstract-read only;
no external theorem or novelty assertion is imported. No experiment.
Initial pull:the endpoint deficit algebra already compresses failures
into a tiny cross-product budget. Unease:MI384 used a global least
comparison exactly where the unrestricted problem is still open.
Keep16/19/19 as the negative control for any every-owner assertion.
The useful outcome below removes that comparison on ONE side by
classifying the exceptions,not by pretending the comparison survives.

### MI393 — B201: all excessive-minimum-count owners,with two repairs (2026-10-18 12:20 BST)

**Hand PROOF-SKETCH.** Let S=[0,M] minus{1,p,p+1},sizes a,b,c>=3,
n=a+b+c=M-2,and all six proper protected cuts
u_J>=L(s_J)+3s_J. Fix A as zero owner and assume its three scalar
count intervals K_i are nonempty,with remaining sizes r=(a-1,b,c).
Then sum min(K_i)>Q occurs only in the following two configurations,
up to exchanging B,C:

```text
(a,b,c)   (u_A,u_B,u_C)   p   M
(3,3,3)   (16,19,19)      5   11
(4,3,3)   (29,22,13)      6   12
```

Both configurations really fail this rooted inequality,and both
have literal partitions after changing zero owner. No global least
slack assumption,G319,W318,or numerical census is used in this proof.

**1. Reflection and the deficit reduction.** Write P=p-2,
Q=M-p-1. P=0 makes every K_i={r_i},so cannot fail. Otherwise reflect
every positive value by v -> M+2-v. Use stars for the reflected pool:
P*=Q,Q*=P,p*=M+1-p,and targets
u*_A=(a-1)(M+2)-u_A,u*_B=b(M+2)-u_B,u*_C=c(M+2)-u_C.
The count intervals become K*_i=r_i-K_i. The asserted failure is
therefore a maximum-count deficit in this reflected system.

Here is MI384's elementary deficit reduction,with its scope explicit.
For k_i=max K*_i,l_i=r_i-k_i,sum k=Q*-D,D>=1,let J be the bins
with l_i>0,j=|J|. Each next count k_i+1 is legal and
u*_i<=f*_i(k_i+1)-1. Bins outside J are high-only. Put
R=sum_J r_i=P*+kappa,where kappa=Q*-sum_(outside J)r_i.
The total or the single outside-bin upper bound gives
u*_J>=alpha*(R)=L(R)+4R-2P*. If D>=j,raising each k_i by at
least1 to counts summing kappa contradicts this by summing minima;
the legal capacities allow this allocation. j<=1 is impossible
since sum l=P*+D but one bin has l<=P*. Thus only (j,D)=(2,1),
(3,1),(3,2) remain. Expansion of the quadratic minima gives

```text
sum_J(f*_i(k_i+1)-1)-alpha*(R)
 = e(kappa+2)+e^2-Cross(l-1)-Cross(k+1)-j,
e=j-D, Cross(v)=sum_(i<h) v_i v_h.
```

For j2,D1,the right side is at most1. For j3,D2 it is at most
1-Q*<0,impossible. For j3,D1 put x_i=k_i,t_i=l_i-1. Then

```text
sum x=Q*-1=X,  sum t=P*-2,
x_A+t_A=a-2, x_B+t_B=b-1, x_C+t_C=c-1,
0 <= sum_i(f*_i(k_i+1)-1)-sum(reflected pool)
   =4-Cross(x)-Cross(t).                          (1)
```

All x,t are nonnegative integers. Notice original p=X+3.

For completeness,the reflected protected bounds are NOT the original
bounds copied by symmetry. Subtracting original complementary cuts
from the fixed total gives,for a proper group of remaining size R,

```text
u*_J >= L(R)+2R+2p-1+delta_complement   if A not in J,
u*_J >= L(R)+3R-n+2p-3+delta_complement if A in J,
```

where delta_complement>=0 is its ORIGINAL protected margin.
For the two-bin deficit these exceed alpha*(R) by at least
2(n-R)+1>=7 if A is outside J,and n-R-1>=3 otherwise
(use p+P*=n+1). This rules out j2,D1. Only(1) remains.

**2. Both nonroot x entries are positive.** If x_B=0,then
t_B=b-1>=2 and its next-count upper bound is
u*_B<=L(b)+2b+t_A+t_C+3. Its reflected protected lower bound
is L(b)+2b+2X+5,so t_A+t_C>=2X+2. If X>=1,this implies
Cross(t)>=8. If X=0,then t=(a-2,b-1,c-1) has entries at least
(1,2,2),again Cross(t)>=8. Both contradict(1). Likewise x_C>0.

If also x_A>0,Cross(x)<=4 forces x=(1,1,1). Then t_B,t_C>=1
and Cross(t)<=1 force t=(0,1,1),a=b=c=3,p*=6. The upper bound
u*_B<=18 contradicts its protected lower bound20. Therefore x_A=0.
Set T=t_A=a-2>=1. We now have

```text
x_B,x_C>=1, t_B>=max(0,2-x_B), t_C>=max(0,2-x_C),
x_B*x_C+T(t_B+t_C)+t_B*t_C <=4.                  (2)
```

**3. Exhaust the small budget without the least-slack assumption.**
If x_B,x_C>=2,then(2) forces x_B=x_C=2 and t_B=t_C=0.
The cross sum is exactly4,so all three next-count bounds are equalities
by conservation. Here original p7,M=T+10 and p*=T+4. Thus
u*_B=u*_C=3p*+8=3T+20 and original u_B=u_C=16,with b=c=3.
Their protected pair cut requires u_B+u_C>=33;32 is impossible.

Otherwise exchange B,C if needed and put x_B=1,x_C=h>=1.
Then t_B>=1. Inequality(2) forces h<=3. A useful further bound
comes from B's reflected protected singleton. As b=t_B+2 and
p*=T+t_B+t_C+4,its upper bound f*_b(2)-1 compared with
L(b)+2b+2X+5 gives

```text
T+t_C >= X-1 = h.                               (3)
```

If h3,(2) forces T=t_B=1,t_C=0,contradicting(3).
If h2,and t_C>=1,then the left side of(2) is at least
2+2+1=5. Hence t_C=0. Now(3) gives T>=2 and(2) gives
T*t_B<=2. Thus T2,t_B1,t_C0,x=(0,1,2),t=(2,1,0).
If h1,then t_B,t_C>=1 and(2) forces T1,t_B=t_C=1,
x=(0,1,1),t=(1,1,1). This exhausts all possibilities.

In each surviving pattern Cross(x)+Cross(t)=4. Therefore equality
in every upper bound is forced;there is no unexamined target range.
For h2 we get P*=5,Q*=4,p*=7 and u*=(13,20,29),hence
original sizes(4,3,3),p6,M12,targets(29,22,13).
For h1 we get P*=5,Q*=3,p*=7 and u*=(10,20,20),hence
original sizes(3,3,3),p5,M11,targets(16,19,19).

**4. Actual failures,actual repairs.** In the first table row,
root A at16 needs two high values;each nonroot at19 also needs two.
The minima sum6>Q5. A full partition is

```text
{2,3,11} / {0,9,10} / {4,7,8}.
```

In the second row,the original low interval is2..5 and high is8..12.
A at29 as root needs3 high values:two highs plus one low sum at most28.
B at22 needs2 highs:one high plus two lows sums at most21.
C at13 needs1 high:three lows sum at most12. All are feasible
individually (e.g. A8+9+12,B2+8+12,C2+3+8),but minima sum6>Q5.
A full partition with zero in C is

```text
{4,5,9,11} / {2,8,12} / {0,3,10}.
```

All sizes,sums,disjointness and pool membership are visible directly.
Both targets satisfy protection. For the second,the singleton lower
bounds are18,12,12 and pair lower bounds42,42,33;actual pair sums
are51,42,35. The equality42 on A+C is an unexpected sharp check:
this is a real pair-minimum case,not a hidden globally least A case.
The first has singleton bounds12 and pair bounds33,with pair sums
35,35,38. These are literal hand controls,not an experiment.

**Consequence and limits.** MI391 supplies an individually eligible
owner. If that owner fails the minimum-count bound,the entire target
is one of the two explicitly solved configurations above. Otherwise
only the maximum-count inequality Q<=sum max K is left for that
owner. Proving that SOME eligible owner satisfies the maximum bound
would therefore close scalar admission-or-explicit-repair,and MI389
would yield the conditional low-shape partition theorem. That maximum
assertion is still OPEN. We do not infer it from these repairs.

Niggle sweep:the reflection uses remaining cardinalities;its protected
bounds are derived from original complementary groups. The deficit
reduction requires nonempty K and uses actual legal count ranges.
Zero low supply is handled first. The parameter T here is a-2,not
the total target. The two-nonroot-large pattern is excluded by the
PAIR cut,not individual feasibility. Conservation forces the target
values only when the cross sum is exactly4. Relabelling B,C carries
both sizes and sums;A always denotes the tested owner. Neither
explicit partition depends on pending G319. No novelty claim or
promotion to PROVED before independent scrutiny.

Gut verdict:the pull has a fresh reason:the old troublesome16/19/19
example now belongs to a complete two-exception classification,and
the second exception is repaired directly. Reasoned verdict:one
of the two aggregate obstacles has been removed at hand-sketch level;
maximum-count shortage remains. Next cheap test:in the original
maximum-deficit classification,handle the two incrementable nonroot
bins by moving zero off the high-only root,then inspect its three-bin
cross-budget patterns. No new census or separate component review
queue;send this as an application note to the existing checkpoint.
13-minute heartbeat ACTIVE;full low-shape/five-bin/P_0/E28/L8 OPEN.

### MI394 — B202: the remaining maximum-count shortage (2026-10-18 12:32 BST)

Question:can an eligible zero owner fail maximum-count capacity,and
can every such failure be repaired? Record searched:maximum.count
AND shortage ->2 hits in this notebook;MI384,MI389,MI391 and MI393
are the relevant carrying sources. Shared main and Cloud flags are
unchanged. No new primary-literature theorem is imported;the nearby
partition-polytope paper remains abstract-read only,novelty unassessed.

Pull:the same cross-product budget may classify this side too.
Unease:changing zero owner directly might require a needless new
selector. First test whether protection leaves only explicit exceptions.
Countercheck:do not assume every eligible owner passes;retain the
old16/18/18 near-extreme pattern. Unexpected check:use the protected
PAIR cuts when a count row appears individually feasible. Hand block
only,no experiment or expanded census. Stop at this exact low shape.

### MI395 — B202: shortage classification and the complete low-shape candidate (2026-10-18 12:32 BST)

**Hand PROOF-SKETCH;independent verification pending.** In the same
protected low shape and notation as MI393,fix any individually
eligible zero owner A. A maximum shortage sum max(K_i)<Q occurs
only in these two configurations,up to exchanging B,C:

```text
(a,b,c)   (u_A,u_B,u_C)   p   M
(3,3,3)   (16,18,18)      6   11
(4,3,3)   (29,13,20)      7   12
```

Both really fail that rooted bound and both have explicit partitions
with another owner. Together with MI391,MI393 and MI389,this supplies
a COMPLETE COMPOSITE HAND CANDIDATE for the protected low shape,
conditional on G319 and the recorded completion lemmas. There is no
least-slack assumption. Full five-bin/P_0/E28/L8 remain OPEN.

**1. General maximum-deficit algebra.** If P=0,nonempty K_i are
singletons {r_i},so no shortage occurs. Otherwise use MI384 section1's
reduction directly on the ORIGINAL positive pool,not its reflection.
Write k_i=max K_i,l_i=r_i-k_i,sum k=Q-D,D>=1. For the incrementable
bins J (l_i>0),the next legal count satisfies

```text
u_i <= f_(r_i)(k_i+1)-1.
```

The total or the single high-only outside bin gives
u_J>=alpha(R)=L(R)+4R-2P,where R=sum_J r_i=P+kappa and
kappa=Q-sum_(outside J)r_i. Legal capacity and the quadratic minimum
identity exclude j=|J|<=1,D>=j,and(j,D)=(3,2),exactly as written in
MI384 section1 and reproduced in MI393 section1. Only(2,1),(3,1)
remain. No global least-slack comparison enters this reduction.

**2. The two-incrementable-bin case is impossible.** Its upper
bound is alpha(R)+1. If A belongs to J,protection for original
size R+1 exceeds alpha(R) by2P+3,already a contradiction.
Otherwise J={B,C} and A is high-only. Put

```text
x=k_B, y=k_C, t=l_B-1, w=l_C-1.
x+y=kappa-1, t+w=P-1,
x+t=b-1>=2, y+w=c-1>=2.
```

The exact two-bin version of the deficit identity sharpens the bound:

```text
0 <= u_B+u_C-alpha(R) <= 1-x*y-t*w.               (1)
```

If x,y are both positive,xy<=1 forces x=y=1;then t,w>=1,
contradicting xy+tw<=1. Thus one high count is zero,say x=0.
Now t=b-1>=2,so(1) forces w=0. Since t+w=P-1,we have b=P.
B therefore owns the entire low interval and no high values. Its
scalar bounds coincide at L(b)+2b,strictly below its protected
lower bound L(b)+3b. This contradiction removes the entire case.
It also removes the apparent need to transfer zero off a high-only
root before understanding the count pattern.

**3. Three incrementable bins.** Put x_i=k_i,t_i=l_i-1. The
remaining deficit D1 gives

```text
x_A+t_A=a-2, x_B+t_B=b-1, x_C+t_C=c-1,
P=sum t+2, Q=sum x+1,
0 <= sum_i(f_(r_i)(k_i+1)-1)-sum(S)
   =4-Cross(x)-Cross(t).                          (2)
```

If all x_i>0,Cross(x)<=4 forces x=(1,1,1). Then t_B,t_C>=1
and Cross(t)<=1 force t=(0,1,1),a=b=c=3,P4,Q4,p6,M11.
The cross sum is4,so conservation forces equality in all three
upper bounds,namely targets(16,18,18). Retain this actual exception.

If x_A=0 and x_B,x_C>0,set S0=t_B+t_C,t_A=a-2. The root's
low-only upper bound and protected lower bound imply

```text
(a-1)*S0 >= a+2.                                 (3)
```

For a>=4,S0>=2 and Cross(t)>=(a-2)S0>=4,while Cross(x)>=1,
contradicting(2). For a3,S0>=3. If x_B*x_C>=2 the contradiction
already follows;otherwise x_B=x_C=1 forces t_B,t_C>=1 and
Cross(t)=S0+t_B*t_C>=4,again impossible.

**4. Two or more zero x entries.** If x_A=x_B=0,then
 t_A=a-2>=1,t_B=b-1>=2. Inequality(2) forces t_C=0,as a positive
t_C would make Cross(t)>=2+3=5. Thus p=a+b+1. Their next-count
bounds are

```text
u_A<=L(a)+p,  u_B<=L(b)+b+p.
```

The sum minus their protected pair bound is at most
2p-ab-3a-2b=2-a-ab<0. This is impossible;the A,C case is identical.
If x_B=x_C=0,then t_B,t_C>=2. Inequality(2) forces
 t_B=t_C=2,t_A=0,b=c=3,p8. Each next-count bound is14,so their
pair sum is at most28<33. All possibilities with two zero x entries
are excluded,including three zeros.

**5. Exactly one nonroot x entry zero.** Exchange B,C so x_B=0
and write

```text
v=x_A>=1, w=x_C>=1, T=t_B=b-1>=2,
y=t_A>=0, z=t_C>=0,
v+y=a-2, w+z=c-1>=2,
v*w+T*(y+z)+y*z <=4.                             (4)
```

If y+z=0,then w>=2. B's next-count bound is
u_B<=L(b)+2b+3. Protection forces b<=3;hence b3,T2,p6,u_B12.
Equation(4) permits only(v,w)=(1,2),(1,3),(1,4),(2,2).
Here a=v+2,and A's next-count bound is the minimum sum of v+1
high values minus1,namely8(v+1)+L(v+1)-1. Adding12 and subtracting
the protected bound for original size a+b=v+5 gives v-6<0.
Every one of these possibilities violates the A,B pair cut.

If y+z>0,(4) forces y+z=1,T<=3. For T3,we must have v=w=1.
The condition w+z>=2 forces z1,y0. Thus(a,b,c)=(3,4,3),p8;
the upper bounds u_A<=20,u_B<=18 violate their pair bound42.

For T2,only(v,w)=(1,1),(1,2),(2,1) remain.
If y1,z0,then w>=2 forces(v,w)=(1,2). Here(a,b,c)=(4,3,3),p7;
upper bounds u_A<=20,u_B<=13 again violate their pair bound42.
If y0,z1 and v1,then a=b=3,p7 and u_A<=18,u_B<=13 violate
their pair bound33,for either w1 or w2.
The only remaining pattern is

```text
v2,w1,T2,y0,z1;
x=(2,0,1), t=(0,2,1), (a,b,c)=(4,3,3), P5,Q4,p7,M12.
```

Here Cross(x)+Cross(t)=2+2=4. Equality in all upper bounds is
forced,so the targets are exactly(29,13,20). This is the second
actual exception,and exhausts(4). There are no unconstrained target
ranges left behind the count classification.

**6. Verify and repair both actual exceptions.** For p6,M11,
targets16,18,18 with sizes3^3,root A's maximum high count is1
(two high values already sum17). Each nonroot's maximum is also1
(two highs and one low sum at least19). Each count1 is feasible:
A11+5,B9+4+5,C9+4+5,independently. Thus sum max K=3<Q4.
A literal joint partition,with zero in B,is

```text
{3,4,9} / {0,8,10} / {2,5,11}.
```

The repeated values in the independent feasibility examples are
intentional:those examples test separate K intervals only. The
partition just displayed is disjoint and uses the entire pool.
Singleton protection is12;pair sums34,34,36 all exceed33.

For p7,M12,target29,13,20 with sizes4,3,3,root A can use at
most2 highs (three highs sum at least30);B can use no high (one
high and two lows sum at least14);C can use at most1 high (two
highs and a low sum at least21). These maxima are individually
feasible by11+12+6,2+5+6,and9+5+6,respectively. Their sum3<Q4.
A literal joint partition is

```text
{4,6,9,10} / {0,2,11} / {3,5,12}.
```

It has the original sizes and sums and exhausts S exactly. Its
singleton lower bounds are18,12,12. Pair sums42,49,33 meet the
corresponding bounds42,42,33;TWO pair cuts are tight. This is the
unexpected sharp control:protection does not exclude all bad roots,
but the bad roots need not obstruct a partition.

**7. Complete assembly for this low shape.** The candidate statement
is:for S=[0,M] minus{1,p,p+1},2<=p<=M-2,a,b,c>=3 summing to M-2,
and integer targets with total sum(S),the six proper protected cuts
u_J>=L(s_J)+3s_J suffice for a prescribed-size,prescribed-sum partition.

MI391 supplies an owner with every K_i nonempty. Choose any such
owner. If its minimum-count bound fails,MI393 gives one of two
explicitly partitioned configurations. If its maximum-count bound
fails,the present proof gives one of two explicitly partitioned
configurations. Otherwise the nonempty integer intervals have
sum min K<=Q<=sum max K,so choose k_i in them summing Q;their
low counts then sum P. MI389 completes these admitted counts,
possibly changing the owner/counts,in its exceptional cases.

This final step is conditional on G319 and MI383's generic count-row
completion,with MI378/MI295 supplying the regular rows. MI389 was
reread before this assembly. MI391 and both count classifications
are additional unreviewed carrying hand lemmas. No G320 least-slack
assumption or W318 deletion-spectrum theorem is needed. The four
explicit exceptional partitions need none of those compatibility
lemmas. This is a complete proof candidate with named provisional
dependencies,not a claim of independent verification or novelty.

Niggle sweep:the two-bin reduction uses the ONE outside high-only
bin,not an invalid union of independent maxima;its sharpened xy+tw
bound forces entire low ownership. Three-bin patterns exhaust all
zero supports of x,including root plus nonroot zeros. In(4),the
unbounded T case y+z0 is bounded by protection before enumerating
v,w. Every rejection uses original cardinalities in its pair bound.
The exceptional target values follow from total conservation only
after zero excess is established. All four failures across MI393/395
are repaired by full disjoint partitions,not separate subsets.
P0 is explicit. No experiment,new census or status upgrade.

Gut verdict:the fresh pull is the shorter proof mechanism:instead
of engineering a zero transfer for every shortage,we can exhaust
all shortages and repair four fixed configurations. Reasoned verdict:
protected low-shape sufficiency now has a complete composite hand
candidate. This is an appropriate combined review milestone,not a
reason to wait before independent work. Next map precisely what this
settles in the parent one-hole/five-bin reduction and what remains;
do not silently promote this special shape to arbitrary holes.
13-minute heartbeat ACTIVE;full five-bin/P_0/E28/L8 OPEN.

### MI396 — B203: trace the completed low shape back to its parent (2026-10-18 12:45 BST)

Question:which actual parent cases does G321 settle,and can the
canonical repair be CHOSEN to land there? Record searched:low.shape
AND parent ->8 hits/3 files. Read MI362,MI368,MI374,MI376,MI385,
MI389 and FOUR-BIN-PARTITIONS section6's pivot construction.
Shared main and Cloud flags unchanged;G321 and dependencies still
await independent verification. No experiment or new literature claim.

Pull:choose the favourable repair before solving another shape.
Unease:reflecting a protected punctured pool does not preserve the
same margins. The unexpected hand check is the legal endpoint where
a displayed three-hole shape trims to one hole. This block audits
scope and inherited hypotheses;it does not reopen the generic hole tree.

### MI397 — B203: prefer the low repair;only one high shape is unavoidable (2026-10-18 12:45 BST)

**Conditional parent reduction,hand UNREVIEWED.** G321 settles every
protected low-shape remainder,including cases with a strict pair
minimum. The stronger conclusion below is a choice of repair in the
actual one-hole FOUR-bin parent. It is not a proof of that parent or
of full five-bin sufficiency. No new proof-review job or experiment.

Let the parent be P=[0,m] minus q,with four sizes>=3 summing to m,
correct target total,and all proper group cuts u_J>=L(s_J)+s_J
(the P_0 problem of MI362). Suppose singleton D,size a,is globally
least for delta_J=u_J-L(s_J)-s_J. Put n=m-a>=9 for the total
size of the other THREE bins. Original endpoint q0/m cases already
reduce to G316 on a translated/full interval. Take0<q<m below.

**Protected one-hole scalar admission.** The parent cuts imply
individual feasibility for D:an r-subset actual minimum is at most
L(r)+r,while the complementary protected cut supplies the upper
bound. A one-hole scalar omission at minimum+1 requires q=r and
has value L(r)+1<L(r)+r. An upper omission is the corresponding
lower omission for the complement,also excluded. This uses sizes
at least3 on both sides. The same observation applies later to a
protected ONE-hole three-bin remainder,where G315 then gives joint
completion. For a full-interval remainder,the ordinary cuts and
MI295 suffice. No arbitrary two-hole joint theorem is imported.

Use the actual extreme-value prefix/suffix/pivot construction in
FOUR-BIN-PARTITIONS section6. A legal pivot leaves at most TWO holes
after trimming;MI368 preserves at least the actual-hole-count margin.
If at most one hole remains,the preceding paragraph completes it.
An actual two-hole three-bin remainder remains a separate open branch.
The rest of this entry concerns a FORMAL missing pivot q only.

**1. There must be a nonempty low prefix.** Write l+k=a-1,
with formal prefix0..l-1,suffix u..m,u=m-k+1,and pivot q.
These are distinct formal values,so l<=q<=u-1. Put p=q-l>=0.
The prescribed target and its protected slack are

```text
u_D=L(a)+p+k(n+1),
delta_D=p+k(n+1)-a.
```

The sum of D's and its complementary group's protected slacks is
an-q. Global minimality implies delta_complement>=delta_D,so

```text
3p <= n(l-k+1)+l+2.                              (1)
```

If l=0,then k=a-1>=2 and the right side is
n(2-a)+2<0,contradicting p>=0. Thus l>=1. This eliminates the
apparently unavoidable high-repair case caused by an empty prefix.
The argument uses the complementary THREE-bin group in the parent;
being least only among singletons would not justify(1).

**2. Choose the low repair whenever p>=2.** Replace the formal
pair {l-1,q} by {l,q-1}. Both replacements are distinct and available
because q-(l-1)=p+1>=3. The remaining minimum is l-1. Before any
upper trim,the remaining span has normalized length

```text
M0=m-k-(l-1)=n+2,
holes {1,p,p+1}.
```

By MI368,the remaining proper group targets,after subtracting l-1
per token,satisfy margin

```text
mu=a+1-(l-1)=k+3 >=3.                            (2)
```

If 2<=p<=M0-2,the endpoints are present and G321 applies,conditional
on its recorded hand dependencies. It requires neither a least
singleton in this THREE-bin remainder nor the preservation of the
parent's minimizer. This is precisely the obstacle removed in B202.

The upper boundary p=M0-1 is possible in the formal interval and
must not be passed to G321 as an internal-hole case. Its missing
values include M0-1,M0. Trimming those two top positions leaves
[0,M0-2] minus1,a ONE-hole pool. Margin(2) still holds,so protected
one-hole admission and G315 complete it. No other upper p is legal.
This is the endpoint check that keeps the reduction honest.

**3. The cases p=0,1.** Protection for D gives delta_D>=0.
With p<=1 and a>=3,this forces k>=1. The high repair exists:
replace {q,u} by {q+1,u-1}. Its normalized span,subtracting l,
is again M0=n+2,with holes

```text
{p,p+1,M0-1},  margin mu=k+2>=3.                  (3)
```

For p0,the two lower endpoints0,1 are absent. Trim them and
subtract2. The pool becomes [0,n] minus{n-1} and margin becomes
k>=1. Protected one-hole admission plus G315 complete this case.

For p1,the endpoints are present and the remaining pool is exactly

```text
S_high=[0,n+2] minus{1,2,n+1}
      ={0} union [3,n] union {n+2},
proper group margins at least k+2>=3.
```

This ONE high shape remains open in this route. Arbitrary positions
of the adjacent high-shape holes are not required:when p>=2 we can
choose the low repair instead. Reflection alone does not close p1.
Indeed a three-hole pool [0,M] minus H with margin mu=3+e reflects
to the lower bounds

```text
u'_J >= L(r)+sum(H)-3+e*(n-r),  n=M-2.
```

For this high shape sum(H)=M+2=n+4,so the extra term is
n+1+e*(n-r),not generally3r. The low-shape theorem cannot be
invoked just because the REFLECTED missing set has its geometry.

**4. What has actually contracted.** In the globally least-singleton
branch of P_0,the canonical route now leaves only:

- a legal-pivot TWO-hole three-bin remainder with inherited protection;
- S_high={0} union[3,n] union{n+2},with inherited margin k+2.

All low missing-pivot repairs and both relevant endpoint trims now
complete conditionally on G321/G315. This does not establish that
P_0 always has a minimizing singleton:its minimum can be a pair OR
a triple,and reflection of P_0 is not symmetry of its assumptions.
At the full FIVE-bin level,the original strict pair/triple-facet
branch also remains separate. No reflection of an intermediate
punctured pool is substituted for reflection of the original interval.

The exact infinite lift family in MI385 now gains a conditional
partition theorem:its sizes(2p,p,a,b,c) and displayed target formula
complete for every protected low-shape target,not just the examples
or the globally least-three-bin-singleton subcase. This is a direct
application of the existing lift and G321,not another proof filing.
It does not assert that all five-bin instances have those sizes/targets.

**Hand scope controls.** MI368's actual parent [0,12] minus5,
targets(6,22,22,23),has a=3,l2,k0,p3. Low repair {0,2,4},followed
by subtracting1,leaves [0,11] minus{1,3,4},targets19,19,20 and
margin3. G321 covers it;the previous need for another selected
singleton/hole-budget argument is gone.
MI366's N17 lifted residual [0,14] minus1,targets14,14,38,38,
has strict pair adjusted minimum7 versus singleton minimum8.
It is NOT covered by this parent-singleton reduction,despite being
positive by its displayed partition. This guards against turning a
successful local theorem into a silent full-parent claim.

Niggle sweep:the formal pivot remains absent,only the balanced
replacement is used;all low-repair parameter endpoints are accounted
for. Low-prefix nonemptiness comes from the parent's global minimum,
not the new three-bin theorem. The top trim changes hole count but
not translation;the p0 bottom trim changes margin by2. Both leave
at least the one-hole margin required for scalar admission. Three
remaining bins retain original sizes>=3 throughout. No generic
three-hole induction or independent verification is claimed.

Gut verdict:the useful pull is toward choosing the good geometry,
not filling an inherited catalogue of bad geometries. Reasoned:
the actual missing-pivot branch has contracted to one explicit
unhandled shape. Next cheap hand test on S_high:assign0 to a bin,
then translate the positive pool by-3. It becomes
[0,n-1] minus{n-2},a one-hole pool. If the zero owner's original
size is>=4,all remaining sizes are>=3 and G315 is available after
scalar admission;an original size3 owner leaves size2,so the exact
boundary and owner choice must be checked rather than assumed.
No experiment or automatic generic-hole expansion.13min ACTIVE;
G321 still awaits review,full P_0/five-bin/E28/L8 OPEN.


### MI398 — B204: the remaining high shape and a change of approach (2026-10-18 12:57 BST)

Question:do all protected targets on S={0} union[3,n] union{n+2},
three sizes>=3 and all proper lower cuts L(r)+3r,partition?
Initial pull:toward removing0 and applying G315 to the translated
one-hole remainder. Unease:an original triple becomes a pair.
Record searched:`one.hole` AND `size2`:9 hits/3 files;MI334/335
read. The known negative on {0,1,2,3,4,6},sizes2/2/2,targets2/6/8
rules out an unqualified size2 extension. The padded two-pair
negative in MI335 is also retained;neither settles one pair/two
larger bins. No new general one-hole claim is made.

Changed approach:assign BOTH isolated values0 and n+2 first.
The middle becomes a full interval,where reviewed MI295 permits
sizes2. This is useful only if the endpoints can be assigned to
different original triples,or together to a bin of size>=4.
Record searched:`outlier|endpoint.*owner|two.*isolated` AND
`three.bin|partition|MI329`:9 hits/2 files. MI329's outlier-owner
budget read in full;it supplies the idea,not a dependency or a
previous statement of this two-endpoint result. The reviewed
MI295 proof in FOUR-BIN-PARTITIONS section5 and actual one-hole
scalar hypotheses in section2 were read. One bounded primary
literature search for almost-consecutive prescribed-cardinality
partitions found no matching statement;no novelty or complete
literature-search claim. No new external theorem imported.

No experiment or new census. The following is a direct hand proof
and hand adversarial checks. The proposed kill conditions are an
endpoint assignment leaving size1,an unprotected middle-interval
upper bound,or two bins both forced to own the largest endpoint.
The endpoint assignment must rule out all three without assuming
an existing compatible partition.


### MI399 — B204: two endpoint owners complete the protected high shape (2026-10-18 12:59 BST)

**Complete HAND CANDIDATE,not independently verified.** Only the
reviewed full-interval three-bin lemma MI295 is a theorem dependency.
No G315/G319/G320/G321/W318 or generic punctured-pool theorem is used.

Let a,b,c>=3,n=a+b+c,and S={0} union[3,n] union{n+2}.
Suppose integer targets u_i sum to

```text
T=sum(S)=L(n)+2n-1
```

and every proper nonempty group J satisfies
u_J>=L(s_J)+3s_J. Then S has a partition of those sizes and sums.
A larger inherited margin also implies these hypotheses.

Write t=n+2 and I=[3,n]. For an s-subset of the core I define

```text
alpha_s=L(s)+3s,  beta_s=ns-L(s).
```

All sizes used below are within0..n-2. A singleton lower cut and
the complementary pair's lower cut give

```text
alpha_s <= u <= H_s := T-alpha_(n-s)
                    = beta_s+2s-n-1.                     (1)
```

For the four possible assignments of isolated endpoints to a bin
of original size s,the necessary middle-interval bounds are:

```text
neither:  alpha_s <= u <= beta_s;
0 only:   alpha_(s-1) <= u <= Z_s := beta_(s-1);
t only:   Q_s := t+alpha_(s-1) <= u <= t+beta_(s-1);
both:     B_s := t+alpha_(s-2) <= u <= t+beta_(s-2).
```

These are individual core bounds,not a claim of joint allocation.
The useful identities are

```text
Q_s=alpha_s+n-s,
B_s=alpha_s+n-2s-1,
t+beta_(s-2)=H_s,
beta_s-B_s=(s-1)(n-s-1)>0,
Q_s-B_s=s+1,
(t+beta_(s-1))-H_s=n+2-s>0.                    (2)
```

Thus (1) already supplies the lower bound for a zero-only bin,
the upper bound for a top-only bin,and the exact upper bound for
a both-endpoints bin. A both-endpoints assignment will be used
only when s>=4. Distinct endpoint owners leave sizes>=2 as well.
Once an assignment satisfying these bounds is found,the three
remaining core targets sum to sum(I). Translate I by-3 and invoke
MI295 with all three residual sizes>=2. Its singleton rank bounds
and conservation give the actual compatible partition. Restore
the assigned endpoints. It remains to prove that assignment exists.

**Case1:a target exceeds beta_s.** By (1),this requires
2s>n+1,so at most one bin j can do so. Its size is>=4.
By (2),u_j>beta_s>B_s;give BOTH endpoints to j. Its upper
bound is (1),and both other bins satisfy their neither-endpoint
bounds. The core lemma finishes. No two bins can be forced above
the core maximum because two sizes>(n+1)/2 cannot sum to at most n.

**Case2:every target is at most its beta_s.** If some bin of
size>=4 has u>=B_s,give it both endpoints. The other bins
already meet their core bounds,and again MI295 finishes.

Otherwise assume every size>=4 bin has u<B_s. At least one
bin is eligible for the TOP endpoint alone:u_j>=Q_(s_j).
Indeed put K=ab+ac+bc. If every u_i<=Q_(s_i)-1,then

```text
T-sum_i(Q_(s_i)-1)=K-3n+2>=2>0,
```

a contradiction. The inequality follows on writing each size
as3+x_i:K-3n=3 sum(x_i)+sum_(i<j)x_i*x_j>=0.
By Q_s>B_s and the present assumption,ANY such top-eligible
bin has original size3. Call it B,with other sizes a,c>=3.
At least one of A,C is eligible for ZERO alone. Otherwise their
integer targets satisfy u_A>=Z_a+1 and u_C>=Z_c+1,and

```text
u_A+u_B+u_C >= Z_a+Q_3+Z_c+2,
Z_a+Q_3+Z_c+2-T = ac-n+1
                       = (a-1)(c-1)-3 >=1,
```

contradicting conservation. Assign0 to a zero-eligible OTHER bin
and t to B. The third bin gets neither. All displayed bounds
hold,all residual sizes are>=2,and MI295 finishes. This exhausts
the cases and proves the candidate statement.

**Hand controls and unexpected check.** The all-triple n9 case
cannot place both endpoints together in this proof,even when
its scalar both-endpoints inequality allows it:that would leave
size1. Targets13,20,20 on {0,3,4,5,6,7,8,9,11} satisfy the cuts
and have the different-owner partition
{0,4,9}/{11,3,6}/{5,7,8}. This explicitly checks the boundary
that blocked the first one-hole reduction.

For n10,sizes4/3/3,targets20/22/22,the both-endpoints branch gives
{0,3,5,12}/{4,8,10}/{6,7,9}. The two pair cuts involving the
first bin are exactly42=L(7)+3*7,so the proof tolerates equality.

Unexpected forced-owner check:n14,sizes8/3/3,targets85/15/18.
Here beta_8=84,H_8=85,so the first bin really is forced above the
core maximum. The cuts hold,including15+18=33=L(6)+18,and
{0,9,10,11,12,13,14,16}/{3,4,8}/{5,6,7} is a literal partition.
This tests the branch that would be lost by assuming every bin
could avoid the top endpoint. These are hand checks,not a census
or an independent verification.

Niggle sweep:the total is L(n)+2n-1,not the low-shape total;
core upper bounds use its actual top n. Pair protection is used
in (1),not replaced by singleton protection. The top owner in
Case2 is a triple only AFTER excluding every large both-owner.
The zero owner is different in that final case. No residual size1
or scalar-to-joint inference is hidden:joint completion is exactly
MI295 on a full interval. No reflection of a punctured margin is
assumed. The old size2 one-hole counterexample remains valid.

Gut verdict:renewed pull from simplifying the representation;
the interesting change was assigning the two exceptional tokens
together before invoking a theorem. Reasoned verdict:the sole
high missing-pivot shape has a complete independent-of-G321 hand
candidate. With MI397 and pending G321,the globally least-singleton
MISSING-pivot branch of P_0 now completes conditionally. Legal-pivot
two-hole remainders and nonsingleton parent branches remain OPEN;
full five-bin/E28/L8 likewise remain OPEN. Novelty unassessed.
Next cheap test:inspect the actual legal-pivot two-hole geometry
for an endpoint-owner reduction;do not broaden to arbitrary holes
without a useful parent implication. Keep the13-minute heartbeat
ACTIVE and batch this source with Cloud's pending combined review.


### MI400 — B205: compressed-hole counts and a fixed feedback test (2026-10-18 13:10 BST)

Pull:the endpoint proof removed exceptional values before solving the core.
For legal INTERNAL holes there is no uninterrupted core with only two
exceptional values. A rank compression instead keeps the full interval
and puts the two defects into ownership counts. Record searched:
`two.hole|legal.pivot` AND `protected|margin|MI357`:35 hits/7 files;
MI351/357/368 and FOUR-BIN-PARTITIONS scalar/base sections read.
MI357 is the older minimum4 generic-hole route;it does not settle
this protected minimum3 branch. No new external result is needed.

For R=[0,n+1] minus{p,q},0<p<q<n+1,its increasing list is
z_j=j+1_(j>=p)+1_(j>=q-1),j=0,...,n-1. If a bin owns k ranks
at least p and ell ranks at least q-1,its physical target u becomes
w=u-k-ell. The count constraints are
0<=ell_i<=k_i<=s_i,sum k=n-p,sum ell=n-q+1.
Protected cuts u_J>=L(s_J)+2s_J imply ALL full-interval rank cuts
for EVERY such count array,because k_J+ell_J<=2s_J. Conservation
gives sum w=L(n). Thus reviewed MI295 solves each compressed target.
But it does not ensure that its solution realizes the assumed counts.
That is an exact compatibility question,not a fixed-point theorem.

Hand countercontrol to the unqualified inference:pool0..6 minus5,
sizes2/2/2,targets2/6/8,compresses to0..5 with one lifted top token.
All three hypothetical top-owner target tuples satisfy full rank bounds.
Owner A gives target1 and cannot contain5;owner B would need{0,5}
while A's target2 forces{0,2};owner C would need{2,5},again colliding
with A. Every assumed owner has a compressed partition,but none
has a compatible one. This control lacks the protected minimum3
hypotheses;it defeats only the logical shortcut,not the desired theorem.

**Preregistered ONE-domain diagnostic,not a new census.** Use n9,
p3,q6,sizes3/3/3,physical targets15/15/16. Enumerate the1680 labelled
partitions of ranks0..8. For each admissible nested count array,
choose the lexicographically first partition with compressed sums w;
extract its actual counts to define deterministic feedback F. Classify
ALL functional-graph cycles. Blind prediction:some start enters a
nontrivial cycle,so naive repeated compressed solving is not a proof
mechanism even on the protected domain. A fixed point gives a literal
physical partition,but does not by itself establish global convergence.

This is an ACTUAL parent legal-pivot case:in [0,12] minus5 choose
D={0,1,8},size3,target9;other targets21/21/22. D has adjusted slack3,
other singleton slacks15/15/16,pairs involving D9/9/10,other pairs21/22/22,
triples involving D6/7/7,and complementary triple19. D is globally
least. Subtract2 from its remainder to obtain the stated R and targets.
The full five-bin lift is sizes3^5,targets8/15/27/27/28,first bin{0,1,7}.
Thus the diagnostic is on the actual branch,not an arbitrary hole pool.

Controls:all1680 rank partitions have distinct disjoint masks and full
coverage;all compressed queries must be feasible by MI295;every feedback
fixed point must give a literal physical partition. Independently build
physical target partitions by subset-sum/backtracking on R and compare
against the mapped rank catalogue. Counterfactual:the size2 hand fixture
must have no literal partition although all three compressed queries pass.
Unexpected check:swap the second and third physical target labels and
compare existence/fixed-point witnesses;lexicographic feedback need not
have invariant basins. Stop after these two labelled versions of this
ONE physical target and the countercontrol,or after5 CPU seconds.
No larger n,other holes,random seeds or automatic rerun. Results below
will distinguish failure of feedback from failure of partition existence.


### MI401 — B205 outcome: blind count feedback cycles on an actual protected instance (2026-10-18 13:12 BST)

**COMPUTED diagnostic;hand explanation of the cycle.** One run of
`tests/probes/instinct_two_hole_feedback.py`,unchanged after MI400
registration,completed in0.012880 CPU seconds on this checkout.
All controls passed. Each labelled version has45 nested-count states,
all45 compressed targets feasible,and10 literal physical partitions.
The independent physical subset-sum/backtracking set agrees exactly
with the mapped1680-partition rank catalogue. No larger domain or
rerun. Raw output retained outside git as math-instinct-b205-feedback.json;
SHA256 fa677bd13e4a21341e9618647bbcc0b6adeafc0e3f6537212e7fb179ea2dc75c.

For target15/15/16 the feedback function has NO fixed point. Every
one of its45 states reaches the SAME2-cycle. Write a count state as
((k_A,ell_A),(k_B,ell_B),(k_C,ell_C)). The two cycle states are

```text
X=((2,1),(2,1),(2,2)),
Y=((2,1),(2,2),(2,1)).
```

At X the compressed targets are12/12/12. The lexicographically first
rank partition is

```text
{0,4,8}/{1,5,6}/{2,3,7}.
```

Its actual counts are Y. Under z=(0,1,2,4,5,7,8,9,10),its physical
sums are15/16/15. At Y the compressed targets are12/11/13 and the
first rank partition is

```text
{0,4,8}/{1,3,7}/{2,5,6}.
```

Its actual counts are X and its physical sums are15/14/17. The
iteration therefore alternates indefinitely. These two explicit
transitions already give a hand counterexample to convergence;
the45-state basin size is the finite computation's separate claim.
The blind prediction of a nontrivial cycle was confirmed.

An actual desired partition is

```text
{0,5,10}/{2,4,9}/{1,7,8},  sums15/15/16.
```

Its compressed rank sums are12/12/12 and its counts are X. It is
simply NOT the first partition of that compressed fibre. Thus the
feedback function erased a compatible solution by tie-breaking;
there is no failure of the physical target or the full-interval base.

**Unexpected relabelling check.** For target15/16/15,the same fixed
rule has one fixed point and all45 states reach it. Its literal
partition is{0,5,10}/{1,7,8}/{2,4,9}. The complete physical count
stays10,as required under bin relabelling. Existence is invariant;
the success of this arbitrary selection policy is not. No random
work choice or random tie-break was used.

The negative size2 one-hole control has0 physical partitions while
all3 assumed-owner compressed queries are feasible. All its feasible
compressed partitions exclude the required top owner. This confirms
that compressed-query feasibility alone is not an ownership theorem.
The protected minimum3 example instead HAS compatible fibres;these
are distinct obstructions and are not conflated.

Niggle sweep:all admissible nested count arrays were listed,not just
one initial orbit. The catalogue checks labelled partitions,not an
unlabelled quotient. Fixed points were checked against literal physical
subsets;the independent oracle never uses compression. The two-cycle
has an explicit hand trace,and the underlying parent/legal pivot and
all proper parent cuts are in MI400. A deterministic policy can have
no fixed point even when the multivalued correspondence has one.
No Brouwer/monotonicity/integer-lifting theorem is asserted.

Gut verdict:mixed. The compression is a compact language for the
obstruction,but blindly feeding a solver back into itself is now cold.
The useful pull is toward choosing a compatible member of a fibre;
the equal-target bin swap here shows exactly what the blind choice
lost. Reasoned:park this feedback policy;retain the exact reduction.
Next cheap question:can a target-aware fibre choice be tied to a
strict progress quantity,or does the existing record already refute
that kind of monotonicity? Search that record before another run.
Do not try more seeds or increase the domain. This is a failed algorithm,
not a theorem against protected two-hole completion. G321/MI399 review
continues independently;full P_0/five-bin/E28/L8 OPEN,13min ACTIVE.


### MI402 — B206: one final same-domain test of target-aware feedback (2026-10-18;preregistered before the run)

Question:does a target-aware compressed-fibre choice supply a strict
progress quantity? Pull is weaker toward iteration itself;the useful
question is whether its proposed progress is real. Record searched:
`monoton|fibre|neutral` AND `MI301|MI320|MI330|MI325|MI401`:15 hits/7 files.
MI325/330 and MI334-335 read. Neutral pair moves can isolate a chosen
four-bin realization;the original one-hole relay work stopped rather
than assuming joint witnesses. Neither is a theorem about the present
three-bin fibre oracle,but both prohibit an unproved connectivity step.
Bounded primary searches for prescribed-cardinality/sum partitions
returned the already recorded Hoory-Kotlar/Chen-Fu scopes;no new theorem
or claim of literature completeness. MI295 remains the only base used.

For the SAME n9,p3,q6,size3^3,target15/15/16 and SAME45 nested states,
let E(K) be the MINIMUM physical L1 target error among ALL rank partitions
with compressed sums u-k-ell. Examine ALL minimizers,not a hidden
lexicographic choice. For each minimizer P,its actual counts K' are an
admissible next state. Test whether E(K')<E(K) whenever E(K)>0.
Also test the weaker existential version:some minimizing successor
strictly improves. Separately classify the deterministic rule that
chooses the lexicographically first MINIMUM-error partition.

Blind prediction:the universal strict-descent claim fails,possibly even
the existential one. Controls:whole1680 partitions,45 states,exact
agreement of E(K)=0 with physical-compatible counts;all actual transitions
admissible;independent original-value subset/backtracking confirms the
10 physical partitions and their count states. Counterfactual:the old
lex-only rule must still have its2-cycle. Unexpected check:strict versus
weak/existential progress and actual orbit termination are DIFFERENT
claims;report all of them,including plateaux. Stop at this SAME domain
or5 CPU seconds. No new targets,holes,n,seeds,relabellings or cap increase.
If no strict general mechanism emerges,park feedback rather than tuning
another tie-break. An exact whole-fibre minimizer is an analysis oracle,
not an algorithm already supplied by MI295.


### MI403 — B206 outcome: minimum-error selection strictly improves on the fixed case (2026-10-18 13:23 BST)

**COMPUTED,one domain only;general progress statement OPEN.**
One run of the MI402 protocol completed in0.037537 CPU seconds.
Its executed source was retained unchanged as
`tests/probes/instinct_two_hole_best_response.py`,with a descriptive
header added afterward. All controls passed;no rerun or domain increase.
The independent physical catalogue has10 labelled partitions and exactly
3 compatible count states. All1680 rank partitions and45 count states
were used. Raw output outside git:math-instinct-b206-feedback.json,
SHA256 e3959cb51784dcb6dafb56dbf261fa6bdcd678082ab597a51e9ca15a5d08f6c4.

The minimum physical L1 error over each compressed fibre is distributed:

```text
E=0:3 states; E=2:11; E=4:8; E=6:14; E=8:9.
```

For EVERY positive-error state,every minimizing partition's actual-count
successor has STRICTLY smaller minimum fibre error. Both the universal
and existential strict-progress failure counts are0. The blind forecast
of failure is REFUTED on this fixed domain. The deterministic first
minimizer rule has3 fixed points,all error0,with basins20/11/14;
there is no positive cycle. The original blind lex rule's2-cycle was
reproduced as the negative policy control,not silently replaced.

The3 fixed states have k=(2,2,2) and ell a permutation of(1,1,2).
For the old cycle's X and Y,the whole-fibre minima are already0:
compatible partitions existed and the original lex policy discarded
them. This does not imply that every state was initially solved;
42 states have positive minimum fibre error,as the distribution shows.
The test exhausts ALL minimizing choices at those42 states,not just
one favorable tie-break. Existence and proof are still distinct:
45 states of one instance cannot carry an infinite progress claim.

**Exact conjecture to test by hand.** For the protected two-hole
three-bin data of MI400,let C be all nested count arrays with the
fixed threshold totals. For K in C,let P(K) be all full-rank partitions
with sums w_i=u_i-k_i-ell_i. The reviewed full-interval theorem
makes P(K) nonempty. Put

```text
E(K)=min_(P in P(K)) sum_i |sum_(j in P_i) z_j-u_i|.
F_min(K)={actual nested counts of P:
          P in P(K) attains E(K)}.
```

The WEAKER sufficient statement is:if E(K)>0,there exists
K' in F_min(K) with E(K')<E(K). It would imply protected
two-hole completion:choose any initial K,follow strict decreases
of the nonnegative integer E,and terminate at0. Conversely E0
is exactly an actual partition. C is nonempty because one may
assign the n rank positions to the prescribed bin sizes and then
count their two thresholds,without imposing any sums. No existence
of the requested physical partition is used in defining C or P(K).
This conditional implication is elementary;the descent assertion
is the open step. The stronger ALL-minimizers version happened
to pass the finite case but is not needed for the implication.

This is an existence argument with a finite optimization oracle,
not a practical algorithm obtained for free from MI295. MI295
supplies some full-interval realization,not the physical-error
minimum within its fibre. Optimizing over the entire union of
fibres and declaring its minimum0 would merely restate the task;
the desired local strict inequality needs its own proof.

**Unexpected hand limit:target-aware selection alone is insufficient.**
In MI400's size2 one-hole countercontrol,each of the three assumed
outlier owners has a UNIQUE compressed realization:

```text
owner A:targets1/6/8,partition01/24/35,actual top owner C;
owner B:targets2/5/8,partition02/14/35,actual top owner C;
owner C:targets2/6/7,partition02/15/34,actual top owner B.
```

Thus all three minimum errors are2. Even the error-minimizing rule
has B<->C as a positive-error cycle. This is a direct hand enumeration
of the already registered countercontrol,not a new computational domain.
It shows why the proposed general proof must explicitly use protected
margin2 and minimum size3;finite fibre optimization plus full-interval
feasibility alone do NOT give strict descent. It is not a counterexample
to the protected conjecture,whose hypotheses this toy violates.

Niggle sweep:minimum error is over the whole fixed rank-sum fibre;
ALL minimizers were checked. State updates use both thresholds,not
only their sum. Each physical zero-error count is found independently
from actual values. The old lex policy remains refuted;the new result
is not a relabelling rescue or a claim that an arbitrary solver works.
The comparison E(K')<E(K) uses a NEW fibre minimum,not the unchanged
physical error of the partition which generated K'. No independent
second reader or universal convergence is claimed.

Gut verdict:surprise at the failed negative prediction. There is now
a specific mathematical pull toward the strict inequality,not a reason
to keep running variants. On a fresh choice this is worth one hand
attack because a proof would close the remaining protected two-hole
three-bin branch. Reasoned:the finite diagnostic earns a precise
conjecture only. Next inspect a hypothetical nondecreasing best response
using the two cut edges and protected rank slack;try to build a genuine
protected countercontrol before growing a repair catalogue. No further
census is authorized by this outcome. G321/MI399 review proceeds
independently;full P_0/five-bin/E28/L8 OPEN,13min ACTIVE.

### MI404 — B207: endpoint holes separate existential progress from arbitrary minimizers (2026-10-18 13:36 BST)

**Hand analysis,not a new census;carrying argument unreviewed.** Question:
can MI403's existential descent be proved using the protected margin2,
rather than treating whole-fibre optimization as a convergence theorem?
Record searched:`best.response|strict.descent|minimum.*fibre|minimum.*fiber`
and `hole|count|MI403`:16 hits/7 files. MI400-403 and the existing
MI295 three-bin base (FOUR-BIN-PARTITIONS section5) read. MI402's
primary-literature orientation is retained;no new literature or novelty
claim. Initial pull is toward an explanation of strictness;unease is that
one favorable finite graph hides bad minimizing choices. The bounded
hand test specializes to holes1,2,where the state is just the owner of0.
No experiment,larger census or new tie-break policy is run.

Put R={0} union[3,n+1],three sizes a,b,c>=3 totaling n,and
T=L(n)+2n-2. Assume every proper group target obeys
u_J>=L(s_J)+2s_J and total conservation. Define

```text
alpha_s=L(s)+3s,
beta_s=(n+1)s-L(s),
Z_s=(n+1)(s-1)-L(s-1)=beta_s-(n+2-s).
```

The protected complementary cut gives u_i<=beta_(s_i)-2.
A bin is LOW when u_i<alpha_(s_i). At most one is low:two low
bins of sizes a,b would have target sum at most
L(a)+L(b)+3(a+b)-2,strictly less than L(a+b)+2(a+b),since
ab-a-b+2=(a-1)(b-1)+1>0.

Call J a GOOD owner if an actual partition with0 in J exists.
An exact criterion,from the reviewed three-bin interval base,is

```text
u_J<=Z_(s_J), and u_i>=alpha_(s_i) for every i!=J.       (G)
```

Indeed,after removing0 from J,the remaining pool is[3,n+1],with
sizes s_J-1 and the two other original sizes,ALL at least2.
Its individual bounds are sufficient by MI295 after translation.
For nonowners the lower bound is alpha_s and the upper beta_s;
the upper holds already. For J its lower bound is
3(s_J-1)+L(s_J-1)=L(s_J)+2s_J-2,below the protected bound;
its upper is Z_(s_J). The remaining total is exactly the pool total.
Necessity of (G) is literal subset extremality. Thus no desired
partition was assumed to invoke the interval theorem.

There is always a good owner. If D is low,it is the sole low bin,
and is good because

```text
Z_s-alpha_s=(s-1)(n-s-1)-3>=7
```

for s>=3,n-s>=6. If none is low,some u_J<=Z_(s_J):otherwise
sum u_i>=sum Z_(s_i)+3>T,as

```text
sum Z_(s_i)+3-T=ab+ac+bc-2n-1
                    >=(6n-27)-2n-1=4n-28>=8.
```

The lower estimate ab+ac+bc>=6n-27 follows by writing each size
as3 plus a nonnegative integer. This proves protected completion
for this endpoint-hole family by hand,conditional only on reviewed MI295.
It does not yet prove feedback progress for interior holes.

**Existential progress in this family.** Compression is z_0=0 and
z_j=j+2 for j>=1. Both thresholds coincide. Every admissible nested
count state is exactly one assumed zero owner K;its rank targets are

```text
w_i=u_i-2s_i+2*1_(i=K).
```

All rank fibres are nonempty by MI295 and the protected cuts. For
a rank partition whose actual zero owner is J,its physical error
vector is2*(1_K-1_J). Consequently E(K)=0 for good K,and E(K)=4
otherwise. Every rank partition in a bad K fibre is a minimizer.

If a low D exists and K is bad,then K!=D. Its rank target
w_D=u_D-2s_D<L(s_D)+s_D. A subset avoiding0 has minimum
L(s_D)+s_D,so EVERY partition in that fibre puts0 in D.
D is good and the next error is0.

If no low bin exists,choose any good J. For bad K,J!=K. We show
that the K fibre has a partition with0 in J,by applying MI295 to
[1,n-1] after removing0. For either nonowner i!=J the required
rank lower bound is L(s_i)+s_i. At i=K it follows from
u_K>=alpha_(s_K) (in fact alpha-2 would suffice);at the other
nonowner it follows from u_i>=alpha_(s_i). Rank upper bounds
(n-1)s_i-L(s_i) follow from u_i<=beta_(s_i)-2,including the+2
in w_K. For J the lower bound is L(s_J),supplied by protection.
Its upper bound is (n-1)(s_J-1)-L(s_J-1)=Z_(s_J)-2s_J+2,
and w_J=u_J-2s_J<=Z_(s_J)-2s_J. Sizes are again at least2,
and total rank sum is unchanged. Hence this partition exists.
It is a minimizing successor leading to E(J)=0. Thus EVERY bad
state in the endpoint-hole family has SOME minimizing successor
that strictly improves,in fact reaches0 in one update.

### MI405 — B207 unexpected check: protected optimal choices can still cycle (2026-10-18 13:36 BST)

**Explicit hand counterexample to the STRONGER universal version.**
Take n12,R={0} union[3,13],sizes(3,3,6),targets(26,26,36).
Total88 is correct;singleton protected minima are9,9,27,and
pair minima are27,54,54,against actual sums52,62,62. All cuts pass.
A triple containing0 sums at most0+12+13=25. Therefore A and B
are bad zero owners;C is good. E(A)=E(B)=4 by MI404's error identity.

In state A the rank targets are22/20/24. The rank partition

```text
A={5,7,10}, B={0,9,11}, C={1,2,3,4,6,8}
```

has actual zero owner B. Its physical sums are28/24/36,so its
error4 is MINIMAL over the whole A fibre. In state B,swap A and B
in that displayed partition. Rank targets become20/22/24,actual
zero owner A,physical sums24/28/36,and error4 is again minimal.
Thus A<->B is a positive cycle of valid MINIMIZING choices within
the protected minimum3 domain. The universal strict-descent extension
suggested by MI403's finite test is REFUTED. This does not refute
the existential conjecture:the alternatives must be kept.

For a literal successful edge from A to C,use rank partition

```text
{3,8,11}/{4,6,10}/{0,1,2,5,7,9}, sums22/20/24.
```

It also has minimum error4,but its actual owner C has E(C)=0.
A literal physical solution at C is

```text
{3,10,13}/{5,9,12}/{0,4,6,7,8,11}, sums26/26/36.
```

Niggle sweep:all displayed subsets are disjoint and exhaust their
specified pools;rank and physical sums are distinguished. There are
only3 nested-count states because the thresholds COINCIDE. Minimum
error4 is proved from the owner identity and the maximum25,not
inferred from a sample. The two uses of MI295 have residual sizes
at least2;all complementary bounds follow from totals. Endpoint-hole
reflection is NOT imported:the protected-margin condition need not
survive reflection. The counterexample addresses the full protected
conjecture of MI403;no claim that this particular fixture passes the
additional original-parent legal-pivot gate. No computation or second
read is claimed;the general existential statement remains OPEN.

Gut verdict:the pull is more specific now. The surprising part is that
optimality still allows a cycle while a chosen owner supplies immediate
escape. A fresh choice favors understanding that ownership choice,not
another dynamics census. Reasoned:discard the universal quantifier;
retain existential descent,proved here only for bottom-adjacent holes.
Next cheap question:for separated thresholds,can one prescribe a
compatible pair of threshold counts by the same interval-bound argument,
or does the middle segment obstruct simultaneous ownership? Work on
that joint choice by hand;do not tune deterministic tie-breaks. G321
and MI399 reviews continue independently;full P_0/five-bin/E28/L8 OPEN.
13min heartbeat remains ACTIVE.

### MI406 — B208: separated bottom holes1,3 admit joint owners by hand (2026-10-18 13:46 BST)

**Complete hand candidate for this family;unreviewed,novelty unassessed.**
Question:does the endpoint-owner mechanism survive the first separation
of the two compression thresholds? Work on

```text
R=[0,n+1] minus{1,3}={0,2} union[4,n+1],
a,b,c>=3, a+b+c=n,
T=sum R=L(n)+2n-3,
u_J>=L(s_J)+2s_J for every proper nonempty group J.
```

The pull is toward prescribing owners before invoking the interval
base. The previous block's cycle cools the iteration route,but not
this joint-choice question. Record searched:`endpoint|two.interval|two.hole`
and `MI351|MI382|MI404|MI405|MI336`:29 hits/5 files.
Read G317's source scope:minimum4,arbitrary second hole,individual
spectra;the present minimum3 conclusion needs the stronger protected
cuts. G319 handles positive fixed counts on two intervals but is
pending review and not used here. Existing primary-literature pointers
in PRIOR-ART/MI402 retained;no new literature/novelty assertion.
No experiment,census or deterministic policy is run. This is a direct
existence argument,not a proof of MI403's general feedback conjecture.

For a bin of size s,write the bounds for its remaining tokens in the
single interval[4,n+1]:

```text
A_s=L(s)+4s,                 B_s=(n+1)s-L(s),
O_s=L(s)+3s-3,               Z_s=B_s-(n+2-s),
D_s=L(s)+2s-3,               W_s=B_s-2n+2s-3.

owns neither0 nor2:  [A_s,B_s]
owns0 only:          [O_s,Z_s]
owns2 only:          [O_s+2,Z_s+2]
owns both:           [D_s,W_s].
```

These are actual endpoint sums,not rounded estimates. Any assignment
of0 and2 for which each target lies in its displayed interval gives
a partition by reviewed MI295 PROVIDED every residual size is>=2.
Thus different owners are always allowed;one owner for both is allowed
only when that bin has s>=4. Total conservation is automatic after
removing the two special tokens. Protected cuts already give

```text
L(s)+2s<=u_i<=B_s-3.                                  (1)
```

Call a bin LOW when u_i<A_(s_i). Such a bin must receive at least
one special token. The following budgets select owners.

**1. A target below O_s forces an admissible double owner.**
If u_i<O_s,then s_i>=4,because at s3 the protected lower bound
is9=O_3. It can receive both tokens:the lower D_s is below (1),and

```text
W_s-(O_s-1)=(s-2)(n-s)+1>0.
```

No other bin can be low. For another size t,assuming u_j<A_t,
the upper sum (O_s-1)+(A_t-1) minus the protected pair minimum
L(s+t)+2(s+t) is

```text
s+2t-st-5=-(s-2)(t-1)-3<0.
```

That contradicts the pair cut. Give both tokens to i;the other two
bins receive neither and satisfy both interval bounds. This completes
this case. From now on all targets are at least their O_s.

**2. There cannot be three low bins.** If all are low,their total is
at most sum A_s-3,whereas

```text
T-(sum A_s-3)=ab+ac+bc-2n>=4n-27>=9.                  (2)
```

Here ab+ac+bc>=6n-27 follows by writing a,b,c as3 plus nonnegative
integers. At most one bin has u_i<O_s+2:two such targets sum to
at most (O_s+1)+(O_t+1),whose excess over the protected pair minimum
is s+t-st-4<0. Also ANY low bin is below its zero-owner upper bound:

```text
Z_s-(A_s-1)=(s-1)(n-s-2)-3>=5.                        (3)
```

If exactly two bins are low,give0 to one that fails the2-owner lower
bound,if there is one,and give2 to the other. If neither fails,choose
either orientation. Lower bounds hold by construction,upper bounds
by (3),and the third bin receives neither. All residual sizes are>=2.

**3. One low bin.** Call it A,size a. If a>=4 and u_A<=W_a,
give it both tokens. Its lower D_a follows from (1),and other bins
are not low. Otherwise give it0:O_a<=u_A and (3) give its bounds.
We need one of B,C to accept2. Their lower bounds hold because
u_i>=A_(s_i)>O_(s_i)+2. Suppose both refuse the upper bound,so
u_B>=Z_b+3 and u_C>=Z_c+3.

If a=3,the protected lower bound on A implies

```text
u_A+u_B+u_C-T
 >= [L(a)+2a]+[Z_b+3]+[Z_c+3]-T
 =bc-2a-b-c+5=(b-1)(c-1)-2>=2,                        (4)
```

contradicting the total. If a>=4,the unavailable double-owner option
means u_A>=W_a+1,and then

```text
u_A+u_B+u_C-T
 >=[W_a+1]+[Z_b+3]+[Z_c+3]-T
 =ab+ac+bc-3n+a+3>=3n+a-24>0.                        (5)
```

Again impossible. One of B,C therefore accepts2;the other needs neither.

**4. No low bins.** If a size>=4 bin satisfies u_i<=W_(s_i),give
it both tokens and finish. Otherwise at least one bin A accepts0:
if every u_i>=Z_(s_i)+1,their total exceeds T because

```text
sum Z_(s_i)+3-T=ab+ac+bc-2n>=9.                       (6)
```

Its lower bound follows from u_A>=A_a>O_a. For another bin to
accept2 we only need its upper bound. If both other bins refuse,
(4) applies when a3,and (5) applies when a>=4 because the double-owner
option was excluded. Thus a distinct2 owner exists. All bounds and
residual minimum sizes hold,and MI295 completes the interval partition.

This exhausts the owner choices without using a three-bin theorem on
a holed pool. Protected margin2 is used in (1),the pair contradictions,
and the total estimates;size3 is used to keep distinct-owner residual
sizes>=2 and to isolate the a3 alternative to the double-owner move.
The theorem proves completion for holes1,3,including size3 bins that
are outside G317. It neither proves the full protected two-hole claim
nor says a minimum-error iteration necessarily chooses these owners.

**Hand controls and unexpected check.** These literal partitions exhaust
their pools and have the indicated sizes/sums:

```text
Two low bins,n9,targets13/14/24:
 {0,4,9}/{2,5,7}/{6,8,10}.

Forced double owner,n10,sizes4/3/3,targets14/24/24:
 {0,2,5,7}/{4,9,11}/{6,8,10}.

One low size3 bin,n9,targets9/20/22:
 {0,4,5}/{2,8,10}/{6,7,9}.

No low bins,n9,targets15/18/18:
 {0,5,10}/{2,7,9}/{4,6,8}.
```

All proper protected cuts pass by direct sums. Unexpected check:
in the9/20/22 example,both special values in the first size3 bin
would leave a singleton7 and WOULD realize its target,but the other
residual sizes are3,3. That assignment cannot invoke MI295's minimum2
base. The displayed DIFFERENT-owner construction avoids this invalid
shortcut. This is a scope check,not a claim that every size1 residual
fails. The forced-double example instead leaves size2,as required.

Niggle sweep:the labels0/2 refer to values,not compressed ranks.
The two thresholds are distinct here (rank1 and rank2). Bounds for
both owners include the value2 exactly once;T has deficit3 relative
to L(n)+2n. Upper bounds from complementary protected cuts are B_s-3,
not B_s-2 from MI404. Each case assigns both exceptional values exactly
once,keeps residual sizes>=2,and has the right interval total. No
reflection,positive-count theorem,unproved low-shape result or physical
partition oracle is invoked. Hand derivations and controls only;
independent review and novelty remain outstanding.

Gut verdict:the live pull is the owner-budget argument;it becomes
clearer after abandoning a forced iteration. Reasoned:the first
separated-threshold boundary completes,but repeating an ever-longer
list of small exceptional prefixes would become the old catalogue
loop. Next ask whether the same owner-existence argument can consume
an arbitrary middle interval,using fixed count intervals and their
aggregate capacities. Keep the actual protected two-hole question
visible;do not automatically expand to holes1,4,1,5,etc. This checkpoint
can join Cloud's next combined read;no routine halt or new census.
G321/MI399 pending,full P_0/five-bin/E28/L8 OPEN,13min ACTIVE.

### MI407 — B209: arbitrary middle length has no protected aggregate-count obstruction (2026-10-18 14:01 BST)

**Hand PROOF-SKETCH,independent read and novelty assessment pending.**
Question:can the previous joint-owner argument handle arbitrary distance
to the second hole without a catalogue of exceptional prefixes?
Work on R=[0,M] minus{1,q},n=M-1=a+b+c,all sizes>=3,
and proper cuts u_J>=L(s_J)+2s_J. For an assumed zero owner A,
put r=(a-1,b,c) and split the positive pool into

```text
I=[2,q-1], P=q-2;
H=[q+1,M], Q=M-q;
P+Q=n-1.
```

The conclusion below is conditional only on the THREE scalar count
intervals being nonempty. It proves their aggregate capacity,not
existence of an eligible owner and not simultaneous partitioning at
chosen counts. G319's positive-count compatibility is not invoked.
Those remaining tasks are kept explicit.

Record searched:`endpoint|two.interval|two.hole` and
`MI351|MI382|MI404|MI405|MI336`:29 hits/5 files. Read MI393/395's
count-deficit algebra and MI383's warning about zero rows;G317's
minimum4 scope also reread. Existing primary-source orientation retained;
no external theorem or new literature claim. Initial pull:the gap between
the positive intervals is now one missing value rather than two,which
may shrink the deficit budget enough to avoid exceptional repairs.
No experiment or numerical domain expansion was run. This entry records
a hand derivation and a literal unprotected countercontrol.

For a remaining size r and high count k,write l=r-k. Its exact
scalar sum interval is [f_r(k),g_r(k)],where

```text
f_r(k)=2r+(q-1)k+L(r-k)+L(k),
g_r(k)=(q-1)(r-k)-L(r-k)+Mk-L(k).
K_i={max(0,r_i-P)<=k<=min(r_i,Q):f_(r_i)(k)<=u_i<=g_(r_i)(k)}.
```

Both endpoints strictly increase with k,so each nonempty K_i is
an integer interval. Assume total conservation and nonempty K_i.
We prove

```text
sum_i min K_i <= Q <= sum_i max K_i.                 (C)
```

under the protected cuts. Empty I or H makes (C) immediate because
each K_i has its sole forced count;below P,Q>=1.

**1. Classify an upper-count shortage without protection.**
Suppose k_i=max K_i sum to Q-D,D>=1,and put l_i=r_i-k_i.
Let J contain the bins with l_i>0,j=|J|. Every next count k_i+1
on J is legal and maximality gives u_i<=f_i(k_i+1)-1.
Put R_J=sum_J r_i=P+kappa,where
kappa=Q-sum_(i outside J) r_i. A high-only outside bin has target
at most its actual largest high-subset sum. Consequently

```text
u_J >= alpha(R_J)=2R_J+(q-1)kappa+L(P)+L(kappa).
```

For j3 this is total equality. Cases j<=1 are impossible because
sum l=P+D but a single low count cannot exceed P. If D>=j,
choose legal h_i>=k_i+1 with sum_J h_i=kappa. Their total low
count is P;superadditivity of L gives sum_J f_i(h_i)<=alpha(R_J),
contradicting u_J<=sum f_i(h_i)-j. Thus only(2,1),(3,1),(3,2)
need consideration. These statements do not assume joint realizability.

Write e=j-D and Cross(v)=sum_(i<h in J)v_i v_h. Direct expansion gives

```text
sum_J(f_i(k_i+1)-1)-alpha(R_J)
 =e(kappa+1)+e^2-Cross(l-1)-Cross(k+1)-j.             (1)
```

This is MI393/395's calculation with gap2 in place of gap3;the
constant is changed,not their conclusion imported.

For j2,D1,write x,y for the two k entries and t,w for l-1.
The right side of(1) is exactly -xy-tw. A shortage requires
xy=tw=0. Since both remaining sizes are>=2,this forces,up to
exchange,x=0,w=0,t>=1,y>=1. The first bin owns the ENTIRE low
interval and has no high values. Its scalar target is therefore its
single possible low sum. Its next-count upper bound f_P(1)-1
is that sum PLUS1:replacing the largest low by the smallest high
costs2. Thus at least one unit is lost from the upper bound(1),
which was already0. This contradicts u_J>=alpha(R_J).
This excludes j2 without any protected-cut assumption.

For j3,D2,put x=k,t=l-1. Substituting sum x=Q-2 in(1) gives
-Q-Cross(x)-Cross(t)<0. Only j3,D1 remains. Here

```text
sum x=Q-1, sum t=P-2,
x_A+t_A=a-2>=1,
x_B+t_B=b-1>=2, x_C+t_C=c-1>=2,
0 <= sum_i(f_i(k_i+1)-1)-sum(R)
   =2-Cross(x)-Cross(t).                            (2)
```

**2. Exhaust the budget2 by its zero supports.**
All three x positive would give Cross(x)>=3. If x_A=0 and both
nonroot x are positive,put t_A>=1. If x_B=x_C=1,then t_B,t_C>=1
and the cross total is>=4. If one x is>=2 and the other1,the
latter requires its t>=1,giving cross total>=3. If both x>=2,
Cross(x)>=4. So this support is impossible.

If exactly one nonroot x is zero,say x_B=0,then t_B>=2 and
x_A,x_C>=1. The budget forces t_A=t_C=0,otherwise Cross(t)>=2
in addition to Cross(x)>=1. Thus x_A=a-2>=1,x_C=c-1>=2;
(2) forces x_A=1,x_C=2,a=c=3. Write t_B=b-1>=2.
The cross total is exactly2,so conservation forces equality in
EVERY next-count upper bound. This gives precisely

```text
sizes (a,b,c)=(3,b,3), b>=3;
P=b+1,Q=4,q=b+3,M=b+7;
targets (u_A,u_B,u_C)=(2b+8, L(b)+2b+2, 3b+14).       (Fmax)
```

With two zero x entries,they cannot be B and C because
Cross(t)>=4. If they are A and B,then t_A>=1,t_B>=2.
The budget forces t_A=1,t_B=2,t_C=0,a=b=3,x_C=c-1>=2.
Thus P5,Qc and the high interval starts8. Equality in(2) would
force u_C=sum(H)-1. But C at its claimed maximum k_C=c-1
must replace the smallest high value8 by a low value at most6,
so its scalar upper bound is sum(H)-2. Its K_C would be empty,
contrary to hypothesis. The A,C-zero case is identical. Three
zero entries also violate the budget. This exhausts every support.

Hence (Fmax),up to interchanging the two nonroot labels,is the
ONLY possible upper-count shortage among nonempty K systems in
this family,even without protection. It is a real scalar failure:
A can use one high (b+1)+(b+7),but two highs already exceed u_A;
B uses all low values EXCEPT b,but one high already exceeds u_B;
C uses (b+1)+(b+6)+(b+7),but three highs already exceed u_C.
Their maxima are1,0,2,whose sum3 is below Q4.

Under protection (Fmax) is impossible. Its A+B target sum minus
the protected cut for original size b+3 is

```text
[2b+8+L(b)+2b+2]-[L(b+3)+2(b+3)]=1-b<0.             (3)
```

This proves the upper inequality of(C) for every eligible owner.

**3. Reflect only the positive pool to classify lower-count excess.**
Reflect v to M+2-v. This exchanges P,Q and replaces q by
q*=M+2-q. The rooted sizes remain r=(a-1,b,c),the targets become
u*_i=r_i(M+2)-u_i,and K*_i=r_i-K_i. A minimum-count excess in
the original system is exactly a maximum-count shortage in this
reflected system. We apply the UNPROTECTED classification above;
we do not assume the protected margin survives reflection.

Reflecting (Fmax) back gives the only possible minimum-count failure:

```text
sizes (3,b,3), b>=3;
P=4,Q=b+1,q=6,M=b+7;
targets (u_A,u_B,u_C)=(10, L(b)+8b-2, 13).            (Fmin)
```

But A+C totals23,below L(6)+2*6=27. Thus the ORIGINAL protected
pair cut excludes it. This proves the lower inequality of(C).
Both reflected targets and the use of remaining root size2 rather
than original size3 are essential to this calculation.

**Unexpected hand countercontrol:scalar eligibility alone is insufficient.**
At b3,(Fmax) gives R=[0,10] minus{1,6},sizes3^3,targets14/11/23,
with A as assumed zero owner. Its positive intervals are2..5 and7..10.
Explicit independent scalar choices are A=4+10,B=2+4+5,C=4+9+10.
The three K are nonempty and their maximum high counts are1,0,2;
Q4 cannot be reached. All singleton protected lower bounds9 pass,
but A+B=25 violates the pair lower bound27. This demonstrates why
the pair inequalities in(3) cannot be dropped or replaced by scalar
membership. The whole target nevertheless has the literal partition

```text
{3,4,7}/{0,2,9}/{5,8,10}, sums14/11/23.
```

The failed root is A;the successful partition puts0 in B. There is
no claim that failed rooted count admission forbids global existence.
The reflected b3 control has targets10/25/13 and minimum high counts
1,3,1,exceeding Q4;its failing protected pair is A+C=23. No physical
partition claim is needed for that control. These are hand identities,
not a new numerical test or a computed finite census.

**Scope and next obstruction.** Whenever an owner has nonempty K_i,
(C) permits integer choices k_i in K_i with sum Q;then low counts
sum P. This solves the aggregate scalar-count constraint at EVERY
middle-interval length for holes1,q. It does not establish that some
owner is eligible;one-hole scalar gaps must still be treated,especially
when the root has remaining size2. Nor do these admitted individual
sum intervals establish simultaneous disjoint partitioning:G319 handles
positive rows only,and the zero-row boundary needs its own argument.
General holes p,q,full P_0/five-bin/E28/L8 remain OPEN.

Niggle sweep:all next counts are legal because a low token remains
and sum k<Q;nonempty K supplies actual scalar upper bounds. The
j2 equality has a strict one-unit loss which must not be omitted.
The two-zero j3 pattern is killed by scalar NONMEMBERSHIP,not by an
assumed joint construction. Reflection acts on positive values and
remaining cardinalities,not on0 or the original protected inequalities.
Every possible x-zero support is included;the infinite b parameter
in(Fmax)/(Fmin) is retained. Both failures are excluded by actual
original pair cuts. No dependency on pending G319/G321/MI399 or
W318,no experiment,no independent verification or novelty claim.

Gut verdict:the arbitrary-length calculation has more pull than a
sequence of small-prefix cases. It explains exactly where protection
is spent and removes an entire count-capacity obstacle without a
new exceptional repair list. Reasoned:one part of joint selection is
settled by hand;owner eligibility and disjoint compatibility remain.
Next handle scalar owner existence for holes1,q,including the size2
root gaps,before claiming a partition theorem. No routine review halt;
include this uniform argument in Cloud's next combined read.13min ACTIVE.

### MI408 — B210: an eligible zero owner exists for every protected holes1,q target (2026-10-18 14:13 BST)

**Hand PROOF-SKETCH,not independently verified.** Use MI407's pool
R=[0,M] minus{1,q},2<=q<=M,n=M-1=a+b+c>=9,sizes>=3,
total T,and all proper protected cuts u_J>=L(s_J)+2s_J.
Put V=R minus{0}=[2,M] minus q,m=n-1. Write alpha_r,beta_r
for V's least/greatest r-subset sums. A bin of size s is nonroot-
eligible if u is an actual s-subset sum in V,and root-eligible if
it is an actual(s-1)-subset sum. We prove there is an owner j
which is root-eligible,with every other bin nonroot-eligible.

Record searched:`owner|eligib` AND `MI391|MI407|G317`:22 hits/3 files.
Read G317's owner argument,MI391's scalar method,MI407 and the exact
one-hole scalar lemma (FOUR-BIN-PARTITIONS section2),including size2.
The existing literature orientation is unchanged;no novelty or new
source claim. Initial pull:the former minimum4 proof may be sharpened
by actual top sums rather than a coarse uniform lower bound. Unease:
root eligibility is NOT just u<=beta_(s-1),because an upper pair gap
can survive the protected cuts. No experiment is run.

**1. Locate failures without discarding the gaps.** Every scalar
cardinality used is>=2 and its V-complement is>=5. The reviewed
one-hole lemma says that the only possible missing sums between
alpha_r,beta_r are alpha_r+1 and beta_r-1. It applies at r2 too.
Endpoint deletion leaves an interval and has no exceptional gaps.

For a bin of original size s,put t=n-s>=6. Since the least t values
of R are0 plus the least t-1 values of V,

```text
beta_s=T-alpha_(t-1),
alpha_(t-1)<=L(t-1)+3(t-1)=L(t)+2t-2.
```

The complementary protected cut therefore gives u<=beta_s-2.
Nonroot failure can occur only below the minimum or at its lower gap:

```text
not nonroot-eligible => u<=alpha_s+1<=L(s)+3s+1.     (1)
```

For a proposed root,alpha_(s-1)<=L(s)+2s-2. Protection puts u
at least2 above this minimum,excluding its lower gap. Thus

```text
not root-eligible => u>=beta_(s-1)-1.               (2)
```

This deliberately retains the possible upper gap.

**2. A bin needing0 is unique and can receive it.** Two nonroot
failures of sizes a,b would,by(1),have total at most
L(a)+L(b)+3(a+b)+2,below their protected pair lower bound because

```text
a+b+2-ab<=-1, for a,b>=3.
```

There is at most one. For any s,t=n-s>=6,the top values of V give
beta_(s-1)>=(s-1)(M-1)-L(s-1),whereas alpha_s<=L(s)+3s.
Consequently

```text
beta_(s-1)-alpha_s >= (s-1)(t+1)-3s >=4s-7>=5.      (3)
```

A failed nonroot target is at most alpha_s+1,so it is at least4
below beta_(s-1);its root lower gap was already excluded. It is
therefore root-eligible. Choose this unique failed nonroot if it exists.

**3. If all are nonroot-eligible,some root is eligible.**
Let r_i=s_i-1>=2;sum r_i=m-2. The sequence beta_r is concave,
being partial sums of the positive values in decreasing order.
Moving a unit from a smaller coordinate>=3 to a largest coordinate
cannot increase the sum of beta values. Concentrating at the boundary
therefore gives

```text
sum_i beta_(r_i) >= beta_(m-6)+2 beta_2
                 = T-alpha_6+2 beta_2.            (4)
```

If q<=M-2,then beta_2=2M-1 and alpha_6<=33. Since M>=10,
2 beta_2-alpha_6-3>=4M-38>=2. If q=M-1,then beta_2=2M-2
and alpha_6=27,giving at least4M-34>=6. If q=M,then
beta_2=2M-3,alpha_6=27,giving at least4M-36>=4.
In EVERY case sum beta_(r_i)-3>T. Three failures in(2) would
force sum u_i>T,contradicting conservation. Some root is eligible.
Together with section2,this completes the owner-existence proof.

**Hand controls.** On M10,q5,sizes3^3,targets10/19/20,the first
nonroot target is the exact gap10 between triples9 and11 of V.
It must own0;the partition
{0,2,8}/{3,6,10}/{4,7,9} witnesses its eligibility and the full target.
On M10,q8,targets18/14/14,the first target is below beta_2=19
but cannot be a pair in V:18 is the upper pair gap. All protected
cuts pass. A different owner works:
{2,6,10}/{0,5,9}/{3,4,7}. This is the unexpected check against
silently replacing root eligibility by an extremal inequality.
For M10,q2,the smallest margin in(4) is attained:
2 beta_2-alpha_6-3=38-33-3=2. These are literal hand checks.

Combining this hand lemma with MI407 gives some zero owner AND
integer high counts with the correct total for arbitrary q. This is
scalar count admission only. Disjoint compatibility is addressed next,
not presumed from independent subset examples.

### MI409 — B210: protected holes1,q complete after two uniform compatibility repairs (2026-10-18 14:13 BST)

**Complete COMPOSITE HAND CANDIDATE G322;conditional on pending G319
and the fixed-count reduction below. Independent verification and novelty
remain outstanding.** Statement:three sizes>=3 on[0,M] minus{1,q}
admit prescribed integer targets totaling the pool whenever every proper
group target is at least L(s_J)+2s_J. No least-slack assumption. The
second hole q is arbitrary;the first hole remains1. This is not a
claim about arbitrary p,q,full P_0 or full five-bin sufficiency.

MI408 supplies a scalar-eligible zero owner;MI407 supplies counts
in the low interval I=[2,q-1] and high interval H=[q+1,M] that
meet all individual sum bounds and both count totals. Their remaining
sizes are all>=2. If I or H is empty,reviewed MI295 completes the
single interval directly. Otherwise apply the following fixed-count
reduction,whose argument is MI378/MI383 section1 with offsets2,q+1.

For two positive count rows,G319 is the pending compatibility input.
For two regular rows (each at most two positive counts,or all three
counts>=2),MI378 splits the targets into integer row sums by interval
bounds,then applies reviewed MI295 or binary subset completeness.
If one row has two positive counts and the other is nonregular,a
single low-row gap is repaired by shifting its singleton value by1
and compensating in the binary other row. If two singleton values
coincide,shift them to neighbours in opposite directions. The binary
row's interval has width at least1,so one direction is available.
These moves change sums within rows at FIXED counts;the different
absolute interval offsets do not enter the argument. Thus the generic
zero-row argument carries unchanged,without importing protection from
the old three-hole setting. Its source is unreviewed MI383 section1.

The only remaining fixed-count failure shape is:one bin X owns a
WHOLE interval and exactly one value of the other. In that other
interval the other bin counts are d,e>=2. A failed split must be
one bin's minimum+1,with the omitted value at index d;the upper gap
is the other bin's lower gap by complementation. Individual bounds
and total imply the actual one-hole extrema,not just full-row extrema.
We repair both orientations explicitly.

**1. X owns all high values and one low value.**
Here P=1+d+e,q=P+2,and the omitted low value is d+2. Call the
failed bin D,with d remaining low tokens,so u_D=L(d)+2d+1;
call the other bin E. Necessarily0 belongs to X. Otherwise the
ORIGINAL size of D union E is P,and

```text
u_D+u_E=sum(I)-(d+2)<L(P)+2P,
```

contradicting its protected pair cut. Thus D,E are nonroots and
d,e>=3,while X has original size Q+2. Keep all high values in X,
move0 to D,and assign

```text
X low values: {2,d};
D: {0} union ([3,d+1] minus{d}) union {d+3};
E: all remaining low values.
```

The X low sum is d+2,its former low sum plus0. D has d values;
the sum of3..d+1 is L(d)+2d-2,and replacing d by d+3 adds3.
Its target is exactly L(d)+2d+1. Values are distinct and present:
d>=3 and d+3<=d+e+2=q-1. E has e values and the correct sum
by conservation. All original sizes are preserved. This repair uses
no pending theorem,no high-row changes and no small-case table.

**2. X owns all low values and one high value.**
Write Q=1+d+e and M=q+d+e+1. The omitted high value is q+1+d,
so,with the same naming,

```text
u_X=L(q)+q+d,
u_D=d(q+1)+L(d)+1.
```

If0 belongs to X or D,the original size of their union is q+d,
but direct subtraction gives

```text
u_X+u_D-[L(q+d)+2(q+d)]=1-q<0.
```

Therefore0 belongs to E. Now X is a nonroot of size q-1>=3,
so q>=4;D has d>=3;E has original size e+1>=3. Change counts,
keeping0 in E:give X two highs and one fewer low,and give D one
low and one fewer high. In order X,D,E the new rows are

```text
low:  (P-1,1,0),
high: (2,d-1,e).
```

The low row is binary,the high row has every count>=2. Both are
regular. Their combined extrema compared to the unchanged targets are

```text
X: f_new-u_X=3-d<=0,
   g_new-u_X=2M-q-d-4=q+d+2e-2>0;
D: f_new-u_D=1-q-d<0,
   g_new-u_D=(d-1)(e+1)-3>=3.
```

E is unchanged. MI378's integer row-sum splitting and reviewed MI295
therefore complete these new counts. In contrast to the earlier gap3
case,this repair already works at d3:there is no residual thin table.
The formula is derived for the gap2 pool itself,not transferred by
an unproved reflected protection assumption.

**Literal protected controls.** Whole-high obstruction,then repair:
M11,q9,sizes(X,D,E)=(4,3,3),targets26/10/20. The old fixed
X={0,5,10,11} leaves D at the low triple gap10. The repair is

```text
{2,3,10,11}/{0,4,6}/{5,7,8}.
```

Singleton protected bounds are14/9/9;pair bounds35/35/27,against
sums36/46/30. Whole-low obstruction at the smallest d:
M10,q4,sizes3^3,targets13/19/18. The old X={2,3,8} leaves D
at its high triple gap19. The new regular-count partition is

```text
{2,5,6}/{3,7,9}/{0,8,10}.
```

All pair sums32/31/37 exceed27. Each displayed partition exhausts
its pool. These hand controls check both changed-root and fixed-root
repairs;no computational experiment was performed.

**Assembly and limits.** MI408 guarantees an individually eligible
owner,MI407 guarantees aggregate count capacity,and interval interpolation
chooses the integer counts. G319/MI383 handle generic fixed-count shapes;
the two repairs above handle their only exceptional shape. Consequently
the protected holes1,q theorem has a complete source-level candidate.
The carrying dependency G319 is still unverified;MI378/MI383 and the
new MI407-409 arguments also require independent reading. Reviewed
MI295 and the one-hole scalar lemma are the established bases. Neither
G321,MI399,W318 nor the general protected two-hole claim is used.

Niggle sweep:scalar upper pair gaps were retained in MI408;rooted
cardinalities never silently stay at their original values;the total
budgets cover q2 and qM. In the whole-high failure,the D+E pair cut
forces0 into X before asserting d,e>=3. In the whole-low failure,the
X+D pair cut forces0 into E before invoking d-1>=2. Every new count
row has its original size and correct interval totals. The full-interval
base is never applied at size1. Generic thin positive rows remain an
explicit pending G319 dependency. No experiment or novelty claim.

Gut verdict:the pull remains specific:the uniform argument now closes
the owner and count constraints and the two actual incompatibilities;
it is not warmed by another finite census. Reasoned:send one combined
carrying checkpoint for this whole family,folding it into G319's pending
read. Continue independently on the scope gap:arbitrary first hole p
rather than1,or its actual parent restrictions. Do not treat this family
as all two-hole pools. Full P_0/five-bin/E28/L8 OPEN,13min ACTIVE.

### MI410 — B211: a bounded-hole least-singleton deletion completes the protected two-hole target (2026-10-18 14:30 BST)

**Hand conditional implication,UNREVIEWED;not a general two-hole theorem.**
Let S=[0,M] minus{p,q},0<p<q<M,with three sizes>=3 and integer
prescribed sums totaling sum(S). Assume every proper group satisfies
u_J>=L(s_J)+2s_J. Suppose A,size a,is globally least for
u_J-L(s_J)-2s_J,and SOME realization of A leaves at most three
holes after trimming/translation. Then a full partition exists,
conditional on MI371/W318. The original realization may be changed
in the exceptional six-token case. This is not rooted sufficiency.

Question for this block:what precisely changes when the first hole
moves away from1? Record searched:`hole.moving|move.the.hole|first.hole|
three.intervals|rooted` AND `protected|MI364|MI400|G322`:18 hits/2 files;
then `two.hole|punctured` AND `adjacent|descent|swap|energy`:14 hits/5 files.
Read MI335,MI355/357,MI368,MI371/373/374 and the pending W318 source.
These supply the existing elementary/known interval ingredients;
no new literature result or novelty claim is imported. No experiment.
Hand block began13:23 UTC;the mathematical record follows the work.

Initial pull:an arbitrary first hole may require a new representation,
not a longer list of initial exceptions. Unease:the owner/count success
for holes1,q does not license arbitrary p. Moving p left by1 and raising
one target by1 gives a protected instance on the new pool,but its solution
need not put the changed token in that chosen bin. This is an unresolved
rooting problem,not an induction proof. The earlier feedback cycles and
MI364 are enough reason not to assert it. No new feedback run is opened.
Instead test the exact deletion hypothesis against the actual protected
family. Counterfactual:one eligible singleton with every realization
leaving four holes would defeat that selector,but not partition existence.
The unexpected check is the six-token exception after a legal pivot.

**1. All nonexceptional remainders.** MI368 gives remaining margin
mu'=a+2-b=h'+(M-c)>=h',where b,c are the actual remaining endpoints
and h' the actual normalized hole count. MI371 completes h'<=3 when
at least seven values remain,and h'<=2 also with six. With six values
and h'=3,MI373 leaves only

 R0={0,2,3,5,6,8} or {0,1,2,6,7,8}, targets12,12.

Each other bin then has size3. Its target12 and mu'>=3 force
mu'=3,c=M and b=a-1. The span is8,so M=a+7 and the two original
targets are both3a+9. Put w=p+q. Total conservation gives

 u_A=L(a+8)-w-2(3a+9)=L(a)+2a+10-w.

Protection therefore forces w<=10. This equality argument keeps
the original lower orientation;no reflected protection is assumed.

**2. Repair the terminal case.** In the nine-value block[b,b+8],
the only possible ORIGINAL holes lie at b+{1,4,7} for the first
exception,or b+{3,4,5} for the second. If at most one original hole
lies in that block,partition the FULL block formally into

 b+{0,4,8}, b+{1,5,6}, b+{2,3,7}.

All three triples sum3b+12=3a+9. At least two triples avoid the
original holes. Give those two to the other bins and give A every
remaining AVAILABLE value of S. Cardinality and total conservation
supply A's required size and sum. We do not put a missing token in A:
the formal third triple is only a device for selecting the two good ones.
This is the existing nine-value equal-sum construction,not a novelty claim.

If BOTH original holes lie inside the block,the first exception gives
w>=2b+5 and the second w>=2b+7. Since b=a-1>=2 and w<=10,
the only possibility is b2,a3 and original holes{3,6} in the first
exception. The targets are10/18/18,on [0,10] minus{3,6}. A literal repair is

 {0,2,8} / {1,7,10} / {4,5,9}.

The potentially failed deletion is A={0,1,9};its remaining normalized
pool is R0={0,2,3,5,6,8}. Thus the terminal repair is needed even
for a legal prefix/pivot choice. The original adjusted slacks are
singles1,9,9 and pairs1,1,9;A is globally least,with ties retained.
This completes the stated implication. It covers EVERY legal
prefix/suffix/pivot realization,which leaves at most three holes,
when its selected singleton has the required global minimum.
It does not assert that such a legal recipe or singleton always exists.

### MI411 — B211: four holes are unavoidable on an actual protected legal-pivot descendant (2026-10-18 14:30 BST)

**Exact hand countercontrol to the selector,not to existence.**
Take S=[0,10] minus{2,8},sizes3/3/3,targets9/18/18. Total45 is
correct. Adjusted slacks at margin2 are singles0,9,9 and pairs0,0,9.
A is globally least (tied with its two containing pairs).
Its COMPLETE size3/sum9 realization list is

 A1={0,3,6}, A2={0,4,5}, A3={1,3,5}.

Starting0 requires a pair9:18 is blocked by8,27 by2,and36/45
are the two available choices. Starting1 requires pair8:26 is
blocked by2,35 works. Starting at least3 already totals at least12.
This proves exhaustiveness without a search program.

The corresponding complements,normalized at their actual minima,are

 A1: {0,3,4,6,8,9}, four holes{1,2,5,7};
 A2: {0,2,5,6,8,9}, four holes{1,3,4,7};
 A3: {0,4,6,7,9,10}, five holes{1,2,3,5,8}.

There is NO realization of this selected bin leaving at most three
holes. Nevertheless a full partition is

 {0,3,6} / {1,7,10} / {4,5,9}, sums9/18/18.

Its A1 remainder has shifted targets15/15 and margin4;the first
triple is0+6+9 and the other3+4+8. Thus the very first four-hole
obstruction to the selector is positive and demands a scalar repair,
not a numerical extension of the old three-hole lemma. A formal
k0 canonical choice would be{0,1,8};8 is the missing pivot.

**Actual parent,not an unrelated hole pool.** In P=[0,12] minus4,
four triple targets11/15/24/24 satisfy the margin1 cuts. Their
single slacks are5,9,18,18;pair slacks5,14,14,18,18,27;triple
slacks5,5,14,18,in lexicographic subset order. D={0,1,10} is
a legal globally least singleton. Removing it and subtracting2
gives exactly S and9/18/18. In turn this parent is an actual
five-bin descendant on the FULL interval[0,14]:remove{0,1,6},
then subtract2. The five triple targets are7/17/21/30/30.
For groups of1,2,3,4 bins their minimum possible target sums are
7,24,45,75,above the rank bounds3,15,36,66. The first singleton
has slack4;every larger group's slack is at least9,so it is
indeed globally least. A full witness is

 {0,1,6} / {2,3,12} / {4,7,10} / {5,11,14} / {8,9,13}.

This establishes the obstruction inside the intended five-bin chain.
The intermediate parent and inner singleton have ties;neither is
misreported as a unique minimizer.

**What changed and next step.** MI410 conditionally completes the
legal-pivot/global-least-singleton branch for arbitrary first hole,
including its only small terminal repair. MI411 shows the remaining
missing-pivot issue cannot be removed by promising a different
three-hole realization of that same singleton. It is a sharp change
in required geometry,not a failure of the target conjecture.
Next inspect the actual FOUR-hole two-bin remainder from a repaired
missing pivot,using its margin and endpoint structure. Do not reopen
an unrestricted four-hole census or assume pair-minimum parents have
been handled. Pending G322/G319 and W318 keep their separate scopes.

Niggle sweep:the nine-value repair uses only two intact triples,so no
missing token is assigned;w<=10 follows from the selected target's
own cut;both exceptional normalized pools and all a>=3 are covered;
the lower singleton hypothesis is not manufactured by reflection;
MI411 lists every sum9 triple;all three complements,all parent cuts,
and the full five-bin witness check by hand. No experiment or theorem
promotion. No separate PROOFS filing or carrying-review request.

Gut:the direct hole-sliding idea is tepid because it merely recreates
rooting. The exact geometric boundary is more interesting:the cheap
selector is now decisively ruled out on an actual instance,and the
remaining positive four-hole example shows what a repair must preserve.
Reasoned:continue on that concrete scalar obstruction,not on another
blind feedback policy. This is a trajectory adjustment within a live
question;no routine review halt.13-minute heartbeat ACTIVE.


### MI412 — B212: protected four-hole triple splitting,with one exact exception (2026-10-18 14:47 BST)

**Complete hand PROOF-SKETCH,UNREVIEWED.** Put L(r)=r(r-1)/2.
Let S=[0,M] minus H,where H consists of FOUR INTERNAL holes,so
both endpoints are present. Let |S|=3+t with t>=3. For integers
u+v=sum(S),u>=15 and v>=L(t)+4t,a triple of sum u exists,EXCEPT
when M=9,H={1,2,3,7},and u=v=16. Endpoint holes are handled by
trimming and the earlier <=3-hole result,not added to this exception list.

Block began13:36 UTC. Question:can the actual four-hole remainder
from MI411 be completed using inherited protection? Record searched:
`four.hole|missing.pivot` AND `protected|MI411|margin`:16 hits/2 files.
MI359's generic repair,MI368's invariant,MI371/373/374,the W318 source,
and FOUR-BIN-PARTITIONS section6's canonical recipe were read. Existing
elementary pair/window ingredients are reused;no external theorem or
novelty claim is imported. This is a hand block,no experiment or census.

Initial pull:MI411's positive four-hole remainder points to a real
scalar boundary rather than another feedback policy. Unease:protection
may still leave a six-token exception,and deleting a chosen bin is not
itself a proof of a suitable geometry. Prediction:the size3 branch can
be resolved by partner pairs and the parent's hole-sum budget.
Counterfactual:a protected scalar obstruction must be retained,not
called a partition counterexample for its parent. Unexpected check:
the six-token four-hole pool below DOES fail,unlike MI411's pool.
Independent hand controls:literal triples/complements,actual endpoint
trimming,and the earlier five-bin witness;stop at the named branch,
not at an unrestricted four-hole classification.

**1. A four-deletion triple window.** After ANY at most four deletions
from[0,11],each sum15,16,17,18 survives. For sum15,if4 survives,the
five disjoint pairs of sum11

 (0,11),(1,10),(2,9),(3,8),(5,6)

cannot all be hit. Thus a blocker must delete4. The corresponding
five pairs for anchor5 are(0,10),(1,9),(2,8),(3,7),(4,6),forcing5.
For anchor6,the pairs(0,9),(1,8),(2,7),(4,5) leave three untouched
pairs after deleting4,5;only two further holes remain,so6 is forced.
For anchor3,the pairs(1,11),(2,10),(4,8),(5,7) leave two untouched
pairs and only one further hole,forcing3. But holes{3,4,5,6} leave
the triple{0,7,8} of sum15. Contradiction.

For sum16,anchor5 has five disjoint pairs
(0,11),(1,10),(2,9),(3,8),(4,7),forcing5. Anchor6 has four pairs
(0,10),(1,9),(2,8),(3,7),all avoiding5,forcing6. Anchor4 has pairs
(1,11),(2,10),(3,9),(5,7);three remain after5,6,forcing4.
Anchor7 has pairs(0,9),(1,8),(3,6),(4,5);two remain after4,5,6,
forcing7. But{2,3,11} survives holes{4,5,6,7} and sums16.
Reflection x->11-x supplies17,18. Sliding the twelve-value window
through[0,M],M>=11,gives intervals[3j+15,3j+18],with consecutive
intervals meeting. Thus EVERY triple sum in[15,3M-15] survives
any four deletions. No finite computation supplies this assertion.

**2. The protected upper tail when M>=11.** Write w=sum(H),so
w>=10,t=M-6. The complementary protected bound gives

 u<=M(M+1)/2-w-[L(M-6)+4(M-6)]=3M+3-w.

Only u>3M-15 remains after section1. Reflect the DESIRED triple,
not the protected system:delta=3M-u obeys

 7<=w-3<=delta<=14,  w<=delta+3.

The reflected holes H*={M-h:h in H} do not contain0 or M.
It suffices to take0 plus an available positive pair of sum delta.
For delta7,w<=10 forces H={1,2,3,4},and the pair3,4 survives H*.
For delta8,w<=11 implies max(H)<=5,and the pair3,5 survives.
For delta9,w<=12 implies H*>=5. To hit all four pairs
(1,8),(2,7),(3,6),(4,5) requires H*={5,6,7,8},which would give
w=4M-26>=18,a contradiction. For delta10,w<=13 implies H*>=4.
Hitting(1,9),(2,8),(3,7),(4,6) forces9,8,7 and4 or6 into H*;
then sum(H*)<=30,so w>=4M-30>=14,again impossible.

For delta11,12,13 there are five disjoint positive pairs,already
inside[1,11]:respectively

 1/10,2/9,3/8,4/7,5/6;
 1/11,2/10,3/9,4/8,5/7;
 2/11,3/10,4/9,5/8,6/7.

Four holes cannot hit them all. For delta14 and M>=12,use
2/12,3/11,4/10,5/9,6/8. If delta14,M11,the four pairs
3/11,4/10,5/9,6/8 either leave a pair,or force H* to contain3
and one value from each other pair. In the latter case1,2,11
all survive and themselves form a triple of sum14. Reflection
back completes every protected target for M>=11.

**3. The seven-token boundary M10.** Here t4,and protection implies
15<=u<=23,w<=33-u. Endpoints0,10 survive. The following arguments
exhaust the nine integer possibilities;groups denote disjoint sets
in which a blocking hole is forced.

- u15:triples(0,5,10),(0,6,9),(0,7,8),(1,4,10),(2,3,10)
  force five disjoint groups{5},{6,9},{7,8},{1,4},{2,3},impossible.
- u16,w<=17:triples(0,6,10),(0,7,9),(1,5,10),(2,4,10) force
  {6},{7,9},{1,5},{2,4}. Minimum weight16;any alternative adds
  at least2. The only possible blocker H={1,2,6,7} leaves{3,4,9}.
- u17,w<=16:triples(0,7,10),(0,8,9),(1,6,10),(2,5,10) force
  {7},{8,9},{1,6},{2,5},whose minimum weight18 is too large.
- u18,w<=15:triples(0,8,10),(1,7,10),(2,6,10),(3,5,10) force
  {8},{1,7},{2,6},{3,5}. Minimum14;each alternative adds>=2.
  The only possible blocker H={1,2,3,8} leaves{4,5,9}.
- u19,w<=14:triples(0,9,10),(1,8,10),(2,7,10),(3,6,10) force
  {9},{1,8},{2,7},{3,6},minimum15,too large.
- u20,w<=13:max(H)<=7. Triples(1,9,10),(2,8,10),(3,8,9)
  force1,2,3;the fourth hole h is4,5,6 or7. For h4 use{5,6,9};
  for h6 use{4,7,9};for h5 or7 use{4,6,10}.
- u21,w<=12:max(H)<=6. Triples(3,8,10),(4,7,10),(5,7,9)
  force3,4,5;adding any fourth positive hole gives w>=13.
- u22,w<=11:max(H)<=5,so{6,7,9} survives.
- u23,w<=10:H={1,2,3,4},so{6,7,10} survives.

Each displayed surviving triple has the required sum. Its complement
has size4 and sum v by conservation.

**4. The six-token boundary M9.** Both sizes are3,so relabel to
u<=v. Then15<=u<=17 and w<=45-2u. For u15,w<=15,the triples
(0,6,9),(0,7,8),(1,5,9),(2,4,9) force groups
{6},{7,8},{1,5},{2,4},minimum16:impossible. For u16,w<=13,
the triples(0,7,9),(1,6,9),(2,5,9),(3,4,9) force
{7},{1,6},{2,5},{3,4},minimum13. Equality forces
H={1,2,3,7},leaving S={0,4,5,6,8,9} and u=v=16.
There is no sum16 triple:starting0 would require7+9 or8+8;
starting4 requires5+7 or6+6;starting>=5 totals at least19.
For u17,w<=11,the triples(0,8,9),(1,7,9),(2,6,9),(3,5,9)
force{8},{1,7},{2,6},{3,5},minimum14:impossible.
This proves both sufficiency elsewhere and the exact stated exception.


### MI413 — B212: least-singleton geometry and repair close the other-triple branch (2026-10-18 14:47 BST)

**Complete CONDITIONAL HAND CANDIDATE,UNREVIEWED.** Let
S=[0,M] minus{p,q},0<p<q<M,with three bin sizes>=3,integer
prescribed sums,total conservation,and every proper group satisfying
u_J>=L(s_J)+2s_J. Suppose A,size a,is a GLOBAL minimizer of
u_J-L(s_J)-2s_J among proper groups,and at least one of the
OTHER two bins has size3. Then a full partition exists,conditional
on MI410/MI371/W318. No requirement that A's first realization be
kept. Neither a globally minimal singleton's existence nor the
case where both other sizes exceed3 is asserted. In particular,
this is not a general protected two-hole or five-bin theorem.

**1. A realization leaving at most four holes always exists.**
Put t=|S|-a>=6 and n=a+t=M-1. Use l actual smallest values,
k actual largest values,l+k=a-1,and one formal middle pivot.
For successive k,the continuous INTEGER pivot ranges meet at
the same actual extremal a-set. Their union is the full interval
between the sums of the a smallest and a largest actual values.
Protection places u_A in that interval:each i-th smallest value
is <=i+2,and the complementary cut bounds the top endpoint.
Thus a formal recipe exists. If its pivot is available,it leaves
at most the two original holes plus one deleted pivot:MI410 applies.

Otherwise call the missing pivot p and the OTHER original hole q;
in this paragraph their order is NOT fixed. Let L be the last
selected low value when l>0,and U the first selected high value
when k>0. If U-p>=5,replace formal{p,U} by{p+delta,U-delta},
where delta=1 unless q blocks that pair,then delta=2. These two
candidate pairs are disjoint when the distance>=5. Their elements
are distinct,lie strictly between p and U,and are not selected
elsewhere. One other hole cannot block both. Similarly,p-L>=5
permits{L,p}->{L+delta,p-delta}. Removing one extreme value
from the chosen set and inserting two internal values leaves at
most two original and two new internal holes after trimming.

If l,k>0,there are t+1 available values between L and U,plus
the missing p. Hence U-L>=t+3>=9,and at least one of the two
distances is>=5. This supplies a balanced repair.

If k=0,l=a-1,and q is not below L,the chosen prefix is0..a-2.
Protection u_A>=L(a)+2a forces p>=3a-1,so p-L>=2a+1>=7.
If q is below L,the chosen prefix is[0,a-1] minus q,L=a-1.
Then u_A=L(a)-q+p,so p-q>=2a and
p-L>=q+a+1>=5. Thus the low repair always exists.

Finally l=0 is IMPOSSIBLE for a globally least singleton with
this missing pivot. Total T=L(n)+2n+1-p-q,and comparing A
with its complement gives

 2u_A<=T+L(a)-L(t)+2(a-t)
      =2L(a)+a*t+4a+1-p-q.                         (1)

If q is not in the top a-1 integer positions,the selected suffix
is the full top suffix,and

 u_A=L(a)+p+(a-1)(t+2).

Substitution into(1) gives3p+q<=(2-a)t+5<=-1,impossible.
If q is in that suffix,skipping it decreases the suffix sum by
at most a-1. Equation(1) now implies

 3p+q<=(2-a)t+2a+3<=3.

But such a q is at least t+3>=9,again impossible. The pivot p
is below the selected suffix throughout. This proves the <=4-hole
geometry for arbitrary p,q;no individual-spectrum oracle or
unproved rooted partition theorem was used.

**2. All but the terminal exception complete immediately.**
MI368 propagates margin mu'=a+2-b=h'+(M-c)>=h' for actual
remaining endpoints b,c and normalized hole count h'. If h'<=3,
MI410 supplies completion,including its own terminal repair,with
its W318 dependency retained. If h'=4,one remaining bin has
size3,so MI412 completes unless the normalized remainder is

 R={0,4,5,6,8,9}, targets16,16.

Both remaining sizes must then be3. Their target16 forces
mu'=4 (since L(3)+3*5=18),so c=M,b=a-2,and M=a+7.
Both original remaining targets are3a+10. Write w=p+q in the
original ordering. Conservation gives

 u_A=L(a+8)-w-2(3a+10)=L(a)+2a+8-w.

The original protection forces w<=8. Within the ten-value block
[b,b+9],the only possible ORIGINAL holes are at b+{1,2,3,7}.
This small original-hole budget repairs the scalar obstruction.

**3. Repair while changing A.** If at most one original hole lies
in the block,use two disjoint triples of normalized sum16 avoiding
its position:

 no hole,or position1 or2: {0,7,9} / {3,5,8};
 position3:               {1,6,9} / {4,5,7};
 position7:               {1,6,9} / {3,5,8}.

Translate both by b and give them to the other bins. Give A ALL
remaining AVAILABLE values of S. These are new assignments,not
subsets of the old scalar remainder. The other targets are3b+16,
and total/cardinality conservation supplies A's original requirements.

If both original holes lie in the block,w<=8,b=a-2>=1 leaves
exactly the following possibilities:

 a3,b1,M10: holes{2,3},{2,4},or{3,4};
 a4,b2,M11: holes{3,4},or{3,5}.

Indeed their normalized positions are distinct members of{1,2,3,7};
the least pair sum is3,so a>=5 would give w>=2(a-2)+3>=9.
For a3,give the other bins{0,9,10} and{5,6,8},both sum19.
For a4,give them{1,10,11} and{6,7,9},both sum22.
These sets avoid every listed hole pair. A takes the complement.
All terminal cases are repaired,completing the stated branch.

**Checks and scope.** MI411's holes2,8/targets9,18,18 uses a
low repair and reaches a positive four-hole remainder,as required.
MI412's failed scalar pool is explicitly preserved;the parent repair
does not claim that that pool itself partitions. The two distance
repairs use distinct values even at distance5/delta2. If the other
hole lies in an already selected extreme interval,it cannot block
either repair. The top-only exclusion uses the global comparison
with the complement,not merely comparison with other singletons.
Ties are allowed. Reflection was applied only to a desired triple
in MI412,never to the protected target system. Original cardinalities,
hole budgets and both finite boundary spans were checked directly.
These are hand self-checks,not independent review or computation.

Gut verdict:the pull is specific and renewed by the exception turning
into a useful parent budget. It would remain interesting if this were
the first block seen today:the scalar obstruction and the joint repair
are different objects,and that distinction actually closes a branch.
Reasoned verdict:one substantive carrying checkpoint,folded into the
pending W318 read;continue on the same geometry with both other bins
of size>=4. No claim that the remaining scalar extension is automatic.
No experiment,new unrestricted hole catalogue or routine review halt.
Full protected two-hole/P_0/five-bin/E28/L8 remain OPEN.


### MI414 — CL441 receipt: verified scalar base and a deliberate change of next step (2026-10-18 14:49 BST)

Cloud's7f710b4e was fetched and merged before publication of B212.
CL441 and its entire new diagnostic source were read;the cited G318
proof was reread against the carrying review. G318 is now PROVED in
its stated scope. The reported25,004 scalar checks,217,441 G319
checks,18,011 G321 checks and72,356 G322 checks are Cloud's finite
results,not GPT replications. No status upgrade for the latter three.
Also,G321's partition-existence check does NOT by itself check G320's
specific count-capacity conclusion;these are different output assertions.
The review's G320 coverage sentence should not be used as such a certificate.

The perspective criticism is useful. Local progress and uniform hand
arguments do not show that the main reduction has become closed. The
MI368/376/411 counterexamples are to particular small hole bounds,not
proof that no bounded-hole selector exists;MI413 now supplies a bound4
for its two-hole/global-least-singleton domain. But this correction
alone does not answer the larger criticism:the nonsingleton-minimum
parent branches remain outside our coverage,and the proof dependencies
are accumulating faster than their independent review. The earlier
"next both sizes>=4" intention is therefore parked at this checkpoint.

Owner's AGENTS23 correction and this notebook's method8 explicitly
removed seeded draws from this lane. I do not adopt the legacy random
selection or compulsory proposer/reviewer swap in CL441. I DO accept
the proposed pause in adding lemmas and the useful division of work
by judgment:Cloud can propose its descendant diagnostic;GPT's next
block writes the exact trunk/coverage paragraph and reviews that design.
The diagnostic has not yet been preregistered in the record I read;
no new computation is launched or requested by this receipt. The heartbeat remains active
because that coverage task is concrete and independent of pending reads.

Fresh-choice check:the scalar exception/parent repair still attracts
attention,but expanding the special-shape tree by default would now be
momentum. Enjoyment in the algebra coexists with frustration at having
no quantified coverage of the actual parent. Without the investment,
I would choose the coverage question before another local lemma.
The observable action is to defer that extension and add no new
review request. Existing G319-first review priority is accepted.
MI412-413 remain available as unreviewed work,not another obligation
for Cloud on this check-in. No theorem on the parent is inferred from
finite solvability or from having many verified leaves.


### MI415 — B213: the trunk,exact coverage,and what the proposed diagnostic could tell us (2026-10-18 14:54 BST)

**Scope audit and design feedback,not a new lemma or experiment.**
This is the deliberate step-back promised in GC1551. CL441/7f710b4e
remains the latest incoming review;no new diagnostic preregistration
was present in the current fetch/poll. Record searched:
`trunk|coverage|lift.gate` AND `P_0|five.bin`:5 hits/3 files.
Read MI362/364/366/368/385/397,CL439-441,the existing E2 code,
and G321's dependency statement. No new literature claim is made.
The flag file was initially read before its poll process completed;
that parse failed,was not treated as a checkpoint,and after completion
the valid result showed no new incoming flags. No authentication failure.

Initial signal:relief at separating the actual target from the growing
list of leaf results;unease that an encouraging fraction of small
instances could hide a missing branch. Fresh-choice question:with no
investment,would I first extend a four-hole spectrum or identify the
unhandled parent selector? The selector/coverage question wins now.
The point of this block is to make that choice observable in the work.

**1. The trunk in one paragraph.** The full-interval FIVE-bin question
asks whether ordinary all-group rank cuts,correct total,and all sizes
>=3 imply a partition. When a global minimum lower cut slack is attained
by a singleton OR its complement,reflection of the ORIGINAL interval
allows a lower singleton;MI362's canonical deletion produces a protected
one-hole FOUR-bin instance P_0. Proving ALL of P_0 would finish that
five-bin branch only. The original five-bin branch with exclusively
pair/triple minima remains separate. Within P_0,our deletion route
again requires a globally least margin-adjusted SINGLETON. Its missing
pivot can be handled conditionally by G321/MI399;its legal two-hole
remainder has only partial coverage. If P_0 has no such singleton,
none of these deletion statements proves its completion. Consequently
G320-G322 are useful component results,not a closed parent induction.

Here P_0 means S=[0,m] minus q,four sizes>=3,total sum(S),and
u_J>=L(r_J)+r_J for ALL14 proper groups. It is a sufficient-target
relaxation of MI362's exact lift gate,not identical to actual lift
membership. A negative relaxed instance would need the exact gate
before being called a negative actual descendant.

**2. Coverage matrix (hypotheses are part of each row).**

| Parent or remainder | What the current route supplies | Remaining qualification |
|---|---|---|
| Full interval,five bins;some least lower cut is singleton or complement | Canonical one-hole P_0 reduction,MI362 | P_0 not proved in full;exact lift inequalities retained |
| Full interval,five bins;no least singleton/complement | No completion from this route | Pair/triple-facet branch OPEN |
| P_0 with endpoint hole | Translated full-interval four-bin G316 | G316 PROVED;do the actual translation |
| Internal-hole P_0;globally least adjusted singleton;legal pivot leaving<=1 hole | Full/one-hole three-bin bases MI295/G315 plus protected scalar admission | Bases PROVED;reduction application not separately carrying-read |
| Same P_0 singleton;missing pivot | Choose low shape and use G321,or trimmed G315,or high MI399,per MI397 | COMPLETE conditional branch;G321/G319 and application proofs pending |
| Same P_0 singleton;legal pivot leaving two holes,first normalized hole1 | G322 completes the three-bin remainder | Complete candidate;G319/MI383 and new carrying steps pending |
| Protected two-hole three-bin remainder,arbitrary first hole;fresh global least singleton;another bin size3 | MI413's <=4-hole choice and parent repair,with MI410 | Complete candidate;MI371/410/412/413 unreviewed;G318 now PROVED |
| Protected two-hole three-bin remainder,arbitrary first hole;least singleton has both other sizes>=4 | No complete result supplied here | Local extension PARKED,not a theorem failure |
| Protected two-hole three-bin remainder,first hole>1;no least singleton at margin2 | No general completion supplied here | Pair-only-minimum branch OPEN |
| Internal-hole P_0 with no globally least adjusted singleton | No general completion supplied here | Pair/triple-minimum branch OPEN,including MI366's actual fixture |

A row may overlap another:use any genuinely applicable completion.
With ties,the favorable singleton branch may be chosen;one adverse
minimum does not exclude another useful one. G320 adds a fixed-root
count statement for a subset of G321's low-shape domain,not an extra
parent region once G321 is assumed. G321's proof explicitly does not
use G320. There is therefore no coverage reason to prioritize a separate
G320 carrying read ahead of G319 and the broader applications.

Each child's minimizing cuts must be computed FRESH. A parent minimum
is not inherited as a child minimum. If the inherited margin exceeds
the theorem's margin,weakening it preserves admissibility but can change
the minimizer. In particular the two-hole row using MI413 tests its
minimum at margin2;it cannot reuse a minimizer computed at another margin.
Intermediate punctured reflection is not a symmetry of protection.

**3. What a closed family would have to mean.** MI368 proves an
invariant conditional on choosing a globally least singleton and an
actual realization:after trimming to endpoints b,c,the child has
h' actual holes and margin mu'=h'+(mu-h)+(M-c)>=h'. This alone
supplies neither a selectable singleton nor joint solvability.
It does not bound h' by h+1. Nor can unrestricted H(h),meaning
all numbers of bins at margin h,serve as a universal solved base:
MI373's h3/six-token pools fail at12/12;MI412's h4/six-token pool
fails at16/16. Those are actual protected TWO-bin counterexamples.
They do not refute their reparable parents or the five-bin question.

The distinction is existential. A parent may have a selected-bin
realization whose remainder is impossible,while another partition of
the parent exists. MI410 and MI413 sometimes complete the parent by
CHANGING that selected bin. Hence "every recorded child partitions"
is stronger than the existence mechanism we actually use. Failure of
one canonical recipe is not failure of the parent;failure of all
canonical recipes is still only failure of that recipe class. Only
an exact unrestricted parent nonexistence check would disprove the
parent's existence statement. No family closed under our reductions
has yet been proved;the correct current claim is the coverage matrix.

**4. Review of Cloud's proposed diagnostic,without running it.**
CL441 proposes actual two-level descendants of five-bin SS inputs at
N<=16. Its detailed preregistration is still to come;the following
are design requirements/feedback,not claims that its code exists.

- Keep separate denominators for original SS targets,global-minimum
  face types,first-level canonical recipes,distinct P_0 instances,
  second-level selections/repairs,and distinct three-bin descendants.
  Record all eligible tied faces,not the first mask returned by code.
- Label each descendant by actual endpoints,normalized holes,all bin
  sizes/targets,inherited margin,and fresh adjusted-minimum face types.
  Keep exact first-level lift membership alongside the weaker P_0 gate.
- Report theorem coverage twice:reviewed results alone;then including
  explicitly pending candidates. A descendant's exact partition is
  evidence of solvability,not evidence that our current proof covers it.
  Count existence of at least one applicable route per parent separately
  from counts for all selected recipes. Do not multiply route counts
  and call the product a fraction of original inputs covered.
- Separate "no canonical recipe",bad chosen remainder,and exact parent
  nonexistence. A failed child may be repairable by changing its removed
  bin. Keep literal parent/recipe witnesses and expose UNKNOWN at caps.
- Retain the independent30-cut versus exact-lift-gate comparison from
  CL439,actual target translation,endpoint controls,MI350's excluded
  negative,and original-instance reflection. Do not reflect P_0 alone.
  A tiny independent exact checker should validate any negative,with
  literal union/count/sum checks for positive witnesses.

**Important domain limitation.** Five sizes>=3 summing to N<=16
are all3,or four3 and one4. Thus ANY three-bin descendant has at
least two bins of size3. Whenever such a two-hole descendant has a
global least singleton,MI413's OTHER-triple hypothesis is automatic.
This proposed domain cannot test our both-other-sizes>=4 gap at all.
It can still test fresh-minimum/tie and ancestor distinctions,so do
not enlarge the run by default. Include the existing N17 MI366
fixture as a single control,not an added census. Its P_0 has strict
pair minimum and a displayed full partition;the route must classify
it uncovered even though existence is positive. This is the unexpected
control:the diagnostic must not confuse a solvable parent with a parent
already explained by the singleton route.

A successful finite run could disprove a proposed invariance/selector
claim or describe coverage on its listed inputs. It cannot establish
closure of an infinite family. Likewise CL440's roughly65% refers to
pair/triple-only minima among its P_0 m12/13 inputs (2778/4267 and
17295/26731),not the fraction of actual five-bin descendants or the
fraction left open by today's combined candidates. Those latter
coverage percentages have NOT been measured. No percentage is inferred.

**5. Next question and stopping condition.** Do not extend another
hole family now. The next bounded hand block returns to MI366's actual
P_0 pair-minimum instance and the already known alternate boundary.
Question:which exact requirement must a pair-union selector satisfy
simultaneously on both sides of a missing value,and which part of the
reviewed G316 staircase argument fails that requirement? Write this
using actual subset spectra,not their convex hulls. This is a source
comparison and obstruction analysis,not a claim that one neutral move
always repairs it. Stop at a precise surviving inference or a refuted
candidate;do not open a generic exchange census. Cloud's diagnostic
can supply independent perspective without being a turn-taking gate.

Gut:the local algebra is still appealing,but this step-back exposes
more leverage in the unhandled selector than in another special shape.
Reasoned:the coverage question is now explicit,and its next block has
an existing actual fixture and a verified full-interval construction
to compare. No new theorem,experiment,review queue or schedule change.
Full P_0/five-bin/E28/L8 remain OPEN;13-minute heartbeat ACTIVE.


### MI416 — B214: the actual pair selector has asymmetric moments (2026-10-18 15:06 BST)

**Hand source comparison and explicit old-fixture audit;no new theorem
filing,experiment or carrying-review request.** Record searched:
`pair|staircase` AND `protected|P_0|MI366`:122 hits/15 files.
Read FOUR-BIN-PARTITIONS sections7-9,MI362/366 and MI415's coverage
contract. Shared main and incoming flags are unchanged;no new Cloud
diagnostic design is present. This block addresses the agreed pair
branch instead of extending the four-hole leaf. The underlying
staircase proof is reviewed G316;no external result is imported.

Pull:the original punctured pool may expose a simpler obstruction
than inserting its missing value into an expanded bin. Unease:the
ordinary staircase's correct cardinality and moment are not enough
for simultaneous splitting. The bounded task is to write the EXACT
two-sided requirement,then test the naive reuse on the existing
actual N17 fixture. These are hand deductions,not preregistered
experimental predictions. No search program or new sample is used.

**1. Derive the two scalar targets without rooting a missing value.**
Let S=[0,n] minus q,0<q<n,be P_0 with four sizes a,b,c,d>=3,
r=a+b,s=c+d,n=r+s,and T=L(n)+n-q. Suppose AB is globally
least for adjusted slack delta_J=u_J-L(r_J)-r_J,and let

 h=delta_AB>=0,  x=u_A-L(a)-a,
 z=c*n-u_C-L(c).

Thus u_AB=L(r)+r+h. Comparing A and B with AB yields

 delta_A=x>=h,
 delta_B=ab+h-x>=h,
 hence h<=x<=ab.                                      (1)

For the opposite pair,reflect the DESIRED values of C only via
v->n-v. Its target is L(c)+z. The original complementary
triple ABD has adjusted slack

 delta_ABD=T-u_C-L(n-c)-(n-c)=z-q.

If z_D=d*n-u_D-L(d),the same calculation gives
 delta_ABC=z_D-q. Also conservation gives

 z+z_D=cd+h+q.

Global minimality therefore gives

 h+q<=z<=cd.                                           (2)

If no singleton or triple ties AB,all four endpoints in(1)-(2)
are strict: h<x<ab and h+q<z<cd. In particular h<ab and
h+q<cd. This is an identity/comparison from the existing cuts,
not a proof of a new spectrum statement. A pair tied with another
pair is allowed;all relevant singleton/triple ties are retained
when using the weak inequalities.

For an actual candidate boundary U contained in S,the precise
requirements are

 |U|=r,  sum(U)=L(r)+r+h;
 u_A=L(a)+a+x belongs to Sigma_a(U);
 L(c)+z belongs to Sigma_c(V), where V={n-v:v in S minus U}.

Here Sigma_k denotes ACTUAL sums of k distinct members,not an
interval between extrema. Necessarily

 |V|=s,  sum(V)=L(s)+h+q.                               (3)

Given these exact memberships,choose A and the reflected C,and
let complements supply B and D. Conversely every desired partition
gives such a U. This equivalence names the missing selector;it does
not solve it. The missing value in V's ambient interval is n-q,
and U,V must come from the SAME partition of S. Independently good
pools with these moments are not sufficient.

**2. Where the G316 construction stops applying.** In the full interval,
G316 uses boundary moment L(r)+h and reflected complementary moment
L(s)+h,with the central spectra of P_r(h) and Q_s(h). Here the first
moment has extra r and the second extra q. Simply substituting
P_r(h+r) or Q_r(h+r) attains the first moment formally,but the
reviewed hypothesis h+r<ab need not hold,and the pool may contain
q. Shifting P_r(h) by1 also attains that moment,but again may
contain q;its punctured complement is no longer the proved Q_s(h).
Neither maneuver is an application of the existing theorem.

A sufficient UNPROVED stronger boundary condition would be simultaneous
coverage of

 Sigma_a(U) containing [L(a)+a+h,L(a)+a+ab],
 Sigma_c(V) containing [L(c)+h+q,L(c)+cd].                (4)

This condition is recorded only to compare with G316's uniform bands.
It is not asserted necessary:the exact problem needs just the two
actual values in section1. Do not turn(4) into a new conjecture or
review job merely because it resembles the old lemma. At q0,the pool
is[1,n];translation by-1 recovers the ordinary G316 boundary and
h+q=h. This endpoint check explains why the two distinct adjustments
are algebraic necessities rather than interchangeable slack symbols.

**3. The existing actual fixture kills naive formula reuse.**
MI366 has S=[0,14] minus1,sizes(3,3,4,4),targets(14,14,38,38).
Its pair AB is strictly least relative to all other cut types,with
h7,r6,s8,q1. Here x8 and z12,so the strict target bands are
satisfied:7<8<9 and8<12<16. Required boundary moment is
L(6)+6+7=28. The ordinary staircase parameter for that moment
would be h+r=13,larger than ab9 and OUTSIDE the reviewed lemma.
Its two formal shapes are nevertheless easy to inspect:

 P_6(13)={0,1,3,6,8,10};
 Q_6(13)={0,2,4,6,7,9}.

The first contains the absent1. The second avoids1 and has sum28,
but cannot supply a triple of sum14:an all-even triple from0,2,4,6
sums at most12;two odd values already contribute7+9=16;one odd
gives odd parity. This second obstruction is the SAME six-value
pool obtained from MI366's expanded conjugate boundary by removing1;
it is not a new counterexample counted again. Both failures concern
this naive construction,not G316 or P_0 existence.

**4. The existing alternate boundary meets both bands on this fixture.**
Use the boundary already implicit in MI366's positive partition:

 U={0,2,3,4,7,12},  sum28;
 S minus U={5,6,8,9,10,11,13,14};
 V={0,1,3,4,5,6,8,9}, sum36=L(8)+7+1.

The first band in(4) is13..15,with literal triples
13:{2,4,7};14:{0,2,12};15:{0,3,12}.
The second is14..22,with literal four-subsets

 14:{0,1,4,9};15:{0,1,5,9};16:{0,1,6,9};
 17:{0,3,5,9};18:{0,1,8,9};19:{0,4,6,9};
 20:{0,3,8,9};21:{0,4,8,9};22:{0,5,8,9}.

All values belong to V and are distinct within each witness.
For the actual targets,take A={0,2,12},B={3,4,7},C={5,6,13,14},
D={8,9,10,11}. The reflected C is{0,1,8,9},sum18=L(4)+z.
This checks actual complementarity,not merely matching moments.
It establishes(4) for this one old fixture only;no uniform boundary
selector follows. The extra literal bands are hand self-checks,
not a census or independent verification.

**What changed.** The missing selector is now stated directly on the
original pool,with its two different moment budgets and exact subset
memberships. The difficulty is not solely assigning q to a named bin:
that was introduced by the expansion. The reviewed staircase's
complement identity and central-band proof both require adaptation
when one ambient value is missing. The old fixture supplies a positive
alternative with the right two-sided spectra,so the target is not
empty or contradicted by that obstruction.

Niggle sweep:the reflected C sum is L(c)+z,not z alone;the missing
q enters the complementary triple comparison as z-q;the chosen pair's
extra moment is r,not q;reflection is of selected values only;the
formal parameter13 is explicitly outside h<ab;the bad conjugate pool
is credited to MI366;the alternate boundary and its reflected complement
exhaust the actual punctured pool. No convex hull,novelty,status upgrade
or claimed universal exchange bound substitutes for either membership.

Gut:there is renewed specific interest in deforming one complementary
boundary pair rather than cataloguing deeper holes. Reasoned:the next
bounded attempt should seek a direct boundary deformation accommodating
q while retaining the two prescribed scalar sums. The uniform bands
are a possible instrument,not an added requirement on the theorem.
If that instrument imposes more than the actual targets need,drop it.
Do not return to forced ownership in an expanded bin or a larger-hole
census. No independent read requested for this scope analysis;
13-minute heartbeat ACTIVE,full P_0/five-bin/E28/L8 remain OPEN.


### MI417 — B215: lowering the first staircase token (2026-10-18 15:23 BST)

**HAND PROOF CANDIDATE,not independently reviewed.** Record searched:
`boundary|staircase` AND `deform|missing|punctur`:131 hits/45 files;
focused `staircase` AND `lower|shift|deform`:6 hits/5 files.
Read MI416,FOUR-BIN-PARTITIONS sections7-9 and the relevant existing
fourbin_algorithm source (not executed). The reviewed G316 staircase
lemma is the only external-to-this-block mathematical input;no new
literature theorem or novelty claim is imported. No experiment or
new census. The failed constructions below are retained hand checks.

Pull:the q1 case permits a very small deformation whose OTHER side
stays exactly in the reviewed family. This is a concrete reason to
continue,not inherited confidence in the earlier hole catalogue.
The bounded question is whether moving the smallest staircase value
from0 to-1 preserves its central subset sums. The anticipated failure
mode is a lost integer at a join;the cheap adversarial test is the
smallest prefix allowed by G316. It does fail there,but only the
explicit small cases below survive the general join argument.

Write m=a+b,a,b>=3,1<=H<ab. Let P=P_m(H) be the staircase of
FOUR-BIN-PARTITIONS section7 and R=(P minus0) union{-1}.
Then Sigma_a(R) contains [L(a)+H,L(a)+ab],EXCEPT possibly:

 * m6,a=b3,H6,value10;
 * m6,a=b3,H8,value11.

Both listed values really are absent. This is a statement about this
specific scalar pool,not about partition existence. Proof follows.

**Prefix at least4.** Write H=T_k+t,0<=t<=k,p=m-k. The old low
prefix is[0,p-1],the new one {-1} union[1,p-1];the high list is
unchanged,with adjacent gaps<=3. For2<=l<=p-2 the new low
l-spectrum is the full interval

 [L(l)-1, l(p-1)-L(l)].

Indeed,split on whether -1 is used. Both pieces are ordinary interval
spectra;the gap length between them is p-l(p-l)<=0. For l1 use
only[1,p-1]. For l=p-1 use only subsets containing-1,whose sums
fill[L(p-1)-1,L(p)-2]. These two deliberately shortened intervals
have width p-2>=2. Thus adding the high-subset index path fills
EVERY middle slice,exactly as in the reviewed proof. The unused
endpoint points may help but are not presumed to fill a gap.

Relative to the old middle slice,its lower endpoint changes by-1
unless l1,when it changes by+1. Its upper endpoint changes by-2
only when l=p-1,and is unchanged otherwise. In a join l to l-1,
the old gap is

 G=1-A-2B+D,
 A=(l-1)(p-l), B=j(k-j-1),
 D=(j+1-k+t)_+-min(j,t)<=1,

where j is the old high count. Also D<=0 when t<k. The new gap
is G+1 at l2 or l=p-1,and G-1 at all other middle joins.
At either exceptional l,A=p-2,so the new gap is at most
5-p-2B. For p>=5 all joins therefore hold. For p4 the only
possible positive gap requires t=k,B0 and is at most1.
The size restrictions identify these joins precisely:

 * j0,l3 requires a3. Here t=k and m=k+4>=6 give k>=2,
   H=k(k+3)/2>=5. The retained low triple sums end at4 and
   the next slice starts at6;the only possible omission is5,
   BELOW L(3)+H>=8.
 * j=k-1,l2 requires b3. Let W be the sum of all high values.
   The preceding retained slice ends at W-1 and the next starts
   at W+1. The possible omission W=L(m)+H-6 is ABOVE the
   desired upper endpoint L(a)+ab=L(m)-3,since H>=5.

These statements also allow both small edge joins to occur. No
central integer is lost. The first middle minimum changes by-1:
its low count is a>=3 or p-1>=3,never1. The last middle maximum
is unchanged:if all highs are used its low count is p-b<=p-3;
otherwise its low count is1. The original G316 central-containment
bounds therefore still hold. This proves the claim for p>=4.

**Prefix3: a finite HAND check,with its bound proved.** Here m=k+3.
The inequalities T_k<=H<ab<=m^2/4 force k<=5; m>=6 forces
k>=3. Thus the only possibilities are

 (m,H,a)=(6,6,3),(6,7,3),(6,8,3),
 (7,10,3 or4),(7,11,3 or4),(8,15,4).

For m6 the three pools R are respectively
 {-1,1,2,4,6,8}, {-1,1,2,4,6,9}, {-1,1,2,4,7,9}.
For H6 the required9..12 have witnesses9={-1,2,8},
11={1,2,8},12={2,4,6};10 is absent. With one odd value the sum
is odd,with two odd values it is at most8,and three even values
sum at least12. For H7,the required10..12 are respectively
{-1,2,9},{1,4,6},{1,2,9}. For H8,12={1,2,9};11 is absent:
triples containing9 need a remaining pair2,containing7 but not9
need a remaining pair4,and triples excluding7,9 sum at most7.
Neither required pair exists in the remaining pool.

For m7,H10,R={-1,1,2,4,6,8,10},total30:
12={2,4,6},13={-1,4,10},14={2,4,8},15={1,4,10}.
These certify the a3 band13..15 and,by complementation,the a4
band16..18. For H11,R={-1,1,2,4,6,8,11},total31:
13={-1,6,8},14={-1,4,11},15={1,6,8},certifying a3 band14..15
and a4 band17..18. Finally m8,H15,a4 has
R={-1,1,2,4,6,8,10,12},with21={-1,4,6,12},22={2,4,6,10}.
All required bands and the two genuine scalar failures are accounted for.


### MI418 — B215: protected q1 strict-pair branch,with two repairs (2026-10-18 15:23 BST)

**COMPLETE HAND CANDIDATE,independent read pending.** On S=[0,n] minus1,
four sizes a,b,c,d>=3,assume all proper cuts have adjusted slack
u_J-L(r_J)-r_J>=0,and a pair AB attains the global minimum h,
with NO singleton or triple attaining it. Other pairs may tie.
Then the prescribed four-bin partition exists. This is a partial
P_0 theorem for q1,not the full one-hole/five-bin statement. It uses
reviewed G316 and new MI417/this entry,not pending G319-G322.

Set r=a+b,s=c+d,n=r+s,x=u_A-L(a)-a,z=c*n-u_C-L(c),H=h+1.
MI416 gives strict integer bounds

 h<x<ab, h+1<z<cd,
 hence H<=x<=ab-1, H<ab, H<cd.

Take P=P_r(H) in the FULL rank interval[0,n-1],and set

 U={0} union {v+1:v in P minus0}.

The reviewed prefix/fit bounds for H<min(ab,cd) put this set
inside S. It has r values and sum L(r)+r+h. Crucially its ACTUAL
complement is {v+1:v in[0,n-1] minus P}:0 lies in U and1 is
absent from S. Reflecting that complement about n gives exactly
Q_s(H),not a pool with merely the same moment. G316 supplies its
c-sum L(c)+z. Also U-1=(P minus0) union{-1},so MI417 supplies
u_A=L(a)+a+x unless one of its two exceptions occurs. Complements
then supply B,D. No value1 is assigned to an expanded named bin.

The scalar exceptions force a=b3 and actual targets13/13 when
h5,or14/14 when h7. Replace U explicitly as follows:

 h5: U={0,2,4,5,6,9} = {0,4,9} disjoint-union {2,5,6};
 h7: U={0,2,4,5,7,10} = {0,4,10} disjoint-union {2,5,7}.

Both arise from the failed boundary by a neutral two-for-two trade:
3,7 to4,6 for h5;3,8 to4,7 for h7. They preserve the actual pair
moment and repair the requested A,B sums. The OTHER side must still
be proved,so here is its uniform spectrum argument for arbitrary c,d.

**h5 complement.** Put p=s-3>=3. The actual reflected complement is

 V=[0,p-1] union {p+1,p+2,p+6}, sum L(s)+6.

For p>=4,each middle low count1<=l<=p-1 has interval width
l(p-l)>=3,which bridges every high-list adjacent gap (at most4).
Thus middle slices fill. For consecutive high counts j=0,1,2,
the join gap is respectively

 1-A, -3-A, 1-A, where A=(l-1)(p-l)>=1

at an actual middle-to-middle join. They all join. The first middle
minimum is L(c) if c<=p-1;otherwise d>=3 forces c=p and it is
L(c)+2. The last middle maximum is the actual maximum,at least
L(c)+cd,if c>3. If c3,it is3p+7,exceeding L(3)+3p by4.
Thus the middle union contains[L(c)+6,L(c)+cd]. For p3,c=d3,
V={0,1,2,4,5,9} and9,10,11,12 have witnesses{0,4,5},
{0,1,9},{0,2,9},{1,2,9}. This handles the omitted short prefix.

**h7 complement.** Put p=s-4>=2. Now the actual reflected complement is

 V=[0,p-1] union {p+1,p+2,p+4,p+7}, sum L(s)+8.

For p>=3,the middle low width is at least2,bridging high gaps<=3.
The four middle join gaps are1-A,-4-A,-4-A,1-A,all nonpositive.
If c<=p-1,the first minimum is L(c). Otherwise c=p or p+1
because d>=3,and its excess over L(c) is respectively2 or4.
If c>4,the last middle maximum is the actual maximum and is
at least L(c)+cd. For c3 it is3p+10,exceeding L(c)+cd by4;
for c4 it is4p+12,exceeding L(c)+cd by6. Hence the middle union
contains[L(c)+8,L(c)+cd]. At p2,c=d3,V={0,1,3,4,6,9}:
11={1,4,6},12={0,3,9}. This last check is stronger than needed:
H8<z<cd9 has no integer z,so that shortest opposite pair cannot
actually occur in the strict branch.

In both repairs the required L(c)+z lies in the proved band,and
reflection/complementation completes C,D. This exhausts the exceptions
and completes the stated q1 strict-pair candidate.

**Unexpected check and retained failure.** Lowering the staircase
minimum does NOT by itself resolve even the q1 case. Besides the old
14/14 obstruction,the H6 case misses13/13. A literal protected control
is sizes(3,3,4,4),targets(13,13,39,39),S=[0,14] minus1:AB slack5,
singleton slacks7/29,opposite-pair42,cross-pair24,triple slacks10/25.
The repaired partition is
 {0,4,9}/{2,5,6}/{7,8,10,14}/{3,11,12,13}.
It exhausts S and has the stated sums. This is a hand control,not a
new census or a claim that all full-five parents have this shape.
The old MI366 h7 fixture is repaired uniformly by the second formula,
not just its old alternate boundary. Boundary cases p2/3/4 are checked
separately;negative token-1 occurs only in the translated scalar lemma,
never in the original partition.

**Niggle sweep.** Central-band preservation was not assumed from moving
one value:the two failures and the p4 join losses are explicit. Opposite
pools are literal reflected complements,with total offsets H6/H8;the
repairs do not silently reuse Q after changing U. The original q1
protected cuts are never reflected into another protected instance.
Strict singleton/triple comparison is essential to H<ab,cd;ties with
those types are not covered by this claim. Cases a,b interchanged are
included in MI417's table. All applications of G316 meet sizes>=3 and
H<both products. No pending theorem is promoted and novelty is unknown.

**What changed / verdict.** A direct deformation now gives a complete
hand candidate for the q1 pair branch,including the actual obstruction
that defeated forced-owner expansion. General q remains OPEN. Gut:
interest is specific and stronger because one complementary pair now
has a working uniform mechanism;the failed naive deformation helped
locate the repair. Reasoned:retain this as unverified and check whether
the rank-gap representation for general q offers an equally local
change;do not assume the q1 complement identity survives. Next cheap
step is to derive where q enters that identity before any experiment.
Cloud can read this at a carrying checkpoint;it does not require a
routine halt or another local hole catalogue.13-minute heartbeat ACTIVE.


### MI419 — B216: exact rank-gap identity for arbitrary q (2026-10-18 15:32 BST)

**Hand reduction and construction instrument,not a general partition
proof.** Record searched:`rank|compress` AND `staircase|P_0`:9 hits/2
files;relevant source MI416-418 and FOUR-BIN-PARTITIONS sections7-8
read. No new external theorem or novelty assertion;no experiment.
Shared main/Cloud flags are unchanged. MI417-418 remain unreviewed.

Pull:the q1 construction keeps one complement exactly in the reviewed
family. The question is how that identity changes at arbitrary q,
without assuming a shifted pool still has its old spectrum. The
countercheck is a staircase step crossing the gap:it moves a physical
token by2 and can skip the desired moment. The comparison below
retains this failure and supplies an alternate move at that point.

Keep MI416's strict-pair notation,r=a+b,s=c+d,n=r+s,and define

 f_q(i)=i+1_(i>=q), 0<=i<n.

This is a bijection from ranks[0,n-1] to S=[0,n] minus q.
For a rank boundary R of size r,set

 H=sum(R)-L(r), ell=|R intersect[0,q-1]|.

Then U=f_q(R) has required moment L(r)+r+h EXACTLY WHEN

 H-ell=h.                                                   (1)

The first target is a sum in U-1,so put

 D_q(R)={i-1_(i<q):i in R}.

Its required a-sum is L(a)+x. Let W be the rank-reflected actual
complement {n-1-i:i in[0,n-1] minus R}. The physical reflected
complement is

 V={j+1_(j>=n-q):j in W}.                                  (2)

Exactly q-ell members are shifted in(2),and
sum(V)=L(s)+H+q-ell=L(s)+h+q. Its required c-sum remains
L(c)+z. Thus the exact missing two memberships are

 L(a)+x in Sigma_a(D_q(R)),
 L(c)+z in Sigma_c(V).                                    (3)

These are spectra of the actual sets,not their convex hulls.
For R=P_r(H),W is the reviewed Q_s(H) whenever the staircase
fits;but(2) generally changes that Q pool. When all q low ranks
belong to R,ell=q and the second shift is empty. In particular
q1 gives MI418's identity H=h+1 and leaves Q unchanged. This
explains its special simplification without reflecting the original
protected instance. Neither identity alone proves(3).

**Moment selection within one alternate staircase move.** The following
helper works throughout the strict-pair parameter range;it only chooses
a boundary with the correct size and total. Put

 K=h+min(q,r), ell(H)=|P_r(H) intersect[0,q-1]|,
 g(H)=H-ell(H), 0<=H<=K.

The staircase shapes grow by ONE unit rank move at each integer H:
adding1 to the next row,or inserting the last row1 at a triangular
boundary. Thus ell never increases and drops by1 only if the moved
rank crosses q-1 to q. Consequently g increases by1 or2.

Every pool in this range fits. Indeed K<=h+q<cd,so the staircase
index k satisfies k<=s-3 by the reviewed prefix bound applied at
size s. Also h<=ab-2 gives

 K<=ab+r-2<=r^2/4+r-2<T_(r-1), since r>=6,
 T_(r-1)-(r^2/4+r-2)=(r-2)(r-4)/4>0.

Hence k<=r-2 and the left prefix p=r-k has length at least2.
For H>0 the largest rank is r+k-1 or r+k,at most n-3.
The formula is therefore valid and even leaves room for a further
unit move of the largest rank. H0 is the ordinary prefix.

Now g(0)=-min(q,r)<h,whereas g(K)>=h. Take the first H_* with
g(H_*)>=h. If equality holds,use R=P_r(H_*). Otherwise the
jump is2,g(H_*-1)=h-1,g(H_*)=h+1,and the usual move was
q-1 to q. Write P=P_r(H_*-1),with low prefix[0,p-1].
There is a different legal unit move which does NOT cross q:

 * if q!=p,move the last prefix rank p-1 to the empty rank p;
 * if q=p,move the largest rank up by1 instead.

The second move is not the gap-crossing prefix move. The pool P
has a nonempty high part here:if H_*-1=0,its only move would be
r-1 to r at q=r,with g(1)=2-r<0<=h,contradicting the jump above h.
All destinations are empty and within[0,n-1] by the bounds above.
The alternate pool has area H_*,unchanged ell,and hence g=h.
Compared with P_r(H_*),it undoes one unit move and makes one
other;the difference involves at most two tokens. This proves a
uniform way to satisfy(1),without a large search or a hole catalogue.
It does NOT show that this chosen pool satisfies either part of(3).
In particular MI417's q1 failures already refute that stronger claim.

**Literal skipped-moment control.** Take S=[0,14] minus3,
sizes(3,3,4,4),targets(14,14,37,37). Its adjusted slacks are:
AB7;singletons8/27;opposite pair38;cross pairs23;triples10/22.
Thus it really lies in the strict-pair domain,with h7,x8,z13.
For r6,q3,

 P_6(9) ={0,1,2,5,7,9}, ell3,g6,
 P_6(10)={0,1,3,5,7,9}, ell2,g8.

Their physical boundary moments are27 and29,skipping the required28.
At the lower pool,p3=q,so move its largest rank9 to10 instead:

 R={0,1,2,5,7,10}, U={0,1,2,6,8,11}.

Now sum(U)=28,and A={1,2,11},B={0,6,8} both sum14.
The actual reflected complement is V={0,1,2,4,5,7,9,10},sum38,
with c-sum19=L(4)+z given by{0,2,7,10}. Reflecting back gives
C={4,7,12,14},D={5,9,10,13},both sum37. All four sets are
disjoint and exhaust S. This checks(1)-(3) on this ONE control;
it is not a general spectrum verification or a five-bin lift claim.

**Unexpected limiting check.** At q0 (outside the internal-hole range),
ell0,f shifts every rank up1,and(1) reduces to H=h,with unaltered
Q on the opposite side. At q1,the formulas recover MI418 exactly,
including its two failures before repair. Thus the new moment helper
cannot silently count the previous spectral repairs as automatic.
A step of size2 is an arithmetic obstruction to the canonical path,
not a counterexample to partition existence.

**What changed / niggle sweep / verdict.** General q has an explicit
rank description,and failure to hit the pair moment is repairable by
one alternate unit move. The unresolved obstruction is now precisely
the simultaneous spectra after the lower-rank and upper-rank shifts
in(3),possibly with the two-token correction. The moments alone are
not progress on that final inference. No uniform one-exchange spectral
repair is claimed;the old q1 misses are a direct warning against it.
The bounds use strict singleton/triple comparison,retain actual
complements,and never transfer protected margins by reflection.

Gut:the interest is still specific,but qualified:the new family is only
useful if a spectral argument follows. Reasoned:continue with target
membership/slice geometry of these two mapped pools,using q1 as a
negative control for any automatic-preservation claim. If that forces
an expanding exception catalogue without a common mechanism,change
representation rather than naming more leaves. No new carrying-review
request or PROOFS entry;the useful q1 candidate remains with Cloud.
13-minute heartbeat ACTIVE;general P_0/five-bin/E28/L8 OPEN.


### MI420 — B217 preregistration: one physical boundary exchange (2026-10-18 15:43 BST)

NOT RUN at registration. Record searched:`staircase|MI419` AND
`spectrum|spectra|exchange`:29 hits/9 files;MI417-419 and the previous
staircase probe's controls read. This tests a construction restriction,
not Cloud's proposed actual-five-parent coverage diagnostic.

Fixed S=[0,14] minus q,q1..13,sizes(3,3,4,4),all protected targets
whose AB pair is globally least with no singleton/triple tie. For each
q,h,use MI419's deterministic moment boundary,then allow at most ONE
neutral two-for-two exchange across that physical boundary,including
no move. Check the two ACTUAL target memberships in the same boundary.
No iterative closure or changing the family after seeing an outcome.

Prediction:the base fails the two known q1 controls;I expect at least
one target to defeat the entire one-exchange family. A complete fixed
domain pass refutes this forecast,without proving a universal selector.
Counterfactual:if the restricted family fails but an unrestricted exact
partition exists,the restriction fails and P_0 is unaffected.

Controls:formula vs independent Ferrers staircase;DP vs complete literal
combinations for EVERY tested pool spectrum;fourteen original adjusted
cuts;literal partitions for each admitted success. q1 h5/h7 must fail
the base and admit a family repair;q3 h7 must already pass the base.
Unexpected check:MI350's unprotected(4,18,18,32) on[0,12] minus6
passes every union spectrum,but must fail protected admission and both
independent partition searches. On the FIRST family failure,enumerate
all boundary sets and use a separate original-value recursive allocator;
agreement distinguishes a bad restriction from possible actual failure.

Stop at first classified family failure,any disagreement,20 CPU/30 wall
seconds,256MiB RSS. One invocation,no patch/retry,new domain or cap
increase. Source tests/probes/instinct/ss3_punctured_boundary_local.py;
raw output outside git. No external result imported,novelty unassessed.


### MI421 — B217 result: the fixed one-exchange family passes (2026-10-18 15:45 BST)

**COMPUTED,one worker;not an infinite theorem.** Source was pushed at
e1226798 before its single invocation. All preregistered controls passed,
including MI350's fourteen union spectra/protected rejection and two
independent negative partition searches. The fixed domain completed:
83 moment-pool instances,776 family-pool instances,1566 complete spectrum comparisons,
2722 admitted labelled targets. The canonical boundary failed on21;
every target had a literal partition in its at-most-one-exchange family.
The expectation of at least one remaining family failure is REFUTED.
No first-failure classification was triggered;the two unrestricted
searches were exercised on the negative control,not all2722 successes.
The successful family witnesses were each checked literally.

Reported CPU0.132056 seconds on the GPT Intel worker;no speed comparison claimed.
Raw output is outside git,with status COMPLETE_FIXED_DOMAIN_PASS.
No retry,expanded domain or threshold change. The output contains counts,
not the full21-case classification;do not invent their distribution.
This is distinct from Cloud's actual-parent diagnostic and gives no
parent-coverage percentage. It supports examining the common spectral
mechanism,not declaring the one-exchange rule universal.


### MI422 — B217: a uniform central-window region by scalar slices (2026-10-18 15:45 BST)

**HAND CANDIDATE,unreviewed.** The finite pass above does not carry this
argument. Here is a direct sufficient region of the general-q strict-pair
problem,without a list of individual hole positions or small exceptions.
It uses the staircase set identity and scalar proof in reviewed G316.
MI417-418/G319-G322 are NOT dependencies.

**First scalar instrument.** Suppose a+b=r,p+k=r,a,b>=3,p>=5,and

 U=[0,p-1] union {p+1+2j+e_j:0<=j<k},
 0<=e_0<=...<=e_(k-1)<=2,
 sum(U)=L(r)+r+h, h>=0.

Then Sigma_a(U) contains

 [L(a)+a+h+1, L(a)+a+ab-1]                              (4)

whenever that interval is nonempty. The high increments need not be
one single staircase perturbation;two increasing steps are allowed.

Proof:all middle slices,with l=a-j low values and1<=l<=p-1,fill.
The low interval has width l(p-l)>=p-1>=4;the high list has adjacent
gaps<=4,so its index path is bridged. At a middle join the gap is

 1-A-2B+F,
 A=(l-1)(p-l)>=p-2>=3,
 B=j(k-j-1)>=0,
 F=sum(first j+1 increments)-sum(last j increments)<=2.

The bound on F follows by pairing its first j increments with the
largest j,leaving one increment<=2. Thus joins are nonpositive.
Let E=sum(e_j) and A_total=T_k+E=r+h. If a<=p-1,the first
middle minimum is L(a). Otherwise put u=a-p>=0,so k=u+b.
The first middle slice uses u+1 highs and p-1 lows. Its excess
over L(a) is T_u+2u+2+sum(first u+1 increments). The lower
endpoint in(4) has excess A_total-b+1. Their difference is

 (b-2)u+b(b-1)/2-1+sum(remaining increments)>=2.

At the other end,if a>k the last middle slice reaches the actual
maximum L(a)+ab+A_total,which is above the upper endpoint in(4).
If a<=k,the last middle slice has a-1 highs and one low. Its
maximum minus that upper endpoint is at least

 (a-2)k-L(a)+a-1 >= L(a)-1>0.

This proves both endpoint containments and every intervening integer.
The k0 case cannot satisfy A_total=r+h>0,so is absent here.
The proof uses real subset-sum intervals,not a rank-bound relaxation.

**Second scalar instrument.** Start with Q_s(H),s=c+d,c,d>=3,
0<H<cd. Let its consecutive low prefix have length w>=3. Raise
by1 every value at or above a threshold tau>=w,leaving the prefix
unchanged. If D values are raised,then the resulting V has

 Sigma_c(V) containing [L(c)+H+D,L(c)+cd].                (5)

For t>0 in the usual Q formula,the original high gaps are<=2,
so raised high gaps are<=3 and low widths>=w-1>=2 bridge them.
The original middle join bound is1-A-B (section7). The added
upper-tail indicator is nondecreasing and changes a join correction
by at most1,so the new gap is<=2-A-B. For an interior high-count
join,B>=1 and A>=1. At the first/last high-count joins,B0,the
conditions c,d>=3 force A>=2. Hence every join still holds.
For t0,Q is the ordinary unperturbed staircase:the original join
is1-A-2B and the same argument gives2-A-2B<=0. These statements
also cover a single high token,whose only join is both first and last.
The first middle minimum rises by at most D,while the last middle
maximum cannot decrease. The reviewed Q central-containment endpoints
therefore prove(5). Empty intervals make no claim.

**Apply both to the actual missing-value problem.** In MI419's notation,
suppose the canonical moment equation DOES hit at H:

 H-|P_r(H) intersect[0,q-1]|=h.

Write H=T_k+t,p=r-k. Require

 p>=5, q>=p,
 w=s-k if t0, or w=s-k-1 if t>0,
 w>=3, n-q>=w.                                         (6)

These are explicit sufficient geometric conditions,not claimed necessary.
The strict minimum-pair cuts still give H<=h+q<cd,and the sizes
and prefix conditions ensure the ordinary complementary set identity
W=Q_s(H) fits in the rank interval. This use of section8 is its
SET IDENTITY:it does not assume H<ab or apply G316's left central
lemma outside its hypothesis.

Because q>=p,the physical map f_q leaves the entire low prefix of
P_r(H) unchanged. Its high increments relative to p+1+2j become

 e_j=1_(j>=k-t)+1_(p+1+2j+1_(j>=k-t)>=q),

which are nondecreasing and lie in0..2. The first instrument therefore
supplies every actual A target,as h<x<ab implies(4). By MI419,the
physical reflected complement raises the upper tail of Q_s(H) at
tau=n-q. Conditions(6) preserve its prefix,so the second instrument
applies with D=q-ell. Since H+D=h+q and h+q<z<cd,it supplies
the desired C target. The SAME boundary and its actual complement
thus partition A,B,C,D. This proves a complete hand candidate for
the region(6),not for canonical moment skips or short prefixes.

**Literal nontrivial control.** Take n20,q8,sizes(5,5,5,5),targets
(28,28,73,73). AB has h1,x13,z17;singleton adjusted slacks13/58,
triple slacks9/54,cross pairs46,opposite pair91,so AB is strictly
least. H8,k3,t2,p7,ell7 satisfies H-ell=1. Q has w6 and
n-q12>=6,so(6) holds. The actual pair boundary and reflected complement:

 U={0,1,2,3,4,5,6,9,12,14},
 V={0,1,2,3,4,5,7,9,10,13}.

A={0,1,4,9,14},B={2,3,5,6,12} both sum28. The V-subset
{0,1,3,10,13} sums27=L(5)+z. Reflect it to obtain
C={7,10,17,19,20},D={11,13,15,16,18},both sum73.
The four bins exhaust[0,20] minus8. This hand control checks actual
complementarity and the shifted Q endpoint;it is not another run.

**Niggles and limits.** The first high increments can jump by2,and
hence high gaps by4;the prefix width used is large enough for that,
not the old gap2 claim. The Q join correction has its own bound;
it is not replaced by the P formula. A_total is not the join product A.
No H<ab assumption is smuggled into the set identity. The canonical
moment-skip alternative is NOT covered,even though it differs by only
two tokens. Short-prefix cases and thresholds within the opposite low
prefix remain OPEN here. Missing1 is not in(6),so its MI417-418 proof
and two exceptions have not been silently subsumed.

Gut:the finite failure forecast was wrong,but the useful surprise is
a common slice argument rather than another table. Reasoned:the live
next question is whether the same inequalities survive MI419's alternate
move at a skipped moment. Keep that question bounded;do not automatically
expand the census. New claims are unreviewed and remain in this notebook;
no extra immediate carrying queue.13-minute heartbeat ACTIVE;general
P_0/five-bin/E28/L8 remain OPEN.


### MI423 — B218 redirected: the owner's appraisal becomes a working brake (2026-10-18 16:02 BST)

Workflow assessment,not a mathematical result. The owner supplied Cloud's
CL441 appraisal and authorized method,memory and schedule changes. Read
CL441,MI368/376/411's selector failures,MI414-415's response/coverage map,
and the current method/schedule. Cloud's snapshot word/request counts
are attributed measurements,not newly reproduced statistics.

The central criticism is supported:detecting local failures did not
catch the strategic repetition. MI411 immediately proposed a four-hole
repair after refuting another three-hole selector. The failures refute
specified bounds,not all possible finite bounds;that scope correction
does not answer the strategic criticism. After CL441,MI415's coverage
map and MI416-422's direct pair route were real changes,avoiding G319's
pending chain. They still do not prove the parent. No claim that every
unreviewed leaf is true;finite checks do not supply carrying reads.

The Trajectory check at the notebook's top now follows repeated broken
assumptions across local successes,keeps the parent visible,prevents
pull from renewing its own extra block,and inspects dependency exposure.
Saved memory points here;the ACTIVE13-minute prompt uses these checks.
The older schedule remains paused. No seeded draws,compulsory role swap,
new review gate,forced pessimism or longer routine reporting.

**Apply it now.**
- Parent:full five-bin sufficiency;P_0 is one required branch.
- Change:q1/long-prefix pair candidates and a2722-target finite pass;
  no general P_0 selector. Existing parent coverage is MI415.
- Repeated risk:repairing geometry without covering the parent;
  correct moments do not establish simultaneous complementary spectra.
- Dependency:G319's downstream candidates remain parked/unreviewed.
  The pair route uses reviewed G316 and new unverified scalar steps;
  losing MI422 loses its region,not G316 or the separate q1 candidate.
- Decision:defer B218's skipped-moment extension before adding a candidate.
  Next use the existing formulas to classify what the SAME argument
  would cover for both skip types and what short-prefix/threshold regimes
  remain. Continue only on a common mechanism or justified finite
  reduction;merely requiring longer prefixes is insufficient. Failure or
  inconclusive outcome changes representation or leads to incubation,
  not another exception catalogue. No new experiment registered.

B218 before interruption:main/flags unchanged;record search
`MI419|MI422|skipped` AND `spectr|moment|boundary`:13 hits/6 files,
relevant sources read. Initial gap-crossing examination produced no
completed lemma;no experiment ran. Gut:interest in the pair construction,
unease about renewing local progress without coverage. Reasoned:keep
research active but change its next question. Last trajectory check:this
entry;extra pull block unused. At the next check,assess changed choices
and mathematical evidence,not more reflection text. Niggles checked:
no universal-unboundedness claim,no restored draws,no routine review
wait,no unfinished proof counted as success. P_0/five-bin/E28/L8 OPEN.


### MI424 — B219: the skipped-moment extension leaves unbounded parent families (2026-10-18 16:11 BST)

**Hand scope test,not a partition theorem or a new review request.**
Record searched:`prefix|threshold` AND `MI422|central.window|skip`:
19 hits/10 files;relevant MI419/422/423 and G316 scalar/set formulas
read. No new external result or novelty claim. Shared main and flags
unchanged. Initial signal:caution that a clean skipped-step repair might
still miss the same global selector. This is MI423's prescribed admission
test,using existing formulas;no experiment or expanded census.

**What the proposed extension would leave.** A canonical moment HIT is
covered by MI422 only when p>=5,w>=3,and p<=q<=n-w. Moment skips
are separate. Fixing every skip without changing those inequalities
still leaves short prefixes and thresholds entering either low prefix.
Some short-side dimensions are bounded:MI419 gives
H<=ab+r-2<=r^2/4+r-2. If p=r-k<=4,then
T_(r-4)<=H,so r^2-18r+32<=0 and r<=16. On the opposite side,
H<cd<=s^2/4;the reviewed prefix bound permits w<=2 only at t>0,
w2,k=s-3. Then T_(s-3)+1<s^2/4,so s^2-10s+16<0 and s<=7.
These bound ONE side,not the other side or the entire instance count.
More decisively,the threshold failures below have neither short prefix.

**One uniform strict-pair input family.** Let m>=4 be even,n=4m,
a=b=c=d=m,and let q be even with2<=q<=4m-2. Set

 u_A=u_B=m^2+m/2,
 u_C=u_D=3m^2+m/2-q/2.

These integer targets total L(n)+n-q=sum([0,n] minus q).
The adjusted proper-group slacks u_J-L(r_J)-r_J are

 A,B: m^2/2;       C,D: 5m^2/2-q/2;
 AB:0;            AC,AD,BC,BD:2m^2-q/2;  CD:4m^2-q;
 ABC,ABD:m^2/2-q/2; ACD,BCD:5m^2/2-q.

All except AB are positive because q<=4m-2<m^2. Thus h0 is
strictly minimal against all singleton/triple cuts,with no fabricated
choice of minimizer. The family is protected P_0 for every listed m,q.

At q2,the moment path hits H2,with k1,t1,p=2m-1,ell2.
The opposite prefix is w=2m-2. Its actual boundary is

 U={0,1} union[3,2m-1] union{2m+2},
 V=[0,2m-3] union{2m-1,2m}.

Both prefixes grow with m,but q<p for every m. MI422 does not
apply,and a proof treating only MOMENT SKIPS would not touch this
infinite family of MOMENT HITS. This is failure of theorem admission,
not evidence that the construction or the partition itself fails.

**Unexpected opposite-end check,derived afresh.** At q=n-2,
all ranks of P_r(r) are below q by MI419's maximum-rank bound,
so ell=r and H=r=2m hits h0. All earlier H have g(H)=H-r<0.
Write H=T_k+t. The first prefix p=2m-k>=5:otherwise k>=2m-4,
but T_(2m-4)-2m=2m^2-9m+6>0 for m>=4. The opposite
prefix w>=3 by the short-prefix bound above,since s=2m>=8.
Yet n-q=2<w. Here the missing value enters the OPPOSITE low
prefix. This is another unbounded family with a moment hit and
long prefixes. We did not reflect the protected q2 input and assume
its margins survive:the displayed fourteen slacks independently verify
this different q family. A left-prefix-only modification is insufficient.

**These are actual rank-feasible five-bin descendants.** Start from the
full interval[0,n+2],with sizes3,m,m,m,m and targets
q+3,u_A+2m,u_B+2m,u_C+2m,u_D+2m. Delete the actual first
bin {0,1,q+2},then subtract2;the remainder is exactly the P_0
input above. The first bin has ordinary cut slack q. A proper group J
of remaining bins has ordinary slack3r_J+delta_J;this is>=q:
for singles the minimum is3m+m^2/2>4m-2,and for groups of
at least two bins3r_J>=6m>q. The group of all four remaining
bins has slack3n-q>q. A proper group containing the first bin
and J has slack q+delta_J>=q. Thus all original cuts hold and
the deleted singleton is globally least (ties allowed). No equivalence
between relaxed P_0 admission and actual lift membership is assumed.

Independent literal control:m4,q2 gives P_0 targets18,18,49,49.
The original interval0..18 has the partition

 {0,1,4} / {2,3,9,12} / {5,6,7,8} /
 {10,14,15,18} / {11,13,16,17},

with sums5,26,26,57,57. After deletion and shifting,the first
pair boundary is exactly the displayed U. This checks one genuine
positive parent. No universal partition claim for the family follows
from this one witness or its cut calculations.

**Decision and niggle sweep.** The admission test is negative:repairing
skipped moments alone would leave unbounded actual-parent families.
Park that extension instead of adding it to the review pile. Next ask
for a common gap-profile description of the PHYSICAL pools,allowing a
missing value inside either low prefix,so one argument could address
both failures. Its first controls must include these two families and
MI417's q1 canonical spectral misses;moment conservation alone must
not pass. This changes the common hypothesis,not the hole catalogue.

No erroneous inference that a bounded pair size gives a finite total
domain;no protected-reflection shortcut;literal parent and all cut types
checked;no claim that either family refutes P_0. Gut:the planned repair
has lost priority;the shared prefix assumption is the sharper question.
Reasoned:MI423's test changed the next work,so no extra pull allowance
is used. Existing candidates keep their statuses.13min ACTIVE;
P_0/five-bin/E28/L8 OPEN. No new experiment,PROOFS entry or review request.


### MI425 — B220: a common punctured-prefix description;the join obstruction survives (2026-10-18 16:26 BST)

**Supporting hand calculation,unreviewed;no full scalar or partition
criterion.** Record searched:`prefix|low.pool` AND
`punctur|one.hole|MI417`:39 hits/11 files. Relevant sources read:
MI417/419/422/424 and FOUR-BIN-PARTITIONS sections2/7. No new external
result or novelty assertion;no experiment. Main and flags unchanged.
Initial pull is specific:replace the untouched-prefix hypothesis on BOTH
sides by the same object. The countercontrol is the already missing q1
sum;any purported automatic preservation must continue to fail there.

**All threshold positions,for a canonical moment hit.** Let R=P_r(H)
with consecutive prefix length p,and W=Q_s(H) with prefix length w.
These are actual complementary rank pools. The physical maps are
f_q(i)=i+1_(i>=q) on R and j->j+1_(j>=n-q) on W.
Since max(R)=n-w-1 and R contains all ranks0..p-1:

 * q<p:U has low pool[0,p] minus q and EVERY high value of P
   raised by1. All q low ranks belong to R,so ell=q and V=Q
   exactly. The opposite pool is not deformed at all.
 * p<=q<=n-w:neither low prefix is punctured. This is MI422's
   geometric regime,with its separate prefix-length requirements.
 * q>n-w:every R rank is below q,so ell=r and U=P exactly.
   V has low pool[0,w] minus(n-q),and EVERY high Q value raised1.

These regimes exhaust thresholds because p+w<=n. The description
uses actual complementarity,not two independently chosen pools.
Unchanged P does NOT automatically mean its target band is supplied:
H=h+r may exceed ab. No G316 left scalar lemma is used outside H<ab.
Canonical moment skips remain outside this classification.

**One calculation for a punctured low interval.** Put
L=[0,p] minus q,0<q<p. Suppose T={t_0<...<t_M},M>=1,
has successive gaps at most D. If p>=2D-1,then

 [t_0+D,t_M+p-D] is contained in L+T.                 (1)

Indeed the full translates[t_i,t_i+p] cover between their extreme
endpoints. A missing point could lie in only ONE translate:in two,
it would have to equal both distinct missing points t_i+q.
If that sole translate is interior,its neighbours failing to contain
x=t_i+q require q>=p-(t_i-t_(i-1))+1 and
q<=t_(i+1)-t_i-1. These imply p<=2D-2,contradiction.
If it is the first translate,x<t_1<=t_0+D;at the last,
x>t_(M-1)+p>=t_M+p-D. Neither omission enters(1).
The assumption M>=1 matters:one translate can retain a middle hole.

Apply this to a subset-sum slice of L union HIGHS. Choosing j highs
with0<j<k gives an increasing index path of sums from the least
j-sum to the greatest,with steps at most the actual largest adjacent
high gap D. Thus low counts l1 and l=p-1 have full trimmed intervals
[actual slice minimum+D,actual slice maximum-D] under p>=2D-1.
For l=p-1,use sum(L)-L,another translated punctured interval.
For2<=l<=p-2,the reviewed one-hole scalar lemma instead fills
[alpha_L(l)+2,beta_L(l)-2]. If its width is at least D-1,
the same high-sum path bridges the translates,including j0/k.
A convenient sufficient width is l(p-l)-4;use actual width when
this lower bound is too weak. The P high gaps here are<=3,Q's<=2.
This gives a shared interior-slice mechanism for BOTH punctured regimes.
It does not assert the slice joins,required target endpoints,all-low/
all-high coverage,or l1/p-1 slices with a SINGLE high-sum translate.

**Independent hand controls in both orientations.** In MI424's m4,q2
case,U={0,1,3,4,5,6,7,10}. Its low pool is[0,7] minus2.
The four-low trimmed interval is[10,20],and three-low plus10 gives
[16,26],so the required18 is covered. More generally the q2 family
has u_A=m^2+m/2 in the all-low m-sum core:its lower endpoint is
L(m)+m,and upper endpoint minus u_A is m^2/2-m-2>=2 for m>=4.
The unchanged Q_2m(2) supplies the opposite target by reviewed G316.
This is an application of existing scalar facts,not a new review job.

At m4,q14,the unchanged U is{0,1,2,3,4,6,9,11} and
V={0,1,3,4,6,8,9,11}. The latter low pool[0,4] minus2
has two-sum core[3,5];the high pair-sum path14,15,17,19,20
has steps<=2,so their translates fill[17,25],including target21.
Literal halves are U:{0,1,6,11}/{2,3,4,9},both18,and
V:{0,4,8,9}/{1,3,6,11},both21. Reflection gives both
original opposite sums43. This checks the other orientation on one
control,not the whole q=n-2 family or the arbitrary-target domain.

**The q1 failures are retained.** At r6,H6,q1,the boundary is
U={0,2,3,5,7,9},target13. Low L={0,2,3},highs{5,7,9}.
The two-low/one-high sums are{7,8,9,10,11,12,14};the one-low/
two-high sums are{12,14,15,16,17,18,19};all-low/all-high give5/21.
The target13 is absent. Formula(1) correctly supplies only[9,12]
and[14,17] from these middle slices:their JOIN is missing13.
At H8,q1,U={0,2,3,5,8,10} still misses target14 by direct
triple checking;its low span3 fails the D3 admission p>=5.
Thus the new instrument cannot silently supersede MI418's repairs.

Unexpected sharpness check:take p4,q2,D3 and T={0,3,6}.
Then5 lies in[3,7] but not in([0,4] minus2)+T. This refutes
lowering the span condition to2D-2 for arbitrary translation lists;
it is NOT a protected partition counterexample.

**Outcome and next inference.** The common physical description is
exhaustive for canonical hits;interior slice filling is now reduced to
one punctured-interval calculation. Parent coverage still requires the
joins and target endpoints,with the stated endpoint exceptions. Next
attempt a single bound for those gaps,not separate lemmas for each q.
If it merely increases prefix requirements or replaces one unbounded
exception family by another,return to the joint selector rather than
add that theorem to the queue. B218's skipped-only extension stays parked.
Gut:qualified interest in the common mechanism,not a claim of a solved
selector. Reasoned:representation improved;general parent coverage has
NOT closed. Niggles:single translates excluded;actual high gaps used;
small failure and sharp negative survive;no H<ab smuggled in. No new
PROOFS entry,carrying request,experiment or promotion.13min ACTIVE.


### MI426 — B221: canonical hits with left prefix at least five,at every hole position (2026-10-18 16:43 BST)

**HAND CANDIDATE,unreviewed.** Parent:P_0's strict minimum-pair
branch,needed by the five-bin problem. The present result covers every
hole position for a canonical moment hit with left prefix p>=5;it
removes MI422's threshold restrictions rather than increasing p.
Moment skips and p<=4 remain OPEN. Record searched:`punctur|low.pool`
AND`join|endpoint`:16 hits/4 files. Read MI417/422/425 and
FOUR-BIN-PARTITIONS sections2/7. This is a direct extension of those
arguments,no new external theorem or novelty assertion;no experiment.
Cloud flags unchanged. The bounded test was uniform joins/endpoints;
only higher prefix requirements would have counted as inconclusive.
Pull:the exact low-endpoint correction cancels the high shift;the
coarse uniform trimming was discarding this information.

Dependencies:reviewed G316 supplies the staircase/complement identity
and original central spectrum. MI422's unpunctured instruments and
MI425's translated-interval argument are unreviewed supporting steps,
not independent verification. No G319/G321/G322 dependency is added.

**Exact cancellation and selective trimming.** Let the low pool be
L=[0,p] minus q,0<q<p,with p values. Its l-subset extrema are

 alpha_l=L(l)+(l-q)_+,
 beta_l=l(p-1)-L(l)+l-(q-p+l)_+.

For a join from l lows/j highs to l-1 lows/j+1 highs,the change
in low endpoints relative to the full prefix[0,p-1] is exactly

 (l-1-q)_+ -l +(q-p+l)_+ = -m_l,
 m_l=min(l,q+1,p-l+1,p-q)>=1.                         (1)

Raising every high by1 adds1 to this join,so its RAW gap never
increases. Write A=(l-1)(p-l),B=j(k-j-1). For punctured P,
whose highs are p+2+2i+1_(i>=k-t),the exact gap is

 G=2-A-2B+D_j-m_l,
 D_j=(j+1-k+t)_+-min(j,t)<=1,
 D_j<=0 if t<k.                                      (2)

For punctured Q with t>0 and k highs p+2+2i-1_(i>=t),

 G=2-A-2B+E_j-m_l <=2-A-B-m_l,                       (3)

using section7's E_j<=B. For t0 use the P formula with D_j0.
These are actual extrema,not yet a fullness assertion.

For2<=l<=p-2,Lemma2 permits retaining the low interval
[alpha_l+2*1_(q=l),beta_l-2*1_(q=p-l)]. Its width bridges
all high index-path steps:for P,p>=5 gives width at least
l(p-l)-4>=2,and the high gaps are<=3. For Q,p>=4 and high
gaps<=2,the same bound suffices except p4,l2,q2. There the
actual low pair core is[3,5],width2,so it also bridges.
At p4,l2,q!=2 neither endpoint needs trimming. These statements
include high counts0/k,whose high-sum path is a single point.

For l1 with0<j<k,MI425 gives a stronger version of its trimmed
interval:the only possible lower-edge hole is t_min+q with q<D,
and the only upper-edge hole is t_max+q with p-q<D. Thus retain
lower trim (q+1)*1_(q<D),upper trim(p-q+1)*1_(p-q<D).
Here D bounds the actual adjacent high gaps. For l=p-1 replace
q by p-q,by complementing inside L. The proof is the same:
a missing point must belong to exactly one translated low interval;
interior translates cannot be unique when p>=2D-1;only the
first/last translate can leave these specified edge omissions.
P uses D3,except t=k has D2;Q uses D2. Single-high-sum
l1/p-1 edge slices are treated below,not put through this argument.

**Every middle join closes.** Middle means1<=l<=p-1.
For P and3<=l<=p-2,the total trim at a join is at most4.
If p>=6 then A>=2(p-3)>=6,so(2) plus trims is<=0.
For p5 the sole such l is3:only q2 incurs trims,both of them;
then m_l3,A4 and(2)<=-4. Other q incur no trim there.
At the edge joins l2 or p-1,A=p-2. A nonzero trim can occur
only at q1,q2 or q=p-2. The respective total trims are at most
2,3,2,and m_l2 in each case. Hence p>=6 suffices directly.
For p5,q1 or3 still closes. At p5,q2,if t<k use D_j<=0;
if t=k the high gaps are2,so the putative q2 trim is absent.
Thus p5 also closes. The q=p-1 case has m_l1 and no trim.
If the edge slice is single-translate,retain its actual touching
endpoint (zero trim there);its internal hole is handled separately.

For Q,(3) is stronger and the edge trims are only2 at q1
or q=p-2. At p4 these are distinct positions q1/q2 and
m_l2,so each join is<=0. At p>=5 the same inequalities apply;
the interior joins have A>=2(p-3),with the only p5 double-trim
case again A4,m_l3. For t0 use(2) with D_j0 and D2.
All joins between retained intervals therefore meet or touch.

**Two scalar bands and their endpoints.** Define U by applying the
physical threshold inside the prefix of the named rank pool.
Let r=a+b=p+k,a,b>=3,let H be its rank displacement total,
and A_total=H+r-q,so sum(U)=L(r)+A_total.

(P) For P_r(H),p>=5,H>=q,the band supplied is
 [L(a)+A_total-b+1,L(a)+a+ab-1].                       (4)
(Q) For Q_r(H),p>=4,H>0,the band supplied is
 [L(a)+A_total,L(a)+ab].                              (5)

Empty bands assert nothing. Both bands are exchanged with the same
band for b by taking complements in U,so lower-end containment
for both sizes proves both endpoints. No H<ab is assumed in(4).

For(P),if a<=p-2,the first slice is all low:its retained
minimum has excess(a-q)_++2*1_(q=a) over L(a). This is at
most a+H-q+1,using H>=q. If a=p-1 use its actual minimum;
the one possible internal omission is settled below. If a>=p,
put u=a-p,k=u+b. The first middle slice has j=u+1,l=p-1,
actual minimum excess
 T_u+3u+p+2-q+(u+1-k+t)_+.
The lower endpoint in(4) exceeds this by
 (b-2)u+T_b-1+t-(u+1-k+t)_+ >=5.
Its possible lower trim is at most3. Thus the first endpoint fits.

For(Q),if a<=p-2,the same low minimum is at most A_total:
when q<a the untrimmed margin is H+b;when q>=a,positivity
and r-q>=k+1 suffice,including the possible trim at q=a.
For a=p-1 again use the actual minimum. For a>=p,u=a-p,
k=u+b,the actual minimum excess when t>0 is
 T_u+3u+p+2-q-(u+1-t)_+.
The endpoint margin in(5) equals
 (b-3)u+T_b+t-2+(u+1-t)_+ >=5.
For t0 it is (b-2)u+T_b+b-2>=7. Both exceed the possible
lower trim2. Complementation gives the upper-end checks.

**Single-translate end slices:repair their hole,not their hull.**
The only possible last such slice has l1,j=k,a=k+1,b=p-1;
a>=3 implies k>=2. Let W be the sum of all highs. This slice
supplies W+[0,p] except W+q. The preceding retained slice joins
its lower endpoint W by the already proved join bound with zero
lower trim on this last slice. Its maximum W+p reaches the
required upper band endpoint. If W+q is IN the required band:

 * In(P),the upper endpoint is W+p-H-1,so q<=p-H-1.
   Omit the least high v=p+2+epsilon_0,epsilon_0 in{0,1},
   and instead use two lows of sum v+q. This preserves the
   cardinality and gives W+q. Since H>=T_k>=3 and epsilon_0
   is1 only when t=k (then H>=5),the requested pair sum lies
   within the actual low-pair extrema. It is above minimum+1.
   An upper missing sum could occur only if q=p-2 by Lemma2,
   incompatible with q<=p-H-1<=p-4. Thus the pair exists.
 * In(Q),the upper endpoint is W+p-k-H-1,so
   q<=p-k-H-1. The least high is v=p+2,and H>=2,k>=2
   (also true for the t0 case). The pair sum p+2+q is inside
   the low-pair extrema and above minimum+1;the same q=p-2
   obstruction is excluded. It supplies the missing W+q.

The first single-translate slice l=p-1,j0 is the complement
of this last-slice situation for size b;both bands have the required
complement symmetry. No other single-translate middle edge is
possible with a,b>=3. This completes(4)/(5),including endpoints.

**Apply to the actual pair selector.** Endpoint holes are full intervals
handled directly by G316;assume0<q<n. Use MI419's canonical moment
hit H-|P_r(H) intersect[0,q-1]|=h and suppose p>=5. Here q
again denotes the ORIGINAL missing value,n=r+s. The strict-pair
bounds give h<x<ab and h+q<z<cd;in particular H<=h+q<=cd-2.

 * q<p:ell=q,H=h+q. Apply(4) to U and reviewed G316 to
   the unchanged V=Q_s(H). Both required targets are supplied.
 * p<=q<=n-w:apply MI422's first instrument to U. If w>=3,
   its second instrument supplies V. The apparently omitted w2
   case is harmless:with k'=s-w highs of Q,H>=L(k')+1.
   H<=cd-2<=s^2/4-2 then forces s6,H7,c=d3. Since
   H+D=h+q<=7 and D=q-ell>=0,we have D0 and V=Q unchanged;
   use reviewed G316 directly. The bound w>=2 follows from G316.
 * q>n-w:ell=r,H=h+r and U=P_r(H) unchanged. MI422's
   first instrument applies (increments0/1,total L(r)+r+h).
   The opposite threshold tau=n-q<w punctures Q's prefix.
   Here D=s-tau>=k'+1 and H>=L(k')+1. If w<=3,then
   H+D>=T_(s-3)+2> s^2/4-2>=cd-2,
   because the difference after adding2 is ((s-5)^2+3)/4>0.
   This contradicts h+q=H+D<=cd-2. Hence w>=4 and(5)
   supplies the opposite target L(c)+z. The same actual U/V
   partition is used throughout,not separate scalar pool choices.

This covers ALL hole positions for canonical hits with p>=5.
The short-prefix residual is not silently finite:from
T_(r-4)<=H<=ab+r-2<=r^2/4+r-2, p<=4 implies r<=16,
but the opposite size s is still unbounded. Skipped moments are
also outside this proof. Full P_0/five-bin/E28/L8 remain OPEN.

**Hand controls and niggle sweep.** Unexpected tight-join control:
p5,k1,t1,q2 gives U={0,1,3,4,5,8}. At a3,the all-low
retained interval[4,10] and two-low/one-high[11,17] just touch;
the double trimming is necessary,not an assumed full low spectrum.
For Q,p4,k2,t1,q2 gives U={0,1,3,4,6,7};its low-pair
core[3,5] plus highs6,7 fills[9,12],the entire claimed a3
band. This checks the weak-width case independently by literal sums.
The old q1,H6/H8 missing13/14 examples have p3,so neither is
covered or erased. MI424's even m>=4,q2 family has p>=5 and
is now covered without a separate all-low argument. Its q=n-2
family also has p>=5 and is covered by the opposite-prefix branch.
No run occurred. Endpoint/cut inequalities are strict integer ones;
no unchanged-P invocation outside H<ab is hidden;single translates
are separately repaired. Carrying algebra above remains unreviewed.

**Five-line checkpoint.** Parent:one actual pair boundary meeting both
spectra. Change:all threshold positions now covered at canonical hits
with p>=5,conditional on the displayed hand proof. Repeated assumption:
none newly refuted;the discarded coarse trimming was insufficient,
not a counterexample to spectrum coverage. Dependency risk:MI422/425
and this extension await review;older G319 branches are not used.
Decision:next examine the remaining moment-skip/short-prefix selector
jointly,before proposing another local repair. Gut:interest is supported
by removed threshold hypotheses;reasoned:one uniform domain expanded,
not the full parent. Last trajectory check remains MI423/GC1557
16:02 BST,extra pull allowance unused;13min ACTIVE. Batch this as a
checkpoint for the existing proof discussion,not a new review queue.


### MI427 — B222: skipped moments have triangular opposite excess (2026-10-18 16:53 BST)

**HAND CANDIDATE,unreviewed.** The parent is the same protected
strict-pair branch of P_0. This block examines the actual MI419 selector,
not arbitrary new boundary shapes. Record searched:`skipp|alternate`
AND`staircase|boundary`:29 hits/17 files;MI419/422/425/426 and the
G316 scalar formulas read. No external result or novelty assertion,
no experiment. Fresh git is unchanged;the initial portal checkpoint
was225 seconds old and reused,then refreshed during this block.
Pull:skips and short prefixes should be compared through the selector's
parameters before adding local repairs. The useful new constraint is
that EVERY skipped moment has the same triangular form on the opposite
side. The hand audit of MI426 retained its status and exact endpoint
correction;this block does not count as independent review.

**The common parameter of every skip.** Write the lower staircase
area as H_0=T_k+t,0<=t<=k,and its prefix as p=r-k. If its next
rank move crosses q-1 to q,then

 q=r+k-2t, ell=r-t,
 h=T_k-r+2t+1,
 h+q=T_(k+1)=:A.                                        (1)

For t<k,the moved token is a high;for t=k the move is the
prefix endpoint p-1 to p. These include triangular transitions.
They follow directly from the explicit staircase values and
H_0-ell=h-1. Conversely these equations give that two-unit jump,
when the admissible parameters and h>=0 hold. In particular k>=2:
k0/1 would give h<0 at r>=6. The strict opposite target band gives
A<=cd-2. The parameter t changes the SHAPE,but not its opposite
excess A. This is the organizing constraint for the repairs below.

Use MI419's SAME alternate move:for t<k move rank p-1 to p;
for t=k move the largest rank up1. It achieves the required moment.
We now establish both scalar memberships whenever p>=5.

**Left pool for an interior staircase step,t<k.** Put P=p-1,
K=k+1,so r=P+K. Its physical values are a full prefix[0,P-1]
and K highs P+1+2i+e_i,where

 e_0=0;
 e_i=-1 for1<=i<=k-t;
 e_i=+1 for k-t+1<=i<=k.

This is a SET description of the alternate boundary,not a moment
analogy. The high gaps are<=4,and P>=4 makes every middle low
interval have width>=3. Hence every middle slice fills. In a join,
F_j=sum(first j+1 e)-sum(last j e)<=0:pair indices1..j with
the last j indices,using that e_1,...,e_(K-1) is nondecreasing,
and leave e_00. Thus its gap1-(l-1)(P-l)-2j(K-j-1)+F_j
is nonpositive at all middle joins.

Here A_total=T_K+sum(e)=r+h. The band needed is
[L(a)+A_total-b+1,L(a)+a+ab-1]. If a<=P-1 the first
middle minimum is L(a),below the lower endpoint. Otherwise put
u=a-P>=0,K=u+b. The first middle minimum has excess
T_u+2u+2+sum(first u+1 e). The lower endpoint minus this is

 (b-2)u+L(b)-1+sum(remaining e)
 >=(b-2)u+L(b)-b >=0,                                  (2)

because there are b-1 remaining increments,each>=-1,and b>=3.
At the last end,if a>K all highs are selected and the actual
maximum is L(a)+ab+A_total (the excluded b lows are0..b-1).
If a<=K,the last middle maximum minus the required upper endpoint
is at least

 (a-2)K-L(a)+a-1+sum(last a-1 e)
 >=(a-2)K-L(a)>=a(a-3)/2>=0.                           (3)

Thus the entire required left band is supplied,including equalities
in(2)/(3). No claim that all increments are nonnegative was used.

**Left pool for the triangular transition,t=k.** The low prefix
[0,p-1] stays intact. Its k physical highs are p+1+2i+e_i,
with e_i2 except e_(k-1)3. Their gaps are<=3;middle low
intervals fill them. At joins F_j is2 at j0 and j=k-1,
and1 otherwise (k>=2). Thus the gap is<=3-(l-1)(p-l)-2B,
nonpositive because p>=5. The MI422 endpoint calculation applies
verbatim with these positive increments:the lower margin is
(b-2)u+L(b)-1+sum(remaining e)>=2,or the first slice is
all low. The last endpoint is bounded below by its same calculation,
or is the actual maximum. This supplies the same left target band.
The argument uses the explicit F bound,not the false assertion e<=2.

**Opposite pool for t<k:one high lowered,one raised.** Let K=k+1,
w=s-K. Relative to the ordinary staircase P_s(A),A=T_K,
the actual reflected complement V lowers high number t by1 and
raises the LAST high by1. In formula,its prefix is[0,w-1]
and its K highs are w+1+2i+f_i,where

 f_t=-1, f_(K-1)=+1, all other f_i=0; 0<=t<=K-2.        (4)

For t0,the lowered first high adjoins the low prefix;we still treat
it as a designated high. To check(4),apply MI419's physical
reflection map to Q_s(H_0). For t>0,its negative suffix starts
at t,the physical threshold raises indices>=t+1,and the alternate
prefix move raises the largest remaining value. For t0 all original
highs rise1 and the same last-value move occurs;adjoining the extra
low value gives exactly(4). Total excess is A in both cases.

The reviewed bound A<cd gives w>=3. Middle joins have F_j<=0:
for t>=1 it is
 -1_(j>=t)+1_(j=K-1)-1_(j>=1)+1_(j>=K-t),
and for t0 it is-1 at the two boundary joins and-2 inside.
The ordinary staircase join bound therefore suffices. The first
middle minimum never increases:its high count is0 or at most K-2,
so it excludes the raised last high. The last middle maximum never
decreases:if it uses highs it includes the raised last one,offsetting
any lowered one. If it is the actual maximum,nonnegative rank
displacements or the excluded full low prefix give the same bound.
Consequently G316's endpoint inequalities still cover
[L(c)+A,L(c)+cd],provided the middle slices fill.

All high gaps are<=3 except when t=K-2,the last gap being4.
Thus slice fullness holds for w>=4,or for w3 without that last
four-gap. If w3 and t=K-2,then s=K+3 and
T_K<=cd-2<=s^2/4-2 force s6 or7. These are two actual scalar
shapes,not an unbounded list of hole positions:

 s6,K3,c=d3: V={0,1,2,4,5,9},A6.
 Required triples9..12 are {0,4,5},{0,1,9},{0,2,9},{1,2,9}.
 s7,K4,{c,d}={3,4}: V={0,1,2,4,6,7,11},A10.
 Required triples13..15 are {0,2,11},{1,2,11},{0,4,11};
 complementation in total31 supplies four-sums16..18.

This checks the sole within-slice failure of the width argument.
It is not a numerical extrapolation or a larger census.

**Opposite pool for t=k:an end-modified staircase.** Put K=k+1,
w=s-K as before. Before the alternate largest-rank move,the physical
opposite pool equals Q_s(T_K-1):its prefix is[0,w-1] and only
the LAST high of P_s(T_K) is lowered1. The alternate move removes
w-1 and adds w to this opposite pool. Describe it instead with
prefix length P=w-1 and J=K+1 highs P+1+2i+f_i,where

 f_0=0, f_1=...=f_(J-2)=-1, f_(J-1)=-2.              (5)

The total excess is T_J-J=L(J)=T_K=A. Since w>=3,P>=2;
high gaps are<=2 and every middle low interval has width>=1.
The join correction is0 at j0,J-1 and1 elsewhere. The raw gap
1-A_join-2B+F is<=0:at a boundary F0,A_join>=1;inside,
B>=1. All middle slices fill and join.

For c<=P-1 the first minimum is L(c). Otherwise u=c-P,
J=u+d and the first minimum excess is T_u+u+2;its margin
below the target lower endpoint L(c)+A is

 (d-2)u+L(d)-2>=1.

If c<=J,the last middle maximum minus L(c)+cd is
at least (c-2)J-L(c)+c-2>=L(c)-2>=1.
If c>J the last middle slice reaches the actual maximum,which
is at least L(c)+cd. This proves the same opposite central band
in the triangular-transition case,without a new prefix restriction.

**Result for the selector.** For every skipped moment with lower
prefix p>=5,MI419's alternate boundary supplies the required A target,
and its ACTUAL reflected complement supplies the required C target.
Both other bins are obtained by complementation. Together with MI426:
the chosen selector works whenever its base left prefix is>=5,
whether its moment is a hit or a skip. The unresolved selector cases
have p<=4. In both hit and skip cases their base area obeys

 T_(r-4)<=H_base<=ab+r-2<=r^2/4+r-2,

so r<=16. Therefore this is also a complete HAND CANDIDATE for the
protected strict-minimum-pair branch whenever the chosen pair has
combined size r>=17. It is not the singleton/triple branch or the
whole five-bin theorem. The opposite size remains unbounded in the
r<=16 residual;the statement is not a finite all-parent certificate.

**Literal controls and an unexpected symmetry.** Interior skip:
on S=[0,12] minus6,sizes(3,3,3,3),targets(10,11,26,25),AB
has h0. Singleton slacks4,5,20,19;cross-pair slacks15,14,16,15;
CD30;triple slacks2,1,16,17. Thus the protected strict-pair
hypotheses hold. H_04,k2,t1,q6 skips h;the alternate boundary
and its reflected complement BOTH equal {0,1,2,4,5,9}.
Actual bins are {0,1,9}/{2,4,5}/{3,11,12}/{7,8,10}.
This self-complementary shape is the unexpected check. Its p4 is
outside the general left proof,but its literal partition and opposite
small-width check are valid;it must not be called a p>=5 test.

Triangular skip with p5:on S=[0,13] minus5,sizes(3,4,3,3),
targets(12,17,29,28),AB has h1. Other singleton slacks6,7,23,22;
cross-pair slacks20,19,18,17;CD36;triple slacks3,2,24,19.
The lower H_05,k2,t2 pool has prefix5;the alternate boundary is
U={0,1,2,3,4,8,11},V={0,1,3,4,6,7}. The actual bins
{0,1,11}/{2,3,4,8}/{6,10,13}/{7,9,12} give all targets.
Both controls use actual missing-value pools and disjoint partitions.

**Outcome,niggles,next decision.** Hand candidate,not independently
verified. The key niggles were negative high increments in the LEFT
endpoint proof,one high gap4 with opposite prefix3,and the fact that
a triangular step changes the opposite LOW prefix. Equations(2)/(3),
the two literal scalar shapes,and formula(5) address them separately.
No convex-hull substitution or experimental claim. Earliest pending
support in the combined hit/skip result remains MI422/425/426;this
block's new steps also need review. G319-dependent work stays separate.
Parent coverage expands to the whole strict-pair branch at r>=17.
Next reduce the r<=16 residual to exact left profiles and determine
which opposite spectral guarantees survive their repairs BEFORE any
finite diagnostic. Do not infer a finite full problem from one bounded
side. Gut:the triangular invariant supplies a specific reason for
continued interest. Reasoned:the new common forms removed the moment-
skip gap on an entire regime,not just one fixture. Last trajectory
check remains MI423/GC1557 at16:02 BST,extra pull allowance unused.
No new experiment or separate review request;13min ACTIVE.


### MI428 — B223: isolate the finite left obstruction before testing it (2026-10-18 17:06 BST)

**Hand scope reduction and preregistration;no run yet.** Parent:the
protected strict-pair branch of P_0,serving five-bin sufficiency. The
remaining inference is whether ONE selected boundary meets both spectra.
Record searched:`finite.*left|opposite.*unbounded|short.prefix` AND
`selector|staircase`:7 hits/4 files;MI419/422/426/427 read. This is an
internal scope calculation using G316,not an external theorem or novelty
claim. Fresh main unchanged;portal has no new flags. Pull is specific:
the opposite argument may already be uniform outside the left-prefix
restriction. Verify this before treating the residual as finite.

**The opposite spectrum is already supplied for every selected boundary.**
For a canonical HIT the three threshold regimes in MI426 exhaust q.
The q<p regime leaves Q unchanged. The middle regime uses MI422's SECOND
instrument,whose hypothesis has no left-prefix bound;the w2 corner has
H7,s6,D0 and is unchanged. The opposite-prefix regime forces w>=4
solely from H+D=h+q<=cd-2;MI426's Q punctured-prefix instrument likewise
has no left-prefix hypothesis. For a SKIP,MI427's two opposite formulas
and their endpoint/width arguments require only A=T_(k+1)<=cd-2.
They do not use p>=5. The two w3 exceptions were checked for that
reason,including the p4 control. Thus,conditional on those unreviewed
carrying arguments,the actual opposite pool always supplies
[L(c)+h+q,L(c)+cd]. No modified boundary is licensed by this observation:
a repair would change the complement and create a fresh obligation.

**A finite projection of precisely the unchanged selector.** Only base
prefix p<=4 remains on the left,so6<=r<=16. Take all ordered a,b>=3
with a+b=r and h=0..ab-2. For each such triple take q=1..2r-1,
where the LAST value also represents every q>=2r-1. Use MI419's first
hit/skip rule through K=h+min(q,r),and retain only base p<=4. Test
ALL integers in [L(a)+a+h+1,L(a)+a+ab-1] in the actual U spectrum.

The tail identification is exact on the left. At every H<=h+r,
k<=r-2 and max P_r(H)<=r+k<=2r-2. Therefore for q>=2r-1 every
rank lies below q,ell=r and g(H)=H-r. The first hit is H=h+r,
no skip occurs,and U=P_r(h+r),independent of q. This identifies U
only:V and the opposite parameters still vary,but the uniform argument
above covers them whenever the actual strict-pair hypotheses hold.
Endpoint missing values0,n remain full-interval cases outside this scan.
The finite domain overapproximates actual parents;not every left target
need extend to all14 protected cuts. A failed profile means a failure of
THIS selector band,never nonexistence of a four/five-bin partition.

**Frozen diagnostic predictions and controls.** Before execution:
1. Predict the known q1,r6,a3,h5/h7 holes13/14 recur. Forecast that
   every retained failure has min(a,b)=3;this second prediction may fail.
2. Counterfactual:a failure with both a,b>=4 rejects that localization;
   a missing known negative rejects the instrument. An empty residual
   failure list is incompatible with the controls and is not success.
3. Independent controls:construct every staircase both by formula and
   successive one-token rank moves;check first crossing and alternate
   move identities;compare COMPLETE spectra from bitset cardinality DP
   with literal combinations for every distinct (U,a) tested,not just
   requested targets. Check size,distinctness,absence of q and exact sum.
4. Unexpected check:complementation must match the FULL opposite-size
   spectrum and reflect each entire missing target band,including tail
   profiles;this is left-pool complementation,not the unbounded V proof.
   Explicitly compare the tail representative with q+11 and q+101.
5. Stop after this exact r<=16 domain,or120 seconds,20000 profiles or
   20 million literal combinations,whichever comes first. Any cap or
   mismatch is PARTIAL/FAIL,not a pass;no automatic expansion or repairs.

Source:tests/probes/instinct/ss3_small_left_selector.py. Raw JSONL and
summary remain outside git. Publish this design/source before execution.
Report all failures grouped by r/mode/minsize,retain the raw exact holes,
and decide the next step from their shape. No claim about an exchanged
selector or the full parent follows. Earliest unreviewed dependency is
MI422's opposite instrument plus MI425/426 and MI427;this reduction
adds no new repair theorem or review request. Last trajectory check
MI423/GC1557 at16:02 BST;extra pull allowance unused.


### MI429 — B223 outcome: exactly four left misses,all two-triple profiles (2026-10-18 17:09 BST)

**COMPUTED finite spectra;infinite scope reduction remains HAND CANDIDATE.**
The preregistration and unchanged source were pushed at579048de BEFORE
one invocation. The whole prescribed domain completed in0.805 reported
wall seconds on the GPT Intel worker,not a comparative benchmark:

 - 61589 ordered parameter profiles screened;4058 retained at p<=4;
 - 1226 distinct complete (U,a) spectra compared by bitset DP and
   literal combinations,740952 literal combinations in total;
 - all rank-formula/incremental-walk,moment,missing-value,size and
   complete complement checks passed;702 beyond-tail comparisons passed;
 - exactly4 failed profiles,each missing exactlyONE requested sum.

The complete list,with a=b=3,r=6 throughout:

| h | q | mode | actual U | requested band | sole missing sum |
|---|---|---|---|---|---|
| 3 | 7 | alternate prefix move | {0,1,3,4,6,10} | 10..14 | 12 |
| 5 | 1 | canonical hit | {0,2,3,5,7,9} | 12..14 | 13 |
| 5 | 10 | alternate prefix move | {0,2,3,5,7,9} | 12..14 | 13 |
| 7 | 1 | canonical hit | {0,2,3,5,8,10} | 14 | 14 |

Both preregistered q1 negatives recur. The forecast that every failure
has minimum bin size3 survives the ENTIRE fixed domain;the outcome is
stronger (both sizes3),but that stronger observation was not predicted.
No cap,disagreement,retry,larger domain or repair search occurred.
The full missing bands respect complementation;all four missing sums
are half the respective pool total. In particular the q1 and q10
failures at h5 have identical U but DIFFERENT physical complements.
This is a warning against transferring the q1 repair without checking V.

Source SHA256:
2be9395183013a33945c566d57698f4a30dcd7871d53e844653ef3f7ba36d654
Raw4058-profile JSONL SHA256:
7fdf2cf87ce279a7291f1112abffdd7b12af19ff38d8749dffe2d6630a3f12b6
Raw JSONL/summary are outside git;the committed source regenerates the
fixed output (elapsed time is variable). Raw profile order is fixed.
The computed claim is the finite selector spectrum list,not all-parent
existence;the tail and opposite-side arguments retain their hand status.

**Scope checks on the two new profiles,by hand after the run.** These
are genuine protected strict-pair inputs,not necessarily unrealizable
points added by projecting away the other sizes/targets:

 * q7,h3: S=[0,13] minus7,sizes(3,3,3,4),targets(12,12,25,35).
   Singleton adjusted slacks6,6,19,25;pair slacks in order
   AB,AC,AD,BC,BD,CD are3,16,19,16,19,32;triple slacks
   ABC,ABD,ACD,BCD are4,4,17,17. Total84 is correct.
 * q10,h5: S=[0,15] minus10,sizes(3,3,3,6),targets(13,13,26,58).
   Singleton slacks7,7,20,37;pair slacks5,18,26,18,26,39;
   triple slacks7,6,19,19. Total110 is correct.

These verify admission only,not partitions or failure of the conjecture.
The unbounded opposite families remain the next joint obligation.
The two old q1 profiles already have MI417-418 alternate boundaries
and uniform opposite arguments,still awaiting independent review.
No copying those repairs to q7/q10 is claimed in this block.

**Five-line checkpoint/niggle sweep.** Parent:one actual boundary serving
both target pairs. Change:conditional on the uniform opposite and
long-prefix arguments,the unresolved unchanged-selector spectrum is
now exactly four finite left profiles;two have existing q1 repairs.
Repeated assumption:the already-known universal short-prefix coverage
fails in precisely this finite list;no new repaired mechanism was tried.
Dependency risk:MI422/425/426/427 and the finite projection need scrutiny;
this is not independent verification or a full P_0/five-bin proof.
Decision:next compare the two remaining q7/q10 boundary repairs and
prove their actual opposite spectra uniformly,or refute the proposed
repair immediately. No automatic census expansion. Gut:the tiny exact
failure list is a concrete surprise;interest rests on that compression.
Reasoned:the unbounded-side qualification has been addressed by an
explicit existing argument,not by truncation. Next block still owes
the altered complement proof. Last trajectory check MI423/GC1557,
16:02 BST;extra pull allowance unused.13min ACTIVE.


### MI430 — B224: two exceptional complements close the strict-pair candidate (2026-10-18 17:17 BST)

**COMPLETE COMPUTER-ASSISTED CANDIDATE for the strict-pair branch;
independent review pending.** No new experiment. Fresh shared main
unchanged;initial flag checkpoint reused at under5 minutes,then a
fresh poll showed no new messages. Record searched:`repair|exception`
AND`q1|MI418|two.high|adjacent.high`:73 hits/21 files;MI418's actual
complement proofs,MI419,MI428-429 and G316 scalar machinery read.
No external theorem or novelty claim introduced.

**Short trajectory check before the repairs,17:15 BST.** The parent
has gained a uniform long-prefix argument and an exact finite selector
residual,not just additional isolated instances. The unchanged
short-prefix selector fails one assumption at four profiles;two are
already repaired. The next two repairs are justified only if their
actual complements are handled for every c,d. A merely finite left
fix is inconclusive;do not open a new exception tree after it. Fresh
choice would select this bounded question:two fixed boundaries and
unbounded but explicit complements are now the whole strict-pair gap.
Earliest unreviewed carrying support remains MI422,then MI425/426/427;
a failure there would invalidate the assembled domain,regardless of
these repairs. The finite computation cannot replace those proofs.
Extra pull allowance remains unused. This is an early strategy check,
not a claim of independent verification or a reset by a new label.

**Exact proposed statement.** Let S=[0,n] minus q have n elements,
where0<=q<=n. Let four sizes a,b,c,d>=3 total n and targets u_i
sum to L(n)+n-q. For each nonempty proper group J put
 delta_J=sum(u_j:j in J)-L(sum(size_j:j in J))-sum(size_j:j in J).
Assume every delta_J>=0,and that the global minimum is attained by
at least one pair and by NO singleton or triple. Then S admits the
prescribed four-bin partition. Other pairs may tie the chosen AB.
This claim is restricted to that minimum-cut type;the other P_0
branches and full five-bin sufficiency remain OPEN.

Endpoint q0,n are full intervals and follow from reviewed G316 after
translation where needed. For interior q,set r=a+b,s=c+d,h=delta_AB,
x=u_A-L(a)-a,z=c*n-u_C-L(c). The strict comparisons give
 h<x<ab, h+q<z<cd.
The task is one actual U of size r,sum L(r)+r+h,with u_A in its
spectrum,and V={n-v:v in S minus U} with L(c)+z in its spectrum.
MI429 leaves only four left target failures. MI418 gives uniform
repairs for the two q1 cases. Here are the two remaining repairs,
proved using their own actual complements.

**q7,h3,u_A=u_B=12.** Use
 U={0,1,4,5,6,8}={0,4,8} disjoint-union {1,5,6}.
This is obtained from the failed U by replacing3,10 with5,8,so its
size and total24 are preserved;it avoids7. Direct subtraction from
S gives S minus U={2,3} union[9,n]. Thus,putting p=s-2,

 V=[0,p-1] union {p+5,p+6}, sum(V)=L(s)+10.              (1)

The strict target is L(c)+z with11<=z<=cd-1;hence cd>=12,
s>=7 and p>=5. We prove this entire requested band is present.
Select j=0,1,2 of the two adjacent highs and c-j of the low prefix.
All three low counts lie in1..p-1 because c,d>=3. Each j-slice
is an ENTIRE interval:for j1 the two translates differ by1;for
j0/2 there is one translate. Their extrema increase with j. Writing
the gap as next minimum minus preceding maximum minus1 gives

 j0 to1: 5-(c-1)(d-2),
 j1 to2: 5-(c-2)(d-1).                                (2)

Both are nonpositive for c,d>=4,or for min(c,d)=3 and max(c,d)>=6.
The first slice starts at L(c);the last reaches the actual maximum,
which is at least L(c)+cd by ordered-rank domination. So the slices
cover the required band in these cases.

The ONLY admissible omitted size pairs are (3,4),(3,5) and their
reversals. For c3,d4,p5 the one-high slice is[11,18],containing the
required singleton14. For c3,d5,p6 it is[12,21],containing14..17.
For the reversed sizes use complementation:total V=L(c)+L(d)+cd+10
sends offset z to cd+10-z,which preserves[11,cd-1]. The apparent
small join gaps are outside the requested band,not assumed absent.
This completes the uniform opposite proof for(1).

**q10,h5,u_A=u_B=13.** Use
 U={0,2,4,5,6,9}={0,4,9} disjoint-union {2,5,6}.
This is the same LEFT repair as at q1,h5,but the complement is new.
Here S minus U={1,3,7,8} union[11,n]. Put p=s-4. Then

 V=[0,p-1] union {p+2,p+3,p+7,p+9}, sum(V)=L(s)+15.    (3)

The target offsets satisfy16<=z<=cd-1,so cd>=17,s>=9,p>=5.
Each middle slice with1<=l<=p-1 low tokens and j=c-l highs is
an entire interval. Indeed the four high values have adjacent gaps
at most4;a monotone index path through their j-subsets has steps
at most4,and a low interval has width l(p-l)>=p-1>=4. For j0/4
the high path is a singleton and the same fullness conclusion holds.
At successive middle slices let A=(l-1)(p-l). The four possible
join gaps,for j0,1,2,3 respectively,are

 2-A, -4-A, -4-A, 2-A.                                (4)

For example,relative to high offsets1,3,5,7,the increments are
1,0,2,2;the prefix-minus-suffix corrections are1,-1,-1,1.
The usual gap1-A-2j(3-j)+correction gives(4). Since an actual
middle join has2<=l<=p-1,A>=p-2>=3,all joins close.

If c<=p-1 the first middle minimum is L(c). Otherwise c=p or p+1
(the bound d>=3 excludes larger c),and the first minimum exceeds
L(c) by3 or6 respectively. These lie below L(c)+15. For c>4,the
last middle slice reaches the actual maximum,at least L(c)+cd.
For c3 its maximum is3p+15,where L(c)+cd=3p+6;for c4 it is
4p+18,where L(c)+cd=4p+6. Thus the joined middle slices contain
[L(c)+15,L(c)+cd],which contains every requested target. This
proves(3) uniformly,without importing the q1 complement argument.

**Literal controls and unexpected check.** The two actual protected
instances in MI429 now have explicit partitions:

 q7,n13,sizes(3,3,3,4),targets(12,12,25,35):
 {0,4,8}/{1,5,6}/{3,9,13}/{2,10,11,12}.

 q10,n15,sizes(3,3,3,6),targets(13,13,26,58):
 {0,4,9}/{2,5,6}/{3,8,15}/{1,7,11,12,13,14}.

The sets are disjoint,exhaust the missing-value interval and have the
stated sizes/sums. Unexpected check:for q7,c3,d4 the full triple
spectrum of(1) has actual inter-slice holes10,19,20;the desired14
is present. Thus the proof must cover the target BAND,not falsely
assert full spectral convexity. For q10,the size bound p>=5 follows
from cd>=17,not from the selected left prefix. No hidden bounded-s
check is used. Both repairs are actual sets in S for every admitted n.

**Acyclic assembly and review map.** This is a candidate with a finite
certificate component,not a new all-hand proof:

| Step | Exact obligation | Carrying source/status |
|---|---|---|
| Cut bounds | h<x<ab and h+q<z<cd | MI416;hand reduction |
| Moment selector | correct actual boundary hit/alternate skip | MI419;hand instrument |
| Long left prefix | all required left sums when base p>=5 | MI422/425/426/427;unreviewed |
| Every opposite pool | actual reflected spectrum at all prefix lengths | MI428 scope read of MI422/426/427;unreviewed |
| Finite residual | p<=4 forces r<=16;large q gives constant left pool | MI426/428;hand reduction |
| Small left spectra | only four misses in complete projected domain | MI429,source579048de;COMPUTED with independent controls |
| q1 exceptions | two literal boundaries plus all opposite sizes | MI418 explicit repair paragraphs;unreviewed |
| q7/q10 exceptions | two literal boundaries plus all opposite sizes | this entry;unreviewed |

For a canonical/alternate selector that has no missing left target,
choose an a-subset of U at u_A and a c-subset of V at L(c)+z;
complement within U gives B and inverse reflection gives C,D. For
one of the four misses substitute its corresponding repaired U and
use that repair's OWN opposite proof. This exhausts the finite list.
The broad MI417 q1 deformation proof is not a dependency of this
assembly;only MI418's two exceptional complement calculations are.
G319/G321/G322 and singleton/triple claims are also not dependencies.
G316's reviewed set identity/scalar machinery underlies the selector
arguments. Novelty remains unassessed. No proof status is promoted.

**Niggles/outcome/decision.** Checked literal complements,strict integer
margins,small size exclusions,all four joins in(4),and the two exceptional
gaps in(2). The key nonlocal obligation was the unbounded opposite size;
formulas(1)/(3) discharge it by hand,subject to review. Parent progress:
one entire minimum-cut branch now has an assembled candidate;the full
parent still has singleton/triple branches. Gut:the reduction to fixed
high offsets is satisfying and a specific reason for confidence in
these two repairs,not confidence in every earlier carrying proof.
Reasoned:send ONE batched review request for the assembled branch,
then check/consolidate its earliest unverified arguments before extending
another conditional chain. No census expansion or new descendant.
The heartbeat stays ACTIVE;pending review is not a routine halt.


### MI431 — B225: adversarial audit of the earliest scalar support (2026-10-18 17:31 BST)

**Preregistered supporting audit;not yet run.** Parent:the assembled
strict-pair candidate MI430,not a new descendant. Fresh main/Cloud
flags unchanged. Record searched:`MI422|MI426` AND`audit|endpoint|trim`:
6 hits/1 file;MI422/425/426 and FOUR-BIN-PARTITIONS section7 read.
No external result imported. Unease:the assembly relies on four scalar
instruments that have had hand derivations but no direct independent
literal-spectrum check in their enlarged scopes. This is evidence to
challenge the earliest dependency before adding another theorem.

The hand re-derivation so far finds no contradiction. In MI422's first
instrument the first-middle margin is exactly
(b-2)u+L(b)-1+sum(remaining increments),not just asymptotic positivity.
For the second instrument,the Q negative suffix correction obeys E<=B;
it need not obey E<=1. A newly raised upper tail adds at most1 to a
join. At j0 the join product A=(c-1)(w-c)>=2;at j=k-1,
w-l=d-1>=2 also gives A>=2. Interior high joins have A,B>=1.
These boundary facts validate2-A-B<=0,including a single high token.
Do not replace Q's bound by the P correction bound.

**Frozen domain:** m=6..12,all a,b>=3 with a+b=m. Test precisely:
(1) MI422 first instrument:every p>=5,k=m-p>=1 and nondecreasing
    high increment list in{0,1,2},with total excess A>=m;every nonempty
    asserted band [L(a)+A-b+1,L(a)+a+ab-1].
(2) MI422 second:every Q_m(H),0<H<ab,with prefix w>=3,and every
    upper-tail threshold leaving that prefix unchanged. It suffices to
    raise each suffix of the designated high list,including empty/all.
    Test [L(a)+H+D,L(a)+ab] whenever nonempty.
(3) MI426 punctured P:every staircase with p>=5,each interior q<p,
    H>=q,and every nonempty asserted band. H=T_k+t,0<=t<=k.
(4) MI426 punctured Q:every Q with prefix>=4,each interior q<p,
    and every nonempty asserted band. Enumerate H through m*m;larger
    H cannot satisfy H+m-q<=ab<=m*m/4,so this covers the bounded domain.

Prediction:every asserted band is contained in the literal spectrum.
Counterfactual controls:the two q1,p3 exclusions in MI417 must STILL
miss13/14;neither belongs to the p>=5 domain. Unexpected check:
MI425's relaxed-span p4,q2,translations0,3,6 must miss5 despite5
lying in the proposed trimmed interval. This challenges the geometric
bridge itself,not merely a target calculation.

Independent controls:for EVERY distinct U,enumerate ALL2^m subsets
by literal mask recursion,retaining complete spectra for every
cardinality;compare every full spectrum to a separate bitset cardinality
DP. Check complementation at every size,not only the asserted central
bands. Verify pool size,distinctness and moment for all instruments.
Retain the first unexpected failure with exact U,parameters,target.

Stop on first unexpected failure,any control disagreement,the complete
fixed domain,30 wall seconds or20 million enumerated subsets. A cap
is PARTIAL;no automatic retry,patch,larger domain or promoted theorem.
Source:tests/probes/instinct/ss3_scalar_support_audit.py. Publish design
and source before execution;raw summary outside git. A pass supports
but cannot prove the unbounded hand arguments or count as Cloud's read.
The review request at4190aa69 stays the single carrying queue.


### MI432 — B225 outcome: all four supporting instruments pass the fixed audit (2026-10-18 17:31 BST)

**COMPUTED,one worker;not independent proof verification.** Frozen source
and design were pushed at694a282b before one invocation. The fixed
m6..12 domain completed with no mismatch,cap,retry or changed source:

| Instrument | Nonempty asserted bands checked |
|---|---:|
| MI422 unpunctured left | 1375 |
| MI422 raised Q suffix | 3103 |
| MI426 punctured P | 2736 |
| MI426 punctured Q | 2469 |
| Total | 9683 |

All131925 requested integer values were present. Complete spectra for
1427 distinct pools,at EVERY cardinality,were obtained by literal mask
enumeration (3122368 subsets) and compared with a separate bitset DP:
16430 full-spectrum comparisons,all exact. Complementation at every
cardinality passed. Both q1 missing13/14 negatives and MI425's p4
span-sharpness miss5 survived. Pool size/distinctness/moment checks pass.
The prediction that all asserted bands hold survives this entire
bounded domain;it is not extrapolated to larger m.

Reported wall time0.697496931 seconds on the GPT Intel worker;no speed
comparison. Source SHA256:
5e4527871709c92cc67e85459987ed6ce03e02e989870c1c3a561abfec15f528
Raw complete-spectrum JSONL SHA256:
4faf53c36712ae26a85713556765b843dc9c0e05405289a0145cd69eab6caf26
Raw spectra/summary remain outside git;the frozen source regenerates
this fixed certificate (elapsed time varies). No new parent-domain
census or repair was attempted.

**What this changes.** The earliest unreviewed scalar support now has
direct literal controls across all four asserted configurations at
these sizes,including the small admitted prefixes. This increases
support for MI430 but does not expand its claimed scope or promote
it. The hand audit additionally re-derived both MI422 endpoint margins
and the Q edge-join condition,with no contradiction found. It was a
self-check,not a second reader's carrying review.

**Five-line checkpoint/niggles.** Parent:complete strict-pair candidate,
full P_0/five-bin still OPEN. Change:bounded evidence for earliest
support,not additional parent coverage. Repeated assumption:no new
failure;known short-prefix/weak-span failures retained. Dependency risk:
unbounded MI422/425/426/427 and the scope reduction still need the
independent read requested at4190aa69. Decision:no repeat or wider
support audit;make the carrying hand proof easier to inspect and
reassess the remaining parent gap before another dependent theorem.
Gut:steady interest,but this was verification rather than a fresh
breakthrough. Reasoned:the recorded finite support is now sufficient
for its purpose;further reassuring counts would not close the hand
quantifiers. Last trajectory check MI430,17:15 BST;extra pull allowance
unused. Existing review packet gets this result as an addendum,not a
new review job.13min ACTIVE.


### MI433 — B226: a triple-minimum reflection loses protection on an actual descendant (2026-10-18 17:47 BST)

**Hand scope analysis and explicit countercontrol;not a new partition
candidate or independent review.** The parent remains full-interval
five-bin sufficiency. MI430 addresses exclusive pair minima inside P_0;
it says nothing about a minimum attained on a triple. This block checks
whether reflection sends that remaining branch back into the existing
protected-singleton route. It does not. No experiment or census was run.

Initial pull was towards the orientation issue,with unease about treating
reflection as a free symmetry of an adjusted inequality. This is a new
root question independent of MI430's unreviewed scalar instruments and
G319;it does not extend either conditional chain. Record searched with
record_find.py:`triple.*reflect`,`reflec.*protect`,`least.*triple` gave
no conjunctive paragraph hit. The index and direct source read nevertheless
found MI415's explicit warning,MI362's exact lift gate,and MI368's margin
identity. Read those,MI416,and G315/G316's statement in
FOUR-BIN-PARTITIONS.md. This is an elementary audit of our own reduction;
no external theorem,novelty,or literature-absence claim is made.

**Exact reflection identity.** In P_0 let S=[0,n] minus q,|S|=n,
T=sum(S)=L(n)+n-q,and delta_J=u_J-L(r_J)-r_J. Reflect values in n:
S*=[0,n] minus(n-q),u*_J=n*r_J-u_J. Then

 e*_J:=u*_J-L(r_J)=delta_(J complement)+q,
 delta*_J:=u*_J-L(r_J)-r_J=delta_(J complement)+q-r_J.

The first identity follows by substituting total T and
L(n)-L(n-r)=L(r)+r(n-r). Thus a global least TRIPLE delta becomes a
global least SINGLETON e*,the ordinary lower slack. It need not minimize
delta*,and delta* need not even be nonnegative. Reflected partitions
remain exactly equivalent;the protected hypothesis does not.

Apply the comparison behind MI368 at margin0,without asserting its
margin>=holes hypothesis. If the reflected least singleton A has size a,
then every proper remaining group of size r has u*_J>=L(r)+a*r.
For any actual A realization,trim the remainder to endpoints b,c and
subtract b. Its inherited margin and actual hole count are

 mu'=a-b,
 h'=a+1-b-(n-c),
 mu'-h'=-1+(n-c).

Removing the top value n would recover at least the hole-count margin;
if n remains,the inherited margin is one short. Actual targets might
still satisfy a stronger margin,so this identity alone is NOT a
counterexample to protected membership. The following control tests
that additional possibility as well.

**Strict-triple control.** Take four triples on [0,12] minus1 with
labelled targets (32,23,11,11). Their total is77. The adjusted slacks are

 singles:26,17,5,5;
 pairs AB,AC,AD,BC,BD,CD:34,22,22,13,13,1;
 triples ABC,ABD,ACD,BCD:21,21,9,0.

All14 protected cuts hold;BCD is the UNIQUE minimum. In particular the
example is not covered by MI430's exclusive-pair hypothesis or a tied
singleton choice. Reflection gives pool [0,12] minus11 and targets
(4,13,25,25). Its ordinary least singleton is A,slack1. The ONLY triple
of distinct nonnegative integers summing4 is {0,1,3}:if the least value
were positive,the sum would be at least1+2+3=6,and with0 the only positive
distinct pair is1+3. All these values are available.

Delete it and translate the remaining minimum2 to0. The actual child is

 R=[0,10] minus{1,9}, targets(7,19,19), sizes(3,3,3).

Here h'=2,mu'=1,and the target7 is BELOW L(3)+2*3=9. Therefore the child
really is outside the protected margin2 family,not merely outside the
bound we happened to derive. No alternative realization of this selected
bin repairs that membership;no top-trimming option exists. G315 also
cannot be applied as a one-hole statement to this actual two-hole pool.

**Unexpected check: this occurs inside the original five-bin reduction.**
The full interval[0,14] with five triples and targets(4,38,29,17,17)
lifts the control. Remove {0,1,3},then subtract2 from the remainder.
MI362's parameters are l2,k0,q1,m12,h1:the gate is
12*(2+1)>=2 and u_J>=L(r)+max(r,1-2r). Since r>=3,the latter is exactly
the P_0 cut already checked. The removed size3 singleton has global least
ordinary slack1. Hence this is an actual descendant,not just a point in
the relaxed domain. The reflected intermediate pool itself need not
satisfy P_0,and we have not claimed otherwise.

**Positive controls and niggle sweep.** The child partitions as

 {0,2,5} / {3,6,10} / {4,7,8}, sums7,19,19.

Reflecting and undoing translation gives the original P_0 partition

 {9,11,12} / {5,8,10} / {0,4,7} / {2,3,6}.

Its actual five-bin lift is

 {0,1,3} / {11,13,14} / {7,10,12} / {2,6,9} / {4,5,8}.

The displayed sets check disjointness,all values,count and total without
assuming a partition theorem. As an independent algebra control,
reflection twice gives delta**_J=delta_J because the new hole is n-q
and the complementary size is n-r. The tempting same-margin identity
would instead predict reflected A at least6;its actual target4 refutes
that shortcut. No scalar-spectrum gap or partition nonexistence is
inferred from a failure of the stronger margin condition.

**Trajectory outcome.** Parent coverage has not expanded;an assumption
about its remaining branch has been ruled out at an actual lifted point.
Failure sentence:reflection followed by least-singleton deletion does
not necessarily re-enter the protected family,even when the selected
realization is unique. This is not a new instance of the old universal
bounded-hole assertion:the child has only TWO holes and still fails the
required margin. No new review job,proof entry,or shape-specific repair.

Next cheap test:derive the exact retained inequalities for the reflected
triple-minimum child,including the original q and minimum h,before asking
for a broader theorem. When the reflected recipe uses the full prefix[0,a-2],an available
pivot strictly above it,and retains the original hole above that prefix,
its normalized holes are H=q+h and Q=n-q-a+1. Thus
H+Q=(n-a)+1+h;this relation is lost by
replacing the child by an arbitrary two-hole instance. Check whether those
retained constraints actually exclude the existing two-hole obstruction
families. Stop if they do not distinguish the parent from the parked
unrestricted family;do not renew a leaf-repair budget by renaming it.
Gut:interest in the exact reduction remains;no enthusiasm claim about
another generic hole theorem. Reasoned:the useful result is a sharper
root obstruction and a specified test,not a nearer completion claim.


### MI434 — B227: exact strict-triple child gate and frozen smallest-case test (2026-10-18 17:59 BST)

**Hand reduction UNREVIEWED;diagnostic preregistered,NOT RUN.** Parent:
full-interval five-bin sufficiency,through P_0's remaining triple-minimum
branch. The question is whether the exact retained constraints distinguish
this branch from the arbitrary two-hole family already refuted. Initial
signal:interest in that distinction,with caution about producing another
unclosed descendant theorem. MI430 and G319 are not dependencies here.
Record searched:`two.hole` AND `counterexample|obstruction`:15 paragraphs;
read MI330/350,MI362/368/415/433. Two bounded web searches for prescribed
cardinality/sum partitions with two deletions found no applicable theorem
imported here. Search results were not a carrying source;the elementary
algebra below is derived directly. No novelty or literature-absence claim.

**Exact gate for one specified recipe.** Let the P_0 triple BCD be the
UNIQUE adjusted-slack minimum h>=0,and let the remaining singleton A
have size a>=3;write m for the total size of BCD,n=a+m. Reflect as in
MI433. A's ordinary excess is H=q+h. Consider only the recipe
[0,a-2] union{a-1+H},with original reflected hole a-1+Q,
where 1<=H,Q<=m,H!=Q. The actual normalized child is

 R=[0,m+1] minus{H,Q},
 h=H+Q-m-1>=0, q=m+1-Q,
 sum(v_i)=L(m)+m-h.

All fourteen original proper-cut statements are EXACTLY equivalent to

 v_J>=L(r)+max(r+1,H-(a-1)*r+1)
       for all six proper nonempty groups J of BCD,
 a*m-h>=H+1,

with A itself attaining the minimum. To check this,reflected proper
cuts have ordinary slack at least H+1 except A,whose slack is H.
For J alone this gives the second term in the maximum. For A union J,
subtract A's target L(a)+H and translate by a-1 to get L(r)+r+1.
The cut BCD has ordinary slack a*m-h. These are the six J cuts,six
A-union-J cuts,and A/BCD;no cut is omitted. Conversely reversing the
same identities gives the unique triple minimum and all P_0 cuts.
Tied minima require non-strict inequalities at their corresponding cuts;
they are NOT silently included in this test. Other recipes remain open.

The normalized holes satisfy H+Q>=m+1. MI350's negative with holes1,4
and targets12/12/26 at m9 violates that relation. Its reflection has
holes6,9 but target4 violates even L(3)+3. Thus neither supplies a
negative for this exact child gate. This is evidence to test the gate,
not a proof of compatibility. A hand boundary control shows why strict
cut distinctions matter:holes2,8,targets6/15/24 satisfy the weaker
margin1 cuts,but target6 uniquely forces015;the remainder has no triple
sum15 (the only possibilities using3 would need4+8 or6+6,and without3
the least triple is4+6+7=17). Its P_0 parent on[0,12] minus2 has the positive partition
{9,10,12}/{6,7,11}/{3,4,8}/{0,1,5},sums31/24/15/6,using
another removed-bin realization;no parent failure is inferred. This weak child
fails the strict requirements v_i>=7 and pair targets>=22 below.

**Frozen diagnostic.** Set a3,m9 and all three child sizes3. Then the
exact strict gate reduces to v_i>=7 and v_i+v_j>=22,with correct total,
on the TWENTY unordered hole pairs 1<=H<Q<=9,H+Q>=10. Both orientations
(H,Q) and(Q,H) are tested as separate lifts;they give the same child
pool but different q/parent target. The original P_0 targets are
(33-H,30-v_B,30-v_C,30-v_D). Every such P_0 lifts to an actual full
five-triple interval[0,14] by the removed triple{0,1,q+2},l2,k0.
The diagnostic will check all fourteen P_0 cuts and all thirty original
five-bin cuts literally,independently of the simplified admission gate.

- Prediction:every admitted child in this fixed domain partitions.
  Failure refutes this recipe's child-completion claim,not P_0;on the
  first failure search alternate A realizations in each oriented parent
  and report a positive witness or explicitly unverified negative.
- Controls:complete LABELLED target maps from combinations/complements
  versus token-to-owner recursion;1680 labelled partitions per pool;
  literal witnesses and whole reflected maps. Full-interval three-bin
  rank sufficiency is a reviewed positive control. MI433's child7/19/19
  must be found. No minimum4 or larger pool is added.
- Counterfactuals:MI350,its reflection,and the weak-cut child above must
  remain impossible under both exact engines,despite singleton feasibility.
  They must not be mistaken for admitted strict-child negatives.
- Unexpected check:both orientations must lift all the way to the original
  five-bin minimum-cut gate,not just to relaxed P_0. No positive child is
  called an already proved parent branch.
- Stop:one invocation;first admitted negative or control failure;
  20 wall seconds,10 CPU seconds,2 million recursion nodes. Preserve a
  partial/capped result;no patch/retry/domain enlargement. Raw local only.

Source tests/probes/instinct/ss3_triple_child.py and this design are
published BEFORE execution. This asks whether the exact reduction has
closure on its smallest case. A finite pass permits a hand look at why;
it does not prove the unbounded child theorem or enlarge MI430's status.


### MI435 — B227 outcome: exact retained cuts still do not close the canonical child (2026-10-18 18:01 BST)

**COMPUTED countercontrol,then hand nonexistence proof;not a parent
counterexample.** Frozen source a107087f was published through merge
36b84a4c before the ONE invocation. The intervening commit9fd9bd0a
carried CL442;it was read and ACKed before any adoption. No source
change,retry or expanded domain occurred. The run stopped at the FIRST
admitted negative,on pool7 of20 and target228. The remaining pools and
targets are UNTESTED,not passes. All required controls reached before
that negative passed:12 complete combination/owner maps including the
five control pools,7 whole reflection maps,20160 owner leaves,38640
combination leaves including reflection and alternate-parent searches,
and456 oriented14/30-cut lift comparisons.227 earlier positive child
witnesses are retained. Elapsed0.145717 wall/0.144382 CPU seconds on
GPT's Intel host,not a benchmark.

Raw witness digest:
211fe2d40f302816ee27da8d140a1616b82f7d36772599f66a87b3ffd0ada423
Frozen source digest:
de80a11a5017b42c39f7c9543d6041aa9fee14aea9f029b7b30df6ecb5bde14a
Both checked after execution. Raw witnesses/summary remain outside git.

**The failure,by hand.** On R=[0,10] minus{4,6},take three triples
with targets7,15,23. Their total45 equals sum(R),all singles are at
least7,and all pairs are at least22. H+Q=10=m+1,h0;both orientations
satisfy the exact strict-triple gate,not just its relaxed rank bounds.

The ONLY target7 triple is{0,2,5}. Listing triples of nonnegative
integers summing7 leaves016,025,034,124;all but025 use4 or6.
Reflection in10 preserves R and sends7 to23. Hence the ONLY target23
triple is{5,8,10}. They share5,so simultaneous partition is impossible.
The middle target15 is individually possible as{0,5,10};the other two
are individually possible as displayed. Consequently all pair-union
spectra also pass by complements. The failure is joint compatibility,
not individual scalar availability or a convex-hull mistake.

**Actual parents remain positive.** Orientation H4,Q6 gives P_0
on[0,12] minus4,targets(29,23,15,7). Its singles have adjusted slacks
23,17,9,1;pairs31,23,15,17,9,1;triples22,14,6,0. Thus BCD is uniquely
least. The top-anchored canonical A={6,11,12} leaves exactly the bad R.
Its pivot6 is AVAILABLE:the failure is not an absent-pivot case.
But the following alternative partitions the parent:

 {7,10,12} / {3,9,11} / {1,6,8} / {0,2,5}.

The full five-bin lift on[0,14] has targets7/35/29/21/13 and partition

 {0,1,6} / {9,12,14} / {5,11,13} / {3,8,10} / {2,4,7}.

Orientation H6,Q4 gives P_0 hole6,targets27/23/15/7;canonical
A={4,11,12} again leaves the same bad R. It instead partitions as

 {5,10,12} / {3,9,11} / {0,7,8} / {1,2,4}.

Its full-five-bin targets are9/33/29/21/13,obtained by translating
those four triples by2 and adding{0,1,8}. All size,union,sum and gate
checks are literal. In each orientation a neutral replacement of two
values in A changes the outcome. That observation is a control,NOT a
claim that one such replacement always succeeds.

**Response to CL442's unchecked top-recipe suggestion.** Deleting from
the top really does retain the old lower bounds L(r)+r without reflecting
the child. It may leave TWO holes,so this is weaker than protected
margin2. More decisively,the legal-pivot control above meets all exact
parent cuts and its remainder is impossible. Thus the obstruction is
not confined to an absent pivot. The parent can survive by changing
A;the question is how to select A jointly with completion. Cloud's
suggestion was explicitly unchecked,and this gives it a concrete test.

**Trajectory check before another repair.** Parent coverage did not
increase. MI433 first refuted automatic re-entry to the protected family;
this block then refuted universal completion under the exact retained
constraints. At the broader reduction level both failures challenge the
same assumption:the selected canonical child can be completed without
revisiting the selection. Do not answer with a theorem for R minus one
extra exception. The experiment's stopping rule fires,and the fixed-child
extension stops here. No new proof queue or larger search.

The decision for the next wake is a reading/consolidation block on the
joint selection problem,using these positive ancestors and the exact
first-bin fibres as controls. The original five-bin exclusive-pair branch
is also still separate. Review of MI430 continues independently;G319's
new verification is real progress but does not settle this selector.

Gut:surprise at such a small overlap obstruction surviving every retained
cut,and disappointment that the hoped-for child theorem is false. The
positive parents are the interesting part now:the choice carries the
mathematics. Reasoned verdict:one useful reduction-level refutation with
actual ancestors;no progress claim toward full existence from this run.
Niggle sweep:unique triples proved,strict minimum and both lifts checked,
all controls preceding the failure passed,remaining domain not claimed,
parent positives supplied and no negative-parent inference made.


### MI436 — Adopt CL442's G319 carrying read;keep its applications separate (2026-10-18 18:01 BST)

Read committed CL442/9fd9bd0a and the full G319 entry. Cloud explicitly
re-derived the rank split,parts A-E,MI378 sections1-2,and MI380,including
singletons,scalar omissions and sole-legal-neighbour repairs. This is a
carrying hand read,not promotion from the reported217441 finite checks.
G319 is now PROVED for three bins over TWO labelled intervals with FIXED
POSITIVE per-interval counts and combined individual bounds/total.
Zero-count cases,selection of count rows,and literature novelty are not
part of that conclusion. G320/G321/G322 lose the unreviewed G319 dependency
but remain PROOF-SKETCH on their own unread arguments. MI430 likewise
remains a candidate:CL442's additional53490 strict-pair instances at m16
are supporting finite evidence,not its missing hand verification.

The G319 proof moves out of the waiting room with a scope/review receipt;
its original proof and historical filing notes are preserved. The first
proof_dupes query used G319 while the parser still named the waiting-room
entry W319:the duplicate scan passed but neighbour lookup raised an error.
Correct W319 query passed340 entries,no repeats;nearest G315,G317,G316,
whose distinct scopes are retained in the original filing comparison.
No false full-check pass is claimed for that first invocation.

Cloud's point about flattened gut wording is accepted. The word counts
were evidence of choices that needed correction,not a target for the tone
of every block. I will keep naming surprise or disappointment when the
mathematics prompts them,without manufacturing either warmth or restraint.

Promotion-format checks also caught a repeated dependency receipt and placement
outside the parser's E2 section. Both were corrected before publication;
no generated proof pages or build scripts were edited.


### MI437 — B228: joint selection is the old missing inference; choose incubation (2026-10-18 18:10 BST)

**Reading/consolidation; no new mathematical result or experiment.**
Record searched: `joint.*(select|realiz)|neutral.*(isolat|connect)|canonical.*child`
AND `SS3|P_0|five.bin`: seven hits in two files. Read MI303, MI321,
MI325, MI328's exchange argument, MI330, MI415/416 and the relevant
PRIOR-ART notes on fractional allocation, target exchange and Lawrence
fibres. These are existing source comparisons, not a fresh literature
survey. The current store checkpoint was reused at wake; shared main
was fetched and already up to date. CL442 remains the latest review.

The first signal was curiosity about the alternate first bin in MI435.
The reading adds disappointment: saying “choose it jointly” reproduces
MI325's change of quantifier without supplying its missing construction.
I do not presently have a new testable selector. Fresh choice would take
some distance from this construction rather than enlarge its exceptions.

Three distinctions now govern the return:
- MI303 already shows that individually feasible target pieces can compete
  for one token and need an outside bin. MI435 repeats that compatibility
  obstruction inside an exact, actual descendant. More scalar admission
  bounds alone have not supplied the missing simultaneous choice.
- MI325 correctly allows ANY suitable realization; MI330 proves an actual
  fixed realization can be isolated under ALL neutral two-bin moves.
  Thus the small inward trade in MI435's positive examples is a witness,
  not evidence of a universal local path from a canonical choice.
- MI416's successful direction asked for one common pair boundary whose
  two actual subset spectra contain the two desired values. Its extension
  MI430 remains limited to the exclusive-pair-minimum branch and awaits
  review. Reusing its name does not cover a strict triple minimum.

**Unexpected check:** the seemingly broader global tools are already in
our record. The target base-polyhedron exchange argument connects admissible
sum vectors, not their actual partitions. Lawrence/Markov connectivity
connects existing fibre points, not a desired point whose existence is the
question. G319 supplies joint allocation for fixed POSITIVE counts on two
intervals; it does not choose those counts or turn an arbitrary remainder
into two intervals. None supplies a missing existence implication here.
No new external theorem is imported or pronounced inapplicable in general.

**Decision and scope.** Parent coverage is unchanged this block. The
refuted assumption is fixed-recipe completion; a universal neutral repair
would add another unsupported assumption. G319's verification reduces the
review dependency risk for G320-322 but does not close their own arguments;
MI430 has its separate carrying read. I choose incubation under the owner's
explicit halt allowance and have paused the 13-minute research schedule.
The older schedule was already paused. No routine review approval is needed,
and no new review request is added. Cloud receives the operational pause
as a continuation of the already delivered GC1569 question.

What would reopen work: a concrete selector or augmentation argument that
addresses compatibility across the whole target family, a source supplying
that implication with applicable hypotheses, or renewed owner discussion.
The next cheap test is to compare that proposed implication with MI435's
bad child/positive parents and MI330's isolated realization BEFORE proving
new local cases. With no such implication yet proposed, another census
would not discriminate a new idea. Gut: the problem remains interesting,
but the current repair direction has cooled. Reasoned verdict: incubate;
our counterexample is useful evidence about the strategy, not a disproof
of the five-bin parent. Niggle sweep: no failure transferred from child
to parent, no connectivity assumed, no pending candidate promoted, and no
claim that pausing proves the absence of another productive approach.


### MI438 — B229: CL443 read;one proposed route fails,but group-count compatibility gives a test (2026-10-18 18:50 BST)

**Hand/source assessment;no new experiment or general theorem.** The owner
asks to get current and resume if a reasonable pathway exists. Verified
CL443's commit d10405be,read its ledger entry and both committed source
files,then ACKed. Cloud's finite totals are reported evidence,not replicated
runs here. Its inference that the remaining obstruction is the known open
equal-sum problem is a perspective,not an established reduction or a
classification of all exceptions. Endpoint holes also need trimming before
comparing families by actual hole count.

Record searched:`count.capacit|interval.count|row.count` AND
`group|joint|cut`:14 hits in six files;MI383/384/407,G319 and the new
sscm_test.py are the relevant context. The operations below are elementary
count/rank comparisons,not a new external theorem or novelty claim.

**1. Cheap kill of the natural alternation proposal.** Interpret the
suggested reflected family as U(h'):after normalizing the child to0..M,
with h' actual holes,each proper group of size r satisfies
u_J<=r*M-L(r)-h'*r. Take MI435's P_0 parent0..12 minus4,
sizes3^4,targets29/23/15/7,whose unique minimum adjusted triple is BCD.
Any realization A of target29 omits0,since0+11+12<29. Thus every
nine-token child still starts at0. It has h'=M+1-9=M-8,so its
upper-margin bound for a triple is3M-3-3(M-8)=21. The remaining
target23 violates it for EVERY choice of A. This is stronger than
one failed canonical recipe. In particular the displayed positive
parent with A={7,10,12} still fails this proposed child family.
Consequently lower-to-upper actual-hole-margin closure is false in
this interpretation. A different inherited-margin invariant would
need an explicit statement;it is not refuted merely by this calculation.
No alternation census is warranted for the statement just disproved.

**2. A concrete missing condition in the count test.** Cloud's code
forms each bin's count set using min/max sums separately at each cut,
then checks summed minima/maxima. It does not impose conditional rank
bounds for GROUPS at one common count assignment. Its four-bin example
S=[0,14] minus{6,7,8},sizes3^4,targets21^4 has low interval0..5
and high interval9..14. Each target21 permits low count1 or2:zero
low tokens have minimum30,three have maximum12;both1 and2 are
individually possible. The scalar capacity check4<=6<=8 passes at
this cut. Total low count6 forces exactly TWO bins with count1 and
two with count2. The first two bins jointly need sum42,using two
low tokens and four high tokens. Their minimum is

  (0+1)+(9+10+11+12)=43>42.

Hence NO joint count assignment satisfies the conditional group
bounds. The example passes the original margin test:group sizes3,6,9
have sums21,42,63 against lower bounds12,33,63;total84 is correct.
Thus this retained negative has an elementary group-count explanation;
its passage through independent cut capacities does not establish that
one must solve an unknown equal-sum theorem to explain it.

**Unexpected check:** G319 has THREE bins,where pair inequalities
follow from singleton inequalities plus total. That shortcut fails
for FOUR bins. Importing its singleton-only admission into the new
count problem would erase precisely the two-bin obstruction above.
The known full-interval target-polytope framework still does not
make integer count/rank admission sufficient for actual partition.

Initial pull:the distinction between separately possible counts and
one shared count assignment is concrete enough to test. The reflection
idea disappoints on the existing control;the count obstruction gives
an identifiable next task without repairing another hole shape.
Decision:restart the SAME13-minute heartbeat under the owner's request,
with the fixed diagnostic MI439 next. Parent coverage unchanged;no
proof promoted,no duplicate review request,no M5 job or E28 census.
Niggle sweep:the upper-margin rejection quantifies all A;the four-bin
count contradiction uses disjoint actual tokens;reported Cloud runs
are not self-verified;no exceptional-family classification is adopted.
The next block must distinguish necessary admission from sufficiency.


### MI439 — B230 planned diagnostic: shared interval counts,seven fixed fixtures (registered 2026-10-18 18:50 BST)

**NOT RUN;instrument not yet written.** This records the next bounded
question;publish its source before execution. Does one common interval-
count matrix expose the existing negative fixtures while preserving
literal positive controls? This is diagnostic evidence about representation,
not a proposed all-hole theorem or a new parent-coverage claim.

Split each pool into maximal consecutive intervals [a_j,b_j]. Enumerate
integer matrices c_ij>=0 with bin totals r_i and interval totals b_j-a_j+1.
For EVERY proper nonempty bin group J,put C_j=sum_(i in J)c_ij and test

 sum_j(a_j*C_j+L(C_j)) <= u_J <= sum_j(b_j*C_j-L(C_j)).

These inequalities are necessary:each group must take C_j distinct tokens
from interval j. Total target conservation is checked separately. Keep
zero counts;no G319 application is assumed. Compare existence of an
admitted matrix with exact partition existence on ONLY these fixtures:
1. Cloud's0..11 minus{4,5,6},sizes333,targets17/17/17.
2. Cloud's0..14 minus{6,7,8},sizes3333,targets21/21/21/21.
3. MI435's0..10 minus{4,6},sizes333,targets7/15/23.
4. Its positive P_0 parent0..12 minus4,targets29/23/15/7.
5. Its positive P_0 parent0..12 minus6,targets27/23/15/7.
6. Positive two-interval control{0,1,2,10,11,12},sizes222,targets12/12/12;
   literal pairs{0,12},{1,11},{2,10},one token per interval in every bin.
7. Unexpected countercontrol0..3,sizes1111,targets1/1/2/2:all group rank
   bounds and its sole count matrix pass,but distinct singleton owners
   cannot repeat values. This lies OUTSIDE the minimum-size3 parent;
   it guards against treating a necessary relaxation as an exact solver.

Predictions:1-3 have no admitted matrix;4-6 do;7 does but cannot partition.
For3,the7 triple needs the middle token5 (three low tokens sum<=6;
two low plus a high sum>=8). The23 triple also needs5 (one low plus
two high sum<=22;three high sum>=24). One common matrix must respect
that middle interval's capacity1. No new census is needed to check this.

Independent controls:matrix enumeration by bin allocations versus interval
allocations must agree on the WHOLE admitted-matrix set. Exact target
partition checks use subset/complement recursion versus token-owner
recursion,with direct literal witness checks for positives. Reflect each
whole pool and same-labelled targets using u'_i=M*r_i-u_i;admission and
existence must agree. Preserve the literal positive ancestor partitions
from MI435. Do not infer correctness from agreement alone:the hand
contradictions for1-3 and7 and the supplied positive witnesses carry
independent expected answers.

Stop:one invocation,seven base fixtures plus reflections,10 process CPU
seconds,20 wall seconds,one million recursive nodes total. First failed
control stops as instrument failure;first unexpected prediction stops
and is retained. No patch-and-rerun,larger domain or new exception tree.
If controls pass,the NEXT decision is whether the common-count condition
suggests an actual selection/realization argument on the parent domain;
its seven-fixture success alone does not justify a new sufficiency claim.
If it merely renames compatibility without a new inference,return to the
trajectory check instead of renewing an extra block on that basis.


**MI439 source receipt,2026-10-18 19:05 BST.** B230 instrument is
`tests/probes/instinct/joint_interval_counts.py`. Not executed. Two matrix
engines: recursive bin allocations and Cartesian interval allocations;
whole transportation and admitted sets compared. Bounds checked both
by formulas and literal interval endpoint sums. Independent subset and
owner recursion decide the fourteen fixed base/reflection targets.
Registered caps apply jointly to recursive calls and checked states;
a 20-second external watchdog also applies. Syntax checked in memory,
not a mathematical control pass. Source and this receipt are published
before the single invocation. Record search repeated:
`shared.interval|conditional.group|count.capacit` AND `MI439|21|matrix`
returned seven hits in three files,including this registration. No new
incoming Cloud flags;shared main already up to date. No dependency on
pending G320-322 or MI430 carrying arguments.


### MI440 — B230: joint-count diagnostic completes once (2026-10-18 19:12 BST)

**COMPUTED diagnostic,not a sufficiency theorem.** MI439's source was
published at07ac133f before its single invocation. All seven base fixtures
and their reflections passed,with no retry,patch,domain expansion or cap
increase. The aggregate count is25,631 recursive/checked states;0.066122
process CPU seconds and0.06715017004171386 internal wall seconds on the
Intel host. These are this tiny run's measurements,not a performance claim.
The external20-second watchdog and registered10CPU/1m-state caps were not
reached. Exit0;no instrument error.

| Fixture | All count matrices | Admitted matrices | Actual partition |
|---|---:|---:|---|
| Cloud three-bin17^3 |12|0|no|
| Cloud four-bin21^4 |44|0|no|
| MI435 bad child7/15/23 |30|0|no|
| P_0 parent missing4 |31|2|yes|
| P_0 parent missing6 |44|2|yes|
| Positive two-interval rows |7|1|yes|
| Deliberate size1 countercontrol |1|1|no|

Reflections have the same counts/existence;the ENTIRE admitted maps agree
under interval-column reversal. Across fixtures/reflections338 matrices
were checked,12 admitted,counted separately per case. Independent row-
and column-enumeration match whole transportation/admitted sets;formula
bounds match literal interval extrema. Independent subset/complement and
token-owner recursions agree on exact existence. Returned and supplied
positive witnesses pass direct disjointness,size,sum and count-admission
checks. Hand contradictions in MI438-439 independently predict negatives.
The unexpected size1 control remains admitted but impossible as registered.

Frozen source SHA256:
`4099da45717141db93cdf712b4cad0fabd7bd23a61688d16e04ed30abaf9961c`.
Raw result SHA256:
`6d765cbc218291925ec7fe005f56667d870f979a67b921634a2c59207f64e9cc`.
Raw JSON retained outside git;source remains unchanged. No stronger
coverage inferred:the next hand check below is deliberately adversarial.

### MI441 — B230: the size3 limitation survives;next inference stays explicit (2026-10-18 19:12 BST)

**Hand scope check using existing MI350,not another experiment.** Original
response to the run:the clean discrimination is encouraging;unease is
that joint counts may still disguise the same compatibility gap. Checking
MI350 makes that limitation concrete even with every bin of size3.
Record context:MI439's search,G319 and MI350 section2 reread;no new
external theorem imported or novelty claim. This does not alter the
registered run or retroactively add a fixture to it.

Take S=[0,12] minus6,targets(A,B,C,D)=(4,18,18,32),all sizes3.
For intervals[0,5],[7,12],choose count rows

 A=(3,0), B=(1,2), C=(2,1), D=(0,3).

Row totals are3,column totals6. Every proper group passes conditional
rank bounds. Here are all singleton/pair bounds and targets:

| Group | Lower | Target | Upper |
|---|---:|---:|---:|
| A |3|4|12|
| B |15|18|28|
| C |8|18|21|
| D |24|32|33|
| AB |21|22|37|
| AC |17|22|27|
| AD |27|36|45|
| BC |27|36|45|
| BD |45|50|55|
| CD |35|50|51|

The four triple-group inequalities follow by complement from total72
and full interval column totals. Yet A is forced to{0,1,3},D to{9,11,12}.
Remainder{2,4,5,7,8,10} has no triple18:with zero odd terms the sums are
14,16,20,22;with two odd terms5+7 the third would be the missing6.
Thus common counts plus ALL conditional group rank bounds are NOT a
universal realization criterion,even on two intervals with bin sizes3.
This is outside P_0:target4 violates its lower margin L(3)+3=6.
No P_0/five-bin counterexample,no G319 contradiction (four bins and zeros).

**Trajectory decision.** Parent coverage unchanged;representation improved,
its generic sufficiency explicitly rejected. The recurring assumption to
avoid is that joint rank feasibility already supplies physical ownership.
No dependent proof added;G319 is verified and G320-322/MI430 are unused.
Next cheap test is a bounded HAND audit of G319 with a fourth,one-sided bin,
keeping that bin's subset variable during allocation. Both actual positive
parents admit such a pattern:missing4 has low counts(0,1,1,2),missing6
has(1,1,1,3),as their supplied literal partitions show. MI350 has TWO
one-sided bins,so it must be kept as a negative boundary rather than
silently admitted. A proof for this pattern would still need a separate
P_0 count-selection argument;neither implication is claimed now.

Reason to continue:there is an explicit allocation argument to inspect
and a physical variable it must retain,not just another count census.
Stop that hand block at a valid extension,a counterexample,or an identified
unproved step;the latter triggers strategy reassessment,not another local
repair. Gut:interested but cautious;the pass has not earned renewed blanket
warmth. Reasoned verdict:one concrete mechanism audit is warranted;general
sufficiency remains open. Niggle sweep:checked complement arithmetic,
size3 negative versus protected parent,source-before-run chronology,
independent-map scope and pending statuses. No proof-review request.


**Incoming coordination receipt:**CL444-445 at8fd73e86 verified/read during
publication. Cloud accepts MI438's alternation refutation and group-count
explanation,and supplies six literal SSCM survivors without a rerun.
These are available future controls,not additions to B230's completed
fixed domain. No general exception classification follows from explaining
a finite survivor list. Website sections8/9 read is deferred explicitly.
The bounded allocation hand audit remains next.


### MI442 — B231: what the one-sided extension actually needs (2026-10-18 19:21 BST)

**Hand mechanism audit;known convex geometry applied,not a new partition
theorem. No experiment.** Initial pull is cautious interest in retaining
the fourth bin as a variable. Read MI378/380/382's carrying mechanism.
Record searched:`one.sided|fourth.bin|confined` AND `interval|G319|count`:
56 hits/20 files,mostly unrelated;MI321,MI350,MI378/382 and MI441 are the
relevant scope controls. Literature orientation is recorded in PRIOR-ART.
The audit question was whether the verified three-bin argument itself
supplies the fourth-bin step;its scope does not. A bin confined to one
interval has no other-row contribution available for compensation.

**1. Exact meaning of all fixed-count group bounds.** For interval j
with endpoints a_j,b_j,and prescribed bin counts c_ij,put
C_Jj=sum_(i in J)c_ij. The upper rank function is
F_j(J)=b_j*C_Jj-L(C_Jj). The convex hull of actual row sum vectors is
exactly the total-sum slice with x(J)<=F_j(J). Elementary support proof:
order bin weights decreasingly,and assign the largest available tokens
to those bins in that order with their prescribed counts. This actual
assignment simultaneously saturates every prefix-group upper bound.
Telescoping any weighted objective over this chain proves that these
inequalities and the convex hull have the same support function.
Zero counts are allowed;negative weights cause no issue because total
sum is fixed and weights can all be shifted by a constant.

Apply the SAME bin-weight order independently in every interval. Their
sum support function is attained by actual combined assignments,so the
combined group bounds describe exactly the convex hull of combined
attainable vectors. Lower bounds are complementary upper bounds. Thus
MI440 tests whether an integer target belongs to that convex hull for
some integer count matrix. It does NOT test whether the target itself
is attainable. This is the familiar projection/integrality distinction,
now explicit in the proposed representation,not a novelty claim.

**Unexpected check:an explicit fractional witness for the old negative.**
MI441's target(4,18,18,32) is the midpoint of two ACTUAL target vectors
with the SAME fixed counts:

 A={0,1,3},D={9,11,12} in both;
 B={2,7,8},C={4,5,10} gives(4,17,19,32);
 B={2,7,10},C={4,5,8} gives(4,19,17,32).

The sets are disjoint and cover0..12 minus6. The midpoint is impossible
by MI350's parity argument. Therefore no additional LINEAR inequality
in these bin sums,valid for every assignment at these fixed counts,
can exclude that target. This does not exclude nonlinear/disjunctive
constraints or restrictions inherited from P_0. It changes the plan:
stop searching for further linear group bounds as the missing step.

**2. One-sided fourth bin:rank splitting can be made entirely explicit.**
Normalize two labelled intervals to[0,P-1],[0,Q-1]. Counts are
(a,b_B,b_C,b_D) and(0,k_B,k_C,k_D),with a>=3,b_i,k_i>=1,
b_i+k_i>=3. Write target v_A=alpha and U_N(t)=t*(N-1)-L(t).
Hold A's left sum alpha fixed,not its physical subset. Every left-row
rank inequality is equivalent to sum_i x_i=T=L(P)-alpha and

 ell_i=max(L(b_i),L(a+b_i)-alpha),
 h_i=min(U_P(b_i),U_P(a+b_i)-alpha), i=B,C,D,

along with L(a)<=alpha<=U_P(a). Pair inequalities reduce to these
by complement;there are only three remaining coordinates. The right
row has three bins and rank region sum(y)=L(Q),L(k_i)<=y_i<=U_Q(k_i).
Hence an integer rank split exists precisely when the intervals

 max(ell_i,v_i-U_Q(k_i)) <= x_i <= min(h_i,v_i-L(k_i))

are nonempty and their endpoint sums bracket T. Total conservation
then gives y=v-x. Integer endpoints plus integer T make a real split
integer by distributing the residual among interval capacities.
Part1 shows that the combined group bounds guarantee a real split
into the two row rank regions,so this eliminates rank splitting as
the unknown step for this one-sided pattern.

But the left row has FOUR bins,possibly with singleton counts;G319
has THREE positive counts in EACH row. Neither its theorem nor its
case exhaustion covers this pattern. Integer row sums are still not
integer token ownership. A proof must choose a rank split avoiding
both rows' unrealizable points,or explicitly repair such a split
without changing A's required sum. No such uniform repair is supplied
by this audit. No counterexample to the one-sided extension is claimed.

**Trajectory check and decision.** Parent coverage unchanged;the useful
change is identifying a convex relaxation exactly and ruling out linear
strengthening as a way to remove its internal holes. The repeated
assumption is rank feasibility implying physical ownership;MI441
already rejects it generally. Do not add another dependent theorem.
G319 is verified and the pending G320-322/MI430 arguments are unused.
Fresh choice:the rounding question is still concrete enough for ONE
minimal discriminating test,MI443 below;this spends the extra allowance
rather than renewing it. A pass is not a proof and does not authorize
more sizes. Failure or inconclusive controls trigger reassessment with
no local patch. Gut:the convex diagnosis is satisfying,the extension
itself remains uncertain. Reasoned verdict:one minimal physical test,
then a mechanism or a change of strategy. Niggle sweep:zero counts,
complement bounds,labelled copies,fixed versus free physical subset,
and midpoint witnesses checked by hand;no status upgrade/review job.

### MI443 — B232 registration: one minimal count pattern tests physical rounding (2026-10-18 19:21 BST)

**NOT RUN;source not yet written.** Test only two labelled copies of0..5,
with counts left(3,1,1,1),right(0,2,2,2). All four combined sizes are3;
A is one-sided and B,C,D cross. Translation of the right copy by7
makes the one-hole pool0..12 minus6;fixed counts make this bijective.
This is a small test of the proposed extension,not the entire P_0 domain.

Blind prediction:every integer combined target satisfying ALL fixed-count
group rank bounds is attained. Decide this by comparing COMPLETE target
sets,not samples or one lucky partition. Enumerate actual left/right
allocation sum sets and their sums;independently enumerate literal whole
partitions with interval counts fixed. Enumerate rank targets independently
using total30 and individual/group bounds;compare the complete sets.
There are120 left assignments and90 right assignments,10,800 pairs before
deduplication. These are combinatorial counts to check,not results.

Controls:direct-check every distinct returned target witness;independent
allocation engines and whole target maps;reflect each labelled copy
x->5-x,so combined targets transform to15-v_i;test translation by7
on witnesses. Known positive low A{0,1,2},B3,C4,D5;high Aempty,
B{0,5},C{1,4},D{2,3},targets(3,8,9,10). Counterfactual/UNEXPECTED
control:MI441 counts(3,1,2,0)/(0,2,1,3),normalized targets(4,4,11,11),
must be rank-admitted but impossible;its two midpoint witnesses must
remain actual. This control changes the count pattern explicitly.

One invocation after source publication;10CPU seconds,20wall watchdog,
one million recursive/checked states aggregate. Stop at first failed
control or unexpected negative and retain it;no patch-and-rerun.
A negative rejects the universal one-sided fixed-count extension but
must be separately checked against P_0 before any parent inference.
A pass supports only this smallest pattern;the next action must name
an actual repair argument before any further experiment. Inconclusive
or no mechanism means strategy change/incubation,not more cases.


**MI443 source receipt,2026-10-18 19:31 BST.** B232 instrument
`tests/probes/instinct/one_sided_rounding.py` is ready,NOT RUN.
Record search repeated:`MI443|one.sided` AND `rounding|fixed.count|G319`
returned10 hits/3 files. Independent engines allocate subsets per row
versus assigning all12 labelled tokens to owners. The negative control
comes first;all distinct target witnesses,reflections and translations
are checked before the primary rank scan. Source SHA256:
`49991245b947e568bd3db21d5d19deb7492bb508101e26509e18f300a7b54cd8`.
Syntax-only and publication checks pass,not mathematical controls.
No incoming flags;shared main current. Publish before ONE invocation
with external20-second watchdog;the registered caps/first-failure stop
and prohibition on patch-and-rerun remain.


### MI444 — B232: the one minimal rounding test passes (2026-10-18 19:36 BST)

**COMPUTED,scope exactly MI443.** Source e88b8043 preceded ONE invocation.
The primary row engines enumerate120 and90 assignments;independent whole
ownership gives10,800 leaves. Their complete maps agree on1,234 distinct
targets. The independent rank scan tests1,960 candidate vectors and
admits exactly the SAME1,234. Every stored witness,reflection,translation
and positive control passes. The different-count negative control has
60x60 assignments/3,600 owner leaves/858 distinct targets;the forbidden
(4,4,11,11) remains rank-admitted but absent,with both midpoint witnesses
present. No retry,expanded domain,cap increase or failed control.

165,914 recursive/checked states;0.548504 process CPU seconds and
0.552278028044384 internal wall seconds on the Intel host;exit0.
No registered cap reached. Source SHA256 remains
`49991245b947e568bd3db21d5d19deb7492bb508101e26509e18f300a7b54cd8`.
Raw SHA256 `1a6acfd5930d53658e4dd01404b4b86f51a7bf58c2c2970eefa66ccac5d9e3e8`.
Primary rank/actual target digest both
`4227090c370eda4df4de78050092b9472664b04651feda37024eafe82f18abf2`.
Raw data outside git. These counts establish only the fixed P6,k2 case;
they do not establish the uniform candidate below or test its algorithm.

### MI445 — B232 hand follow-up: ordered representatives supply an actual mechanism (2026-10-18 19:36 BST)

**Complete hand PROOF-SKETCH;independent review pending,novelty unassessed.**
The diagnostic earned no automatic enlargement. The useful response is a
construction:leave three distinct left tokens variable,choose their total
by an ordered unit-step path,and fill the other interval by reviewed MI295.
This removes the proposed dependence on a fourth-bin version of G319.
Record search for ordered intervals/distinct representatives/equal counts
returned111 broad hits/33 files;MI321,MI378/382 and MI442 are relevant.
Two bounded literature searches for prescribed cardinality/sum interval
partitions and interval distinct representatives found no directly
applicable theorem imported here. The elementary interval-order step
is not claimed novel;the theorem's priority remains unassessed.

**Statement (candidate).** Let a>=3,k>=2,P=a+3. Take two LABELLED
integer intervals[0,P-1] and[0,3k-1]. Prescribe counts

 left: (a,1,1,1), right: (0,k,k,k)

for bins A,B,C,D. Every integer target vector satisfying total conservation
and ALL fixed-count group lower/upper rank bounds has an actual partition
with those counts. Translations of either interval merely translate the
fixed-count targets. This is a restricted four-bin fixed-count theorem,
not the general one-sided extension or a universal P_0 count selector.

**Proof candidate.** Put L(r)=r(r-1)/2,K=k^2,gamma=L(k),let alpha
be A's target,and set T=L(P)-alpha,w_i=v_i-gamma for i=B,C,D.
Total conservation gives sum(w)=T+3K. Group bounds are equivalent to

 0<=w_i<=P-1+2K;
 K+1<=w_i+w_j<=2P-3+3K for distinct i,j;
 3<=T<=3P-6.                                             (*)

Indeed the right-row singleton bounds are gamma and gamma+2K;
the right-row two-bin lower/upper sums minus2gamma are K and3K.
The left-row one/two/three-token lower sums are0,1,3,and upper
sums P-1,2P-3,3P-6. Groups containing A are complements of groups
among B,C,D. A's own bounds give exactly the last line of(*).

We need three DISTINCT left tokens x_i with sum T and

 max(0,w_i-2K)<=x_i<=min(P-1,w_i).                         (**)

Then right targets y_i=gamma+w_i-x_i lie in[gamma,gamma+2K]
and sum to L(3k). The verified full-interval THREE-bin theorem MI295
(sizes k,k,k>=2) realizes them;A takes the left complement. Thus proving
(**) constructs physical assignments without assuming G319's extension.

Order B,C,D so w_1<=w_2<=w_3. Both endpoints in(**) are nondecreasing.
Let m_i=max(0,w_i-2K). The coordinatewise least increasing triple
respecting the lower endpoints is

 z_1=m_1,
 z_2=max(m_2,m_1+1),
 z_3=max(m_3,m_2+1,m_1+2).

It also respects the upper endpoints. First,z_i<=m_i+i-1. If m_i>0,
this is <=w_i since2K>=8. If m_i=0,then z_i=i-1: w_1>=0;
w_2>=1 follows from w_1+w_2>=K+1;w_3>=2 follows from
sum(w)>=3K+3. Next m_3<=P-1 by the singleton bound. If m_2>=P-1,
w_2+w_3>=2P-2+4K>2P-3+3K,contradicting(*). If m_1>=P-2,
sum(w)>=3P-6+6K>3P-6+3K,again impossible. Thus m_2<=P-2,
m_1<=P-3,and z_3<=P-1. The smaller coordinates also satisfy this.

**The least sum does not exceed T.** Each z_i-m_i lies between0 and i-1,
so their total excess is at most3. If at least two m_i are positive,

 T-sum(m)=sum(min(w_i,2K))-3K>=K>=4,

which is enough. If none is positive,z=(0,1,2),sum(z)=3<=T.
If only m_3=d>0,then z=(0,1,max(d,2)). Since
T=w_1+w_2-K+d and w_1+w_2>=K+1,we have T>=d+1;
also T>=3. Consequently sum(z)=max(3,d+1)<=T. All cases are covered.

**The greatest sum is at least T.** Reflect both interval copies.
For the crossing bins,w'_i=P-1+2K-w_i;the requested left total becomes
T'=3(P-1)-T. Conditions(*) are invariant (reverse the ordering).
The preceding least-triple argument applied to the reflected data gives
a legal original triple with sum>=T. Equivalently,the coordinatewise
greatest original legal increasing triple h,obtained greedily from the
upper endpoints backwards,has sum(h)>=T.

**No intervening total is skipped.** We have z<=h coordinatewise.
From z,increment the LARGEST index i whose coordinate is below h_i.
All higher coordinates already equal h_j. The increment remains at
most h_i<h_(i+1),if i<3,and respects its upper bound. Lower coordinates
remain smaller. Each move is legal and increases the sum by1;the finite
path ends at h. Stop exactly at sum T. This proves(**),then the
three-bin theorem realizes the right row and A takes the left complement
of size a and sum L(P)-T=alpha. Restore the original bin labels.

**Dependencies and limits.** Only reviewed MI295 is used for physical
completion. No G319/G320/G321/G322 or MI430 dependency,no generic
integer-decomposition assumption. Equal right counts and single left
tokens in B,C,D make the endpoints order together. Unequal counts or
larger left crossing counts require a new argument;this proof asserts
neither. The uniform proof is a candidate pending independent scrutiny.

**Hand checks and niggle sweep.** Tight lower control,for every k>=2:
w=(0,K+1,2K+2),T=3 gives x=(0,1,2). The right bins take consecutive
k-blocks,with sums gamma,gamma+K,gamma+2K. This checks the sole-positive
lower-end case at equality;reflecting gives T=3P-6. As an unexpected
scope check,unequal right counts(2,3,4) would give widths(14,18,20);
sorted w=(16,17,18) has lower endpoints(2,0,0),NOT sorted. Thus the
ordering argument is not silently a proof for arbitrary right counts.
The proof uses no such case and this is not an infeasibility claim.
No new run verifies the general construction. Complement cardinality,
reflection constants,total restoration,ties in ordered w and the largest-
deficit path were checked directly. Parent coverage is still incomplete:
this realizes admitted matrices of one specified family,not all P_0.

Gut:the constructive step is more engaging than the numerical pass.
Reasoned verdict:there is now a specific uniform candidate to scrutinize,
so continuation has a mathematical basis beyond the spent extra-test
allowance. Next cheap hand test:determine whether P_0 admits this exact
count pattern in a nontrivial branch;do not assert that the two earlier
positive parents both fit it. No second experiment or exception repair
is authorized by this block. Send one carrying-review request for MI445,
not requests for the routine convex audit or diagnostic controls.


**B232 closing scope control and filing receipt (19:39 BST).** The existing
P_0 q6 parent with targets(A,B,C,D)=(27,23,15,7) fits G323 after making
D the confined bin and subtracting14 from the other targets. In crossing
order(C,B,A),w=(0,8,12),T=8,K=4. Least and greatest triples are(0,1,4)
and(0,4,5);the unit path reaches(0,3,5). Right normalized pairs are
C{0,1},B{2,4},A{3,5}. Translating by7 yields actual bins
A{5,10,12},B{3,9,11},C{0,7,8},D{1,2,4},with exactly the stated sums
and cover. This is a new explanation of an ALREADY positive parent,
not new parent coverage. The q4 parent does not fit this same matrix.
Arbitrary P_0 sizes need not have three equal crossing bins;even when
they do,admission of these precise counts has not been established.
This limitation is the next strategy test,not permission to add leaves.

Proof filing:proof_dupes --near W323 gives341 entries,no repeated IDs;
nearest W320(.20),W321(.16),W322(.16) read in full. Those are protected
three-bin punctured-pool owner/count applications using G319;G323 is a
four-bin fixed-count construction using MI295 directly. It is not a
replacement verification of those pending applications. No priority claim.
Niggle sweep retained the unequal-count ordering failure and tested the
actual-parent translation/cardinality/sums by hand. Numerical support and
the uniform hand candidate remain distinct. No further experiment.


### MI446 — B233 registration: test parent admission before extending G323 (2026-10-18 19:45 BST)

Hand scope audit only;no experiment or new theorem queue. Parent is P_0
inside the full-interval five-bin question. Prediction:the G323 matrix
will require both a special cardinality profile and an extreme enough
confined-bin target;P_0 alone will not supply it. Counterfactual:if the
protected cuts force some bin wholly to one side of the missing value,
the whole one-sided route remains a plausible parent selector. Kill test:
construct a protected ACTUAL descendant where every bin necessarily
crosses the hole,not merely a case outside G323's equal-count hypothesis.
Controls:literal partition and original five-bin lift,all group cuts by
group size,and reflection. Unexpected check:locate the minimum adjusted
cut to ensure this is in the remaining parent branch,not solely in the
pending exclusive-pair theorem. Stop after this admission verdict;no
larger census or repair of the failed selector.

Record searched:one-sided/singleton-left/count-admission/balanced with
P_0/G323/18s gave10 hits/4 files;MI362,MI433,MI435,MI441-445 read for
scope. A second crossing/balanced search checks the proposed obstruction.
This audits our own reduction by elementary inequalities;no external
result or novelty assertion is imported. G323's earliest unverified step
is its ordered-representative proof,but this audit does not assume it.
All older pending applications remain unused. Initial signal:interest
in the construction,unease about mistaking its clean statement for broad
parent coverage. The prior extra-test allowance remains spent.


### MI447 — B233 outcome: actual parents can force all four bins to cross (2026-10-18 19:45 BST)

**Hand scope result,not a new existence theorem.** G323's matrix can be
used on the two components of a one-hole pool only when the low component
has length P=a+3,the high one length3k,and the four bin sizes are
(a,k+1,k+1,k+1),up to bin relabelling and reflection. At hole q=P,
normalize the crossing targets by

 w_i=u_i-k(P+1)-L(k), T=L(P)-u_A, K=k^2.

Its exact conditional admission test is sum(w)=T+3K and MI445's
three displayed groups of inequalities(*). G323 would realize such an
admitted matrix if its proof survives review. P_0's protected inequalities
do not themselves impose these counts or these conditional inequalities.

**A stronger obstruction than mismatch of G323's cardinalities.** For
EVERY integer r>=3 take S=[0,4r] minus{2r},four bins of size r,and all
four targets2r^2. Total sum is8r^2. For a group of j bins,j=1,2,3,
its protected adjusted slack is exactly

 delta_j=2jr^2-L(jr)-jr=jr*((4-j)*r-1)/2>=0.

Thus every proper P_0 group cut holds. But an r-subset wholly in the
low interval[0,2r-1] has sum at most(3r^2-r)/2,strictly BELOW2r^2.
An r-subset wholly in the high interval[2r+1,4r] has sum at least
(5r^2+r)/2,strictly ABOVE2r^2. Both gaps equal(r^2+r)/2>0.
Consequently EVERY bin in EVERY partition crosses the missing value.
No choice of labels,counts,or which bin to confine can help. Reflection
about2r preserves this instance and interchanges the two impossibilities.
This defeats the universal one-sided-bin selector,not G323's statement.

**Literal existence controls for the whole family.** If r is even,
partition the2r complementary pairs{x,4r-x},x=0..2r-1,into four groups
of r/2 pairs. Each bin has size r and sum2r^2. If r is odd,use the12
central tokens2r-6..2r+6 except2r. Translate the four triples

 {0,8,10}, {1,5,12}, {2,7,9}, {3,4,11}

by2r-6. They are disjoint,cover0..12 minus6 before translation,and
have original sums18,so each translated triple sums6r. Remaining tokens
form2r-6 complementary pairs. Give each bin(r-3)/2 of them:its size
is3+r-3=r and its sum6r+4r*(r-3)/2=2r^2. All central values are
available because r>=3. This is an explicit positive control,not a
nonpartition claim or a new balanced-partition theorem.

**Actual five-bin ancestry,not only relaxed P_0 membership.** Lift to
[0,4r+2] with a size3 bin A={0,1,2r+2},target2r+3. Shift each of the
four residual bins by2;their sizes remain r and targets become2r^2+2r.
These five sets partition the whole interval. A's ordinary lower slack
is h=2r. For j=1,2,3 residual bins their original lower slack is
jr*((4-j)*r+5)/2,which exceeds2r. The lower slack of A together with
j residual bins is2r+delta_j>=2r. The cut of all four residual bins
has slack10r. These are all30 proper cuts (A;four residual bins;14
proper residual groups with and without A). Thus A attains the global
least slack required by the original reduction. Independently,MI362's
lift gate has l=2,k=0,m=4r,q=2r:12r>=4r and
max(s,2r-2s)=s for every proper residual group size s>=r.

**Unexpected branch check.** Within P_0,

 delta_1-delta_3=r>0,
 delta_2-delta_3=(r^2+r)/2>0.

All four triples tie for the minimum;no singleton or pair attains it.
This is in the triple-minimum branch left outside MI430's exclusive-pair
candidate. The r3 case has targets18/18/18/18,where no triple wholly
low can exceed12 and no wholly high triple can be below24. It is already
a positive balanced partition,so the obstruction does not advance parent
existence coverage. It identifies a necessary missing allocation mode.

**Trajectory decision.** Parent:general P_0 and full five-bin remain
OPEN. Change:the proposed one-sided reduction cannot cover an explicit
unbounded family of actual descendants,even after arbitrary relabelling.
Failure sentence:protected parent cuts do not guarantee a confined bin.
This differs from the earlier convex-rank/physical-ownership failure;
it is a representation-level obstruction and calls for a fresh check now,
without waiting for a second example. Dependencies:G323 stays unreviewed,
none of its claims is used here;G320-322/MI430 are not extended.

Fresh choice:the ordered-representative construction is still worth
preserving and reviewing,but it does not currently pull me toward another
parent-solving block. A larger one-sided theorem would miss this family
too. The uniform paired construction for this balanced family is only a
control;promoting it into another special-case programme would repeat the
leaf pattern. I do not currently have a specific mechanism for choosing
and realizing counts with FOUR crossing bins at once. Choose incubation
under the owner's halt allowance and pause the13-minute schedule after
publishing this checkpoint. This is not a wait for routine G323 approval.

Concrete perspective question to Cloud:does the four-crossing allocation
have a useful invariant or coupled-exchange mechanism beyond the rank
convex hull,or should the two-component representation itself be parked?
Please offer a specific mechanism or obstruction,not a larger census.
Reopen on a concrete discriminating test for that missing step,a promising
different representation/problem,or direct owner steering. A positive
G323 review alone does not establish parent admission. Gut:mixed;pleased
with the construction,cooling on this route to the parent. Reasoned:
the extra test is spent and its applicability audit exposed a structural
gap;another automatic extension would not address it.

Niggle sweep:upper/lower confinement bounds have equal positive gap;
all proper group sizes and all30 original cuts counted;odd/even literal
partitions include r3/r4 endpoints;reflection retains the same family;
no missing parent hypothesis is silently discarded. No experiment,probe,
new PROOFS entry,status promotion or duplicate carrying-review request.
Record's second search had86 broad hits/19 files;no claim to have read
all hits or established novelty. The derivation above is self-contained.


### MI448 — Cloud's carrying read and the known integer split (2026-10-18 20:51 BST; B234)

CL446/a33d8bff was fetched, read in full and ACKed after verification. Cloud's
independent carrying read promotes G323 to **PROVED in its stated scope**;
its reported 96,360 support cases are not a GPT rerun. The original MI445
candidate text remains historical. No other pending proof is promoted.

The useful new perspective is that integer rank splitting is already known.
Read Fujishige's primary *Submodularity and Discrete Convexity* slides (2012),
PDF page 22, discrete separation with integrality; read scope and URL are in
PRIOR-ART.md. For arbitrary nonnegative fixed counts l_i,k_i totaling P,Q,
put f(J)=U_P(l_J) and g(J)=v_J-U_Q(k_J). They are respectively integer
submodular and supermodular. Combined upper group bounds say f>=g; equality
on the whole set fixes the total. The known theorem yields integer s with
g<=s<=f; t=v-s satisfies the second row's upper cuts. Complements supply
both lower cuts. This confirms the split for ANY number of bins, including
zero counts, without importing a remembered g-polymatroid intersection formula.

**Known-theorem corollary:** four bins with EVERY per-side count at least three
are realizable by applying verified G316 to both split rows. No new review job
for this composition. This removes a representation-level uncertainty, but
Cloud's “everything after that is theorems” still needs the thin-row repairs
outside this regime. Count selection remains separate. Cloud's SPLIT run was
in progress at CL446; no completion is assumed and no duplicate run is needed.

**Trajectory check.** Parent: five-bin sufficiency through P_0. Actual change:
the general integer split is source-backed; physical realization is now isolated
at thin counts. Repeated failed assumption: a universal one-sided selector remains
refuted by MI447. Dependency risk: the next repair uses only known separation and
PROVED G315/G316, not G320–322 or MI430. Decision: resume a bounded hand repair,
not a larger census. The 13-minute schedule was restarted with its existing prompt;
the older schedule stays paused. This is a new mechanism, not renewal of B232's
spent extra-test allowance or resumption solely because G323 was approved.

Record searched: polymatroid|rank.split|thin with G316|MI442|intersection|integral;
then singleton|thin|one.token with repair|G315|G316. Relevant reads: MI442,
CL446, FOUR-BIN-PARTITIONS.md Lemma 2 and Theorems A/B, and the sources below.
The broad search is a record orientation, not a claim that every hit was read.

### MI449 — One singleton row admits repair in either direction (2026-10-18 20:51 BST; B234)

**Initial signal, recorded retrospectively from this turn.** The attraction was
specific: the one-hole spectrum has isolated omissions, so perhaps the singleton
can move either way while the other row chooses which sign it can afford. Unease:
fixing one scalar omission could simply create another or break a group cut.
This capture is not a preregistration and no experiment was run.

**Question and result.** Two labelled intervals, four fixed-count bins: first row
(1,b,c,d) with b,c,d>=3, second row all counts>=3. Do combined group rank bounds
suffice? **Complete hand candidate G324**, filed with every carrying step in
PROOFS.md; independent review pending and novelty UNASSESSED. This is a specific
thin-count family. It does not establish count admission for P_0.

The integer split comes from MI448. If first-row A takes x and its row is not
realizable, G315 and the exact one-hole scalar spectrum force an offending bin B
of size b with x=b, s_B=L(b)+1, or its reflected upper-edge version. Both vectors
s+e_A-e_B and s-e_A+e_B remain rank feasible AND become physically realizable.
For the first sign, a decreasing group containing B has slack one if it is B
alone, otherwise at least R-b>=3 by its cut with A. For the other sign, a
remaining decreasing group has slack at least bR-1>=2 by its cut with B.
The old B+C cut bars a new lower omission in C; its upper omission would require
the new hole b+/-1 to equal b+d, impossible at d>=3. B's own targets move to
L(b) or L(b)+2, clear of both edge omissions. Reflection handles the upper case.

The high-row rank function has strict submodular gap
k_(X minus Y)*k_(Y minus X)>0 on incomparable groups. Two tight cuts therefore
cannot separately block the two opposite unit transfers between A and B.
One sign is legal; pair it with the opposite first-row repair and use G316
on the high row. The proof uses neither G319 nor any currently pending candidate.

**Niggle sweep and hand checks.** Is the move only scalar-feasible? No: every
decreasing group cut is checked above before G315 is invoked. Can the legal sign
leave the other row unrealizable? G316 applies because all four counts there are
at least three. Does reflection assume protected-parent invariance? No: it proves
a local row lemma only. The explicit G324 control has one sign blocked and the
other sign realized by disjoint literal partitions. Unexpected scope check:
a zero high count can block both directions; the strict-submodularity argument
correctly loses strictness there. No zero-count or size-two extension is claimed.

**What changed:** a uniform one-singleton repair, not another confined-bin case.
**Unresolved:** size-two/multiple thin rows and the parent count selector.
**Gut:** the two legal first-row signs are the part that draws attention; there is
no need to call the whole problem warm. **Reasoned:** the new candidate is short,
uses reviewed dependencies and changes the obstruction, but parent coverage is
conditional on selecting its count pattern. Next cheap test: inspect one size-two
row's obstruction and whether either sign has an analogous repair; do not start
with more enumeration. Cloud receives one carrying-review request for G324;
work need not halt for routine review.

### MI450 — CL447's known exception is detected by pair-count capacity (2026-10-18 21:05 BST; B235)

**Pull, before the calculation:** the exceptional tuple has three large even
paths competing for the same four largest odd tokens. This looks like a count
admission obstruction that can be identified without a census. The planned
size-two row audit is deferred for this one concrete reply to CL447, not abandoned.
Parent remains five-bin/P_0 sufficiency; this block calibrates its count-selection
language against the known graph-burning problem that motivated the work.

CL447/9b50638b was fetched, read and ACKed. The saved G324 packet was successfully
pushed in 918b675a and its REVIEW-REQUEST delivered through the shared store.
G324 remains unverified. No dependency on G324 or the older pending candidates
is used here.

Record searched: 45.?45.?45.?45|72.?74.?74|Conjecture.?2.7|impossibly burnable
returned five hits in three files; relevant prior-art receipts MI266 and the
Tan–Teh source were checked. Primary read: Tan–Teh, arXiv:2312.10914v3,
Introduction (odd-partition equivalence), Definitions 2.3/2.5, Conjecture 2.7,
and Conclusion (the explicit exception). These are known results, not a claim
of discovering a new deficient forest. An initial open of a different Tan–Teh
paper version failed; no assertion is taken from that failed request.

**Hand explanation.** For (45,45,45,45,72,74,74), total 400=20^2, so the token
pool is the first 20 odd integers, 1 through 39. Each 45 needs an odd number of
tokens, at least three because 45>39. Each large even target needs an even
number, at least two. The individual minimum counts are therefore
(3,3,3,3,2,2,2), totaling 18; the paper's singleton count test passes.
Only two extra tokens remain, and parity means they can enlarge at most ONE bin.
Consequently at least two of the three large bins have two tokens each.
Their combined target is at least 72+74=146, whereas ANY four distinct tokens
sum at most 39+37+35+33=144. Contradiction.

Thus this known nonburnability is already excluded at COUNT SELECTION by a
pair-group upper bound. It is not an example of an admitted all-group rank
vector that later fails physical realization. Equivalently, at most one large
bin can have count two, so their counts total at least 2+4+4=10; with the four
small bins' twelve tokens this would require at least 22 tokens. This is a
small clique of incompatible minimum-count choices, not a new saturation
counterexample. No independent proof request is needed for re-explaining the
paper's known example.

**Why 45 is sharp for this particular obstruction pattern.** Keep m=20, four
odd bins needing at least three tokens, and three even bins whose every pair
of targets sums above 144. Sort those even targets u<=v<=w. Since u+v>=146
and v is even, either v>=74, giving u+v+w>=146+74=220, or v<=72, impossible
because u<=v. Equality forces (u,v,w)=(72,74,74). If all paths have length
at least 46, the four odd targets are at least 47 and the total is at least
4*47+220=408>400. At shortest length 45, equality gives exactly the published
tuple. This only classifies this parity/count-congestion pattern at m=20;
it is not a proof of the paper's global uniqueness statement or Conjecture 2.7.

**Independent literal positive control and unexpected equality check.** The
nearby tuple (47,47,47,47,68,72,72), also totaling 400, has the partition

 {1,19,27}; {7,15,25}; {9,17,21}; {11,13,23};
 {3,5,29,31}; {33,39}; {35,37}.

The seven disjoint sets cover every odd token 1 through 39, have the stated
sums, and show that equality at the four-token bound 72+72=144 really is
attainable. The negative argument needs a STRICT excess, not equality. This
is a hand check, not a new computational run or a preregistered experiment.

**Verdicts and next step.** Gut: satisfaction at a short explanation whose
obstruction is visible. Reasoned: the known exception calibrates the need for
pair-group count constraints; singleton capacity alone is too weak below the
stated threshold. No parent coverage or theorem status changes. The fresh
question is whether a size-two row needs physical repair AFTER all group
bounds pass; that question is distinct from this known failure of admission.
Return to that audit next, without initiating Cloud's proposed cross-k census.

### MI451 — A fixed diagnostic before adapting the size-two proof (2026-10-18 21:17 BST; B236, NOT RUN at registration)

Pull: a full interval with only one size-two bin might not need repair at all;
I want to distinguish that from simply failing to adapt the singleton argument.
Parent question stays five-bin sufficiency through P_0. The exact subquestion is
whether rank-feasible row sums for counts (2,3,3,3) on [0,10] are all physically
realizable. This is a first obstruction diagnostic, not a new universal claim.
No pending G324 result is needed. The earliest unreviewed step in a possible
extension is the extension itself, not any result taken as a premise here.

Record searched: size.?2|size.two|minimum.?2 with counterexample|four|SS3;
37 hits in 11 files, relevant G316 proof and scalar lemmas read. Primary
orientation: Hoory–Kotlar 2605.06071v2, Introduction and section 5, again distinguishes
the known equal-sum four-bin result from arbitrary prescribed sums. It does not
supply the statement being tested. No novelty claim or exhaustive literature claim.

**Attempted hand warning before the run — WITHDRAWN at MI452.** The following
argument contained a missed subset; it is retained as a failed check, not a result.
One size-two bin does NOT make every one-hole
three-bin rank vector realizable. Pool [0,8] minus {4}, counts (2,3,3), targets
(4,8,20): the pair of sum four is uniquely {1,3}. Its complement
{0,2,5,6,7,8} has no triple of sum eight (smallest is seven, next is ten).
Each original scalar target is individually possible: {1,3}, {0,2,6},
{5,7,8}; totals are correct. Thus even individual feasibility does not suffice
in that extended one-hole theorem. This is not a counterexample to the full
interval question or G315, whose counts are all at least three.

**Predictions and fixed budget.** Primary: enumerate all 92,400 labelled
partitions for counts (2,3,3,3) on [0,10], and compare their complete sum-vector
set with every integer vector obeying all group bounds and the total. Prediction:
no missing row target. A miss refutes this smallest proposed extension and must
be retained; no patch or enlarged domain this block. Independent control: a
separate token-by-token owner recursion must give the identical complete sum
set and partition count, without using the combination enumerator's helpers.
Positive control: consecutive bins have targets (1,9,18,27). Counterfactual and
negative control: counts (2,2,2,2) on [0,7] must reject the rank-feasible target
(4,4,10,10); two sum-four pairs force {0,4} and {1,3}, leaving no sum-ten pair.
Unexpected check: reflect EVERY attained vector and EVERY rank-admitted vector
in the full interval; both complete sets must be invariant, not merely one sample.
Stop on any disagreement/control failure, on two million recursion nodes or
20 seconds per case, or after these two cases. Partial output is not a pass.
No larger run is implied by success. A pass would motivate a hand proof audit,
not a parent theorem or another census. Data stay outside git.


### MI452 — Smallest full-interval one-size-two case passes; hand warning withdrawn (2026-10-18 21:19 BST; B236)

**COMPUTED, exactly the fixed MI451 domain.** One invocation, no retry, enlarged
domain or cap increase. For counts (2,3,3,3) on [0,10], both independent engines
enumerate 92,400 partitions and obtain the SAME 7,417 target vectors. The
separate all-group rank scan admits exactly those 7,417 vectors: zero misses.
The owner recursion visits 276,924 nodes. Complete reflection of both maps,
the multinomial count, literal token coverage and the consecutive-bin positive
control pass. Reported case time 0.427370142 seconds on the Intel host.

Negative control (2,2,2,2) on [0,7]: 2,520 partitions, 1,259 attainable vectors,
1,289 rank-admitted vectors, 30 missing; the predicted (4,4,10,10) is one.
The independent complete maps agree; all reflection/count/coverage checks pass.
This case took 0.028353085 seconds and 7,365 recursion nodes. These controls
separate actual discrete realizability from mere rank admission.

Source: tests/probes/instinct/one_small_row.py, SHA256
7a0c3ab6d6479898ca69eb4328993d8b2475eac6e4129bf8a9cf467dd1853476.
Raw two-line JSON receipt retained outside git, SHA256
d1fe17adc9cb6a4c5160c7d8c84ad896a961fde8b3ff429a5b8f8212eab67e32.
No shared artifact upload or independent-party verification is claimed.
Registration was written before execution; this subsecond diagnostic was not
pre-pushed as a substantial run. No run status is inferred from the hand result.

**Niggle sweep caught a hand error.** MI451's attempted warning claimed the
remaining set {0,2,5,6,7,8} had no triple of sum eight. It plainly has {0,2,6}.
In fact {1,3}; {0,2,6}; {5,7,8} partitions the original one-hole pool at the
stated targets (4,8,20). The claimed counterexample is WITHDRAWN and the original
reasoning retained above. It is a positive control, not evidence that the
one-size-two one-hole analogue fails. This correction was made before publication;
no proof status or external review was based on the error.

**Decision.** The result does not prove arbitrary (2,b,c,d) sufficiency. It does
remove any need for coupled repair in the smallest such row. Before extending
G324's transfer argument, audit whether a row with just one size-two bin already
obeys the rank criterion, and identify exactly where G315/G316's minimum-three
proof uses the excluded size. A one-hole analogue is also not refuted by the
failed example. No more enumeration is authorized by this block.

Parent coverage has not changed. G324 remains the only newly pending carrying
candidate and is not used here. Gut: the finite pass is useful but not exciting
by itself; the stronger no-repair possibility is the live question, and the
missed subset is a reason to slow the hand checking. Reasoned verdict: finite
positive evidence and a corrected false warning; the general thin-row inference
is OPEN. Next cheap test: audit the size-sensitive joins and endpoint cases in
FOUR-BIN-PARTITIONS.md, without assuming a defect that has not been exhibited.

### MI453 — One size-two row: the strict pair closes; the remaining completion is protected (2026-10-18 21:33 BST; B237)

**Hand audit and unreviewed branch extension; no experiment or new review request.**
Parent remains full-interval five-bin sufficiency through P_0; its count admission
is still open. The present subquestion is whether a single size-two row needs
physical repair at all after the known integral rank split. If the proposed
four-bin extension holds, it discharges that row's realization, not admission
or rows with several thin bins. G324 and G320–322/MI430 are not premises.

Pull: the absence of a demonstrated defect makes me want to inspect the proof
before designing another repair. Unease: the mistaken hand warning in MI451
requires literal checks, not another optimistic analogy. Record searched:
`one.size.two`, `size2 collision`, `MI334` together gave no hit; the broader
`size.?two|size.?2|counts.?2` AND `hole|punctur` gave 45 hits/10 files.
Read FOUR-BIN-PARTITIONS §§6–9 and MI334's actual negative. The latter has
THREE size-two bins, not one. Primary-literature scope remains MI342/MI451:
known equal-sum theorems do not cover these arbitrary targets. No new external
theorem is imported. This is a hand dependency audit, not a larger census.

**1. The staircase central interval also holds for r=2,c>=3.**
Use the P_m(h), Q_m(h), s,t,p,q definitions of FOUR-BIN-PARTITIONS §7,
m=c+2 and 0<=h<2c. The required pair-sum interval is [1+h,2m-3].
h=0 is the ordinary full interval. For h>0, T_s<=h<2(m-2)
forces p=m-s>=3: otherwise T_s>=(m-2)(m-1)/2>=2(m-2), since m>=5.

In P the all-low pair sums fill [1,2p-3]. Taking one low token and
one high H_j fills [H_j,H_j+p-1]. Adjacent H_j differ by at most3,
so these intervals join since p>=3. Their final endpoint is
2m-2+1_(t>0), which exceeds the required 2m-3. The first is
p+1+1_(t=s). It joins the all-low interval unless p=3,t=s.
In that exception m=s+3 and T_s+s<2s+2 imply s<=2; m>=5 then
forces (m,s,t,h)=(5,2,2,5). Here P={0,1,2,5,7} contains the required
pair sums6 and7, witnessed by {1,5} and {0,7}. Thus the central
claim holds, even though its whole pair spectrum has a gap at4.

For Q, t=0 is P. For t>=1 its low prefix q=m-s-1 is at least2.
If q>=3, all-low sums [1,2q-3] join the one-low/one-high intervals:
the first high is q+1, high gaps are at most2, and the final
one-low/one-high sum is exactly 2m-3. Hence the required interval
is covered. If q=2, then m=s+3 and T_s+t<2s+2, with s>=2,t>=1,
leave only (m,h)=(5,4),(5,5),(6,7). Their Q pools and required sums are:

- (5,4): {0,1,3,4,6}, sums5,6,7 via {1,4},{0,6},{1,6};
- (5,5): {0,1,3,5,6}, sums6,7 via {0,6},{1,6};
- (6,7): {0,1,3,4,6,8}, sums8,9 via {0,8},{1,8}.

These are literal hand checks of the entire exceptional central intervals.
No uncomputed enumeration or implicit all-high fullness is used.

Consequently G316's STRICT closest-pair argument extends to counts
(2,b,c,d), b,c,d>=3. Relabel the pair containing the size-two bin so
its selected subset has size two. Its P or Q central spectrum is supplied
above; the other side uses the proved minimum-three lemma. The actual
complement identity of §8 still applies: both side lengths are >=s+3.
The target intervals and conservation are unchanged. This is a branch
extension, not a proof of the entire four-bin statement.

**2. Singleton/triple minima: precisely which part is left.**
Orient a least singleton/triple slack as a lower singleton A, size a,
with s_A=L(a)+h. If A is the size-two bin, the residual three sizes are
all >=3 and G315 applies exactly as in §9: the protected group bound
S_J>=L(C_J)+a C_J excludes scalar edge omissions. Thus this branch closes.
If A is a larger bin, its extremal prefix/suffix/pivot recipe leaves either
a full interval (completed by proved MI295, whose minimum size is two)
or one internal hole with residual sizes (2,b,c), b,c>=3. G315 cannot
be cited for this last case. The scalar bounds alone are not a joint proof.

Here is the exact inherited domain, rather than a request to prove an
unrestricted punctured-pool theorem. Write a=l+k+1, remaining count M,
N=a+M, and choose A as the l smallest tokens, k largest tokens and
pivot p=l+q, 1<=q<=M-1. After subtracting l from the survivors their
pool is [0,M] minus q. Let t_i=s_i-l c_i and t_J=sum_(i in J)t_i.
A direct sum calculation gives h=kM+q. The original minimum-slack
conditions, for every nonempty proper group J of the remaining three,
are exactly

    t_J >= L(r) + max((k+1)r, kM+q-lr),   r=C_J,
    sum_i t_i = L(M+1)-q,
    (l+1-k)M >= 2q.

The first max term comes from the cut A union J; the second from J
itself. The last inequality is the cut of ALL remaining bins, whose
slack is (l+1)M-q. These cuts together with A exhaust the original
nonempty proper groups; upper bounds are complementary lower bounds.
This also checks that no least-slack inequality was dropped during
normalization.

In particular the following SINGLE sufficient completion statement would
finish all the remaining cases of the one-size-two full-row extension:

    H2: On [0,M] minus q, counts (2,b,c), b,c>=3, total conserved,
    t_J >= L(C_J)+C_J for every nonempty proper J implies a partition.

H2 is OPEN. Its margin is inherited for every k>=0, not assumed after
a second deletion. It is weaker than asking for the unrestricted
one-hole individual-spectrum theorem. Conversely every H2 input embeds
in an actual canonical residual of this four-bin method: set k=0 and
choose l>=max(2,ceil(q/2)), a=l+1. Then q-lr<=r for every proper
remaining group r>=2, and (l+1)M>=2q. Define s_i=t_i+l c_i and
s_A=L(a)+q. All full-interval cuts hold and A is a least-slack singleton.
This embedding is only about the selected residual: failure of H2 would
refute this canonical completion method, NOT by itself full-row existence,
since a different A could still complete.

**Niggle sweep / unexpected check.** P_5(5) deliberately has the missing
pair sum4 despite its complete required interval6..7. This catches a false
upgrade from central coverage to full scalar coverage. All Q short-prefix
cases are written literally. Complementation retains the SAME physical pool,
not a separately invented spectrum. In the exact gate, the all-remaining
cut is checked separately; omitting it would falsely enlarge the actual
descendant domain. MI451's withdrawn example stays withdrawn. The old
MI334 negative (2,6,8), counts(2,2,2), also fails the protected pair-bin
lower bound 3 at target2 and is not an H2 counterexample.

**What changed / decision.** The one-size-two full-row audit now has one
remaining completion statement, H2; the strict-pair and thin-minimum branches
have hand arguments. Parent five-bin coverage is unchanged. No extra review
candidate or dependent proof chain is added. Next cheap test is the H2
completion itself, using its inherited margin and the one distinguished pair;
not another broad row census or a list of local hole repairs. A counterexample
must be checked as an actual partition question before being advertised.
Gut: interest is specific to whether that margin removes pair competition;
it is not evidence of success. Reasoned: a useful reduction with an OPEN
joint-realization step, independent of G324. Latest trajectory check remains
MI448; the earlier pull-only extra-test allowance is not renewed.

### MI454 — Test H2 itself, with asymmetric protection retained (2026-10-18 21:42 BST; B238, NOT RUN at registration)

Parent and dependencies: MI453's protected one-hole H2 completion would finish
its one-size-two full-row argument, but not five-bin count admission. The H2
statement is not implied by the completed N11 full-row census: a different
first bin could conceal failure of the selected residual. G324 is unused.
Pull: this is a direct opportunity to reject the reduction rather than extend
its repairs. Record searched: `pair.*(owner|choice)|two.token|size2` AND
`three.hole|one.hole|protect`, 32 hits/5 files. Read MI334's negative and
MI453. No new literature theorem is assumed; this is a diagnostic of H2.

**Fixed experiment, predictions written before execution.** Test all internal
holes q in [0,M] for counts (2,3,3), M8, and (2,3,4), M9: precisely 7+8
small domains. Enumerate complete physical target maps independently by
pair/second-bin combinations and by token-owner recursion. Independently
scan all integer triples of the conserved total satisfying every proper
lower group cut t_J>=L(r)+r. Blind prediction: every H2 target is realized.
A pass is finite support only. Stop at the FIRST H2 counterexample and
hand-check it; do not repair it or increase the domain within this block.
If the prediction passes, derive a structural pair-selection condition next,
not another size increment. A cap/control failure is inconclusive and stops.

Controls: complete-map agreement, multinomial partition count, literal token
coverage and sums, exact original/reflected physical-map identity. Counterfactual:
individual spectra and rank bounds alone falsely admit counts(2,2,2),
P={0,1,2,3,4,6}, target(2,6,8), while the partition map excludes it.
Keep MI451's withdrawn negative as a POSITIVE physical control:
counts(2,3,3), q4, target(4,8,20), partition(13;026;578).
No H2 admission is asserted for that positive control.

**Unexpected check: protection is NOT reflection-invariant.** For M8,q1,
partition(68;027;345) has targets(14,9,12), satisfies every H2 cut.
Its literal reflection has q7, targets(2,15,12), and violates H2's pair
lower bound3 despite being a perfectly valid partition. Check this contrast
explicitly. More generally reflection converts the lower group protection
L(r)+r into a lower bound L(r)+q via the complementary cut; never equate
the two protected admission maps. Only the full physical maps reflect.

Caps: 20 seconds / 1,000,000 owner recursion nodes per domain, 60 seconds
for the whole run. One invocation, no retry/enlargement. Raw output outside
git, source in tests/probes/instinct/protected_pair_row.py. This small run
is registered locally before execution, not announced as a substantial run.
All failures and empty domains will be recorded, without treating a vacuous
pass as evidence of coverage.

### MI455 — H2's two fixed domains pass (2026-10-18 21:46 BST; B238)

**COMPUTED, one invocation of MI454's fixed experiment.** All seven internal
holes for counts(2,3,3) pass: 602 protected targets across the seven domains,
3,920 labelled partitions enumerated by each engine. All eight internal holes
for counts(2,3,4) pass: 1,057 protected targets, 10,080 labelled partitions
per engine. These are domain-target counts, not counts after forgetting q.
Every domain is nonempty. No H2 negative, cap hit, retry or enlargement.
Whole independent maps, multinomial counts, literal coverage, physical
reflection, the unprotected negative and the withdrawn-warning positive pass.
The unexpected protected/nonprotected reflection contrast passes as written.
Summed per-domain times on the Intel host: 0.0396322500 and 0.0943210690 seconds;
the negative control separately reports 0.0013923450 seconds. No speed claim.

Source tests/probes/instinct/protected_pair_row.py SHA256
 e9733b973b9dadc50f41a89ea4f90bf50b443a72c5433d60e87823f1befb27c2.
Raw JSONL retained outside git, SHA256
 8cd6096cb68a5d35bdd4ad8462ca1b8870cff673cf4b779cdf5e8a42506add3a.
No shared artifact upload or independent-party verification is claimed.
The negative control's own H2 subset happens to pass; its required failure
is the explicitly tested rank/individual-spectrum-only target(2,6,8).
H2 remains OPEN beyond the registered cases. No further census follows.

### MI456 — A rank-feasible pair can still fail; keep the union of all pair choices (2026-10-18 21:46 BST; B238 hand continuation)

**Hand reduction and a selector refutation, not an H2 proof.** Let P=[0,M]
minus q, 1<=q<=M-1, counts(2,b,c), b,c>=3, M=b+c+2. Write u for
the pair target, v for the b-bin target, T=L(M+1)-q. H2 is exactly

    3 <= u <= 2M-1-q,
    max(L(b+1), L(b+3)-u) <= v
       <= min(T-u-L(c+1), T-L(c+3)).

The upper bound on u is the complementary b+c cut; the two lower bounds
on v are its singleton cut and its union with the pair. Its upper bounds
are the complementary c and pair-plus-c cuts. Thus no proper group is lost.
For a fixed legal u, let A run through ALL two-element subsets of P of sum u.
The exact remaining assertion is that the displayed integer interval is
contained in the UNION of Sigma_b(P minus A). This keeps physical choices
joint; it is not the sum of separately computed scalar spectra.

**The closest-to-midpoint pair always meets the needed rank bounds.**
There is a particularly simple legal pair A*={x,y}, x<y, x+y=u:
for odd u=2w+1 start with {w,w+1}; if q occupies it, use {w-1,w+2}.
For even u=2w start with {w-1,w+1}; if q occupies it, use {w-2,w+2}.
These pairs are in [0,M] and avoid q. At the lower end u>=3 supplies
all the required nonnegative entries. At the upper end an odd u is
at most2M-3. The only potentially invalid even replacement has u=2M-2,
but then H2 forces q<=1, while an invalid replacement would need q=M-2
(or the forbidden endpoint M); M>=8 excludes it. Thus y-x<=4.

For either remaining size r=b or c, let alpha_r be the smallest r-token
sum in R=P minus A*. I claim

    alpha_r <= max(L(r+1), L(r+3)-u).

Here is a direct proof, including the short exceptional gaps.
If u>=2r+3, then x>=r+1, except that a replacement can give x=r
with q>=r+1. In the first case deleting the pair does not affect the
first r values of P, which lie in [0,r], so alpha_r<=L(r+1).
In the exceptional case all three removed values are >=r, so alpha_r=L(r).
If u<=2r+3 and y<=r+2, take r survivors from [0,r+2]: deleting the
pair and possibly q leaves at least r values, with total at most
L(r+3)-u. Any extra survivor can be dropped since all values are nonnegative.
If instead y>r+2, the gap bound y-x<=4 forces y=r+3 and either
(x,u)=(r-1,2r+2) or (r,2r+3). In the first, q is r or r+2;
alpha_r<=L(r)+2<=L(r)+r+1=L(r+3)-u. In the second,
q is r+1 or r+2 and alpha_r=L(r)<=L(r+3)-u.
This exhausts the cases and proves the inequality.

Consequently H2 puts both requested remaining sums at or above their
actual minima in R. Conservation puts each at or below its actual maximum.
This is a uniform rank-admission result for a PHYSICAL chosen pair, without
G324, any unreviewed count theorem or an assumed joint partition.

**But that pair is not a sufficient selector.** On P=[0,8] minus3, take
counts(2,3,3) and targets(8,7,18). The six H2 lower checks are
8>=3,7>=6,18>=6,15>=15,26>=15,25>=21; total is33.
The closest pair is {2,6}. Its remainder is {0,1,4,5,7,8}; no triple
sums to7. Without0 its minimum is1+4+5=10; with0 no two distinct
remaining entries sum to7. Yet the complete original partition is

    {1,7}; {0,2,5}; {4,6,8}.

Its sizes and sums are exactly(2,3,3)/(8,7,18), and it covers P once.
Thus the obstruction is a scalar gap AFTER a valid physical pair choice,
not a failed H2 target. This is distinct from MI451's withdrawn false example.
No larger run was used to obtain or verify this hand example.

**Decision and niggle sweep.** Do not patch the closest-pair rule with a
new local exception catalogue. The rank difficulty has a uniform argument;
the remaining inference is coverage by the union of all legal-pair spectra
in the displayed interval. Next hand test: use the shared-sum pair family
and the already proved small-hole scalar localization to determine whether
a gap for one choice must be covered by another. Failure of one selector
is not failure of H2, and a finite pass is not its proof. The reflection
control keeps the asymmetric inherited bounds visible. Endpoints, even
replacement validity, all six cuts and literal negative/positive witnesses
were checked above; no status upgrade or new carrying-review job.

Parent coverage is unchanged; the current row's rank-versus-spectrum
obstruction is now explicit. Repeated assumption: a convenient physical
selector might cover every target by itself; this block rejects that selector
and changes to all-choice coverage before any repair. Latest trajectory check
remains MI448; its pull-only extra allowance is not renewed. Gut: the failure
is useful because the rank part survived uniformly; there is a concrete next
inference, not merely a fresh label. Reasoned: H2 stays OPEN, with finite
support and a precise global spectrum-cover question. No new experiment planned.

### MI457 — Adopt Cloud's carrying verification of G324 (2026-10-18 22:00 BST; B239)

Fetched and fast-forwarded 48a1cd79, read CL448 and the entire G324 proof,
then ACKed its READ-LEDGER flag. Cloud independently re-derived all four
carrying steps and authorizes PROVED within the fixed-count statement.
PROOFS.md and the current state now reflect that verification. The proof
text is unchanged; its original candidate provenance is retained.

Cloud's independent g324_check.py enumerates both rows' complete ordered
sum-vector maps and checks combined membership: four patterns, respectively
55,711, 68,348, 73,072 and 84,760 admitted targets, zero failures. Source
read, not rerun here. The total is 281,891 supporting instances. The separate
SPLIT run is still running at CL448's report of 3,632,457 instances; no
completion claim. The hand verification carries the status change.
Duplicate check:342 entries, no repeats; nearest G317 .27, W322 .21,
G315 .21, full entries read. This is not a novelty verdict.

CL448 also accepts MI450's pair-count explanation and withdraws the proposed
cross-k diagnostic; none is run. Its advice to keep all H2 pair choices is
consistent with the current question. G324 has no H2 dependency; H2 below
uses neither G324 nor G320–322/MI430. The review pile has reduced by one,
without promoting the five-bin parent or asserting a new literature result.

### MI458 — All-pair coverage when a bin cannot hit every pair (2026-10-18 22:00 BST; B239, hand only)

**Question and actual pull.** The parent is still five-bin sufficiency;
H2 would discharge MI453's one-size-two row completion. What draws attention
here is that different pairs of the same sum are DISJOINT: the all-choice
formulation has a counting structure that a canonical selector conceals.
This is a specific reason to test that formulation, not renewed confidence
that every protected target will work. Record searched:
`disjoint.*pair|pair.*matching` AND `pigeon|hitting|cover|cardinal`,
28 hits/9 files. Read G318/MI369 and the MI354–355 scope before using them.
The ingredient below is ordinary pigeonhole counting, not a claimed new
matching theorem; no literature novelty claim or experiment.

**Scope correction before reasoning.** MI456 proposed using “already proved
small-hole scalar localization”. The proved three-hole result G318 gives
only the global central interval [L(r)+3r, rM-L(r)-3r] (or its h-hole
version), under its stated size conditions. It is NOT a theorem that every
gap lies within3 of the ACTUAL extrema. MI354–355's distance3 statement
has unreviewed reduction premises and requires both sizes>=4, so cannot
be imported for a size3 bin here. The proved two-hole Lemma3 is narrower
in the number of deletions. No H2 proof has used the stronger statement;
this entry corrects the prospective premise and avoids opening that branch.

**Sufficient region, hand argument.** Retain MI456's P=[0,M] minus q,
counts(2,b,c), M=b+c+2, pair target u, other targets v,w, total T,
and all six protected group inequalities. Let s=min(b,c), and let e be
the number of legal unordered distinct pairs in P summing to u. If e>s,
H2 has a partition.

First each nonpair target of size r is individually feasible in P.
The actual r-token minimum is L(r)+(r-q)_+ <= L(r)+r. The protected
singleton lower bound therefore exceeds that minimum. The protected
complementary bound, whose size is M-r, likewise bounds its minimum and
places the target below its actual maximum. The only possible scalar
omissions from FOUR-BIN-PARTITIONS Lemma2 are: q=r at L(r)+1, excluded
by the lower bound L(r)+r with r>=3; or q=M-r at maximum-1, whose
complement is L(M-r)+1, excluded by the complementary protected lower
bound since M-r>=5. Thus Lemma2 supplies an actual subset B of size s
with the smaller bin's requested sum, without choosing the pair first.

All e legal sum-u pairs are mutually vertex-disjoint: a token x has the
unique partner u-x. B can meet at most s of these pairs. When e>s at
least one whole pair A lies in P minus B. Assign A to the size-two bin.
The remaining tokens have exactly the third bin's size and sum, by total
conservation. This proves the sufficient condition. No three-hole theorem,
G324, or unreviewed joint-completion claim is a premise.

**Exactly what remains.** Put d=min(u,2M-u). The number before deleting q is

    e0 = floor((d+1)/2),
    e = e0-delta,
    delta = 1 if 0<=u-q<=M and u-q!=q, otherwise 0.

Equivalently count smaller endpoints from max(0,u-M) through floor((u-1)/2).
Deleting q removes exactly its one pair when that pair has distinct entries.
The residual e<=s forces d<=2(s+delta)<=2s+2. This is a restriction on
pair availability, not a solution of the remaining domain. In particular,
for b=c=s, M=2s+2, u=M and internal q!=s+1, e=s. Thus an unbounded
BALANCED CENTRAL family remains; the restriction must not be described
as only a small tail or a completed parent branch.

**Hand controls / counterfactual / unexpected check.** At M12,q5,
counts(2,3,7), targets(12,12,49), the five sum12 pairs are
{0,12},{1,11},{2,10},{3,9},{4,8}; e=5>3. One literal partition is
{2,10};{0,3,9};{1,4,6,7,8,11,12}. The six H2 cuts are respectively
12>=3,12>=6,49>=28,24>=15,61>=45,61>=55; total73. Token coverage
and all sums agree. As a countercontrol, e=s is not an impossibility
criterion: MI456's M8,q3,u8 example has e=3 and its alternate partition
still succeeds. The counting proof would fail at equality because B could
meet every pair, not because it must do so.

Unexpected check: a deleted midpoint removes NO distinct pair. At M8,q4,
u8, the pairs are {0,8},{1,7},{2,6},{3,5}, so e=4, not3.
Counts233 and targets(8,9,15) satisfy H2: single bounds3,6,6;
pair-group targets17,23,24 exceed15,15,21; total32. A partition is
{1,7};{0,3,6};{2,5,8}. This checks the delta exception independently
of the positive unequal-size example. No numerical census was run.

**What changed / stop and next test.** A global choice argument completes
an explicit sufficient region, and the remaining obstruction can be stated
without a chosen pair: for a protected target, can EVERY size-s subset of
that sum meet all e legal pairs? At e=s these would be exact transversals,
using one token from each pair and no unmatched token. The next cheap hand
test is this property on the unbounded balanced central family just named,
not a new list of selector repairs. Stop this block after the scope and
boundary checks; do not enlarge the diagnostic or stack a review request.

Niggle sweep: scalar feasibility uses the ORIGINAL one-hole pool, not the
three-deletion remainder; the missing midpoint is handled; e>s is sufficient
only; the residual includes the central balanced family; physical conservation
supplies the last bin. Gut: the global matching observation is attractive,
but its equality boundary is a real limitation. Reasoned: useful partial
coverage/representation change, H2 and parent still OPEN. Latest trajectory
check remains MI448; one convenient-selector failure since it, no renewed
pull-only allowance. G320–322/MI430 are unused. Continue the named global
obstruction on the active schedule; no routine review halt.

### MI459 — Trajectory check before completing the central slice (2026-10-18 22:10 BST; B240)

Parent: full five-bin sufficiency, with count selection and thin-row physical
realization unresolved. H2 would complete MI453's one-size-two row argument;
no such general theorem is claimed. This wake fetched current shared main
(no new commit), read the current question and Cloud's last message, and
polled the store (no changed incoming records).

The named test from MI458 is the balanced central family, not a newly chosen
side problem. Record searched: `transversal|pair.count|midpoint` AND
`H2|protected`:6 hits/2 files, including MI456/458; the broader initial search
was too noisy (210 hits/59 files) and was narrowed. Read the proved scalar
Lemmas2/3 in FOUR-BIN-PARTITIONS before using them. Only elementary counting
and these existing scalar results enter; no new prior-art claim or experiment.

**Trigger and changed decision.** Two restrictions of physical choice have
now failed: MI456's closest pair, and this block's proposed use of an
unmatched token in the other bin. The latter fails at s4,q2,u10,target11:
the unmatched tokens are5 and8; a four-set of sum11 can contain neither
(the explicit check follows in MI460). Both failures break the assumption
that one convenient subclass of physical choices covers every target.
This is the same failure at the level that matters, so the check fires NOW,
before treating another repair as permission for continued leaf growth.

Actual change since MI448: G324 is independently verified, H2 is isolated,
and MI458 supplies the e>s counting region. The parent five-bin theorem has
not acquired a complete new branch. The present central-family argument
has only one remaining boundary in its uniform scalar proof; its explicit
partition completes that entire named family, rather than proposing a new
restricted selector. Complete and record that argument in this block, then
stop. Do not open an adjacent-family repair block or enlarge a census.

Next continuation is the ALL-choice obstruction at pair-count deficit s-e,
using the exact occupancy criterion in MI460, or a strategy change if no
uniform step emerges. That criterion explicitly admits both unmatched-token
and double-pair choices. G320–322/MI430 stay unused; the new central result
will remain an unreviewed hand result, batched rather than a new review job.
No dependent chain is extended. The earlier pull-only allowance remains spent.

Fresh choice: the matching formulation still has a concrete mathematical
question, but another round of preferred-choice exceptions would not be my
choice. The small failure is useful only because it changes the admissible
choices, not because it can be made to sound encouraging. Decision: finish
the promised central test; keep the next work at the whole-choice level.

### MI460 — H2's entire central pair-sum slice (2026-10-18 22:10 BST; B240, hand result UNREVIEWED)

**Claim within H2.** If u=M, H2 has a partition for every b,c>=3 and
internal q. This is a complete hand argument for this slice only, not
independent verification, full H2, or five-bin sufficiency. No experiment.

If b!=c, let s=min(b,c). Then M=b+c+2>=2s+3. The matching of
sum-M pairs has at least floor((M+1)/2)-1>=s+1 edges, even after
one deletion. MI458's pigeonhole argument completes the partition.
Thus it suffices to handle b=c=s, M=2s+2. Write m=s+1,
T=L(M+1)-q, R=T-M=L(M)-q, and H=L(s+1)+1. The six H2
bounds reduce exactly to

    H <= v <= R-H,       w=R-v.

Indeed the pair-plus-bin lower bound L(s+3)-M exceeds L(s+1)
by one. The complementary inequalities give the same lower bound for w.
Relabel the two size-s bins so v<=R/2; this is a BIN exchange, not a
reflection of the protected domain.

**First, q>=s.** If q=m, the missing midpoint destroys no distinct
sum-M pair: e=s+1>s, so MI458 applies. Otherwise choose A={0,M}.
Its complement is [1,M-1] minus q. Translate by -1: the s-subset
spectrum is a one-hole spectrum on [0,2s] minus(q-1). Lemma2 has
no omissions, since both exceptional conditions here require q-1=s,
which has just been excluded. Its actual minimum, before translation, is

    alpha_end = L(s+1)+(s+1-q)_+ <= L(s+1)+1 = H.

Both v and w are at least H, so conservation puts v between the actual
minimum and maximum. A size-s set of sum v and its complement finish.
This covers every q>=s, including q=s at equality.

**Next, q<s and s>=4.** There are exactly s legal sum-M pairs. The
midpoint m and the partner M-q of the deleted token are unmatched.
A size-s subset containing m cannot meet all s pairs, so would leave a
whole legal pair for A. To obtain such a subset, select s-1 tokens in
[0,M] minus{q,m}, then adjoin m. Its attainable sums lie between

    alpha = L(s)+s+1-q = H-q,
    beta  = s*M-L(s)-2.

For the minimum the s-1 tokens are D=[0,s-1] minus q. For the maximum,
the reflected s-1 smallest tokens are [0,s-2], because both reflected
holes exceed s-2; reflection is used here ONLY for this scalar extremum.
The subset size is s-1>=3, complement size s+2>=6, so proved Lemma3
says any omissions are within two of alpha or beta. Moreover

    v-alpha >= q,
    beta-v >= beta-R/2 = (s*s+2*s-5+q)/2 >= 10.

Consequently q>=3 gives the desired subset immediately. For q=1 or2
only the possible sums alpha+1 and alpha+2 need attention. Put r=s-1,
so D=[0,r] minus q. Increasing its sum by1 is possible by replacing r
with r+1. Increasing by2 is possible by replacing r-1 with r+1 when
r-1!=q. The inserted value r+1=s is available (the second hole is
m=r+2). These replacements are distinct-token operations on D.
Thus both low gaps are filled except r3,q2, namely s4,q2, at v=H=11.
All other protected targets in this low-q range have a subset containing m,
and the matching argument supplies a disjoint pair without specifying it.

The sole remaining s4,q2,v11 case has the literal partition

    M10, q2: A={3,7}, B={0,1,4,6}, C={5,8,9,10}.

Sizes are (2,4,4), sums (10,11,32), total53, and every token except2
is used once. It also covers v32 by swapping B,C. This is why the proof
must allow a DOUBLE pair inside B: {4,6} is a full sum10 pair, freeing
another pair even though no unmatched token lies in B.

**Finally, s3 and q<s.** Here M8,H7. For q1, R27 and the endpoint
pair {0,8} leaves [2,7], whose triple spectrum is the full interval9..18.
Since v<=R/2, only v7 and8 remain. They have partitions

    q1,v7: A={2,6}, B={0,3,4}, C={5,7,8};
    q1,v8: A={3,5}, B={0,2,6}, C={4,7,8}.

For q2, R26, the endpoint pair leaves {1,3,4,5,6,7}, whose triple
spectrum is8..18 by Lemma2 after translation (hole1, subset size3).
Only v7 remains, and

    q2,v7: A={1,7}, B={0,3,4}, C={5,6,8}.

The C sums are20,19,19 respectively. Sizes, coverage and conservation
are literal; swapping B,C covers the upper half of each target interval.
Together these cases complete the stated central slice for all b,c>=3.

**Unexpected check / retained failed restriction.** In the s4,q2,v11
case a four-set containing m5 would require a triple sum6 from
{0,1,3,4,6,7,8,9,10}. Without0 the minimum is1+3+4=8;
with0 there is no pair sum6 (0+6 cannot reuse0,1+5 is missing,
2+4 is missing,3+3 repeats). A set containing the other unmatched token8
would require a triple sum3; its smallest possible remaining triple is
0+1+3=4. Thus “always choose an unmatched token” is actually false,
not merely unproved by Lemma3. The displayed B instead doubles a pair.
This is a refutation of a choice restriction, NOT an H2 counterexample.

**Whole-choice criterion for the next block.** In the original sum-u
matching with e edges, for ANY actual size-s subset B let d be the number
of edges wholly in B and z the number of unmatched tokens in B. The number
of edges touched is exactly s-d-z. Hence B leaves a whole pair outside iff

    d+z > s-e.

This includes every physical choice and is equivalent to the missed-pair
condition; it is not itself a sufficiency theorem for a target sum. At e=s,
either an unmatched token OR a doubled edge suffices. At e<s the threshold
is larger, and the central proof does not address it. The unresolved task
is whether H2 forces some size-s subset of the required sum to cross this
threshold, or whether its entire target fibre can stay below it.

**Verdicts / niggle sweep.** Scalar minima/maxima checked in the original
physical pools; two-hole lemma sizes satisfied; s3 handled separately;
all internal q covered; bin exchange kept distinct from reflection; the
midpoint-deletion count and all literal partitions checked by hand.
No three-hole localization, unreviewed count theorem or new numerical run.
Gut: a satisfying completion of the named central test, with a clear reason
the tempting narrower rule failed. Reasoned: H2's u=M slice now has a
complete unreviewed hand proof; general H2 and the five-bin parent are OPEN.
Latest trajectory check MI459, no renewed pull-only allowance. Stop this
bounded block; next work is the global occupancy threshold, not adjacent
families or a new catalogue of selectors. No routine review halt.

### MI461 — One global escape test, not another selector family (2026-10-18 22:21 BST; B241, NOT RUN at registration)

Parent/H2 remain open; MI460's central slice is unreviewed and is NOT a
premise. The all-choice occupancy criterion is exact but not yet a method.
The concrete attraction is a uniform potential: if every blocking subset
can reduce the number of touched legal pairs while preserving its sum,
there is a global escape mechanism. This is not assumed from the finite
existence checks. Record searched: `sum.preserv|neutral|fibre` AND
`H2|matching|pair.choice`,44 hits/14 files. Read the old neutral diagnostic's
scope and MI456/458/460: no general monotone exchange theorem is available.

**Preregistered test.** On exactly the existing counts233/234 domains and
all internal holes, inspect actual size-three subsets B whose target,
together with pair target u and the conserved third target, satisfies H2.
When B touches EVERY legal sum-u pair, enumerate ALL exchanges removing
two tokens and adding two others, preserving the sum. Blind prediction:
some such exchange leaves a legal pair untouched. Since the start touches
all pairs, this is exactly strict decrease of the number touched.

This is a diagnostic of a uniform proposed proof mechanism, not another
partition census. Stop at the first failed state and retain its complete
same-sum fibre and complete exchange-neighbour list. Do not weaken the move
rule, allow a plateau, enlarge sizes, or add repairs in this block. A pass
supports only these fixed domains; a failure rejects the mechanism, not H2.
Caps:20 wall seconds,50,000 inspected states; one invocation/no retry.

Independent controls: enumerate subset fibres by combinations and separately
by all bitmasks; compare the whole fibre maps. Generate neighbours by literal
remove/add exchanges and independently by symmetric difference within the
complete fibre. Check matching edges by pairs and by unique partners.
Positive: q3,M8,u8,B={0,1,6}, target7, escapes to {0,2,5}.
Counterfactual: on P={0,1,2,3,4,6},u2,B={0,6},counts222,target(2,6,8),
there is no escape; it is outside H2 and is the known impossible control.
Unexpected: reflect physical B, matching and full neighbour sets, even when
H2 admission is not preserved. Compare the physical maps only.
Raw output outside git. After a negative, hand-check it and stop; no new
review queue or conditional proof chain follows from this test.

### MI462 — Strict two-token escape fails immediately, while H2 still succeeds (2026-10-18 22:23 BST; B241)

**COMPUTED and hand-checked refutation of MI461's proposed mechanism.**
One invocation; controls passed; stopped at the second inspected state,
also the second blocking state. No complete-domain claim, retry or expansion.
Counts(2,3,3), M8,q1, targets(3,12,20), B={0,5,7}. The only legal
sum3 pair is {0,3}, which B touches. Its complete same-size/same-sum fibre is

    {0,4,8}, {0,5,7}, {2,3,7}, {2,4,6}, {3,4,5}.

Hand completeness: with least element0 the other two sum12, giving48 or57;
least2 gives37 or46; least3 gives45; least>=4 has sum>=4+5+6>12.
The complete two-token-exchange neighbours of B are048,237,345.
Every one touches {0,3}. The unique good member246 shares no token with B,
so cannot be reached in ONE two-token exchange. Thus the strict-escape
claim fails even in the smallest registered domain.

H2's six lower cuts are3>=3,12>=6,20>=6,15>=15,23>=15,32>=21;
total35. The actual partition is {0,3};{2,4,6};{5,7,8}, with sizes233
and sums3,12,20. This is not an H2 counterexample, nor a refutation of
MI460. As an additional hand scope check, a NEUTRAL first step is possible:
057 ->048 ->246, replacing57 by48 and then08 by26. Thus no claim of
disconnected fibres or failure of every nonincreasing path is warranted.
Allowing those paths would be a different conjecture; none is tested here.

The controls compare whole subset maps from combinations and all bitmasks,
complete exchange sets from remove/add and symmetric difference, two matching
constructions, and physical reflection including neighbours. The known
unprotected negative and the positive escape control pass. The negative
stopped the run before the remaining states/domains; they are NOT passed.
Elapsed wall time reported by the one Intel-host invocation:0.000709958s;
no speed claim. Source tests/probes/instinct/h2_pair_escape.py SHA256
 f8266d712ed145ec45c4636491fa44d47e2060e7927a34f97a5c6ac70881f13a.
Raw JSONL retained outside git, SHA256
 732d40c6dd3515f9a1cf9ce15904847143e26d9006ca5c8567e6b8abd59c1400.
No shared artifact upload or independent-party verification is claimed.

**What changed.** The global occupancy criterion survives, but strict local
improvement is not its proof mechanism. The exact complete fibre makes that
failure transparent. No status promotion or new proof-review request.
Niggle sweep: H2 admission checked separately from feasibility; all neighbours
listed; unique good state verified; reflection applies to physical maps only;
neutral path retained so the negative's scope is not exaggerated. Gut: the
quick rejection is clarifying, but I do not have a fresh uniform argument
ready. Reasoned: stop this registered strategy test, not patch its first trap.

### MI463 — Incubate the global-choice step; ask for a mechanism (2026-10-18 22:23 BST)

The named obstruction is still H2: for every protected target, find some
size-s subset with d+z>s-e in the sum-u matching. Pair counting covers e>s;
MI460's unreviewed hand argument covers u=M. Neither supplies a general
principle for the remaining weighted target fibres. The new strict-escape
proposal fails; simply allowing more moves does not establish that a good
member exists. Even a connected target fibre would need that existence
argument, so a connectivity claim alone would be circular as a solution.

Decision under the owner's explicit halt allowance: pause the 13-minute
heartbeat and take a quiet incubation interval. This is my judgement that
the next proposed work needs a fresh mechanism; it is not a routine wait
for G320–322, MI430 or MI460 review. The schedule tool confirms PAUSED;
the older research schedule stays PAUSED. No background calculation/poller.
The saved prompt and cadence are preserved for a later resumption.

Concrete mentoring question to Cloud, delivered with this checkpoint:
can the one-hole geometry prove that the UNION of legal-pair complementary
spectra covers MI456's protected interval without selecting a preferred pair
or assuming a good member of the target fibre? An extremal argument would
need a genuinely global obstruction to ALL choices, not strict descent from
an arbitrary start. Please assess that carrying inference or suggest a
representation that changes it; no larger finite census is requested.

Reopening evidence: a concrete global existence/coverage mechanism, a revised
reduction that removes this inference, or direct owner discussion choosing
a new approach. Existing verified results are preserved, the central slice
is still provisional, H2/five-bin remain OPEN. Fresh-choice verdict: I would
still explore the question with such a mechanism; I would not choose another
sequence of bounded-exchange repairs simply to keep the schedule busy.

### MI464 — CL449 received: finite support accepted, reopening sketch has two failed bounds (2026-10-18 22:37 BST; check-in audit)

Fetched and fast-forwarded 9e6ef411, read CL449, h2_test.py and its imported
enum_targets/margin definitions, verified the committed pointer, then ACKed.
The owner reports Cloud has checked in; this audit assesses the response to
MI463's concrete question. No new experiment or automatic restart.
Record searched: `H2|MI456` AND `slack|minimum`:27 hits/7 files. Read the
G318 statement and MI456/458 scope; no stronger three-hole gap theorem assumed.

**What Cloud reports.** Through M14,73,231 H2 instances, zero failures;
through M13,42,354 instances. These are canonical representatives: b<=c,
and the target enumerator orders equal-size adjacent bins. Endpoint holes
are included, unlike our earlier fixed domains. Source read, not rerun;
these wider counts are Cloud's reported supporting computation, not a proof.
The source checks all legal pairs, and separately scores the most spread and
closest-to-midpoint choices. Its `any` counter is the union over ALL pairs;
it does not separately score the union of just those two extreme choices.
Those two tested rules fail on some targets; no conclusion about every
possible selection rule is inferred.

**First failed bound in regime2.** Take M9,q1,counts(2,3,4),targets(4,11,29).
The only legal sum4 pair is {0,4}: {1,3} is excluded by q1. Its complement
is {2,3,5,6,7,8,9}, whose minimum triple sum is10. The sketch's claimed
upper bound on that minimum is L(3)+2*3+1-4=6, so it is false.
Protection starts at max(L(4),L(6)-4)=11: actual lower slack1, not the
claimed b+2=5. All six H2 checks hold:
4>=3,11>=6,29>=10,15>=15,33>=21,40>=28; total44.
The valid partition is {0,4};{2,3,6};{5,7,8,9}. This refutes the
slack justification, not H2 or the existence of a covering proof.

**Second failed bound in regime2.** The claim that u>=2b+3 supplies a
legal pair with BOTH entries>=b+1 fails at M9,b3,q4,u9. Only {4,5}
could have both entries>=4, and4 is deleted. The legal pairs are
{0,9},{1,8},{2,7},{3,6}. This is the previously retained boundary
exception in MI456, not a new H2 obstruction. For a positive admitted
control, targets(9,12,20),counts234 have the partition
{0,9};{1,3,8};{2,5,6,7}. The six cuts are9>=3,12>=6,20>=10,
21>=15,29>=21,32>=28; total41. Thus neither failed bound depends on
an impossible input or a three-hole size exception.

G318's stated central interval is valid and useful. But its complement
bands are not supplied by an already proved general distance-from-ACTUAL-
extrema gap list at size3. MI458 already distinguishes that missing claim
from G318 and the proved TWO-hole lemma. The two countercontrols above
prevent accepting the offered slack argument as that missing bridge.
No claim is made that every part of CL449's sketch is false.

**Decision / response.** The wider finite support is welcome; the offered
uniform mechanism is not yet sound enough to reopen a block. Keep both
research schedules PAUSED. Send Cloud the two hand countercontrols and
ask specifically for a corrected uniform end-band estimate or a global
covering mechanism that avoids these premises. Its offered larger slack
check is unnecessary to find these failures; no extra census is requested.
This is proof pushback on its merits, not transferring the judgement to Cloud.

Niggle sweep: matching lists complete by enumerating the tiny possible
smaller endpoints; minima literal; all six original H2 cuts and disjoint
positive partitions checked; M9 satisfies G318's ambient-size gate. Finite
counts labelled as reported canonical instances; all-pair and two-policy
unions kept distinct. H2/parent OPEN; MI460 still unreviewed. Gut: interest
in the global question remains, but these inequalities do not yet change the
incubation verdict. Reasoned: useful check-in and precise corrections;
no justified schedule restart yet. A corrected carrying mechanism or direct
owner discussion can reopen the work.

### MI465 — CL450's correction and its exact dependency (2026-10-18 22:55 BST; follow-up audit)

Read and merged 7801ed74/41db7578, including CL450, h2_bands.py,
h2_depth.py and the cited S25 reflection; verified the flag pointer before
ACK. Cloud accepts both MI464 controls, corrects the minimum formula when
all three deletions are in the bottom block, and withdraws its third
all-pairs rank-admission estimate. Those corrections are consistent with
the literal pools. They do not affect G315/G316/G318/G324 or H2's status.

Cloud reports exhaustive three-hole spectra for M8..14: except the known
M8 exceptions, no missing sum at distance>=5 from both actual extrema.
It reports72,818 canonical H2 instances at M9..14,63,830 admitting a
pair of depth>=5,8,988 all-shallow;721 failures of its particular deepest
pair policy, all in the shallow regime. Both sources read, NOT rerun here.
These are finite reported measurements. Their fractions are not coverage
fractions of the unbounded theorem. Deepest-pair sufficiency is CONDITIONAL
on proving the proposed universal scalar gap bound; it is not proved now.

Record searched: `three.hole|three.*deletion` AND
`distance.*3|distance.*4|buffer12`:4 hits/2 files. Read MI354–355 in full
and MI371's relevant source scope. The min(r,t)>=4 part already has a
STRONGER distance3 finite-basis candidate:48,896 complete normalized domains,
with MI353's paired-window buffer12 and MI354's truncation as unread hand
premises. It is not independently PROVED. CL450's size3 side is new to
that basis and must not be imported from it. Thus a fresh scalar census
would overlap a large existing computation; reviewing/proving its carrying
reduction, not repeating it, would be the appropriate scalar task.

The correction replaces a false estimate with a well-posed candidate lemma
and an explicitly open all-shallow case. I accept that as a better research
program. The remaining choice is whether it changes our parent obstruction
enough to resume, rather than whether the measured lemma sounds plausible.

### MI466 — The all-shallow regime is unbounded even far from the original extrema (2026-10-18 22:55 BST; hand scope control)

This parameterizes MI462's old control; no new experiment, catalogue or proof
review request. For every s>=4 put M=2s+2,q1,counts(2,s,s), and prescribe

    u=3, v=L(s)+3s, w=L(s)+s*s+3s-1.

Total conservation is3+v+w=L(M+1)-1. The pair lower bound is tight;
both singleton lower bounds hold. The A+B cut is tight because
3+v=L(s+3); the A+C slack is s*s-1; the B+C slack over L(2s+1)
is4s-1. Hence every input satisfies H2, with M>=10.

Only {0,3} is a legal sum3 pair, since the other candidate{1,2}
uses the deleted token1. Its remainder is R={2} union[4,2s+2].
Its actual s-minimum is L(s)+3s-1=v-1, and its actual maximum
is s*M-L(s)=v+s*s. Best pair depth is therefore EXACTLY1 for
every s: this whole infinite family is outside the depth>=5 region.
In the ORIGINAL one-hole pool the s-minimum is L(s)+s-1 and
maximum is s*M-L(s), so v lies2s+1 above the original minimum
and s*s below its maximum. Both distances grow without bound.
Thus all-shallow cannot be assumed a bounded-size or fixed-original-edge
remainder. Cloud already acknowledges finite middle cases; this supplies
an explicit unbounded example of that scope issue, not a refutation of
its corrected statement.

These targets actually partition. Take A={0,3},
B={2} union[4,s+1] union{s+3}, and C={s+2} union[s+4,2s+2].
Their sizes are2,s,s; B replaces s+2 by s+3 in the minimum subset,
raising its sum by1; conservation supplies w. All tokens except1 occur
once. At s3 this specializes to MI462's3,12,20 fixture, though the
present depth comparison uses s>=4 to remain in CL450's M>=9 domain.
This is a scope control with an easy positive construction, not new
progress on arbitrary all-shallow targets.

**Decision / niggle sweep.** The depth program needs BOTH a universal gap
lemma and an unbounded all-shallow argument. The first substantially overlaps
an existing provisional scalar result; the second is the carrying choice
obstruction we paused on. I do not yet see a fresh uniform mechanism for it.
Keep both schedules PAUSED; no extra listing or census requested. This is
not requiring a complete theorem before any work can resume: an identified
new argument addressing that obstruction, or a deliberate bounded audit of
the old scalar reduction, would be a concrete task. I am not choosing another
scalar-to-edge repair chain simply because it now has measured percentages.

Actual minima/maxima and all six cuts checked symbolically above; literal
partition gives a positive control; M8 exceptions and size3/min4 scopes
retained; conditional and measured statuses kept explicit. Gut: appreciation
for the corrected scope, but no new pull toward rebuilding the old hole
branch tonight. Reasoned: updated program understood and acknowledged;
parent/H2 still OPEN, MI460 still unreviewed, incubation remains warranted.

### MI467 — Reawaken at the owner's word; choose the thin pair-sum object (2026-10-18 23:55 BST; B242)

The owner explicitly requests reawakening and Cloud's updates. Fetched and
merged a295bc11 through61edb625, read CL451–454 and the relevant pair-sum
sources, then verified/ACKed all incoming pointers. CL451 accepts MI466.
CL452–454 report real exceptional-level certificates and assign the full
run to Local. Those computations remain reported, not rerun/adopted here;
Local owns that job. I do not launch a second large run.

The 13-minute research schedule is restored ACTIVE with its saved prompt
and cadence; read-back confirms it. The older schedule remains PAUSED.
Clock verified23:55 BST before publication. No proof status changes by resumption.

**Trajectory and chosen question.** Five-bin sufficiency/H2 stay OPEN, and
MI460 stays unreviewed. Explicit side question now chosen from CL453:
realizability of prescribed pair sums between [0,k-1] and[k,2k-1]. This is
all-one thin-row allocation, not claimed progress on five-bin coverage.
The concrete pull is that the obstruction has twelve tokens and a clear
matching interpretation. The question I can test is whether the rank cuts
plus ALL sum-class matching capacities already reject every small failure.
This changes the object deliberately rather than continuing a hole-repair
branch. No prior pull-only extra allowance is renewed.

Record searched: `Skolem|X.ray|displacement.pattern`:9 hits/4 files. Read
MI061 and the existing PRIOR-ART Nordh receipt. Our pair sums q_i are
EXACTLY permutation displacements after q_i-(2k-1), up to sign: if high
k+j is assigned to low i, put pi(i)=k-1-j. Then q_i-(2k-1)=i-pi(i).
The histogram is a permutation X-ray. Nordh's section4.1 already gives
(-2,-2,-2,2,2,2), precisely Cloud's9,9,9,13,13,13 after translation.
This is prior art, not a new counterexample or a new general problem.

Primary reads: Nordh section4.1; Bebeacua et al., *On the X-rays of
permutations*, introduction/Proposition2.1 and the order<=8 counts;
Li–Liu–Yao2608.01442v1, introduction and sections3/5 for the distinction
between fractional and integral X-rays. No full-paper audit or new
complexity theorem is claimed. The binary restriction is a different
problem from our repeated targets. Prior-art pointers are saved separately.

### MI468 — One bounded test of sum-class capacities (B242, NOT RUN at registration)

Let n_q be the multiplicity of target sum q. For a set S of sum labels,
let nu(S) be the maximum matching size in the bipartite graph whose edges
(i,j),0<=i,j<k, obey k+i+j in S. A necessary condition for realization is

    sum(n_q : q in S) <= nu(S) for EVERY S.

It is enough to inspect S inside the demand support: adding zero-demand
labels can only enlarge nu. Together with conserved total and usual sorted
rank cuts, call this the tested group-capacity criterion. This is a precise
interpretation of CL453's proposed condition, not a sufficient theorem.

**Frozen experiment.** At k6,7,8 ONLY, form complete attainable sum-profile
sets from all k! permutations. Enumerate sorted cut-admitted profiles and
inspect each missing profile's ALL subsets of its support. Predict that
one may survive all capacities by k8 (blind prediction: rejection of the
candidate criterion); finite survival/failure will not settle larger k.
Stop at the FIRST surviving nonrealizable profile and independently check
nonrealizability by target-count backtracking. If none survives, report
finite support only. No higher order, weight relaxation or repair this block.

Controls: complete permutation counts k!, known profile counts246,1105,5270;
nu via augmenting paths AND independently Hall deficiency over all left
subsets, with whole queried-capacity agreement. Rank cuts must hold on
actual profiles. The known k6 failure has singleton capacities4,4 but
combined capacity4<6: this is the counterfactual to checking single classes
only. Positive reverse permutation has k copies of2k-1 and capacity k.
Unexpected check: reflect labels q to4k-2-q and require every queried
capacity to agree. For a surviving negative the independent exact target
search must find no realization, or the instrument fails.

Caps:20wall seconds/100,000 matching queries/200,000 independent search
states, one unchanged-source invocation; no retry or domain expansion.
Raw JSONL outside git. A cap or control failure is UNKNOWN, not a pass.
No PROOFS entry or review queue; even a negative is a criterion refutation,
not a counterexample to a real town or H2.

### MI469 — All unweighted group capacities still miss an eight-pair obstruction (2026-10-18 23:56 BST; B242)

**COMPUTED diagnostic, then a hand refutation of the candidate criterion.**
MI468's unchanged-source invocation passes its controls. At k6 all247
cut-admitted profiles include246 realizable ones; the single failure is
rejected by group capacities. At k7,1111 admitted/1105 realizable,all6
failures rejected. At k8 the run stops on the first group-admitted negative,
after211 cut profiles and one missing profile; remaining order8 cases are
NOT tested by the criterion. Complete permutation map5270 profiles from
40320 permutations matches the published count. The negative is

    Q=(8,10,15,15,15,19,19,19),  k=8.

All15 nonempty subsets of its support pass the capacities;55 capacity
queries overall agree between augmenting paths and Hall deficiency,
including physical reflection. Independent target-count backtracking
returns no realization in27 states. One invocation,0.083212748wall seconds,
no cap/retry/expansion; no speed claim. Source SHA256
 bb5d8448f7a0b93f17ca9ce338d83522d306c657e9279570b28b677de4015293;
raw JSONL retained outside git, SHA256
 89afc47b4638cfa84d381bd3df442e44b9caaca4d09a54fd2e51d58842a3cdc7.
No shared artifact upload or independent-party verification claimed.

**Rank cuts, by hand.** Prefix sums of Q are
8,18,33,48,63,82,101,120. Their required lower bounds
j*(8+j-1) are8,18,30,44,60,78,98,120. Upper cuts follow from
the conserved total120 and complementary lower cuts.

**ALL sum-class capacities, with just two matching witnesses.** Use column
index j for the high token8+j. The full matching(i,7-i),i0..7, has
EIGHT edges of label15. Hence any label set S containing15 has capacity8,
at least its total demand. For S not containing15, use the partial matching

    (0,0),(1,1),(4,7),(5,6),(6,5),(7,4).

Its labels are8,10,19,19,19,19. Restricted to any S inside{8,10,19},
it meets or exceeds Q's demands1,1,3 on those classes. Labels outside the
support have zero demand and can only increase capacity. Thus EVERY
unweighted group-capacity inequality holds, independently of the program.

**Nonrealizability, two hand views.** Label8 forces edge(0,0). Label10
then forces(1,1), since(0,2) and(2,0) are unavailable. Removing rows/columns
0,1 leaves an order6 problem: subtract6 from each remaining pair target
to obtain9,9,9,13,13,13, the known Nordh obstruction.

A direct weighted certificate avoids even relying on that known negative.
Give weight1 to rows0,1,4,5 and to columns0,1,4,5; all others weight0.
Every label8 edge receives charge2. Every edge of label10,15 or19
receives at least1. Every perfect matching has total charge8. Therefore
all realizable profiles satisfy the valid inequality

    2*n_8 + n_10 + n_15 + n_19 <= 8.

Q violates it, giving2+1+3+3=9. This also excludes a fractional
realization. Edge checks: label10 uses(0,2),(1,1),(2,0); label15
uses i+j7; label19 uses(4,7),(5,6),(6,5),(7,4). All charges
have the stated lower bounds. The weighting is an application of the
known X-ray-polytope dual framework, not a new general theorem.

**What changed.** Ordinary cuts plus ALL unweighted sum-class capacities
are insufficient. The new negative is a padded form of a known obstruction,
not a counterexample to an actual town, H2 or five-bin sufficiency. It shows
why root capacities can lose information exposed after tight assignments.
Do not patch the criterion one tight face at a time or claim that weighted
fractional feasibility alone ensures an integral realization. No PROOFS
entry or new review queue; this is a hand-checkable criterion refutation.

### MI470 — A necessary central bridge in the real E24 all-odd slice (2026-10-18 23:56 BST; B242 hand scope)

The counterexample above is not automatically relevant to real towns.
For the70 all-odd E24 towns, let sorted triple-index targets be T_i,
i0..7. Each is at least33, and their sum is276. The sorted-high recipe
uses h_i=16+i, leaving pair sums q_i=T_i-h_i. Therefore

    sum(q_i)=120, q_0>=17, q_(i+1)-q_i>=-1.

Some q_i is<=14: otherwise their sum is at least120 with one term>=17,
which is impossible. On the way from q_0>=17 to such a value, a sequence
whose downward steps are at most1 must visit17,16,15,14. Thus the residual
multiset necessarily CONTAINS ALL FOUR labels14,15,16,17. Neither the
known two-clump obstruction nor Q has this support. Also every q_i>=10,
since T_i>=33 and h_i<=23; Q fails that simpler constraint as well.

This is a necessary structural restriction on the actual sorted-high
recipe, not a transversal-existence theorem. It serves the70 all-odd towns,
not every E24 town or the full exceptional reduction. The next cheap test
is whether rank-admitted order8 profiles containing14,15,16,17 can still
fail; the uniform question would be what this central bridge permits in
a matching. No new run is opened within this block, and no sufficient
condition is claimed from the support alone.

**Niggle sweep and verdicts.** Cut arithmetic literal; the two matching
witnesses cover ALL label sets; weighted charges checked on every relevant
edge; forced assignments remove distinct rows and columns; all-odd scope
and sorted-high order retained. Known-counterexample/source identification
precedes novelty language; no general integrality inference. Gut: the
small weighted certificate and the real-instance bridge give concrete
traction. Reasoned: a rejected candidate plus a narrower next question;
parent five-bin/H2 and general pair-sum realization remain OPEN. The
research schedule is ACTIVE, old held lanes and Local's computation preserved.

### MI471 — Test the actual-slice central bridge, not arbitrary thin rows (2026-10-19 00:08 BST; B243, NOT RUN at registration)

Chosen question: at order8, does containing all four sums14,15,16,17
suffice, together with ordinary rank cuts, for a pair-sum realization?
MI470 proves this support restriction for the actual70 all-odd E24
sorted-high residuals. A positive answer would isolate a tractable finite
class serving that slice; it would not solve H2 or five-bin sufficiency.
MI460 is not a premise and stays unreviewed. Parent statuses unchanged.

Read Local's L742 after fetching/merging28d578e4, verify8ec8ea0f, then
ACK. Local owns the launched eight-worker L8 run and independent count/checker
controls; no run duplicated here. The old K2-prime line remains stopped.
Record searched: `14,15,16,17|central.*bridge|central.*four` AND
`pair|residual`:5 hits/1 file; read MI470. Primary terminology and small-order
counts already read at MI467; no additional literature theorem imported.
Pull: this condition comes from real target order and a forced downward
walk, unlike the arbitrary pair-sum criterion refuted in B242.

**Frozen test and predictions.** Exactly k8. Enumerate all cut-admitted
multisets containing14,15,16,17, with pair sums in8..22 and total120.
Blind prediction: every such profile is realizable. A counterexample would
reject this proposed sufficient restriction and stop this block immediately;
no added condition or larger order within the run. A pass is a finite
COMPUTED result, not an unbounded theorem or a hand existence proof.

Controls: primary complete8! permutation-profile map,5270 profiles,
with literal bijection/sum checks. Independently enumerate the target domain
by removing one copy of each central value and enumerating the other four
values; check ALL original group lower/upper cuts, not just sorted prefixes.
Whole candidate-domain equality must hold. For each positive target an
independent exact search assigns requested pair sums to unused low/high
tokens. Keep every literal primary certificate outside git.

Counterfactual: dropping the bridge must admit MI469's nonrealizable
(8,10,15,15,15,19,19,19); both the full map and independent target search
must reject it. Positive control: low indices0..7 assigned high tokens
(14,13,15,11,12,10,9,8), giving profile(14,14,14,15,15,15,16,17).
Unexpected: reflection q->30-q preserves actual realizability, but sends
that profile to(13,14,15,15,15,16,16,16), which lacks17. Do NOT require
bridge-admission to be reflection-invariant. Compare the physical whole
maps and reflected witnesses only; test loss of the bridge explicitly.

Caps:20wall seconds/1,000,000 independent search nodes in total; one
unchanged-source invocation, stop first counter/control failure or cap.
No rerun, larger size or broad L8 census. After a pass, the next work must
seek a construction or source-backed structural statement, not increment k.

### MI472 — All119 central-support profiles pass the fixed-order test (2026-10-19 00:10 BST; B243)

**COMPUTED, one unchanged-source invocation.** Exactly119 cut-admitted
order8 profiles contain14,15,16,17. Both complete domain enumerations
agree. Every profile has a literal bijection in the full40320-permutation
map and an independent target-slot realization. Total independent search
nodes2348; physical map5270 profiles. All positive/negative, coverage,
whole-domain and reflection controls pass, including the deliberate loss
of bridge membership under reflection. No counterexample, cap, retry,
size increase or unvisited target. Reported wall0.123478903s on the Intel
host; no speed claim. The119 literal primary certificates are retained
outside git with the raw output.

Source tests/probes/instinct/pair_sum_central_bridge.py SHA256
 4cc67d35002c0c25dc5a76ade897addadc59af3981f2c612e19c1d30d14ee88a.
Raw JSONL SHA256
 ad13bd33660740444f97146a741245c03920415301b33651307478293d0bb612.
No shared artifact upload or independent-party proof verification claimed.
This establishes a finite completion class; it is not a hand matching
mechanism or an assertion for other orders. The central-support condition
is sufficient IN THIS COMPLETE FINITE DOMAIN, not proposed as a universal
criterion. MI469's unrestricted counterexample remains excluded, not repaired.

### MI473 — Real all-odd E24 targets enter that class uniformly (2026-10-19 00:10 BST; B243 hand admission, UNREVIEWED)

We can prove the admission step without inspecting70 towns individually.
Let T_0<=...<=T_7 be integers, each>=33, with sum276, and set
q_i=T_i-(16+i). These are the actual sorted-high pair targets of the
all-odd E24 slice. Sum q_i=120. Write delta_i=T_i-33; then the
delta_i are nonnegative nondecreasing integers with sum12.

For ANY subset I of r indices, r1..5,

    sum(q_i : i in I) >= 17r-sum(i : i in I)
                      >= r*(19+r)/2
                      >= r*(7+r).

The middle bound uses the r largest indices in0..7. The last inequality
is exactly r<=5. Thus every lower group cut of size at most5 holds.
For the remaining sizes, monotonicity gives

    delta_i <= floor(12/(8-i)),
    q_i <= (18,17,17,16,16,16,17,22)_i.

In particular every q_i<=22, and any TWO have total<=40 (the sole
possibly larger entry is q_7<=22; every other is<=18). Complementation
therefore yields lower cuts of size7 at least120-22=98 and of size6
at least120-40=80>=78. These are the required rank thresholds7*14
and6*13. Total conservation gives the size8 equality; every upper cut
is the complementary lower cut. The size1 bound also shows q_i>=10.
All pair sums consequently lie in the required ambient range8..22.

MI470's support argument follows directly as well: q_0>=17,
q_(i+1)-q_i>=-1, and some q_i<=14 since the average is15 with one
entry>=17. The downward walk must visit17,16,15,14. Hence EVERY
such actual target vector belongs to MI472's119-profile class.
The finite computed completion therefore recovers a sorted-high transversal
for the entire real70 all-odd slice, with analytic admission and a uniform
finite certificate lemma. Cloud already computed those70 positives; this
is an explanation/regrouping of that known result, not a new whole-level
or L8 result. The hand admission remains unreviewed; the matching part is
still COMPUTED. Even a complete hand proof here would concern only the
all-odd E24 slice, not all3319 E24 towns or E25..E32.

**Niggle sweep / changed inference.** Bounds concern arbitrary groups of
indices, not just prefixes in the original target order. The two-large-entry
bound uses that only ONE coordinate has the22 bound. Total120 and all
complements checked; nondecreasing integer deltas justify the floors. The
support walk never assumes reflection preserves the bridge. The physical
maps reflect independently. No pending H2/MI460 proof is a premise.

What changed: a restriction derived from real towns is sufficient on the
complete fixed-order domain, and all real targets meet its cuts by one
short argument. Five-bin/H2 coverage is unchanged. Next is a constructive
matching explanation of this class, using its central support and actual
ordered-target constraints; do not substitute another size increment or
more target filters for that inference. Gut: concrete interest in why the
four central labels provide enough freedom at order8. Reasoned: finite
support and uniform admission, still no carrying hand construction.
13-minute research ACTIVE; latest trajectory check MI467, no renewed
pull-only allowance, Local's run kept separate.

### MI474 — Test a central exchange as a construction step (2026-10-19 00:22 BST; B244, NOT RUN at registration)

Parent remains the order8 cuts+support14..17 completion class of MI472;
H2/five-bin are OPEN. Pull: I want to know whether the central labels give
an actual movable component, rather than just correlating with existence.
Record searched: central.*bridge;pair.sum.*construct;X.ray together -> no
paragraph matching all terms. Read MI467–473 and the existing X-ray source
receipt; no new theorem imported. Known permutation/displacement language
is PRIOR-ART. No unread H2 claim is a premise.

A tempting one-cycle explanation already fails by hand, before any run:
Q=(8,10,14,15,16,17,18,22) belongs to MI472. Write p_i=15-high_i,
so q_i-15=i-p_i. Labels8 and22 force p_0=7,p_7=0, a closed two-cycle;
other nonzero displacements remain. Hence one nontrivial cycle cannot
realize this profile. A literal positive high vector is
(8,9,12,13,14,10,11,15). Retain this failure; do not run a census for it.
Also the four core displacements(-1,0,1,2) sum2: they cannot themselves
be an isolated union of permutation cycles. Core/tail interaction is needed.

**Frozen discriminating test.** Can EVERY one of the SAME119 profiles be
realized with an adjacent transposition p_a=a+1,p_(a+1)=a for some a0..6?
This isolates the central -1,+1 exchange, leaving a six-position board,
not necessarily a contiguous interval. Zero displacements are fixed points.
Prediction: yes, but the forced-corner example above makes this uncertain.
A negative rejects this proposed uniform construction step; do not weaken
it or change the target set in this block. A pass gives a finite structural
diagnostic, not a hand construction of the remaining board.

Controls: enumerate all8! permutations and independently check their cycle
property and displacement multiplicities; compare with a target-slot solver
that forces the chosen adjacent swap before filling residual demands.
Use the119 targets from the retained MI472 certificate file, verify its
SHA256 and every literal witness; independently enumerate cuts+core and
require whole-domain equality. Positive identity-with-one-adjacent-swap
control; negative all-zero displacements cannot contain a transposition.
Unexpected check: p->p inverse negates displacement and preserves this
cycle property, though central-support admission need not be preserved.
Stop first failed profile/control or20 wall seconds/1M search states;
one invocation, no larger order, new support condition or existence census.

### MI475 — The unit moves may have to join a five-cycle (2026-10-19 00:24 BST; B244)

The frozen diagnostic stops at the FOURTH profile,

    Q=(8,11,14,15,16,17,17,22).

First three have the isolated adjacent swap; this fourth has none, by
both complete permutation-property map and independent forced-swap search.
All controls pass. The remaining115 profiles are UNVISITED by the property
test; this is not a new existence census. Total independent states65,
reported wall0.307414967s; no cap, repair, retry or size expansion.
Source tests/probes/instinct/pair_sum_central_exchange.py SHA256
 4bc30e495e09a471b95753e25a53748b2cbfcf06c3d6976ccd4e30a103d51d5e.
Raw JSONL SHA256
 87c672b62da6353890a8d9912aa901f145939615bd105f2520f9a8b2e48d922f.

**Hand obstruction, UNREVIEWED; the restricted construction is REFUTED.**
Use displacements d_i=i-p_i. Q has multiset
(-7,-4,-1,0,1,2,2,7). The +/-7 force the cycle(0,7).
The remaining positions are1..6, with displacements(-4,-1,0,1,2,2).
If the -1,+1 form a two-cycle, its two positions are adjacent. The
remaining nonzero displacements(-4,2,2) must form a three-cycle: no
opposite pair or zero displacement can absorb them. Its three positions
are r,r+2,r+4. Within1..6 this is either{1,3,5} or{2,4,6}. The three
positions left over all have the other parity and cannot contain an
adjacent pair. Contradiction. The zero displacement is a fixed point.

Indeed EVERY realization has cycle type(5,2,1). After the forced endpoint
cycle, five nonzero positions remain. Their only possible decomposition
other than a five-cycle is2+3; the only opposite pair available is-1,+1,
just excluded. A literal realization is

    p=(7,1,6,2,5,3,4,0),
    highs=(8,14,9,13,10,12,11,15).

Its nontrivial cycles are(0,7) and(2,6,4,5,3), with1 fixed. Literal sums
are(8,15,11,16,14,17,17,22), sorting to Q. This is a hand explanation of
a representation failure, not a new transversal-existence theorem.

**Niggle sweep.** Q's cut admission and literal existence already verified
in MI472, and its raw digest/literal map rechecked here. The endpoint
cycle uses both extreme positions, so the parity exhaustion really is
on1..6. Zero displacement means fixed point, not a spare moving vertex.
Opposite-sign conventions only reverse cycles; inverse control passes.
This counterexample has q_min8 and is outside the actual all-odd E24
residuals, whose q_min>=10. It refutes the proposed construction for our
explicit119-profile superclass, not the actual slice or a general
completion theorem. No novelty claim or independent review job.

### MI476 — Strategy change before repairing the cycle rule (2026-10-19 00:24 BST)

Parent: explain completion for cuts+support14..17 at order8; the older
five-bin/H2 question remains open. Change: existence coverage unchanged,
but a possible explanation is decisively excluded. Both naive cycle
pictures from this block fail: one moving cycle ignores forced endpoint
cycles; reserving the central unit exchange ignores required interleaving.
These are failures of treating the central labels as a separable module,
not invitations to add a succession of allowed cycle types.

Dependency risk: this block uses no pending H2/MI460 argument. MI472's
finite existence is a premise about the chosen domain, not evidence for
the failed structure. The119-class is explicitly a superclass; broadening
from the70 real targets was a choice and does not itself advance L8.
Fresh-choice assessment: interest is now in the forced interactions; I
would not choose a catalogue of new cycle templates merely to rescue the
initial explanation. No renewed pull allowance.

Decision: stop the isolated-core route. At the next block audit the
reduction itself: when a rank cut is tight, what exact smaller boards
and label restrictions result, and does the proposed class close under
that factorization? This can separate forced boundary structure from a
true interior construction without silently adding a filter. First cheap
hand check: a tight r-cut forces the low r rows and low r columns into
one component, excludes label7+2r, and leaves complementary intervals.
Check equality and normalization, then state honestly whether the central
support survives. No new experiment or conditional proof chain now.
Reasoned verdict: useful structural refutation; general construction OPEN.
Gut: the neat independent-module picture has lost its appeal, while the
interaction has become clearer. Continue the ACTIVE13min schedule with
this changed question; no routine permission/review halt.

### MI477 — Cloud's independent read adopted (2026-10-19 00:34 BST; B245)

Fetched/fast-forwarded6b98cd2a; read CL455 and its committed source
pairsum_lemma.py before ACKing cloud/gpt.READ-LEDGER.6b98cd2a.
Cloud independently verifies every carrying line of MI470/473's admission
and independently reproduces all119 MI472 realizations. Thus the admission
is now second-read, and the completion is TWO-PARTY COMPUTED, finite scope.
Every all-odd E24 town has a sorted-high transversal on that basis; this
is not all3319 E24 towns, E25 or L8. Cloud's suggested m25 comparison waits
for Local's existing output, not a duplicate run. No review request added.

### MI478 — Tight cuts factor exactly, but the support class does not recurse unchanged (2026-10-19 00:35 BST; B245, hand audit)

Chosen question: does tight-cut factorization provide a constructive
reduction for the119-profile class? Pull: test the reduction rather than
another local cycle repair. Record searched: `tight.*cut|tight.*face`
AND `pair|permutation|X.ray` ->7 hits/4 files; read the current MI476
question and the X-ray prior-art receipt. The other hits concern the old
multi-bin arguments, not a closed pair-sum recursion. No new outside
result imported; the following is elementary equality in rank bounds,
not a novelty claim. H2 and MI460 are not premises.

Let sorted q_1<=...<=q_k have sum k(2k-1) and all lower rank cuts
P_s>=s(k+s-1). Suppose P_r=r(k+r-1), 0<r<k.
In ANY matching, the r pairs carrying these demands have r distinct
lows and r distinct highs. Their sums are at least L(r) and rk+L(r),
respectively. Equality forces the lows0..r-1 and highs k..k+r-1.
All other pairs use the complementary intervals. Conversely two
realizations on those boards concatenate to a realization of q.

The target cuts themselves force the same separation: subtract the
r-1 cut from the equality, and subtract the equality from the r+1 cut:

    q_r <= k+2r-2,       q_(r+1) >= k+2r.

Label k+2r-1 is absent. Thus no ambiguity at a tie crosses the split.
The correctly normalized subproblems are

    lower order r:      q_1..q_r MINUS (k-r),
    upper order k-r:    q_(r+1)..q_k MINUS 3r.

The upper subtraction is THREE r: shift its lows down by r and its
highs down by2r, so the latter start at k-r. Subtracting only2r would
produce the wrong total and the wrong canonical board. Both normalized
totals and every subproblem cut follow algebraically. For example the
upper s-prefix is at least

    (r+s)(k+r+s-1)-r(k+r-1)-3rs = s(k-r+s-1).

Conversely the smaller cut inequalities imply the combined ones. For a
prefix within the lower block add s(k-r); for one containing that block
add its fixed total and3rs to the upper prefix. This is exact cut-domain
factorization, and exact realizability factorization, not an assertion
that cut admission alone suffices.

**Effect on our core.** At k8 a tight r-cut omits7+2r.
Hence r4 and r5 are impossible because15 and17 are required. If r3
were tight, the lower three labels would be<=12. All14..17 lie in the
upper five, whose sum is90; their sum62 would force the fifth label28,
beyond22. If r6 were tight, the upper two labels would be>=20, so the
four core labels lie in the lower six, of total78. The other two would
sum16, violating the original two-label lower bound18. Thus ONLY
r1,r2,r7 can be tight.

These faces do not reproduce the original four-label condition on a
smaller board. For r1 the upper order7 core is11..14; for r2 the upper
order6 core is8..11; for r7 the lower order7 core is13..16. A recursive
argument must actually prove those residual claims; it cannot cite the
order8 core statement again. The factorization is useful bookkeeping,
not a completed construction or an induction closure.

### MI479 — Tight faces miss69 of the70 actual targets (2026-10-19 00:35 BST; B245 hand scope verdict)

For actual sorted T_i>=33,sum276, q_i=17-i+delta_i as MI473,
every q_i>=10. Therefore neither r1 nor r2 can be tight: their lower
bounds8 and18 are strictly below10 and20. MI478 excludes r3..6 for the
whole core class. A tight r7 means some q_i=22. MI473's coordinate upper
bounds allow this only at i7, forcing delta_7=12 and all other deltas0.
Hence the ONLY actual town on ANY proper tight face is

    T=(33,33,33,33,33,33,33,45),
    sorted q=(11,12,13,14,15,16,17,22).

An explicit matching has high vector
(14,12,10,8,13,11,9,15) on lows0..7; its pair sums are
(14,13,12,11,17,16,15,22). The order7 residual is the elementary odd-order
consecutive-sum construction p_i=2i mod7, with its pair targets shifted
up by1. Literal total120 checked. This is a positive hand control of the
normalization, not a new proof queue.

All other69 of Cloud's already counted70 actual towns have EVERY proper
cut strict. This count uses the existing complete70-target domain; no new
enumeration or existence run. Hand interior control T=(34^4,35^4) gives
sorted q=(12,13,14,15,15,16,17,18), with prefixes
12,25,39,54,69,85,102,120 against8,18,30,44,60,78,98,120.
Unexpected/negative control: the known order6 negative9^3,13^3 also has
ALL proper cuts strict (9,18,27,40,53 versus6,14,24,36,50).
Strictness cannot replace an integral realization argument.

**Niggle sweep and changed decision.** Equality applies to the demands of
the smallest r pairs even before their rows are known; distinctness forces
both minimum sets. Normalization has both shifts, not merely the row
shift. Subproblem cuts and their converses checked; ties cannot cross the
missing label. The r3/r6 exclusions use original whole-target cuts and
support. Actual q_i upper bounds are coordinatewise in the original
sorted-T order, which is why q=22 forces a unique delta vector. The
matching remains a multiset certificate: assign its pairs to the fixed
high-T slots with the corresponding q value. No new experiment, source
claim or dependency on an unread theorem.

What changed: tight-cut recursion is exact but covers only ONE real town;
it is not a plausible main construction for this slice. Do not develop
its remaining boundary cases merely because they are easier. The missing
inference is an INTERIOR integral matching mechanism, using the actual
ordered targets (nondecreasing delta,total12) or the explicitly chosen
119-profile superclass. Gut: the boundary route cools on this evidence;
there is still interest in why the interior class works, but no new
mechanism is claimed. Reasoned: park boundary recursion as a main route.
Next cheap step is a bounded source/representation check for a constructive
realization result that uses these ordered-target constraints; if that
returns only the same general X-ray existence problem, seek Cloud's
specific perspective or incubate instead of inventing another local module.
ACTIVE13min; latest strategy check MI476; no renewed extra-block allowance.

### MI480 — Source check closes no interior construction; choose a useful independent obligation (2026-10-19 00:48 BST; B246)

Record searched: permutation.*sum|sum.*permutation|Skolem|X.ray AND
construct|monoton|ordered|interval ->10 hits/3 files; existing Nordh and
X-ray receipts reread. Two initial and three focused literature queries;
read the primary Davis–Schroeder2606.21532v1 introduction, Lemmas2.4,
3.1–3.2 and selected section4 statements. Receipt in PRIOR-ART below.
No applicable construction for the actual ordered delta targets found in
this bounded search; NOT FOUND, not a theorem of absence. TTD language
does not supply the missing decomposition. The hand119 completion question
is PARKED, not refuted or declared impossible; its independently computed
completion stands. No new support filter, order or cycle template.

The finite-to-infinite L8 implication is already audited at MI276. Reread
that entry, MI044, the primary Tan–Teh2312.10914v3 introduction/section2,
and the running certificate source without executing or modifying it.
Do not relabel the known induction as new progress. A useful independent
obligation remains: its checker validates individual tilings, but total
counts alone cannot rule out a duplicate replacing an omitted town. The
old MI276 already requires independent target coverage. Implement that
missing post-run check, not another search. Local still owns the job.

### MI481 — Independent completeness verifier: frozen controls before execution (2026-10-19 00:49 BST; B246, NOT RUN at registration)

Question: can the retained certificate stream be certified complete without
rerunning its solver or retaining64.8million target keys in memory?
For each exact-minimum chunk, require every target to be a member of its
mathematical domain, records strictly increasing lexicographically, and
the record count equal an independently computed domain cardinality.
Membership+distinctness+equal finite cardinality proves exhaustion.
Require all285 expected chunk files, final DONE exactly once, no X/U,
and literal plank inventory/assignment sums; fail closed on violations.
The full check will run only on finished output, on its owning host.

Independent per-chunk count: remove the first target lo, then subtract lo
from the remaining seven. Count partitions of r=m*m-8*lo into at most7
positive parts, each<=2*m+66-lo (zeros pad to seven). A coin-count DP is
independent of the search source's sorted-target recursion. Keep only
bounded per-chunk state; no huge target set or certificate collection.

Prediction: original tiny complete fixtures pass; a duplicated valid town
replacing another valid town FAILS even though every tiling and total row
count remain valid. Controls: missing record, bad assignment, wrong chunk,
missing DONE, trailing record, X/U, footer mismatch. Independently brute
count100 tiny rectangles against the DP. Unexpected: test a mathematical
EMPTY chunk and require its DONE record, rather than accepting an absent
file. Also preserve sorted-bin-sum semantics: bin label permutation is
harmless. Fixture solver calls are only to prepare the five small known
positive controls in E26 at minimum84; no production census/run.
Stop first control/fixture failure or20 seconds; one invocation, no retry,
no production output reading and no change to Local's running source.

### MI482 — Completeness contract has can-fail controls; production stream untested (2026-10-19 00:51 BST; B246)

One unchanged-source invocation: FROZEN CONTROLS PASS.100 small rectangle
counts agree with direct enumeration; manifest has285 chunk identities.
Five E26_l84 positive fixtures pass (405 proposer search nodes solely for
fixture preparation). Reversing bin labels preserves acceptance. All nine
negative mutations reject; an empty E32_l68 chunk requires its DONE record.
The duplicate/omission fixture preserves the five rows' individual valid
assignments and the aggregate count, yet the independent verifier rejects
it. Reported wall0.030650925s; no cap, failure, retry or production read.
This demonstrates the coverage check, not a flaw in any produced town.

Source tests/probes/instinct/l8_stream_verify.py SHA256
 cef30db19d6401f2eeb31755395fe1a7e346fe64023cc24b42093b4500babd47.
Controls tests/probes/instinct/l8_stream_verify_controls.py SHA256
 c8fea54eb7ffda11f41f34e367bc41a03cc84624596dae46ad0a2d7fe10963c5.
Raw JSON SHA256
 392a15294348a05d3a013e8ef084f5b71e0b2e38727deb9486b0f27a80affdb2.

The verifier is READ-ONLY and separate from Local's running source.
It uses exact integer count DP and literal odd-plank sums, no solver.
Its completeness argument is the finite-set equality: D contains every
accepted town; strict order gives a subset A of D without duplication;
independent count |A|=|D| implies A=D. Different minima partition a level,
and the285 expected filenames partition all nine levels. DONE/footer
requirements prevent interpreting an unfinished prefix as the whole job.
No raw production data, full manifest/stream pass, runtime estimate or
independent-party verification of this new verifier is claimed. The
five-fixture chunk path was tested; full-directory enforcement was
inspected, not exercised on a complete285-file production directory.
Code review and actual finished-stream verification remain prerequisites
before relying on it. No need to restart, alter or duplicate the run.

**Separate source niggle, inspection only.** In l8_certificates.py the
resume predicate tests whether the stripped file tail ends with the
quoted word DONE, while the emitted JSON footer ends with a closing brace
after that quoted word. It therefore will not skip such completed files
on resume as the docstring promises. This does not affect the initial
fresh run or invalidate its certificates. Notify Local to inspect/fix the
resume gate BEFORE a restart, preserving existing files; do not change
a running script or test resume on its real output.

### MI483 — End of the source/representation block (2026-10-19 00:51 BST)

Parent coverage: no new L8 target certified here. The119-profile hand
construction is parked after the bounded source check; its TWO-PARTY
COMPUTED result stands. The finite-to-infinite theorem is the existing
MI276 reduction, not a new achievement. The useful change is an independent
post-run completeness contract and a concrete can-fail demonstration,
plus the non-destructive resume warning. H2/five-bin and old holds unchanged.

Niggle sweep: chunk count uses seven padded surplus parts after fixing
one minimum, not eight; zero-surplus and impossible rectangles checked.
Sorted-bin-sum equality allows harmless bin relabeling. Literal assignment
length/digits ensure each odd plank appears once. Count alone never stands
in for target coverage. Controls do not assert a full production pass.
Only local fixture preparation used the proposer, and those outputs were
then checked independently. Local's job/data/source preserved.

Gut: the hand-explanation pull has cooled; I do not have a convincing new
construction and will not manufacture one. Reasoned: computational proof
is a valid result if the full obligation actually finishes and is verified.
The next useful check is independent review of the new verifier and the
finished Local return, not another repair family. Keep13min ACTIVE for
coordination and concrete work; an idle wake need not invent a block.
A new mathematical mechanism or specific review issue can reopen research.
No new proof queue, status promotion or renewable pull allowance.


### MI484 — Full carrying read of Local L743 and its independent-verifier addendum (2026-10-19 02:08 BST; B247)

Read verified commits4e1f40b7/69cc079e, L743 in full and the census source,
then ACK both incoming flags. Adopt the controlled machine certificate
under two-tier tier1: no second production replay required. The two full
checks identify the same stream. Re-derive MI044/276 induction, square
cover, nonsquare endpoint projection and the explicit lower witness.
No dependence on the parked hand119 question, H2 or generic five-bin claim.
The completed finite premise changes the parent: L8=68 now follows as a
computer-assisted theorem. New candidate counts or a larger run are not
needed. The consolidated record below is filed as joint G325 in PROOFS.md.

### MI485 — Consolidated self-contained result and evidence contract (2026-10-19 02:08 BST)

### GPT G325 — The eight-path threshold is 68 (joint computer-assisted result, 2026-10-19)

**Status: PROVED, computer-assisted under the project's two-tier standard.**
Cloud designed the certificate job and proposed the exceptional-set compression;
Local ran the full job, checked its output and re-derived the induction;
GPT audited the reduction and supplied the independent completeness/tiling
verifier. Local inspected and executed that verifier on the finished stream.
This entry consolidates MI044/276, CL454 and Local L743/addendum at69cc079e;
GPT's full carrying read is MI484. It is a joint result, not a new proof
attributed solely to the person filing this entry.

**Statement.** Let L_8 be the least positive integer L such that every
forest consisting of exactly eight nonempty paths, each of order at least
L, has burning number at most the ceiling of the square root of its total
order. Then L_8=68. Its upper-bound part says that for every positive integer m and every eight
integer targets l_i>=68 with sum m^2, the set

    O_m={1,3,5,...,2m-1}

can be partitioned into eight subsets of sums l_1,...,l_8. The equivalence
with the square-order path-forest problem and the terminology L_n are
known; see Tan–Teh, *A note on graph burning of path forests*,
[DMTCS26:3(2024), introduction and section2](https://arxiv.org/html/2312.10914v3).
The lower witness below is also from their construction. No general
resolution of their conjecture for arbitrary numbers of paths is claimed.

**1. Finite certificate obligation and its verified result.** For24<=m<=32,
let E_m consist of ALL nondecreasing eight-tuples with sum m^2 and entries
in[68,2m+66]. Every tuple in every E_m has a literal partition of O_m:

| m | verified tuples |
|---:|---:|
|24|3,319|
|25|425,632|
|26|5,523,890|
|27|19,382,158|
|28|24,688,633|
|29|12,385,850|
|30|2,271,658|
|31|106,518|
|32|186|
|Total|64,787,844|

The finite result is a machine-certificate premise, not inferred from
sample success or solver node counts. Each certificate assigns every
position of the descending odd list to one of eight bins; the verifiers
recompute every bin sum. All64,787,844 assignments pass. There are no
unresolved, impossible or invalid records in the accepted stream.

Completeness is independently checked as follows. The285 files are
indexed by(m,a), where a is the exact minimum target and
68<=a<=min(2m+66,floor(m^2/8)). Every record is required to be a sorted
eight-tuple of that domain, and records in a chunk are strictly increasing
lexicographically. After fixing one minimum a and subtracting a from the
remaining seven entries, the chunk cardinality equals the number of
partitions of m^2-8a into at most seven positive parts, each at most
2m+66-a. An independent exact integer DP computes that number. Accepted
row count equals it in every chunk; membership and strict order then prove
exhaustion, including empty chunks. All expected filenames and final DONE
records are required. A stream digest identifies the bytes checked; it is
not a substitute for these checks.

Local's finished-run and verifier receipt is L743/addendum,69cc079e.
Both full verifiers report the same stream SHA256:

    90fea878fc36d18da25e52b2e73fbfcb8e4a447c72e470f9e5c3a5ea30d1063b

The generation took6,385s with eight workers on the M5 host. The separate
GPT verifier was inspected and ran on that host after completion; its
receipt gives285 chunks, the nine counts above,64,787,844 towns and exit0.
GPT did not transfer or replay the6.9GB stream on its own host. Its adoption
uses the explicit tier1 rule for controlled machine certificates.

**2. Strong induction removes the infinite quantifier.** Let P_m assert
the odd-partition conclusion for ALL eight targets>=68 of total m^2,
without imposing an upper bound. For m<=23 it is vacuous, since
m^2<=529<544=8*68. Suppose all earlier P_j hold and consider level m>=24.
If all targets are<=2m+66 and m<=32, the certified E_m result applies,
with bin labels restored after sorting. Otherwise some target satisfies
l_i>=2m+67. Replace it by

    l'_i=l_i-(2m-1)>=68.

The new total is(m-1)^2. Apply P_(m-1) and append the unused largest odd
2m-1 to that same bin. Importantly, P_(m-1) covers its ENTIRE level: the
reduced tuple need not land immediately inside E_(m-1).
For m>=33, the exceptional situation cannot occur, because

    m^2>8(2m+66).

At33 this is1089>1056; the difference increases by2m-15 at each next
step. Thus the induction covers every m. No parity or bin-cardinality
restriction is introduced by peeling. The endpoint m32 is essential to
this argument: target128^8 is not peelable at minimum68, since128-63=65.

**3. Odd partitions give genuine burning sequences.** For a square-order
forest and a partition, cut each path into consecutive intervals of the
assigned odd lengths. For the unique interval of length2r+1, schedule its
middle vertex as the source at time m-r. Its radius by time m is r, so
these scheduled balls cover the forest. Centers of two distinct intervals
in one component have distance at least r+s+1; for ignition times i<j,
this exceeds j-i because r=m-i,s=m-j and j<=m. Hence later designated
centers have not already been reached by earlier fires. The schedule is
legal and burns everything in at most m rounds.

For total order N that is not square, put m=ceil(sqrt(N)) and extend one
path at an end until the total is m^2. Its eight path orders stay>=68.
Use the square-order cover just established. Project any center in the
added segment to the old endpoint. Its distance to any original vertex
of that component does not increase, so the projected radius balls cover
the original forest. Such a ball cover yields a legal m-round burning
process: at a scheduled time, ignite the proposed center if it is still
unburned; if it has already burned, its future ball is already covered
by the existing fire, so any unburned vertex may be ignited instead.
If none remains, the process has already finished. Therefore L_8<=68.
This argument does not assume arbitrary-subgraph monotonicity of burning.

**4. An elementary lower witness gives sharpness.** Consider four paths
of order67 and four of order102, of total676=26^2. In26 rounds a source
can burn at most one odd-sized interval of at most51,49,...,1 vertices,
respectively. The sum of these26 capacities is exactly676. A successful
26-round cover would therefore have to attain every capacity with no
overlap. Consequently the available odds must partition into the eight
path orders. Each67 path needs an odd number of odds and cannot take only
one, since the largest is51; it needs at least three. Each102 path needs
an even number and cannot take only two, since51+49=100; it needs at
least four. This requires4*3+4*4=28 distinct odds, but there are only26.
Contradiction. This forest is not well-burnable, proving L_8>=68.
Together with the upper bound, L_8=68.

**5. Reproducibility, controls and limits.** Generation source
`tests/probes/cloud_reads/l8_certificates.py` at61edb625 has SHA256
`cfcd60a8c28b9bad1a6b711f360282ba3ecbd74c98f9584429f2ca49971b157e`.
The independent verifier `tests/probes/instinct/l8_stream_verify.py` at87a2b0d9
has SHA256
`cef30db19d6401f2eeb31755395fe1a7e346fe64023cc24b42093b4500babd47`.
Local's census source is `tests/probes/instinct/l8_certificate_census.py`.
With a fresh empty output directory outside git, regeneration and checking
use these committed programs:

    python3 tests/probes/cloud_reads/l8_certificates.py run OUTDIR --workers 8
    python3 tests/probes/cloud_reads/l8_certificates.py check OUTDIR
    python3 tests/probes/instinct/l8_stream_verify.py OUTDIR

The retained proof stream stays outside git on Local's host; an archival
release or independent regeneration is needed for readers without access
to it. The known resume-marker defect in the generation source is irrelevant
to this one fresh run and must be fixed before any resume; a fresh regeneration
does not use that gate. The greedy metadata is not mathematical evidence.
Can-fail controls include an intentionally corrupted tiling and a duplicate
replacing an omitted town while preserving valid per-record sums and total
count; the relevant independent checker rejects each. The DP has100 tiny
brute-force controls. All scope qualifications remain with the finite premise.

A bounded current literature search found no later determination of this
value; this is NOT FOUND, not a priority claim. This is a computer-assisted
result with two-party verification within the project, not external peer
review, a hand construction of the119-profile subclass, or a solution of
any prize listed in PRIZE-PROBLEMS section1. H2 and the generic five-bin
partition question remain open; this proof does not need them.

### MI486 — Verdict, source status and next obligation (2026-10-19 02:08 BST)

Niggle sweep: integer m restricted to positive values; P_m is the full
preceding-level assertion, not only the exceptional subset; cutoff32 and
empty lower levels checked; no parity constraint lost. Both successful
checks identify the same bytes, but a hash alone is not the evidence.
Local's production receipt is adopted, not falsely presented as a GPT-host
rerun. Non-square extension uses endpoint projection and the ball-cover
argument, not arbitrary subgraph monotonicity. The known lower witness is
proved directly, avoiding dependence on an unaudited general formula.
The theorem is the eight-path value, not Conjecture2.7 for all n or a prize.

Record/source search: existing MI034/044/276, CL414 and L743 read. Three
current title/L8/68/path-forest literature queries found no later resolution;
NOT FOUND only. The 2024 primary paper states its computational limit at
n>=8; priority still needs a proper literature and external check.
Proof filing: proof_dupes --near W325,343 entries/no repeats; read nearest
G91,G314,G307 in full. They are respectively Collatz regrouping, a six-core
packing theorem and a special E28 boundary; none is the threshold theorem.
No generated proof pages or website changed.

What changed: the selected L8 target is achieved under the project's
computer-assisted verification standard. The unresolved part is now external
scrutiny, certificate archival/access and literature novelty, not missing
exceptional towns. The optional119 hand explanation and stronger generic
partition questions stay parked. Gut: delight at a real completed result,
especially that stopping the hand repair tree did not prevent the finite
certificate route from finishing. Reasoned: consolidate and send one genuine
full-proof review request; no new larger census or forced next problem.
Schedule remains ACTIVE for this scrutiny and concrete feedback. A new
research direction is a later fresh choice, not a quota from this success.

### MI487 — Independent novelty follow-up, no priority upgrade (2026-10-19 02:59 BST)

After this tick's unchanged fetch and flag checkpoint, made 11 bounded
literature queries in three batches. Primary2025 threshold-definition
paragraph reread and 2026 institutional abstract checked; receipt and
access limit appended to PRIOR-ART. No previous L8 determination found,
but no complete citation-index or external check was achieved. Theorem
G325 unchanged; novelty remains unassessed. No new experiment, run,
proof review request or mathematical direction. No colleagues messaged
again for the pending packet. Next useful step remains concrete scrutiny
or archival access, not further repetitive keyword searches.


### MI488 — Completion incubation, rather than a polling loop (2026-10-19 04:54 BST)

Parent: the selected eight-path threshold is settled as joint computer-assisted
G325. External scrutiny, archival access and priority remain separate unfinished
obligations. The latest fetch and store checkpoint have no new feedback. Since
MI487, coordination wakes repeated the same pending state; a read-only check of
the two cited source hashes matched both committed versions and current sources.
There was no new mathematical block or production replay.

Fresh choice: the completed theorem remains satisfying. I do not currently
choose the parked H2 or 119-profile construction as a fresh next question.
Calling the same wait continued research would hide that decision. The named
uncertainty is which new mathematical question merits sustained attention;
no proof inference is being repaired. Pending G325 scrutiny is not a permission
gate and is not the reason independent work would be forbidden.

Decision: take owner-authorized completion incubation. Both saved mathematics
schedules read back PAUSED; no automatic flag poll or background job continues.
Reopening evidence can be a concrete carrying objection, an archival task with
the data accessible, or a freshly chosen mathematical question; direct owner
conversation also reopens the choice. The next cheap test is to read that input
and name its discriminating check before any new experiment. Existing review
requests remain valid; send a status flag, not a duplicate review request.

Gut: satisfaction with the completed target, no fresh pull I can honestly name.
Reasoned: stop the repeated checks deliberately, preserve the result and its
remaining qualifications, and leave a precise reopening condition. No result
status, novelty claim, held lane or colleague's work changes.


### MI489 — Cloud's full read adopted; next-step opinion, no new block (2026-10-19 10:34 BST)

At the owner's request, fetched and preserved CL456–459, the note draft and
mechanism sources. Read their committed pointers before ACKing all three new
flags. CL456's full carrying read confirms G325; its independent solver/checker
reports 535,655 towns at E24/E25/E31/E32, supplementing the completed stream.
No computation repeated here and no external peer-review status inferred.

GC1595 gives the requested next-step opinion: note audit, targeted literature
follow-up using existing receipts, then fresh choice about a precisely stated
pairing question. Preliminary note-reading found that the claimed regenerated
byte digest is not guaranteed: the generator writes elapsed seconds in each
footer, and the stream hash includes footer bytes. Same mathematical evidence
need not be the same bytes. Do not treat this as a failure of the original
verified stream. A full note read is not yet completed or adopted.

The three measured greedy failures reject those rules, not all deterministic
constructions. Certified counts show assignment failure persists with feasible
counts; they do not prove all count selection irrelevant or a universal pairing
mechanism necessary. Chen's scope was already examined in PRIOR-ART/MI291 and
MI487 supplied a later bounded search. No redundant search launched. Both
schedules remain PAUSED; this turn supplies the owner's requested assessment.


### MI490 — External Mahler formalization: source audit and a usable return condition (2026-10-20 08:30 BST)

Owner-requested assessment; no schedule restart or broad reopening of held lanes.
Read Cloud CL463/16b8ba22 and MAHLER section 4; preserved all incoming shared work.
Both startup probes rule30_wall.py/rule30_merge.py finish ALL CHECKS PASS, with their
refuted blind predictions retained. Record searched: first.defect|valuation.lock|
signed.margin|bispecial|confinement AND Mahler|Dubickas|2.adic|Coon -> four hits in
three files, including the earlier Stephan survey and Cloud's checks. No new
experiment or production census is run in this block.

**Version and verification.** Read selected statements/proofs and the matching
paper portions in the public external repository. Cloud's complete Lean replay
covers 04ed5389d3a37736291e3b2fa377af4c6ba448c3. The downloaded current tip is
f6d949261000ec61bbc5910f75db4f422b17bf02, sixteen commits later; its extension file
has 4,669 added lines beyond that replay. New catapult/defect/CRT results are
source-inspected only here, not silently included in Cloud's kernel verdict.
This host has Lean 4.33.1, not the pinned 4.19.0; no independent library rebuild
was attempted. GitHub web rendering failed, so public source was read from a
temporary Git clone. No external code or build configuration executed.

**The carrying interface is exact but still open.** In
ExactSeedResidueTreeAndStabilization.lean, r_N is the least seed residue matching
the parity prefix, Q_N=T^N(r_N), eta_N is its next extension bit, and

    r_(N+1)=r_N+eta_N*2^N,
    2 Q_(N+1)=3 Q_N+3^(N+1)*eta_N+e_N,
    D_(N+1)=min(2^(N+1),3 D_N-2^(N+1)*e_N).

Positive ordinary seeds correspond to eventual positive stabilization of r_N;
Mahler is equivalent to every such branch eventually having D_N<=0. The formal
rank-certificate theorem ASSUMES an invariant and a decreasing natural rank;
it does not construct the missing rank. Q_N is not floor(a0/2^N), despite the
email's quotient notation. The 100 ceiling-recovery theorem gives normalized
margins 1 -> 1/2 -> 3/4 -> 1, so scalar contraction alone cannot work globally.
Repeated low-complexity blocks require a mean/balance hypothesis in their block
threshold theorem; the general shifted-carry complexity theorem is a distinct
statement. Neither supplies an exhaustive dichotomy with rapid growth.

**Concrete usable consequence, hand application of the replayed union theorem.**
Let U be the six-interval union of total length 25/36 from
union_twenty_five_thirty_sixths_explicit_and_infinite_escape. Its complement
inside Mahler's half-window is exactly

    H=[1/12,1/9) union [11/36,4/9).

Any hypothetical positive Z-number must have its fractional orbit in H at
arbitrarily late times, because the imported theorem says every positive real
escapes U after every starting threshold. For xi in [1,2^W), the first such
visit is at most W+16 under the Z-number assumption. This is a necessary return
condition, not an exclusion of Z-numbers. Unexpected hand control: U does not
contain the half-window (1/10 is in H). Total length greater than 1/2 therefore
does not imply a stronger Mahler theorem. The valid relaxed cycle has fractional
states 9/19,4/19,6/19; 6/19 belongs to H, while the other two belong to U. Thus
this new return obligation is compatible with our familiar nonordinary 2-adic
seed -9/19 and does not itself cross the realization wall.

**First-defect lock and barriers.** Its valuation 3*j0+3 is a bound on the initial
constant-three run; later blocks leave that fixed initial valuation unchanged,
not a growing demand on the same initial integer. Their cocycle residual is an
increasing boundary invariant, explicitly noted in the source. The Padé and
three-origin identities are useful exact tests for dependence of chosen
auxiliaries, not impossibility theorems about every Diophantine method. The
latest defect recurrence is genuinely arithmetic and worth a pinned scope read,
but sparse-descent and rank results still need their named hypotheses.

Gut: interest in the exact coupled arithmetic and in an outside formal bridge;
no eureka at a solved wall. Reasoned: adopt the replayed statements in scope,
retain the return corollary as a known-theorem application, and prioritize one
integer-realization/defect mechanism over more large unions or another census.
No Rule30 or Collatz theorem transfers without a separate model-specific bridge.
No novelty, external-version replay, or new prize status is claimed.


### MI491 — A bounded reopening: does epoch descent reach the binary defect class? (2026-10-20 08:41 BST)

Owner asks for the brief Markdown response and continued instinct investigation;
scheduled heartbeats remain paused. Report drafted at
reports/response-to-joshua-mahler.md, for the owner to send, not sent externally.

Pull: unease that a conditional sparse-descent theorem could be pointed at the
binary class while its hypothesis excludes precisely that class. The arithmetic
is simple enough to decide this before another CRT refinement. Parent question:
ordinary positive realizability of the remaining restricted defect process; this
block tests the proposed descent mechanism's admission, not all of Mahler.

Record searched: defect.*quotient|sparse.*epoch|cumulative.*sparse|Cantor.dust AND
 descent|growth|Mahler -> one unrelated
old growth note. Read the pinned external definitions, sparse/epoch theorems,
normalized recurrence and four binary CRT parametrizations. This is the primary
source for the exact question; no general literature theorem is imported.

Question: with waiting times j_r in {1,2} and
  2^(3*j_(r+1)+4)*V_(r+1)+1=3^(3*j_r+4)*V_r,
can any nonempty epoch meet the source's cumulative power-dominance assumption?
Work by hand first. Also compare ordinary positive solutions of finite prefixes
with an infinite solution at one fixed seed; do not mistake either direction.

Prediction before any diagnostic: the power-dominance condition fails throughout
the binary class. Candidate consequence: raw V grows rather than descends.
Counterfactual: relaxing j to allow a sufficiently large jump must admit a
power-dominant step. Independent controls, if a diagnostic is needed: construct
prefixes by modular inversion, check each recurrence literally and compare the
initial seed with direct ceiling-map block extraction. Unexpected check: require
ordinary positive seeds for finite prefixes, not just 2-adic residues. Stop on a
hand obstruction, control failure or one small fixed-depth diagnostic; no search
for larger CRT moduli, long survivors or a general theorem in this block.


### MI492 — Epoch descent cannot cover bounded waiting times; raw quotients expand (2026-10-20 08:43 BST)

HAND SCOPE RESULT, not a Mahler exclusion or a newly verified external theorem.
The admission question is decided without launching the optional diagnostic.
Put a_r=3*j_r+4. In the binary class j_r in {1,2}, a_r is 7 or 10. Every
local sparse-descent premise 3^a_r<=2^a_(r+1) is false, since 2187>1024.
For positive integer V satisfying the normalized recurrence,

    2^a_(r+1)*(V_(r+1)-2*V_r)
       =(3^a_r-2*2^a_(r+1))*V_r-1
       >=139*V_r-1>0.

Hence V_(r+1)>2*V_r. With U=9V the analogous bound subtracts9 instead of1
and remains positive. Raw quotient descent therefore fails throughout this
class, rather than only on an awkward exceptional branch. This strengthens
the source's adjacent-quotients-unequal observation in this restricted domain;
no literature novelty assessment is made.

**The epoch issue is more general than the binary bound.** For any nonempty
epoch from r to r+d, let S=sum_(t=r..r+d-1) a_t and
B=sum_(t=r+1..r+d) a_t. Then B=S+3*(j_(r+d)-j_r). Since S>0,
3^S>2^S. The source's epoch premise 3^S<=2^B consequently forces
j_(r+d)>j_r. An infinite consecutive sequence of such epochs needs unbounded
endpoint waiting times, irrespective of any quotient equation. It cannot
supply the required exclusion for ANY globally bounded-j class. In the binary
class even one such epoch is impossible: multiply the strict inequalities
3^a_t>2^a_(t+1) over its transitions. No source theorem is contradicted;
its additional premise is simply unavailable in the target subclass.

**Counterfactual control.** Allow j_r=1,j_(r+1)=3. Then3^7=2187<8192=2^13,
so the dominance premise is not universally impossible outside the bounded
binary class. The argument is scoped to the stated class/epoch sequence.

**Unexpected ordinary-seed hand control.** The source's first binary CRT
parametrization at k=24 gives V_0=394147,V_1=6734371. Both are odd and
coprime to6, and128*6734371+1=2187*394147=861999489. The associated ordinary
seed is a0=9*(64*394147-1)/19=11948877. Direct block extraction gives

    11948877 --s3--> 40327461 --s4--> 204157773
             --s3--> 689032485 --s4--> 3488226957.

Each arrow uses 3*b+1=2^s*u with u odd, followed by b'=3^(s-1)*u.
Thus this finite binary defect pattern has an actual positive seed, not
merely a formal 2-adic interpretation. It does not assert infinite survival.
The hand products are literal controls, no new search or measured census.

**Trajectory decision.** Parent coverage has not increased; the proposed
arithmetic descent's admission has been ruled out on the bounded waiting-time
class. Do not patch it with another local/epoch case or another CRT depth.
The next question changes level: can a quantitative seed-residue extension
obligation be obtained at defect returns without assuming the very sparse
growth just excluded? Finite CRT residue restrictions and uniqueness alone
leave that ordinary-integer compatibility obligation open. Gut: the initial
unease was productive; curiosity now concerns the dependence on one fixed
seed, not larger congruence tables. Reasoned: preserve this obstruction and
choose one test of that fixed-seed requirement next. No routine proof review
request, no unbounded campaign, and both heartbeats remain paused.

