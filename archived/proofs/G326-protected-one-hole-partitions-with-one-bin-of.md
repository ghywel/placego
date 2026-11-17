# Protected one-hole partitions with one bin of size two

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT326. Protected one-hole partitions
with one bin of size two (H2; second-read by Cloud, 2026-10-20)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Remove one middle number from 0, 1, 2, ... and the rest can be dealt into a pair and two bigger groups with any
agreed totals, if no group, or two groups together, asks for too little.

**What it says.** Take the whole numbers from 0 to some largest number M, and remove one number that is neither 0
nor M (the "hole"). Split all the rest into three bins: one holds exactly two numbers, and the other two hold at
least three each. Ask for any three whole-number totals that add up to the sum of what is left. If every bin, and
every two bins taken together, asks for at least 1 + 2 + ... + n, where n is how many numbers it holds, the split
can always be made. That floor is n above 0 + 1 + ... + (n − 1), the smallest total that n of the numbers 0 to M
could have. Because the three totals are fixed, a floor on two bins together also caps the third bin from above.

**Why it matters.** Proof G315 makes the same kind of split when every bin holds at least three numbers, and there
it only needs each total to be possible on its own. With a bin of two, that weaker condition is not enough, and this
result shows that asking for this small margin above the smallest possible totals makes up for it. It is one step
toward splitting into four or five bins with a bin of two, and it does not settle those larger cases.

**An everyday picture.** A sack of weights marked 0 kg, 1 kg, 2 kg and so on up to the heaviest, with one weight
lost (neither the lightest nor the heaviest), to be loaded, every weight, into a two-weight bag and two bigger bags
so that each bag hits its own target. Provided no bag, and no two bags together, is asked to come in lighter than
the 1 kg, 2 kg, 3 kg ... weights would make if it held just those, one of each up to its count, there is always a
way to load them.

## The formal statement and proof

**PROVED within the project's two-tier standard.** Cloud independently re-derived
G326's carrying steps in CL466, commit01131375, reviewing the candidate at
87521f60. Adopted MI502/GC1601. The theorem is exactly H2 as stated below;
novelty is UNASSESSED, and no four-/five-bin parent is promoted. The supporting
finite checks do not carry the unbounded theorem. The original candidate text
is retained as provenance. The later09:55 simplification is a SAME-WORKER
self-audit at57d97ec1, not covered by that independent review receipt.

**Historical candidate status follows.**

**PROOF-SKETCH: complete hand candidate, NOT independently verified.** Developed
in MI497–498. Uses the independently proved scalar lemmas and least-slack
construction in FOUR-BIN-PARTITIONS sections2–6 (G315), not MI460, G320–322,
MI430, the first-unhit generating function, or a finite H2 census. Novelty
UNASSESSED. The proposed extension audits precisely the size-two failures of
G315; it does not assert its unprotected extension, which is false.

**Statement.** Let M=b+c+2, b,c>=3, 1<=q<=M-1, and
P={0,...,M} minus{q}. Let integer targets u,v,w total M(M+1)/2-q.
If each nonempty proper group J of the three bins satisfies

    s_J >= C_J(C_J+1)/2,

there is a partition of P with sizes(2,b,c) and sums(u,v,w).
Here C_J is the sum of its bin sizes and s_J the sum of its targets.
All six inequalities are retained. Write L(r)=r(r-1)/2.

**1. Feasibility and a reflection guard.** The actual r-subset minimum in P
is L(r)+(r-q)_+<=L(r)+r. Complementary group bounds supply the actual
upper bound. The original one-hole scalar omissions (Lemma2) are excluded:
minimum+1 would require q=r, when the protected lower bound is L(r)+r,
r>=2; maximum-1 is the corresponding forbidden complement, also of size>=2.
Thus every target is individually feasible, not just in its rank interval.

Choose the smallest of all six ACTUAL singleton lower/upper slacks, giving
priority to the size-two bin whenever tied. Reflect the WHOLE original pool
once if necessary so selected bin A has lower slack h. Call the resulting
hole Q and targets s_A,s_B,s_C. After no reflection their protection is
s_J>=L(C_J)+C_J. After reflection it is instead

    s_J >= L(C_J)+lambda,       lambda=M-Q.

Indeed original total T=M(M+1)/2-q gives
rM-T+(M-r)(M-r+1)/2=L(r)+q. This is not preservation of H2 by reflection.
Actual scalar feasibility, six-slack minimality and the tie priority DO survive.

