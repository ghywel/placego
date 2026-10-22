# Group coarsening with any-realization margin inheritance (Cloud CL508/515; second-read by GPT, MI619)

*Short proofs restated from the running text. Derived from [PROOFS.md](../PROOFS.md), entry "C.9 Group coarsening
with any-realization margin inheritance (Cloud CL508/515; second-read by GPT, MI619)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** PROVED for lemma(a)–(c), under the stated hypotheses,.

## In plain words

**A least-slack group can be merged without losing the precise child margins.**
Coarsening the other bins preserves the original cut conditions. Every
actual realization of the least-slack group then leaves the outside bins
with a shifted per-number margin at least their actual hole count.

**Why it matters.** This removes a hidden canonical-choice assumption in
that inheritance step. It still requires the smaller instances to be
feasible, including top-tight coarsenings and any exceptional children.

## The formal statement and proof

*Status:* PROVED for lemma(a)–(c), under the stated hypotheses,
by Cloud's hand argument and GPT's targeted carrying read,2026-10-22.
This verifies coarsened cut admission and the exact shifted child margin.
It does not prove the top-tight lemma or solve base exceptions. CL515's
correction is part of the adopted scope; the original pair-branch claim
is not adopted. The original candidate below is retained as provenance.

**Carrying check, GPT.** A group containing the merged bin is exactly an
original proper group; for a proper outside child group K, G union K is
still proper, so subtracting least slacks gives the g*r term. Actual hole
count is g+h-b-(M-c); shifting targets subtracts b*r and gives exactly
mu'=h'+(mu-h)+(M-c). No geometry of a canonical R is used. At h=0
reflection swaps complementary slacks because the pool is a full interval;
that argument is not imported at h>0. Fewer-bin feasibility/exception
control remain premises of the global induction. This is MI368's known
margin computation combined with the requested coarsening application,
not a new GPT theorem or a new computational run.

### Cloud CL508 — Coarsening reduction: H(h) reduces to its co-singleton case (Cloud, 2026-10-22; waiting room)

*Status:* hand proof, single-party (the overnight arrangement, CL481); a second reader is needed before adoption. Step
(b) is MI368's computation with a group in place of a singleton. The new step is the use of (a), coarsening (GPT's device in MI576, there applied to G315), which removes the
pair/triple branch that CL439 expected to need G316's staircase. Machine support (tier 1, single-party):
- `descent_every.py`: every realization of a least-slack singleton or pair keeps the child in its family, with 0 bad
  out of 20,396 and 2,972 realizations;
- `kholek.c`: coarsened instances (one big bin) have no H(h) failures for k = 3, sizes (3,3,6..9), (3,4,7), h ≤ 6, and
  for k = 4, sizes 333X, h ≤ 6 (CL503).

**Setting.** S = [0, M] ∖ H with |H| = h, n = |S| = M + 1 − h, and k bins of sizes c_i ≥ 3 summing to n, with targets
u_i summing to ΣS. The instance is in H(μ), μ ≥ h, if u_J ≥ L(r_J) + μ·r_J for every proper nonempty group J, where
r_J = Σ_{i∈J} c_i and L(r) = r(r − 1)/2. Its slack is σ_J = u_J − L(r_J) − μ·r_J ≥ 0.

**Lemma.** Let G be a proper group of least slack with s bins, 1 ≤ s ≤ k − 2, and g = r_G.
- (a) The coarsened instance I_G (the bins of G, plus one bin B of size n − g ≥ 6 and target ΣS − u_G) is in H(μ) on S.
- (b) For ANY partition of S realizing I_G, let R be the union of G's sets and b ≤ c the least and greatest elements of
  S ∖ R. Shifted by −b, the k − s bins outside G form an instance on S ∖ R ⊆ [b, c] with h′ = (c − b + 1) − (n − g)
  holes, and it is in H(μ′) with μ′ = h′ + (μ − h) + (M − c) ≥ h′.
- (c) Consequently, if I_G and that child are both feasible, so is the instance.

**Proof.**
- (a) A proper nonempty group of I_G either omits B, and is then a nonempty union of G's bins, or contains B and
  omits some bin of G. In both cases it is a union of original bins that is neither empty nor everything, hence an
  original proper group. Its cut condition is the original one, with the same size and target.
- (b) Let K be a proper nonempty group of the bins outside G, with r = r_K. Then G ∪ K is a proper group of the
  instance (it omits a bin outside K), so σ_{G∪K} ≥ σ_G. Since L(g + r) − L(g) = L(r) + g·r,
  u_K = u_{G∪K} − u_G ≥ L(r) + (g + μ)·r.
  Counting S ∖ R in [b, c] gives h′ = (c − b + 1) − (n − g) = g + h − b − (M − c), using n = M + 1 − h. So the shifted
  target is u_K − b·r ≥ L(r) + (g + μ − b)·r = L(r) + μ′·r with μ′ = h′ + (μ − h) + (M − c) ≥ h′. ∎
- (c) Is immediate.

**Consequence.** By induction on k, H(μ) instances whose least slack is attained by some group of at most k − 2 bins
reduce to two instances with fewer bins, each in its own H family:
- the coarsened one, on the same pool, has a big bin;
- the child has h′ holes.

The irreducible instances are those whose least slack is attained ONLY by co-singletons, i.e. groups of k − 1 bins (a
top-tight bin).

At h = 0 the family H(0) on [0, M] is reflection-symmetric: x ↦ M − x maps the slack of J to the slack of its
complement, because L(n) − L(n − r) = rM − L(r) when n = M + 1. So a least-slack co-singleton becomes a least-slack
singleton after reflection, and every H(0) instance reduces.

**Hence SS3 for every k (h = 0) follows from:**
- (i) H₂, the subset-sum spectrum lemma (G318 for at most three deletions);
- (ii) H_j(h) with h ≥ 1 for j < k, in particular its co-singleton case;
- (iii) control of the base exceptions (H₃, H₄ equal-sum cores; CL503–504).

The co-singleton case at h ≥ 1 is CL443's wall. In the five-bin samples of CL505, 55% of H₅(1) instances are of this
kind.

**Correction (Cloud, CL515, 2026-10-22 04:04 BST).** The lemma (a)–(c) stands, but the consequence overstated what it
removes. For s ≥ 2 the coarsened instance I_G has least slack σ_G, because G is one of its groups and is globally
least. In I_G, G is the complement of the single bin B, so **I_G is itself top-tight, with the big bin B top-tight**.
So:
- only singleton-least instances (s = 1) reduce to H₂ plus a child;
- pair- or triple-least instances reduce to a child plus a top-tight instance with one big bin.

The conclusion "SS3 for every k follows from H₂ plus the top-tight lemma (all smaller k, h ≥ 1)" is unchanged, by
induction on k. But CL439's pair/triple branch does not disappear; it becomes the top-tight lemma for instances with a
bin of size ≥ 6. At h = 0 reflection still reduces everything.
