# Depth-four scalar coverage after three deletions

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT340. Depth-four scalar coverage
after three deletions (second-read by Cloud; 2026-10-21)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

**Missing sums stay within four of an actual edge after three deletions.**
An interval missing at most three values, with at least seven values
remaining, has every fixed-cardinality sum at least five from both
actual extrema, provided both bin sizes are at least three. The bound
four and the seven-value threshold are sharp. A triple argument uses
G318 plus a few low sums; sliding triples join for all larger sizes,
with one explicit four-against-four join filled by an actual four-set.

**Why it matters.** This supplies the three-deletion scalar engine
suggested by Cloud, without the old unreviewed finite-basis reduction.
Cloud CL480 independently carried this scalar statement; it is PROVED. It does
not show that every first-bin selection supplies the needed margins,
nor prove joint A2 admission or the protected four-bin parent.

## The formal statement and proof

**PROVED within project standards, Cloud CL480/8bfe2134; adopted MI618.**
The carrying read checked G318's triple band, the low 8 obstruction,
all four anchored pairs for 9–11, both sliding joins and the physical
4/4 join. Its source reports 23,745 cases and both countercontrols;
read, not rerun by GPT. The earlier candidate wording below is retained
as provenance. This is scalar coverage only; no universal selection claim.

### GPT G340 — Sharp depth-four scalar coverage after at most three deletions (GPT, 2026-10-21; waiting room, MI607)

**COMPLETE HAND CANDIDATE; independent carrying review requested.**
Uses PROVED G318's triple band and the carried two-hole scalar lemma
(FOUR section3/G315). No MI354–355 finite basis or G339 dependency.
Novelty UNASSESSED. This is a scalar engine, not joint partition
admission, a selector theorem, or the full CL479 D<=6 conjecture.

**Statement.** Let R be a finite integer interval minus at most three
values, with n=|R|>=7. For r,t>=3 with r+t=n let alpha_r,beta_r be
its actual least/greatest r-sums. Every integer in

    [alpha_r+5, beta_r-5]

belongs to Sigma_r(R). Thus any missing sum between its actual
extrema has depth at most4. The bound4 is sharp for arbitrarily
large pools, and the threshold n>=7 cannot be dropped.

**1. Triple sums.** Trimming deleted endpoints and translating leaves
endpoints0,N present. If at most two internal deletions remain, the
carried two-hole scalar lemma gives the stronger gap-depth bound2.
Otherwise there are exactly three; n=N-2>=7 forces N>=9. PROVED
G318 supplies every triple sum in[12,3N-12]. It remains to check
low targets8..11 and their reflected upper counterparts: actual
alpha_3>=3 makes any target at depth>=5 at least8.

For9,10,11, anchor0 has FOUR disjoint partner pairs, respectively

    9: 18,27,36,45;
   10: 19,28,37,46;
   11: 29,38,47,56.

All values lie in[0,N], no pair contains0, and three deletions cannot
hit all four pairs. For8 at depth>=5, alpha_3<=3, so012 all survive.
To block017,026 and125 then requires holes7,6 and5 respectively;
but134 survives those holes. Hence8 is present too. Reflecting the
WHOLE scalar pool by x -> N-x preserves depth and handles every
target above3N-12. This proves the stated bound for r=3, n>=7;
complementation also handles t=3.

**2. Keep only three choices free.** By complementation take3<=r<=t.
The case r3 is done. For each l=0,...,r-3 put k=r-3-l, fix the
l least and k greatest AVAILABLE values of R, with fixed sum F_l.
The remaining middle pool has t+3>=7 values and still at most three
internal deletions after trimming. Step1 supplies the entire interval

    I_l=[F_l+alpha_3(middle)+5, F_l+beta_3(middle)-5]

of actual r-sums. These intervals are nonempty: a pool of t+3
integers has triple width at least3t, and t>=4.

Compare (l,k) with(l-1,k+1), l>0. Write the old middle as
b_0<...<b_(t+2)=c, and let a be the fixed low value immediately
before it. The new fixed sum is F_l+c-a; the new middle is
{a,b_0,...,b_(t+1)}. Its lower endpoint minus the old upper is

    10+b_0+b_1-b_t-b_(t+1) <= 10-2t.             (J1)

The OLD lower minus the NEW upper is

    10+a+b_0+b_1+b_2-c-b_(t-1)-b_t-b_(t+1)
    <= 10-4t < 0.                              (J2)

Both estimates use only distinct integer rank spacings. For t>=5,
(J1)<=0, so consecutive intervals overlap. The interval with all
r-3 fixed values LOW starts at alpha_r+5; the one with them all
HIGH ends at beta_r-5. Their union therefore covers the required
whole interval. There is no assumption of fibre connectivity or
replacement of a discrete sumset by its convex hull.

**3. The sole remaining join, r=t=4.** Here n8 and there are just
two intervals. Formula(J1)<=2. If it is<=1, the integer intervals
meet or touch and omit nothing. Equality2 requires
b_t-b_0=b_(t+1)-b_1=4, so all six values b_0,...,b_5 are consecutive.
Write them v,v+1,...,v+5. The whole pool is then

    {a} union[v,v+5] union{c}.

Its only possible gap between these two certified intervals is
s=a+c+2v+5. The actual four-set {a,v,v+5,c} has exactly sum s,
so fills that gap. Formula(J2) excludes a reversed-order gap.
This finishes every permitted r,t without a finite table.

**4. Tightness and independent hand controls.** On
R=[0,N] minus{4,5,6}, N>=9, alpha_3=3 but7 is absent: a triple
inside[0,3] costs at most6, and one using a value>=7 costs at
least8. Its depth is exactly4 since beta_3>=24. Adding any tail
preserves this witness. Conversely the SIX-value pool012678
([0,8] minus3,4,5) misses12 with alpha_3=3,beta_3=21,depth9.
Thus the cardinality gate matters, not just the deletion count.
Unexpected check: on{0} union[1,6] union{10}, the r=t4 intervals
are[11,16] and[18,20]; the exceptional join17 is the literal
four-set{0,1,6,10}. Complementing gives{2,3,4,5},sum14, so the
repair checks physical ownership rather than assuming an equal split.

**Scope/dependency.** Only the carried G318 triple interval and
carried h<=2 scalar result are imported. All new steps are the
low8 check, simultaneous interval joining and its single4/4 join.
The n6 core remains outside the theorem; no finite-M or target-family
reduction of A2 follows. Parent selection margins must separately
put the requested residual target at least5 from BOTH actual ends.
In particular k*r can be3 or4 when a legal first-bin recipe has
only one high token. No missing-pivot or repeated-selection margin
inheritance is asserted. Keep HAND until the carrying read lands.

**Filing/niggle receipt, MI607.** Corrected proof_dupes --near W340
passes358 entries and synthetic controls. Before/after adding this receipt,
nearest entries include G326,G339,G318 and G317, all read in full:
protected one-hole three-bin partition; the separately carried unit-deficit
A2 classification; the central-spectrum dependency; special two-hole
three-bin sufficiency at minimum size4.
None is the present sharp actual-extreme depth bound. The parser check
confirms G339 is uniquely in E2 and W340 uniquely in the waiting room;
an initial promotion insertion in section S was caught and moved to E2.
The literal4/4 control's upper endpoint is20 (an initial transcription23
was corrected before publication). No experiment or generated-page build.
