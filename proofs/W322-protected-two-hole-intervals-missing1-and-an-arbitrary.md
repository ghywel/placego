# Protected two-hole intervals missing1 and an arbitrary second value

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G322 — Protected two-hole
intervals missing1 and an arbitrary second value (GPT,2026-10-18;waiting room,MI407-409)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A run of numbers from 0, missing 1 and one other, can be split into any three groups of three or more whose totals
keep a safety margin.

**What it says.** Take the whole numbers from 0 up to some top number, and remove 1 and any one larger number.
Choose three group sizes, each at least three, that together account for every remaining number, and three target
totals that add up to the sum of those numbers. The safety margin asks that each group's target, and the combined
target of each pair of groups, be at least 2 + 3 + 4 + ..., with one term for each number held: at least 9 for a
group of three, and 27 for two groups of three together. That floor always sits above the smallest total that many
of the numbers could make. Whenever the margin holds, the numbers can be split into groups of exactly those sizes
and totals.

**Why it matters.** Proof G317 handles the same kind of run for groups of four or more, asking only that each total
be possible on its own. For groups of three that is not enough, and this result reaches them by asking for the
margin on pairs of groups as well as on single groups. It says nothing about targets that miss the margin, does not
cover two missing numbers placed anywhere (one of them must be 1), and does not settle the larger five-group
splitting question behind this work.

**An everyday picture.** Three players share out a set of numbered pool balls, counting the white cue ball as 0,
after the 1 ball and one other have rolled under the sofa. Each is promised three or more balls whose numbers add up
to a set score, and the three scores add up to the total of the numbers on all the balls left. If the 4 is the lost
ball, two players each promised three balls with a score of 12 can never both be paid, because any two such trios
share a ball; the margin forbids that pair of promises, since 12 + 12 falls short of 27, and whenever it holds,
every promise can be kept.

## The formal statement and proof

**Dependency update,2026-10-18:** The G319 dependency is now PROVED (CL442);G322's own two-hole argument remains a candidate.
This entry stays PROOF-SKETCH;its historical pending-G319 wording is superseded.

*Status:* COMPLETE COMPOSITE HAND PROOF-SKETCH;independent review pending.
*Where:* GPT-MATH-INSTINCT.md MI407,MI408,MI409,with full carrying arguments and controls.
*Novelty:* UNASSESSED. Conditional on pending G319 and generic zero-row compatibility MI383.

**Statement.** Let R=[0,M] minus{1,q},2<=q<=M. Three integer
sizes a,b,c>=3 sum to M-1. Integer targets total sum(R) and satisfy
u_J>=L(s_J)+2s_J for every proper nonempty bin group J,where
L(s)=s(s-1)/2. Then R has a partition of these sizes and sums.
The first deleted value remains1;arbitrary p,q and full five-bin
sufficiency are not conclusions.

**Source-level proof and dependency map.** Assign0 to a prospective
root A;its remaining size is a-1>=2. The positive intervals are
[2,q-1] and[q+1,M],of lengths P=q-2,Q=M-q. Define

```text
f_r(k)=2r+(q-1)k+L(r-k)+L(k),
g_r(k)=(q-1)(r-k)-L(r-k)+Mk-L(k),
K_i={legal k:f_(r_i)(k)<=u_i<=g_(r_i)(k)}, r=(a-1,b,c).
```

MI408 proves that some root has every K_i nonempty. The exact
one-hole scalar lemma retains both possible endpoint gaps,including
size2. Nonroot failure forces u<=alpha_s+1;two such failures violate
a protected pair cut. The unique failed nonroot,if any,is root-eligible
because beta_(s-1)-alpha_s>=5 and the lower root gap is excluded.
If there is no nonroot failure,concavity gives
sum beta_(s_i-1)>=T-alpha_6+2 beta_2,and
2 beta_2-alpha_6-3>=2. Thus not all three roots can fail.

MI407 proves that EVERY scalar-eligible root meets both aggregate
count bounds. Its complete unprotected deficit calculation reduces
maximum shortage to a cross-product budget2 and the sole family
(3,b,3),q=b+3,M=b+7,targets(2b+8,L(b)+2b+2,3b+14).
Its A+B protected pair cut fails. Positive-value reflection gives the
sole minimum-excess family q6,M=b+7,targets(10,L(b)+8b-2,13),
whose A+C pair cut fails. Hence sum min K<=Q<=sum max K.
Choose integer counts with the correct total by interval interpolation.

G319 handles positive count rows. MI378's regular-row splitting and
MI383 section1's fixed-count singleton repairs handle generic zero rows;
their derivations apply to arbitrary interval offsets. The only remaining
shape has one bin X owning a whole interval and one value of the other,
with a minimum-plus1 omission for a different bin D. MI409 completes
both orientations by the following explicit arguments.

If X owns all high values and low value d+2,then D's target is
L(d)+2d+1. The D+E protected pair cut forces0 to belong to X;
thus d,e>=3. Keep the highs in X and give it low values2,d. Give D
0,all values3..d+1 except d,and value d+3. Its cardinality is d
and its sum is the required target. E receives the remaining lows;
its size and target follow by conservation. All values are present and
distinct because d>=3,e>=3. The root moves from X to D.

If X owns all low values and high value q+1+d,then
u_X=L(q)+q+d,u_D=d(q+1)+L(d)+1. The X+D pair cut forces0
into E. Thus q>=4,d>=3,e>=2. Change the low/high count rows to
(P-1,1,0)/(2,d-1,e),in order X,D,E. They are regular. For X
the lower and upper excesses over its target are3-d and
2M-q-d-4;for D they are1-q-d and(d-1)(e+1)-3. The signs
admit both targets;E is unchanged. MI378 and reviewed MI295 finish.
Empty positive intervals use MI295 directly with all residual sizes>=2.

This establishes the composite candidate with no numerical premise
and no use of G321,MI399,W318 or general two-hole completion.
The full calculations and adversarial hand controls are in MI407-409;
all new carrying steps and the pending G319 dependency require review.
G317 already proves individual-spectrum sufficiency at minimum4;
this candidate reaches minimum3 using stronger protected pair cuts.

**Filing comparison.** Native proof_dupes --near W322 passes with340
entries and no repeated IDs. Nearest W321,W319,W320 read in full:
W319 is the pending fixed-positive-count ingredient;W320/W321 concern
the three-hole low shape,not this protected two-hole family. G317
has weaker scalar hypotheses but requires every size>=4;the present
minimum3 statement uses protected pair cuts. No novelty verdict follows.
The first nearest-entry call preceded insertion of W322:its ID scan
passed but target lookup failed because W322 did not yet exist. After
insertion,the full check succeeded;no mathematical test was rerun.


*GPT G323, G324 and G325 stood here. Their carrying reads having landed, Cloud moved them verbatim to the end of
section E2 on 2026-10-22 (spring clean), each under a G.GPT wrapper heading as E2's other entries are.*
