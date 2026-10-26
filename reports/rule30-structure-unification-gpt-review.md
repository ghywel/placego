# GPT carrying review: runs, staircase rain, and the capped right-edge ruler

GC1935 / MI854, 26 October 2026 (UTC). Owner-requested manual review.
Sources: L999 at dee6395a08c9ad929a35a675ea55c1bc23cdd2d2;
L1000 at 7ff066881a3a0323eea732103add4fd614175c35;
L1001 at 04a5a3d1c4c702f98d05428f48b4835874332e0a.
Read the three complete reports, their three checker sources, and both exploratory
edge scripts. Re-read Proposition 23 in PROOFS.md entry36, RULE30-PRIZE.md 8.73,
GC808/810 and the CPY primary paper's relevant theorems/proofs. No new simulation,
rerun, schedule, M5 job or submission. Execution counts/timings remain Local's
reported outcomes; this is an independent hand/source review.

## Verdict

**Real progress.** L999's companion, persistent rain front and hanging/rhythm
mechanisms carry under the stated sufficient window. L1000's finite-run R,
precise one-step P, bridge bound and finite-seed E carry. L1001's theorem for
FINITE matching depth carries, including the permanent cap and timing. The
unqualified infinite-depth ordinary-time-shift sentence does not follow from
the supplied proof. Preserve the accepted result and qualify that sentence;
this is not a refutation of the finite-depth theorem.

GC1934's original staircase argument is now independently carried by L999;
its source-described independent crop recomputation is adopted as Local's
execution, not a GPT rerun. No discovery or novelty priority is asserted.

## 1. L999: the same object viewed along rows and columns

The left companion follows from 1 = left XOR 1, hence left=0. Applied to the
successor1-bar [s,b+2], it gives precisely the same zero interval [s,b+1] as
GC1934. The two explanations really meet.

A maximal alternating stretch of length at least3 has unchanged interior and
a flipped first cell. Thus the surviving patch of the SAME fixed alternating
background starts at a+1. This persists while enough interior remains; it is
not a rule for arbitrary singleton agreement patches.

If the front is1 and the run ending there is [p,a], length>=2, the next row is
1 at p, zeros on [p+1,a+1], and1 at a+2: the hanging lemma carries. With the
initial stretch extending through a+5, a width>=3 gives a zero at a at the
intermediate stage, leaving exactly the two-cell run that hangs the next
width2. Width2 instead turns wholly1, giving the next run length>=3. Both
rhythm directions carry with enough remaining rain. The source S5 directly
asserts only the >=3-to-2 direction; the reverse direction here has a hand
read, not a claimed dedicated S5 assertion.

The marked clock breaks after its support ends as reported. Generally loss
of that support ends our guarantee; it does not force every possible clock
to break at that exact time. Do not generalize the crop's timing without the
actual next-neighbour values.

## 2. L1000: R, P and the bridge

R's six cell cases are correct for finite maximal runs bounded by the opposite
colour. Add the obvious unbounded-run convention before saying every row:
a constant row maps to all0; a semi-infinite0 run changes only its finite end;
a semi-infinite1 run has a surviving head only if it has a finite left end.
On constant rings the counting law counts boundaries/heads, hence zero runs,
as the checker implements. A whole uniform ring is not one ordinary bounded run.

P's exact one-step clauses carry. Its prose "the left edge of any agreement
moves right ... always" is too broad. For x with ones at -1,+1 and zeros
elsewhere, compared with all0, the singleton agreement at0 stays0 next step.
Both mismatching neighbours are still1, so that singleton boundary has not
advanced. P itself correctly includes this exception. For a length>=2 interval,
its old leftmost cell is lost; follow the surviving interior only while it
exists. The new maximal agreement region can extend to the right; P describes
agreement at the OLD boundary, not its complete future maximal extent.

