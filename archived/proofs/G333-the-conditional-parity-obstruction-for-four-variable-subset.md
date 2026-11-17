# The conditional parity obstruction for four-variable subset intervals

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT333. The conditional parity
obstruction for four-variable subset intervals (second-read by Cloud, 2026-10-20)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

If fractions can meet whole-number limits on four numbers and their sums, whole numbers can too, except when the
limits pin everything to one answer made of halves.

**What it says.** Take four numbers whose total is a fixed whole number, and set a whole-number lower and upper
limit on the sum of every group of one, two or three of them. Suppose some choice of the four with that total,
fractions allowed, keeps every sum within its limits. Then some choice of four whole numbers does too, with one
exception. The exception is when the limits pin every sum of two of the numbers to a single value, and the three
pinned sums that include the first number add up to an odd number while the total is even, or to an even number
while it is odd. Only one choice then fits, and each of its four numbers lies halfway between two whole numbers,
such as 1/2 or 3/2.

**Why it matters.** It serves the project's puzzle of sharing out a run of whole numbers, one of them missing, among
four bins of chosen sizes and totals, where the four numbers are how many of each bin's members lie above the
missing number. There it turns the hunt for whole-number counts into a hunt for fractional ones, plus a check for
the one exception. It does not show that fractional counts exist, does not by itself rule the exception out in that
puzzle (that is left to proof G334), does not say which numbers go in which bin, and is not claimed for five or more
numbers in place of four.

**An everyday picture.** Four children share four sweets. If Ann and Ben must have one sweet between them, Ann and
Cat two, and Ann and Dan two, the only share that fits is half a sweet each for Ann and Ben and one and a half each
for Cat and Dan, so sweets must be cut. Let Ann and Ben have one or two between them and one whole sweet each fits;
for four children and rules in whole sweets, the knife is only ever needed when the rules leave just one possible
share.

## The formal statement and proof

**Current status: PROVED within project standards, CL474/16404637, adopted MI575.**
Cloud carried singleton-facet integrality, the fractional pair-box corner,
the one-unit parity correction and both directions, including degenerate
faces. Nonempty REAL P and integer endpoints remain hypotheses; no
integrality-of-all-vertices or five-variable assertion. Supporting I2
reports20000 integer systems,17094 REAL-nonempty,1015 genuine obstructions,
zero mismatches. GPT read the complete instrument, not rerun. Novelty
UNASSESSED. The original candidate below is preserved as discovery history;
its pending-review wording is historical. The protected application is
G334, not an additional conclusion of this general theorem.

### GPT G333 — The sole real/integer obstruction for four-variable subset intervals (GPT, 2026-10-20; waiting room, MI555–556)

**Status: COMPLETE HAND PROOF CANDIDATE, not independently verified.**
Cloud CL472/49912d98 supplied the pair-box coordinates. This argument
isolates their integer-feasibility obstruction; novelty is UNASSESSED.
No partition theorem or protected-parent existence theorem is asserted.

**Statement.** Let H and all bounds l_J,u_J be integers, for every
nonempty proper J subset of{1,2,3,4}. Define the bounded polytope

    P={k in R^4: sum_i k_i=H, l_J<=k(J)<=u_J for all J}.

Assume P is nonempty. Symmetrize each bound against its complement:

    a_J=max(l_J,H-u_(J^c)), b_J=min(u_J,H-l_(J^c)).

Put A=(a_12,a_13,a_14), B=(b_12,b_13,b_14). Then P contains NO
integer vector if and only if A=B and A_1+A_2+A_3 is incongruent
to H modulo2. In that exceptional case P is a single half-integral
point, with all four coordinates nonintegral. Thus any positive width
among these three pair intervals guarantees an integer point, provided
P is real-feasible. Empty real regions are excluded explicitly.

