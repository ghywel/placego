module

public import Ruliology.CellularAutomata.Rule30UniversalLeftSide

/-!
# Fronts on a tree of strips at period 32: the settling recursion, the moves with the time carried, and the walk

The generic part of `Rule30FiveFronts`, after `Rule30FourFrontsBase` and the walk of `Rule30FourFronts`, with two
changes: the period is 32 (every strip whose period divides 32 is covered, the doubled one included) and the width `K` of
the register is a parameter. A strip is a row `v` with `rowAt K v 32 = v`; its wheel `j` is the word of 32 bits `wd K v j`.
The settling recursion of `Rule30FrontLaw` (`frontBound`) is a state machine on the pair `(F j, F (j + 1))` over a word
function; the moves of `Rule30FourLeftSides` carry the time: at a nearer word with a black the child is in its cycle from one
tick after the first black at or after the parents' time (`step_black`), at a white nearer word it is the strip's word or its
complement from the parents' time (`step_white`), and the complement is absorbed by a shift at a doubling wheel
(`white_shift`) or by the fork's other strip (`white_fork`). Below the first fork the doubling wheels 2, 7, 28, 399 give the
budget `lsum` (`low_from`). The walk evaluates the recursion: from wheel `j` at tick `t`, move on at a black cell and wait at a
white one (`walk`, `frun_of_walk`, `seg_black`), thirty-two ticks a round (`st32`, `w32`, `fastWalk`). `not_related` separates
two strips by a wheel where they are complements and a wheel of primitive period 16, on per-wheel periods, so that a strip
of period 32 is handled too. The long stretch of a run is checked in blocks of rounds (`w32_chain`, `fastWalk_of`), so that
no single kernel check holds more than a block's rows.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30FiveFrontsBase

open Rule30AgedLeftDiagonals (Recurrence)
open Rule30UniversalLeftSide (child_same child_white rec_zero rec_one rowAt rowAt_add_mul stepK_bit_step)

set_option autoImplicit false

/-! ### Strips of rows -/

/-- Wheel `j` of the row `v` at tick `t`, on `K` wheels. -/
def Sp (K v j t : Nat) : Bool := (rowAt K v t).testBit j

theorem Sp_add_mul' {K v P : Nat} (hv : rowAt K v P = v) (j t q : Nat) : Sp K v j (t + q * P) = Sp K v j t := by
  simp only [Sp]
  rw [rowAt_add_mul hv]

theorem Sp_mod_period {K v P : Nat} (hv : rowAt K v P = v) (j t : Nat) : Sp K v j t = Sp K v j (t % P) := by
  have h := Sp_add_mul' hv j (t % P) (t / P)
  have e : t % P + t / P * P = t := by rw [Nat.mul_comm]; exact Nat.mod_add_div t P
  rw [e] at h
  exact h

theorem Sp_add_mul {K v : Nat} (hv : rowAt K v 32 = v) (j t q : Nat) : Sp K v j (t + q * 32) = Sp K v j t :=
  Sp_add_mul' hv j t q

theorem Sp_mod {K v : Nat} (hv : rowAt K v 32 = v) (j t : Nat) : Sp K v j t = Sp K v j (t % 32) :=
  Sp_mod_period hv j t

theorem Sp_rec {K : Nat} (v j t : Nat) (hj : j + 2 < K) :
    Sp K v (j + 2) (t + 1) = xor (Sp K v j t) (Sp K v (j + 1) t || Sp K v (j + 2) t) := by
  simp only [Sp, rowAt]
  rw [stepK_bit_step hj]

/-- A wheel that repeats after `L` ticks repeats after `q * L`. -/
theorem per_mul {K v j L : Nat} (h : ∀ t, Sp K v j (t + L) = Sp K v j t) (t : Nat) : ∀ q, Sp K v j (t + q * L) = Sp K v j t
  | 0 => by simp
  | q + 1 => by
    rw [show t + (q + 1) * L = (t + q * L) + L by rw [Nat.add_mul]; omega, h, per_mul h t q]

