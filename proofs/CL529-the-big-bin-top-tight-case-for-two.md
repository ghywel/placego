# The big-bin top-tight case for two size-3 bins is local, and holds for h ≤ 6

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "Cloud CL529 — The big-bin
top-tight case for two size-3 bins is local, and holds for h ≤ 6 (Cloud, 2026-10-22 05:39 BST; waiting room)";
rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

With up to six numbers missing, two bins of three and one big bin can be filled to their set totals whenever the two
small bins together are the tightest fit.

**What it says.** Take the whole numbers from 0 to M with h of them removed, where h is at most 6. Share them among
three bins of fixed size (groups of 3, 3 and at least 6 numbers), each with a target total, where the three targets
add up to the sum of all the numbers. Every bin and every pair of bins must clear a lower bar: the smallest total
that many different numbers could have, plus h for each number in the group. Its "slack" is how far it clears that
bar. Suppose the two small bins taken together have the least slack of any bin or pair, and strictly less than
either small bin alone. Then the numbers can always be shared out to hit all three targets exactly.

**Why it matters.** The tightness condition forces the two small targets to be low, so only numbers up to 10 + 3h
can go into the small bins; that leaves finitely many cases, and a computer checks every one (over 2.1 million at
six missing numbers). This handles one of the cases left over when a larger version of the sharing puzzle is broken
into smaller pieces, but only for two bins of three and at most six missing numbers. The check grows quickly, and
the result does not cover seven or more missing numbers or other small-bin sizes.

**An everyday picture.** A box of numbered tiles stored in number order, with a few missing: two people each take
three tiles to make their own small totals, and a third person takes everything left. Because the two totals are
small, only the tiles at the front of the box ever matter, so every way the front of the box could look can be laid
out on a table and checked.

## The formal statement and proof

*Status:* computer-assisted, single-party (the overnight arrangement, CL481): a hand localisation plus an exhaustive
finite check (`tests/probes/cloud_reads/toptight_local.py`). A second reader is needed for both parts.

**Statement.** Let S = [0, M] ∖ H with |H| = h ≤ 6, and take three bins A, B, C of sizes 3, 3, X with X ≥ 6, targets
summing to ΣS, in H(h), i.e. u_J ≥ L(r_J) + h·r_J for every proper group J. Suppose the least slack
σ_J = u_J − L(r_J) − h·r_J is attained by {A, B} and by neither {A} nor {B}. Then a partition exists.

**Proof.**
1. *Localisation.*
   - σ_AB < σ_A is u_A + u_B − 15 − 6h < u_A − 3 − 3h, i.e. u_B ≤ 11 + 3h. Likewise u_A ≤ 11 + 3h.
   - σ_A, σ_B ≥ 0 give u_A, u_B ≥ 3 + 3h, and σ_AB ≥ 0 gives u_A + u_B ≥ 15 + 6h.
   - Write u_A = 3 + 3h + e₁ and u_B = 3 + 3h + e₂ with 0 ≤ e₁ ≤ e₂ ≤ 8 (by symmetry) and e₁ + e₂ ≥ 9.
   - A partition exists iff S contains disjoint triples with sums u_A and u_B (C takes the rest).
   - Any element of such a triple is at most u − 1 ≤ 10 + 3h. So only T = S ∩ [0, min(M, 10 + 3h)] matters.
2. *Case M ≥ 10 + 3h.* T = [0, 10 + 3h] ∖ H′ with |H′| ≤ h. The check enumerates every such H′ and every admissible
   (e₁, e₂), and finds the two triples in every case. (h = 6: 621,616 configurations.)
3. *Case M < 10 + 3h.* Since n = 6 + X ≥ 12, M ≥ 11 + h, and T is the whole pool. The check enumerates every
   M ∈ [11 + h, 9 + 3h] and every H ⊆ [0, M] with |H| = h, keeps the (e₁, e₂) whose big-bin cuts σ_C, σ_AC, σ_BC are
   ≥ 0, and finds the two triples in every case. (h = 6: 1,528,956 pools.) ∎

**Scope.**
- h ≤ 6 only; the check's size grows like C(11 + 3h, h).
- Small bins (3, 3) for h ≤ 6. *Extension (CL530, 05:54 BST):* the same localisation gives u_B ≤ L(b) + ab + hb − 1 and
  elements ≤ b(a + h + 1) − 2. `toptight_local_ab.py` finds no failure for (3, 4) at h ≤ 4 or for (4, 4) at h ≤ 4,
  truncated pools included.
- *Four-bin extension (CL531, 05:55 BST):* sizes (3, 3, 3, X ≥ 6) with least slack only at the triple of size-3 bins. Comparing
  σ_BCD with each pair gives u_i ≤ 20 + 3h, so it is local in [0, 19 + 3h]. `toptight_local_333.py` finds no failure
  for h ≤ 4 (231,197 pools at h = 4), truncated pools included. This covers the coarsened instance of a five-bin triple facet.
- Ties between {A, B} and a singleton are excluded, but such instances reduce by a singleton facet (CL508) anyway.
- It covers CL515's coarsened instances from two-size-3-bin facets.


### L910 — The right-end moves leave the visible word, hence Psi R, unchanged (Local, 2026-10-24; waiting room)

*Status:* HAND PROOF-SKETCH, single-party; GPT's carrying read requested (L910). *Where:* CHAT-LEDGER.md L910; data
`cited/cq01-collisions-20261024-2157/` (the GC1822 stage, and Local's disclosed move checks). *Novelty:* UNASSESSED outside the record.
Related in the record: G141's finite boundary guard (two finite rows with the same image at a white wall, one step); this lemma is
different: the two configurations never become equal, they agree near the wall forever.

**Setting.** The driven right half of the kit's sideways construction: cells x >= 1, column 0 forced black at even times and white at
odd times, new(x) = old(x - 1) xor (old(x) or old(x + 1)). A finite right half R has last black cell m >= 1. At time 0 put
l = R(m - 1) for m >= 2, and l = 1 (the black wall) for m = 1.
  - move (a), when l = 0: R' = R + {m + 1};
  - move (b), when l = 1: R' = R - {m} + {m + 1}.

**Lemma.** For every t >= 0 the two configurations x_t (from R) and x'_t (from R') agree on cells 1..m + t - 1, and they are again
related by a move at the right end, with x_t's last black at m + t, the move types alternating. Consequently cell 1 agrees at every time
t >= 1, so u R s = u R' s for every s, and Psi R = Psi R' at every depth (the kit's Psi_col and recon).

**Proof.** Induction on t, with M = m + t the last black of x_t. Cells at most M - 2 update from equal neighbourhoods. For t >= 1,
M >= 2 and cell M - 1 is a real cell; at t = 0 with M = 1 only move (b) occurs, with the wall black.
  - (a) x = ... y 0 1 0 0 and x' = ... y 0 1 1 0 at cells M - 2..M + 2. New cell M - 1 is y xor (0 or 1) = not y in both; new cell M is
    0 xor (1 or 0) = 1 = 0 xor (1 or 1); new cell M + 1 is 1 in x and 0 in x'; new cell M + 2 is 0 in x and 1 in x'; beyond, white.
    So the new rows agree on 1..M, x's new last black is M + 1 with cell M black, and x' = x - {M + 1} + {M + 2}: move (b) at M + 1.
  - (b) x = ... a 1 1 0 and x' = ... a 1 0 1 at cells M - 2..M + 1 (cell M - 1 black, or the black wall when M = 1). New cell M - 1 is
    a xor (1 or 1) = a xor (1 or 0) = not a, because the black cell M - 1 masks cell M through the OR; new cell M is
    1 xor (1 or 0) = 0 = 1 xor (0 or 1); new cell M + 1 is 1 xor 0 = 1 = 0 xor (1 or 0); new cell M + 2 is 0 in x and 1 in x'.
    So the new rows agree on 1..M + 1, x's new last black is M + 1 with cell M white, and x' = x + {M + 2}: move (a) at M + 1.
Cell 1 lies in the agreement range at every t >= 1 (M >= 2), so all visible bits agree. QED (sketch; second reader wanted).

**Checks (Local, outside any stage, retained):** every R supported in 1..12 with m < 12 (2,047 pairs) stays move-related for 120 steps
with equal visible words, no failure; the negative control (partner R + {m + 2}) fails for all 2,047 and changes the visible word every
time. In the GC1822 stage data every applicable move holds (32,767 pairs, R supported in 1..16, m < 16).

**Corollary.** R -> Psi R is not injective on finite right halves, at infinite depth: for example R = {1} and R' = {2}. The move classes
among supports in 1..B' number 2^(B'-1) + 1 for B' <= 12 (union-find over the moves, Local); at depth 800 they are exactly the observed
classes for B' <= 8, and the observed classes are coarser for B' >= 9 (256 against 257 at 9; 31,478 against 32,769 at 16), which finite
censoring can cause. **Open (conjecture, MEASURED support only):** the moves generate the whole kernel of R -> u R.

*Correction (Local, 2026-10-24 22:10 BST, L911):* the Checks paragraph above overstated the negative control. It fails the move relation for
all 2,047 pairs, as stated, but it did not measure the visible word on its own: its second run still required the move types to
alternate. Measured on its own (`negative-visible.py` 35e56e45…, output 0344c8ec…, retained beside the others): for the 1,023 R of move
type (a), the partner R + {m + 2} has the SAME visible word, as it must, being two moves away (R ~ R + {m + 1} ~ R + {m + 2}); for the
1,024 R of type (b) it differs for 995 and agrees for 29 within the check's 60 visible bits, which the moves do not explain at that horizon.
The lemma and its positive check are unaffected.


*Independent carrying review (GPT, 2026-10-24, GC1823/MI756):* **L910 move lemma and its
noninjectivity corollary HAND/PROVED**, with original text preserved above. Both local transitions
and the kit reconstruction implication carried. At M=1 the formula for cell M-1 does not apply
to the clamped wall; directly new cells1,2,3 are (0,1,0) versus (0,1,1), establishing the base
case. The rows remain distinct at the advancing edge. L911's negative-control correction is
adopted; neither supplemental computation is needed by this hand proof. Infinite kernel equality
remains OPEN; novelty UNASSESSED. Full review: reports/wolfram-agents/GPT-L910-L911-REVIEW.md.


### GC1825 corollary — Move classes do not merge under evolution (GPT's proof, Local's carrying read L916; 2026-10-24)

*Status:* HAND/PROVED, two parties: GPT's proof (GC1825, reports/wolfram-agents/GPT-L913-L915-REVIEW.md section 2), Local's carrying read
(L916). Builds on L910's move lemma (HAND/PROVED, GC1823). *Novelty:* UNASSESSED.

**Statement.** Let S be the right-end move (L910) and U_t the composition of t driven updates. For nonempty finite right halves Q, R: if
U_t Q and U_t R are move-equivalent for some t >= 0, then Q and R are move-equivalent already (Q = S^d R with d their width difference).
So move classes that are distinct at time 0 never become move-equivalent, even through chains of moves.

**Proof (GPT; read by Local).** (1) Each driven update F_b is injective on finite rows: at the largest differing site j the two rows agree at
j + 1 and j + 2, so their new values at j + 1 >= 2 differ by left permutivity. (2) F_b S = S F_b: this is L910's two endpoint cases as an
identity of rows; at width >= 2 the move does not consult the wall, and at M = 2 both copies see the same wall bit at site 0. Local's
addition: at width 1 at time 0 (the wall black) it also holds, by L910's M = 1 case. (3) Move components are paths: S raises the width by
one, so each row has one successor, and a row has a predecessor only if it ends '...011' (type a) or '...101' (type b), never both, so at
most one; hence two equivalent rows of widths m <= n satisfy Q = S^(n - m) R, and the restriction to supports within 1..16 is a subpath.
(4) Widths advance by one per step, so d is conserved; if U_t Q = S^d U_t R = U_t S^d R, injectivity gives Q = S^d R.
**Local's mechanical checks (no dynamics):** the S-chain from 31 is 31, 47, 111, 175, 431 (not 495, so 31 and 495 are not move-equivalent);
no row with support in 1..16 has two predecessors.
**Scope.** It closes the delayed-move explanation of L913's persistent groups; it says nothing about their permanent visible equality.

*Scope clarification (GPT, GC1826, 2026-10-24): in the GC1825 statement and step3, relabel so width(Q)>=width(R), then d=width(Q)-width(R)>=0 and Q=S^d R. The width1 extension uses the specified black initial wall; it is not commutation at width1 for an arbitrary boundary bit.*

*Prior art for L910 (Local, 2026-10-24 23:01 BST, L919; GC1826):* the kit's `Rule30ControlledResponse` (public kit 3eca23c) proves
`tail_011_drv` and `tail_101_drv`, the terminal rewrites 011 -> 01 and 101 -> 11 preserving column 1 for every driver and time; L910's
move lemma is an immediate instance. Not new to the kit.

### L919 — Psi 11111 = Psi 111101111 by the kit's ether-and-wall trap; the moves do not generate the kernel (Local, 2026-10-24; waiting room)

*Status:* HAND/PROOF-SKETCH composition, single-party; GPT's carrying read requested (L919). *Where:* CHAT-LEDGER.md L919;
`cited/cq01-deeptime-20261024-2255/` (trap-certificate-31-495.py and output, kit-wallstates-3eca23c.json). *Novelty:* the trap and the
absorption route are the kit's (Rule30Ether, Rule30PeriodTwoSideways); the application here is UNASSESSED against the kit's catalog.

**Statement.** Let R = {1,2,3,4,5} (11111, cell 1 first) and R' = {1,2,3,4,6,7,8,9} (111101111). Then u R = u R', hence Psi R = Psi R';
R and R' are not move-equivalent; and Psi R has infinitely many black cells (CQ01 for R; likewise for R').

**Proof (sketch).** F = drv altCol R satisfies IsR30 (drv_isR30). Column 0 is altCol t = ether 3 (t + 3) for all t (ether column B4 is
0, 1, 0, 1). At t1 = 9, columns 1..6 equal ether (3 + p) (9 + 3) and columns 7..19 form a wall state at phase (9 + 3) % 4 (finite
computation, retained); (3 + 6) % 7 = 2. By the kit's trap_invariant, columns 1..6 equal the ether at every t >= 9, so column 1 is
ether 4 (t + 3) for t >= 9. The same holds for R' with t1 = 5 and the same phase s = 3. At the odd times 1, 3, 5, 7 the two columns 1
agree (finite computation). So u R s = u R' s for every s, and Psi R = Theta (not u R) = Psi R'. They are not move-equivalent: by the
GC1825 corollary move classes are paths, and the forward moves from 11111 are 31, 47, 111, 175, 431, never 495. Since u R is eventually
periodic, the kit's not_finSupp_Psi_of_eventuallyPeriodic gives infinitely many black cells in Psi R. QED (sketch; second reader wanted;
a Lean version would decide drv on cells 1..19 at t <= 9 and apply trap_invariant).

*Independent carrying read (GPT, GC1828/MI761, 2026-10-24): L919 is HAND/PROVED as a composition using the kit's existing theorems, not a new Lean replay. Full nine-step hand table and all hypotheses in reports/wolfram-agents/GPT-L919-TRAP-AND-OUTCOME.md section2. The row from31 at t4 is495 and at t9 is{6,8,14}; its phase0 wall word is0100000100000. Consequently u31(q)=u495(q)=q mod2 for every q, Psi31=Psi495, and both Psi rows have infinite support. The move path reaches431 at width9, not495. General CQ01 and novelty remain open/unassessed.*

### GC1974 — the canonical white-triangle lineage under a fair initial left half (GPT, 27 October 2026; waiting room)

**Status:** complete hand PROOF-SKETCH; Local independent carrying read pending. No novelty claim.
[Full definition, proof and adversarial checks](../reports/rule30-triangle-lineage-fresh-input.md).
Fix the entire initial suffix from -1 rightward, with101 at -1,0,1, and take the remaining
left cells independent fair. Start at the specified singleton0 and follow each hung child's
shrinking core, continuing at odd singleton tips and stopping at an even final pair.
Every reached width has conditional lawP(M=m)=2^-m under the specified exposure; for a finite
list with all earlier widths odd the probability is2^-sum(m). Survival through n odd children
is(2/3)^n, so this canonical chain terminates almost surely. Carrying step: frontierb=c-1-t
falls by m in the scan and equals(c-r)-1-(t+r+1) at the next tip whenm=2r+1. Left permutivity
supplies a unique fresh initial bit per inspected output. No initial cell beyond that frontier
is read during core erosion. Not a fixed single-seed, general connected-component or centre-clock theorem.

*GC1975: the independent read is parked under L1025's owner full halt. No active reviewer task; candidate remains PROOF-SKETCH.*

### GC2035 — triangle origin carried by a two-cell parity (waiting for Local)

**Update L1083 (29 October): PROVED, two-party carrying read by Local; finite-context scope only.** Earlier status retained below.

PROOF-SKETCH with independent exact finite controls. For arbitrary exterior and x[0..7]=1 b 00000 1,
F^6(x)_6 XOR F^6(x)_7=1 XOR b, although each cell varies with the exterior. The [hand derivation](../reports/rule30-structure-afterlife.md)
tracks a white-anti-diagonal relation r OR s=1 through three short updates. Review that carrying derivation;
no claim for every triangle context. At t7 the eight-site observation supports overlap (COMPUTED), so this
window no longer always decodes b. The cap's separate five-cell exclusion is COMPUTED, not this lemma.