**Proof.** Complement symmetrization preserves P since k(J^c)=H-k(J).
Write a_i,b_i for the resulting singleton bounds. The only remaining
independent constraints are those four singleton intervals and the
three pair intervals. Set y=(k_1+k_2,k_1+k_3,k_1+k_4). On the total-H
hyperplane this is an affine isomorphism, whose inverse is

    2k_1=y_1+y_2+y_3-H,
    2k_2=y_1-y_2-y_3+H,
    2k_3=-y_1+y_2-y_3+H,
    2k_4=-y_1-y_2+y_3+H.

The pair constraints are exactly A<=y<=B. The four singleton
intervals are four slabs. For integer y, all four inverse numerators
have the same parity, so k is integral exactly when sum(y)==H mod2.

First, any vertex v of P on a singleton boundary is integral. Indeed,
fixing k_i to that integer endpoint leaves three variables with an
integer total. Every subset inequality then becomes an integer bound
on one of those variables: two of the remaining three are the
complement of the third, and pairs containing i give singleton bounds
after subtracting its fixed value. The face is therefore a box in
three variables intersected by an integer-sum plane. At a vertex of
such a face, at least two coordinates are at integer endpoints;
otherwise two coordinates can be perturbed oppositely in both
directions, contradicting extremality. The total makes the third
integer. A vertex of P remains a vertex of this face. This also
handles redundant bounds, tied endpoints and lower-dimensional faces.

Choose a vertex v of nonempty bounded P. If it is integral, the
required point is already found. Otherwise the preceding paragraph
shows that ALL singleton inequalities are strict at v. Each y
coordinate must then lie at an endpoint of its pair interval:
if one were interior, a sufficiently small positive and negative
change of that coordinate would preserve the box and all strict
slabs, again contradicting extremality. Thus y(v) is an integer box
corner. Since v is fractional, all four v_i lie in Z+1/2.

If some B_j>A_j, the integer endpoints give B_j-A_j>=1. Move y(v)
one unit along axis j TOWARD the other endpoint. This stays in the
pair box, including when the other two intervals are singletons.
The inverse formula changes each k_i by exactly plus or minus1/2.
Every half-integer v_i strictly between integer a_i,b_i satisfies
a_i+1/2<=v_i<=b_i-1/2. Hence all four changed coordinates stay in
their singleton intervals, in either sign direction. The changed
point therefore lies in P. Its y parity has flipped, making every
k_i an integer. This proves the positive-width assertion.

If P is integer-empty, the vertex argument now forces A=B. The
affine inverse leaves just one possible k, and nonemptiness puts it
in all four slabs. Its parity must be wrong. Conversely, if A=B
with wrong parity, every feasible k is that unique nonintegral
inverse point, so P has no integer point. This proves both directions.

**Hand controls and hypotheses.** With H4, y=(1,2,2), all singleton
bounds[0,2], the only k is(1/2,1/2,3/2,3/2): a genuine obstruction.
It is CL472's actual q4,count2222,target5/5/11/11 example. The
baseline-protected min3 example M12,q1,counts3333,targets6/21/24/26
instead has unique y=(5,5,5), H11, giving integer k=(2,3,3,3);
its literal partition is024/{3,7,11}/{5,9,10}/{6,8,12}.

For the degenerate-width control take H4, y_1 in[1,2], y_2=y_3=2,
k_1,k_2 in[0,1], k_3,k_4 in[1,2]. The bad corner is the first
half-integral point above; the unit step gives(1,1,1,1), hitting ALL
four singleton boundaries. Two pinned axes therefore cause no gap.
For the empty-region guard, pin y=(1,2,2) but impose k_1>=1:
there is no real point, and the statement deliberately makes no
existence claim. Integrality of endpoints is essential: replacing
the first control's width by y_1 in[1,2] but imposing k_1<=1/2
can trap the wrong-parity point despite positive box width.

**Coverage and limits.** This proves an exact conditional integer
selection criterion for the entire four-variable interval class,
not merely for measured inputs. Protected-parent real feasibility
and exclusion of its forced wrong-parity box remain OPEN, as does
physical completion of thin count rows. The result does not say P
is an integral polytope, nor extend automatically to five variables.
No numerical experiment, census or machine verification was run.
Only elementary vertex and interval arguments are used; no unread
partition result is a premise. Independent carrying review pending.
