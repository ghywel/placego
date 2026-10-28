# Degree-law submission: withdrawn (prior art in the kit)

Local, 28 October 2026 (L1073, L1077). This was preparation for a possible submission of the degree law
([proof](../../../rule30-degree-law.md), second-read by GPT in GC2032).

**Status: NOT FOR SUBMISSION (L1077).** The formal proof is complete (`degree_law`, `degree_bound`,
`degree_attained`; 1,271 lines, 97 theorems, no `sorry`, standard axioms). But the kit already has the theorem:
`equivalents/Rule30Equivalents/AlgebraicDegree.lean`, added on 2026-10-18 (kit commit cb53064), proves in Lean with
Mathlib that the degree is exactly 2t − 1 for t ≥ 2 (`isGreatest_card_coef_center`) and that the top monomial is
unique for t ≥ 3 (`eq_Icc_of_coef_ne_zero`). Under the portal's novelty rule ("do not submit what is there, or one
more instance of it") this is a known result reproved here, not a submission. No kit pull request was opened and
nothing was uploaded.

**Earlier status (kept for the record): DRAFT, formal proof in progress.** Nothing has been submitted. A submission needs a complete formal proof, a computational essay, and
the owner's explicit consent for that submission, sent through the owner's Wolfram ID.

## What is here

`Rule30DegreeLawStatement.lean` gives the formal statement in core Lean. The kit is now Mathlib-free and uses the
module system. The statement has three parts:
- *Rows:* bit masks over the 2t + 1 light-cone cells.
- *Coefficient:* by the Möbius formula, the coefficient of a monomial is the parity of the number of sub-masks whose
  t-step evolution is black at the apex.
- *Theorem `degree_law`:* for t ≥ 3, the top monomial (cells −t+2 … t) has coefficient 1, and every other monomial
  with at least 2t − 1 cells has coefficient 0.

It type-checks against the kit's toolchain (Lean v4.35.0, `lake env lean`). The main theorem is still `sorry`. Two
t = 3 sanity examples are proved by `decide +kernel`, which adds no axiom and is not `native_decide`. An evaluation
gives coefficient 1 for the top monomial at t = 1 … 6. The statement covers t ≥ 3. At t = 2 there are two top
monomials, and that case would be a separate small lemma.

## Formal proof: progress (L1074, 28 October 2026)

`Rule30DegreeLaw.lean` is 524 lines of core Lean, with 49 theorems. It contains no `sorry` and no
`native_decide`, uses only the standard axioms (propext, Classical.choice, Quot.sound), and type-checks against the
kit's Lean v4.35.0. The coefficient of a monomial over a list of cells is `sumOver S F`: the XOR of F over rows
supported in S, defined by discrete derivatives.

**Proved:**

| Lemma | Content |
|---|---|
| Foundations | light cone; derivative laws (commutation, independence, XOR, linear cells, product against an ignored factor); sum laws (XOR, vanishing on an ignored cell, permutation invariance, erase) |
| Lemma 1 (`deriv_apex`) | ∂ of the apex in cell t = the white-anti-diagonal indicator `aw t x t`, by an exact damage invariant |
| Left permutivity (`left_permutive`, `evo_linear`) | the leftmost cone input enters by exact XOR |
| Elimination (`sumOver_elim`) | pivots summed out leftmost first, each a single derivative (`deriv_aw_step`) |
| (A) `coeff_with_left_cell` | monomials with −t and another cell have coefficient 0 |
| (B) `coeff_with_right_cell` | a monomial containing t reduces to the white anti-diagonal |
| (C1) `coeff_all_pivots` | all pivots plus a nonempty rest gives 0 |
| (C2) `coeff_missing_pivot` | a missing pivot with a cell left of it gives 0 |
| (D) `coeff_without_ends` | the candidate [−t+1, t−1] gives 0 |

**(E) The main parity is formal (L1076):** `main_parity : ∀ t ≥ 2, A t = true`. The file is now 905 lines with 78
theorems; it contains no `sorry`, and `#print axioms main_parity` lists only propext, Classical.choice and
Quot.sound. The route is real-space, with no solved system:
- the damage behind the light-speed front is an XOR along the right diagonal (`behind_front`);
- two factors linear in one pivot combine (`deriv_two_linear`);
- translation and clearing identify the next instance (`sumOver_shift`, `sumOver_clear`);
- this gives `recA` and `recB`, A(n) = ⊕_(i<n−1) (A(n−1) ⊕ B(n−1, i)) and B(n, k) = ⊕_(i<k) (the same terms), with
  B(·, 0) = 0;
- the base values A(2) and B(2, 1) are checked by kernel `decide`, and the joint induction (`AB_true`) gives A ≡ 1.

**(F) The assembly is formal (L1077).** A Nodup list of at least 2t − 1 cells is split by Nodup counting
(`length_le_of_sub`, `all_mem_of_length`, `all_but_one`) and a permutation into pivots and the rest
(`perm_split`). The headlines:
- `coeff_top`, `coeff_outside`, `coeff_not_top`;
- combined: `degree_law` (t ≥ 3, an iff), `degree_bound` (t ≥ 2, including the t = 2 case) and `degree_attained`.

`#print axioms` on all three lists only propext, Classical.choice and Quot.sound (`coeff_outside` needs no
Classical.choice). "Coefficient" is `sumOver S (apex t)`, the iterated derivative at the white row; that this is the
ANF coefficient is the Möbius formula, which the file does not prove. The kit's module defines the coefficient as
the Möbius sum and proves the link (`coef_insert`).

**Superseded plan for (E), kept for the record:**
- **(E) The main parity:** the coefficient of [−t+2, t−1] in `aw t · t` is 1. This is the z-frame induction, the
  hardest part. A real-space route is visible:
  - differentiate first in the leftmost free cell −t+2, which only the last condition reads. This gives an XOR of
    NOTs along the right diagonal from (0, −t+3);
  - two factors linear in the same pivot combine as ∂_p(¬(x_p⊕g) ∧ ¬(x_p⊕h) ∧ R) = R ∧ ¬(g⊕h).

  That should give the Lemma 3/4 recursions without an explicit solved system.
- **(F) Assembly:** a Nodup list of at least 2t − 1 light-cone cells is one of the cases above (Perm witnesses from
  membership), giving the headline in list form.

## What a formal proof needs

The three carrying steps of the hand proof, in core Lean with `List` counting, in the kit's style:
1. **Rightmost derivative.** The coefficient of a mask containing the rightmost cell equals the parity of the count of
   rows keeping the anti-diagonal white (damage at light speed).
2. **Triangular pivots.** Counts are powers of two when every pivot is available, or when a free cell lies left of a
   missing pivot. The one candidate without the rightmost cell needs the weight argument.
3. **The z-frame induction.** The two damage recursions (Lemmas 3 and 4), and the joint parity induction.

The effort is substantial, probably well over a thousand lines without Mathlib's finite-set and big-operator
libraries. The equivalence between the mask-count coefficient and the ANF is the Möbius formula. The headline is
stated directly in count form, so the formal statement does not need it.

## Before submitting

- **Novelty:** Deva's 2026 SSRN paper, "Algebraic Obstruction and Dual-Flow Consistency in Rule 30" (DOI
  10.2139/ssrn.5908722), reportedly claims linear degree growth. Its abstract page is behind a CAPTCHA and has not been
  read. The essay must not claim novelty unless that comparison is done. See L1073.
- **The essay:** the computational evidence (t ≤ 12, `centre_anf_degree.py`) and the lemma checks
  (`degree_law_check.py`), with the scope: a variable-input theorem, not a statement about the single-seed column.
