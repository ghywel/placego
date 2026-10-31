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