### GC2038 — the cap's minimal five-cell exclusion, hand explanation (waiting for Local)

**Update L1083 (29 October): PROVED, two-party carrying read by Local, including the relaxed four-step implication.** Minimality remains the separate finite support certificate.

Earlier status — PROOF-SKETCH: x_0[0..7]=01111110 implies x_8[8..12]!=00010 for every exterior. The
[hand proof](../reports/rule30-cap-five-cell-proof.md) carries10r1(NOT r) into a1abc with a AND b=0 and
 a OR b OR c=1, then two local exclusion lemmas eliminate all two-step predecessors of00010.
The stronger relaxed four-step statement is checked on1280 local inputs; a contrary case violating the
second premise reaches00010. Minimality against any four-cell support test remains GC2035's exact certificate;
no statistical independence or infinite persistence claim. Local: read A–C, especially Lemma B2.

### GC2153 — Exact single-doubling countdown and local zero-pair controls (waiting for Local)

PROOF-SKETCH, exact countdown already recorded GC2008 and recovered here; no novelty or submission claim.
[Full hand account](../reports/rule30-edge-density-account.md): nonconstant source s of dyadic periodH,
low stream anti-H and returning high stream h imply Delta^(H+1)h=NOTs; least vanishing difference
indices give r_h=r_s-1. The01 case is the kit's order_of_antiperiod. Actual finite controls pass.
A separate explicit periodic temporal control allows00 resource drop H/2-1->0, all three least periodsH,
two consecutive OR gates, first-contact and final-black guards respected. Another permits0->2. Neither is an adjacent-diagonal
root-seed construction. The missing density inference is precisely a restriction from common ancestry.

### GC2154 — Third-gate consistency and complete white-run filling (waiting for Local)

PROOF-SKETCH, direct consequence of known R_step, not a proposed new submission. For periodic s,b,
there exist periodic u,v with Db=s OR u and Ds=u OR v iff s<=Db<=s OR Ds. Sufficiency takes
u=Db AND NOTs, v=Ds. Thus b is constant on every complete white run of s. This next gate excludes
GC2153's synthetic family at t=a+2; its earlier two-gate scope remains accurate.
[Polynomial explanation and actual fixed-cycle witness](../reports/rule30-edge-density-account.md):
filled runs contribute X^a U_L, order2^v2(L)-1 (known1b82d8.geometric_exact). Actualsourceorder127
and outputorder1 require forcingorder2, which cannot result from zero or one filledrun. The checked
witness has47. No sublinear count bound follows; original seed/whole-stack question remains open.

### GC2156 — Full-space linear parity signatures cannot close shift and OR (waiting for Local)

PROOF-SKETCH, standard Boolean-ring algebra reproved for a representation boundary; no novelty claim.
[Proof and actual-witness reduction](../reports/rule30-edge-density-account.md). On all H-periodic words,
an XOR-linear signature compatible with cyclicshift and pointwiseOR is either zero or injective.
Nonzero kernelword a and unit e_i with a_i=1 give sigma(e_i)=sigma(a AND e_i)=0 byOR compatibility;
shifts give every unit, and linearity gives the zero signature. This does not cover restricted seed
families, nonlinear signatures, approximation or computation-time lower bounds. Modulo(1+X)^3, the
retained47-run witness reduces to3odd residue classes and forcing(1+X)^2; sourceorder127 vanishes.

### GC2157 — Quantitative geometry of the known seed odometer (waiting for Local)

PROOF-SKETCH, known odometer and classical homogeneous-tree machinery applied by hand, not a novelty
or submission claim. [Full carrying proof](../reports/rule30-edge-odometer-dimension.md): in the
first-difference metric, the actual single-seed orbit closure has2^e_j prefixes through j, uniform
prefix masses, and distance2^(-J_k-1) between phases whose difference has2-adic valuation k.
Its Hausdorff dimension is liminf e_j/(j+1), and its box dimensions are the corresponding liminf/
limsup. The free spatial positions carry independent fair labels under Haar phase measure, with
no typicality assertion for any chosen orbit. Levelwise Cauchy gives the exact minimum energy
1+(2^s-1)sum_j2^(sj-e_j). Known e_(2m)<=m+Q(0,m), Q<=floor(log2m)+1 force infinite critical
1/2-energy for every probability. Subcritical finite energy, dimension1/2 and the density limit
remain open. No CA simulation or formal build was performed; independent carrying read requested
only when Local resumes.

### GC2158 — The next ancestor forces non-singleton black-run boundary flips (waiting for Local)

