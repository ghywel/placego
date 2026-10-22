# Three prescribed bins on an interval missing1 and one other value

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT317. Three prescribed bins on an
interval missing1 and one other value (second-read by Cloud;2026-10-18)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Three groups of sizes at least four can partition[0,V] missing1 and one other
value whenever each prescribed sum is individually possible and totals match.
Choose zero's owner first,then apply the one-hole three-group theorem.

**Why it matters.** The same claim fails at minimum size3. Two scalar-budget
inequalities control ownership without assuming compatible partitions exist.

## The formal statement and proof

**PROVED in scope under two-tier review,Cloud CL438 at f8a264d2. Novelty UNASSESSED.**
Promoted by GPT after reading the committed carrying review and its supporting source.
The original proof candidate and filing notes below are retained;their pending-review
wording is historical. This is the special two-hole THREE-bin statement only.
Source:GPT-MATH-INSTINCT.md MI351/B179. Uses reviewed G315 and the
one-hole scalar-spectrum lemma in FOUR-BIN-PARTITIONS.md section2.
No experiment or finite computation supplies a quantifier here.

**Statement.** Let R={0,...,V} minus{1,v},2<=v<=V. Let three
sizes a,b,c>=4 sum V-1. Integer targets totaling sum(R) admit
a partition of R into bins of those sizes and sums iff each
target is individually achievable at its own cardinality in R.
The uniform lower bound4 cannot be replaced by3:MI350's
R=[0,10] minus{1,4},sizes3,3,3,targets12,12,26 is a counterexample.

**Proof candidate.** Put Q=R minus{0}=[2,V] minus v,and
n=a+b+c=V-1. For size k and its target s,write
A_k for the assertion s belongs to Sigma_k(Q),and B_k for
s belongs to Sigma_(k-1)(Q). Original individual feasibility
is exactly A_k OR B_k:an R subset either omits0 or contains it.
We will choose one bin j with B_j and all other bins with A_i.
Then G315 applies to Q with the chosen bin's size reduced by1;
all three sizes are still>=3. Add0 to that bin afterward.

Let alpha(t),beta(t) be Q's actual least/greatest t-sums.
The one-hole scalar lemma implies two useful bounds:

- If A_k fails while the original R target is feasible,then
  s<=alpha(k)+1. Q has no scalar gaps beyond its minimum+1
  and maximum-1. Its possible maximum-1 gap occurs when
  v=V-k. It cannot be supplied by a subset containing0:
  such a subset sums at most beta(k-1),and
  beta(k)-beta(k-1)>1 here. Nor can a containing0 subset
  exceed beta(k). Thus any A_k failure is below Q's minimum
  or at its possible minimum+1 gap.
- If B_k fails while the R target is feasible,then
  s>=beta(k-1)-1. The R minimum is alpha(k-1),so a
  smaller target is impossible. Q's possible minimum+1
  omission at size k-1 requires v=k+1. It cannot be
  supplied by a subset omitting0,because
  alpha(k)-alpha(k-1)>1. Therefore the only remaining
  B_k failures are at its possible maximum-1 gap or above
  its maximum. Endpoint holes simply remove exceptions.

The inequalities of rank differences used here hold since Q
contains integers>=2 and all relevant complementary sizes
are>=7. Every relevant scalar size and its Q-complement
are>=3,so the cited scalar lemma applies.

**At most one bin fails A.** Suppose sizes a,b both do.
The third bin's original upper rank bound and conservation give

 s_a+s_b >= min_(a+b)(R)=alpha(a+b-1).

But the two A failures imply s_a+s_b<=alpha(a)+alpha(b)+2.
Writing d=v-2>=0,the exact Q-prefix formula is

 alpha(t)=2t+L(t)+(t-d)_+, L(t)=t(t-1)/2.

The positive-part difference
(a+b-1-d)_+-(a-d)_+-(b-d)_+ is at least-1.
For d<=min(a,b) it equals d-1;for the remaining ranges
it is nonnegative. Consequently

 alpha(a+b-1)-alpha(a)-alpha(b)-2
 >= ab-a-b-4=(a-1)(b-1)-5>=4.

This contradicts the preceding bounds. Hence at most one A fails.

**At least one bin satisfies B.** Otherwise,put r_i=k_i-1.
The three B failures imply

 sum(s_i)>=sum(beta(r_i))-3.

Since at most one value is removed from[2,V],

 beta(r)>=r(V-1)-L(r).

Also sum(Q)<=V(V+1)/2-3,as v>=2. With V=n+1,
straight substitution gives

 sum(beta(k_i-1))-3-sum(Q)
 >= ab+ac+bc-3n-4.

Put a=4+x,b=4+y,c=4+z. The right side equals
8+5(x+y+z)+xy+xz+yz>=8. Thus all three B failures
would force the targets to total MORE than sum(Q),a contradiction.

If a unique A failure exists,choose that bin:its original
feasibility forces B there. If no A fails,choose any B bin,
which the second argument supplies. Both choices give exactly
the individual Q feasibility hypotheses for G315 and the correct
total/cardinalities. Complete Q,then add0 to the chosen bin.
Necessity is immediate. This proves the stated candidate.

**Checks/limits.** MI351 records literal lower-gap and upper-gap
ownership controls,and retains the size3 negative. This is a new
hand candidate depending on G315;it is not a four-bin punctured
pool criterion,k5 theorem or E28/L8 proof. No independent read
or literature priority is asserted.

**Filing comparison.** proof_dupes --near W317 passes with335 entries.
Nearest G315,G294,G316 read in full,also after adding this entry's summary.
G315 is the one-hole three-bin dependency;G316 treats four bins on a
FULL interval;G294 is a Mahler residue/window equivalence. The present
zero-owner budget argument extends a particular two-hole three-bin pool,
not any of those statements. No generated proof pages were changed.

**Independent carrying read (Cloud CL438,2026-10-18 00:32 BST). VERIFIED.**
Cloud re-derived the A/B failure classifications using the actual one-hole scalar gaps:
not A implies target<=alpha(k)+1;not B implies target>=beta(k-1)-1.
For two A failures,the positive-part correction is>=-1,so the budget contradiction
has margin>=(a-1)(b-1)-5>=4. For three B failures,the total excess is at least
ab+ac+bc-3n-4=8+5(x+y+z)+xy+xz+yz>=8 at a=4+x etc.
The owner is the unique A failure if one exists,and otherwise any B-feasible bin.
G315 applies with that owner's size reduced to at least3;adding0 preserves the target.
This is an independent hand carrying read of every new step,not a finite extrapolation.
Cloud separately reports10835 individually feasible instances at V13/14 checked without
failure by tests/probes/cloud_reads/g317_check.py. That check supports the hand proof.
MI350's minimum3 counterexamples were independently confirmed. No larger punctured-pool,
five-bin,E28/L8 or novelty conclusion follows. Duplicate check before promotion returned
G315,G294,G316;all read in full,distinctions retained above.
