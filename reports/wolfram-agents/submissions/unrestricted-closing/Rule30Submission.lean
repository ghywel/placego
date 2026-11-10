import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30ZeroBoundary
/-!
# Rule 30, zero-boundary left half: unrestricted tail closing fails on the constrained class

Three starts of the zero-boundary left half (`Rule30ZeroBoundary.zrow`), read from depth `1`
(depth `0` is the white wall):

* `rowA`: the period-`7` word `1011111`;
* `rowB`: black at depths `1, 2`, then the period-`14` word `01001011001000` from depth `3`;
* `rowC`: the period-`7` word `1100001`.

**The cycle.** Write `G` for two ticks. Then `G A = C`, `G B = C` and `G C = A` at every depth
(`two_A`, `two_B`, `two_C`, `two_cycle`). Two ticks at depth `k ≥ 3` read the start at depths
`k - 2, …, k + 2` only (`zrow_two`), so each identity passes from `k` to `k + 7` (or `k + 14`)
(`two_shift`, `periodic_ind`), and one period of depths is checked by `decide`.

**Membership of the constrained class `K = InX`.** The even-tick rows cycle `A, C, A, C, …` and
`B, C, A, C, …`, and each of these rows is black at depth `1`, so all three starts are in `InX`
(`inX_A`, `inX_B`, `inX_C`). Their free words (depth `1` at the odd ticks) are `fA = 1010…`,
`fB = 001010…` and `fC = 0101…` (`free_A`, `free_B`, `free_C`), so `zrow rowA 0 = Theta fA`, and
likewise for `B` and `C` (`theta_A`, `theta_B`, `theta_C`, by `Theta_unique`).

**Infinite mismatch.** `A` and `B` differ at every depth `14 q + 3` (`differ_AB`), so they agree on
no tail of depths. One tick already separates them at every depth `14 q + 4`, where the
neighbourhoods read `111` in `A` and `010` in `B` (`differ_one_tick`).

**Unrestricted closing fails on `K`.** `not_unrestricted_closing`: two starts in `K` with the same
row after one double step need not agree on any tail. So the unrestricted eventual-tail closing
property, with no hypothesis on the gate streams, fails on `K`.

Context, not a theorem of this module: this does not contradict the guarded `HomoclinicClosing`
and `AllPastClosing` of open kit pull request 52, which assume `GateLegal` gate streams. In the
convention of that pull request the gate words are the complemented even heads one tick later, and
the common future here starts with the window value `85`, outside its ten legal windows.

Nothing here decides `Q01` or period 2.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

open Rule30ZeroBoundary

/-! ### Locality of one and two ticks -/

/-- One tick at depth `j + 2` reads the start at depths `j + 1, j + 2, j + 3`. -/
theorem zrow_one (L : Nat → Bool) (j : Nat) :
    zrow L 1 (j + 2) = xor (L (j + 3)) (L (j + 2) || L (j + 1)) :=
  rfl

/-- Two ticks at depth `j + 3` read the start at depths `j + 1, …, j + 5` only. -/
theorem zrow_two (L : Nat → Bool) (j : Nat) :
    zrow L 2 (j + 3) =
      xor (xor (L (j + 5)) (L (j + 4) || L (j + 3)))
        (xor (L (j + 4)) (L (j + 3) || L (j + 2)) || xor (L (j + 3)) (L (j + 2) || L (j + 1))) :=
  rfl

/-- Two ticks commute with a shift by `p` of a start that is `p`-periodic from depth `a ≥ 1` on,
at the depths `k ≥ a + 2`. -/
theorem two_shift {L : Nat → Bool} {a p : Nat} (ha : 1 ≤ a) (hL : ∀ d, a ≤ d → L (d + p) = L d)
    {k : Nat} (hk : a + 2 ≤ k) : zrow L 2 (k + p) = zrow L 2 k := by
  obtain ⟨j, rfl⟩ : ∃ j, k = j + 3 := ⟨k - 3, by omega⟩
  have h : ∀ i, 1 ≤ i → L (j + p + i) = L (j + i) := fun i hi => by
    rw [show j + p + i = (j + i) + p by omega]
    exact hL _ (by omega)
  rw [show j + 3 + p = (j + p) + 3 by omega, zrow_two, zrow_two, h 1 (by omega), h 2 (by omega),
    h 3 (by omega), h 4 (by omega), h 5 (by omega)]

/-- **Periodic induction.** A property that holds below `m + p` and passes from `k` to `k + p` for
every `k ≥ m` holds everywhere. -/
theorem periodic_ind {P : Nat → Prop} {m p : Nat} (hp : 0 < p) (base : ∀ k, k < m + p → P k)
    (step : ∀ k, m ≤ k → P k → P (k + p)) : ∀ k, P k := by
  have h : ∀ n k, k < n → P k := by
    intro n
    induction n with
    | zero => intro k hk; exact absurd hk (Nat.not_lt_zero k)
    | succ n ih =>
      intro k hk
      by_cases hb : k < m + p
      · exact base k hb
      · obtain ⟨j, rfl⟩ : ∃ j, k = j + p := ⟨k - p, by omega⟩
        exact step j (by omega) (ih j (by omega))
  exact fun k => h (k + 1) k (by omega)

