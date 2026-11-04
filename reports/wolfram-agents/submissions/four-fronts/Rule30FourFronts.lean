module

public import Ruliology.CellularAutomata.Rule30FourFrontsBase

/-!
# The forced front on the four strips: every configuration with a leftmost black cell is on its strip through wheel 87,866 by an explicit tick

`Rule30FourLeftSides` placed every configuration with a leftmost black cell on one of four strips through wheel 87,866, after
a time shift and from some time on. This module makes the time explicit, as `Rule30ForcedFront` did below the first fork. The
settling recursion of `Rule30FrontLaw` (`frontBound`), run in strip time on each strip's sixteen-row cycle, gives a tick
`F j` for every wheel; the induction of `Rule30FourLeftSides` with the time carried (`Rule30FourFrontsBase`) shows that wheel
`j` of every array with the recurrence and a black start carries its strip from `F j` on, at a shift of at most `15`
(`forced_front_four`). The recursion's values come from the walk below: from wheel `j` at tick `t`, move to wheel `j + 1` if the
strip's cell is black and stay if it is white, the tick moving on either way (`walk`, `frun_of_walk`). That is one addition, one
shift and one mask per tick, so the kernel runs all four strips in seconds. At wheel 87,866 the fronts are 176,968 (A0), 177,229
(A1), 177,170 (B0) and 177,560 (B1). Since the fronts are monotone, every such array carries the whole of its strip through wheel 87,866 from strip tick 177,560, that is from
tick at most 177,575 of its own clock (`forced_front_four_uniform`, `forced_front_four_left_side`, `forced_front_four_seed`).
The linear bound `1 + 16 j`, the form of the kit's `frontBound_le_linear` at period 16, is 1,405,857 at that wheel. Across a fork the front is carried by
`F_congr`: the two strips agree below the fork wheel, so their recursions agree through it. Cloud (CL734), the walk Local (L1524),
after `Rule30FourLeftSides` (L1513), `Rule30ForcedFront` (CL733) and the kit's `Rule30FrontLaw`.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30FourFronts

open Rule30FourFrontsBase
open Rule30AgedLeftDiagonals Rule30FiniteDiagonals Rule30Diagonals Rule30Realization
open Rule30UniversalLeftSide (rowAt)
open Rule30FourLeftSides (Sp A0 A1 B0 B1 A0_return A1_return B0_return B1_return A0_zero A0_one black_or_white
  strip_shift per2 anti2 per7 anti7 per28 anti28 per399 anti399 white_53207 white_58286 white_72575
  low_B0 low_A1 low_B1 top_B0 top_A1 top_B1 wA0_low wA0_high wA1_high wB0_low wB0_high wB1_high
  low_of_phase comp_of_phase Aligned)

set_option autoImplicit false

/-! ### The walk: the recursion as one arithmetic step per tick -/

/-- The cell of wheel `j` at tick `t` of the sixteen-row cycle `R`, as a number. -/
def tb (R : Nat → Nat) (t j : Nat) : Nat := Nat.land (Nat.shiftRight (R (t % 16)) j) 1

/-- From wheel `j` at tick `t`, `n` ticks: a black cell moves on to the next wheel, a white one waits. -/
def walk (R : Nat → Nat) : Nat → Nat → Nat → Nat
  | 0, _, j => j
  | n + 1, t, j => walk R n (t + 1) (j + tb R t j)

theorem tb_eq (R : Nat → Nat) (t j : Nat) : tb R t j = ((R (t % 16)).testBit j).toNat := by
  show (R (t % 16) >>> j) &&& 1 = _
  rw [Nat.and_one_is_mod, Nat.shiftRight_eq_div_pow, Nat.testBit_eq_decide_div_mod_eq]
  rcases Nat.mod_two_eq_zero_or_one (R (t % 16) / 2 ^ j) with h | h <;> simp [h]

theorem tb_le (R : Nat → Nat) (t j : Nat) : tb R t j ≤ 1 := by
  rw [tb_eq]; exact Bool.toNat_le _

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
  | zero => have : n = 0 := by omega
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

theorem tb_word (hR : ∀ j r, r < 16 → (w j).testBit r = (R r).testBit j) (t j : Nat) :
    tb R t j = ((w j).testBit (t % 16)).toNat := by
  rw [tb_eq, hR j (t % 16) (Nat.mod_lt _ (by decide))]

