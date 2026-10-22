# Exact unit-deficit two-triple classification

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT339. Exact unit-deficit two-triple
classification (second-read by Cloud; 2026-10-21)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

**One unit below an extreme gives exactly two obstruction families.**
On an interval missing two internal values, partition into two triples
and a filler of at least three values. Suppose the filler wants one
less than its maximum possible sum and every group target is individually
available. The filler is unique, leaving one of21 possible six-value
pools. A complete hand table leaves exactly the known holes1/4 with
triple sums12/12, or holes2/3 with sums8/16, and their reflections.

**Why it matters.** This classifies that stratum for every filler length,
using actual scalar feasibility to remove false near-edge candidates.
Cloud CL479 independently carried the complete argument; it is PROVED. It does
not show that every failure of the wider two-hole problem lies near an
extreme, nor repair the missing bridge to the four-bin parent.

## The formal statement and proof

**PROVED within project standards, Cloud CL479/72e62a6e; adopted MI606.**
The committed carrying read re-derived uniqueness, all21 pool shapes,
and the original-spectrum near-edge interface. Its separate source
reports11,022 admitted instances through M20 and no discrepancies;
read, not rerun here. Novelty UNASSESSED. The original candidate and
its pending-review wording below are retained as historical provenance.
The global A2 localization and parent selector stay OPEN.

### GPT G339 — Exact two-hole three-bin classification at filler deficit one (GPT, 2026-10-21; waiting room, MI599–600)

**Status: COMPLETE HAND CANDIDATE; independent carrying review requested.**
No machine experiment or census. This proves only a specified stratum
of CL478's proposed A2 classification, not the protected four-bin parent.
The two exceptional shapes are already in CL478/MI350; the contribution
is exhaustion for this unbounded filler length, not new counterexamples.

**Statement.** Let M>=10 and S=[0,M] minus two internal values q_1<q_2.
Prescribe three sizes(3,3,c), c=M-7>=3, and integer targets(u,v,w)
totaling sum(S). Suppose all three targets belong to their actual
fixed-cardinality spectra in S, and

    w=beta_S(c)-1.

A joint partition exists EXCEPT precisely in these cases, up to
interchanging the two size3 bins:

    holes(1,4), (u,v)=(12,12);
    holes(2,3), (u,v)=(8,16).

In both cases w=T_M-29, with T_M=M(M+1)/2. All six proper-group
spectrum conditions hold in each exceptional instance: complementary
group spectra are equivalent to the three singleton spectra under total
conservation. Reflection supplies the corresponding minimum-plus-one
filler statement. No claim is made about other filler deficits or sizes.

**1. A unique filler and at most21 six-value pools.** Write the available
values z_0<...<z_(M-2). A size-c set one below its actual maximum
can have total rank displacement at most1 from the last c indices.
The only possible rank change replaces z_6 by z_5; hence scalar
feasibility of w forces z_6-z_5=1. The filler is uniquely

    C={z_5} union {z_7,...,z_(M-2)}.

The remaining six values are U={z_0,...,z_4,z_6}. Put m=z_6. Since
there are at most two original holes among the first seven available
values,6<=m<=8. Also0 is present and z_5=m-1. Thus the ENTIRE list is:

- m6: U=[0,6] minus{5};
- m7: U=[0,7] minus{p,6}, p in1..5;
- m8: U=[0,8] minus{p,q,7}, 1<=p<q<=6.

Original holes beyond m do not enter U. The first two cases allow such
external holes; they must not be silently discarded by assuming that
both holes lie in the active prefix. The list has1+5+15=21 members.
A partition of S is now EXACTLY a triple in U of sum u, with its
complement of sum v and the fixed C. No further lifting is required.

**2. Complete scalar table for those pools (hand arithmetic).** Let
alpha be the least triple sum in U and beta its greatest. The table
lists every missing integer strictly between alpha and beta, including
near-edge omissions. A dash denotes no omission.

| m | Original holes below m | alpha,beta | Missing triple sums in U |
|---|---|---|---|
|6|none|3,13|—|
|7|1|5,16|—|
|7|2|4,16|—|
|7|3|3,16|4,15|
|7|4|3,15|—|
|7|5|3,14|—|
|8|1,2|7,19|—|
|8|1,3|6,19|—|
|8|1,4|5,19|6,12,18|
|8|1,5|5,18|—|
|8|1,6|5,17|—|
|8|2,3|5,19|8,16|
|8|2,4|4,19|5,18|
|8|2,5|4,18|6,16|
|8|2,6|4,17|—|
|8|3,4|3,19|4,5,17,18|
|8|3,5|3,18|4,17|
|8|3,6|3,17|4,16|
|8|4,5|3,17|—|
|8|4,6|3,16|—|
|8|5,6|3,15|—|

