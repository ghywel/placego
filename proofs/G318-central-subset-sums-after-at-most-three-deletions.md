# Central subset sums after at most three deletions

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT318. Central subset sums after at
most three deletions (second-read by Cloud;2026-10-18;MI369)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Deleting up to three numbers still leaves a guaranteed middle interval of fixed-size sums.

**What it says.** Start with the integers from zero through at least nine and delete up to three. Choose at least three numbers and leave at least three behind. Every total in an explicit central interval can still be made with the required number of choices.

**Why it matters.** This supplies one subset-sum ingredient for allocating numbers among several groups. It does not ensure that all groups can receive their requested totals simultaneously.

**An everyday picture.** Some numbered tickets are missing from a roll. Fix a few tickets at either end and leave three choices free in the middle. Sliding those three choices produces overlapping ranges of totals, with short repairs at their boundaries.

## The formal statement and proof

*Status:* PROVED in the stated scope;Cloud independently re-derived the carrying proof in CL441,commit7f710b4e.
*Where:* GPT-MATH-INSTINCT.md MI369,responding to Cloud CL440. Novelty UNASSESSED.

**Statement.** Let S=[0,M] minus H,|H|=h<=3,M>=9. Let r>=3 and
 t=|S|-r>=3. Write L(r)=r(r-1)/2 and U_r(M)=r*M-L(r).
Every integer in

 [L(r)+h*r, U_r(M)-h*r]

is the sum of r distinct members of S.

**1. Three-element windows.** For eta=0,1,2,3,an interval[0,2eta+3]
with at most eta deletions realizes every triple sum3eta+3 through3eta+6.
Reflection reduces the four sums to the first two. Here are hand covering
certificates;all triples below consist of distinct values.

- eta0:the four three-subsets of[0,3] have sums3,4,5,6.
- eta1:for6 use015,024,123;for7 use025,034,124. Each displayed triple
  family has empty total intersection,so one deletion cannot meet them all.
- eta2:for9 use027,036,045,126,135,234;for10 use037,046,127,136,145,235.
  In the first family the only degree3 vertices are0,2,3;in the second
  they are1,3. All other vertices have degree<=2. Two vertices neither
  of degree3 cannot meet all six triples. After deleting any degree3
  vertex,the three unhit triples have empty intersection,so a second
  deletion cannot finish the cover. Thus two deletions cannot meet all six.
- eta3,sum12:anchors1,3,4 each have FOUR disjoint partner pairs:
  for1,pairs29/38/47/56;for3,09/18/27/45;for4,08/17/26/35.
  If one anchor survives,three deletions cannot meet all its pairs.
  If all three anchors are deleted,057 survives and sums12.
  Sum13:anchor4 has pairs09/18/27/36. If4 survives this suffices.
  If4 is deleted,at most two deletions remain for the six triples
  067,058,139,157,238,256. Vertex5 has degree3 and every other vertex
  has degree<=2. A pair avoiding5 hits at most four triples;after deleting5,
  the unhit067,139,238 have empty intersection. Again no two-cover exists.

Triples such as015 mean the SET {0,1,5},not a number. The partner pairs
never contain their anchor. Translating these windows by b=0,...,D-(2eta+3)
produces intervals[3b+3eta+3,3b+3eta+6]. Consecutive intervals share an
endpoint. Therefore for D>=2eta+3,and at most eta holes in[0,D],

 [3+3eta, 3D-3-3eta] is contained in its triple spectrum.       (T)

In particular,the eta3 triple case works for EVERY M>=9 without a census.

**2. Arbitrary r:keep three choices free.** Exclude temporarily h=t=3.
Write S={z_0<...<z_(n-1)}. For every l+k=r-3,fix the l smallest and k
largest available values,and let their sum be F. The remaining middle pool
has t+3 values,smallest b,largest c,and eta<=h holes. Hence

 c-b=t+2+eta.

In the present cases t>=eta+1,so (T) applies to the middle interval.
Adding the fixed values gives a FULL r-sum interval

 I_l=[F+3b+3+3eta, F+3c-3-3eta]
    =[F+3c-3t-3, F+3b+3t+3].

It remains to join consecutive I_l;no convex hull replaces an absent sum.
For l>0,move from(l,k) to(l-1,k+1). Put a=z_(l-1),
 d=z_(n-k-2),p=b-a>=1,q=c-d>=1. The new fixed sum is F+c-a;
its middle endpoints are a,d. The gap from the OLD upper to NEW lower is

 g=lower(new)-upper(old)=-2t+2+4eta+p-3q.

The missing values in the gap a..b are disjoint from the eta middle holes,
so p<=h-eta+1. Therefore g<=-2t+3eta+h. In the opposite direction,

 lower(old)-upper(new)=2eta+2p-4t-2 <=2h-4t<0.

Thus adjacent intervals join as integer intervals whenever g<=1,even if
one interval is contained in the other. With h<=3,t>=3 and (h,t)!=(3,3),
the ONLY possible positive integer gaps are the following. They require
eta=h,p=q=1;hence b,c-1,c are all present.

- h2,t3:c=b+7,g=2. The missing value upper(old)+1 is supplied by
  the triple {b,c-1,c},whose sum is3b+13.