/-- A wheel with no black cell at the next `n` ticks waits. -/
theorem walk_stay (hR : ∀ j r, r < 16 → (w j).testBit r = (R r).testBit j) {j : Nat} :
    ∀ n t, (∀ i, i < n → (w j).testBit ((t + i) % 16) = false) → walk R n t j = j := by
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

theorem srch_min (x m : Nat) : ∀ fuel, fuel ≤ 16 → ∀ i, 16 - fuel ≤ i → i < srch x m fuel →
    x.testBit ((m + i) % 16) = false
  | 0, _, i, _, h => by
    have : srch x m 0 = 16 := rfl
    omega
  | fuel + 1, hf, i, h1, h2 => by
    simp only [srch] at h2
    split at h2
    · omega
    · rename_i hb
      rcases Nat.lt_or_ge i (16 - fuel) with hlt | hge
      · have e : i = 16 - (fuel + 1) := by omega
        subst e
        simpa using hb
      · exact srch_min x m fuel (by omega) i hge h2

/-- At a black wheel the wait of `srch` is the walk. -/
theorem walk_srch (hR : ∀ j r, r < 16 → (w j).testBit r = (R r).testBit j) (hw : ∀ j, w j < 2 ^ 16) {j : Nat}
    (hb : w j ≠ 0) (m : Nat) :
    walk R (srch (w j) m 16) m j = j ∧ walk R (srch (w j) m 16 + 1) m j = j + 1 := by
  have h1 : walk R (srch (w j) m 16) m j = j :=
    walk_stay hR _ m (fun i hi => srch_min (w j) m 16 (Nat.le_refl _) i (Nat.zero_le _) hi)
  refine ⟨h1, ?_⟩
  rw [walk_end, h1, tb_word hR, srch_black (w j) m (bit_of_ne (hw j) hb)]
  rfl

/-- A wheel the walk has passed is black. -/
theorem walk_black (hR : ∀ j r, r < 16 → (w j).testBit r = (R r).testBit j) :
    ∀ n t j j', j ≤ j' → j' < walk R n t j → w j' ≠ 0 := by
  intro n
  induction n with
  | zero => intro t j j' h1 h2; exact absurd h2 (by show ¬ j' < j; omega)
  | succ n ih =>
    intro t j j' h1 h2
    have e : walk R (n + 1) t j = walk R n (t + 1) (j + tb R t j) := rfl
    rw [e] at h2
    by_cases hb : (w j).testBit (t % 16) = true
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
        cases hc : (w j).testBit (t % 16)
        · rfl
        · exact absurd hc hb
      rw [t0, Nat.add_zero] at h2
      exact ih (t + 1) j j' h1 h2

theorem frun_last (v : Nat → Nat) (i n : Nat) (st : Nat × Nat) :
    frun v i (n + 1) st = fstep v (i + n) (frun v i n st) := by
  rw [frun_add]; rfl

/-- The recursion from a state `(a, b)` with `a ≤ b` is the walk from wheel `j0 + 1` at tick `b`: the second front after `n` black
wheels is the tick at which the walk reaches wheel `j0 + 1 + n`. -/
theorem run_arrival (hR : ∀ j r, r < 16 → (w j).testBit r = (R r).testBit j) (hw : ∀ j, w j < 2 ^ 16)
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
    have hf : fstep w (j0 + n) (x, y) = (y, y + srch (w (j0 + n + 1)) y 16 + 1) := by
      simp only [fstep, hb, ite_false, hmax]
    rw [hf]
    obtain ⟨k1, k2⟩ := walk_srch hR hw hb y
    generalize srch (w (j0 + n + 1)) y 16 = k at k1 k2
    simp only
    have e0 : b + (y - b) = y := by omega
    have e1 : y + k + 1 - b = (y - b) + (k + 1) := by omega
    have e2 : y + k + 1 - b - 1 = (y - b) + k := by omega
    have e3 : j0 + 1 + n = j0 + n + 1 := by omega
    refine ⟨by omega, by omega, ?_, fun _ => ⟨by omega, ?_⟩⟩
    · rw [e1, walk_add, c3, e0, e3, k2]; omega
    · rw [e2, walk_add, c3, e0, e3, k1]; omega

