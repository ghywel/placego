import Ruliology.CellularAutomata.Rule30FourFrontsBase

namespace WalkTest
open Ruliology.CellularAutomata.Rule30FourFrontsBase

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
def fast (R : Nat → Nat) (h g d t j : Nat) : Nat :=
  walk R d (t + h + 16 * g) (w16 R g (walk R h t j))

theorem fast_eq (R : Nat → Nat) {h g d t j : Nat} (ht : (t + h) % 16 = 0) (hj : 1 ≤ j) :
    fast R h g d t j = walk R (h + (16 * g + d)) t j := by
  show walk R d (t + h + 16 * g) (w16 R g (walk R h t j)) = _
  rw [w16_walk R g (t + h) _ ht (Nat.le_trans hj (le_walk R h t j)), ← walk_add, ← walk_add]

end WalkTest
