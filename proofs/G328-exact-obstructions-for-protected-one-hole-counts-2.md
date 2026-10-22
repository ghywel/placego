# Exact obstructions for protected one-hole counts (2,2,c)

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT328. Exact obstructions for
protected one-hole counts (2,2,c) (second-read by Cloud, 2026-10-20)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Given a small margin, a run of numbers with one gap can be split into two pairs and a big bin with requested totals,
except in three cases.

**What it says.** Take the run of whole numbers from 0 up to some top number and remove one that is not at either
end, leaving a gap. Divide what is left among two pairs and one big bin of at least three numbers, each bin with a
requested total, the three totals adding up to the sum of all the numbers. Suppose every bin, and every two bins
together, asks for at least 1 + 2 + ... + r, where r is how many numbers they hold: a small margin above the least
that many numbers could add up to (so a pair asks for at least 3, and both pairs together for at least 10). Then it
can always be done, except in exactly three cases: the gap is at 1 and the pairs ask for 4 and 6, however long the
run; or the run is 0 to 7, the gap is at 3, and the pairs ask for 3 and 8, or for 4 and 10. In each, one pair total
can be made only one way, and that pair shares a number with every pair that could make the other.

**Why it matters.** With one pair and two bins of at least three numbers, the same margin is always enough (proof
G326); with two pairs it is not, and this result lists every failure. Each failure sits exactly on the edge of one
margin, so asking for strictly more than 1 + 2 + ... + r everywhere always works. It covers three bins only: a
four-bin result uses it as one step, but on its own it settles no four-bin case and solves no prize problem.

**An everyday picture.** The opposite faces of a die pair off to make 7 (1 and 6, 2 and 5, 3 and 4), and no face is
in two of those pairs, because each face has only one partner; in the same way, no number in the run is in two pairs
that make the same total. That is the heart of the proof: if each pair total can be made in two or more ways, a pair
for each can always be found with no number in common, and the leftover numbers then make up the big bin's total by
themselves.

## The formal statement and proof

**Review update, MI531 (2026-10-20): PROVED within project standards.**
Cloud CL468/0e3f4daa independently verified all-cut reduction, unique-fibre
exhaustion, spectrum joins and all three obstruction families. Its
committed g328_review.py reports3,539,232 admitted inputs to M60,56
failures exactly as classified, zero mismatches. Supporting computation
is reported, not rerun here; the hand read carries the verdict. Novelty
UNASSESSED. The candidate-status wording below is the original filing.

**PROOF-SKETCH: complete hand classification, NOT independently verified.**
MI507–508. Independent of G327 and of G326's joint partition proof; uses only
the elementary pair count and matching argument given here. No numerical
census or formal verification. The matching observation is elementary,
not claimed novel; novelty of the classification is UNASSESSED.

**Statement.** Put c>=3, M=c+4, 1<=q<=M-1 and P=[0,M] minus{q}.
Let integers u,v,w total T_M-q, where T_r=r(r+1)/2, and assume every
nonempty proper group of bins of sizes(2,2,c) has target >=T_(group size).
A partition exists EXCEPT in the following cases, with u,v interchangeable:

1. q1, {u,v}={4,6}, w=T_M-11, for every M>=7;
2. M7,q3, {u,v}={3,8}, w14;
3. M7,q3, {u,v}={4,10}, w11.

Every displayed exception satisfies ALL six protected cuts and has no
partition. All other admitted targets partition. Consequently the STRICT
version of all six protected cuts is sufficient at counts(2,2,c), c>=3:
each exception has at least one protected cut tight. This is not the
ordinary full-four-bin cut criterion, which MI506 shows may fail strictly.

**1. Two sum fibres, all choices.** For any finite set P of distinct real
values define E_z={{x,y} subset P: x!=y, x+y=z}. Each E_z is a matching,
since a token has only the partner z-x. If |E_u|,|E_v|>=2, disjoint
representatives exist. For u=v, choose two different edges. Otherwise,
assuming no representatives disjoint, choose two disjoint u-edges.
Every v-edge must meet BOTH and therefore lies on their four vertices,
one endpoint in each. Two disjoint v-edges cover all four vertices, so
summing their labels gives2v=2u, contradicting u!=v. This proves the claim.
Thus incompatibility of nonempty fibres requires a UNIQUE pair in at
least one fibre. If E_u={A}, incompatibility is exactly E_v(P minus A)
empty. No interval geometry has been used in this reduction.

**2. Protection and the unique-pair list.** Conservation makes the six
protected cuts equivalent to

    3<=u,v<=H=2M-1-q,
    10<=u+v<=K=4M-6-q.                         (2)

Before deletion, the number of distinct pairs of sum z in[0,M] is
floor((min(z,2M-z)+1)/2), for1<=z<=2M-1. Deleting q removes at most one
pair (none if q is its midpoint). For3<=z<=2M-3 the original count is at
least2, so a legal pair always survives. The only other possible z under
(2) is2M-2, which forces q1; its unique pair {M-2,M} survives. Therefore
both E_u,E_v are nonempty without a scalar feasibility premise.

A unique surviving pair can only come from an original fibre of size1
or2. The lower targets1,2 are excluded. For z3,4 the lists are literal:

| unique target u | q | unique pair A |
|---|---|---|
| 3 | 1 or2 | {0,3} |
| 3 | 3 | {1,2} |
| 4 | 1 or3 | {0,4} |
| 4 | 4 | {1,3} |