/-- **A block of black wheels by the walk.** Four facts about the walk fix the state after `n ≥ 2` wheels; the wheels need not be known
to be black, since the walk passes them. -/
theorem frun_of_walk (hR : ∀ j r, r < 16 → (w j).testBit r = (R r).testBit j) (hw : ∀ j, w j < 2 ^ 16)
    {j0 n a b A B : Nat} (hab : a ≤ b) (hn : 2 ≤ n) (hA : b < A) (hB : A < B)
    (f1 : walk R (A - 1 - b) b (j0 + 1) = j0 + n - 1) (f2 : tb R (A - 1) (j0 + n - 1) = 1)
    (f3 : walk R (B - 1 - A) A (j0 + n) = j0 + n) (f4 : tb R (B - 1) (j0 + n) = 1) :
    frun w j0 n (a, b) = (A, B) := by
  -- the walk from the start at the four ticks
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
  -- every wheel of the block is black
  have hbl : ∀ i, i < n → w (j0 + 1 + i) ≠ 0 := fun i hi =>
    walk_black hR (B - b) b (j0 + 1) (j0 + 1 + i) (by omega) (by rw [wB]; omega)
  obtain ⟨c1, c2, c3, c4⟩ := run_arrival hR hw hab n hbl
  obtain ⟨d1, d2, d3, d4⟩ := run_arrival hR hw hab (n - 1) (fun i hi => hbl i (by omega))
  obtain ⟨c5, c6⟩ := c4 (by omega)
  obtain ⟨d5, d6⟩ := d4 (by omega)
  -- the two fronts are the two arrivals
  have hy : (frun w j0 n (a, b)).2 - b = B - b :=
    arrival_unique R b (j0 + 1) (J := j0 + 1 + n) (by omega) (by omega) c3 c6 wB (by rw [show B - b - 1 = B - 1 - b by omega, wB1]; omega)
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

/-! ### Sixteen ticks at a time -/

/-- One tick of a row `x`. -/
def s (x j : Nat) : Nat := Nat.add j (Nat.land (Nat.shiftRight x j) 1)

/-- Sixteen ticks from a tick that is a multiple of sixteen. -/
def st16 (R : Nat → Nat) (j : Nat) : Nat :=
  s (R 15) (s (R 14) (s (R 13) (s (R 12) (s (R 11) (s (R 10) (s (R 9) (s (R 8) (s (R 7) (s (R 6) (s (R 5) (s (R 4)
    (s (R 3) (s (R 2) (s (R 1) (s (R 0) j)))))))))))))))

/-- `16 g` ticks. The test forces the value at each round, so the kernel's recursion stays shallow; it is never true. -/
def w16 (R : Nat → Nat) : Nat → Nat → Nat
  | 0, j => j
  | g + 1, j => cond (Nat.beq (st16 R j) 0) 0 (w16 R g (st16 R j))

theorem s_eq (R : Nat → Nat) {t i : Nat} (h : t % 16 = i) (j : Nat) : s (R i) j = j + tb R t j := by
  show Nat.add j (Nat.land (Nat.shiftRight (R i) j) 1) = j + Nat.land (Nat.shiftRight (R (t % 16)) j) 1
  rw [h]; rfl

theorem st16_walk (R : Nat → Nat) {t : Nat} (ht : t % 16 = 0) (j : Nat) : st16 R j = walk R 16 t j := by
  have wk : ∀ i, i < 16 → walk R (i + 1) t j = s (R i) (walk R i t j) := fun i hi => by
    rw [walk_end, s_eq R (t := t + i) (i := i) (by omega) (walk R i t j)]
  have e1 : walk R 1 t j = s (R 0) j := wk 0 (by omega)
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
  rw [e16, e15, e14, e13, e12, e11, e10, e9, e8, e7, e6, e5, e4, e3, e2, e1]
  rfl

theorem w16_walk (R : Nat → Nat) : ∀ g t j, t % 16 = 0 → 1 ≤ j → w16 R g j = walk R (16 * g) t j := by
  intro g
  induction g with
  | zero => intro t j _ _; rfl
  | succ g ih =>
    intro t j ht hj
    have e := st16_walk R ht j
    have hp : 1 ≤ st16 R j := by
      rw [e]; exact Nat.le_trans hj (le_walk R 16 t j)
    have hb : Nat.beq (st16 R j) 0 = false := by
      cases h : st16 R j with
      | zero => omega
      | succ q => rfl
    show cond (Nat.beq (st16 R j) 0) 0 (w16 R g (st16 R j)) = _
    rw [hb]
    show w16 R g (st16 R j) = _
    rw [ih (t + 16) (st16 R j) (by omega) hp, e, ← walk_add]
    have : 16 + 16 * g = 16 * (g + 1) := by omega
    rw [this]