Related prose repairs: an odd white triangle reaches a singleton which can
persist or hang a child; its zero lineage does not necessarily die after
ceil(n/2) rows. The fixed alternating background contains perpetual singleton
zeros. The formula describes the triangular shrinking core, not every later
connected white cell. Also a white pair joins the right black head, but joins
the left head only if the left black run was a singleton: 11001 maps in those
five cells to10111, not a single merged black block.

**Bridge bound supplied explicitly.** Pair each bounded black run B_m with
its following white run W_n. The only unit whose ENTIRE image is1 is
B_1 W_2 = 100, with image111. Every other unit contains a zero. A maximal output
black run crossing r consecutive whole bridge units therefore consists of:
- a suffix of the preceding nonbridge unit, length0,1 or2;
- r copies of111;
- a prefix of the following nonbridge unit, length1 or2.
Thus 3r+1 <= L <= 3r+4. Black runs wholly inside a nonbridge unit have length1
or2 and satisfy the r=0 case. A ring made exclusively of100 units maps to the
uniform1 ring and has no bounded output run: exclude it as the source does.
This gives the missing short proof of the table's bridge assertion.

The counting laws follow by enumerating these same unit images, using the
constant-ring convention. E items1-3 follow at the finite seed's zero exterior.
For E4, read the white run just left of an isolated edge1: widths1,>=3,2 give
next edge black-run lengths2,3,>=4 respectively. Their next emissions have
widths1,2,>=3. The four initial suffix cases in E5 are correct, including the
single-cell seed with two zero exterior bits. E is independently carried.

## 3. L1001: finite-depth theorem carried

Let T(R)=R XOR(2R OR4R), let C_k be the orbit of1 modulo2^k, and let p_k=|C_k|.
The triangular map modulo2^k is a permutation: successively recover input bit j
from output bit j and the already recovered lower bits. Its orbit over C_k at
the next level has period p_k or2p_k, since after p_k steps only one remaining
binary bit can be permuted. Therefore if R first leaves the single-seed cycles
at level k+1, that level cannot double. At any phase s matching mod2^k, R is the
other lift modulo2^(k+1). First disagreement at bit k is preserved by every
update. This verifies the carrying lifting and permanence steps.

**A direct gap proof avoids any diagonal-index ambiguity.** At positive time u,
let j be the first set bit of T^u(1) above bit0. Then

    p_j divides u, but p_(j+1) does not divide u.

Indeed the first condition says precisely that the lower j bits have returned
to the residue1; the next prefix has not. Hence p_(j+1)=2p_j: level j+1 doubles.
The zero-run width is j-1, i.e. (doubling level)-2. Conversely a doubling level
l gives that first set bit at j=l-1 at time p_(l-1). Level2 gives width0 (no
emission); the positive emission widths correspond to doubling levels l>=4.
Unbounded prefix periods follow because a bounded common period would return
the whole finite code1, whereas T increases a positive finite code's degree by2.

This is also a safe translation of Proposition23: use PREFIX periods p_k,
which are lcm of the first k diagonal periods. The first nondividing prefix
occurs at the same first offending diagonal, with prefix index j+1. No need
to assume every individual diagonal period equals its entire prefix period.

At finite depth k, bit1 agrees forever, so emissions have identical timing to
phase s of the single seed. Smaller widths (<k-1) are decided below bit k and
agree. Width k-1 is absent from the reference ruler, because level k+1 does not
double. At any larger reference width, the differing bit k is1 in R, ending
its white run at exactly k-1. Thus at every emission

    width_R(t) = min(width_single(t+s), k-1).

This is a general hand proof, independent of the reported finite census.
The timing and width sequence depend only on the first k+1 bits, so they are
purely periodic with period dividing p_k; no transient allowance is needed.
Every non-doubling level>=3 supplies a finite odd twin lift, realizing its cap.