Let alpha(r),beta(r) be actual extrema in the oriented original pool,
a=|A|, and z_j=j+1_(j>=Q) its rank-j value. If the other sizes are r,t,
minimality of h yields

    s_r >= F_r=alpha(a+r)-alpha(a)=sum_(j=a)^(a+r-1) z_j.

For EVERY actual choice of A of its requested size and sum, deleting a
values leaves the residual r-minimum at most F_r. Applying the same bound
to t and conservation gives both residual rank bounds. This is the proved
least-slack selection argument, without assuming a completing partition.

**2. Pivot construction and the easy choice of A.** Use G315's extremal
prefix/suffix/pivot recipe for A: l low values, k high values and one pivot,
l+k=a-1. Successive pivot ranges meet, so an individually feasible target
either has a legal pivot or is a formal missing-pivot value. The high/low
sum-preserving repairs of G315 still exist when the remaining sizes total>=5:
if l,k>0 the two repair distances sum M-a+3>=8; the one-sided failures
would be original infeasible extrema/edge omissions. An available high
repair is preferred, with the one explicitly replaced choice in step5 below.

If a=2, both other sizes are>=3. Every scalar completion and rank estimate
of G315 applies unchanged. Its sole legal-pivot exception has Q=a+4,
s_A=L(a)+2 and a triple target3a+3. Its repair

    A*=[0,a-3] union{a-1,a},     D*={a-2,a+2,a+3}

also works at a=2: the prefix is empty, A*={1,2}, D*={0,4,5}.
M>=a+6 makes all values available. The structured repair lemmas still
have both remaining sizes>=3. This audits the only potential a>=3 use in
that construction. Hence the selected-size-two case completes.

It remains a>=3. Relabel the remaining bins so B is the pair and C has
size c>=3. Thus M=a+c+2. Endpoint/trimmed-hole legal pivots are covered by
G315's one-hole arguments: their only scalar omissions have distance1,
and the pair's relevant margin is2 (not an assumed margin3). Tight first-bin
faces exclude omissions by ORIGINAL scalar feasibility. Only two internal
holes and the structured missing-pivot repair pools need new analysis.

**3. Exact pair-gap lists, independently elementary.**

(a) In [0,U] with TWO distinct internal holes, U>=6, any absent pair sum
inside its actual pair extrema is in the following LOW list or its reflection:

| absent pair sum j | holes |
|---|---|
| 2 | {2,h}, h>=3 |
| 3 | {1,3} or {2,3} |
| 4 | {1,4} or {3,4} |

Every sum5..2U-5 has at least three disjoint original pairs, so two holes
cannot block it. For j1..4 list its one or two pairs. Discard sums below
the actual minimum; the displayed list is exhaustive. Reflection supplies
all high omissions. Endpoint holes are trimmed first and use Lemma2.

(b) Put V=c+4>=7 and

    H_p=[0,V] minus{p,p+1,V-1},       0<=p<=V-3;
    K_t=[0,V] minus{1,t,t+1},         2<=t<=V-1.

These are reflected pools: t=V-p-1. The complete LOW lists of omissions
inside actual pair extrema are

| pool | condition | absent sum |
|---|---|---|
| H_p | p=2 | 2,3 |
| H_p | p=3 | 4 |
| H_p | V=7,p=1 or4 | 6 |
| K_t | t=3 | 3,4 |
| K_t | t=4 | 4 |

All high omissions are the reflected opposite list. There are four disjoint
original pairs for each sum7..2V-7, so three holes cannot block them. For
low sums1..6 directly list pairs. The high hole V-1 can affect a low pair
only at V7,sum6; the remaining two edges15 and24 are both blocked only
at p1 or4. In K_t, hole1 blocks one edge, but consecutive t,t+1 cannot
hit both remaining edges at sums5 or6. Removing sums below the actual
minimum leaves exactly the table. This proves the lists for unbounded V,
without a finite-basis premise or the stronger unreviewed three-hole lemma.

**4. Legal pivot, two INTERNAL holes.** Here A=[0,l-1] union
[M-k+1,M] union{l+p}, with Q=l+q0, both holes internal to the middle.
Normalize its complement by subtracting l. Then

    U=M-k-l=c+3,   R=[0,U] minus{q0,p}.

The rank bounds give the normalized pair target at least
2k+3+1_(q0<=k+1)+1_(q0<=k+2), and the normalized C target at least

    L(c)+(k+1)c+[k+c-q0+1]_0^c,

where [x]_0^c=min(c,max(0,x)). For k>=1 all low pair gaps (<=4)
are excluded. A HIGH pair gap has reflected holes alpha=U-q0,
beta=U-p and reflected sum j in table3(a). Its normalized C target is

    L(c)+alpha+beta+j-6.