/-- A head of `h` ticks up to a multiple of sixteen, `16 g` ticks, and a tail of `d` ticks. -/
def fastWalk (R : Nat → Nat) (h g d t j : Nat) : Nat :=
  walk R d (t + h + 16 * g) (w16 R g (walk R h t j))

theorem fastWalk_eq (R : Nat → Nat) {h g d t j : Nat} (ht : (t + h) % 16 = 0) (hj : 1 ≤ j) :
    fastWalk R h g d t j = walk R (h + (16 * g + d)) t j := by
  show walk R d (t + h + 16 * g) (w16 R g (walk R h t j)) = _
  rw [w16_walk R g (t + h) _ ht (Nat.le_trans hj (le_walk R h t j)), ← walk_add, ← walk_add]

/-! ### The words of the four strips -/

/-- The sixteen-bit word of wheel `j` of the strip of `v`: bit `r` is the wheel at phase `r`. -/
def wd (v j : Nat) : Nat := word16 (fun r => (rowAt 87867 v r).testBit j)

abbrev wdA0 : Nat → Nat := wd A0
abbrev wdA1 : Nat → Nat := wd A1
abbrev wdB0 : Nat → Nat := wd B0
abbrev wdB1 : Nat → Nat := wd B1

theorem wd_row (v : Nat) : ∀ j r, r < 16 → (wd v j).testBit r = (rowAt 87867 v r).testBit j := fun _ r hr =>
  word16_bit _ r hr

theorem wd_lt (v j : Nat) : wd v j < 2 ^ 16 := word16_lt _

theorem words (v : Nat) : Words v (wd v) := ⟨wd_lt v, fun j r hr => wd_row v j r hr⟩

theorem wordsA0 : Words A0 wdA0 := words A0
theorem wordsA1 : Words A1 wdA1 := words A1
theorem wordsB0 : Words B0 wdB0 := words B0
theorem wordsB1 : Words B1 wdB1 := words B1

/-! ### White wheels, black windows and the agreement below the forks -/

theorem wdA0_53207 : wdA0 53207 = 0 := word_zero_of_white wordsA0 white_53207
theorem wdA0_58286 : wdA0 58286 = 0 := word_zero_of_white wordsA0 white_58286
theorem wdB0_72575 : wdB0 72575 = 0 := word_zero_of_white wordsB0 white_72575

theorem hbwA0 : ∀ m, m < 53207 → wdA0 m ≠ 0 ∨ m = 2 ∨ m = 7 ∨ m = 28 ∨ m = 399 := fun m hm => by
  rcases black_or_white hm with ⟨r, hr, hb⟩ | h
  · exact Or.inl (word_ne_of_black wordsA0 hr hb)
  · exact Or.inr h

set_option exponentiation.threshold 90000 in
theorem bA0_low : ∀ m, 53208 ≤ m → m < 58286 → wdA0 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wA0_low h1 (by omega)
  exact word_ne_of_black wordsA0 hr hb
set_option exponentiation.threshold 90000 in
theorem bA0_high : ∀ m, 58287 ≤ m → m < 87866 → wdA0 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wA0_high h1 (by omega)
  exact word_ne_of_black wordsA0 hr hb
set_option exponentiation.threshold 90000 in
theorem bA1_high : ∀ m, 58287 ≤ m → m < 87866 → wdA1 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wA1_high h1 (by omega)
  exact word_ne_of_black wordsA1 hr hb
set_option exponentiation.threshold 90000 in
theorem bB0_low : ∀ m, 53208 ≤ m → m < 72575 → wdB0 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wB0_low h1 (by omega)
  exact word_ne_of_black wordsB0 hr hb
set_option exponentiation.threshold 90000 in
theorem bB0_high : ∀ m, 72576 ≤ m → m < 87866 → wdB0 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wB0_high h1 (by omega)
  exact word_ne_of_black wordsB0 hr hb
set_option exponentiation.threshold 90000 in
theorem bB1_high : ∀ m, 72576 ≤ m → m < 87866 → wdB1 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wB1_high h1 (by omega)
  exact word_ne_of_black wordsB1 hr hb