/-! ### The three rows -/

/-- Row `A`: the period-`7` word `1011111`, read from depth `1`. Depth `0` is the white wall. -/
def rowA (d : Nat) : Bool :=
  if d = 0 then false else [1, 0, 1, 1, 1, 1, 1].getD ((d - 1) % 7) 0 == 1

/-- Row `B`: black at depths `1, 2`, then the period-`14` word `01001011001000` from depth `3`. -/
def rowB (d : Nat) : Bool :=
  if d = 0 then false else if d ≤ 2 then true else
    [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0].getD ((d - 3) % 14) 0 == 1

/-- Row `C`: the period-`7` word `1100001`, read from depth `1`. -/
def rowC (d : Nat) : Bool :=
  if d = 0 then false else [1, 1, 0, 0, 0, 0, 1].getD ((d - 1) % 7) 0 == 1

theorem rowA_add (d q : Nat) (hd : 1 ≤ d) : rowA (d + 7 * q) = rowA d := by
  unfold rowA
  rw [ite_eq_right (show ¬ d + 7 * q = 0 by omega), ite_eq_right (show ¬ d = 0 by omega),
    show (d + 7 * q - 1) % 7 = (d - 1) % 7 by omega]

theorem rowB_add (d q : Nat) (hd : 3 ≤ d) : rowB (d + 14 * q) = rowB d := by
  unfold rowB
  rw [ite_eq_right (show ¬ d + 14 * q = 0 by omega), ite_eq_right (show ¬ d + 14 * q ≤ 2 by omega),
    ite_eq_right (show ¬ d = 0 by omega), ite_eq_right (show ¬ d ≤ 2 by omega),
    show (d + 14 * q - 3) % 14 = (d - 3) % 14 by omega]

theorem rowC_add (d q : Nat) (hd : 1 ≤ d) : rowC (d + 7 * q) = rowC d := by
  unfold rowC
  rw [ite_eq_right (show ¬ d + 7 * q = 0 by omega), ite_eq_right (show ¬ d = 0 by omega),
    show (d + 7 * q - 1) % 7 = (d - 1) % 7 by omega]

theorem rowA_period (d : Nat) (hd : 1 ≤ d) : rowA (d + 7) = rowA d := rowA_add d 1 hd

theorem rowB_period (d : Nat) (hd : 3 ≤ d) : rowB (d + 14) = rowB d := rowB_add d 1 hd

theorem rowC_period (d : Nat) (hd : 1 ≤ d) : rowC (d + 7) = rowC d := rowC_add d 1 hd

/-! ### The two-tick cycle -/

/-- `G A = C`: two ticks take row `A` to row `C`, at every depth. -/
theorem two_A : ∀ k, zrow rowA 2 k = rowC k := by
  refine periodic_ind (m := 3) (p := 7) (by decide) (by decide) fun k hk ih => ?_
  rw [two_shift (Nat.le_refl 1) rowA_period (by omega), ih, rowC_period k (by omega)]

/-- `G B = C`: two ticks take row `B` to row `C`, at every depth. -/
theorem two_B : ∀ k, zrow rowB 2 k = rowC k := by
  refine periodic_ind (m := 5) (p := 14) (by decide) (by decide) fun k hk ih => ?_
  have hC : rowC (k + 14) = rowC k := rowC_add k 2 (by omega)
  rw [two_shift (a := 3) (by decide) rowB_period (by omega), ih, hC]

/-- `G C = A`: two ticks take row `C` to row `A`, at every depth. -/
theorem two_C : ∀ k, zrow rowC 2 k = rowA k := by
  refine periodic_ind (m := 3) (p := 7) (by decide) (by decide) fun k hk ih => ?_
  rw [two_shift (Nat.le_refl 1) rowC_period (by omega), ih, rowA_period k (by omega)]

/-- The cycle as equalities of rows: `G A = G B = C` and `G C = A`. -/
theorem two_cycle : zrow rowA 2 = rowC ∧ zrow rowB 2 = rowC ∧ zrow rowC 2 = rowA :=
  ⟨funext two_A, funext two_B, funext two_C⟩

/-! ### Membership of the constrained class -/

theorem inX_AC (s : Nat) : zrow rowA (2 * s) 1 = true ∧ zrow rowC (2 * s) 1 = true := by
  induction s with
  | zero => exact ⟨rfl, rfl⟩
  | succ s ih =>
    rw [show 2 * (s + 1) = 2 + 2 * s by omega, zrow_shift rowA 2, zrow_shift rowC 2,
      two_cycle.1, two_cycle.2.2]
    exact ⟨ih.2, ih.1⟩

theorem inX_A : InX rowA := fun s => (inX_AC s).1

theorem inX_C : InX rowC := fun s => (inX_AC s).2

theorem inX_B : InX rowB := by
  intro s
  cases s with
  | zero => rfl
  | succ s =>
    rw [show 2 * (s + 1) = 2 + 2 * s by omega, zrow_shift rowB 2, two_cycle.2.1]
    exact inX_C s