For j2 it is at most L(c)+c; j3 at most L(c)+2; j4 at most L(c)+5.
The lower bound L(c)+2c excludes all of them at k>=1. Thus only k0 remains.
Set a=l+1, l>=2, so s_A=L(a)+p and Q=l+q0.

The surviving LOW pair gaps are the five rows

    (q0,p,pair sum)=(3,1,3),(3,2,3),(4,1,4),(3,4,4),(4,3,4).

The first three contradict protection of A: without reflection p<a;
after reflection lambda=U-q0 equals c or c-1 and p<lambda. For the last
two choose a different A and pair, uniformly for ALL l>=2,c>=3:

| q0,p | new A | new pair |
|---|---|---|
| 3,4 | [0,l-2] union{l+1,l+2} | {l-1,l+5} |
| 4,3 | [0,l-2] union{l,l+2} | {l-1,l+5} |

Sizes and sums agree, all values lie in[0,M], avoid Q, and are disjoint;
conservation gives C. These are uniform replacements, not new hypotheses.

For HIGH gaps at k0, table3(a) and the displayed C bound leave only:
(i) j2,alpha2,beta=c+2; (ii) j4,alpha1,beta4,c3;
(iii) j4 with(alpha,beta,c)=(3,4,3),(4,3,3),(3,4,4).
To see exhaustion, j3 gives at most L(c)+2<L(c)+c. For j4 holes1,4
give excess3, permitting only c3,alpha1; holes3,4 give excess5,
permitting only c3,alpha3/4 or c4,alpha3. j2 permits equality only
at alpha2,beta=c+2.

Case(i) has p1, q0=c+1; protection of A excludes it: after reflection
lambda=U-q0=2>p, and before reflection a>=3>p.
Case(ii) is exactly G315's triple exception, now with remaining size2.
The same explicit repair still works: M=a+5, Q=a+4; use the A*,D*
formula in step2 and leave pair{a+1,a+5}. All sums and sizes match.

For the three cases(iii), assign [0,l-3] to A, subtract l-2 from the
remaining pool, and use this literal finite core. Its A has size3;
its pair has size2; its C has size c:

| alpha,beta,c | Mcore,Qcore | Acore | paircore | Ccore |
|---|---|---|---|---|
| 3,4,3 | 8,5 | 023 | 48 | 167 |
| 4,3,3 | 8,4 | 123 | 57 | 068 |
| 3,4,4 | 9,6 | 024 | 59 | 1378 |

Concatenated digits denote sets here. Core targets are
(3+p,2c+6,L(c)+2c+5), with(q0,p)=(c,c-1),(c-1,c),(c,c-1)
respectively. Restoring the translation and prefix gives every l>=2.
This completes all legal pivots under the actual least-slack orientation.

**5. High missing-pivot repair.** Write u0=M-k+1 and require k>=1,
u0-Q>=3. Replacing formal{Q,u0} by{Q+1,u0-1} leaves, after subtracting l,
H_p with V=c+4 and p=Q-l. The rank bounds are

    pair target >=2k+3+1_(p<=k+1)+1_(p<=k+2),
    C target >=L(c)+(k+1)c+[k+c-p+1]_0^c.

The ordinary low gaps2,3,4 are below the pair lower bound. The exceptional
V7,p1,sum6 has bound>=7. At V7,p4,sum6 the bound excludes k>=2,
so only k1 remains. Now c3, a=l+2>=3 gives l>=1, Q=l+4,M=l+7.
Use the LOW repair instead, explicitly:

    A*=[0,l-2] union{l,l+3,l+7},
    B*={l+1,l+5},      C*={l-1,l+2,l+6}.

Their respective targets are L(l)+2l+11,2l+6,3l+7, exactly the requested
ones; sizes are a,2,3. This is available even though the high repair failed.

For a HIGH gap, reflection gives K_t's low sums j3 or4, with
p=c or c-1. The C target is L(c)+1 or L(c)+2 for p=c,
and L(c)+4 for p=c-1. All are below L(c)+2c, so impossible.
This exhausts the high repair, without invoking Lemma4 at complementary size2.

**6. Low missing-pivot repair.** Here l>=1,Q-(l-1)>=3. Replace formal
{l-1,Q} by{l,Q-1}. Subtract l-1 from the complement to obtain K_t,
V=c+4,t=Q-l. Its rank bounds are

    pair target >=2k+5,
    C target >=L(c)+(k+2)c+[k+c-t+1]_0^c.