/-- Below a fork the two strips have the same words, so the same fronts. -/
theorem wB0_eq_A0 : ∀ i, i + 2 ≤ 53208 → wdA0 (i + 1) = wdB0 (i + 1) := fun i hi =>
  (word_eq_of_low wordsA0 wordsB0 (fun r _ => low_of_phase A0_return B0_return low_B0 (i + 1) r (by omega))).symm
theorem wA1_eq_A0 : ∀ i, i + 2 ≤ 58287 → wdA0 (i + 1) = wdA1 (i + 1) := fun i hi =>
  (word_eq_of_low wordsA0 wordsA1 (fun r _ => low_of_phase A0_return A1_return low_A1 (i + 1) r (by omega))).symm
theorem wB1_eq_B0 : ∀ i, i + 2 ≤ 72576 → wdB0 (i + 1) = wdB1 (i + 1) := fun i hi =>
  (word_eq_of_low wordsB0 wordsB1 (fun r _ => low_of_phase B0_return B1_return low_B1 (i + 1) r (by omega))).symm

/-! ### The tree, with the time carried -/

/-- **The forced front on the four strips.** Every array with the left-diagonal recurrence and a black wheel 0 carries one of
the four strips on every wheel `j ≤ 87,866` from strip tick `F j` on, at a shift of at most `15`. -/
theorem forced_front_four {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 15 ∧ (AlignedFrom a A0 s (F wdA0) 87866 ∨ AlignedFrom a A1 s (F wdA1) 87866 ∨
      AlignedFrom a B0 s (F wdB0) 87866 ∨ AlignedFrom a B1 s (F wdB1) 87866) := by
  obtain ⟨s, hs, h⟩ := low_from ha ha0 A0_return wordsA0 A0_zero A0_one hbwA0
    (strip_shift (m := 2) per2 anti2) (strip_shift (m := 7) per7 anti7) (strip_shift (m := 28) per28 anti28)
    (strip_shift (m := 399) per399 anti399) 53207 (Nat.le_refl _)
  refine ⟨s, by rw [lsum_53207] at hs; exact hs, ?_⟩
  rcases step_white ha A0_return wordsA0 (by omega) h wdA0_53207 with hA | hB
  · -- the A side: on A0 through the first fork
    have h2 : AlignedFrom a A0 s (F wdA0) 58286 :=
      extend_from ha A0_return wordsA0 (by omega) (by omega) (by omega) hA bA0_low
    rcases step_white ha A0_return wordsA0 (by omega) h2 wdA0_58286 with hA0 | hA1
    · exact Or.inl (extend_from ha A0_return wordsA0 (by omega) (by omega) (by omega) hA0 bA0_high)
    · have h3 : AlignedFrom a A1 s (F wdA0) 58287 := white_fork h2 hA1
        (fun j t hj => low_of_phase A0_return A1_return low_A1 j t (by omega))
        (comp_of_phase A0_return A1_return top_A1)
      have h4 : AlignedFrom a A1 s (F wdA1) 58287 :=
        alignedFrom_congr (fun j hj => F_congr j (fun i hi => wA1_eq_A0 i (by omega))) h3
      exact Or.inr (Or.inl (extend_from ha A1_return wordsA1 (by omega) (by omega) (by omega) h4 bA1_high))
  · -- the B side: the complement at 53,208 is B0's word
    have h3 : AlignedFrom a B0 s (F wdA0) 53208 := white_fork h hB
      (fun j t hj => low_of_phase A0_return B0_return low_B0 j t (by omega))
      (comp_of_phase A0_return B0_return top_B0)
    have h4 : AlignedFrom a B0 s (F wdB0) 53208 :=
      alignedFrom_congr (fun j hj => F_congr j (fun i hi => wB0_eq_A0 i (by omega))) h3
    have h5 : AlignedFrom a B0 s (F wdB0) 72575 :=
      extend_from ha B0_return wordsB0 (by omega) (by omega) (by omega) h4 bB0_low
    rcases step_white ha B0_return wordsB0 (by omega) h5 wdB0_72575 with hB0 | hB1
    · exact Or.inr (Or.inr (Or.inl (extend_from ha B0_return wordsB0 (by omega) (by omega) (by omega) hB0 bB0_high)))
    · have h6 : AlignedFrom a B1 s (F wdB0) 72576 := white_fork h5 hB1
        (fun j t hj => low_of_phase B0_return B1_return low_B1 j t (by omega))
        (comp_of_phase B0_return B1_return top_B1)
      have h7 : AlignedFrom a B1 s (F wdB1) 72576 :=
        alignedFrom_congr (fun j hj => F_congr j (fun i hi => wB1_eq_B0 i (by omega))) h6
      exact Or.inr (Or.inr (Or.inr (extend_from ha B1_return wordsB1 (by omega) (by omega) (by omega) h7 bB1_high)))

/-- The classification of `Rule30FourLeftSides`, recovered with its shift bounded by `15`. -/
theorem classification_bounded {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 15 ∧ (Aligned a A0 s 87866 ∨ Aligned a A1 s 87866 ∨ Aligned a B0 s 87866 ∨ Aligned a B1 s 87866) := by
  obtain ⟨s, hs, h⟩ := forced_front_four ha ha0
  refine ⟨s, hs, ?_⟩
  rcases h with h | h | h | h
  · exact Or.inl (aligned_of_alignedFrom h)
  · exact Or.inr (Or.inl (aligned_of_alignedFrom h))
  · exact Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h)))
  · exact Or.inr (Or.inr (Or.inr (aligned_of_alignedFrom h)))