/-! ### The free words -/

/-- The free word `1010…` of row `A`. -/
def fA (s : Nat) : Bool := decide (s % 2 = 0)

/-- The free word `001010…` of row `B`. -/
def fB (s : Nat) : Bool := decide (2 ≤ s ∧ s % 2 = 0)

/-- The free word `0101…` of row `C`. -/
def fC (s : Nat) : Bool := decide (s % 2 = 1)

theorem fA_succ (s : Nat) : fA (s + 1) = fC s := by
  unfold fA fC; exact decide_eq_decide.mpr (by omega)

theorem fB_succ (s : Nat) : fB (s + 1) = fC s := by
  unfold fB fC; exact decide_eq_decide.mpr (by omega)

theorem fC_succ (s : Nat) : fC (s + 1) = fA s := by
  unfold fC fA; exact decide_eq_decide.mpr (by omega)

theorem free_AC (s : Nat) : zrow rowA (2 * s + 1) 1 = fA s ∧ zrow rowC (2 * s + 1) 1 = fC s := by
  induction s with
  | zero => exact ⟨rfl, rfl⟩
  | succ s ih =>
    rw [show 2 * (s + 1) + 1 = 2 + (2 * s + 1) by omega, zrow_shift rowA 2, zrow_shift rowC 2,
      two_cycle.1, two_cycle.2.2, fA_succ, fC_succ]
    exact ⟨ih.2, ih.1⟩

theorem free_A : ∀ s, zrow rowA (2 * s + 1) 1 = fA s := fun s => (free_AC s).1

theorem free_C : ∀ s, zrow rowC (2 * s + 1) 1 = fC s := fun s => (free_AC s).2

theorem free_B : ∀ s, zrow rowB (2 * s + 1) 1 = fB s := by
  intro s
  cases s with
  | zero => rfl
  | succ s =>
    rw [show 2 * (s + 1) + 1 = 2 + (2 * s + 1) by omega, zrow_shift rowB 2, two_cycle.2.1,
      fB_succ]
    exact free_C s

theorem theta_A : zrow rowA 0 = Theta fA := Theta_unique inX_A free_A

theorem theta_B : zrow rowB 0 = Theta fB := Theta_unique inX_B free_B

theorem theta_C : zrow rowC 0 = Theta fC := Theta_unique inX_C free_C

/-! ### The mismatch -/

/-- Rows `A` and `B` differ at every depth `14 q + 3`: `A` is black there and `B` is white. -/
theorem differ_AB : ∀ q, rowA (14 * q + 3) ≠ rowB (14 * q + 3) := by
  intro q
  rw [show 14 * q + 3 = 3 + 7 * (2 * q) by omega, rowA_add 3 (2 * q) (by decide),
    show 3 + 7 * (2 * q) = 3 + 14 * q by omega, rowB_add 3 q (Nat.le_refl 3)]
  decide

/-- One tick separates `A` and `B` at every depth `14 q + 4`: the neighbourhoods read `111` in `A`
and `010` in `B`. -/
theorem differ_one_tick : ∀ q, zrow rowA 1 (14 * q + 4) = false ∧ zrow rowB 1 (14 * q + 4) = true := by
  intro q
  have hA : ∀ i, 1 ≤ i → rowA (14 * q + 2 + i) = rowA (2 + i) := fun i hi => by
    rw [show 14 * q + 2 + i = (2 + i) + 7 * (2 * q) by omega, rowA_add _ _ (by omega)]
  have hB : ∀ i, 1 ≤ i → rowB (14 * q + 2 + i) = rowB (2 + i) := fun i hi => by
    rw [show 14 * q + 2 + i = (2 + i) + 14 * q by omega, rowB_add _ _ (by omega)]
  rw [show 14 * q + 4 = (14 * q + 2) + 2 by omega, zrow_one, zrow_one, hA 1 (by omega),
    hA 2 (by omega), hA 3 (by omega), hB 1 (by omega), hB 2 (by omega), hB 3 (by omega)]
  decide

/-! ### Closing -/

/-- **Unrestricted tail closing fails on the constrained class.** It is not true that any two
constrained starts (`InX`) with the same row after one double step (two ticks) agree on a tail of
depths: `rowA` and `rowB` are constrained, have the common image `rowC`, and differ at every depth
`14 q + 3`.

This negates the unrestricted eventual-tail closing property on `K`, after one double step, with no
hypothesis on the gate streams. The legal-gate formulations, which assume legality of the gate
streams, are not contradicted. -/
theorem not_unrestricted_closing :
    ¬ ∀ L L' : Nat → Bool, InX L → InX L' → (∀ k, zrow L 2 k = zrow L' 2 k) →
      ∃ N, ∀ k, N ≤ k → L k = L' k := by
  intro h
  obtain ⟨N, hN⟩ := h rowA rowB inX_A inX_B fun k => by rw [two_A, two_B]
  exact differ_AB N (hN (14 * N + 3) (by omega))

end Rule30Submission
