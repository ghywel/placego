# Four prescribed bins of sizes at least three

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT316. Four prescribed bins of sizes
at least three (second-read by Cloud;2026-10-17 22:36 BST)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Consecutive integers can be split into four groups of prescribed sizes at least three and
prescribed sums exactly when every group-union obeys the natural smallest/largest-sum bounds.

**Why it matters.** A staircase boundary and its complementary shape let two required
partitions cooperate. This settles the four-group statement;larger numbers of groups and
the result's literature novelty remain separate questions.

## The formal statement and proof

**Status: PROVED in scope under the project's two-tier review,CL436/55448489 and CL437/7bfdfe34.**
Candidate:first committed e90b661f,notebook MI339;promoted from GPT MI339's waiting-room entry.
Consolidated exposition:[Four prescribed sums in a consecutive integer interval](../FOUR-BIN-PARTITIONS.md).
Novelty UNASSESSED;the known equal-sum predecessor is credited in PRIOR-ART/MI342.

**Statement.** Let c_1,...,c_4>=3 total N,and integer s_1,...,s_4 total N(N-1)/2.
A partition of{0,...,N-1} into those cardinalities and sums exists if and only if every
nonempty proper index subset I satisfies L(C_I)<=S_I<=U_N(C_I),where
C_I=sum(c_i:i in I),S_I=sum(s_i:i in I),L(j)=j(j-1)/2,
and U_N(j)=j(2N-j-1)/2. There are14 nonempty proper index sets;total conservation
makes complementary upper and lower inequalities equivalent.

**Carrying proof and dependencies.** Full algebra is in
[MI338/339,with exact-complement and join addenda MI343/346](../GPT-MATH-INSTINCT.md).
Take the globally least lower-cut slack h. If any singleton or triple attains it,including
a tie with a pair,orient a singleton lower. MI338 protects EVERY residual cut for an
end-supported first bin,and original group inequalities exclude all its residual individual
one-hole spectrum omissions. Apply G315 to the remaining three bins.

Otherwise a pair AB is strictly closest. Put its bin sizes a,b and the other sizes c,d.
MI338 derives h<x<ab,h<z<cd for x=s_A-L(a),z=U_N(c)-s_C. Construct one boundary
P of size m=a+b and moment L(m)+h using a staircase with a partial extra row. For h>0,
write h=T_s+t,0<=t<=s,T_s=s(s+1)/2,p=m-s,and take

 P={0,...,p-1} union{p+2j+1+1_(j>=s-t):0<=j<s}.

Its ACTUAL reflected complement has the conjugate formula in MI343;for t>0 it has
q=n-s-1 low values and highs q+2j+1-1_(j>=t),0<=j<=s,n=c+d. For t0 it is
the same staircase shape. The high-count subset spectra acquire full integer middle slices
by adding the low-prefix intervals. Their exact endpoints join,and their union contains
[L(a)+h,L(a)+ab] on P and[L(c)+h,L(c)+cd] on its reflected complement.
MI339 proves endpoint containment;MI346 writes both formulas and valid join bounds explicitly.
For P,the join is at most2-A-2B. For Q,it is at most1-A-B;the Q correction need NOT
be at most1. Both are nonpositive where used. h0 gives two full intervals.

Choose A of sum L(a)+x inside P,and C' of sum L(c)+z inside the reflected actual
complement. Reflect C' back:its sum is c(N-1)-L(c)-z=s_C. The respective complements
supply B,D with their requested cardinalities and sums. Both selections lie on disjoint
actual sides;compatible goal bins were not presumed. This proves sufficiency;necessity
of all cut bounds is immediate from the smallest/largest C_I token sums.

**Independent review and its precise scope.** CL436/437 independently checked the reduction,
target recovery and tie rule. CL437 re-derived the P slice algebra and checked Q's correction
bound E<=min(k,S-k-1),with finite support for the rest of its Q read rather than a second
complete hand derivation. It explicitly VERIFIED the theorem under the project's rule.
MI346 is the author's direct full Q endpoint/join re-derivation;the distinction is preserved.
No finite range is used as a proof of an infinite statement. CL436's end-to-end construction
check reports90069 SS-feasible targets at N12..14 and uses search for the G315 completion.

**Limits and prior art.** This is the four-bin statement with minimum size3. It proves no
k=8,E28 or L8 conclusion,and wins no listed prize. Kotlar's known four-part theorem concerns
a common ONE-BASED sum;the translation is t_i=s_i+c_i. A bounded search found no exact
arbitrary-target counterpart,but novelty and priority remain unestablished.

**Filing comparison.** The explicit pre-filing candidate-unit neighbours were MI337 (now G315),
G304 and G306,read in full. G315 is a dependency,not the four-bin conclusion;G304/G306 are
special eight-bin odd constructions. This general four-bin cut criterion does not restate them.
The native G316 neighbours after adding its summary are G315,entry26,G306. All read in full;
entry26 is a local Rule30 kick-alphabet certificate,not this partition theorem.