/-! ### The numbers, by the walk -/

/-- A black run of a strip by the walk, with the long stretch sixteen ticks at a time. -/
theorem seg_black {v j0 n a b A B h g d : Nat} (hab : a ≤ b) (hn : 2 ≤ n) (hA : b < A) (hB : A < B)
    (e : A - 1 - b = h + (16 * g + d)) (ht : (b + h) % 16 = 0)
    (k1 : fastWalk (rowAt 87867 v) h g d b (j0 + 1) = j0 + n - 1)
    (f2 : tb (rowAt 87867 v) (A - 1) (j0 + n - 1) = 1)
    (f3 : walk (rowAt 87867 v) (B - 1 - A) A (j0 + n) = j0 + n)
    (f4 : tb (rowAt 87867 v) (B - 1) (j0 + n) = 1) : frun (wd v) j0 n (a, b) = (A, B) :=
  frun_of_walk (wd_row v) (wd_lt v) hab hn hA hB
    (by rw [e, ← fastWalk_eq _ ht (by omega)]; exact k1) f2 f3 f4

theorem low_congr {w w' : Nat → Nat} {n : Nat} {st : Nat × Nat} (h : ∀ i, i < n → w (i + 1) = w' (i + 1)) :
    frun w 0 n st = frun w' 0 n st :=
  frun_congr n 0 st (fun i hi => by rw [Nat.zero_add]; exact h i hi)

theorem a_low : frun wdA0 0 400 (0, 1) = (783, 784) := by decide +kernel

theorem a_1 : frun wdA0 400 52806 (783, 784) = (107308, 107310) :=
  seg_black (v := A0) (h := 0) (g := 6657) (d := 11) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)

theorem a_2 : frun wdA0 53206 1 (107308, 107310) = (107310, 107310) := frun_white (by decide) wdA0_53207

theorem a_53207 : frun wdA0 0 53207 (0, 1) = (107310, 107310) :=
  (frun_chain _ 0 400 52807 _ _ _ a_low
    (frun_chain _ 400 52806 1 _ _ _ a_1
    a_2))

theorem a_3 : frun wdA0 53207 5078 (107310, 107310) = (117438, 117439) :=
  seg_black (v := A0) (h := 2) (g := 632) (d := 13) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)

theorem a_4 : frun wdA0 58285 1 (117438, 117439) = (117439, 117439) := frun_white (by decide) wdA0_58286

theorem a_58286 : frun wdA0 0 58286 (0, 1) = (117439, 117439) :=
  (frun_chain _ 0 53207 5079 _ _ _ a_53207
    (frun_chain _ 53207 5078 1 _ _ _ a_3
    a_4))

theorem a_5 : frun wdA0 58286 29579 (117439, 117439) = (176966, 176968) :=
  seg_black (v := A0) (h := 1) (g := 3720) (d := 5) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)

theorem a_6 : frun wdA0 87865 1 (176966, 176968) = (176968, 176968) := frun_white (by decide) (by decide +kernel)

