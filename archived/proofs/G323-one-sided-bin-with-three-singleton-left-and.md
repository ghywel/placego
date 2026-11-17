# One-sided bin with three singleton-left and equal-right crossings

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT323. One-sided bin with three
singleton-left and equal-right crossings (second-read by Cloud, CL446; moved here 2026-10-22)"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

With six or more numbers per row, four bins (one left-only, three taking one left number plus equal-sized right
shares) can meet any target sums passing the obvious checks.

**What it says.** Two rows of consecutive whole numbers, each at least six long and the right one's length a
multiple of three, are shared out among four bins (boxes): A takes all but three of the left row, and B, C and D
each take one left number and a third of the right row's numbers. Each bin has a target sum, and two checks are
plainly needed: the targets add up to the grand total, and every group of bins asks for a sum within the range
possible for that many numbers from each row. These checks are also enough: whenever they pass, all four targets can
be met at once. The proof nudges the three lone left numbers up one step at a time, each within the range its bin
allows, until the numbers left for A sum to A's target; an earlier result for three bins sharing one unbroken row
then deals out the right row.

**Why it matters.** The result survives sliding either row along the number line, so the rows can be the two sides
of one missing number in a longer row; dealing such a row into four bins of given sizes and sums is the wider
problem this serves. It covers only this one way of dividing each bin's numbers between the two sides, not right
shares of different sizes or bins taking several left numbers as well as right ones, and it does not show that a
workable division can always be chosen, so it does not solve that wider problem.

**An everyday picture.** Three friends must take different seats in one numbered cinema row, each within their own
stretch. From the lowest seats they may take, the friend furthest along who still has room moves up one seat, again
and again. Each move adds exactly one to their seat-number total, so it passes every total between their lowest and
highest seatings, and the checks ensure the wanted one is among them.

## The formal statement and proof

### GPT G323 — One-sided bin with three singleton-left and equal-right crossings (GPT,2026-10-18; reviewed by Cloud CL446, MI445)

*Status:* PROVED in scope, independent carrying read by Cloud CL446/a33d8bff; adopted in MI448.
*Where:* GPT-MATH-INSTINCT.md MI445;minimal P6,k2 diagnostic MI444 is finite support only.
*Novelty:* UNASSESSED. Verified dependency:MI295 three-bin full-interval theorem only.

**Review update, 2026-10-18 (MI448): PROVED in the stated scope.** Cloud CL446,
commit a33d8bff, independently re-derived all carrying steps below and reports
96,360 supporting cases with no failures. The original candidate wording is
preserved as history. No general count-selection or five-bin conclusion follows.

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


**Filing comparison.** proof_dupes --near W323:341 entries,no repeated
IDs;nearest W320(.20),W321(.16),W322(.16) read in full. Those protected
three-bin punctured-pool arguments use G319;this four-bin fixed-count
candidate uses MI295 and ordered representatives. Their pending status
is unchanged. No novelty verdict;no circular dependence on G323.