- h3,t5:c=b+10,g=2. The same triple has sum3b+19 and supplies the gap.
- h3,t4:c=b+9,g=4. The three missing middle sums are3b+16,3b+17,3b+18.
  The middle one is {b,c-1,c}. For16,use c plus a pair of translated
  values summing7:07/16/25/34. For18,use c plus a pair summing9:
  18/27/36/45. Each list has four disjoint pairs in[0,8],so three holes
  cannot meet all of them. The anchor c is present and in no pair.

For example,when h3,t4 and eta<=2,the bound on g is already<=1;
when eta3,all holes are internal,p=1,and q>=2 gives g<=1. The other
rows follow identically;larger t gives g<=0. This exhausts the join
exceptions by the displayed inequality,not by enumerating hole locations.
All interval joins and their extra points therefore form one interval.

For its lower endpoint,take l=r-3=s,k=0. If h0 holes lie below b,then
b=s+h0,F<=L(s)+h0*s,and eta<=h-h0. Hence

 lower(I_s)<=L(s)+h0*s+3s+3h+3
             =L(r)+h0*(r-3)+3h <= L(r)+h*r.

Reflecting the entire scalar construction x->M-x gives an upper endpoint
at least U_r(M)-h*r. This is reflection of a subset-sum statement,not an
assertion that the protected multi-bin hypothesis is reflection invariant.
The joined interval proves the assertion except for h=t=3.

**3. The complementary triple case h=t=3.** Here n=M-2,r=M-5>=4.
The proposed interval consists of the SINGLE value x=r*M/2,which is an
integer. Put w=sum(H). Since sum(S)-x=3M-w,it is enough to find a triple
in S of sum3M-w.

If12<=w<=3M-12,this follows from (T) with eta3. Otherwise reflection of
the entire scalar problem permits assuming w<=11. Let H*={M-q:q in H}.
If H and H* are disjoint,H* itself is the desired triple.

If H contains a complementary pair {a,M-a},write its third value b.
Then b is not central:otherwise w=3M/2>=15. Select another nondegenerate
complementary pair,avoiding the pair of a and the pair of b. There are
floor((M+1)/2)>=5 such pairs,and at most two are excluded. That pair
together with M-b avoids H and has sum2M-b=3M-w.

The only remaining overlap is a central value:M=2d,d>=5 and
H={d,a,b},with a+b=w-d<=11-d. We seek a triple B of sum w avoiding
H*={d,2d-a,2d-b};its reflection will give the desired triple in S.
Zero is not in H*. For9<=w<=11,there are at least four disjoint POSITIVE
pairs summing w,all inside[1,2d],since their largest value is<=10<=2d.
Three excluded values cannot meet all pairs,so add0 to a surviving pair.
For the remaining w=6,7,8,the positive pair counts are respectively2,3,3.
The two high forbidden values are both>=3d-w:for w6,7 they lie above
all pair values;for w8 at most one can equal7 and enter a pair.
Together with the central forbidden d,at most1,1,2 pairs are blocked.
Again add0 to a surviving pair. These are all possibilities,as
w=d+a+b>=d+1>=6. This completes the proof.

**Sharp controls and scope.** At M8,h3,r=t3,the pools
{0,2,3,5,6,8} and {0,1,2,6,7,8} both omit the required sum12.
For the first,starting0 needs a pair12 which is absent;starting2 needs
5+5 or3+7;starting>=3 already gives>=14. For the second,a triple with
at most one of6,7,8 sums<=11,and one with at least two sums>=13.
These explain why the hypothesis M>=9 cannot simply be dropped.
MI368's near-full r9 example explains the complementary size>=3 condition.

The lemma's symmetric upper endpoint is NOT automatically the full upper
range admitted by H(h). That upper range is sum(S)-L(t)-h*t;its difference
from U_r(M)-h*r is L(h)+h*r-sum(H),which can be positive. Example:P_0 on
[0,12] minus1 admits targets(6,19,20,32);all14 cuts hold,but the target32
lies above this lemma's r3 upper endpoint30. The scalar target32 is feasible
({9,11,12});the example only prevents treating the lemma as a complete
joint-partition induction. No five-bin,P_0,E28 or L8 status changes.


**Filing comparison.** Native proof_dupes --near W318:336 entries,no repeats.
Nearest G315,G46,G316 read in full. The first and third are simultaneous
partition criteria on different pools;G46 concerns Collatz ceilings.
This candidate is a central scalar-spectrum statement,not a restatement
or a new multi-bin theorem. See MI369 for primary-literature read scope.


**Independent review adopted (B212).** Cloud CL441/7f710b4e re-derived
all three parts,including interval joins and the complementary triple case.
Cloud also reports25,004 exact (pool,r) checks for M9..16;those are
supporting independent computations,not the infinite proof or a GPT rerun.
Moved out of the waiting room on this carrying read. The full protected
upper range and simultaneous multi-bin completion remain outside this
lemma;MI371 and later applications are not promoted by this receipt.


**Promotion filing check.** The initial relocation used an unrecognized
section/heading combination;the neighbour query failed,so that check
was not a pass. Filing under E2 with the standard G.GPT318 heading
restored all340 entries;duplicate and nearest-entry checks pass.
Nearest G46,G82,G313 were read in full:Collatz ceilings,coin smoothing,
and folded-gap matching respectively,not this scalar deletion theorem.
No generated proof page was edited.
