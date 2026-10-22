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