theorem SA0 : S wdA0 87866 = (176968, 176968) :=
  frun_chain _ 0 58286 29580 _ _ _ a_58286 (frun_chain _ 58286 29579 1 _ _ _ a_5 a_6)

theorem b_53207 : frun wdB0 0 53207 (0, 1) = (107310, 107310) :=
  (low_congr (fun i hi => (wB0_eq_A0 i (by omega)).symm)).trans a_53207

theorem b_1 : frun wdB0 53207 19367 (107310, 107310) = (146462, 146463) :=
  seg_black (v := B0) (h := 2) (g := 2446) (d := 13) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)

theorem b_2 : frun wdB0 72574 1 (146462, 146463) = (146463, 146463) := frun_white (by decide) wdB0_72575

theorem b_72575 : frun wdB0 0 72575 (0, 1) = (146463, 146463) :=
  (frun_chain _ 0 53207 19368 _ _ _ b_53207
    (frun_chain _ 53207 19367 1 _ _ _ b_1
    b_2))

theorem b_3 : frun wdB0 72575 15291 (146463, 146463) = (177170, 177173) :=
  seg_black (v := B0) (h := 1) (g := 1919) (d := 1) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)

theorem SB0 : S wdB0 87866 = (177170, 177173) := frun_chain _ 0 72575 15291 _ _ _ b_72575 b_3

theorem a1_58286 : frun wdA1 0 58286 (0, 1) = (117439, 117439) :=
  (low_congr (fun i hi => (wA1_eq_A0 i (by omega)).symm)).trans a_58286

theorem a1_1 : frun wdA1 58286 29580 (117439, 117439) = (177229, 177232) :=
  seg_black (v := A1) (h := 1) (g := 3736) (d := 12) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)

theorem SA1 : S wdA1 87866 = (177229, 177232) := frun_chain _ 0 58286 29580 _ _ _ a1_58286 a1_1

theorem b1_72575 : frun wdB1 0 72575 (0, 1) = (146463, 146463) :=
  (low_congr (fun i hi => (wB1_eq_B0 i (by omega)).symm)).trans b_72575

theorem b1_1 : frun wdB1 72575 15291 (146463, 146463) = (177560, 177563) :=
  seg_black (v := B1) (h := 1) (g := 1943) (d := 7) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)

theorem SB1 : S wdB1 87866 = (177560, 177563) := frun_chain _ 0 72575 15291 _ _ _ b1_72575 b1_1

theorem FA0_87866 : F wdA0 87866 = 176968 := F_of_S SA0

theorem FA1_87866 : F wdA1 87866 = 177229 := F_of_S SA1

theorem FB0_87866 : F wdB0 87866 = 177170 := F_of_S SB0

theorem FB1_87866 : F wdB1 87866 = 177560 := F_of_S SB1

/-- Every front through wheel 87,866 is at most 177,560, the B1 front there. -/
theorem fronts_le : (∀ j, j ≤ 87866 → F wdA0 j ≤ 177560) ∧ (∀ j, j ≤ 87866 → F wdA1 j ≤ 177560) ∧
    (∀ j, j ≤ 87866 → F wdB0 j ≤ 177560) ∧ ∀ j, j ≤ 87866 → F wdB1 j ≤ 177560 :=
  ⟨fun j hj => Nat.le_trans (F_mono wdA0 hj) (by rw [FA0_87866]; omega),
   fun j hj => Nat.le_trans (F_mono wdA1 hj) (by rw [FA1_87866]; omega),
   fun j hj => Nat.le_trans (F_mono wdB0 hj) (by rw [FB0_87866]; omega),
   fun j hj => Nat.le_trans (F_mono wdB1 hj) (by rw [FB1_87866]; omega)⟩

/-! ### The headlines -/

/-- **From strip tick 177,560**, that is from tick at most 177,575 of its own clock, every array with the recurrence and a
black start carries the whole of one of the four strips through wheel 87,866. -/
theorem forced_front_four_uniform {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 15 ∧ (OnStrip a A0 s 177560 87866 ∨ OnStrip a A1 s 177560 87866 ∨
      OnStrip a B0 s 177560 87866 ∨ OnStrip a B1 s 177560 87866) := by
  obtain ⟨s, hs, h⟩ := forced_front_four ha ha0
  refine ⟨s, hs, ?_⟩
  rcases h with h | h | h | h
  · exact Or.inl (onStrip_of_alignedFrom fronts_le.1 h)
  · exact Or.inr (Or.inl (onStrip_of_alignedFrom fronts_le.2.1 h))
  · exact Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom fronts_le.2.2.1 h)))
  · exact Or.inr (Or.inr (Or.inr (onStrip_of_alignedFrom fronts_le.2.2.2 h)))

