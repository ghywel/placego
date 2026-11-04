module

public import Ruliology.CellularAutomata.Rule30FourLeftSides

/-!
# The forced front on the four strips: the recursion and the moves, with the time carried

The generic part of `Rule30FourFronts`. The settling recursion of `Rule30FrontLaw` (`frontBound`), written as a state machine
on the pair `(F j, F (j + 1))` over a word function `w` (the sixteen-bit word of each wheel of a strip's cycle), and the two
moves of `Rule30FourLeftSides` (`extend`, `branch`) with the time carried. At a nearer word with a black, the child is in its
cycle from one tick after the first black at or after the parents' time (`step_black`, from `child_same`); at a white nearer
word the child is the strip's word or its complement from the parents' time (`step_white`, from `child_white`), and the
complement is absorbed by a shift at a doubling wheel (`white_shift`) or by the fork's other strip (`white_fork`). Below the
first fork the four doubling wheels give the shift budget `1 + 2 + 4 + 8 = 15` (`low_from`). Nothing here is evaluated: the
recursion's values on the four strips are in `Rule30FourFronts`.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30FourFrontsBase

open Rule30AgedLeftDiagonals (Recurrence)
open Rule30UniversalLeftSide (child_same child_white rec_zero rec_one rowAt)
open Rule30FourLeftSides (Sp Sp_mod Sp_rec orRows orRows_black)

set_option autoImplicit false

/-! ### Sixteen-bit words -/

/-- The word with bits `f 0, …, f 15`. -/
def word16 (f : Nat → Bool) : Nat :=
  (f 0).toNat + 2 * ((f 1).toNat + 2 * ((f 2).toNat + 2 * ((f 3).toNat + 2 * ((f 4).toNat + 2 * ((f 5).toNat + 2 * ((f 6).toNat + 2 * ((f 7).toNat + 2 * ((f 8).toNat + 2 * ((f 9).toNat + 2 * ((f 10).toNat + 2 * ((f 11).toNat + 2 * ((f 12).toNat + 2 * ((f 13).toNat + 2 * ((f 14).toNat + 2 * (f 15).toNat))))))))))))))

theorem horner_zero (b : Bool) (n : Nat) : (b.toNat + 2 * n).testBit 0 = b := by
  cases b <;> simp only [Nat.testBit_zero, Bool.toNat_true, Bool.toNat_false, decide_eq_true_eq,
    decide_eq_false_iff_not] <;> omega

theorem horner_div (b : Bool) (n : Nat) : (b.toNat + 2 * n) / 2 = n := by
  cases b <;> simp only [Bool.toNat_true, Bool.toNat_false] <;> omega

theorem horner_last (b : Bool) : b.toNat.testBit 0 = b := by
  cases b <;> rfl

theorem word16_bit (f : Nat → Bool) : ∀ r, r < 16 → (word16 f).testBit r = f r
  | 0, _ => by unfold word16; rw [horner_zero]
  | 1, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, horner_zero]
  | 2, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 3, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 4, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 5, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 6, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 7, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 8, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 9, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 10, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 11, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 12, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 13, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 14, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 15, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_last]
  | n + 16, h => absurd h (by omega)

theorem word16_lt (f : Nat → Bool) : word16 f < 2 ^ 16 := by
  unfold word16
  have h0 := Bool.toNat_le (f 0)
  have h1 := Bool.toNat_le (f 1)
  have h2 := Bool.toNat_le (f 2)
  have h3 := Bool.toNat_le (f 3)
  have h4 := Bool.toNat_le (f 4)
  have h5 := Bool.toNat_le (f 5)
  have h6 := Bool.toNat_le (f 6)
  have h7 := Bool.toNat_le (f 7)
  have h8 := Bool.toNat_le (f 8)
  have h9 := Bool.toNat_le (f 9)
  have h10 := Bool.toNat_le (f 10)
  have h11 := Bool.toNat_le (f 11)
  have h12 := Bool.toNat_le (f 12)
  have h13 := Bool.toNat_le (f 13)
  have h14 := Bool.toNat_le (f 14)
  have h15 := Bool.toNat_le (f 15)
  omega

