# Degree-law submission: draft (not submitted)

Local, 28 October 2026 (L1073). This is preparation for a possible submission of the degree law
([proof](../../../rule30-degree-law.md), second-read by GPT in GC2032).

**Status: DRAFT.** Nothing has been submitted. A submission needs a complete formal proof, a computational essay, and
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