/-- **Every configuration with a leftmost black cell**, whatever lies to its right: on one of the four strips through wheel
87,866 from tick 177,560 + s of its own clock, s ≤ 15. -/
theorem forced_front_four_left_side {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false)
    (hlo : x lo = true) :
    ∃ s, s ≤ 15 ∧ (OnStrip (Ld x lo) A0 s 177560 87866 ∨ OnStrip (Ld x lo) A1 s 177560 87866 ∨
      OnStrip (Ld x lo) B0 s 177560 87866 ∨ OnStrip (Ld x lo) B1 s 177560 87866) :=
  forced_front_four_uniform (Ld_recurrence hleft) (by simpa [Ld, evol] using hlo)

/-- The single black cell. The proof does not say which strip. -/
theorem forced_front_four_seed :
    ∃ s, s ≤ 15 ∧ (OnStrip D A0 s 177560 87866 ∨ OnStrip D A1 s 177560 87866 ∨
      OnStrip D B0 s 177560 87866 ∨ OnStrip D B1 s 177560 87866) :=
  forced_front_four_uniform Rule30FourLeftSides.D_recurrence (D_zero 0)

/-- Below the first fork the four strips are one, so the front there comes sooner: `107,310`, the value `F 53207` of `Rule30ForcedFront`. -/
theorem F_low : F wdA0 53207 = 107310 ∧ F wdA1 53207 = 107310 ∧ F wdB0 53207 = 107310 ∧ F wdB1 53207 = 107310 := by
  have h0 : F wdA0 53207 = 107310 := F_of_S a_53207
  have h2 : F wdB0 53207 = 107310 := F_of_S b_53207
  exact ⟨h0, by rw [← h0]; exact (F_congr 53207 (fun i hi => wA1_eq_A0 i (by omega))).symm, h2,
    by rw [← h2]; exact (F_congr 53207 (fun i hi => wB1_eq_B0 i (by omega))).symm⟩

theorem low_front {a : Nat → Nat → Bool} {v s : Nat} {w : Nat → Nat} (hF : F w 53207 = 107310)
    (hs : ∀ j t, j ≤ 53207 → Sp v j t = Sp A0 j t) (h : AlignedFrom a v s (F w) 87866) : OnStrip a A0 s 107310 53207 :=
  fun j hj t ht => by
    rw [h j (by omega) t (Nat.le_trans (by rw [← hF]; exact F_mono w hj) ht)]
    exact hs j t hj

/-- **Through the first fork's wheel**: every array with the recurrence and a black start carries the strip of `A0` through wheel 53,207
from strip tick 107,310, that is from tick at most 107,325 of its own clock. -/
theorem forced_front_low {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 15 ∧ OnStrip a A0 s 107310 53207 := by
  obtain ⟨s, hs, h⟩ := forced_front_four ha ha0
  obtain ⟨f0, f1, f2, f3⟩ := F_low
  have eB0 : ∀ j t, j ≤ 53207 → Sp B0 j t = Sp A0 j t := fun j t hj =>
    low_of_phase A0_return B0_return low_B0 j t (by omega)
  refine ⟨s, hs, ?_⟩
  rcases h with h | h | h | h
  · exact low_front f0 (fun _ _ _ => rfl) h
  · exact low_front f1 (fun j t hj => low_of_phase A0_return A1_return low_A1 j t (by omega)) h
  · exact low_front f2 eB0 h
  · exact low_front f3 (fun j t hj => by
      rw [low_of_phase B0_return B1_return low_B1 j t (by omega)]; exact eB0 j t hj) h

/-- Every configuration with a leftmost black cell, through wheel 53,207 from tick 107,310 + s of its own clock, s ≤ 15. -/
theorem forced_front_low_left_side {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false)
    (hlo : x lo = true) : ∃ s, s ≤ 15 ∧ OnStrip (Ld x lo) A0 s 107310 53207 :=
  forced_front_low (Ld_recurrence hleft) (by simpa [Ld, evol] using hlo)

end Ruliology.CellularAutomata.Rule30FourFronts