/-- A word below `2 ^ 16` is its sixteen bits. -/
theorem word_eq {x y : Nat} (hx : x < 2 ^ 16) (hy : y < 2 ^ 16)
    (h : ∀ r, r < 16 → x.testBit r = y.testBit r) : x = y := by
  apply Nat.eq_of_testBit_eq
  intro r
  rcases Nat.lt_or_ge r 16 with hr | hr
  · exact h r hr
  · have hp : 2 ^ 16 ≤ 2 ^ r := Nat.pow_le_pow_right (by decide) hr
    rw [Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hx hp), Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hy hp)]

theorem word_zero {x : Nat} (hx : x < 2 ^ 16) (h : ∀ r, r < 16 → x.testBit r = false) : x = 0 :=
  word_eq hx (by decide) (fun r hr => by rw [h r hr, Nat.zero_testBit])

theorem bit_of_ne {x : Nat} (hx : x < 2 ^ 16) (h : x ≠ 0) : ∃ r, r < 16 ∧ x.testBit r = true := by
  apply Classical.byContradiction
  intro hno
  apply h
  apply word_zero hx
  intro r hr
  cases hb : x.testBit r
  · rfl
  · exact absurd ⟨r, hr, hb⟩ hno

/-! ### The words of a strip -/

/-- `w j` is the sixteen-bit word of wheel `j` of the strip of `v`: bit `r` is the wheel at phase `r`. -/
def Words (v : Nat) (w : Nat → Nat) : Prop :=
  (∀ j, w j < 2 ^ 16) ∧ ∀ j r, r < 16 → (w j).testBit r = Sp v j r

theorem white_of_word {v : Nat} {w : Nat → Nat} (hv : rowAt 87867 v 16 = v) (hw : Words v w) {m : Nat}
    (h : w m = 0) (t : Nat) : Sp v m t = false := by
  rw [Sp_mod hv, ← hw.2 m (t % 16) (Nat.mod_lt _ (by decide)), h, Nat.zero_testBit]

theorem word_ne_of_black {v : Nat} {w : Nat → Nat} (hw : Words v w) {m r : Nat} (hr : r < 16)
    (hb : Sp v m r = true) : w m ≠ 0 := by
  intro h0
  have e := hw.2 m r hr
  rw [h0, Nat.zero_testBit, hb] at e
  exact Bool.false_ne_true e

theorem word_zero_of_white {v : Nat} {w : Nat → Nat} (hw : Words v w) {m : Nat}
    (h : ∀ r, r < 16 → Sp v m r = false) : w m = 0 :=
  word_zero (hw.1 m) (fun r hr => by rw [hw.2 m r hr, h r hr])