/-- The OR of the first `n` rows of `v`'s cycle. -/
def orRows (K v : Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => orRows K v n ||| rowAt K v n

theorem orRows_black {K v n m : Nat} (h : (orRows K v n).testBit m = true) : ∃ r, r < n ∧ Sp K v m r = true := by
  induction n with
  | zero => simp [orRows] at h
  | succ n ih =>
    simp only [orRows, Nat.testBit_or, Bool.or_eq_true] at h
    rcases h with h | h
    · obtain ⟨r, hr, hc⟩ := ih h
      exact ⟨r, by omega, hc⟩
    · exact ⟨n, by omega, h⟩

/-- Every wheel in a window has a black at some phase, from one kernel evaluation. -/
theorem black_window_phase {K v lo n m : Nat} (h : (orRows K v 32 >>> lo) % 2 ^ n = 2 ^ n - 1) (h1 : lo ≤ m)
    (h2 : m < lo + n) : ∃ r, r < 32 ∧ Sp K v m r = true := by
  have hl : m - lo < n := by omega
  have e := congrArg (fun y => y.testBit (m - lo)) h
  simp only [Nat.testBit_mod_two_pow, Nat.testBit_two_pow_sub_one, Nat.testBit_shiftRight, hl,
    decide_true, Bool.true_and, show lo + (m - lo) = m by omega] at e
  exact orRows_black e

theorem low_of_phase {K v v' n : Nat} (hv : rowAt K v 32 = v) (hv' : rowAt K v' 32 = v')
    (h : ∀ r, r < 32 → rowAt K v' r % 2 ^ n = rowAt K v r % 2 ^ n) (j t : Nat) (hj : j < n) :
    Sp K v' j t = Sp K v j t := by
  have e := congrArg (fun y => y.testBit j) (h (t % 32) (Nat.mod_lt _ (by omega)))
  simp only [Nat.testBit_mod_two_pow, hj, decide_true, Bool.true_and] at e
  rw [Sp_mod hv', Sp_mod hv j t]
  exact e

theorem comp_of_phase {K v v' w : Nat} (hv : rowAt K v 32 = v) (hv' : rowAt K v' 32 = v')
    (h : ∀ r, r < 32 → Sp K v' w r = !Sp K v w r) (t : Nat) : Sp K v' w t = !Sp K v w t := by
  rw [Sp_mod hv', Sp_mod hv w t]
  exact h _ (Nat.mod_lt _ (by omega))

theorem white_of_phase {K v w : Nat} (hv : rowAt K v 32 = v) (h : ∀ r, r < 32 → Sp K v w r = false)
    (t : Nat) : Sp K v w t = false := by
  rw [Sp_mod hv]
  exact h _ (Nat.mod_lt _ (by omega))

theorem black_of_phase {K v w : Nat} (hv : rowAt K v 32 = v) (h : ∀ r, r < 32 → Sp K v w r = true)
    (t : Nat) : Sp K v w t = true := by
  rw [Sp_mod hv]
  exact h _ (Nat.mod_lt _ (by omega))

/-- A shift by `L` that the wheels through `m` do not see and that complements wheel `m + 1`, from the phases. -/
theorem strip_shift {K v m L : Nat} (hv : rowAt K v 32 = v)
    (h1 : ∀ r, r < 32 → rowAt K v (r + L) % 2 ^ (m + 1) = rowAt K v r % 2 ^ (m + 1))
    (h2 : ∀ r, r < 32 → Sp K v (m + 1) (r + L) = !Sp K v (m + 1) r) :
    (∀ j, j ≤ m → ∀ t, Sp K v j (t + L) = Sp K v j t) ∧ ∀ t, Sp K v (m + 1) (t + L) = !Sp K v (m + 1) t := by
  have ht : ∀ t, t + L = (t % 32 + L) + t / 32 * 32 := by intro t; omega
  constructor
  · intro j hj t
    have e := congrArg (fun n => n.testBit j) (h1 (t % 32) (Nat.mod_lt _ (by omega)))
    simp only [Nat.testBit_mod_two_pow, show j < m + 1 by omega, decide_true, Bool.true_and] at e
    rw [ht t, Sp_add_mul hv, Sp_mod hv j t]
    exact e
  · intro t
    rw [ht t, Sp_add_mul hv, Sp_mod hv (m + 1) t]
    exact h2 _ (Nat.mod_lt _ (by omega))

/-- The white wheels below the first fork. -/
def whiteMask : Nat := 2 ^ 2 ||| 2 ^ 7 ||| 2 ^ 28 ||| 2 ^ 399

theorem black_or_white {K v n m : Nat} (hmask : (orRows K v 32 ||| whiteMask) % 2 ^ n = 2 ^ n - 1) (hm : m < n) :
    (∃ r, r < 32 ∧ Sp K v m r = true) ∨ m = 2 ∨ m = 7 ∨ m = 28 ∨ m = 399 := by
  have h := congrArg (fun y => y.testBit m) hmask
  simp only [Nat.testBit_mod_two_pow, Nat.testBit_two_pow_sub_one, Nat.testBit_or, whiteMask,
    Nat.testBit_two_pow, hm, decide_true, Bool.true_and, Bool.or_eq_true, decide_eq_true_eq] at h
  rcases h with h | h
  · exact Or.inl (orRows_black h)
  · right
    omega

/-! ### Words -/

/-- The word with bits `f 0, …, f (n - 1)`. -/
def wordOf : Nat → (Nat → Bool) → Nat
  | 0, _ => 0
  | n + 1, f => (f 0).toNat + 2 * wordOf n (fun r => f (r + 1))

theorem horner_zero (b : Bool) (n : Nat) : (b.toNat + 2 * n).testBit 0 = b := by
  cases b <;> simp only [Nat.testBit_zero, Bool.toNat_true, Bool.toNat_false, decide_eq_true_eq,
    decide_eq_false_iff_not] <;> omega

theorem horner_div (b : Bool) (n : Nat) : (b.toNat + 2 * n) / 2 = n := by
  cases b <;> simp only [Bool.toNat_true, Bool.toNat_false] <;> omega

theorem wordOf_bit : ∀ (n : Nat) (f : Nat → Bool) (r : Nat), r < n → (wordOf n f).testBit r = f r
  | 0, _, _, h => absurd h (Nat.not_lt_zero _)
  | n + 1, f, 0, _ => by
    simp only [wordOf]
    rw [horner_zero]
  | n + 1, f, r + 1, h => by
    simp only [wordOf]
    rw [Nat.testBit_succ, horner_div]
    exact wordOf_bit n _ r (by omega)

theorem wordOf_lt : ∀ (n : Nat) (f : Nat → Bool), wordOf n f < 2 ^ n
  | 0, _ => by simp [wordOf]
  | n + 1, f => by
    simp only [wordOf]
    have h1 := Bool.toNat_le (f 0)
    have h2 := wordOf_lt n (fun r => f (r + 1))
    rw [Nat.pow_succ]
    omega

/-- A word below `2 ^ 32` is its thirty-two bits. -/
theorem word_eq {x y : Nat} (hx : x < 2 ^ 32) (hy : y < 2 ^ 32)
    (h : ∀ r, r < 32 → x.testBit r = y.testBit r) : x = y := by
  apply Nat.eq_of_testBit_eq
  intro r
  rcases Nat.lt_or_ge r 32 with hr | hr
  · exact h r hr
  · have hp : 2 ^ 32 ≤ 2 ^ r := Nat.pow_le_pow_right (by decide) hr
    rw [Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hx hp), Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hy hp)]

theorem word_zero {x : Nat} (hx : x < 2 ^ 32) (h : ∀ r, r < 32 → x.testBit r = false) : x = 0 :=
  word_eq hx (by decide) (fun r hr => by rw [h r hr, Nat.zero_testBit])

theorem bit_of_ne {x : Nat} (hx : x < 2 ^ 32) (h : x ≠ 0) : ∃ r, r < 32 ∧ x.testBit r = true := by
  apply Classical.byContradiction
  intro hno
  apply h
  apply word_zero hx
  intro r hr
  cases hb : x.testBit r
  · rfl
  · exact absurd ⟨r, hr, hb⟩ hno

/-- `w j` is the thirty-two-bit word of wheel `j` of the strip of `v`: bit `r` is the wheel at phase `r`. -/
def Words (K v : Nat) (w : Nat → Nat) : Prop :=
  (∀ j, w j < 2 ^ 32) ∧ ∀ j r, r < 32 → (w j).testBit r = Sp K v j r

/-- The word of wheel `j` of the row `v`, from the rows themselves. -/
def wd (K v j : Nat) : Nat := wordOf 32 (fun r => (rowAt K v r).testBit j)

theorem wd_row (K v : Nat) : ∀ j r, r < 32 → (wd K v j).testBit r = (rowAt K v r).testBit j := fun _ r hr =>
  wordOf_bit 32 _ r hr

theorem wd_lt (K v j : Nat) : wd K v j < 2 ^ 32 := wordOf_lt 32 _

theorem words (K v : Nat) : Words K v (wd K v) := ⟨wd_lt K v, fun j r hr => wd_row K v j r hr⟩

theorem white_of_word {K v : Nat} {w : Nat → Nat} (hv : rowAt K v 32 = v) (hw : Words K v w) {m : Nat}
    (h : w m = 0) (t : Nat) : Sp K v m t = false := by
  rw [Sp_mod hv, ← hw.2 m (t % 32) (Nat.mod_lt _ (by decide)), h, Nat.zero_testBit]

theorem word_ne_of_black {K v : Nat} {w : Nat → Nat} (hw : Words K v w) {m r : Nat} (hr : r < 32)
    (hb : Sp K v m r = true) : w m ≠ 0 := by
  intro h0
  have e := hw.2 m r hr
  rw [h0, Nat.zero_testBit, hb] at e
  exact Bool.false_ne_true e

theorem word_zero_of_white {K v : Nat} {w : Nat → Nat} (hw : Words K v w) {m : Nat}
    (h : ∀ r, r < 32 → Sp K v m r = false) : w m = 0 :=
  word_zero (hw.1 m) (fun r hr => by rw [hw.2 m r hr, h r hr])

theorem word_eq_of_low {K v v' : Nat} {w w' : Nat → Nat} (hw : Words K v w) (hw' : Words K v' w') {j : Nat}
    (h : ∀ r, r < 32 → Sp K v' j r = Sp K v j r) : w' j = w j :=
  word_eq (hw'.1 j) (hw.1 j) (fun r hr => by rw [hw'.2 j r hr, hw.2 j r hr, h r hr])

/-! ### The settling recursion as a state machine -/

/-- The wait from phase `m` to the next black of the word `w`, searching the offsets `32 - fuel, …, 31`; `32` if none. -/
def srch (w m : Nat) : Nat → Nat
  | 0 => 32
  | fuel + 1 => if w.testBit ((m + (32 - (fuel + 1))) % 32) then 32 - (fuel + 1) else srch w m fuel

/-- One wheel: from `(F j, F (j + 1))` to `(F (j + 1), F (j + 2))`, reading the word of wheel `j + 1`. -/
def fstep (w : Nat → Nat) (j : Nat) (st : Nat × Nat) : Nat × Nat :=
  if w (j + 1) = 0 then (st.2, max st.1 st.2)
  else (st.2, max st.1 st.2 + srch (w (j + 1)) (max st.1 st.2) 32 + 1)

/-- `n` wheels from wheel `j`. -/
def frun (w : Nat → Nat) (j : Nat) : Nat → Nat × Nat → Nat × Nat
  | 0, st => st
  | n + 1, st => frun w (j + 1) n (fstep w j st)

/-- The state after `j` wheels: `(F j, F (j + 1))`. -/
def S (w : Nat → Nat) (j : Nat) : Nat × Nat := frun w 0 j (0, 1)

/-- The forced settling tick of wheel `j`, in strip time. -/
def F (w : Nat → Nat) (j : Nat) : Nat := (S w j).1

theorem srch_spec (w m : Nat) : ∀ fuel, fuel ≤ 32 →
    (∃ k, 32 - fuel ≤ k ∧ k < 32 ∧ w.testBit ((m + k) % 32) = true) →
    w.testBit ((m + srch w m fuel) % 32) = true
  | 0, _, ⟨k, hk1, hk2, _⟩ => absurd hk2 (by omega)
  | fuel + 1, hf, ⟨k, hk1, hk2, hk⟩ => by
    simp only [srch]
    split
    · assumption
    · rename_i hw
      apply srch_spec w m fuel (by omega)
      refine ⟨k, ?_, hk2, hk⟩
      rcases Nat.lt_or_ge k (32 - fuel) with hlt | hge
      · have e : k = 32 - (fuel + 1) := by omega
        subst e
        exact absurd hk hw
      · exact hge

theorem srch_black (w m : Nat) (hw : ∃ r, r < 32 ∧ w.testBit r = true) :
    w.testBit ((m + srch w m 32) % 32) = true := by
  obtain ⟨r, hr, hb⟩ := hw
  refine srch_spec w m 32 (Nat.le_refl _) ⟨(r + 32 - m % 32) % 32, by omega, Nat.mod_lt _ (by decide), ?_⟩
  rw [show (m + (r + 32 - m % 32) % 32) % 32 = r by omega]
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

theorem low_congr {w w' : Nat → Nat} {n : Nat} {st : Nat × Nat} (h : ∀ i, i < n → w (i + 1) = w' (i + 1)) :
    frun w 0 n st = frun w' 0 n st :=
  frun_congr n 0 st (fun i hi => by rw [Nat.zero_add]; exact h i hi)

theorem S_succ (w : Nat → Nat) (j : Nat) : S w (j + 1) = fstep w j (S w j) := by
  unfold S
  rw [frun_add w 0 j 1 (0, 1), Nat.zero_add]
  rfl

theorem fstep_fst (w : Nat → Nat) (j : Nat) (st : Nat × Nat) : (fstep w j st).1 = st.2 := by
  unfold fstep
  split <;> rfl

theorem fstep_snd (w : Nat → Nat) (j : Nat) (st : Nat × Nat) : (fstep w j st).2 =
    if w (j + 1) = 0 then max st.1 st.2 else max st.1 st.2 + srch (w (j + 1)) (max st.1 st.2) 32 + 1 := by
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
    else max (F w j) (F w (j + 1)) + srch (w (j + 1)) (max (F w j) (F w (j + 1))) 32 + 1 := by
  have h : F w (j + 2) = (fstep w j (S w j)).2 := by
    show (S w (j + 2)).1 = _
    rw [S_succ, fstep_fst, S_succ]
  rw [h, fstep_snd, S_snd]
  rfl

theorem F_white (w : Nat → Nat) (j : Nat) (hb : w (j + 1) = 0) : F w (j + 2) = max (F w j) (F w (j + 1)) := by
  simp [F_succ_succ, hb]

theorem F_black (w : Nat → Nat) (j : Nat) (hb : w (j + 1) ≠ 0) :
    F w (j + 2) = max (F w j) (F w (j + 1)) + srch (w (j + 1)) (max (F w j) (F w (j + 1))) 32 + 1 := by
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
def OnStrip (K : Nat) (a : Nat → Nat → Bool) (v s T J : Nat) : Prop :=
  ∀ j, j ≤ J → ∀ t, T ≤ t → a j (t + s) = Sp K v j t

/-- The same with a time for each wheel. -/
def AlignedFrom (K : Nat) (a : Nat → Nat → Bool) (v s : Nat) (F : Nat → Nat) (J : Nat) : Prop :=
  ∀ j, j ≤ J → ∀ t, F j ≤ t → a j (t + s) = Sp K v j t

/-- The alignment of `Rule30FourLeftSides`, on `K` wheels. -/
def Aligned (K : Nat) (a : Nat → Nat → Bool) (v s J : Nat) : Prop :=
  ∀ j, j ≤ J → ∃ T, ∀ t, T ≤ t → a j (t + s) = Sp K v j t

theorem aligned_of_alignedFrom {K : Nat} {a : Nat → Nat → Bool} {v s J : Nat} {F : Nat → Nat}
    (h : AlignedFrom K a v s F J) : Aligned K a v s J :=
  fun j hj => ⟨F j, h j hj⟩

theorem onStrip_of_alignedFrom {K : Nat} {a : Nat → Nat → Bool} {v s T J : Nat} {F : Nat → Nat}
    (hT : ∀ j, j ≤ J → F j ≤ T) (h : AlignedFrom K a v s F J) : OnStrip K a v s T J :=
  fun j hj t ht => h j hj t (Nat.le_trans (hT j hj) ht)

theorem alignedFrom_congr {K : Nat} {a : Nat → Nat → Bool} {v s J : Nat} {F F' : Nat → Nat}
    (hF : ∀ j, j ≤ J → F j = F' j) (h : AlignedFrom K a v s F J) : AlignedFrom K a v s F' J :=
  fun j hj t ht => h j hj t (by rw [hF j hj]; exact ht)

/-- Wheels `0` and `1`: black from ticks `0` and `1`. -/
theorem base_from {K : Nat} {a : Nat → Nat → Bool} {v : Nat} {w : Nat → Nat} (ha : Recurrence a) (ha0 : a 0 0 = true)
    (h0 : ∀ t, Sp K v 0 t = true) (h1 : ∀ t, Sp K v 1 t = true) : AlignedFrom K a v 0 (F w) 1 := by
  intro j hj t ht
  rcases Nat.lt_or_ge j 1 with hlt | hge
  · have e : j = 0 := by omega
    subst e
    show a 0 t = Sp K v 0 t
    rw [rec_zero ha ha0, h0]
  · have e : j = 1 := by omega
    subst e
    rw [F_one] at ht
    obtain ⟨u, rfl⟩ : ∃ u, t = u + 1 := ⟨t - 1, by omega⟩
    show a 1 (u + 1) = Sp K v 1 (u + 1)
    rw [rec_one ha ha0 u, h1]

/-- **The forced child.** At a nearer word with a black, wheel `k + 2` carries the strip from `F (k + 2)` on. -/
theorem step_black {K : Nat} {a : Nat → Nat → Bool} {v s k : Nat} {w : Nat → Nat} (ha : Recurrence a)
    (hv : rowAt K v 32 = v) (hw : Words K v w) (hk : k + 2 < K)
    (ih : AlignedFrom K a v s (F w) (k + 1)) (hb : w (k + 1) ≠ 0) : AlignedFrom K a v s (F w) (k + 2) := by
  have hF := F_black w k hb
  have hblack : Sp K v (k + 1) (max (F w k) (F w (k + 1)) + srch (w (k + 1)) (max (F w k) (F w (k + 1))) 32) = true := by
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

/-- **A white nearer word.** From the parents' time, which is `F (k + 2)`, the child is the strip's word or its complement. -/
theorem step_white {K : Nat} {a : Nat → Nat → Bool} {v s k : Nat} {w : Nat → Nat} (ha : Recurrence a)
    (hv : rowAt K v 32 = v) (hw : Words K v w) (hk : k + 2 < K)
    (ih : AlignedFrom K a v s (F w) (k + 1)) (hb : w (k + 1) = 0) :
    AlignedFrom K a v s (F w) (k + 2) ∨ ∀ t, F w (k + 2) ≤ t → a (k + 2) (t + s) = !Sp K v (k + 2) t := by
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
theorem white_shift {K : Nat} {a : Nat → Nat → Bool} {v s k L : Nat} {w : Nat → Nat}
    (ih : AlignedFrom K a v s (F w) (k + 1))
    (h : ∀ t, F w (k + 2) ≤ t → a (k + 2) (t + s) = !Sp K v (k + 2) t)
    (hper : ∀ j, j ≤ k + 1 → ∀ t, Sp K v j (t + L) = Sp K v j t)
    (hanti : ∀ t, Sp K v (k + 2) (t + L) = !Sp K v (k + 2) t) :
    AlignedFrom K a v (s + L) (F w) (k + 2) := by
  intro j hj t ht
  rcases Nat.lt_or_ge j (k + 2) with hlt | hge
  · rw [show t + (s + L) = (t + L) + s by omega, ih j (by omega) (t + L) (by omega), hper j (by omega) t]
  · have e : j = k + 2 := by omega
    subst e
    rw [show t + (s + L) = (t + L) + s by omega, h (t + L) (by omega), hanti t]
    cases Sp K v (k + 2) t <;> rfl

/-- **A fork.** The complement is the other strip's word, and that strip agrees with `v` below. -/
theorem white_fork {K : Nat} {a : Nat → Nat → Bool} {v v' s k : Nat} {w : Nat → Nat}
    (ih : AlignedFrom K a v s (F w) (k + 1))
    (h : ∀ t, F w (k + 2) ≤ t → a (k + 2) (t + s) = !Sp K v (k + 2) t)
    (hlow : ∀ j t, j ≤ k + 1 → Sp K v' j t = Sp K v j t) (hcomp : ∀ t, Sp K v' (k + 2) t = !Sp K v (k + 2) t) :
    AlignedFrom K a v' s (F w) (k + 2) := by
  intro j hj t ht
  rcases Nat.lt_or_ge j (k + 2) with hlt | hge
  · rw [ih j (by omega) t ht, hlow j t (by omega)]
  · have e : j = k + 2 := by omega
    subst e
    rw [h t ht, hcomp t]

/-- **Going up without a fork**, with the time carried: while every nearer word has a black, the same shift. -/
theorem extend_from {K : Nat} {a : Nat → Nat → Bool} {v s j0 J : Nat} {w : Nat → Nat} (ha : Recurrence a)
    (hv : rowAt K v 32 = v) (hw : Words K v w) (h1 : 1 ≤ j0) (hJ : J < K) (hj : j0 ≤ J)
    (hal : AlignedFrom K a v s (F w) j0) (hb : ∀ m, j0 ≤ m → m < J → w m ≠ 0) :
    AlignedFrom K a v s (F w) J := by
  have aux : ∀ n, j0 + n ≤ J → AlignedFrom K a v s (F w) (j0 + n) := by
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

/-- **Through wheel 53,207**, for a strip whose white wheels there are the four doubling wheels, with the time carried. -/
theorem low_from {K : Nat} {a : Nat → Nat → Bool} {v : Nat} {w : Nat → Nat} (hK : 53207 < K) (ha : Recurrence a)
    (ha0 : a 0 0 = true) (hv : rowAt K v 32 = v) (hw : Words K v w) (h0 : ∀ t, Sp K v 0 t = true)
    (h1 : ∀ t, Sp K v 1 t = true)
    (hbw : ∀ m, m < 53207 → w m ≠ 0 ∨ m = 2 ∨ m = 7 ∨ m = 28 ∨ m = 399)
    (hs2 : (∀ j, j ≤ 2 → ∀ t, Sp K v j (t + 1) = Sp K v j t) ∧ ∀ t, Sp K v (2 + 1) (t + 1) = !Sp K v (2 + 1) t)
    (hs7 : (∀ j, j ≤ 7 → ∀ t, Sp K v j (t + 2) = Sp K v j t) ∧ ∀ t, Sp K v (7 + 1) (t + 2) = !Sp K v (7 + 1) t)
    (hs28 : (∀ j, j ≤ 28 → ∀ t, Sp K v j (t + 4) = Sp K v j t) ∧ ∀ t, Sp K v (28 + 1) (t + 4) = !Sp K v (28 + 1) t)
    (hs399 : (∀ j, j ≤ 399 → ∀ t, Sp K v j (t + 8) = Sp K v j t) ∧
      ∀ t, Sp K v (399 + 1) (t + 8) = !Sp K v (399 + 1) t) :
    ∀ n, n ≤ 53207 → ∃ s, s ≤ lsum n ∧ AlignedFrom K a v s (F w) n
  | 0, _ => ⟨0, by simp [lsum], fun j hj t _ => by
      have e : j = 0 := by omega
      subst e
      show a 0 t = Sp K v 0 t
      rw [rec_zero ha ha0, h0]⟩
  | 1, _ => ⟨0, by simp [lsum], base_from ha ha0 h0 h1⟩
  | n + 2, hn => by
    obtain ⟨s, hs, ih⟩ := low_from hK ha ha0 hv hw h0 h1 hbw hs2 hs7 hs28 hs399 (n + 1) (by omega)
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

/-! ### The walk: the recursion as one arithmetic step per tick, at period 32 -/

/-- The cell of wheel `j` at tick `t` of the thirty-two-row cycle `R`, as a number. -/
def tb (R : Nat → Nat) (t j : Nat) : Nat := Nat.land (Nat.shiftRight (R (t % 32)) j) 1

/-- From wheel `j` at tick `t`, `n` ticks: a black cell moves on to the next wheel, a white one waits. -/
def walk (R : Nat → Nat) : Nat → Nat → Nat → Nat
  | 0, _, j => j
  | n + 1, t, j => walk R n (t + 1) (j + tb R t j)

theorem tb_eq (R : Nat → Nat) (t j : Nat) : tb R t j = ((R (t % 32)).testBit j).toNat := by
  show (R (t % 32) >>> j) &&& 1 = _
  rw [Nat.and_one_is_mod, Nat.shiftRight_eq_div_pow, Nat.testBit_eq_decide_div_mod_eq]
  rcases Nat.mod_two_eq_zero_or_one (R (t % 32) / 2 ^ j) with h | h <;> simp [h]

theorem walk_add (R : Nat → Nat) (x y : Nat) : ∀ t j, walk R (x + y) t j = walk R y (t + x) (walk R x t j) := by
  induction x with
  | zero => intro t j; simp [walk]
  | succ x ih =>
    intro t j
    have e : x + 1 + y = (x + y) + 1 := by omega
    rw [e]
    show walk R (x + y) (t + 1) (j + tb R t j) = walk R y (t + (x + 1)) (walk R x (t + 1) (j + tb R t j))
    rw [ih]
    have e2 : t + 1 + x = t + (x + 1) := by omega
    rw [e2]

theorem walk_one (R : Nat → Nat) (t j : Nat) : walk R 1 t j = j + tb R t j := rfl

theorem walk_end (R : Nat → Nat) (n t j : Nat) :
    walk R (n + 1) t j = walk R n t j + tb R (t + n) (walk R n t j) := by
  rw [walk_add, walk_one]

theorem walk_le_succ (R : Nat → Nat) (n t j : Nat) : walk R n t j ≤ walk R (n + 1) t j := by
  rw [walk_end]; omega

theorem walk_mono (R : Nat → Nat) (t j : Nat) {n m : Nat} (h : n ≤ m) : walk R n t j ≤ walk R m t j := by
  induction m with
  | zero =>
    have : n = 0 := by omega
    rw [this]; exact Nat.le_refl _
  | succ m ih =>
    rcases Nat.lt_or_ge n (m + 1) with h1 | h1
    · exact Nat.le_trans (ih (by omega)) (walk_le_succ R m t j)
    · have : n = m + 1 := by omega
      rw [this]; exact Nat.le_refl _

theorem le_walk (R : Nat → Nat) (n t j : Nat) : j ≤ walk R n t j :=
  walk_mono R t j (Nat.zero_le n)

/-- A wheel is reached at one tick only. -/
theorem arrival_unique (R : Nat → Nat) (t j : Nat) {n1 n2 J : Nat} (h1 : 1 ≤ n1) (h2 : 1 ≤ n2)
    (a1 : walk R n1 t j = J) (b1 : walk R (n1 - 1) t j + 1 = J)
    (a2 : walk R n2 t j = J) (b2 : walk R (n2 - 1) t j + 1 = J) : n1 = n2 := by
  rcases Nat.lt_trichotomy n1 n2 with h | h | h
  · have := walk_mono R t j (show n1 ≤ n2 - 1 by omega)
    omega
  · exact h
  · have := walk_mono R t j (show n2 ≤ n1 - 1 by omega)
    omega

section words
variable {R w : Nat → Nat}

theorem tb_word (hR : ∀ j r, r < 32 → (w j).testBit r = (R r).testBit j) (t j : Nat) :
    tb R t j = ((w j).testBit (t % 32)).toNat := by
  rw [tb_eq, hR j (t % 32) (Nat.mod_lt _ (by decide))]

/-- A wheel with no black cell at the next `n` ticks waits. -/
theorem walk_stay (hR : ∀ j r, r < 32 → (w j).testBit r = (R r).testBit j) {j : Nat} :
    ∀ n t, (∀ i, i < n → (w j).testBit ((t + i) % 32) = false) → walk R n t j = j := by
  intro n
  induction n with
  | zero => intro t _; rfl
  | succ n ih =>
    intro t h
    have h0 := h 0 (by omega)
    have e : tb R t j = 0 := by
      rw [tb_word hR]; rw [Nat.add_zero] at h0; rw [h0]; rfl
    show walk R n (t + 1) (j + tb R t j) = j
    rw [e, Nat.add_zero]
    apply ih
    intro i hi
    have := h (i + 1) (by omega)
    have e2 : t + (i + 1) = t + 1 + i := by omega
    rw [e2] at this
    exact this

theorem srch_min (x m : Nat) : ∀ fuel, fuel ≤ 32 → ∀ i, 32 - fuel ≤ i → i < srch x m fuel →
    x.testBit ((m + i) % 32) = false
  | 0, _, i, _, h => by
    have : srch x m 0 = 32 := rfl
    omega
  | fuel + 1, hf, i, h1, h2 => by
    simp only [srch] at h2
    split at h2
    · omega
    · rename_i hb
      rcases Nat.lt_or_ge i (32 - fuel) with hlt | hge
      · have e : i = 32 - (fuel + 1) := by omega
        subst e
        simpa using hb
      · exact srch_min x m fuel (by omega) i hge h2

/-- At a black wheel the wait of `srch` is the walk. -/
theorem walk_srch (hR : ∀ j r, r < 32 → (w j).testBit r = (R r).testBit j) (hw : ∀ j, w j < 2 ^ 32) {j : Nat}
    (hb : w j ≠ 0) (m : Nat) :
    walk R (srch (w j) m 32) m j = j ∧ walk R (srch (w j) m 32 + 1) m j = j + 1 := by
  have h1 : walk R (srch (w j) m 32) m j = j :=
    walk_stay hR _ m (fun i hi => srch_min (w j) m 32 (Nat.le_refl _) i (Nat.zero_le _) hi)
  refine ⟨h1, ?_⟩
  rw [walk_end, h1, tb_word hR, srch_black (w j) m (bit_of_ne (hw j) hb)]
  rfl

/-- A wheel the walk has passed is black. -/
theorem walk_black (hR : ∀ j r, r < 32 → (w j).testBit r = (R r).testBit j) :
    ∀ n t j j', j ≤ j' → j' < walk R n t j → w j' ≠ 0 := by
  intro n
  induction n with
  | zero => intro t j j' h1 h2; exact absurd h2 (by show ¬ j' < j; omega)
  | succ n ih =>
    intro t j j' h1 h2
    have e : walk R (n + 1) t j = walk R n (t + 1) (j + tb R t j) := rfl
    rw [e] at h2
    by_cases hb : (w j).testBit (t % 32) = true
    · have t1 : tb R t j = 1 := by rw [tb_word hR, hb]; rfl
      rw [t1] at h2
      rcases Nat.lt_or_ge j j' with hlt | hge
      · exact ih (t + 1) (j + 1) j' (by omega) h2
      · have : j' = j := by omega
        subst this
        intro h0
        rw [h0, Nat.zero_testBit] at hb
        cases hb
    · have t0 : tb R t j = 0 := by
        rw [tb_word hR]
        cases hc : (w j).testBit (t % 32)
        · rfl
        · exact absurd hc hb
      rw [t0, Nat.add_zero] at h2
      exact ih (t + 1) j j' h1 h2

theorem frun_last (v : Nat → Nat) (i n : Nat) (st : Nat × Nat) :
    frun v i (n + 1) st = fstep v (i + n) (frun v i n st) := by
  rw [frun_add]; rfl

/-- The recursion from a state `(a, b)` with `a ≤ b` is the walk from wheel `j0 + 1` at tick `b`: the second front after `n`
black wheels is the tick at which the walk reaches wheel `j0 + 1 + n`. -/
theorem run_arrival (hR : ∀ j r, r < 32 → (w j).testBit r = (R r).testBit j) (hw : ∀ j, w j < 2 ^ 32)
    {j0 a b : Nat} (hab : a ≤ b) : ∀ n, (∀ i, i < n → w (j0 + 1 + i) ≠ 0) →
    (frun w j0 n (a, b)).1 ≤ (frun w j0 n (a, b)).2 ∧ b ≤ (frun w j0 n (a, b)).2 ∧
    walk R ((frun w j0 n (a, b)).2 - b) b (j0 + 1) = j0 + 1 + n ∧
    (1 ≤ n → b + 1 ≤ (frun w j0 n (a, b)).2 ∧
      walk R ((frun w j0 n (a, b)).2 - b - 1) b (j0 + 1) + 1 = j0 + 1 + n) := by
  intro n
  induction n with
  | zero =>
    intro _
    refine ⟨hab, Nat.le_refl _, ?_, fun h => absurd h (by omega)⟩
    show walk R (b - b) b (j0 + 1) = j0 + 1 + 0
    rw [Nat.sub_self]; rfl
  | succ n ih =>
    intro hbl
    obtain ⟨c1, c2, c3, _⟩ := ih (fun i hi => hbl i (by omega))
    rw [frun_last]
    generalize hst : frun w j0 n (a, b) = st at c1 c2 c3 ⊢
    obtain ⟨x, y⟩ := st
    simp only at c1 c2 c3
    have hb : w (j0 + n + 1) ≠ 0 := by
      have := hbl n (by omega)
      have e : j0 + 1 + n = j0 + n + 1 := by omega
      rw [e] at this
      exact this
    have hmax : max x y = y := Nat.max_eq_right c1
    have hf : fstep w (j0 + n) (x, y) = (y, y + srch (w (j0 + n + 1)) y 32 + 1) := by
      simp only [fstep, hb, ite_false, hmax]
    rw [hf]
    obtain ⟨k1, k2⟩ := walk_srch hR hw hb y
    generalize srch (w (j0 + n + 1)) y 32 = k at k1 k2
    simp only
    have e0 : b + (y - b) = y := by omega
    have e1 : y + k + 1 - b = (y - b) + (k + 1) := by omega
    have e2 : y + k + 1 - b - 1 = (y - b) + k := by omega
    have e3 : j0 + 1 + n = j0 + n + 1 := by omega
    refine ⟨by omega, by omega, ?_, fun _ => ⟨by omega, ?_⟩⟩
    · rw [e1, walk_add, c3, e0, e3, k2]; omega
    · rw [e2, walk_add, c3, e0, e3, k1]; omega

/-- **A block of black wheels by the walk.** Four facts about the walk fix the state after `n ≥ 2` wheels. -/
theorem frun_of_walk (hR : ∀ j r, r < 32 → (w j).testBit r = (R r).testBit j) (hw : ∀ j, w j < 2 ^ 32)
    {j0 n a b A B : Nat} (hab : a ≤ b) (hn : 2 ≤ n) (hA : b < A) (hB : A < B)
    (f1 : walk R (A - 1 - b) b (j0 + 1) = j0 + n - 1) (f2 : tb R (A - 1) (j0 + n - 1) = 1)
    (f3 : walk R (B - 1 - A) A (j0 + n) = j0 + n) (f4 : tb R (B - 1) (j0 + n) = 1) :
    frun w j0 n (a, b) = (A, B) := by
  have eA : A - b = (A - 1 - b) + 1 := by omega
  have eB1 : B - 1 - b = (A - b) + (B - 1 - A) := by omega
  have eB : B - b = (B - 1 - b) + 1 := by omega
  have wA1 : walk R (A - 1 - b) b (j0 + 1) = j0 + n - 1 := f1
  have wA : walk R (A - b) b (j0 + 1) = j0 + n := by
    rw [eA, walk_end, wA1]
    have e : b + (A - 1 - b) = A - 1 := by omega
    rw [e, f2]; omega
  have wB1 : walk R (B - 1 - b) b (j0 + 1) = j0 + n := by
    rw [eB1, walk_add, wA]
    have e : b + (A - b) = A := by omega
    rw [e, f3]
  have wB : walk R (B - b) b (j0 + 1) = j0 + 1 + n := by
    rw [eB, walk_end, wB1]
    have e : b + (B - 1 - b) = B - 1 := by omega
    rw [e, f4]; omega
  have hbl : ∀ i, i < n → w (j0 + 1 + i) ≠ 0 := fun i hi =>
    walk_black hR (B - b) b (j0 + 1) (j0 + 1 + i) (by omega) (by rw [wB]; omega)
  obtain ⟨c1, c2, c3, c4⟩ := run_arrival hR hw hab n hbl
  obtain ⟨d1, d2, d3, d4⟩ := run_arrival hR hw hab (n - 1) (fun i hi => hbl i (by omega))
  obtain ⟨c5, c6⟩ := c4 (by omega)
  obtain ⟨d5, d6⟩ := d4 (by omega)
  have hy : (frun w j0 n (a, b)).2 - b = B - b :=
    arrival_unique R b (j0 + 1) (J := j0 + 1 + n) (by omega) (by omega) c3 c6 wB
      (by rw [show B - b - 1 = B - 1 - b by omega, wB1]; omega)
  have hy' : (frun w j0 (n - 1) (a, b)).2 - b = A - b := by
    have e : j0 + 1 + (n - 1) = j0 + n := by omega
    rw [e] at d3 d6
    exact arrival_unique R b (j0 + 1) (J := j0 + n) (by omega) (by omega) d3 d6 wA
      (by rw [show A - b - 1 = A - 1 - b by omega, wA1]; omega)
  have hlast : frun w j0 n (a, b) = fstep w (j0 + (n - 1)) (frun w j0 (n - 1) (a, b)) := by
    have e : n = (n - 1) + 1 := by omega
    conv => lhs; rw [e]
    rw [frun_last]
  have h1 : (frun w j0 n (a, b)).1 = A := by
    rw [hlast, fstep_fst]; omega
  have h2 : (frun w j0 n (a, b)).2 = B := by omega
  exact Prod.ext h1 h2

/-- A white wheel leaves the second front where it is. -/
theorem frun_white {j a b : Nat} (hab : a ≤ b) (h0 : w (j + 1) = 0) : frun w j 1 (a, b) = (b, b) := by
  show fstep w j (a, b) = (b, b)
  simp only [fstep, h0, ite_true, Nat.max_eq_right hab]

end words

/-! ### Thirty-two ticks at a time -/

/-- One tick of a row `x`. -/
def s (x j : Nat) : Nat := Nat.add j (Nat.land (Nat.shiftRight x j) 1)

/-- Thirty-two ticks from a tick that is a multiple of thirty-two. -/
def st32 (R : Nat → Nat) (j : Nat) : Nat :=
  s (R 31) (s (R 30) (s (R 29) (s (R 28) (s (R 27) (s (R 26) (s (R 25) (s (R 24) (s (R 23) (s (R 22) (s (R 21) (s (R 20) (s (R 19) (s (R 18) (s (R 17) (s (R 16) (s (R 15) (s (R 14) (s (R 13) (s (R 12) (s (R 11) (s (R 10) (s (R 9) (s (R 8) (s (R 7) (s (R 6) (s (R 5) (s (R 4) (s (R 3) (s (R 2) (s (R 1) (s (R 0) (j))))))))))))))))))))))))))))))))

/-- `32 g` ticks. The test forces the value at each round, so the kernel's recursion stays shallow; it is never true. -/
def w32 (R : Nat → Nat) : Nat → Nat → Nat
  | 0, j => j
  | g + 1, j => cond (Nat.beq (st32 R j) 0) 0 (w32 R g (st32 R j))

theorem s_eq (R : Nat → Nat) {t i : Nat} (h : t % 32 = i) (j : Nat) : s (R i) j = j + tb R t j := by
  show Nat.add j (Nat.land (Nat.shiftRight (R i) j) 1) = j + Nat.land (Nat.shiftRight (R (t % 32)) j) 1
  rw [h]; rfl

theorem st32_walk (R : Nat → Nat) {t : Nat} (ht : t % 32 = 0) (j : Nat) : st32 R j = walk R 32 t j := by
  have wk : ∀ i, i < 32 → walk R (i + 1) t j = s (R i) (walk R i t j) := fun i hi => by
    rw [walk_end, s_eq R (t := t + i) (i := i) (by omega) (walk R i t j)]
  have e1 : walk R 1 t j = s (R 0) (walk R 0 t j) := wk 0 (by omega)
  have e2 : walk R 2 t j = s (R 1) (walk R 1 t j) := wk 1 (by omega)
  have e3 : walk R 3 t j = s (R 2) (walk R 2 t j) := wk 2 (by omega)
  have e4 : walk R 4 t j = s (R 3) (walk R 3 t j) := wk 3 (by omega)
  have e5 : walk R 5 t j = s (R 4) (walk R 4 t j) := wk 4 (by omega)
  have e6 : walk R 6 t j = s (R 5) (walk R 5 t j) := wk 5 (by omega)
  have e7 : walk R 7 t j = s (R 6) (walk R 6 t j) := wk 6 (by omega)
  have e8 : walk R 8 t j = s (R 7) (walk R 7 t j) := wk 7 (by omega)
  have e9 : walk R 9 t j = s (R 8) (walk R 8 t j) := wk 8 (by omega)
  have e10 : walk R 10 t j = s (R 9) (walk R 9 t j) := wk 9 (by omega)
  have e11 : walk R 11 t j = s (R 10) (walk R 10 t j) := wk 10 (by omega)
  have e12 : walk R 12 t j = s (R 11) (walk R 11 t j) := wk 11 (by omega)
  have e13 : walk R 13 t j = s (R 12) (walk R 12 t j) := wk 12 (by omega)
  have e14 : walk R 14 t j = s (R 13) (walk R 13 t j) := wk 13 (by omega)
  have e15 : walk R 15 t j = s (R 14) (walk R 14 t j) := wk 14 (by omega)
  have e16 : walk R 16 t j = s (R 15) (walk R 15 t j) := wk 15 (by omega)
  have e17 : walk R 17 t j = s (R 16) (walk R 16 t j) := wk 16 (by omega)
  have e18 : walk R 18 t j = s (R 17) (walk R 17 t j) := wk 17 (by omega)
  have e19 : walk R 19 t j = s (R 18) (walk R 18 t j) := wk 18 (by omega)
  have e20 : walk R 20 t j = s (R 19) (walk R 19 t j) := wk 19 (by omega)
  have e21 : walk R 21 t j = s (R 20) (walk R 20 t j) := wk 20 (by omega)
  have e22 : walk R 22 t j = s (R 21) (walk R 21 t j) := wk 21 (by omega)
  have e23 : walk R 23 t j = s (R 22) (walk R 22 t j) := wk 22 (by omega)
  have e24 : walk R 24 t j = s (R 23) (walk R 23 t j) := wk 23 (by omega)
  have e25 : walk R 25 t j = s (R 24) (walk R 24 t j) := wk 24 (by omega)
  have e26 : walk R 26 t j = s (R 25) (walk R 25 t j) := wk 25 (by omega)
  have e27 : walk R 27 t j = s (R 26) (walk R 26 t j) := wk 26 (by omega)
  have e28 : walk R 28 t j = s (R 27) (walk R 27 t j) := wk 27 (by omega)
  have e29 : walk R 29 t j = s (R 28) (walk R 28 t j) := wk 28 (by omega)
  have e30 : walk R 30 t j = s (R 29) (walk R 29 t j) := wk 29 (by omega)
  have e31 : walk R 31 t j = s (R 30) (walk R 30 t j) := wk 30 (by omega)
  have e32 : walk R 32 t j = s (R 31) (walk R 31 t j) := wk 31 (by omega)
  rw [e32, e31, e30, e29, e28, e27, e26, e25, e24, e23, e22, e21, e20, e19, e18, e17, e16, e15, e14, e13, e12, e11, e10, e9, e8, e7, e6, e5, e4, e3, e2, e1]
  rfl

theorem w32_walk (R : Nat → Nat) : ∀ g t j, t % 32 = 0 → 1 ≤ j → w32 R g j = walk R (32 * g) t j := by
  intro g
  induction g with
  | zero => intro t j _ _; rfl
  | succ g ih =>
    intro t j ht hj
    have e := st32_walk R ht j
    have hp : 1 ≤ st32 R j := by
      rw [e]; exact Nat.le_trans hj (le_walk R 32 t j)
    have hb : Nat.beq (st32 R j) 0 = false := by
      cases h : st32 R j with
      | zero => omega
      | succ q => rfl
    show cond (Nat.beq (st32 R j) 0) 0 (w32 R g (st32 R j)) = _
    rw [hb]
    show w32 R g (st32 R j) = _
    rw [ih (t + 32) (st32 R j) (by omega) hp, e, ← walk_add]
    have : 32 + 32 * g = 32 * (g + 1) := by omega
    rw [this]

/-- A head of `h` ticks up to a multiple of thirty-two, `32 g` ticks, and a tail of `d` ticks. -/
def fastWalk (R : Nat → Nat) (h g d t j : Nat) : Nat :=
  walk R d (t + h + 32 * g) (w32 R g (walk R h t j))

theorem fastWalk_eq (R : Nat → Nat) {h g d t j : Nat} (ht : (t + h) % 32 = 0) (hj : 1 ≤ j) :
    fastWalk R h g d t j = walk R (h + (32 * g + d)) t j := by
  show walk R d (t + h + 32 * g) (w32 R g (walk R h t j)) = _
  rw [w32_walk R g (t + h) _ ht (Nat.le_trans hj (le_walk R h t j)), ← walk_add, ← walk_add]

/-- The rounds compose. -/
theorem w32_add (R : Nat → Nat) (g1 g2 j : Nat) (hj : 1 ≤ j) : w32 R (g1 + g2) j = w32 R g2 (w32 R g1 j) := by
  rw [w32_walk R (g1 + g2) 0 j rfl hj, w32_walk R g1 0 j rfl hj,
    w32_walk R g2 (32 * g1) (walk R (32 * g1) 0 j) (by omega) (Nat.le_trans hj (le_walk R _ 0 j))]
  rw [Nat.mul_add, walk_add, Nat.zero_add]

/-- A chain of blocks of rounds. -/
theorem w32_chain (R : Nat → Nat) {g1 g2 j j' j'' : Nat} (hj : 1 ≤ j) (h1 : w32 R g1 j = j')
    (h2 : w32 R g2 j' = j'') : w32 R (g1 + g2) j = j'' := by
  rw [w32_add R g1 g2 j hj, h1, h2]

/-- A head, a chain of blocks and a tail give the fast walk. -/
theorem fastWalk_of (R : Nat → Nat) {h g d t j j1 j2 J : Nat} (hh : walk R h t j = j1) (hg : w32 R g j1 = j2)
    (hd : walk R d (t + h + 32 * g) j2 = J) : fastWalk R h g d t j = J := by
  unfold fastWalk
  rw [hh, hg, hd]

/-- A black run of a strip by the walk, with the long stretch thirty-two ticks at a time. -/
theorem seg_black {K v j0 n a b A B h g d : Nat} (hab : a ≤ b) (hn : 2 ≤ n) (hA : b < A) (hB : A < B)
    (e : A - 1 - b = h + (32 * g + d)) (ht : (b + h) % 32 = 0)
    (k1 : fastWalk (rowAt K v) h g d b (j0 + 1) = j0 + n - 1)
    (f2 : tb (rowAt K v) (A - 1) (j0 + n - 1) = 1)
    (f3 : walk (rowAt K v) (B - 1 - A) A (j0 + n) = j0 + n)
    (f4 : tb (rowAt K v) (B - 1) (j0 + n) = 1) : frun (wd K v) j0 n (a, b) = (A, B) :=
  frun_of_walk (wd_row K v) (wd_lt K v) hab hn hA hB
    (by rw [e, ← fastWalk_eq _ ht (by omega)]; exact k1) f2 f3 f4

/-! ### Two strips are not one -/

/-- Two strips related by a time shift through wheel `J`. -/
def Related (K J v v' : Nat) : Prop := ∃ s, ∀ j, j ≤ J → ∃ T, ∀ t, T ≤ t → Sp K v j (t + s) = Sp K v' j t

/-- Strips that are complements at a wheel `w` and agree at a wheel `p` of primitive period 16 are unrelated, on per-wheel
periods: wheels `w` and `p` of `v` and wheel `p` of `v'` repeat after 16 ticks. -/
theorem not_related {K J v v' w p : Nat} (hw : w ≤ J) (hp : p ≤ J)
    (hvw : ∀ t, Sp K v w (t + 16) = Sp K v w t) (hvp : ∀ t, Sp K v p (t + 16) = Sp K v p t)
    (hv'p : ∀ t, Sp K v' p (t + 16) = Sp K v' p t)
    (hc : ∀ t, Sp K v w t = !Sp K v' w t) (h4 : ∀ t, Sp K v p t = Sp K v' p t)
    (hprim : ∀ d, d < 16 → d ≠ 0 → ∃ q, q < 16 ∧ Sp K v p (q + d) ≠ Sp K v p q) : ¬ Related K J v v' := by
  rintro ⟨s, hs⟩
  obtain ⟨T1, h400⟩ := hs p hp
  obtain ⟨T2, htop⟩ := hs w hw
  by_cases hd : s % 16 = 0
  · have e := htop T2 (Nat.le_refl _)
    have pw : Sp K v w (T2 + s) = Sp K v w T2 := by
      have h := per_mul hvw T2 (s / 16)
      rwa [show T2 + s / 16 * 16 = T2 + s by omega] at h
    rw [pw, hc T2] at e
    cases h : Sp K v' w T2 <;> simp [h] at e
  · obtain ⟨q, hq, hne⟩ := hprim (s % 16) (Nat.mod_lt _ (by omega)) hd
    have e := h400 (q + T1 * 16) (by omega)
    have e1 : Sp K v p (q + T1 * 16 + s) = Sp K v p (q + s % 16) := by
      have h := per_mul hvp (q + s % 16) (T1 + s / 16)
      rwa [show q + s % 16 + (T1 + s / 16) * 16 = q + T1 * 16 + s by omega] at h
    rw [e1, per_mul hv'p q T1, ← h4 q] at e
    exact hne e

/-- Two alignments of one array relate their strips. -/
theorem side_unique {K J : Nat} {a : Nat → Nat → Bool} {v v' s s' : Nat} (hv' : rowAt K v' 32 = v')
    (h : Aligned K a v s J) (h' : Aligned K a v' s' J) : Related K J v v' := by
  refine ⟨s' + 31 * s, fun j hj => ?_⟩
  obtain ⟨T, hT⟩ := h j hj
  obtain ⟨T', hT'⟩ := h' j hj
  refine ⟨T + T', fun t ht => ?_⟩
  have a1 := hT (t + (s' + 31 * s)) (by omega)
  have a2 := hT' (t + 32 * s) (by omega)
  rw [← a1, show t + (s' + 31 * s) + s = t + 32 * s + s' by omega, a2,
    show t + 32 * s = t + s * 32 by omega, Sp_add_mul hv']

end Ruliology.CellularAutomata.Rule30FiveFrontsBase
