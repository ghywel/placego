import Mathlib

/-!
# Uniform ancestry capture and band exit (Local, L1287, 2026-11-01)

GPT's GC2357, carried by Local in L1284, formalised. A configuration `x0 : ℤ → Bool` has a leftmost black cell `e`.
Marks start at `e` at time 0 and pass along every black-parent edge (`mark`). Diagonal `k` at time `t` is the cell
`e - t + k` (left-edge coordinates, as in JenPow2.lean), `D k t` its colour and `M k t` its mark.

The rule is any `f : Bool → Bool → Bool → Bool` with `f 0 0 0 = 0`, `f 0 0 1 = 1`, `f 1 0 0 = 1` (the F1 class
of L1285; `rule30` is one, `rule30_edgy`). Those three entries are all the proof uses.

* `edge`: the leftmost black cell moves left one cell a step, and everything left of it is white.
* `pair`: diagonals `n, n+1` are not both white for `n+1` consecutive times (GC2357's 17.2).
* `capture`: every black cell on diagonal `j` is marked from time `C j`, with `C 0 = 0`, `C 1 = 1`,
  `C (j+2) = C (j+1) + (j+1)`, that is `C j = 1 + j (j - 1) / 2` (`C_closed`).
* `exit`: from any time `t0`, within `C (D+2) + D + 1 = (D+2)(D+3)/2` steps a marked cell lies beyond diagonal `D`.
* `unbounded`: so the marked front is beyond every `D` at arbitrarily late times (the premise of L1283's lock).

How to check: copy into the formal-conjectures checkout used for JenPow2.lean (Mathlib available) and run
`lake env lean LocalScratch/Capture.lean`; the `#print axioms` lines must list no `sorryAx`.
-/

set_option Elab.async false

namespace Capture

/-- The three table entries the argument uses. -/
structure Edgy (f : Bool → Bool → Bool → Bool) : Prop where
  h000 : f false false false = false
  h001 : f false false true = true
  h100 : f true false false = true

def rule30 (a b c : Bool) : Bool := xor a (b || c)

theorem rule30_edgy : Edgy rule30 := ⟨by decide, by decide, by decide⟩

def step (f : Bool → Bool → Bool → Bool) (x : ℤ → Bool) : ℤ → Bool :=
  fun i => f (x (i - 1)) (x i) (x (i + 1))

def ev (f : Bool → Bool → Bool → Bool) (x0 : ℤ → Bool) : ℕ → ℤ → Bool
  | 0 => x0
  | t + 1 => step f (ev f x0 t)

lemma ev_succ (f : Bool → Bool → Bool → Bool) (x0 : ℤ → Bool) (t : ℕ) (i : ℤ) :
    ev f x0 (t + 1) i = f (ev f x0 t (i - 1)) (ev f x0 t i) (ev f x0 t (i + 1)) := rfl

/-- Marks: the edge cell at time 0, then along every black-parent edge. -/
def mark (f : Bool → Bool → Bool → Bool) (x0 : ℤ → Bool) (e : ℤ) : ℕ → ℤ → Bool
  | 0 => fun i => decide (i = e)
  | t + 1 => fun i => ev f x0 (t + 1) i && (mark f x0 e t (i - 1) || mark f x0 e t i || mark f x0 e t (i + 1))

/-- Diagonal `k` at time `t`. -/
def D (f : Bool → Bool → Bool → Bool) (x0 : ℤ → Bool) (e : ℤ) (k t : ℕ) : Bool := ev f x0 t (e - t + k)

/-- The mark of diagonal `k` at time `t`. -/
def M (f : Bool → Bool → Bool → Bool) (x0 : ℤ → Bool) (e : ℤ) (k t : ℕ) : Bool := mark f x0 e t (e - t + k)

section
variable (f : Bool → Bool → Bool → Bool) (hf : Edgy f) (x0 : ℤ → Bool) (e : ℤ)
  (he : x0 e = true) (hl : ∀ j < e, x0 j = false)

include hf he hl in
lemma edge (t : ℕ) : ev f x0 t (e - t) = true ∧ ∀ j < e - t, ev f x0 t j = false := by
  induction t with
  | zero => simpa using ⟨he, hl⟩
  | succ t ih =>
    obtain ⟨h1, h2⟩ := ih
    constructor
    · rw [ev_succ]
      have a1 : ev f x0 t (e - ↑(t + 1) - 1) = false := h2 _ (by push_cast; omega)
      have a2 : ev f x0 t (e - ↑(t + 1)) = false := h2 _ (by push_cast; omega)
      have a3 : e - ↑(t + 1) + 1 = e - ↑t := by push_cast; ring
      rw [a1, a2, a3, h1, hf.h001]
    · intro j hj
      rw [ev_succ]
      have b1 : ev f x0 t (j - 1) = false := h2 _ (by push_cast at hj; omega)
      have b2 : ev f x0 t j = false := h2 _ (by push_cast at hj; omega)
      have b3 : ev f x0 t (j + 1) = false := h2 _ (by push_cast at hj; omega)
      rw [b1, b2, b3, hf.h000]

include hf he hl in
lemma D_zero (t : ℕ) : D f x0 e 0 t = true := by
  unfold D; simpa using (edge f hf x0 e he hl t).1

include hf he hl in
lemma ev_left (t : ℕ) (i : ℤ) (hi : i < e - t) : ev f x0 t i = false :=
  (edge f hf x0 e he hl t).2 i hi

include hf he hl in
lemma mark_left (t : ℕ) (i : ℤ) (hi : i < e - t) : mark f x0 e t i = false := by
  cases t with
  | zero =>
    unfold mark
    simp only [Nat.cast_zero, sub_zero] at hi
    simp [ne_of_lt hi]
  | succ t =>
    unfold mark
    rw [ev_left f hf x0 e he hl (t + 1) i hi]
    rfl

lemma D_succ2 (k t : ℕ) :
    D f x0 e (k + 2) (t + 1) = f (D f x0 e k t) (D f x0 e (k + 1) t) (D f x0 e (k + 2) t) := by
  unfold D
  rw [ev_succ]
  congr 2 <;> push_cast <;> ring

include hf he hl in
lemma D_succ1 (t : ℕ) : D f x0 e 1 (t + 1) = f false (D f x0 e 0 t) (D f x0 e 1 t) := by
  unfold D
  rw [ev_succ]
  rw [ev_left f hf x0 e he hl t (e - ↑(t + 1) + ↑(1 : ℕ) - 1) (by push_cast; omega)]
  congr 2 <;> push_cast <;> ring

lemma M_succ2 (k t : ℕ) :
    M f x0 e (k + 2) (t + 1) =
      (D f x0 e (k + 2) (t + 1) && (M f x0 e k t || M f x0 e (k + 1) t || M f x0 e (k + 2) t)) := by
  unfold M D
  simp only [mark]
  have h1 : e - ↑(t + 1) + ↑(k + 2) - 1 = e - ↑t + ↑k := by push_cast; ring
  have h3 : e - ↑(t + 1) + ↑(k + 2) + 1 = e - ↑t + ↑(k + 2) := by push_cast; ring
  have h2 : e - ↑(t + 1) + ↑(k + 2) = e - ↑t + ↑(k + 1) := by push_cast; ring
  rw [h3, h1, h2]

include hf he hl in
lemma M_succ1 (t : ℕ) :
    M f x0 e 1 (t + 1) = (D f x0 e 1 (t + 1) && (M f x0 e 0 t || M f x0 e 1 t)) := by
  unfold M D
  simp only [mark]
  rw [mark_left f hf x0 e he hl t (e - ↑(t + 1) + ↑(1 : ℕ) - 1) (by push_cast; omega)]
  have h3 : e - ↑(t + 1) + ↑(1 : ℕ) + 1 = e - ↑t + ↑(1 : ℕ) := by push_cast; ring
  have h2 : e - ↑(t + 1) + ↑(1 : ℕ) = e - ↑t + ↑(0 : ℕ) := by push_cast; ring
  rw [h3, h2]
  simp

include hf he hl in
lemma M_zero (t : ℕ) : M f x0 e 0 t = true := by
  induction t with
  | zero => simp [M, mark]
  | succ t ih =>
    unfold M
    simp only [mark]
    have h1 : e - ↑(t + 1) + ↑(0 : ℕ) = e - ↑(t + 1) := by push_cast; ring
    rw [h1, (edge f hf x0 e he hl (t + 1)).1]
    have h2 : e - ↑(t + 1) + 1 = e - ↑t + ↑(0 : ℕ) := by push_cast; ring
    rw [h2]
    unfold M at ih
    rw [ih]
    simp

include he in
lemma M_imp_D (k t : ℕ) (h : M f x0 e k t = true) : D f x0 e k t = true := by
  cases t with
  | zero =>
    unfold M mark at h
    simp only [Nat.cast_zero, sub_zero, decide_eq_true_eq] at h
    unfold D
    simp only [Nat.cast_zero, sub_zero]
    rw [h]; exact he
  | succ t =>
    unfold M at h
    rw [mark] at h
    unfold D
    exact (Bool.and_eq_true _ _ |>.mp h).1

/-! ### The white-pair window (17.2) -/

include hf he hl in
lemma pair (n : ℕ) : ∀ T : ℕ, ∃ s, s ≤ n ∧ (D f x0 e n (T + s) = true ∨ D f x0 e (n + 1) (T + s) = true) := by
  induction n with
  | zero =>
    intro T
    exact ⟨0, le_refl 0, Or.inl (D_zero f hf x0 e he hl (T + 0))⟩
  | succ n ih =>
    intro T
    by_contra hcon
    have hall : ∀ s, s ≤ n + 1 → D f x0 e (n + 1) (T + s) = false ∧ D f x0 e (n + 2) (T + s) = false := by
      intro s hs
      constructor
      · cases h : D f x0 e (n + 1) (T + s)
        · rfl
        · exact absurd ⟨s, hs, Or.inl h⟩ hcon
      · cases h : D f x0 e (n + 2) (T + s)
        · rfl
        · exact absurd ⟨s, hs, Or.inr h⟩ hcon
    obtain ⟨s, hs, hor⟩ := ih T
    rcases hor with h | h
    · have h2 := (hall (s + 1) (by omega)).2
      rw [show T + (s + 1) = T + s + 1 by ring, D_succ2, h, (hall s (by omega)).1, (hall s (by omega)).2,
        hf.h100] at h2
      exact Bool.noConfusion h2
    · exact Bool.noConfusion ((hall s (by omega)).1 ▸ h)

/-! ### Capture -/

/-- Diagonal `k` is captured from time `T`: every black cell there is marked. -/
def Cap (k T : ℕ) : Prop := ∀ t, T ≤ t → D f x0 e k t = true → M f x0 e k t = true

lemma Cap_mono (k T T' : ℕ) (h : T ≤ T') (hc : Cap f x0 e k T) : Cap f x0 e k T' :=
  fun t ht => hc t (le_trans h ht)

/-- A black captured predecessor marks any black child (17.3, the clearing case). -/
lemma clear (k T t : ℕ) (hk : Cap f x0 e k T) (hk1 : Cap f x0 e (k + 1) T) (ht : T ≤ t)
    (hb : D f x0 e k t = true ∨ D f x0 e (k + 1) t = true) (hc : D f x0 e (k + 2) (t + 1) = true) :
    M f x0 e (k + 2) (t + 1) = true := by
  rw [M_succ2, hc]
  rcases hb with h | h
  · rw [hk t ht h]; simp
  · rw [hk1 t ht h]; simp

include hf in
/-- With both predecessors white, a black child copies its own colour and mark (17.3, the persisting case). -/
lemma persist (k t : ℕ) (h0 : D f x0 e k t = false) (h1 : D f x0 e (k + 1) t = false)
    (hm : D f x0 e (k + 2) t = true → M f x0 e (k + 2) t = true)
    (hc : D f x0 e (k + 2) (t + 1) = true) : M f x0 e (k + 2) (t + 1) = true := by
  have hcol : D f x0 e (k + 2) t = true := by
    rw [D_succ2, h0, h1] at hc
    cases h : D f x0 e (k + 2) t
    · rw [h, hf.h000] at hc; exact Bool.noConfusion hc
    · rfl
  rw [M_succ2, hc, hm hcol]
  simp

include hf in
/-- Once a black predecessor has been seen at time `t0 ≥ T`, diagonal `k + 2` is captured from `t0 + 1`. -/
lemma cap_step (k T t0 : ℕ) (hk : Cap f x0 e k T) (hk1 : Cap f x0 e (k + 1) T) (ht0 : T ≤ t0)
    (hb : D f x0 e k t0 = true ∨ D f x0 e (k + 1) t0 = true) : Cap f x0 e (k + 2) (t0 + 1) := by
  intro t ht
  obtain ⟨s, rfl⟩ : ∃ s, t = t0 + 1 + s := ⟨t - (t0 + 1), by omega⟩
  induction s with
  | zero => exact clear f x0 e k T t0 hk hk1 ht0 hb
  | succ s ih =>
    intro hc
    have ih' := ih (by omega)
    rw [show t0 + 1 + (s + 1) = t0 + 1 + s + 1 by ring] at hc ⊢
    by_cases hw : D f x0 e k (t0 + 1 + s) = true ∨ D f x0 e (k + 1) (t0 + 1 + s) = true
    · exact clear f x0 e k T (t0 + 1 + s) hk hk1 (by omega) hw hc
    · have hw1 : D f x0 e k (t0 + 1 + s) = false := by
        cases h : D f x0 e k (t0 + 1 + s)
        · rfl
        · exact absurd (Or.inl h) hw
      have hw2 : D f x0 e (k + 1) (t0 + 1 + s) = false := by
        cases h : D f x0 e (k + 1) (t0 + 1 + s)
        · rfl
        · exact absurd (Or.inr h) hw
      exact persist f hf x0 e k (t0 + 1 + s) hw1 hw2 ih' hc

/-- `C 0 = 0`, `C 1 = 1`, `C (j+2) = C (j+1) + (j+1)`: the capture times. -/
def C : ℕ → ℕ
  | 0 => 0
  | 1 => 1
  | j + 2 => C (j + 1) + (j + 1)

lemma C_closed (j : ℕ) : 2 * C (j + 1) = j * (j + 1) + 2 := by
  induction j with
  | zero => rfl
  | succ j ih => rw [C]; rw [Nat.mul_add, ih]; ring

lemma C_mono (j : ℕ) : C j ≤ C (j + 1) := by
  cases j with
  | zero => decide
  | succ j => rw [C]; omega

include hf he hl in
lemma cap0 : Cap f x0 e 0 (C 0) := fun t _ _ => M_zero f hf x0 e he hl t

include hf he hl in
lemma cap1 : Cap f x0 e 1 (C 1) := by
  intro t ht hb
  obtain ⟨s, rfl⟩ : ∃ s, t = s + 1 := ⟨t - 1, by rw [C] at ht; omega⟩
  rw [M_succ1 f hf x0 e he hl, hb, M_zero f hf x0 e he hl]
  simp

include hf he hl in
theorem capture_pair (j : ℕ) : Cap f x0 e j (C j) ∧ Cap f x0 e (j + 1) (C (j + 1)) := by
  induction j with
  | zero => exact ⟨cap0 f hf x0 e he hl, cap1 f hf x0 e he hl⟩
  | succ j ih =>
    obtain ⟨hj, hj1⟩ := ih
    refine ⟨hj1, ?_⟩
    have hj' : Cap f x0 e j (C (j + 1)) := Cap_mono f x0 e j _ _ (C_mono j) hj
    obtain ⟨s, hs, hb⟩ := pair f hf x0 e he hl j (C (j + 1))
    have hc := cap_step f hf x0 e j (C (j + 1)) (C (j + 1) + s) hj' hj1 (by omega) hb
    exact Cap_mono f x0 e (j + 2) _ _ (by rw [C]; omega) hc

include hf he hl in
/-- **Capture.** Every black cell on diagonal `j` is marked from time `C j`. -/
theorem capture (j t : ℕ) (ht : C j ≤ t) (hb : D f x0 e j t = true) : M f x0 e j t = true :=
  (capture_pair f hf x0 e he hl j).1 t ht hb

/-! ### Exit from every band -/

include hf he hl in
/-- **Exit.** From any time `t0`, within `C (Dd + 2) + Dd + 1` steps some marked cell lies beyond diagonal `Dd`. -/
theorem exit (Dd t0 : ℕ) :
    ∃ t, t0 ≤ t ∧ t ≤ t0 + (C (Dd + 2) + Dd + 1) ∧ ∃ k, Dd < k ∧ M f x0 e k t = true := by
  obtain ⟨s, hs, hb⟩ := pair f hf x0 e he hl (Dd + 1) (max t0 (C (Dd + 2)))
  have hT : C (Dd + 2) ≤ max t0 (C (Dd + 2)) + s := by omega
  refine ⟨max t0 (C (Dd + 2)) + s, by omega, by omega, ?_⟩
  rcases hb with h | h
  · exact ⟨Dd + 1, by omega, capture f hf x0 e he hl (Dd + 1) _ (le_trans (C_mono (Dd + 1)) hT) h⟩
  · exact ⟨Dd + 2, by omega, capture f hf x0 e he hl (Dd + 2) _ hT h⟩

include hf he hl in
/-- The marked front is beyond every band at arbitrarily late times. -/
theorem unbounded (Dd t0 : ℕ) : ∃ t, t0 ≤ t ∧ ∃ k, Dd < k ∧ M f x0 e k t = true := by
  obtain ⟨t, ht, _, hk⟩ := exit f hf x0 e he hl Dd t0
  exact ⟨t, ht, hk⟩

end

/-- The Rule 30 instance. -/
theorem capture30 (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (j t : ℕ)
    (ht : C j ≤ t) (hb : D rule30 x0 e j t = true) : M rule30 x0 e j t = true :=
  capture rule30 rule30_edgy x0 e he hl j t ht hb

theorem exit30 (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (Dd t0 : ℕ) :
    ∃ t, t0 ≤ t ∧ t ≤ t0 + (C (Dd + 2) + Dd + 1) ∧ ∃ k, Dd < k ∧ M rule30 x0 e k t = true :=
  exit rule30 rule30_edgy x0 e he hl Dd t0

end Capture

#print axioms Capture.capture
#print axioms Capture.exit
#print axioms Capture.unbounded
#print axioms Capture.capture30
#print axioms Capture.exit30