theorem word_eq_of_low {v v' : Nat} {w w' : Nat → Nat} (hw : Words v w) (hw' : Words v' w') {j : Nat}
    (h : ∀ r, r < 16 → Sp v' j r = Sp v j r) : w' j = w j :=
  word_eq (hw'.1 j) (hw.1 j) (fun r hr => by rw [hw'.2 j r hr, hw.2 j r hr, h r hr])

/-- Every wheel in a window has a black at some phase, from one kernel evaluation (`Rule30FourLeftSides.black_window`,
stopped at the phase). -/
theorem black_window_phase {v lo n m : Nat} (h : (orRows v 16 >>> lo) % 2 ^ n = 2 ^ n - 1) (h1 : lo ≤ m)
    (h2 : m < lo + n) : ∃ r, r < 16 ∧ Sp v m r = true := by
  have hl : m - lo < n := by omega
  have e := congrArg (fun y => y.testBit (m - lo)) h
  simp only [Nat.testBit_mod_two_pow, Nat.testBit_two_pow_sub_one, Nat.testBit_shiftRight, hl,
    decide_true, Bool.true_and, show lo + (m - lo) = m by omega] at e
  exact orRows_black e

/-! ### The settling recursion as a state machine -/

/-- The wait from phase `m` to the next black of the word `w`, searching the offsets `16 - fuel, …, 15`; `16` if none. -/
def srch (w m : Nat) : Nat → Nat
  | 0 => 16
  | fuel + 1 => if w.testBit ((m + (16 - (fuel + 1))) % 16) then 16 - (fuel + 1) else srch w m fuel

/-- One wheel: from `(F j, F (j + 1))` to `(F (j + 1), F (j + 2))`, reading the word of wheel `j + 1`. -/
def fstep (w : Nat → Nat) (j : Nat) (st : Nat × Nat) : Nat × Nat :=
  if w (j + 1) = 0 then (st.2, max st.1 st.2)
  else (st.2, max st.1 st.2 + srch (w (j + 1)) (max st.1 st.2) 16 + 1)

/-- `n` wheels from wheel `j`. -/
def frun (w : Nat → Nat) (j : Nat) : Nat → Nat × Nat → Nat × Nat
  | 0, st => st
  | n + 1, st => frun w (j + 1) n (fstep w j st)

/-- The state after `j` wheels: `(F j, F (j + 1))`. -/
def S (w : Nat → Nat) (j : Nat) : Nat × Nat := frun w 0 j (0, 1)

/-- The forced settling tick of wheel `j`, in strip time. -/
def F (w : Nat → Nat) (j : Nat) : Nat := (S w j).1

theorem srch_spec (w m : Nat) : ∀ fuel, fuel ≤ 16 →
    (∃ k, 16 - fuel ≤ k ∧ k < 16 ∧ w.testBit ((m + k) % 16) = true) →
    w.testBit ((m + srch w m fuel) % 16) = true
  | 0, _, ⟨k, hk1, hk2, _⟩ => absurd hk2 (by omega)
  | fuel + 1, hf, ⟨k, hk1, hk2, hk⟩ => by
    simp only [srch]
    split
    · assumption
    · rename_i hw
      apply srch_spec w m fuel (by omega)
      refine ⟨k, ?_, hk2, hk⟩
      rcases Nat.lt_or_ge k (16 - fuel) with hlt | hge
      · have e : k = 16 - (fuel + 1) := by omega
        subst e
        exact absurd hk hw
      · exact hge

theorem srch_black (w m : Nat) (hw : ∃ r, r < 16 ∧ w.testBit r = true) :
    w.testBit ((m + srch w m 16) % 16) = true := by
  obtain ⟨r, hr, hb⟩ := hw
  refine srch_spec w m 16 (Nat.le_refl _) ⟨(r + 16 - m % 16) % 16, by omega, Nat.mod_lt _ (by decide), ?_⟩
  rw [show (m + (r + 16 - m % 16) % 16) % 16 = r by omega]
  exact hb

theorem frun_add (w : Nat → Nat) (i a b : Nat) (st : Nat × Nat) :
    frun w i (a + b) st = frun w (i + a) b (frun w i a st) := by
  induction a generalizing i st with
  | zero => rw [Nat.zero_add]; rfl
  | succ a ih =>
    rw [show i + (a + 1) = (i + 1) + a by omega, show a + 1 + b = (a + b) + 1 by omega]
    rw [frun, frun]
    exact ih (i + 1) (fstep w i st)

theorem frun_chain (w : Nat → Nat) (i a b : Nat) (st st' st'' : Nat × Nat) (h1 : frun w i a st = st')
    (h2 : frun w (i + a) b st' = st'') : frun w i (a + b) st = st'' := by
  rw [frun_add, h1, h2]

/-- Two word functions that agree on the wheels read give the same run. -/
theorem frun_congr {w w' : Nat → Nat} : ∀ (n j : Nat) (st : Nat × Nat),
    (∀ i, i < n → w (j + i + 1) = w' (j + i + 1)) → frun w j n st = frun w' j n st
  | 0, _, _, _ => rfl
  | n + 1, j, st, h => by
    have h0 : w (j + 1) = w' (j + 1) := h 0 (by omega)
    have e : fstep w j st = fstep w' j st := by
      unfold fstep
      rw [h0]
    simp only [frun]
    rw [e]
    exact frun_congr n (j + 1) _ (fun i hi => by
      have := h (i + 1) (by omega)
      rwa [show j + (i + 1) + 1 = j + 1 + i + 1 by omega] at this)

theorem S_succ (w : Nat → Nat) (j : Nat) : S w (j + 1) = fstep w j (S w j) := by
  unfold S
  rw [frun_add w 0 j 1 (0, 1), Nat.zero_add]
  rfl

theorem fstep_fst (w : Nat → Nat) (j : Nat) (st : Nat × Nat) : (fstep w j st).1 = st.2 := by
  unfold fstep
  split <;> rfl

theorem fstep_snd (w : Nat → Nat) (j : Nat) (st : Nat × Nat) : (fstep w j st).2 =
    if w (j + 1) = 0 then max st.1 st.2 else max st.1 st.2 + srch (w (j + 1)) (max st.1 st.2) 16 + 1 := by
  unfold fstep
  split <;> rfl

theorem S_snd (w : Nat → Nat) (j : Nat) : (S w j).2 = F w (j + 1) := by
  show (S w j).2 = (S w (j + 1)).1
  rw [S_succ, fstep_fst]

theorem F_zero (w : Nat → Nat) : F w 0 = 0 := rfl

theorem F_one (w : Nat → Nat) : F w 1 = 1 := by
  show (fstep w 0 (0, 1)).1 = 1
  rw [fstep_fst]

theorem F_succ_succ (w : Nat → Nat) (j : Nat) : F w (j + 2) =
    if w (j + 1) = 0 then max (F w j) (F w (j + 1))
    else max (F w j) (F w (j + 1)) + srch (w (j + 1)) (max (F w j) (F w (j + 1))) 16 + 1 := by
  have h : F w (j + 2) = (fstep w j (S w j)).2 := by
    show (S w (j + 2)).1 = _
    rw [S_succ, fstep_fst, S_succ]
  rw [h, fstep_snd, S_snd]
  rfl

theorem F_white (w : Nat → Nat) (j : Nat) (hb : w (j + 1) = 0) : F w (j + 2) = max (F w j) (F w (j + 1)) := by
  simp [F_succ_succ, hb]

theorem F_black (w : Nat → Nat) (j : Nat) (hb : w (j + 1) ≠ 0) :
    F w (j + 2) = max (F w j) (F w (j + 1)) + srch (w (j + 1)) (max (F w j) (F w (j + 1))) 16 + 1 := by
  have hb' : ¬ w (j + 1) = 0 := hb
  simp [F_succ_succ, hb']

theorem F_step_le (w : Nat → Nat) (j : Nat) : F w (j + 1) ≤ F w (j + 2) := by
  rw [F_succ_succ]
  split <;> omega

theorem F_mono (w : Nat → Nat) {j k : Nat} (h : j ≤ k) : F w j ≤ F w k := by
  induction k with
  | zero =>
    have e : j = 0 := by omega
    subst e
    exact Nat.le_refl _
  | succ k ih =>
    rcases Nat.lt_or_ge j (k + 1) with hlt | hge
    · have hk := ih (by omega)
      cases k with
      | zero => exact Nat.le_trans hk (by rw [F_zero, F_one]; omega)
      | succ k => exact Nat.le_trans hk (F_step_le w k)
    · have e : j = k + 1 := by omega
      subst e
      exact Nat.le_refl _

/-- Read the front off a computed pair; stated with variables, so that an instance asks the kernel for no unfolding. -/
theorem F_of_S {w : Nat → Nat} {j a b : Nat} (h : S w j = (a, b)) : F w j = a := by
  show (S w j).1 = a
  rw [h]

/-- The front through wheel `j` reads only the words of wheels `1, …, j - 1`. -/
theorem F_congr {w w' : Nat → Nat} : ∀ j, (∀ i, i + 2 ≤ j → w (i + 1) = w' (i + 1)) → F w j = F w' j
  | 0, _ => rfl
  | 1, _ => by rw [F_one, F_one]
  | j + 2, h => by
    rw [F_succ_succ w j, F_succ_succ w' j, h j (by omega), F_congr j (fun i hi => h i (by omega)),
      F_congr (j + 1) (fun i hi => h i (by omega))]

/-! ### Alignment with the time carried -/

/-- `a` carries the strip of `v` on every wheel through `J` from strip tick `T` on, at the shift `s`. -/
def OnStrip (a : Nat → Nat → Bool) (v s T J : Nat) : Prop :=
  ∀ j, j ≤ J → ∀ t, T ≤ t → a j (t + s) = Sp v j t

/-- The same with a time for each wheel. -/
def AlignedFrom (a : Nat → Nat → Bool) (v s : Nat) (F : Nat → Nat) (J : Nat) : Prop :=
  ∀ j, j ≤ J → ∀ t, F j ≤ t → a j (t + s) = Sp v j t

theorem aligned_of_alignedFrom {a : Nat → Nat → Bool} {v s J : Nat} {F : Nat → Nat} (h : AlignedFrom a v s F J) :
    Rule30FourLeftSides.Aligned a v s J :=
  fun j hj => ⟨F j, h j hj⟩

theorem onStrip_of_alignedFrom {a : Nat → Nat → Bool} {v s T J : Nat} {F : Nat → Nat} (hT : ∀ j, j ≤ J → F j ≤ T)
    (h : AlignedFrom a v s F J) : OnStrip a v s T J :=
  fun j hj t ht => h j hj t (Nat.le_trans (hT j hj) ht)

theorem alignedFrom_congr {a : Nat → Nat → Bool} {v s J : Nat} {F F' : Nat → Nat} (hF : ∀ j, j ≤ J → F j = F' j)
    (h : AlignedFrom a v s F J) : AlignedFrom a v s F' J :=
  fun j hj t ht => h j hj t (by rw [hF j hj]; exact ht)

/-- Wheels `0` and `1`: black from ticks `0` and `1`. -/
theorem base_from {a : Nat → Nat → Bool} {v : Nat} {w : Nat → Nat} (ha : Recurrence a) (ha0 : a 0 0 = true)
    (h0 : ∀ t, Sp v 0 t = true) (h1 : ∀ t, Sp v 1 t = true) : AlignedFrom a v 0 (F w) 1 := by
  intro j hj t ht
  rcases Nat.lt_or_ge j 1 with hlt | hge
  · have e : j = 0 := by omega
    subst e
    show a 0 t = Sp v 0 t
    rw [rec_zero ha ha0, h0]
  · have e : j = 1 := by omega
    subst e
    rw [F_one] at ht
    obtain ⟨u, rfl⟩ : ∃ u, t = u + 1 := ⟨t - 1, by omega⟩
    show a 1 (u + 1) = Sp v 1 (u + 1)
    rw [rec_one ha ha0 u, h1]

/-- **The forced child.** At a nearer word with a black, wheel `k + 2` carries the strip from `F (k + 2)` on. -/
theorem step_black {a : Nat → Nat → Bool} {v s k : Nat} {w : Nat → Nat} (ha : Recurrence a)
    (hv : rowAt 87867 v 16 = v) (hw : Words v w) (hk : k + 2 < 87867)
    (ih : AlignedFrom a v s (F w) (k + 1)) (hb : w (k + 1) ≠ 0) : AlignedFrom a v s (F w) (k + 2) := by
  have hF := F_black w k hb
  have hblack : Sp v (k + 1) (max (F w k) (F w (k + 1)) + srch (w (k + 1)) (max (F w k) (F w (k + 1))) 16) = true := by
    rw [Sp_mod hv, ← hw.2 (k + 1) _ (Nat.mod_lt _ (by decide))]
    exact srch_black (w (k + 1)) _ (bit_of_ne (hw.1 (k + 1)) hb)
  have hnew := child_same (k := k) (s := s) (T := max (F w k) (F w (k + 1))) ha (fun t => Sp_rec v k t hk)
    (fun t ht => ih k (by omega) t (by omega)) (fun t ht => ih (k + 1) (by omega) t (by omega))
    (Nat.le_add_right _ _) hblack
  intro j hj t ht
  rcases Nat.lt_or_ge j (k + 2) with hlt | hge
  · exact ih j (by omega) t ht
  · have e : j = k + 2 := by omega
    subst e
    exact hnew t (by omega)

/-- **A white nearer word.** From the parents' time, which is `F (k + 2)`, the child is the strip's word or its
complement. -/
theorem step_white {a : Nat → Nat → Bool} {v s k : Nat} {w : Nat → Nat} (ha : Recurrence a)
    (hv : rowAt 87867 v 16 = v) (hw : Words v w) (hk : k + 2 < 87867)
    (ih : AlignedFrom a v s (F w) (k + 1)) (hb : w (k + 1) = 0) :
    AlignedFrom a v s (F w) (k + 2) ∨ ∀ t, F w (k + 2) ≤ t → a (k + 2) (t + s) = !Sp v (k + 2) t := by
  have hF := F_white w k hb
  rcases child_white (k := k) (s := s) (T := max (F w k) (F w (k + 1))) ha (fun t => Sp_rec v k t hk)
    (fun t ht => ih k (by omega) t (by omega)) (fun t ht => ih (k + 1) (by omega) t (by omega))
    (fun t _ => white_of_word hv hw hb t) with h | h
  · left
    intro j hj t ht
    rcases Nat.lt_or_ge j (k + 2) with hlt | hge
    · exact ih j (by omega) t ht
    · have e : j = k + 2 := by omega
      subst e
      exact h t (by omega)
  · right
    intro t ht
    exact h t (by omega)

/-- **A doubling wheel.** The complement is a shift by the lower strip's period `L`, which the lower wheels do not see. -/
theorem white_shift {a : Nat → Nat → Bool} {v s k L : Nat} {w : Nat → Nat}
    (ih : AlignedFrom a v s (F w) (k + 1))
    (h : ∀ t, F w (k + 2) ≤ t → a (k + 2) (t + s) = !Sp v (k + 2) t)
    (hper : ∀ j, j ≤ k + 1 → ∀ t, Sp v j (t + L) = Sp v j t)
    (hanti : ∀ t, Sp v (k + 2) (t + L) = !Sp v (k + 2) t) :
    AlignedFrom a v (s + L) (F w) (k + 2) := by
  intro j hj t ht
  rcases Nat.lt_or_ge j (k + 2) with hlt | hge
  · rw [show t + (s + L) = (t + L) + s by omega, ih j (by omega) (t + L) (by omega), hper j (by omega) t]
  · have e : j = k + 2 := by omega
    subst e
    rw [show t + (s + L) = (t + L) + s by omega, h (t + L) (by omega), hanti t]
    cases Sp v (k + 2) t <;> rfl

/-- **A fork.** The complement is the other strip's word, and that strip agrees with `v` below. -/
theorem white_fork {a : Nat → Nat → Bool} {v v' s k : Nat} {w : Nat → Nat}
    (ih : AlignedFrom a v s (F w) (k + 1))
    (h : ∀ t, F w (k + 2) ≤ t → a (k + 2) (t + s) = !Sp v (k + 2) t)
    (hlow : ∀ j t, j ≤ k + 1 → Sp v' j t = Sp v j t) (hcomp : ∀ t, Sp v' (k + 2) t = !Sp v (k + 2) t) :
    AlignedFrom a v' s (F w) (k + 2) := by
  intro j hj t ht
  rcases Nat.lt_or_ge j (k + 2) with hlt | hge
  · rw [ih j (by omega) t ht, hlow j t (by omega)]
  · have e : j = k + 2 := by omega
    subst e
    rw [h t ht, hcomp t]

/-- **Going up without a fork**, with the time carried: while every nearer word has a black, the same shift. -/
theorem extend_from {a : Nat → Nat → Bool} {v s j0 J : Nat} {w : Nat → Nat} (ha : Recurrence a)
    (hv : rowAt 87867 v 16 = v) (hw : Words v w) (h1 : 1 ≤ j0) (hJ : J ≤ 87866) (hj : j0 ≤ J)
    (hal : AlignedFrom a v s (F w) j0) (hb : ∀ m, j0 ≤ m → m < J → w m ≠ 0) :
    AlignedFrom a v s (F w) J := by
  have aux : ∀ n, j0 + n ≤ J → AlignedFrom a v s (F w) (j0 + n) := by
    intro n
    induction n with
    | zero => intro _; exact hal
    | succ n ih =>
      intro hn
      have hp := ih (by omega)
      obtain ⟨k, hk⟩ : ∃ k, j0 + n = k + 1 := ⟨j0 + n - 1, by omega⟩
      rw [hk] at hp
      rw [show j0 + (n + 1) = k + 2 by omega]
      exact step_black ha hv hw (by omega) hp (hb (k + 1) (by omega) (by omega))
  have h := aux (J - j0) (by omega)
  rwa [show j0 + (J - j0) = J by omega] at h

/-! ### Below the first fork: the shift budget -/

/-- The shift budget through wheel `n`: `1, 2, 4, 8` become available at wheels `3, 8, 29, 400`. -/
def lsum (n : Nat) : Nat := min 1 (n / 3) + 2 * min 1 (n / 8) + 4 * min 1 (n / 29) + 8 * min 1 (n / 400)

theorem lsum_53207 : lsum 53207 = 15 := by decide

/-- **Through wheel 53,207**, for a strip whose white wheels there are the four doubling wheels, with the time carried:
the shift stays within the budget. -/
theorem low_from {a : Nat → Nat → Bool} {v : Nat} {w : Nat → Nat} (ha : Recurrence a) (ha0 : a 0 0 = true)
    (hv : rowAt 87867 v 16 = v) (hw : Words v w) (h0 : ∀ t, Sp v 0 t = true) (h1 : ∀ t, Sp v 1 t = true)
    (hbw : ∀ m, m < 53207 → w m ≠ 0 ∨ m = 2 ∨ m = 7 ∨ m = 28 ∨ m = 399)
    (hs2 : (∀ j, j ≤ 2 → ∀ t, Sp v j (t + 1) = Sp v j t) ∧ ∀ t, Sp v (2 + 1) (t + 1) = !Sp v (2 + 1) t)
    (hs7 : (∀ j, j ≤ 7 → ∀ t, Sp v j (t + 2) = Sp v j t) ∧ ∀ t, Sp v (7 + 1) (t + 2) = !Sp v (7 + 1) t)
    (hs28 : (∀ j, j ≤ 28 → ∀ t, Sp v j (t + 4) = Sp v j t) ∧ ∀ t, Sp v (28 + 1) (t + 4) = !Sp v (28 + 1) t)
    (hs399 : (∀ j, j ≤ 399 → ∀ t, Sp v j (t + 8) = Sp v j t) ∧ ∀ t, Sp v (399 + 1) (t + 8) = !Sp v (399 + 1) t) :
    ∀ n, n ≤ 53207 → ∃ s, s ≤ lsum n ∧ AlignedFrom a v s (F w) n
  | 0, _ => ⟨0, by simp [lsum], fun j hj t _ => by
      have e : j = 0 := by omega
      subst e
      show a 0 t = Sp v 0 t
      rw [rec_zero ha ha0, h0]⟩
  | 1, _ => ⟨0, by simp [lsum], base_from ha ha0 h0 h1⟩
  | n + 2, hn => by
    obtain ⟨s, hs, ih⟩ := low_from ha ha0 hv hw h0 h1 hbw hs2 hs7 hs28 hs399 (n + 1) (by omega)
    have hlsum : lsum (n + 1) ≤ lsum (n + 2) := by simp only [lsum]; omega
    by_cases hb : w (n + 1) = 0
    · rcases step_white ha hv hw (by omega) ih hb with h | h
      · exact ⟨s, Nat.le_trans hs hlsum, h⟩
      · rcases hbw (n + 1) (by omega) with hne | h2 | h7 | h28 | h399
        · exact absurd hb hne
        · have e : n = 1 := by omega
          subst e
          exact ⟨s + 1, by simp only [lsum] at hs ⊢; omega, white_shift ih h hs2.1 hs2.2⟩
        · have e : n = 6 := by omega
          subst e
          exact ⟨s + 2, by simp only [lsum] at hs ⊢; omega, white_shift ih h hs7.1 hs7.2⟩
        · have e : n = 27 := by omega
          subst e
          exact ⟨s + 4, by simp only [lsum] at hs ⊢; omega, white_shift ih h hs28.1 hs28.2⟩
        · have e : n = 398 := by omega
          subst e
          exact ⟨s + 8, by simp only [lsum] at hs ⊢; omega, white_shift ih h hs399.1 hs399.2⟩
    · exact ⟨s, Nat.le_trans hs hlsum, step_black ha hv hw (by omega) ih hb⟩

end Ruliology.CellularAutomata.Rule30FourFrontsBase
