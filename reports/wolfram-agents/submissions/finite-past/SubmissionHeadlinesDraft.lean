module
public import Ruliology.CellularAutomata.Rule30Prize
public import FiniteParentCriterionDraft
public import FinitePastCountDraft

/-!
UNCOMPILED public headline wrappers, GC2292. The four proof modules are local
preparation files, not verifier imports. A later self-contained assembly must
carry their full bodies and import the official Rule30Prize statements.
Known G121/G122/L077 and Karttunen's 2016 OEIS ancestry records are credited.
No official replay, source acceptance, notebook build or posting is claimed.
-/
@[expose] public section
namespace Rule30Submission
open Ruliology.CellularAutomata.Rule30Realization
open Ruliology.CellularAutomata.Rule30FinitePastDraft

/-- Unique finite root and age, with the physical support-depth bound. -/
theorem finite_root_age {y : Int → Bool} {l r : Int} (hy : Span y l r) :
    ∃ x n, Root x ∧ evol x n=y ∧ 2*n ≤ (r-l).toNat ∧
      ∀ x' n', Root x' → evol x' n'=y → x'=x ∧ n'=n :=
  finite_root_decomposition hy

/-- A test for an actual predecessor with the stated white-right boundary. -/
theorem finite_parent_test {p y : Int → Bool} {l r : Int}
    (hy : Span y l r) (he : evol p 1=y)
    (hr : ∀ i, r≤i → p i=false) :
    FiniteNonzero p ↔ y (l+1)=true ∧ p (l+1)=true :=
  finite_white_parent_iff hy he hr

/-- Both injection and the exact range, so the image statement is a bijection. -/
theorem normalized_ancestor_bijection (w n : Nat) :
    (∀ x y : Int → Bool, Normal w x → Normal w y →
      normalizedImage n x=normalizedImage n y → x=y) ∧
    (∀ y : Int → Bool, (∃ x, Normal w x ∧ normalizedImage n x=y) ↔
      Normal (w+2*n) y ∧ Past n y) := by
  constructor
  · intro x y hx hy he
    exact normalizedImage_injective hx hy he
  · exact normalizedImage_range w n

/-- The normal-word enumeration is exhaustive and duplicate-free, with exact size. -/
theorem finite_word_enumeration (w : Nat) :
    (allRows w).Nodup ∧ (∀ y : Int → Bool, y ∈ allRows w ↔ Normal w y) ∧
      (allRows w).length=widthCount w :=
  ⟨allRows_nodup w,mem_allRows w,allRows_length w⟩

/-- Counts actual finite-parent words, with no unproved enumeration assumption. -/
theorem finite_parent_enumeration (w : Nat) :
    (parentRows w).Nodup ∧
    (∀ y : Int → Bool, y ∈ parentRows w ↔ Normal w y ∧ Past 1 y) ∧
    (parentRows w).length=(if 3≤w then widthCount (w-2) else 0) :=
  ⟨parentRows_nodup w,mem_parentRows w,parentRows_count w⟩

theorem finite_parent_count {w : Nat} (hw : 4≤w) :
    (parentRows w).length=2^(w-4) :=
  parentRows_count_ge_four hw

theorem finite_parent_small_widths :
    (parentRows 1).length=0 ∧ (parentRows 2).length=0 ∧ (parentRows 3).length=1 :=
  parentRows_count_small

end Rule30Submission