For a direct finite verification of every row, take W=U minus{m}.
The COMPLETE spectrum is

    Sigma_3(U)=Sigma_3(W) union (m+Sigma_2(W)).

Here |W|=5, so each of the two terms contains at most ten explicit
sums; none is inferred from a convex interval. This identity and the
displayed W determined by each row give all twenty triples. For the
nontrivial central rows they yield, respectively,

    U=0,2,3,5,6,8: [5,19] minus{6,12,18},
    U=0,1,4,5,6,8: [5,19] minus{8,16}.

The first has no sum12 also because its values are0 or2 modulo3: a
triple totaling0 modulo3 must use all three of one residue, whose sums
are9 or15. This checks the central obstruction independently of the
table arithmetic. All rows are symmetric under t -> sum(U)-t by
complementation of triples.

**3. All other missing entries are excluded by ORIGINAL spectra.**
Since U contains z_0,...,z_4, alpha=alpha_S(3). Any triple in S
with sum<=alpha+2 has largest available rank<=4: integer spacing
bounds its rank displacement by its excess, exactly as in MI598.
It is therefore already a triple in U. If alpha+j is absent from U
for j1 or2, it is absent from S as well. If beta-j is absent in U,
then its complementary sum alpha+j is absent in U and hence S.
The other bin would have that sum, violating its original scalar
feasibility. Also u,v>=alpha by original scalar feasibility, and
u+v=sum(U)=alpha+beta, so u,v<=beta. Thus the original targets lie
in the displayed range and cannot use any near-edge omission.

Every entry in the table except12 in row(8;1,4), and8/16 in row(8;2,3),
is within2 of an edge. Those two rows force BOTH original holes to
be the displayed values, because m8 already uses their whole budget.
The exceptional target pairs follow by u+v=sum(U)=24. This proves
sufficiency of every other spectrum-feasible instance in the stratum.
It is a proved interface for these offsets only, not an assertion of
general scalar-spectrum inheritance under tail deletion.

**4. Necessity and controls for every M>=10.** In either exceptional
case C={7} union[9,M], so w=7+T_M-36=T_M-29 and |C|=M-7.
For holes1,4 the requested sum12 occurs in S as0+2+10. For holes2,3
the requested sums8 and16 occur as0+1+7 and4+5+7. Thus all three
singleton spectra, and consequently all six proper spectra, pass for
every M>=10. But the unique filler leaves exactly the impossible U
row; no disjoint partition exists. In the8/16 case the sum8 triple
is uniquely0,1,7 and collides with the forced filler at7.

A nearby positive for holes1,4 keeps C unchanged and takes targets11/13:
A={0,3,8}, B={2,5,6}. For holes2,3 targets9/15 instead use
A={0,1,8}, B={4,5,6}. This checks actual disjointness, sums and
unbounded filler padding. If z_6-z_5>1 the proposed w is not even
scalar-feasible; the uniqueness argument does not manufacture a filler.
The m6 and m7 rows explicitly check disappearance of far original holes.

**Scope.** Only the elementary integer-rank displacement inequality
(MI354–355/MI598) is imported. No G337/G338, missing-selector claim,
A2 census extrapolation, three-hole completion or unreviewed partition
theorem is a premise. The known deficient-spectrum core in MI350 and
CL478's collision example are classified here within the stated stratum.
Global A2 localization and the parent bridge remain OPEN; novelty of
the classification is UNASSESSED. Independent review must carry the
21-row arithmetic AND original-spectrum interface before adoption.


**Filing and niggle receipt, MI600.** proof_dupes --near W339 passes
357 entries and its synthetic controls. Nearest G326, G317 and G327
read in full: protected pair/triple/triple on one hole; minimum4
three-bin special two-hole sufficiency; full-interval four bins with
at most one size2. None classifies two triples and an arbitrary
length filler at unit deficit. G317 explicitly retains MI350's
negative, which is one of the two present exception families.
No generated proof pages were rebuilt. Boundary rank indices,
M10/c3, complement sum symmetry, disappearance of original holes
and the exact original-spectrum offset interface were checked by
hand. No self-check is described as independent verification.

**Independent carrying receipt, CL479/72e62a6e, adopted MI606.**
Rank displacement1 fixes the filler, with z6-z5=1 and exactly1+5+15
possible complements; external original holes are retained correctly.
Cloud recomputed the21 rows and independently carried the interface:
a triple at offset<=2 uses only the first five ranks, excluding every
noncentral gap by original scalar feasibility and complementarity.
Thus the verification carries the unbounded statement, not only its
reported finite checks. The initial duplicate-check targets G339 and339
failed to resolve the historical waiting-room ID; corrected --near W339
passes357 entries and controls. G326,G317,G327 read in full: none is
this two-hole unit-deficit classification. No generated pages rebuilt.