**Concrete hand example.** Take the finite seed100001, edge code33. The cycle
of1 mod64 is 1,7,25,47,17,55,9,63 (then1), and its mod32 projection has8 points.
Code33 agrees with1 mod32 but is absent mod64: k=5, phase0, cap4. Its successive
emitted widths are 2,3,2,4,2,3,2,4,... rather than the uncapped
2,3,2,5,2,3,2,6,... . This is capping selected widths throughout time, not a
pattern that first behaves normally and then stops after a particular date.

## 4. The infinite-depth clause needs qualification

From membership in every C_k we get compatible residues s_k mod p_k, not yet
one ordinary nonnegative integer s satisfying all of them. The proof cannot
simply reuse the finite-k choice of s0 when k=infinity.

A correct general replacement is an inverse-limit phase alpha=(s_k): every
fixed finite edge window agrees, for all future times, with the single-seed
history at its corresponding phase s_k. This is the orbit-closure/odometer
meaning of phase. For a seed explicitly equal to T^tau(1), alpha is the ordinary
integer tau and the claimed single time shift holds. There are already many
non-single-cell examples, such as111=T(1), with no finite cap.

To keep the stronger ordinary-time-shift wording for EVERY finite seed of
infinite depth, prove the extra assertion:

    {finite odd codes in closure of orbit(1)} = {T^tau(1): tau>=0}.

That assertion is neither established nor refuted by this review. Alternatively
state the universal result using the compatible phase definition. This repairs
the statement without discarding the finite-depth theorem. "The same edge"
must in any event mean the emission timing/width sequence, not equality of the
entire spatial edge region: higher bits remain unconstrained for finite k.

## 5. What the sources and numerical guards actually establish

CPY, *Prevalence of odometers in cellular automata*, arXiv:math/0511030,
https://arxiv.org/pdf/math/0511030 : Theorems1 and4/proofs build compatible finite
phases and an adding-machine orbit closure. They do not state this particular
Rule30 triangle-width capping formula or identify every finite point in the
single seed's closure with an ordinary orbit point. This targeted source check
supports the ingredients, not a literature-wide novelty claim.

The checker sources were read; no run repeated. Local's headers report all
checks passing. Qualifications for any numerical summary:
- U's56 cases reaching KMAX40 are DEPTH>=40, not certified infinite depth or
  exactly depth40. In those cases the code uses an artificial cap39; agreement
  in the observed window does not certify that cap forever.
  There is a useful hand accounting check: T^tau(1) has width2tau+1. For
  tau=0..6 its presentations in windows of width<=14 number
  14+12+10+8+6+4+2=56. Each certainly reaches depth40. Thus, conditional on
  Local's reported total56, ALL tested deep cases are already accounted for
  by ordinary descendants of1. This supports the observed special cases but
  leaves the all-width orbit-closure assertion open.
- U3 rejects observed widths at non-doubling levels<=40. It does not alone
  prove all widths occur or exhaust the infinite gap list. The hand proof does.
- The16,383 inputs count finite words/presentations; padding zeros on the left
  can repeat the same normalized edge code. Do not call them distinct
  translation classes. The complete declared finite-word loop is still useful.
- edge_levels_look.py does not separately assert prediction Q2's eventual
  periodicity; its printed shape classification is not that assertion.
- Final guard source has no stage-wide CPU/memory/wall supervisor or retained
  raw receipts cited in these notes. I accept the hand proofs independently;
  I do not certify resource enforcement, the reported timings or failures as
  inspected raw execution evidence. Preserve drafts/failures if promoting
  execution claims. No rerun is needed to settle this review.

## 6. Review disposition and next concrete step

Accept L999's scoped new lemmas, L1000 R/P/bridge/E and L1001 finite-depth U.
Adopt L999's independent GC1934 read. Amend the overbroad patch/lifetime prose,
whole-edge wording and infinite-depth phase clause. Return this exact report
to Local with the remaining ordinary-phase obligation explicit. The useful
next hand question is already identified; no new census or automatic schedule
restart is requested. Gut verdict: warm. The visual analogies led to a common
mechanism and a real classification of the finite-depth emitted-width sequence.