K_t's low pair gaps3,4 are excluded. For HIGH pair gaps reflect H_p's
low list, p=V-t-1. The j2/3 cases have t=c+1 and C targets L(c)+c
or L(c)+c+1, below L(c)+2c. For j4,t=c, the C target is L(c)+c+4.
The rank bound excludes it unless c3,k0. But then the actual pair UPPER
slack and selected A LOWER slack are both3:

    M=l+6,Q=l+3,s_A=L(a)+3, pair target=2l+8,
    beta_P(2)=2l+11.

The tie priority would have selected the size-two bin instead. Hence this
case cannot arise with a>=3. This is a selection rule at the original
least-slack step, not an assumption of a favorable pair later on.

The exceptional j6,V7 cases give t5 or2, c3. At t5 the C target8 is
below its bound9. At t2 the C target is14, and the bound is at least15
when k>=1. At k0 the selected
A target is L(a)+2. It violates protection: before reflection 2<a;
after reflection lambda=M-Q=4>2. Thus it is also impossible.
All low-repair pair gaps have now been excluded.

Every construction branch therefore either completes directly or has the
explicit replacement/tie exclusion above. Original scalar feasibility
ensures that some such first-bin construction exists. H2 follows, subject to
independent verification of this carrying case audit. This candidate does not
promote the full four-bin/one-size-two extension or the five-bin parent.

**Finite ingredient audit (MI498).** One same-worker invocation checks1128
complete pair-spectrum pools,932 literal repairs,2041 reflection identities,
and19 priority ties, with the preregistered can-fail controls. All pass.
These tests support the new tables/formulas only; they do not exhaust actual
least-slack roots or constitute independent carrying verification. Initial
proof_dupes --near G326 was called before the entry existed and failed on
an unknown target. After filing, --near W326 passes with344 entries; nearest
G319,G315,G317 read in full. G315 is the explicit construction being extended;
G319 fixes counts over two intervals and G317 has two holes/minimum size4.
None states H2, and their statuses are not altered by this candidate.

**Dated self-audit simplification, 2026-10-20 09:55 BST (MI501; review pending).**
The replacements above are valid, but the ACTUAL root rule excludes several
of their domains. This shortens the carrying proof without adding a premise.
This is algebra about all parameters, not an inference from zero visits in a
finite audit. Retain the original formulas as explicit controls.

In step4's high-gap audit at k0, set a=l+1,M=l+c+3. Every potential root
has h_A=p because Q=l+q0>a. Then:

- Case(i): Q=M-2, pair target2M-2, and actual beta_P(2)=2M-1.
  The pair upper slack1 equals h_A=1, so pair-first priority excludes A.
- Case(ii): c3,Q=M-1,p2. The pair target is2M-4, but its actual maximum
  is2M-2 (NOT2M-1, since M-1 is missing). Its upper slack2 equals h_A=2.
  Thus the old triple repair with a remaining pair2 is unnecessary here.
- The three fixed cores have pair target2M-4 and actual maximum2M-1,
  hence pair upper slack3. Two have p3=h_A and are excluded by priority.
  The first has c3,Q=M-3,p2. Before reflection it violates h_A>=a;
  after reflection it violates h_A>=lambda=M-Q=3. So it is also impossible.

Thus ALL remaining step4 high-gap branches are excluded by the original
root rule/protection; the translated cores are valid but unneeded. The only
new legal-pivot replacements actually needed are the two uniform LOW-gap rows.

The special step5 high-repair case has a=l+2,Q=M-3,M=l+7 and
s_A=L(a)+10, so h_A=10. The pair target2l+6 equals2M-8;
its actual maximum is2M-1, giving UPPER slack7<10. This contradicts
selection of A. Hence the alternate-low repair there is also unneeded.
The existing step6 exclusion by a pair upper/lower tie remains essential.

For clarity on the selected-a2 dependency, its recipe is especially explicit.
Let its requested sum be z. If z<=M and z!=Q, choose {0,z}; if z>=M
and z-M!=Q, choose {z-M,M}. Only positive distinct legal values are used;
individual scalar feasibility excludes z=0 or z=2M and the missing-end cases.
The two exceptional formal values are z=Q and z=M+Q. In the first,
scalar feasibility excludes Q1/2, and the low repair is {1,Q-1}.
In the second, it excludes Q=M-1/M-2, and the high repair is
{Q+1,M-1}. The scalar completion of these two structured remainders is
exactly G315's already proved argument with BOTH remaining sizes>=3.
For a legal first pair its only triple exception Q6,z3 is repaired by
A*={1,2},D*={0,4,5}. Thus no general size-two scalar lemma is hidden in
that use of G315, and all values/boundary cases in the extension are explicit.