At the upper end u=2M-3 requires q<=2 by(2), whereas uniqueness would
require q>=M-3>=4, impossible. For u=2M-4, uniqueness needs q in
{M-4,M-3,M-1}, while(2) forces q<=3. The ONLY case is M7,q3,u10,
whose unique pair is{4,6}. Finally u=2M-2 forces q1 and gives{M-2,M}.
These exhaust all unique fibres at M>=7. We may swap u,v so that the
unique fibre is named u. The following cases check every possible v.

**3. Unique low target u3.** Here(2) requires7<=v<=H. Removing A gives
these ACTUAL pair spectra; fixed-cardinality sums of a full interval
fill their ordinary pair interval:

| q | P minus A | its pair spectrum |
|---|---|---|
| 1 | {2} union[4,M] | [6,M+2] union[9,2M-1] |
| 2 | {1} union[4,M] | [5,M+1] union[9,2M-1] |
| 3 | {0} union[4,M] | [4,M] union[9,2M-1] |

The first two unions join for M>=7 and cover every permitted v.
The last joins for M>=8. At M7 it misses only8 in the permitted
range7..H=10, giving exception2 and no other failure in this case.

**4. Unique low target u4.** Now(2) gives6<=v<=H. The actual spectra are

| q | P minus A | its pair spectrum |
|---|---|---|
| 1 | {2,3} union[5,M] | {5} union[7,M+3] union[11,2M-1] |
| 3 | {1,2} union[5,M] | {3} union[6,M+2] union[11,2M-1] |
| 4 | {0,2} union[5,M] | {2} union[5,M+2] union[11,2M-1] |

For q1 the intervals join for every M>=7 and the sole missing permitted
v is6: exception1. For q3 they join at M>=8; at M7 the permitted range
ends H10 and its sole missing value is10: exception3. For q4 the possible
M7 gap10 is OUTSIDE H=9; for M>=8 the intervals join. Hence no failure
comes from q4. None of these joins is inferred from a numerical sample.

**5. The upper unique cases are genuinely checked.** At M7,q3,u10,
removing {4,6} leaves {0,1,2,5,7}. Its complete pair spectrum is
{1,2,3,5,6,7,8,9,12}. Conditions(2) now give3<=v<=9, so only v4 is
missing; this is the already listed exception3 with u,v interchanged.

For u=2M-2,q1, (2) gives3<=v<=2M-5. After deleting {M-2,M}, choose:
- v3 or4: {0,v};
- 5<=v<=2M-7: a pair from the full interval[2,M-3], whose pair spectrum
  is exactly[5,2M-7];
- v=2M-6: {M-5,M-1};
- v=2M-5: {M-4,M-1}.
All avoid1,M-2,M and are distinct at M>=7. This covers EVERY allowed v,
so this legal high unique fibre creates no exception. It must not be
silently dropped from the exhaustion by an upper-margin estimate.

**6. Exhaustion, failure witnesses and controls.** If neither fibre is
unique, step1 supplies disjoint pairs. If one is unique, steps3–5 either
supply a disjoint pair or produce one of the three displayed exceptions.
The complement of two disjoint pairs automatically has size c and sum w.
For the exceptions: q1,u4 forces04 and every sum6 pair (06 or24) meets it;
M7,q3,u3 forces12 and sum8 has only17,26; M7,q3,u4 forces04 and sum10
has only46. Thus no partition exists. Substitution in(2) verifies admission:
case1 has u+v10 tight; case2 has the smaller pair target3 tight;
case3 has4+w15=T5 tight.
All remaining cuts follow directly from(2), establishing the strict-cut
corollary without a separate margin hypothesis or repair argument.

Literal nearby compatible controls, in pair/pair/remainder order:

    q1, all M>=7: 04 /25 / rest, targets4,7,T_M-12;
    M7,q3: 12 /45 /067, targets3,9,13;
    M7,q3: 04 /27 /156, targets4,9,12.

Two fibres of size EXACTLY2 each already suffice: M7,q1,targets(5,6,16)
partition as23 /06 /457. Equal-sum control M7,q3,targets(8,8,9) partitions
as17 /26 /045; it uses two DIFFERENT sum8 pairs. The abstract alternating
four-cycle with two edges of each colour is a countercontrol to arbitrary
matching sufficiency, not an additive-sum instance: unequal constant sums
on its two alternating matchings would imply2u=2v. No code was run.

**Scope.** This is a complete HAND CANDIDATE for one-hole THREE-bin
counts(2,2,c), not a new full-four-bin or five-bin theorem. It refines the
false universal two-pair extension rather than patching it. The first
obstruction recovers MI308/MI506's old mechanism; the all-choice exhaustion
and the two M7 exceptions are explicit. Neither G327 nor its review is a
premise. A carrying independent read is required before project PROVED status.


**Filing receipt (MI508).** proof_dupes --near W328 passes346 entries.
Nearest W327,G326,W322 read in full: they concern a full four-bin interval,
a one-hole3 problem with ONE pair bin, and a protected two-hole3 problem
with minimum sizes3, respectively. The present result has TWO pair bins
and an exact obstruction list, with no dependency on those candidates.
It neither restates nor upgrades their claims. No separate proof entry or
novelty claim is made for the elementary two-matching observation.