PROOF-SKETCH, Boolean elimination of known R_step equations, not a new delivery claim.
[Full proof and controls](../reports/rule30-edge-density-account.md#gc2158-one-more-upstream-gate-leaves-choices-only-at-isolated-black-cells):
periodic u,v,w with Db=s ORu, Ds=u ORv, Du=v ORw exist iff GC2154's filter holds and every011
in s forces Db=1 at its first tick. Explicit maximal u gives sufficiency. For mixed periodic s,
white-fill bits across a following black run of length K>=2 obey y_next=y XOR1 XOR(Kmod2).
Thus S>0 singletonblackruns give exactly2^S relaxed assignments. Retained256-cycle: R93,S69,
24constraints, all three lowcoefficients still free. Patches preserve three gates but replace
the true upstream profiles, so no actual-root counterexample or asymptotic density statement.

### GC2159 — Signed opposite-arc separation adapter for G134/G135 (waiting for Local)

PROOF-SKETCH variant of the already carried hand argument, classical basis machinery, no novelty
claim. [Exact argument and three uncompiled sources](../reports/wolfram-agents/ACTUAL-CONTINUANT-SOURCE-REVIEW.md#gc2159-exact-opposite-scale-separation-now-has-carrying-source):
adjacent-basis errors epsilon,eta have opposite signs. In the spatial strip[-Q-D,D], D<q<=Q,
a return error opposite to eta and smaller than|epsilon| forces coordinates(0,-1). Actual opposite
carry arcs supply the signed error via a floor-difference lift plus/minus1. Coefficient-one actual
continuant recurrences and finite visit bounds give the strip, hence k=h+q_current. Thirteen staged
heads are UNCOMPILED; previous21 passing heads unchanged. The complete251 horizon is not yet assembled.

GC2161 independent carrying read: Local L1168 accepts the complete signed strip, half-open lift and
actual-continuant indexing. **PROVED by hand, two-party; to move out of the waiting room.** The
requested cast normalization is applied; all13new source heads remain UNCOMPILED. No full251 or
current-toolchain certificate follows. Local takes final assembly; GPT source/review work continues.

### Waiting room — GC2205 ruler-closure count (29 October2026)

PROOF-SKETCH, independent read pending: [successive exceptional1(10)^m11 blocks](../reports/wolfram-agents/RIGHT-PROFILE-DELIVERY-SPEC.md#gc2205-exceptional-ruler-closures-have-a-deterministic-sparse-count)
have starting exponents e_next>=e+2^e, so completed-block counts have zero density. Known reset/countdown mechanism;
no fair-transition, downstream-influence or new half-rate theorem. The underlying closing-length law is carried
against Cloud's independently written CL645; the new counting argument remains solo. Finite control GC2204 passed.

### Waiting room — GC2206 primitive-front class cardinalities (29 October2026)

PROOF-SKETCH, solo GPT. For k>=5,K>k, the submitted short-inverse classes partition W<2^k in counts2^(k-4),3*2^(k-4),12*2^(k-4). This is an elementary injection/image-count corollary, not a new inverse-tail theorem; exact eight-bit odd classes4/12/48 independently checked in one finite control. No survivor frequency or orbit density. [Proof, guards and source comparison](../reports/rule30-primitive-source-review.md#elementary-cardinality-guard--proof-sketch-not-independently-read). Independent reader held without waking Local/Cloud.

### Waiting room — GC2208 clocked driven-boundary interface (29 October2026)

PROOF-SKETCH, solo GPT. Restarting230bc7's driven trace at oddT=2a+1 makes its u R(a+k) the white-even channel observable. The full-root/EdgeOK certificate induction applies directly to a clamped right half, without assuming a whole-line clock extension. Shift-closure language inherits the published path bound. [Exact proof, source and boundaries](../reports/rule30-clocked-gap-interface.md#exact-objects-and-the-boundary-guard). No new Lean replay; existing forbidden gaps recovered as prior art. GC2209's finite graph/oracle check passed and does not independently carry this universal interface proof.

### Waiting room — GC2210 guarded00 two-start-bit phase law (29 October2026)

PROOF-SKETCH, solo GPT; [full carrying proof](../reports/rule30-zero-pair-phase.md). On an actual finite-seed prefix Q_j=Q_(j+1)=Q_(j+2)=H even, beta/gamma start flips give c'=c+gamma+beta*prefix-XOR(NOTa). The second0 survives iff beta*parity(a)=0; on that branch the next flag is F+beta*A+gamma*B, with A=parity(c XOR(b AND h)), B=parity(b). The alternative01 branch reads the next flag B over2H. One-bit term is already GC2014/L1070; eight fixed controls pass GC2211. Whole older profiles remain required; no root-density, novelty or general00 phase-invariance claim.

### Waiting room — GC2212 finite-precision regularity of the right-edge map (30 October 2026)

PROOF-SKETCH, solo GPT; [full quotient and endpoint proof](../reports/rule30-edge-regularity.md). For Phi(x)=x XOR(2x OR4x), the differentiability loci modulo 2,4,8,16 are all 2-adic integers, Z, nonnegative integers and the empty set, respectively. The modulo-four quotient depends exactly on the two bits below the perturbation scale. Ordinary 2-adic differentiability fails everywhere. This closes a direct application of Shi–Anashin–Lin's uniformly differentiable transitive theorem; no density theorem, new experiment, independent read or novelty claim.

GC2213 extends this sketch: exact finite-scale iterate quotients multiply and telescope to the known delayed parity coefficient at prefix returns. Every fixed positive iterate still lacks a common modulo-four threshold even on actual finite-time root states, by the known top-edge growth. [Carrying continuation](../reports/rule30-edge-regularity.md#gc2213-the-return-quotient-is-the-known-delayed-phase-coefficient). No new numerical validation or density bound.

### Waiting room — GC2214 thinning consistent periodic drivers (30 October 2026)

PROOF-SKETCH, solo GPT. [Exact reduction](../reports/rule30-periodic-mask-review.md#solo-consequence-two-driver-classes-suffice-for-the-strong-assertion): for nonzero e=c AND shift(c), k=previous(e) OR e removes isolated black cells and preserves every remaining effective-consistency pin. For e=0 retain one pulse per period. The strong left-only exclusion reduces exactly to these two classes. No period excluded and no right-half realization preserved; PR57's separately reviewed transport theorem is prior art.

GC2215 adds a [solo ZBL countercontrol](../reports/rule30-periodic-mask-review.md#an-aperiodic-actual-zbl-trace-with-every-p-th-bit-black): zeros exactly at P*3^n+1 give an aperiodic trace with every P-th bit black. Known reconstruction realizes it; known Jen clock forces the start infinite. PROOF-SKETCH, no finite counterexample or new priority claim.


### Waiting room — GC2216 reset-free finite predecessor multiplicity (30 October 2026)

PROOF-SKETCH, solo GPT. [Full pair-image proof and boundary guards](../reports/rule30-reset-free-review.md#exact-multiplicity-consequence--solo-proof-sketch): a finite zero-wall row has exactly one finite predecessor iff it avoids0 1^(3m+1) 0; a reset gives zero or two. With externally carried PR53, every three successive positive-time rows of a nonzero finite orbit include a two-parent row. Old G13/G141 mechanisms credited. This does not keep either branch alive to a prescribed horizon; the complete13-tree has an immediate dead branch. No independent carrying read or new machine check of this consequence yet.

GC2218: the eight named boundary controls passed once (COMPUTED, not a universal certificate). The same solo argument now gives an exact all-width count: for a_n unique finite-parent targets of width at most n, A(z)=(1+z^2)/(1-z-2z^3); a_n=a_(n-1)+2a_(n-3), initial1,1,2. Finite support growth gives a_n+2d_n=2^(n-1), hence uniform finite-word zero/one/two-parent proportions tend to3/4,0,1/4 with unique fraction at most(7/8)^n. [Full grammar, endpoint guard and prior-art comparison](../reports/rule30-reset-free-review.md#gc2218-the-fixed-control-passed-exact-finite-word-counts-by-hand). PROOF-SKETCH; no orbit-density or survival consequence.


### Waiting room — GC2219 exact two-substitution silver-word endpoint (30 October2026)

PROOF-SKETCH, solo GPT. For the carried silver word c(s)=floor(s(2-sqrt2))mod2 and odd convergent i>=3, q=q_i,r=q_(i-1),q'=2q+r,Q=q+r, the longest Q-periodic prefix obtainable with at most two substitutions has length2q'+Q; edits at q and2q' attain it. The next letter raises the minimum cost to three because two residue classes require1+2 edits. [Full signed-arc exclusion, majority proof and hand control](../reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2219-two-substitutions-have-an-exact-endpoint-set-by-a-residue-chain). Classical Hamming-consensus method credited; no optimum over lags, fixed-edit hierarchy, Rule30-preserving modification, new numerical check or priority claim.


### Waiting room — GC2220 uniform edge-window half-rate and local covering (30 October2026)

PROOF-SKETCH, solo GPT. Restarting the existing kit Path at a gives parameter nu+E(a), because no initial resource is prescribed. Its known potential bound yields e_(2a+2d)-e_(2a)<=d+Q(e_(2a),d)<=d+Q(0,d). Even-endpoint rounding gives every N-window at most N/2+O(log N) doublings, uniformly in depth. Exact homogeneous prefix fibers then give dim_Assouad(K)<=1/2. [Full source comparison, restart proof and metric guards](../reports/rule30-edge-odometer-dimension.md#gc2220-the-known-accounting-bound-restarts-in-every-spatial-window). No lower bound, density equality, uniform critical covering constant, novelty clearance, compilation or independent read.


### Waiting room — GC2221 ruler-law control has unbounded critical excess (30 October2026)

PROOF-SKETCH, solo GPT. Starting at s1=3,e1=1 after10, concatenate1(10)^(2^e-1), with e_next=e+2^e and s_next=s+2^(e+1)-1. Every occurrence of the exact carried closing law and the no111 rule holds. At n=s_r-1,2E_n-n=r-1, yet E_n/n tends to1/2. The same construction attaches after any actual finite prefix ending00. [Full occurrence, boundary and density proof](../reports/rule30-edge-odometer-dimension.md#gc2221-the-ruler-law-permits-unbounded-critical-excess). Symbolic sufficiency control only, not a Rule30 orbit, full Path model or refutation of the actual critical covering estimate.


### External carrying review — GC2222 PR48 edge-clock source (30 October2026)

Complete external source accepted in stated scope: period h, then antiperiod h, cannot be followed by period h; a constant edge column forces every older column white. An explicit periodic free carrier supports an8-to2 template drop with arbitrary older depth; genuine finite odd codes imitate it through2n+1 ticks at depths4n+3,4n+4. [Proof, boundary guards and evidence review](../reports/rule30-edge-clock-drop-review.md). The latter is finite imitation, not an actual all-time period drop. Retained author99-constant/13-headline replay passes; no GPT compiler or new portal/Human Verified claim.

### Waiting room — GC2223 guarded carrier invasion and exact imitation lifetime (30 October2026)

PROOF-SKETCH, solo GPT. [Four-phase guard induction and all exit cases](../reports/rule30-carrier-invasion.md): the half-line1110 carrier front advances six depths every four ticks after its exceptional entrance. The closed101/1011/100/100 guard masks arbitrary older cells. For PR48 seeds c_n, first terminal-pair failure is f0=6; f_(3k+1)=8k+6,f_(3k+2)=8k+9,f_(3k+3)=8k+13. A leading-defect-only control lacks the guard. No density/centre-period consequence or novelty clearance; one separately frozen local/table self-check pending, independent carrying read pending.

GC2224: the frozen control passed once, including all four local incoming assignments and the omitted-guard witness. Actual receipts retained; no new independent carrying read or status upgrade for the universal argument.

GC2225 strengthens and clarifies the front law: at phase A the leading defect alone forces6depths/4ticks, with arbitrary older continuation. [Exact trailing map](../reports/rule30-carrier-invasion.md#gc2225-exact-guard-map-and-the-remaining-capture-question) gives p'=p AND(q OR r), q'=1 if p1, otherwise q OR NOT(r OR u). Both101 and111 are closed signatures;001 capture for finite older prefixes remains open, and a hand example requires12ticks. PROOF-SKETCH, no new machine check. The omitted101 guard affects the signature, not the phase-dependent speed; GC2223's finite-family exit proof is unchanged.


### Waiting room — GC2231 full-line four-return reproof (30 October2026)

PROOF-SKETCH, solo GPT; known conclusion, explanatory reproof. For Phi(x)_j=x_j XOR(x_(j-1) OR x_(j-2)) on bi-infinite rows, Phi^4(x)=x iff Phi^2(x)=x. G258 forbids odd-weight four-profiles; a primitive0011 profile forces two older0101 profiles and then a newer forcing0111 with odd parity, impossible at clock four. [Complete proof, known two-return classification and scope controls](../reports/rule30-full-line-small-clocks.md). A finite older-side chain can end in0011 but its next profile has clock eight. No centre-column conclusion, higher-clock classification, new numerical check or independent carrying read.


### External carrying review — GC2232 finite eight-return criterion (30 October2026)

PR33 current395-line source09aa298b accepted in its all-width finite-white-boundary scope. Its36-pair certificate and length induction give eight-return iff two-return after deleting three newest cells; the first two/eight-step discrepancies are exactly three cells apart when present. The newest-first state bridge preserves full equality through same-length injectivity. [Source, hand certificate reduction and retained evidence](../reports/rule30-finite-return-eight-review.md). Current128/four-headline replay is reported by author with maintainer headline confirmation; older26/three-headline raw replay separately inspected, no GPT compiler. Safety completeness remains open.

### Waiting room — GC2233 two-run even profiles force the next doubling (30 October2026)

PROOF-SKETCH, solo GPT. In an actual forward Phi spacetime, a q-periodic temporal profile with exactly one white and one black cyclic run, even q>=4, forces its two older profiles to equal Delta C and its next newer profile to have least period2q. Known G258 forces lengths2and q-2; known GC798 projection plus one more actual equation forces the ancestors, then the next forcing has odd weight and least periodq. For q>4 the consecutive periods are q,q,q,2q; for q4 they are2,2,4,8. [Complete proof and scope guards](../reports/rule30-full-line-small-clocks.md#gc2233-an-even-two-run-profile-forces-the-next-period-to-double). No white-root occurrence, frequency, general00 closure, new compute or independent carrying acceptance.


### External carrying review — GC2234 oriented height (30 October2026)

[Exact signed-event identity and oriented safety converse](../reports/rule30-oriented-height-review.md) accepted in scope for arbitrary Boolean drivers. Both complete sources and retained43/8 plus13/3 author replay/headline records read; no GPT compile. The integrality argument and initial-colour mark are essential. No finite-white safety completeness, root frequency or period bound follows. GC2235's separate core-only ancestor draft is UNCOMPILED at freeze and does not upgrade the GC2233 hand period theorem.


### External finite witness and failed development check — GC2236–GC2237 (30 October2026)

GC2235's final core theorem failed elaboration:7helper/control heads have empty reported axioms, final head has sorryAx, and the module is NOT accepted. [Exact failure and caps](../reports/rule30-full-line-small-clocks.md#gc2236-the-core-check-stopped-on-an-elaboration-error); no rerun. Separately, [GC2237 finite reset witness](../reports/rule30-reset-excursion-review.md) is independently carried with defining semantics and6/1 author replay/headline evidence. Its unsafe initial00 trace limits the conclusion to one-excursion parent decoding, not safety completeness.


### Waiting room — GC2238 run-count next-period law (30 October2026)

PROOF-SKETCH, solo GPT. [Exact inverse and period proof](../reports/rule30-run-period-law.md): for an actual q-periodic profile with every cyclic run length at least2, both older profiles equal Delta C. The next forcing C OR SC is inverted by adjacent AND and has least periodq; the next newer profile has least periodq or2q according to parity of black cells plus black runs. Known kit input-parity rule credited. No root occurrence/density/general00 theorem or successful core-module compilation.

### External carrying review — GC2239 transition-cover obstruction (30 October2026)

[Complete normalized derivative-chain theorem and evidence](../reports/rule30-transition-cover-review.md) carried in scope. Every nonzero dyadic word has a TC chain; actual shared OR recurrence is absent. Raw37constant/3headline author replay accepted in scope, no GPT compiler. The added0001 hand control and pair-projection explanation are solo sketches, not independently reviewed new claims.


### Development validation — GC2241 core ancestor and inverse (30 October2026)

[One changed-source check](../reports/rule30-run-period-law.md#gc2241-the-repaired-core-and-inverse-pass-the-development-check):13core heads compile on4.33.1 with empty axioms, expected false-negative and16/8 finite controls pass. GC2236 failure remains retained. This validates local Boolean/forward-profile steps only; no formal least-period/count proof, independent carrying read or official4.35 replay.

### External carrying review and waiting room — GC2242–GC2243 (30 October2026)

[Antiperiod-height source and free-partner construction](../reports/rule30-antiperiod-height-review.md). Existing necessity is carried with26constant/6headline author evidence: periodic b, antiperiodic c and safe child imply zero drift/height diameter<=2. New converse is solo PROOF-SKETCH: the height criterion exactly characterizes existence of some freely chosen antiperiodic partner and a safe child returning after2P. Binary-track endpoint exchange is explicit. Neither actual shared ancestry nor a converse for a prescribed c follows; no new trajectory computation.


### Fixed validation and waiting room — GC2245–GC2246 (30 October2026)

[One fixed constructor pilot and exact partner-count sketch](../reports/rule30-antiperiod-height-review.md#gc2245-the-fixed-pilot-passes-once). All84P2/4/6drivers agree with8736independent partner/initial-colour cases; endpoint-exchange mutant rejected, receipts retained, no repeat. The universal free-partner theorem remains solo. GC2246 counts safe phase-anchored pairs as2^(P-k+2-D) for2k>0white ticks and height spanD1or2 with zero drift; all-black case2^(P+1), failed criterion0. The bijective excursion proof is PROOF-SKETCH; all84existing counts match without new dynamics. Actual shared ancestry remains absent.


### Waiting room — exact free-partner driver language (GC2247, 30 October2026)

[Carrying proof](../reports/rule30-free-partner-language.md), solo PROOF-SKETCH. For P=2m the zero-drift/diameter2 height language has trace(M2^m)-trace(M1^m) phase-anchored words. The three containing strips and two nontrivial overlaps establish the formula; the even/odd intermediate-height guard fixes the top loop count. Dominant cubic root gives an exponentially small fraction of all binary words. This uses known bounded-Motzkin transfer matrices and, for the free-partner interpretation, GC2243's solo converse. No actual-root frequency conclusion or new enumeration.


### External carrying review — the exact D3 equivalence (GC2248, 30 October2026)

[Source, induction and guard audit](../reports/rule30-d3-completeness-review.md). RootD3Reduction013b6889 and CedarD3Converse1db70283 are carried in conditional scope: normalized safe words have a safe prefix1–3cells earlier iff all safe finite-white words return8. Neither assertion is proved. The short-extension dependency repeats only an already-returning prefix; full extension safety remains all-time.529retained author replay declarations/20headlines checked across two checkpoints, no GPT replay. Generated trajectory certificate evidence and individual hand-reading limits are explicit. Known1000010 demonstrates why EightWindow alone is insufficient.


### External carrying review — arbitrary-future gate-past closing (GC2250,30 October2026)

[Exact source/evidence](../reports/rule30-gate-past-closing-review.md): finite4–7bit covers prove spatial closing for every infinite legal future. Absorbing full-past column pairs and finite tree soundness were read. The all-length conditional finite-row exclusion uses exact support preservation and periodic splicing, not a linear closing bound. AllPastClosing/FiniteCoverFamily remain open. Author3057replayed/37headlines and exact13source closure retained; no GPT replay, generated-reduction and guard limits explicit.


### Waiting room — exact finite-cover completeness (GC2251,30 October2026)

[Complete hand converse](../reports/rule30-gate-past-closing-review.md#gc2251-the-finite-cover-format-is-complete-for-qualitative-closing), solo PROOF-SKETCH. For each fixed n, qualitative closing yields an equal pair of full finite-past columns by actual outer locality, hence a finite-prefix leaf. Finite-past legality and canonical packed triangles give the exact PR52 format; König's lemma produces finite root trees. Thus Closing(n), Cover(n) and a uniform cutoff are equivalent. This does not prove their truth for every n, an explicit rate, or a new finite-row exclusion. Independent read and formalization remain pending.

### GC2253 — The finite carrier exit has two different newer-clock outcomes

PROOF-SKETCH, solo hand specialization of the known parity rule. [Exact equations and source-scope correction](../reports/rule30-carrier-reach-pilot.md#exact-hand-diagnosis-and-the-other-exit-choice): PR48's endpoint234,170has forcingEAof odd weight, so either next initial bit gives least period16. Choosing85instead of170one step earlier joins the alternating tail and matches PR58's existing witness. No full-line16-return, new novelty claim or completed q16 computation. The failed positive control is retained.


### Waiting room — Boolean gates and an AND branch label (GC2258,30 October2026)

[Complete carrying steps and evidence](../reports/quadratic-edge-clock-transfer.md). PROOF-SKETCH: own-bit-XOR triangular updates with arbitrary time-independent two-input Boolean gates satisfy the kit's record-charge window bound, hence upper clock rate and Assouad dimension at most1/2. The generic vanishing argument transfers inequalities without dividing by the quadratic coefficient. All-affine gates have a standard logarithmic bound. Separately, on AND's x0=x1=1 branch, C=x5 XOR x2*x3*x4 distinguishes two six-bit8cycles; seeds3 and35 have equal prefix clocks through j8 but different E9. Solo hand results, not compiled; the frozen80case control covered the earlier quadratic family only. Known Skirrow domino formula and kit mechanism credited. Section2 independently carries Cloud's four elementary break rules in corrected scope.

### Waiting room — choked gates and backward periodic branches (GC2261–GC2270,30 October2026)

[Exact arguments and scoped answer table](../reports/cloud-question-workflow-20261030.md). Solo PROOF-SKETCH: for odd seeds, g=b AND NOT s has E(n)<=ceil(log2(floor(n/2)+1)); g=NOT b AND s has E(n)<=ceil(log2(floor((n-1)/2)+1)). Forced constant coordinates give an invariant affine subsystem. A mixed least-period-p spatial driver has parent period exactly p or2p, determined by the permutation of the at-most-two-state recurrent image; constant-one has the separate3cycle. The complete background graph restricts every finite root through40inverse steps to two period sequences; the graph-to-root reduction awaits carrying review. The two final necklaces differ, no all-depth coalescence claim.

Further solo identities in that account: corrected physical finite-parent count2^(w-4) forw>=4, physical/wall bridge T(r)=(r mod2)+2Psi(r), exact reversal response and a specified fresh-bit conditional law. Cloud's antiperiodic-support and physical finite-parent/depth arguments are carried in corrected scope; their source assertions and corrected corollaries are distinguished. Five passed stages, a retained failed control and an unclosed P128substep are separately documented. No new Lean or Human Verified status.

### Waiting room — outside-edge clock imitations and backward period family (GC2272,30 October2026)

[Full short arguments](../reports/cloud-revised-questions-review-20261030.md#gc2272-two-immediate-answers-in-the-revised-list), solo PROOF-SKETCH. Known realization with a white right half and trace0101... has rightmost initial black at-1; truncation to[-N,-1] preserves that trace through timeN. This refutes CL663 A6's proposed width-independent constant outside the right edge, without asserting an eternal clock from a finite row. Separately, E2's mixed-driver p/2p law and the initial black/period3 tails imply least backward tail periods3*2^e at every finite depth>=2, for any finite root's white-right history. No branch-count, growth or coalescence theorem. Current RingOrbits' temporal1/2 classification is a different statement.

### Waiting room — a conditional ether return and exact fixed-left optimum (GC2274–GC2276,30 October2026)

[Complete carrying steps](../reports/rule30-relay-witness-audit.md). PROOF-SKETCH: the specified seven-cell path0010000->0111000->1100100->101111u->0010000 is equivalent to left exterior inputs0001 and right inputs00uv with u OR v=1. The u=1 orbit is known Rule30Ether; arbitrary boundary histories are not physical realizations. Separately, for the entire initial half-line i<=7 black only at0,7 and centre8white, first failure of0101... is at most17 for every right completion. The forced right samples010101001 contain the already certified finite forbidden word101001; finite row {0,7,14,17} attains17. New independent carrying read needed for the frame/finite-prefix transfer; existing certificate is credited, not recompiled. Two finite controlled computations and receipts retained in the linked account; the predicted improvement to18 failed.


### Waiting room — dyadic phase clocks preserve the proposed half-rate mechanism (GC2278, 30 October 2026)

[Complete carrying argument and failed unscaled control](../reports/quadratic-edge-clock-transfer.md#12-gc2278-curiosity-pull--a-fixed-dyadic-phase-clock-can-be-absorbed), solo PROOF-SKETCH. For own-bit-XOR updates with two earlier inputs and coefficients sharing a fixed temporal period L=2^ell, include the phase in every prefix clock and use floor(order/L). Block differences yield the same reset/countdown Path with parameter E_a-ell, hence the proposed window bound. An actual phase-2 three-bit example refutes the unscaled reset law. L=1 recovers the static argument. No odd-period/nonperiodic conclusion, density equality, independent read, compilation or novelty clearance. This is separate from the current static submission candidate.


### Waiting room — arbitrary finite forcing clocks (GC2281,30 October2026)

[Full two-difference proof](../reports/quadratic-edge-clock-transfer.md#13-gc2281-use-a-phase-step-difference-for-any-fixed-forcing-period), solo PROOF-SKETCH. For a common finite temporal period L and own-bit-XOR gates with two earlier inputs, the phase-augmented prefix periods are L*2^K_j. The phase-step difference D_L=S^L+I commutes with ordinary Delta; cancellation gives the forward vanishing implication needed for reset/countdown and Path(K_a). Thus the proposed window bound for K has the same thresholds as the static theorem, including odd L. The L-step composite need not have two-input memory and is not used. No nonperiodic/longer-memory claim, independent read, compilation or new dynamics; kept separate from static Package A.


### Waiting room — exact ancestral-age count and temporal memory recovery (GC2284–GC2285,30 October2026)

[Ancestral-age argument](../reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2284-a-counting-consequence-for-finite-ancestral-age), solo PROOF-SKETCH derived from the already carried G121/L077: uniform normalized width-w words have Pr(A>=k)=C(w-2k)/C(w), with the width-one correction and exact finite means tending to1/3. No orbit measure, independence assumption or novelty claim. [Memory recovery](../reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2285-the-hidden-memory-bit-is-ambiguous-only-at-c-to-b), solo PROOF-SKETCH from the actual two lower recurrences: C,C forces hidden h=0, C,A forces h=1, and only C,B retains a local choice. This gives a finite-prefix counting upper bound, not global ancestry or return-word injectivity. Neither has an independent carrying read or new compilation. GC2282 corrects attribution of the finite-past core to G121/G122 and L077; it does not promote these two new consequences.


### Waiting room — finite ancestry with at most three black cells (GC2289,30 October2026)

[Complete argument](../reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2289-at-three-black-cells-finite-ancestry-has-depth-at-most-two), solo PROOF-SKETCH. One/two-black rows are roots. A three-black width-w row has a parent only if it is11 0^(w-3)1; that parent is the solid width-(w-2)block, which has a root predecessor exactly when3divides w-2. Therefore all three-black ages are<=2and the fixed-width/fixed-three-black mean is(1+[w=2mod3])/(w-2). Known G121/G122/L077 and GC544/GC593/CL058 mechanisms credited. No monotone black-count assumption, numerical fit, orbit law, independent read or compilation. The separate GC2286/GC2288 Lean sources transcribe the older finite core and remain UNCOMPILED after the pilot stopped in an unchanged dependency.


### Waiting room — four-black finite ancestry has sharp age bound four (GC2291,30 October2026)

[Complete proof and branch table](../reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2291-four-black-cells-have-ancestral-age-at-most-four), solo PROOF-SKETCH. Every nonroot four-black row at0,1,k,R has k>=3 and parent1^(k-2)0 1^(R-k). The inverse table reduces the exceptional branch to11(001)^q and then(110)^(q-1)111, whose parent exists exactly for odd q and is a root. The sharp bound is4, attained by110010001. No independent read, machine computation, general fixed-mass bound or novelty claim. Known G121/G122/L077 and current Preimages machinery credited; GC2290 also records the externally known OEIS root/age definitions.


### Waiting room — finite mass and one-step parent counts (GC2296,30 October2026)

[Complete hand argument](../reports/rule30-finite-mass-parent-count.md), solo PROOF-SKETCH. A nonzero finite parent's image has population r+2+2h, where r counts black runs and h counts internal white gaps of length at least2. Positive run/gap compositions and known finite injectivity give an exact rational width/mass enumerator and fixed-K parent fraction asymptotic to(K-2)/w. It recovers the known all-width counts and low-mass shapes. No maximal/mean age or actual-orbit conclusion;1001->111111 refutes run monotonicity. Independent carrying read pending; excluded from Package B.


### GC2298 / GC2305 — exact two-past gap counts, carried L1238

[Full boundary machine and phase-path argument](../reports/rule30-two-step-finite-past.md), PROVED two-party hand in
L1238's scope: the16state inverse accepts precisely finite two-step ancestors; zero gaps have period3after2;
fixed-mass counts are eventual period3quasipolynomials. The leading coefficient is the explicit binomial-residue
filter of GC2305. The ratio to one-past counts still requires soloGC2296. No single-root or age conclusion.

### Waiting room — compact two-past series and exact mass moments (GC2307–GC2309)

[Complete new carrying steps](../reports/rule30-two-step-finite-past.md#gc2307-a-seven-state-quotient-and-compact-exact-bivariate-series),
PROOF-SKETCH: seven quotient states and exact zero-padding removal give H=z^5u^3PS/(P^2-z^2uPR-z^3S^2),
P=1-z, R=P+zu^2, S=P+zuR. GC2308's one frozen exact-arithmetic control passes; this is a self-check, not a carrying
read. Separate pole/derivative algebra gives, for uniform normalized width-W rows with two finite past steps and
W>=16, mean W/2+1 and variance W/4-7/8. The new algebra/moments remain unreviewed and are outside deliveredB.


GC2310 status amendment: L1240 independently carries GC2307's quotient, elimination and padding, now PROVED
two-party hand. GC2309's later moments are still a solo sketch. L1239's generic no-three law is also carried by GPT;
its proposed next-doubling and inner-countdown steps now have explicit guarded GPT proofs awaiting Local.


### Waiting room — nested gate-clock record thresholds (GC2311)

[Complete last-ascent and last01 proof](../reports/rule30-gate-clock-sharpness.md#gc2311-a-last-ascent-argument-closes-losses-and-recoveries),
PROOF-SKETCH. For static two-input GateClock with e(0)=0, e(2m)<=m+2 for m<2058. The first higher-record interval
is trimmed after the last lower-level visit, permitting arbitrary earlier00losses and recoveries; initial first-bit
countdown and final last-bit countdown give the bound. Recursive T_q written in the source. No attainment, lower
clock rate, single-root density, compiler result or larger beam. L1241post11order M-2 carries independently here.


GC2312 status amendment: the nested gate-clock record thresholds are PROVED two-party hand by Local L1243's
complete carrying read, agreeing with its independent L1242 draft. Local owns the separate Lean preparation;
no compilation or submission of this sharpening yet. The actual L1241 single-family witness/receipts are read,
with its period replay accepted only through 38 bits and its manifest sanitation-length distinction recorded.


### Waiting room — direct finite-image boundary covariance explanation (GC2313)

[Complete elementary argument](../reports/rule30-two-step-finite-past.md#gc2313-the-variance-correction-comes-from-four-boundary-covariances),
PROOF-SKETCH. A triangular bijection makes L-2 output bits jointly fair independent in the two-step image of a
uniform normalized ancestor of width L=W-4. Four left-boundary bits have variance3/8; their only nonzero bulk
covariances are1/8,1/64,-1/64, summing to1/8. Thus the mean W/2+1 and variance W/4-7/8 hold for W>=14.
Independent derivation of solo GC2309, not an independent worker read, new computation, fixed-mass or root-orbit law.

L1251 status amendment: Local read every carrying step, so GC2313 is now **PROVED two-party hand** for W>=14.
An exact control by plain Rule 30 steps (`gc2313_moment_check.py`, W=12..20) matches it from 14 to 20. It also shows
the guard is sharp: at W=12 and 13, Cov(S,Z_8)=0 and the variance exceeds W/4-7/8 by 1/32. GC2309's pole argument
stays solo.


### Waiting room — finite-image binomial coupling and constant cumulant corrections (GC2314)

[Complete proof and guards](../reports/rule30-two-step-finite-past.md#gc2314-every-fixed-ancestry-depth-has-a-binomial-bulk-and-finite-boundary-corrections),
PROOF-SKETCH. Uniform normalized width-W rows with at least t finite past steps, W-2t>=2: K=2+S+B with
B~Binomial(W-2t-2,1/2),0<=S<=2t, possibly dependent. Fixed-order cumulants have a width-independent correction
at W>=2t(r+1)+2 by connected input cones. Classical binomial CLT transports when t=o(sqrt(W)); no root-orbit law.
The generic triangular fair-bit and CLT ingredients are known kit results, credited. One frozen moment-only control
GC2315 has not run at this entry and cannot independently carry the hand argument.

GC2316 update: the six-case moment control passed once; all finite controls and actual evidence retained.
The general hand statement remains PROOF-SKETCH. GC2317 separately accepts L1244's full nested gate-clock
development source and exact threshold meaning; this is not an official-checker or new submission receipt.


### Waiting room — bipermutive finite-image control and the missing Rule30 estimate (GC2321)

[Bipermutive boundary control](../reports/rule30-two-step-finite-past.md#gc2321-a-bipermutive-control-isolates-the-missing-boundary-estimate), PROOF-SKETCH. For a quiescent bipermutive diameter-D Boolean rule and uniform normalized input of width L,
output width W=L+D has mean W/2+1 for L>=D+2 and variance(W-2)/4 for L>=2D+2. The latter uniform guard is sharp.
Two separate binomial marginals, which need not be independent, give a classical Gaussian transport for D=o(W).
Rule30 lacks the second permutivity property. Its sufficient open target is Var(S_t)=O(t), equivalently an O(t)
bound on the sum of squared conditional martingale increments; centering at W/2 separately needs small bias.
Known triangular independence and Doob mechanisms credited. No computation, independent carrying read or root claim.

### Waiting room — three hand steps from the 31 October inquisition (Local, L1256–L1257)

[Full statements, proofs and their exact controls](../reports/inquisition-20261031.md). PROOF-SKETCH (Local solo; GPT's
carrying read requested in [the handover](../reports/HANDOVER-GPT-20261031.md)):
1. **Death kinds are a fair coin before the news.** In the kit's normal form, for an even death time t with
   2 ≤ t ≤ W − 1, the starts of width W dying at t split exactly half starved, (x_2, x_1) = (0, 0) at t − 1, and half
   cancelled, (1, 1). Pairing: flip depth t, then flip depth t + 1 iff x_1(t) became black. Both depths reach depth 1
   only at the cone's XOR edge. COMPUTED exact at every such t, W ≤ 20.
2. **Two adjacent left diagonals are coordinates.** For every n, the map from a base row segment of 2n cells to the
   two left diagonals {(−t, t), (−t+1, t) : t < n} is a bijection. Each strip cell's leftmost input enters by XOR, and
   these inputs are distinct, so the map is triangular. COMPUTED N(n) = 4^n, n ≤ 9.
3. **No right diagonal carries 00100 or 11011.** The flips along s(t) = x(t, t) are x(t+1, t) OR x(t+2, t). The
   flip word 0110 is impossible by a two-case analysis on x(3, 0). COMPUTED: the minimal forbidden words to length 10;
   absent in about 6,000 random diagonals of 2,000 steps.

No centre-column or prize inference.


GC2326 status amendment (31 October 2026): GPT has independently carried all three Local steps above. They are
**PROVED, two-party hand**, with the death-pairing ensemble clarified to all starts *supported within* W, not
necessarily having a black final cell. The diagonal-word claim is already G258 (October 9), known and reproved
here; Local's numerical runs were not replayed. [Scoped carrying read](../reports/GPT-INQUISITION-20261031.md#carrying-reads-gc2326).

### Waiting room — finite ether episodes beside a moving black edge (GC2327–GC2328)

[Complete upper proof and lower family](../reports/GPT-INQUISITION-20261031.md#a-finite-ether-window-bound-gc2327-proof-sketch),
**PROOF-SKETCH**. Applied to Lowry's exact PR69 invariant, eight phase-dependent local implications and a 17-edge
potential give no good-pair interval of length floor(2k/3)+5 at depth k. A parity guard handles the only past-time
premise. A concrete actual ether, with its edge replaced by black, has a masking-front bound floor(3t/2), and
prefix autonomy gives finite-row matching episodes of length ceil(2k/3). Therefore the maximal episode length
M(k) lies between ceil(2k/3) and floor(2k/3)+4, so M(k)/k tends to 2/3 in both finite and arbitrary black-edge row
classes. One frozen finite self-check passed; it preceded the lower construction. No independent carrying read,
compilation, exact additive sharpness, global orbit speed, fixed-centre or doubling-density claim. Review the phase
3 past dependency, the phase 6 three-tick case, and the masking-front/truncation step before any delivery.


L1258 status amendment (31 October 2026, Local): Local has independently read both GC2327 and GC2328 against PR69's
actual source (head fcffbaa9): all eight local implications, the 17 potential edges, the parity guard, the phase
identity, the edge-phase table, the masking-front lemma with its four reference bits, and the truncation. Both are
**PROVED, two-party hand**: ceil(2k/3) <= M(k) <= floor(2k/3)+4, so M(k)/k -> 2/3. Local's exact computation
(`tests/probes/ether_episode_exact.py`, k <= 20, output 3dd3599b) finds every M(k) inside the bounds and the GC2328
witness attaining M(k). [Carrying read and T-M](../reports/inquisition-20261031.md#outcomes-of-round-3).

### Waiting room — the exact ether-episode constant for k ≡ 1 (mod 3) (Local, L1258)

[Hand step](../reports/inquisition-20261031.md#a-sharper-lower-bound-by-hand-local-proof-sketch), **PROOF-SKETCH**,
for GPT's read. The GC2328 witness heals at once: X(1) = E(1) and X(2) = E(2) at every depth, edge included,
because E's own OR masks the black edge. At t = 3 the two agree beyond depth 0. Restarting the masking front there
(advance two at odd t, one at even t; reference bits E_(3n+3)(4+2n) = ether(2,5), ether(1,7), ether(0,1),
ether(3,3), all 1) gives R_t = ceil(3(t-3)/2). Hence M(k) >= floor(2(k-1)/3) + 4. With GC2327 this makes
M(k) = floor(2k/3) + 4 exactly for k ≡ 1 (mod 3). COMPUTED (k <= 20), CONJECTURE beyond:
M(k) = floor(2k/3) + 4 - [k ≡ 0 or 2 (mod 6)]. Moving black edge only; no fixed-wall, centre or density claim.


GC2330 status amendment (31 October 2026): GPT has carried L1258's early healing at t=1,2,3, checking the special
depth-one boundary update separately, all four masking reference bits, the integer endpoint count and truncation.
The waiting-room step is **PROVED, two-party hand**: floor(2(k-1)/3)+4 <= M(k) <= floor(2k/3)+4, and
M(3n+1)=2n+4 for every n>=0. The all-residue formula remains a conjecture beyond the reported k<=20 computation.
[Detailed carrying read](../reports/GPT-INQUISITION-20261031.md#gc2330--carrying-locals-early-healing-refinement).


### Waiting room — the exact mismatch front of the GC2328 witness, and M(k) for every k ≢ 0, 2 (mod 6) (Cloud, CL669)

[Certificate and argument](../reports/inquisition-20261031.md#round-4-2026-10-31-cloud-cl669-the-exact-mismatch-front-of-the-witness-the-final-tick-for-k--3-5-mod-6-and-why-the-even-residues-are-different),
**PROOF-SKETCH** (Cloud, solo; a finite certificate plus the two-party front lemma), for GPT's or Local's read.
For the GC2328 witness the maximal mismatched depth is R*(t) = 2 floor((3t − 8)/4) for every t ≥ 4 (direct to
t = 12; then a band of depths [b(t), R*(t)+1], content 111010111 at t = 12, evolves on its own by the masking rule
with E above it by the two-party lemma ceil(3(t−3)/2) ≤ R*(t)+1, and returns shifted by 12 after 8 ticks under the
ether's (2, 4) glide). The front never rests on an odd depth, so the witness's episode at (k, k+1) has length
ceil((4 ceil(k/2)+8)/3) = floor(2k/3)+4 − [k ≡ 0 or 2 (mod 6)], and with GC2327:
M(k) = floor(2k/3) + 4 for all k ≡ 1, 3, 4, 5 (mod 6). For k ≡ 0, 2 (mod 6) only the upper bound is open; the exact
max-plus form of GC2327's tree is already floor(2k/3)+4, the good predicate is exact at k ≡ 0 and loose by one at
k ≡ 2 (mod 6) (computed to k = 20). Moving black edge only; no fixed-wall, centre or density claim.


GC2331 status amendment (31 October 2026, GPT): CL669's carrying argument is independently read and **PROVED,
two-party hand**. GPT checked the bootstrap by explicit hexadecimal rows, U-R by all four residues and the guarded
band's four-tick/six-depth return by hand. First-arrival arithmetic proves the full witness length for every k.
Consequently M(k)=floor(2k/3)+4 for k≡1,3,4,5 mod6. The universal upper improvement for residues0,2 is still open;
Cloud's finite diagnostics do not close it. Exact-pair descent has the necessary endpoint guard t<=L-2.
[Full carrying read](../reports/GPT-INQUISITION-20261031.md#gc2331--clouds-exact-front-carried-with-a-four-tick-band-certificate).


### Waiting room — the exact ether-episode length M(k) for every k (Local, L1259)

[Theorem, three proofs and their verification](../reports/inquisition-20261031.md#outcomes-of-round-5-mk-for-every-k),
**PROOF-SKETCH** (Local; machine certificates with controls), for GPT's carrying read. For every k ≥ 1,
M(k) = floor(2k/3) + 4 − [k ≡ 0, 2 (mod 6)]. At edge phase 7 the GC2328 witness is the unique optimal prefix.
- **Proof 1, the front potential.** In the two-sided frame the mismatch front's moves follow an 8-phase table, and
  Φ = R + g(ψ) − 3t/2 is invariant. There is no retreat after tick 0. The floors at t = 1 (the c = 2, 4 exclusion
  and the c = 7 dichotomy) give R(t) ≥ R_w(t) for every row and phase. Certificate:
  `ether_front_potential_certificate.py`.
- **Proof 2, the six-depth descent.** An exact window of length L ≥ 11 at depth j forces the exact ether at depth
  j − 6 on 0..L − 5, for every phase. That reduces to 56 light-cone windows, enumerated exhaustively; the bases are
  M(1..8). Certificate: `ether_six_depth_descent_certificate.py`.
- **Proof 3, rigidity with LRAT.** GC2327's tree for r ≠ 7, plus 254 LRAT-checked local systems for r = 7.
  Certificate: `ether_rigidity_certificate.py`.
- **Steps to read.** For Proof 1: the two-sided reduction, Lemma B, the t = 1 floors and the modified-row reduction.
  For Proof 2: the light cone, translation, window containment and the induction. Either proof alone suffices.
- **Self-checks so far.** Twelve same-worker verifiers, none refuting.
- **Scope.** Moving black edge only; no fixed-wall, centre or density claim.


GC2333 status amendment (31 October 2026, GPT): L1259's all-depth formula and phase-seven prefix uniqueness are
**PROVED, two-party hand**, via the front-potential proof with the corrected hypothesis of right-bounded mismatch
(finite positive mismatch, not finite support on Z). GPT carried all requested hand steps, including the healing
exclusion and clean-tail induction, and replayed the small finite certificate with a rejected-potential control.
Proof2's requested hand reductions also check; its finite enumerations were source-read, not rerun. No independent
LRAT replay or Lean verification is claimed. [Full carrying read and evidence](../reports/GPT-INQUISITION-20261031.md#gc2333--l1259l1260-reviewed-the-all-depth-maximum-and-the-phase-seven-optimum).


### Waiting room — same-edge rigidity for eight periodic backgrounds, including the classic 7 × 4 ether (Local, L1261)

[Statement, certificate and scope](../reports/inquisition-20261031.md#outcomes-of-round-6-which-periodic-backgrounds-a-black-edge-can-follow), **PROOF-SKETCH** (hand reduction by Local; machine certificate with
checked LRAT proofs), for GPT's read.
- **Claim.** No black-edge code follows white, PR69's one-in-four ether, (5, 5), the classic 7 × 4 ether (7, 28),
  (8, 20), (9, 72), (10, 6) or (12, 12) at two adjacent depths forever. Episodes are at most M_R(1) + (a + b)(k − 1).
- **The steps that carry it:**
  - black-edge codes as generic two-sided configurations, and the light cone;
  - the onset-free descent: time translation, so each tick a..L − 1 − b of the shallower pair is covered by a window
    inside the episode;
  - the base M_R(1) finite.
- **Certificate.** `inquisition_background_rigidity_certificate.py`, 1,266 windows, kissat and cadical, LRAT-checked,
  with replay controls.
- **Open.** (7, 63), (9, 57) and (12, 68) have shadows and remain open beyond k = 12.

GC2335 review amendment: L1261's generic model, exact light cone, onset-free descent and base-enumeration
logic are **carried, two-party**. The eight-background numerical premises remain Local's reported
proof-checked T-D4 computation; GPT read the complete certificate source but did not replay its raw proofs.
The classic-ether identity is explicitly R_j(t)=P(2+t-j,t), with least moving period 28 carried by hand.
[Review and evidence scope](../reports/GPT-INQUISITION-20261031.md#gc2335--l1261-carried-odd-period-backgrounds-have-a-separate-obstruction).

### Waiting room — odd-period ring backgrounds cannot attach to a black-edge pair (GC2335)

**PROOF-SKETCH, GPT.** For any spatially periodic generic background of non-dyadic least temporal
period q, every episode at black-edge depths k,k+1 has length at most 2^(k+1)+q-1, from any onset.
Known dyadic prefix clocks plus P+q matching force the reference pair to have dyadic period; XOR
accumulation propagates that property around the ring, contradicting q. This reuses GC734's odd-part
invariant and the kit's periodic-word comparison. It would settle qualitative exclusion for L1261's
three shadowed cycles (reported q=63,57,68), leaving linear bounds open. Separate short hand proof:
M_white(k)=ceil(k/2), by backward white-cone growth and the single-black seed.
[Carrying steps, controls and attribution](../reports/GPT-INQUISITION-20261031.md#gc2335--l1261-carried-odd-period-backgrounds-have-a-separate-obstruction).

L1262 status amendment (31 October 2026, Local): M(k) = floor(2k/3)+4-[k ≡ 0, 2 mod 6] for every k >= 1, and the
phase-7 prefix uniqueness, are now **kernel-checked in Lean 4.35** (`lean/Rule30EtherEpisode.lean`, SHA256
33aff7322077fb0b…, core Lean, imports only the kit's `Rule30FrozenRuler`; standard axioms only; two independent
same-worker verifiers, one with a standalone kit-independent re-check). [Details](../reports/inquisition-20261031.md#the-lean-formalization-of-mk-l1262).
No submission.

L1263 status amendment (31 October 2026, Local's carrying read of GC2335): the **odd-period obstruction** (a spatially
periodic background of non-dyadic least period q cannot be followed forever; M_R(k) <= 2^(k+1)+q-1) and
**M_white(k) = ceil(k/2)** are **PROVED, two-party** (GPT GC2335, Local L1263); known mechanism (GC733/GC734, GC738),
applied. With GC2335's carrying read of L1261's hand reduction, the **same-edge rigidity of the eight backgrounds**
above is **PROVED** (two-party hand reduction; T-D4's machine certificate, LRAT-checked with controls, not replayed by
GPT), scoped to the eight printed orbit words. [Read, controls and corrections](../reports/inquisition-20261031.md#the-carrying-read-of-gc2335).

### Waiting room — attachment to a periodic background is the alternating one alone, for every ring size p <= 26 (Local, L1264)

**PROVED, given T-Y's COMPUTED census.** A black edge can follow a spatially periodic background of the edge frame
with p <= 26 at two adjacent depths forever iff the background is the alternating one. It is a case split over
already-proved pieces: non-dyadic backgrounds (GC2335, two-party), white (ceil(k/2), two-party), PR69's ether (PR69;
M(k) exact), alternating (explicit code 1,0,1,0,...). T-Y shows that these are all the dyadic ring cycles with
p <= 26. CONJECTURE for every p: no other dyadic ring cycle exists. [Results and scope](../reports/inquisition-20261031.md#t-y-results).

L1265 amendment (Local): `lean/Rule30EtherEpisode.lean` v2 (SHA256 2ea831a9de66fefc…) adds `wit_episode` (the named
witness) and `episode_witness_finite` (a finite row, black bits only in 0..k+1, attains M(k)); purely additive over v1;
builds clean, standard axioms. [Details](../reports/inquisition-20261031.md#lean-v2-the-witness-named-and-a-finite-witness-l1265).

GC2336 formal-source amendment: GPT carried the complete Lean v2 source at5e44f902,
SHA2562ea831a9de66fefc63e621a218f49e53ed4230f41a15577bfa8e4b01c3c95c22. Statement fidelity and
proof-source review PASS for episode_bound, episode_max, witness_unique, wit_episode and
 episode_witness_finite. No GPT compiler replay; Local's current-main rebuild remains distinct
from its reported ee2f421 build. [Exact review scope](../reports/GPT-INQUISITION-20261031.md#gc2336--lean-v2-source-review-passes-current-main-rebuild-remains-locals).

L1266 amendments (Local, after GC2336):
- **The Lean artifact.** `lean/Rule30EtherEpisode.lean` v2 (SHA256 2ea831a9…) builds on the kit's current main
  842b756f, both as an outside file and as an in-tree module, with unchanged axioms. With GPT's GC2336 source and
  fidelity PASS, the Lean artifact for M(k) is two-party reviewed and kernel-checked on current main.
- **The attachment waiting room (L1264).** Its census is L1066's, known and reproved by T-Y, which extends it to every
  power-of-two period for p ≤ 26. Its scope, per GC2336: a background is a spatiotemporally periodic orbit, and the
  all-p classification would imply alternating-only attachment, not conversely.
  [Corrections](../reports/inquisition-20261031.md#t-y-results).

### Waiting room — uniform capture by leftmost ancestry and escape from every left band (GC2357)

**Carried by Local (L1284): PROVED two-party; see the entry "GC2357 / L1284" above.** Original statement: For any Rule30 initial row with a
leftmost black cell e, mark e and propagate along every black-parent edge. In coordinates
j=x-e+t, every black cell on diagonal j is marked from time C_j=1+j(j-1)/2 (j>=1), with C_0=0.
A pair of diagonals n,n+1 cannot both stay white for n+1 consecutive rows (the known B1 descent).
Once the preceding two diagonals are captured, unmarked black at j persists precisely while
both preceding cells are white. This gives the induction and uniform exit from band0..D by
(D+2)(D+3)/2 updates. Restarting proves no eventual finite-band confinement. The carried L1283
finite-word lock then excludes eventual periodicity of the seed's (r,L) history. Existing
`JenPow2.infinitely_many_black` gives distance from the edge tending to infinity. No positive
physical speed or centre claim. [Full proof, scope and controls](../reports/rule30-genealogy.md#17-a-uniform-capture-argument-replaces-the-clock-induction-gc2357).
All2048 width12 initial prefixes pass67 updates; computation is a self-check, not the carrying read.

### Carrying amendment — F1/F2 uniform escape and Capture.lean fidelity (GC2358)

L1286's classification is **PROVED two-party hand**, Local proof/GPT carrying read: among the64
edge rules, uniform all-parent ancestry escape holds for exactly the32 F1 rules and8 F2 rules;
the other24 have a seed confined to0..1. The single-diagonal descent and capture induction carry.
[Exact arguments and qualifications](../reports/rule30-genealogy.md#22-gpt-review-of-l1284l1287-and-the-exact-lean-packet-gc2358).
L1287's exact Capture.lean source passes GPT statement/proof-source review; its compilation is
Local's reported Mathlib build using Lean4.33.1. The entire Rule30 nonperiodicity chain remains two-party
hand, with only capture/exit formalised here. The Rule210 history extrapolation is not carried.

### Carrying amendment — eternal edge cycles through period64 (GC2359)

L1292's temporal-ring graph equivalence is **PROVED two-party hand**, Local/GPT. Independent
literal temporal integration and Kahn acyclicity, with retained descending ranks and controls,
certify that Fix(Phi^64) consists of the two alternating phases -1/3 and -2/3. The all-period
conjecture is open; no Lean formalisation claimed. [Exact review and data](../reports/rule30-genealogy.md#271-carrying-verdict-on-the-temporal-ring-reduction).

### Waiting room — affine conjugacy obstruction from the genuine two-cycle (GC2359)

**PROOF-SKETCH, GPT.** Phi has a genuine two-cycle but Phi^2(0)=12 is not0. If a bijection
conjugates it to A(y)=a*y+b on Z_2, a point of exact period2 gives
0=A^2(y)-y=(a+1)(A(y)-y), hence a=-1 by absence of zero divisors. Then A^2=id everywhere,
a contradiction. No continuity or residue-compatibility assumption is needed. This repairs
the broader claim whose mod8 argument only addressed residue-compatible conjugacies.
[Proof and qualifications](../reports/rule30-genealogy.md#273-arithmetic-review-and-a-stronger-repair-of-the-affine-claim).


### Carrying amendment — finitary return sections and the temporal halving identity (GC2362)

**PROVED two-party hand**, L1304–L1305 proof/GPT carrying read: return sections of cycle length L
are ell c^L with finitary ell of depth at most2L; split/doubling formulas and lambda_(2L) recursion
carry. The anchored F_(2L,n)=F_(L,n) XOR F_(L,n) after c^L, and its half-period derivative
interpretation, carry. Local L1304 carried GC2361's level-sign/depth-two, abelian control,
infinite OS(psi) and pairing deductions. [Scope and full read](../reports/rule30-genealogy.md#321-what-carries-and-the-precise-objects).
No compressed invariant, termination rank or distributional genericity follows.

### Waiting room — influence countercontrol and entrance-to-cycle reduction (GC2362)

**PROOF-SKETCH, GPT.** A four-bit block-swap example has coordinate influences1/2 even on a
proper invariant subset, but its paired derivative vanishes identically. The fixed-p window
graph reduces infinite continuation from valid entrances E_p to reachability of a directed
cycle; a backward-closed separator containing all cyclic vertices and excluding E_p would
suffice. No such uniform separator is yet proved.
[Countercontrol](../reports/rule30-genealogy.md#323-a-hand-countercontrol-generic-single-bit-influence-can-hide-a-perfect-constraint) ·
[Graph reduction and obligations](../reports/rule30-genealogy.md#325-change-the-question-to-entrance-versus-recurrence).

### Waiting room — the episode bridge: no eternal point of any period ends in the phase E iff M_E(k) < ∞ for every k (Cloud, CL676) — *carried by Local, L1310 (PROVED two-party); the G8 corollary is the kit's own `episode_bound` plus `Rule30EtherGrounding`, known*

[Argument](../reports/rule30-genealogy.md#382-a-bridge-to-the-episode-line-proof-hand-short-cloud-read-requested), **PROOF-SKETCH**
(Cloud, hand, short), for Local's or GPT's read. For a phase E (a two-sided configuration of the edge frame, periodic
in time with period p and in depth up to a time shift) other than the rain, and M_E(k) the longest agreement of the
pair of columns (k, k+1) with E over every row of depth k + 1 behind a black edge and every alignment (CL672):
M_E(k) = ∞ for some k gives a prefix whose pair agrees for ever, hence every deeper cell stays E, and the autonomous
finite prefix is eventually periodic with a power-of-two period, so the row is an eternal point with tail E; conversely
an eternal point with tail E beyond depth d has M_E(k) = ∞ for every k ≥ d. Consequence: `Rule30EtherEpisode`
(M(k) = ⌊2k/3⌋ + 4 − [k ≡ 0, 2 mod 6] for PR69's ether, which is the phase G8) proves that no eternal point of any
period has tail G8. Light-speed frame, black edge; no claim about the conjecture itself, the centre or the prize problems.

### Waiting room — affine disturbance families and a moving-record certificate (GC2385)

**PROOF-SKETCH, GPT.** A family E_n+a_n·z remains affine through one interior
edge-frame Rule30 update iff each pair a_(n-1),a_(n-2) has rank at most one
(over the two-element field: one is zero or they are equal). Equal nonzero
labels add an exact correction to the Jacobian update. The condition must be
propagated at every tick. A finite common-front family with exact boundary
interfaces and translated return E,A→E,AM yields uniform positive advance
when its return shift is positive; existence and arbitrary-prefix entry remain
open. [Derivation and precise hypotheses](../reports/GPT-BOUNDARY-LAYER-REVIEW-20261102.md#gc2385--an-exact-test-for-an-affine-layer).
512 local/32,768 family truth-table checks are self-checks, not a carrying read.


### Carrying amendment — T41 robustness graph to actual front (GC2386)

**PROVED two-party hand**, Local L1316/GPT carrying read, conditional on the
finite graph facts. At W8/R>=12, a FAIL-free forward closure with edge advances
>=-1 and every three-step path gaining>=1 keeps the actual front within its
valid interior range and gives unbounded advance. The480 case has nonnegative
edges and two-step gain>=2. Local's416/389-state enumeration is COMPUTED M5;
GPT source review and240-state transition comparison are not an independent
reconstruction. [Full hypotheses and capture-interface qualification](../reports/GPT-BOUNDARY-LAYER-REVIEW-20261102.md#gc2386--locals-new-robustness-certificate-changes-the-live-target).
Entry from arbitrary finite prefixes remains open.
### CL681 corollary — the classic ether absorbs a black edge: news speed exactly zero (Cloud's proof, Local's carrying read L1320, the two-sided step kernel-checked; 2026-11-02)

*Status (Local, L1320, 2026-11-02):* PROVED, computer-assisted, two parties. The eternal part is a Lean theorem: Lowry's trap in its
two-sided form, `trap_two_sided` and `news_bounded` in [tests/probes/lean/EtherTwoSided.lean](../tests/probes/lean/EtherTwoSided.lean),
kernel-checked against the kit's `Rule30Ether` at kit main c42f6e5 (Lean 4.35.0; axioms `propext` and `Quot.sound` only; source
SHA-256 f5d8afce…19b2). The hand step below is that theorem's induction: the kit's, with the prescribed column 0 replaced by the
induction hypothesis on every column left of the B3. When the B3 is black, its right input is masked (a ⊕ (1 ∨ r) = ¬a); when it is
white, `wall_facts` makes the wall's head the ether's B4. The finite part (entry) is COMPUTED by two independent programs:
Cloud's `ether_trap_check.py` and Local's [`ether_trap_replay.py`](../tests/probes/ether_trap_replay.py) ([output](../tests/probes/ether_trap_replay.out)).
The replay compares against the kit's own ether (not a frame-built one) over every column inside the left light cone. It
enumerates the 28 kit alignments (7 spatial × 4 temporal), which cover Cloud's 196. All 28 enter by t = 222, at the entry
times Cloud found. Before entry the leftmost mismatch is never left of −37, so Cloud's window from −40 was wide enough, by
three cells. After entry, 2,000 exact ticks show no mismatch at or left of the B3; 60 random right halves beside a wall state
do the same. **A uniform bound follows:** at every alignment, no column x ≤ −38 is ever disturbed (least B3 at entry −38).
*Update (Local, L1345, 3 November):* now formalised in full. `edge_pinned` in
[tests/probes/lean/EtherEdgeZero.lean](../tests/probes/lean/EtherEdgeZero.lean) proves, for all 28 alignments, that from a
finite time on the ether is undisturbed at and left of x_B and the disturbance never heals within the next 13 cells.
The 28 entries and the never-heals table are kernel `decide`s, with the light cone and the simulation bridge as lemmas.
It is kernel-checked against kit main c42f6e5 with standard axioms (propext, Classical.choice, Quot.sound); the build
takes 34 s, 2.6 GB peak, on the M5. Source SHA-256 005f5e3e…dfe2. Awaiting GPT's source read (NIGHT-TASKS A1).


[Argument and checks](../reports/inquisition-20261031.md#round-11-2026-11-02-cloud-cl681-the-classic-ethers-exact-zero-the-inserted-edge-enters-lowrys-ether-wall-trap-at-every-alignment-so-the-ether-is-never-disturbed-beyond-a-bounded-distance-news-speed-exactly-zero-proved-on-the-kits-trap_invariant).
**Statement.** For every alignment of the classic ether (the kit's `Rule30Ether`: spatial period 7, temporal period 4), a black
edge inserted at x = 0 with white to its right never disturbs the ether to the left of a fixed column: the leftmost mismatch
x_min(t) is bounded below for all t. **Status:** PROVED modulo one short hand step. The finite part (every one of the 196
alignments enters Lowry's ether-wall trap, ether columns up to a B3 followed by one of the 109 wall states, by t = 222) is
machine-checked in `ether_trap_check.py`, which also replays the kit's kernel fact `wallOK_true` (closure under every right
input and the masked head condition) and `ether_rule`. The eternal part is the kit's Lean theorem `trap_invariant` (Lowry,
PR65). The hand step, for Local's or GPT's read: the kit's induction assumes a prescribed ether column 0; with the whole left
half-line at the ether at t1 instead, each column left of the B3 reads three ether cells (its right neighbour is at most the
B3), the B3 reads the wall's head only when white and that head is then the ether's B4 (`wall_facts`), and the strip's next
state is in the set for either right value; so all columns up to the B3 stay ether for ever. Prior art: the trap and the ether
are Lowry's (PR65); the kit uses the trap to exclude ether walls beside a periodic centre column. The entry of the inserted
edge, the exact zero of the news speed, and the velocity-spectrum reading are ours. Lab frame; no claim about the centre column.


### GC2389 — certified front clock and single-flip completion (GPT's proof, Local's carrying read L1322; 2026-11-02)

*Status (Local, L1322):* PROVED two-party, computer-assisted. Local read the clock transfer, the telescoped speed bound, the
singleton resets, the single-flip congruence (195 · (−21) ≡ 1 mod 1024) with its depth guard, and the noninterference corollary.
All are sound given the finite facts. Local's own generator (`front_closure.py P1024 8 --all-theta --clock`, independent of GPT's
literal reconstruction) reproduces every finite fact exactly: the per-class advance is unique, there is one 52-cycle with total
advance 68, the advance word has least period 52 and is identical to GPT's, the potential range is 55, the four singleton fibres
have a longest wait of 47, and (882, 0) is the only window-0 state ([genealogy §47](../reports/rule30-genealogy.md#47-locals-carrying-read-of-gc2389-the-exact-front-clock-and-the-one-flip-completion-l1322)).
The same test gives the 480-state phase an exact clock as well: 288 classes in one cycle, total advance 480, advance word of least
period 18 (+30), longest wait to a forced window 2, and no window-0 state.


[Complete statements, proof and finite certificate](../reports/GPT-CAPTURE-CHECK-20261102.md).
COMPUTED independently on Intel:389-state S_E closed,520 edges, all400 original
rows enter; phase projection one52-cycle, total advance68; four singleton
fibres, reached within47 steps. Existing GC2386 supplies unbounded advance.
PROVED two-party after Local L1322: after entry R(t+52)=R(t)+68 and
|13(R(t+n)-R(t))-17n|<=55; front motion ignores older wake. For any prescribed
K-cell prefix/alignment theta, choose R>=max(K+8,12) with
R=21*(theta-882) modulo1024; background beyondK with a single flip at R is
already in S_E. The first such R is at most1023 cells farther. This gives
captured completions of every prefix, not capture of each unmodified row.
No whole-wake periodicity, all-prefix capture, centre theorem or Lean claim.


### Waiting room — free-boundary front transfer, guarded wall clauses and exact locality (GC2390)

[Statements and proof obligations](../reports/GPT-CAPTURE-CHECK-20261102.md#gc2390--use-the-certificate-as-a-guarded-wall-obstruction).
PROOF-SKETCH: the certified front induction only needs the rule at depths>=2,
so arbitrary time-dependent shallow columns are allowed. Permanent-tail strips
therefore avoid S_E at a deepest mismatch of depth>=12; exact clauses must keep
the deeper-suffix guard. The reversed upward-rigidity indexing is supplied.
For paired K-prefixes sharing their bottom L<K cells, mutual differences reach
at most K-L-1+2t; if this is<=R_A(t)-9, their front and eight-cell states agree
at t. Endpoint agreement yields capture by T; agreement of first capture times
requires the guard at every prior tick. No pre-capture speed assumption.


### GC2390 carrying amendment (Local L1323, GPT receipt GC2392)

The free-boundary transfer, deepest-mismatch guarded clauses with reversed CNF
indexing, and paired-prefix light-cone guard are PROVED two-party, conditional
on the finite S_E certificate. Local carried the exact induction and source
mapping in L1323; the earlier waiting-room text retains its pre-review status.
No augmented/original-CNF certificate equivalence or universal capture follows.
### GC2393 — the two-open reset of the front's trailing pair (GPT's proof, Local's carrying read L1327; 2026-11-02)

[Statement and proof](../reports/GPT-OPEN-STRETCH-REVIEW-20261102.md). *Status:* PROVED two-party. Local re-derived it by hand and
checked it on 16,000 random literal rows with its own code (L1327). If the deepest mismatch is at R and the background at depths
R−2 .. R+3 reads d c 0 0 z z, the next two moves are both +2. The two cells behind the new front become (¬c ∧ ¬z, c ∨ d),
whatever the old pair and every deeper cell were. E_R = 0 is also necessary: with E_R = 1 two open moves keep at least two
distinguishable images of the four old pairs (2 or 3 in Local's check). Scope: erasure of the trailing pair only, not of the
8-cell window, not S_E entry, and no claim that every front meets the block.

### Waiting room — the moving-anchor closed-set certificate, and the (9, 7) law of (7, 63) at 28 alignments (Cloud, CL682)

**READ REQUEST CLOSED — GPT GC2404:** the corrected abstract closed-set soundness
is carried for matching half-line plus strip membership, giving bounded front
motion and limiting speed. Individual numerical runs retain their computed
status and initialization premises; exact front recurrence needs the offset
check. CL676 and CL681 requests were already carried by Local and are now read
by GPT too. [Complete CL676–CL684 verdict register](../reports/GPT-CLOUD-REVIEWS-CL676-CL684-20261102.md).

[Statement, soundness and results](../reports/inquisition-20261031.md#round-12-2026-11-02-cloud-cl682-the-closed-set-certificate-with-a-moving-anchor-passes-both-controls-g8s-lean-verified-law-lowrys-109-states-rediscovered-for-the-classic-ether-proves-the-9-7-law-of-7-63-at-28-alignments-and-fails-on-9-57s-519-at-every-window-to-32-although-that-law-holds-to-t--20000).
**Soundness (hand, short; PROOF-SKETCH until read).** If the real state (ether phase at the anchor, the W cells right of it) lies
in a set closed under "retreat the anchor by one when its own next cell differs from the ether, else keep it and compute the far
cell for both values of the cell beyond", with every strip holding a mismatch, then the state stays in the set for ever (cells
left of the anchor read only ether cells; the anchor reads the strip's head; the strip's next contents are exact but for the far
cell), so the leftmost mismatch stays within W of the anchor, and if every path of length P in the recurrent part moves the
anchor by S − P, the front stays within a bounded distance of a line of slope (S − P)/P. With a stationary anchor this is the
kit's `trap_invariant`. **Controls:** G8's Lean-verified (4, 2) law at all 32 alignments; the classic ether at all 196 with 763
states = Lowry's 109 × 7. **Theorem (COMPUTED closures; PROVED modulo the soundness read):** at 28 alignments of (7, 63) the inserted
edge's front law is (9, 7), lab speed exactly 2/9, with closed sets of 70–74 states at W = 16. Lab frame; no claim about the
centre column.


### CL682 scoped carrying amendment — GPT GC2394

The abstract matching-half-line/closed-strip induction and bounded-distance
front-speed implication are carried, with exact background phase and matching
at the anchor included. Individual28 certificates are not upgraded: the public
source loses a spatial phase for (9,57), and the positive control receipts do not
match the committed output. Exact front recurrence still needs the offset test.
[Full review and repair](../reports/GPT-ANCHOR-PHASE-REVIEW-20261102.md).

### Waiting room — GC2395: an erased pair bit returns through the deeper wake

[Two explicit actual histories](../reports/GPT-RESET-MEMORY-RETURN-20261102.md)
share a pair after the carried two-open reset, but recover the old pair bit in
their next pair after a blocked step. PROOF-SKETCH with six literal self-check
updates, awaiting Local; no assertion of occurrence in P1024 or480.
**Correction (Cloud, CL683, after GPT's review).** The CL682 entry above said (9, 57)'s 5/19 law was not a wall law at widths up to
32. The certificate's phase bookkeeping was wrong for backgrounds whose spatial period does not divide the frame period (G28); with
it fixed, (9, 57) is certified at all 60 sampled alignments (closures 102–4,432 states at widths 16 and 24; a direct replay of 300
real transitions passes), so its (19, 14) law, lab speed 5/19, is a moving wall, PROVED modulo the soundness read. The controls and
the (7, 63) result are unaffected (their spatial periods divide their frame periods).


### GC2398 finite horizon carried; GC2401 single clause implication

L1332 carries3(D-r) contradiction horizon for original permanent-tail strips
entered in S_E at depth r>=12. GC2401 separately retains a cake_lpr-accepted
LRAT proof of one D13 phase882/word0 clause from the exact original CNF, with
empty-proof rejection and byte-bound target. The stage's later harness assertion
failed on checker exit-code convention; raw failure preserved, no rerun.
[Evidence and exact scope](../reports/GPT-GUARDED-ONEPROOF-20261102.md#outcome--gc2401-one-implication-checked-harness-failure-preserved).


### Corrected CL683–684 carrying scope — GPT GC2402

The laboratory phase defect is repaired and the corrected transition/tail-DP
algorithm is carried for bounded-distance front motion and limiting speed,
conditional on the finite checks and valid initialization. Exact front
recurrence still needs offset-aware path scores; per-alignment start guards
are explicit in [the carrying review](../reports/GPT-CORRECTED-ANCHOR-READ-20261102.md).
This supersedes the earlier statement that the current source still loses phase.

### T48 graph carrying scope and weighted physical guard — GC2403

Universal finite graph reachability by rank is carried from Local's algorithm.
Its physical application needs sufficient depth for cumulative retreat.
[H(v) guard](../reports/GPT-FUNNEL-DEPTH-READ-20261102.md) is PROOF-SKETCH awaiting
Local; no all-A one-cell retreat bound or new graph census claimed.


### L1333 depth16 attractor transfer carried — GC2403 crossing receipt

GPT read the full F/G recursion and hand proof. With reported Fmax6, Gmax4,
any P1024 A state at depth>=16 follows graph edges at depth>=10 and reaches S_E
at depth>=12 within113 ticks. PROVED two-party conditional on finite graph
and drawdown facts. [Source qualifications and receipt](../reports/GPT-FUNNEL-DEPTH-READ-20261102.md#crossing-update-l1333-resolves-the-practical-guard).
### Waiting room — the doubling bit's descent calculus and the forced family 11(01)^k (Cloud, CL686; 2026-11-02 23:30 GMT)

**Carrying read returned, GPT GC2405:** Lemmas P/F/I below are now PROVED
hand/two-party at their stated coefficient-period guards. The conditional
five-state model has exact mean2/5. The general zero-family inference is not
carried: [review](../reports/GPT-CLOUD-REVIEWS-CL685-CL686-20261102.md) restores the
already-carried CL645/GC2205 rule k<=q0-1 and nextbit1 iff k=q0-1 for context
11(01)^k, q0 the prefix period before its first1. k2 is already the unconditional
GC2201 exclusion; all-k zero thresholds need the exceptions and actual-root
guards. “Free” is an unresolved functional, not proved stochastic freedom.
The original statement is retained below with this amendment controlling status.

**Setting.** R_j(t) = bit j of Φ^t(a) for an odd seed a, Φ(x) = x XOR ((x << 1) OR (x << 2)); L_j the period of the prefix through
bit j (the kit's lifting rule: L_j = L_(j-1) or 2 L_(j-1) by the parity of g_j = R_(j-1) OR R_(j-2) over L_(j-1), `S_rule`);
d_j = log2(L_j / L_(j-1)). For f of period P and c on Z/2^m: F_c(f; P) = Σ_{s<P} c(s mod 2^m) f(s) mod 2. Then d_j = F_1(g_j; L_(j-1)).

**Lemma P (pairing).** If a(s + P/2) = NOT a(s), b(s + P/2) = b(s) and 2^m | P/2, then F_c(a OR b; P) = Σ_{s<P/2} c(s) + F_c(b; P/2).
*Proof.* Pair s with s + P/2; c agrees on the pair; (a OR b) + (NOT a OR b) is 2 where b = 1 and 1 where b = 0. ∎

**Lemma F (forcing).** If a(s + P/2) = NOT a(s) and 2^m | P/2, then F_c(a; P) = Σ_{s<P/2} c(s). *Proof.* a + NOT a = 1 on each pair. ∎

**Lemma I (integration).** If R(s) = R(0) XOR Σ_{u<s} g(u) with 2^m | P, then F_c(R; P) = R(0)·Σ_{s<P} c(s) + F_{c'}(g; P) with
c'(u) = Σ_{u<s<P} c(s mod 2^m) mod 2, which depends on u only through u mod 2^(m+1). *Proof.* Exchange the two sums; the tail sum is
the total minus the prefix Σ_{s≤u} c(s mod 2^m), and a full block of 2^m contributes Σ c, so the parity is 2^(m+1)-periodic in u. ∎

**Applicability.** When d_(j-1) = 1, R_(j-1) has antiperiod L_(j-2) = L_(j-1)/2 (the kit's `antiperiod`: an odd-weight integrand over
its period) and R_(j-2) has period L_(j-2); when d_idx = 0, R_idx = R_idx(0) XOR the running XOR of g_idx, of period L_idx (`R_step`).
So reading the letters backwards from d_(j-1), with the object alternating between an OR (level G) and a diagonal (level R):
a 1 at level G applies P and moves to the lower diagonal at half the period; a 1 at level R applies F and stops (FORCED);
a 0 at level R applies I and moves to the OR one level down at resolution m + 1; a 0 at level G stops (FREE).

**Theorem (the forced family; PROOF-SKETCH).** The descent reaches FORCED exactly when the backward word is 1(01)^k 1, k ≥ 0, i.e.
when the forward word d_(j-2k-2) … d_(j-1) is 11(01)^k, and then d_j equals the accumulated constant, which is 0 once the periods are
large enough: for k = 0, L_(j-2) ≥ 4 (no_three); for k = 1, L_(j-4) ≥ 8 (GC2007's 11011 after base 4; the constant q/2 + q/4 is 1 at
q = 4); for k = 2, L_(j-4) ≥ 16 (new: 1101011 forbidden). *What a reader should check:* Lemma P's use of the coefficient vector
(the period condition 2^m | P/2 at each pairing), and the general-k period condition, derived here only to k = 2 (the code carries
every constant; all 832 forced leaves in the data matched d_j, including the 64 forced ones).

**Not claimed.** Nothing about the density limit: the free leaves are measured fair (CL686) and the fair-except-forced chain's 2/5 is
a model value. The alternating word is free under the family (GC2164).

### Waiting room — GC2408 common-target window refinement (GPT,3 November2026)

**Carried, Local L1343; adopted GPT GC2409:** the common-target closure,
rank monotonicity and native8/10/12 equality are PROVED two-party at the
stated finite-fact/physical-depth premises. Downloaded artifact digests are in
[the source manifest](../reports/GPT-CLOUD-REPAIRS-REVIEW-20261103-sources.json).
The dated sketch wording below is retained as history.

[Complete statement, FAIL case and rank proof](../reports/GPT-WINDOW-REFINEMENT-REVIEW-20261103.md).
Local L1340's guarded W->W+2 projection is now PROVED hand/two-party. New corollary
PROOF-SKETCH: target at width W all refinements of certified S_E8; its universal
attractor C_W lifts into C_(W+2), with nonincreasing ranks. Native good G_W is
contained in C_W; if the lifted target lies in G_W then equality holds. T51's
finite mask facts supply this at8/10/12. No new set computation, all-width decay,
measure-zero theorem or universal rooted capture. Physical use retains width/
drawdown/entry guards. Local carrying read requested; no duplicate job.
### CL686 waiting-room amendment after GPT's GC2405 (Cloud, CL687; 2026-11-03 00:04 GMT)

Lemmas P, F and I above are **PROVED hand/two-party** (GC2405 supplies the XOR-pair derivations). The **"forced family" theorem is
withdrawn as stated**: its all-k period condition p_(j−4) ≥ 2^(k+2) is only q0 ≥ 4 in GC2201's notation and does not remove the ruler
exceptions. The carried statement is GC2201's (with CL645's composition, GC2205): for a forward context d_s … d_(s+2k+1) = 11(01)^k with
q0 = L_(s−1), **k ≤ q0 − 1 and d_(s+2k+2) = 1 iff k = q0 − 1**; so an appended 1 is possible only when k + 1 is a power of two, 1101011 is
forbidden outright, 11011 closes with 1 exactly at q0 = 2 (the universal start), and 11010101 would close with 1 at q0 = 4 if that
context occurred (no actual-root occurrence is asserted; the retained k = 3 examples start at q ≥ 256, and the code stops SMALL_R at
that boundary rather than certifying a zero). The descent calculus is an alternative organisation of that result; its forced
constants reproduce the exceptions it can reach. Nothing here concerns the density limit.

### Waiting room — GC2409 finite-path bound and guarded healed-strip010 corollary

[Exact statements and scopes](../reports/GPT-CLOUD-REPAIRS-REVIEW-20261103.md).
PROOF-SKETCH: max integer weight M over all K-edge paths gives every cycle mean
<=M/K; repaired G8 graph bounds are conditional on its retained output integers,
with one-step-rise<=W guard. Separately, an old mismatch at L and agreement of
the images on(L,Y) excludes common010 starting at L<q with q+2<Y, by actual kit
Preimages.eq_of_evol_one_eq_on_of_window.010 at L remains allowed. New guarded
application awaiting independent read; known GC521/522 jump laws already carried.

### Waiting room — GC2412 arbitrary right tails beyond198 for the ether edge

[Source read and light-cone consequence](../reports/GPT-ETHER-EDGE-ZERO-SOURCE-READ-20261103.md).
The original380-line EtherEdgeZero source is carried. New corollary PROOF-SKETCH:
initial agreement with initRow on x<=198 suffices for its eventual pinning, with
arbitrary right tail farther out, since xB+t1+13<=198 at every recorded alignment.
Local carrying/formalization choice pending; current original headline remains
about its stated cut row. No final submission packet accepted yet.

### GC2413 — A2 universal recruitment agreement, source carried

Local HealingBound.healing_bound, front_ge and K_succ_bounds are **PROVED,
two-party hand read**, with Local's kernel/checker reports separate from GPT's
source read. [Exact source hashes, induction and scopes](../reports/GPT-A1-A2-PACKET-REVIEW-20261103.md).
The background can be aperiodic; the theorem is an agreement bound, not a general
speed-limit existence or actual-front sharpness theorem. Classical masking and
half-line propagation are prior art, as compared in that report.

### Waiting room — GC2415 exact prefix codec and separator decoder criterion

[Carrying proof sketch](../reports/GPT-INVERSE-PREFIX-CODEC-20261103.md).
For the actual kit inverse/uninverse pair, decoder output j needs only input0..j.
Known D F=id and equal finite prefix alphabets give F D=id, prefix isometry and
exact membership v in F(HardCore) iff HardCore(D(v)). The generic finite-prefix
principle is known; this specific consequence awaits independent carrying read.
No all-label separator, physical-origin or random-seed conclusion.

### GC2416 — The ether edge with arbitrary right tails beyond198

[Revised source and actual checker receipts](../reports/GPT-A1-TAIL-AND-RECEIPTS-READ-20261103.md).
GC2412's pending corollary is now **PROVED two-party**, formalized by Local as
edge_pinned_tail and source-carried by GPT. Entry transfer keeps the entire
matching half-line and13-cell wall, then uses the existing trap. No finite-seed
prize consequence. Final public packet/notebook status is tracked separately.

### GC2418 — GC2415 prefix codec independently carried

Local L1353 reads the actual kit definitions, equal-prefix decoder induction,
finite cardinality step, reverse composition and exact hard-core image/count.
Adopted: [GC2415](../reports/GPT-INVERSE-PREFIX-CODEC-20261103.md) is **PROVED two-party,
hand**, conditional on the cited kit lemmas; no Lean compilation claimed.
The old waiting-room request is closed. All-label SEP remains open.

### Waiting room — GC2417 separator-label scan and admission

[Exact growing-word formula](../reports/GPT-DECODER-LABEL-SCAN-20261103.md),
PROOF-SKETCH. Reuses known GC1208 bulk scan; new label boundary, guarded3->1
normalization and SEP/mortality dictionary need carrying read. The complete
carry-group/length/head quotient has an explicit admitted-prefix hand counter.
No no-finite-state theorem, unbounded ancestry construction or census.

### GC2421 — GC2417 dictionary independently carried; finite adaptive strip pending

Local L1356 carries [GC2417](../reports/GPT-DECODER-LABEL-SCAN-20261103.md):
exact growing-word identities, admission, guarded normalization and explicit
quotient counter now PROVED two-party, hand. This closes that waiting-room
read, not all-label mortality. Its bulk scan is known GC1208.

[GC2419](../reports/GPT-FINITE-INTERVAL-RECRUITMENT-20261103.md) and the
[GC2421 translated wall-entry bridge](../reports/GPT-ETHER-ADAPTIVE-SHIELD-PILOT-20261103.md#outcome--gc2421)
remain PROOF-SKETCH. The computed112 cutoff is conditional on that hand
transfer; it does not replace the ready formal198 theorem.

### Waiting room — GC2423 exact backward threshold of the adaptive boundary

[Three-case inequality and composition](../reports/GPT-BACKWARD-SHIELD-THRESHOLD-20261103.md).
For f_t(p)=p−1+E(t,p), h_t(q)=q at black E(t,q), else q+1,
f_t(p)>=q iff p>=h_t(q). Reverse-time composition gives the exact least
initial cutoff for a target inequality. PROOF-SKETCH awaiting carrying read;
standard order-adjunction principle specialized, no inverse Rule30 assertion.

### Waiting room — GC2424 correlated two-tick prefix recruitment

[Exact suffix guard, monotone macro and backward threshold](../reports/GPT-TWO-TICK-RECRUITMENT-20261103.md).
Known GC2026/L1143 a10 identity is already carried. New application: two orbits
agreeing through p with suffix010 still agree through p after two ticks; A2
alone retains p−1. Suffix110 leaves an unknown gap and is not enough. The
actual-orbit macro is monotone and lowers the backward target threshold by1
exactly when010 ends at that target. PROOF-SKETCH for these applications;
no computation, optimal-tiling claim or new formal source.

### GC2425 — Optional112 wall transfer and backward threshold carried

Local L1358 carries [GC2421's translated agreement and wall entry](../reports/GPT-ETHER-ADAPTIVE-SHIELD-PILOT-20261103.md#independent-carrying-read-adopted--gc2425)
and [GC2423's threshold equivalence/composition](../reports/GPT-BACKWARD-SHIELD-THRESHOLD-20261103.md).
Now PROVED two-party hand, conditional on finite entry/threshold certificates;
Local independently recomputed all28 on M5. No Lean112 theorem, no claim to
optimal robust shielding. The separate finite-left GC2419 and correlated
GC2424 macro remain sketches; A2's final packet passes independently of them.

### GC2426 — Finite interval and correlated010 macro carried

Local L1359 independently reads [GC2419's finite-interval agreement](../reports/GPT-FINITE-INTERVAL-RECRUITMENT-20261103.md)
and [GC2424's prefix joining, monotone actual-orbit macro and threshold](../reports/GPT-TWO-TICK-RECRUITMENT-20261103.md).
These are PROVED two-party hand; M5 finite checks separate. The later finite-left
wall corollary is not promoted by inference. A separately frozen same-table
pilot will test whether the stronger certificate reduces the common112 cutoff.

### GC2429 — Backward-threshold coalescence carried

Local L1360 carries [GC2427's one-tick01 merge and ordered-gap criterion](../reports/GPT-TWO-TICK-SHIELD-PILOT-20261103.md#outcome--gc2427).
PROVED two-party hand for certificate maps, not dynamical mixing. Two safe
actual singleton completions remain COMPUTED finite examples, not all-tail
agreement. [GC2430's exact87-input whole-line bridge](../reports/GPT-SHIELD-EXACT-TAIL-QUERY-20261103.md)
is a separate PROOF-SKETCH awaiting carrying read; no solver status inferred.

### Waiting room — L1362 rooted-front observer: exact cutoff 87 for GC2430's target, common cutoff 87 (Local, 3 November 2026)

[T54: observer, soundness sketch, controls and outcome](../reports/rule30-genealogy.md#58-does-a-rooted-front-certify-more-than-a2-t54-l1362).
The observer branches on the leftmost difference L and keeps a three-valued window of width W to its right, with E's
values as the coefficients of the exact mismatch identity. Half-line states and pruned states are certified by A2's
threshold (GC2423, carried).
- **Soundness (PROOF-SKETCH, carrying read requested).** Every actual trajectory heals, becomes A2-certified, or stays
  matched by a live state.
- **Computed with W ≥ 2 at (4, 3), under this soundness.** Agreement through 87 suffices for agreement through −24 at
  222 for every tail, and the flip at 87 shows that 86 fails. So 87 is exact, and GC2430's 111 question is answered
  "yes".
- **Computed over the 28 entries.** The common cutoff is exactly 87 (A2: 112). 24 entries are exact; four have open
  gaps.
- **Not claimed.** No eventual-pinning optimality, and nothing in Lean.

### GC2434 — L1362 rooted-front observer carried

[Complete GPT carrying read](../reports/GPT-ROOTED-FRONT-REVIEW-20261103.md).
Step/scan/half-line expansion/A2 pruning/zero completion and initial-cut
monotonicity now PROVED two-party hand. Conditional finite table gives common87
for the28 specified entry-agreement targets, with matching witness at(4,3).
No Intel replay, Lean87 or optimal eventual-pinning theorem. Four finite-width
gap plateaus and P1024 transfer remain separate open questions.

### GC2435 — Exact original111 circuit independently LRAT certified

[Proof/input/checker hashes and scope](../reports/GPT-TAIL-SOLVE-PILOT-20261103.md#outcome--gc2435).
Original68907-variable CNF063ae6ae is MACHINE-CERTIFIED UNSAT by CaDiCaL LRAT
and unchanged cake_lpr; protected unit kept out of original. Via the carried
cone bridge/controlled literal encoding, all initial tails after111 preserve
the retained(4,3) agreement target. Corroborates the rooted87 observer; not
its Lean formalization, no optimal eventual-pinning result.

### L1366 — Rooted-front observer and A1's cutoff 87, kernel-checked (Local, 3 November 2026)

[Section 60](../reports/rule30-genealogy.md#60-the-rooted-observer-in-lean-a1s-right-tail-from-198-down-to-87-l1366):
`tests/probes/lean/RootedFront.lean`. **PROVED (Lean, standard axioms; the kit's Check.lean passes).**
- **The general theorem.** `check_sound` and `tick_sound` formalise the observer GC2434 carried by hand, for every
  pair of whole-line rule-30 evolutions, with the thresholds as untrusted data.
- **The result.** `edge_pinned_tail87` is A1's tail theorem with cutoff 87 in place of 198, at all 28 alignments. That
  87 is the least cutoff for the (4, 3) entry rests on the computed flip-87 witness, not on this file. This supersedes
  the L1362 waiting-room entry for the 28 fixed entries.

### GC2440–GC2442 — Exact entry cutoff and scoped carrying reads (3 November2026)

[Original-CNF certificate](../reports/GPT-ONE-GAP-SOLVE-20261103.md#outcome--gc2440): cutoff43 exact for alignment(5,1),T148,Q−11 entryagreement target; original LRAT checked, flip43 witnesses failure42. [T55 review](../reports/GPT-ETHER-INVASION-REVIEW-20261103.md): strip actual-path inclusion and cyclemean-to-asymptotic-speed argument CARRIED conditional on finite graph bound; displayed44cycle unrealizability CARRIED. Reusable temporal-clause application remains PROOF-SKETCH pending Local. [L1366 scoped read](../reports/GPT-ROOTED-LEAN-STATEMENT-REVIEW-20261103.md): actual theorem/hypotheses and checker JSON PASS, no new Intel build or public verification status.

### GC2447/2448 — Certified wall entry and a guarded prefix family (3 November2026)

[Completed finite check](../reports/GPT-RETAINED-HISTORY-CHECK-20261103.md#outcome--gc2447): Local's S13 exact7/44potential/cycle checked independently onIntel; actual retainedtail firstenters109wall at558,anchor−82,phase2/word5284, minfront−81. [Arbitrary continuation corollary](../reports/GPT-PREFIX490-CAPTURE-20261103.md) is PROOF-SKETCH pendingLocal carry: first490initialcells force permanentcapture/exactdepth81 with sameinitialleftether. No uniformalltail or shortestprefix assertion.

### GC2451–GC2453 — Prefix490 carried; reset/return-law sketches (3 November2026)

[L1373 scoped adoption](../reports/GPT-PREFIX490-CARRY-READ-20261103.md): prefix490 exactdepth81 arbitrarycontinuation family PROVED hand/two-party, conditional finiteentrycertificate. [Finite52frame export](../reports/GPT-52-STATE-CHECK-20261103.md#outcome--gc2452) checked actualreset1951 but refuted repeatedpaths. [Universalreset and guarded return/family arguments](../reports/GPT-RESET-RETURN-LAW-20261103.md) remain PROOF-SKETCH awaitingcarry, with exactfinitecosttable and existingpotential theorem as premises.

### GC2458 — Endpoint-free budget from a critical reset (3 November2026)

[Full guarded hand argument](../reports/GPT-CRITICAL-RESET-BUDGET-20261103.md), PROVED hand/two-party L1378: 44R+8C≤t for every actual right tail when the initial core has global-minimum potential; the complete finite certificate and carried strip transfer are premises. No frequency/capture claim or new Lean verification.

### GC2460/2461 — Three fastest falls exist; continuation-family sketch (3 November 2026)

[Complete original-model/physical check](../reports/GPT-THREE-FAST-FALLS-RESULT-20261103.md): CHECKED SAT, independently replayed L1379, an actual ether-left/core1951 row falls at 44,88,132 with endpoint cores 1951,1951,4767. The original 114,348 clauses and wider scalar/packed replay pass; no infinite repetition claim. The finite-prefix consequence (all continuations beyond118 preserve the three falls; beyond124 also preserve endpoint4767) is PROVED hand/two-party L1379, conditional finite witness.

### GC2462 — A fixed actual-row map for fast returns (3 November 2026)

[Hand reformulation](../reports/GPT-FAST-RETURN-MAP-20261103.md), PROVED hand/two-party L1380, conditional carried budget/transfer: F(r)(x)=Q^44(r)(x−7); from ether-left/core1951, F(r) has the same prefix exactly when the first fall is44 and returns to1951. Nested survivor sets use sufficient prefix13+37n. The checked three-fall row lies in K2 but not K3; no third same-core return, infinite survivor, finite-state closure or periodic tail is supplied. Moving frames and compactness are known background.

### GC2463/2464 — Exact pre-return packet and a conditional mask (3 November 2026)

[Hand proof](../reports/GPT-RESET-PREIMAGE-PACKET-20261103.md), PROVED hand/two-party L1381: phase2 ether-left B3 gives a fall/core1951 iff its first seven right cells are10011pq with p∨q=1. This yields five units/one OR as an exact next-return condition. It is not implied by previous returns alone. If the last packet has p=1, prefix12+37n suffices for n same-core returns. Existing witnesses instantiate a49-cell one-return family and86-cell two-return family; no minimality or later-motion claim. Local's16384-case check and Intel's128-parent self-check are separate computations; the independent hand read carries the general statements.

### GC2471 — Mahler post-B continuation boundaries (3 November2026)

[Complete hand application](../reports/GPT-MAHLER-POST-B-BOUNDARY-20261103.md), PROVED hand/two-party L1383: under the exact4,11,6 prefix and B<a≤T4, finite feasibility is a>T_f and acceptance of every already-a-admissible tail is a≥S_f. Constructive finite repeats prove necessity without a density assumption. The first feasible next gap diverges as a↓B but at most one extra step resets the fractional bound. Generic geometric recovery/tail identities are known; no positive-integer survivor or complete new-language classification in this prefix theorem.

### GC2473 — Infinite plateau family and fixed-code right limit (3 November2026)

[Complete hand argument](../reports/GPT-MAHLER-PLATEAU-CASCADE-20261103.md#completed-argument--gc2473), PROVED hand/two-party L1384: all f≥5 give exact L_f formal language on(S_f,T_(f−1)], with four exhaustive first blocks, lower periodic/upper finite witnesses, equality classification and closed lower criterion for integer codes. IntersectionallL_f has exactly terminal eventually-zero extras over the old language; no exchange of fixed and varying integers. Generic affine-supremum method known; no actual integer existence or kernel compilation.


### GC2475 — A nested two-parameter Mahler plateau family (3 November 2026)

[Complete five-case hand argument](../reports/GPT-MAHLER-NESTED-PLATEAUS-20261103.md), PROVED hand/two-party L1385.
For all f≥5,h≥5, L_f plus the next-gap rule after (4,11,6,f) gives the exact language on
(R_(f,h),V_(f,h−1)]. These intervals lie inside (T_f,S_f); periodic/finite witnesses give maximality,
and the fixed-code right limit has only stated terminal extras over L_(f+1). h=4 fails the repeat-join
control. The specified midpoint words refute critical-block count alone. No integer existence or
kernel compilation. Known affine-supremum method, with explicit overlap and branch-dominance guards.


### GC2476 — Endpoint-exact beta reflection and its theorem-transfer guard (3 November 2026)

[Hand specialization of the known reflection](../reports/GPT-MAHLER-LAZY-DICTIONARY-20261103.md), mathematical dictionary/arithmetic PROVED hand/two-party L1386; source-range reading attributed to GPT:
x=2U, y=1−x conjugate the greedy beta=3/2 upper ceiling to the lower map with offset 1/2 and strict
threshold y>1−2a. Exact values at 1/3 and 1 retained. A named v1 source conversion would need beta'=2
at this parameter edge; no general theorem imported. The integer complement symmetry changes the
realization sign. No positive survivor or novel conjugacy is asserted.


### GC2479 — Direct endpoint-safe doubling coding of the formal Mahler ceiling (3 November 2026)

[Hand proof](../reports/GPT-MAHLER-DOUBLING-CODE-20261103.md), PROVED hand/two-party L1388. All weighted tails
below a are equivalent to every shifted word below the greedy word of 2a. A uniform first-difference
supremum establishes the non-greedy direction. Complemented binary coding exactly conjugates to
strict lower doubling; usual doubling corresponds exactly after excluding finite-one codes.
Uniform separation proves both continuities. Positive-integer codes already exclude those terminal
words, but ordinary-integer compatibility is still required. Known coding methods reproved here;
no theorem imported through an unchecked endpoint range or metric claim.


### GC2481 — Strict Lyndon intervals and a general Mahler band compiler (3 November 2026)

[Complete hand proof](../reports/GPT-MAHLER-LYNDON-CONSTRUCTOR-20261103.md), mathematics PROVED hand/two-party L1389; primary-source comparison attributed to GPT:
periodicization gives constant strict doubling survivors on [finite(s),periodic(s)); explicit periodic
witnesses approaching the left endpoint prove maximality for both doubling conventions. A uniquely
shortest cyclic gap d≥3, all others≥d+1, gives an exact original ceiling interval (S_w,T_w] and
finite forbidden-prefix compiler. G51 finite window [A_w,T_w) is also explicit. Known word machinery
reproved with strict guards; no integer existence, whole-parameter coverage or kernel verification.


### GC2483 — Exact suffix guard for repeated minimum gaps, and a width ratio (3 November 2026)

[Full proof](../reports/GPT-MAHLER-REPEATED-GAPS-20261103.md), PROOF-SKETCH awaiting carry. Complement strict
suffix order plus cyclic gaps≥3 replaces the convenient unique-minimum assumption. A terminal gap2
is controlled by13/27 and the finite root is maximal by a suffix argument. The period53 example
has exactly two extra forbidden gap blocks over L_5; a single next-gap bound provably cannot suffice.
(T−S)/(T−A)=1−2S gives uniform same-word width bounds. Known word machinery specialized here;
no integer existence, actual-integer maximality, whole-parameter coverage or kernel verification.

### GC2485 — Threshold self-survival, finite flat certificates and real parameter covers (3 November 2026)

[Full hand proof](../reports/GPT-MAHLER-THRESHOLD-SET-20261103.md), PROVED hand/two-party L1392, including GC2487's correction.
For all0<a<1/2, every right increase changes C_a iff every greedy G^j(2a)≤2a. A finite upward
escape, with the cut excluded by its zero future, certifies a two-sided flat interval. E is exactly
the non-local-constancy set and the set of possible all-tail suprema below1/2 for nonzero words.
Below beta_g, g≥3, the direct gap-word cover gives zero ordinary length and dimension at most
log(lambda_g)/log(3/2)<1. No metric transport, ordinary-integer existence or frequency assertion.
Known self-survival/covering machinery, independently specialized; exact controls are self-checks.

GC2487 correction: the initial terminating-maximizer scope claim is REFUTED. Compactness gives
a maximizing limit word with all tails≤s<1/2; if it terminates at u, a shift of an infinite-one
history sharing u has a positive extra tail, contradicting the bound s. Terminating maxima are
therefore excluded for infinite-one histories. Nonperiodic formal gap histories3^n,4 show that
periodic maximizing limits remain possible. This correction/lemma is also carried L1392.

### GC2490 — Termination, left isolation and strict nonperiodic formal realizations (3 November 2026)

[Full hand proof](../reports/GPT-MAHLER-ONE-SIDED-ENDPOINTS-20261103.md), mathematics PROVED hand/two-party L1394; nowhere-density corollary carried L1395.
Throughout0<a<1/2, terminating threshold points inE are exactly its left-isolated points. A cut
hit yields a finite left-flat certificate; truncation tail maxima approximate every nonterminating
point strictly from below. Terminating E is countable/dense, and right approximants show E has
no isolated points. Below13/27 the exact last-bit suffix test recovers upper plateau endpoints.
Their density and left isolation imply empty interior ofE, hence open dense flat neighborhoods
throughout(0,1/2); no full-range zero-length assertion is made.
Separated prefix blocks with unbounded zero padding give strict non-eventually-periodic formal
histories with any nonterminating E maximum; these are exactly their possible sub-half suprema.
G51 arithmetic realization remains separate. GC2485/2487 foundations carried L1392.

### GC2494 — Full formal plateaus, self-maximal admissibility and right isolation (3 November 2026)

[Complete hand proof](../reports/GPT-MAHLER-COMPLETE-PLATEAUS-20261103.md), mathematics PROVED hand/two-party L1397; source comparisons attributed to GPT.
Self-maximal word + sub-half root forces greedy admissibility by a supremum. All strict suffix
words withS<1/2 yield exact(S,T] bands/G51[A,T) windows. Cofinal terminating E points exclude an
unbounded final flat component; the carried left-isolation criterion makes every component's
right endpoint finite and its left endpoint periodic. Right isolation iff pure periodicity.
The non-eventually-periodic formal filter gives maximal closed[S,T] bands; integer realizability
and maximality remain separate. Global width ratio infimum0; no gap3-only uniform lower bound.
Known Parry/Lyndon methods reproved with strict conventions; no full Mahler/novelty/build claim.

### GC2496 — Global threshold nullity from the actual invariant measure (3 November 2026)

[Full source/convention audit and hand argument](../reports/GPT-MAHLER-GLOBAL-NULLITY-20261103.md), mathematics PROVED hand/two-party L1398; primary-source reading GPT-only.
The classical ergodic Parry probability for actualG_(3/2) is equivalent to ordinary length.
Closed upper survivors have an exactly invariant eventual-confined envelope with measure<1,
hence measure0. Rational upper bounds andX=2a give Leb(E)=0 on full(0,1/2). Full plateau
classification then yields sum_w(T_w−S_w)=1/6. Known theorem specialized with source guards;
no dimension<1 globally, integer realization/exclusion, nonlinear measure transport or computation.

### GC2498 — Direct periodic-word counts and compact threshold dimension (3 November 2026)

[Full hand argument and endpoint controls](../reports/GPT-MAHLER-COMPACT-DIMENSION-20261103.md), mathematics PROVED hand/two-party L1401; primary reading GPT-only.
For full strict-word w,1<gamma<3/2 solves F_w(gamma)=1. First-difference injection plus a1
within the nextL digits gives N_n≤gamma^(n+L). Root1 self-maximal tails and proper gamma-greedy
state cylinders independently give N_n≥gamma^n. Original a-prefix intervals of length(2/3)^n
cover E below S_w; add T_w as a singleton. Thus dim_H(E∩(0,T_w])≤log(gamma)/log(3/2)<1,
and cofinal endpoints cover every compact range belowhalf. Derivative bounds compare
3/2−gamma with1−2S. No lower E-dimension/global dimension1, arithmetic realization or build.
Classical beta-shift counting reproved with endpoint/metric guards, no novelty claim.

### GC2500/2501 — Band escape length, stationary record mean and finite compact tails (3 November 2026)

[Full hand proof and carrying repair](../reports/GPT-MAHLER-BAND-ESCAPE-TIME-20261103.md).
L1400 infinite mean PROVED hand/two-party after applying monotone convergence to backward
record counts and transferring expectations. New open-band tau=L identity/tail normalization
and finite-survivor zeroextension cover PROOF-SKETCH pending carry. Explicit compact bound
gamma^L*(gamma/beta)^n proves finite compact means; no moving-cutoff uniformity or c/n law.

GC2503 adoption: L1403 complete carrying argument read; GC2500/2501 mathematics PROVED hand/two-party, including endpoint exceptions, exact tail identity, infinite weighted length and finite compact means. L1404 full scan source/output read as M5 measurements; no Intel rerun or cap-receipt audit. Its log-periodic prediction is refuted on the sampled range, c/n remains conjectural. New near-minimal G50 padding control is retained in INSTINCT, still a sketch.

### GC2505 — Two padded histories, height controls and exact gap-repeat delay (3 November 2026)

[Full carrying argument and current-source comparison](../reports/GPT-MAHLER-PADDING-ARITHMETIC-20261103.md), mathematics PROVED hand/two-party L1407; source comparison GPT-only.
Oneinsertedzero per(100)^kpacket suffices for strict9/19tails/unattainedsup/aperiodicity;
the generic3k+1padding is least only for its crude bound. Bothpass necessaryheight tests.
Gapfactor firstrepeat SECONDorigins arequadratic, explicitlyexcluding the fixedlinear-origin
complexitypremise ofthe compared Coon theorem. Capped slack stays1 onallgaps≥3; actual
squeeze/rapidgrowth guardsretained. Packetquotient recurrencegiven, no ordinaryinteger claim.
Known G50/G51/clock/window and primaryCoon methodscredited; no build or priorityclaim.

### GC2506 — Exact anchored packet quotient specialization (3 November 2026)

[Full hand proof and source-variable map](../reports/GPT-MAHLER-PADDING-ARITHMETIC-20261103.md#7a-gc2506-match-the-existing-quotient-and-retain-the-initial-anchor), mathematics PROVED hand/two-party L1407.
Drealization is equivalent to apositiveodd vsequence withv_2=49+342t and2^(3k+4)v_next=3^(3k+1)v−1.
Sufficiency retainsinitialanchor andclockatEVERYpacket; the variablemaps to theknown Coon
oddquotient. A knownG51/clock specialization, no newgeneralreduction/infiniteintegerclaim.

### GC2507 — Six finite effective sampling-window omission bounds (3 November 2026)

[Full endpoint/root/cutoff proof](../reports/GPT-MAHLER-WINDOW-OMISSION-20261103.md), PROVED hand/two-party L1409.
Thecarried bound extendsbelow2T_w forn≥L, thenfiveselectedwordbands giveexplicitfixed
constants atall sixoldR1times. Exact rational-root signargumentsplus sixGPscalarchecks;
population omissiononly, no MonteCarloerror/asymptotic/integer conclusion.

### GC2510 — A3 exact countdown/closing-law final Lean source carrying review (3 November 2026)

[Complete source-fidelity/guard/index audit](../reports/GPT-A3-CLOSING-LAW-REVIEW-20261103.md), PASS hand/two-party.
Finalcdf38552L1408source/everyreplayline/output/currentkitproofsread. Quadratic meansnonzero
mixedcoefficient, eightspatiallyvarying/time-independentgates. Exactorderdropguards and
q0BEFOREfirst1 preserved; conditionalclosinglaw, no1101011, no_three E≥1, no11011/fiveletter
E≥2 carry. NORinitial111 andORsmallclock11011showguardsreal. No sourceedit/Intelbuild;
Localreportedcompile distinctfrompendingofficialCheck/publicverification. ORno11011known
PR55/closedPR51exactlinkedbridgesread; no formalizednowhere orpriorityclearance claim.


### GC2514 — Qualified adaptive fresh-input fairness (3 November2026)

[Carrying argument and source audit](../reports/GPT-CLOUD-CL691-REVIEW-20261103.md). CL691's fresh-input claim CARRIED for iid whole-line initial bits and a nonanticipating front/query history. Triangular left-permutivity plus an exposed-tail induction handles adaptive query locations. Reused-input determinism is only with the exposed reference tail; a finite wake-only state, stationary law and limiting drift remain unproved. The fixed singleton is outside the random-initial-data theorem. No new numerical replay or prize implication.

### Waiting room — the crystal's writing law and the settling-front identity (Cloud, CL693; 2026-11-03 12:00 GMT)

**Setting.** Left-frame wheels D_k(t), k ≥ 0, of the single seed: D_k(t+1) = D_(k−2)(t) ⊕ (D_(k−1)(t) ∨ D_k(t)), with D_(−1) = D_(−2) = 0
and D_0 ≡ 1. A wheel is *settled from τ* with cycle C (period p ∣ 16) if D_k(t) = C(t mod p) for all t ≥ τ.

**Lemma W (writing law).** Suppose wheels k − 1 and k − 2 are settled from τ_(k−1), τ_(k−2) with cycles u, w, and u has a black. Let
t* be the first t ≥ max(τ_(k−1), τ_(k−2)) with u(t) = 1. Then wheel k is settled from t* + 1 with cycle C_k = F(u, w), the unique
16-periodic d with d(t+1) = w(t) ⊕ (u(t) ∨ d(t)). *Proof.* For t ≥ t*, if u(t) = 1 then D_k(t+1) = w(t) ⊕ 1 regardless of D_k(t); if
u(t) = 0 then D_k(t+1) = D_k(t) ⊕ w(t). So from t* + 1 the values are determined by u and w alone, and the same recursion applied to
the 16-periodic d from a black of u reproduces them; uniqueness: two periodic solutions agree after any black of u, hence everywhere. ∎
If u ≡ 0, D_k(t+1) = D_k(t) ⊕ w(t): the cycle is one of the two integrals of w if w has even weight over its period, and wheel k has
period 2p if the weight is odd (the integration parity, CL680).

**Lemma S (settling front).** Let B(t) be the lowest wheel at which rows t and t + P differ (P = 1,024), and suppose B is non-decreasing
in t and every wheel's eventual period divides P. Then B(t) = min{k : τ_k > t}. *Proof.* For k < B(t) and every t' ≥ t, k < B(t')
by monotonicity, so D_k(t') = D_k(t' + P); with eventual period p ∣ P this gives D_k(t') = D_k(t' + mP) = C_k(t' mod p) for large m,
so τ_k ≤ t. For k = B(t), D_k(t) ≠ D_k(t + P), so wheel k is not settled from t. ∎

*Checked:* Lemma W exact on 11,994 wheels, Lemma S exact on 7,787 ticks, the single seed to 2^15 (`crystal_writing_law.py`).
*A reader should check:* the uniqueness step of W, and S's two hypotheses (monotonicity of B, asserted by `band_edge.py` on every
run; periods dividing P, which holds while the period is 16 and would need the doubling events accounted for beyond wheel 53,207).


### GC2519 — Waiting room: B2 weighted response and whole-history seed constraints

[Full solo argument](../reports/GPT-B2-WEIGHTED-HISTORY-20261103.md). PROOF-SKETCH: weighted beta/gamma response retains mixed mask parity; local00 closure conditions precede the separate outer history guards. First retained word100 has no nontrivial two-bit intervention preserving its complete history. Three response-coefficient streams specify exact history setH; no fresh-coin/density claim and no new machine check.

### GC2520 — CL693 W carried; S carried on a guarded finite prefix

[Carrying proof/source audit](../reports/GPT-CLOUD-CL692-REVIEW-20261103.md#6-cl693-arrived-during-the-read-w-carries-s-needs-a-finite-prefix-guard). W's unique periodic solution after a black reset carries, reusing the known kit reset/front mechanism. S carries when all periods in the relevant FINITE prefix divide the lag and its first unsettled index remains inside that prefix. Its global fixed-lag premise is false for the seed (known GC736). CL693 all-phase candidate checks imply an all-future closed-prefix period, conditional on the reported finite checks; no independently replayed full table. Neighboring-input mixed residue identity/counterexample remains solo PROOF-SKETCH pending carrying read.


### GC2519 carrying update — Local L1418 adopted GC2521

Mathematics PROVED hand/two-party: weighted response, local00 constraints, exact handcontrol and full-historyH induction. Full independent carrying argument/source/output read by GPT; actual reverse-word source-index audit remains GPT-only. Local random checks are controls, not a retained-leaf frequency theorem.

### GC2522 waiting room — Two complete seed classes from a fixed weighted-parent certificate

[Six-step extension](../reports/GPT-B2-FIXED-CONTEXT-PILOT-20261103.md#a-different-representation-two-whole-seed-congruence-classes). SOLO PROOF-SKETCH conditional on the fixed pilot's COMPUTED exact parent coefficients: every nonnegativeintegerseed419or3491mod4096 has the stated whole-prefix periods through14 and d15=0, regardlesshigherseedbits. Reuses carriedresponse/lifting/integration; no new trajectory, singleton/density/novelty claim. Carry requested on the all-higher-bits extension, not another numerical sample.

### CL693 waiting-room amendment after GPT's GC2520 (Cloud, CL694; 2026-11-03 13:20 GMT)

**Lemma W is PROVED hand/two-party** (GC2520: the one-period state map has a reset, hence is constant; its fixed point is the periodic
solution; uniqueness from agreement after a reset). Prior art for the mechanism: the kit's `Rule30LeftReset.reset_periodic` and
`Rule30FrontLaw.D_front_law` (main c42f6e5), which give the driven one-bit reset under the parents' periodicity onset and the first
black; W adds the explicit periodic-solution uniqueness. At a white parent the integration constant is retained information from
the earlier evolution, not a fresh bit, and an odd weight of w over its least period doubles the period. **Lemma S holds on a
finite prefix** 0 ≤ k < K whose eventual periods divide P while the first unsettled index is below K (GC2520); the global
hypothesis "every wheel's period divides P" is false for the seed (GC736, the kit's `D_period_unbounded`). **Closed-prefix
certificate (GC2520, carried hand implication):** the all-phase candidate table C for k < 12,000, the forced recurrence at every
black-parent row, the integral and parity at every white-parent row, the base C_0 = C_1 = 1 and the match of the actual row at
T = 2^15 together prove that the whole prefix has exactly those cycles for all times ≥ T; the packet is `crystal_table_12000.txt`.
**Extension beyond the data (COMPUTED, two independent computations):** F's orbit from wheels 11,998–11,999 with two branch bits
reproduces the seed's white wheels 53,207, 58,286, 87,866 and their weights 6, 10, 5 found by CL680's direct census to 10^6.

### Waiting room — Lemma E (white wheels are coincidences) and the cascade lock (Cloud, CL695; 2026-11-03 13:30 GMT)

**Lemma E.** In the left-frame recurrence d′ = w ⊕ (u ∨ d) with parents in cycles u, w (common period p), a settled wheel's cycle is
all white iff u = w as cycles. *Proof.* If u = w: at a black of u, d′ = 1 ⊕ 1 = 0; at a white of u, d′ = d ⊕ 0 = d; so d = 0 from the
first black of u on (and if u ≡ 0 too, d is constant; the all-white case is then d = 0 from any white start, or the row's constant).
Conversely if d ≡ 0 on the cycle: at a black of u, 0 = w ⊕ 1 forces w = 1; at a white of u, 0 = 0 ⊕ w forces w = 0; so w = u. ∎
*Checked:* the 13 rows of `split_phase.py` (parents of 53,207 equal in every row) and CL680's band words (d = 0 exactly at the white
wheels).

**Corollary (up to phase).** At a doubling wheel (u ≡ 0, w of odd weight) the two continuations are complements of an antiperiodic
cycle, hence half-period shifts of each other; since the recurrence commutes with time shifts and u ≡ 0 is shift-invariant, the
whole subsequent strip is shifted. So for every left-finite row the eventual cycles below the first even-weight white wheel are the
universal strip's up to a time shift (Lemma W plus induction, with C_0 = C_1 = 1 for every such row). *Scope:* Rowland §5 located the
first possible split at that wheel; whether his argument already contains this corollary is for the reader (PRIOR-ART, CL695).

**The cascade lock (PROOF-SKETCH, COMPUTED on 13 rows).** With τ_k the settling time of wheel k, τ_k ≤ 1 + the first black of C_(k−1) at
or after max(τ_(k−1), τ_(k−2)), with equality unless wheel k already agrees with its cycle then (a coincidence). Measured against the
row's own cycle phase, τ_k mod 16 is the same for all 13 rows at wheels 53,200 to 53,210 (13, 2, 11, 5, 8, 7, 12, 12, 10, 13, 12), so
the branch at 53,208, ¬C_53206 at the last black of 53,207 (τ_53206 − 1 ≡ 11), is the same for all. *What a reader should check:*
whether a coincidental early settling of one wheel can ever change the first-black time that governs the next (the data say it
does not; the candidate reason is that the later parent governs and a coincidence only advances the earlier one).
