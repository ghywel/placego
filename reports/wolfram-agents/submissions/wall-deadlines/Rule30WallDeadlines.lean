module

public import Ruliology.CellularAutomata.Rule30ZeroBoundary

/-!
# Wall deadlines of rules 90 and 150

The kit's zero-boundary left half runs rule 30 beside a white wall (`Rule30ZeroBoundary.zrow`).
Every rule of the form `left xor h (centre, right)` has the same frame, `zr h`, and `zr_or_eq_zrow`
shows that `h = or` is rule 30's. `Q01` asks, for rule 30, whether every finite start turns
depth `1` white at some even tick. For rules 90 (`h b c = c`) and 150 (`h b c = b xor c`) this
module gives the exact answer: the last tick at which a start of width at most `W` can still be
black at depth `1` at every even tick.

* `odd90`: for rule 90, if depth `1` is black at every even tick up to `T`, then every cell with
  depth plus tick odd and at most `T + 1` is `fib2` of its depth, Fibonacci modulo `2` (white
  exactly at the multiples of `3`, `fib2_mod`). The parity class is closed under the rule and its
  boundary is the white wall and the black column.
* `deadline90`, `sharp90`: so a start of width at most `W` turns depth `1` white at some even tick
  at most `kstar W - 1`, where `kstar W` is the least odd number above `W` not divisible by `3`;
  and every start of width at most `W` whose odd depths follow `fib2` keeps depth `1` black at
  every even tick `2 s` with `2 s + 2 ≤ kstar W`.
* `two_step150`, `odd150`: for rule 150, two steps act on the odd depths at even ticks by their own
  rule, `x (k, t + 2) = x (k + 2, t) + x (k, t) + x (k - 2, t)`, with `x (1, t + 2) = x (3, t)` at
  the wall. If depth `1` is black at every even tick up to `T`, every odd depth is black at every
  even tick within that triangle.
* `deadline150`, `sharp150`: so a start of width at most `W` turns depth `1` white at some even
  tick at most `2 ⌈W / 2⌉`, and every start of width at most `W` with all odd depths black keeps
  depth `1` black at every even tick below `2 ⌈W / 2⌉`.

These rules are linear and are not rule 30; nothing here decides `Q01`.
-/

@[expose] public section

namespace Ruliology.CellularAutomata
namespace Rule30WallDeadlines

open Rule30ZeroBoundary

/-- The zero-boundary frame for the rule `new = left xor h (centre, right)`: depth `0` is a white
wall and depth `k + 1` lies to the left of depth `k`. -/
def zr (h : Bool → Bool → Bool) (L : Nat → Bool) : Nat → Nat → Bool
  | 0, k => if k = 0 then false else L k
  | t + 1, k => if k = 0 then false else xor (zr h L t (k + 1)) (h (zr h L t k) (zr h L t (k - 1)))

theorem zr_wall (h : Bool → Bool → Bool) (L : Nat → Bool) : ∀ t, zr h L t 0 = false
  | 0 => rfl
  | _ + 1 => rfl

theorem zr_zero (h : Bool → Bool → Bool) (L : Nat → Bool) (k : Nat) : zr h L 0 (k + 1) = L (k + 1) := rfl

theorem zr_succ (h : Bool → Bool → Bool) (L : Nat → Bool) (t k : Nat) :
    zr h L (t + 1) (k + 1) = xor (zr h L t (k + 2)) (h (zr h L t (k + 1)) (zr h L t k)) := rfl

/-- `h = or` is rule 30's frame, the kit's `zrow`. -/
theorem zr_or_eq_zrow (L : Nat → Bool) : ∀ t k, zr (fun b c => b || c) L t k = zrow L t k := by
  intro t
  induction t with
  | zero => intro k; cases k <;> rfl
  | succ t ih =>
    intro k
    cases k with
    | zero => rfl
    | succ k => rw [zr_succ, zrow_succ, ih, ih, ih]

/-- The light cone: the cell at depth `k` and tick `t` reads the start only at depths up to
`k + t`. -/
theorem zr_cone (h : Bool → Bool → Bool) {L L' : Nat → Bool} :
    ∀ t k, (∀ i, 1 ≤ i → i ≤ k + t → L i = L' i) → zr h L t k = zr h L' t k := by
  intro t
  induction t with
  | zero =>
    intro k hL
    cases k with
    | zero => rfl
    | succ k => rw [zr_zero, zr_zero, hL (k + 1) (by omega) (by omega)]
  | succ t ih =>
    intro k hL
    cases k with
    | zero => rfl
    | succ k =>
      rw [zr_succ, zr_succ, ih (k + 2) (fun i h1 h2 => hL i h1 (by omega)),
        ih (k + 1) (fun i h1 h2 => hL i h1 (by omega)), ih k (fun i h1 h2 => hL i h1 (by omega))]

/-! ### Rule 90 -/

/-- Rule 90: `left xor right`. -/
def h90 (_b c : Bool) : Bool := c

/-- Fibonacci modulo `2`. -/
def fib2 : Nat → Bool
  | 0 => false
  | 1 => true
  | k + 2 => xor (fib2 (k + 1)) (fib2 k)

theorem fib2_three (k : Nat) : fib2 (k + 3) = fib2 k := by
  show xor (xor (fib2 (k + 1)) (fib2 k)) (fib2 (k + 1)) = fib2 k
  generalize fib2 (k + 1) = a
  generalize fib2 k = b
  cases a <;> cases b <;> rfl

/-- Fibonacci modulo `2` is white exactly at the multiples of `3`. -/
theorem fib2_mod (k : Nat) : fib2 k = decide (k % 3 ≠ 0) := by
  have key : ∀ n, fib2 (3 * n) = false ∧ fib2 (3 * n + 1) = true ∧ fib2 (3 * n + 2) = true := by
    intro n
    induction n with
    | zero => exact ⟨rfl, rfl, rfl⟩
    | succ n ih =>
      refine ⟨?_, ?_, ?_⟩
      · rw [show 3 * (n + 1) = 3 * n + 3 by omega, fib2_three]; exact ih.1
      · rw [show 3 * (n + 1) + 1 = 3 * n + 1 + 3 by omega, fib2_three]; exact ih.2.1
      · rw [show 3 * (n + 1) + 2 = 3 * n + 2 + 3 by omega, fib2_three]; exact ih.2.2
  obtain ⟨h0, h1, h2⟩ := key (k / 3)
  rcases (show k % 3 = 0 ∨ k % 3 = 1 ∨ k % 3 = 2 by omega) with hr | hr | hr
  · rw [show k = 3 * (k / 3) by omega, h0, decide_eq_false (by omega)]
  · rw [show k = 3 * (k / 3) + 1 by omega, h1, decide_eq_true (by omega)]
  · rw [show k = 3 * (k / 3) + 2 by omega, h2, decide_eq_true (by omega)]

theorem zr90_succ (L : Nat → Bool) (t k : Nat) :
    zr h90 L (t + 1) (k + 1) = xor (zr h90 L t (k + 2)) (zr h90 L t k) := rfl

/-- **The odd parity class of rule 90 is Fibonacci.** If depth `1` is black at every even tick up
to `T`, every cell with depth plus tick odd and at most `T + 1` is `fib2` of its depth. -/
theorem odd90 {L : Nat → Bool} {T : Nat} (hblack : ∀ s, 2 * s ≤ T → zr h90 L (2 * s) 1 = true) :
    ∀ k t, (k + t) % 2 = 1 → k + t ≤ T + 1 → zr h90 L t k = fib2 k := by
  have key : ∀ k, (∀ t, (k + t) % 2 = 1 → k + t ≤ T + 1 → zr h90 L t k = fib2 k) ∧
      (∀ t, (k + 1 + t) % 2 = 1 → k + 1 + t ≤ T + 1 → zr h90 L t (k + 1) = fib2 (k + 1)) := by
    intro k
    induction k with
    | zero =>
      refine ⟨fun t _ _ => zr_wall h90 L t, fun t ht hT => ?_⟩
      obtain ⟨s, rfl⟩ : ∃ s, t = 2 * s := ⟨t / 2, by omega⟩
      exact hblack s (by omega)
    | succ k ih =>
      refine ⟨ih.2, fun t ht hT => ?_⟩
      have e : zr h90 L t (k + 2) = xor (zr h90 L (t + 1) (k + 1)) (zr h90 L t k) := by
        rw [zr90_succ]
        generalize zr h90 L t (k + 2) = a
        generalize zr h90 L t k = b
        cases a <;> cases b <;> rfl
      rw [e, ih.2 (t + 1) (by omega) (by omega), ih.1 t (by omega) (by omega)]
      rfl
  exact fun k => (key k).1

/-- The least odd number above `W` that is not a multiple of `3`. -/
def kstar (W : Nat) : Nat :=
  if (W + 1 + W % 2) % 3 = 0 then W + 3 + W % 2 else W + 1 + W % 2

theorem kstar_spec (W : Nat) :
    kstar W % 2 = 1 ∧ W < kstar W ∧ kstar W % 3 ≠ 0 ∧
      ∀ k, k % 2 = 1 → W < k → k < kstar W → k % 3 = 0 := by
  unfold kstar
  by_cases h : (W + 1 + W % 2) % 3 = 0
  · rw [ite_eq_left h]
    refine ⟨by omega, by omega, by omega, fun k hk1 hk2 hk3 => ?_⟩
    have : k = W + 1 + W % 2 := by omega
    rw [this]; exact h
  · rw [ite_eq_right h]
    exact ⟨by omega, by omega, h, fun k hk1 hk2 hk3 => by omega⟩

/-- **Rule 90's wall deadline.** A start of width at most `W` turns depth `1` white at some even
tick at most `kstar W - 1`. -/
theorem deadline90 {L : Nat → Bool} {W : Nat} (hW : ∀ k, W < k → L k = false) :
    ∃ s, 2 * s ≤ kstar W - 1 ∧ zr h90 L (2 * s) 1 = false := by
  obtain ⟨hodd, hgt, hmod, -⟩ := kstar_spec W
  apply Classical.byContradiction
  intro hno
  have hblack : ∀ s, 2 * s ≤ kstar W - 1 → zr h90 L (2 * s) 1 = true := by
    intro s hs
    cases hc : zr h90 L (2 * s) 1 with
    | true => rfl
    | false => exact absurd ⟨s, hs, hc⟩ hno
  have e := odd90 hblack (kstar W) 0 (by omega) (by omega)
  obtain ⟨k, hk⟩ : ∃ k, kstar W = k + 1 := ⟨kstar W - 1, by omega⟩
  rw [hk, zr_zero, ← hk, hW (kstar W) hgt, fib2_mod, decide_eq_true hmod] at e
  exact Bool.noConfusion e

/-- Every row whose odd depths follow `fib2` keeps the odd class of rule 90 equal to `fib2`. -/
theorem fwd90 {M : Nat → Bool} (hM : ∀ k, k % 2 = 1 → M k = fib2 k) :
    ∀ t k, (k + t) % 2 = 1 → zr h90 M t k = fib2 k := by
  intro t
  induction t with
  | zero =>
    intro k hk
    obtain ⟨k', rfl⟩ : ∃ k', k = k' + 1 := ⟨k - 1, by omega⟩
    rw [zr_zero]
    exact hM (k' + 1) (by omega)
  | succ t ih =>
    intro k hk
    cases k with
    | zero => rw [zr_wall]; rfl
    | succ k =>
      rw [zr90_succ, ih (k + 2) (by omega), ih k (by omega)]
      show xor (xor (fib2 (k + 1)) (fib2 k)) (fib2 k) = fib2 (k + 1)
      generalize fib2 (k + 1) = a
      generalize fib2 k = b
      cases a <;> cases b <;> rfl

/-- **Rule 90's deadline is sharp.** Every start of width at most `W` whose odd depths follow
`fib2` keeps depth `1` black at every even tick `2 s` with `2 s + 2 ≤ kstar W`. -/
theorem sharp90 {L : Nat → Bool} {W : Nat} (hodd : ∀ k, k % 2 = 1 → k ≤ W → L k = fib2 k)
    (hW : ∀ k, W < k → L k = false) :
    ∀ s, 2 * s + 2 ≤ kstar W → zr h90 L (2 * s) 1 = true := by
  obtain ⟨hko, hgt, -, hgap⟩ := kstar_spec W
  intro s hs
  let M : Nat → Bool := fun k => if k % 2 = 1 then fib2 k else L k
  have hM : ∀ k, k % 2 = 1 → M k = fib2 k := fun k hk => by
    show (if k % 2 = 1 then fib2 k else L k) = fib2 k
    rw [ite_eq_left hk]
  have agree : ∀ i, 1 ≤ i → i ≤ 1 + 2 * s → L i = M i := by
    intro i hi1 hi2
    show L i = if i % 2 = 1 then fib2 i else L i
    by_cases hi : i % 2 = 1
    · rw [ite_eq_left hi]
      by_cases hiW : i ≤ W
      · exact hodd i hi hiW
      · rw [hW i (by omega), fib2_mod, decide_eq_false (by
          have := hgap i hi (by omega) (by omega); omega)]
    · rw [ite_eq_right hi]
  rw [zr_cone h90 (2 * s) 1 agree, fwd90 hM (2 * s) 1 (by omega)]
  rfl

/-! ### Rule 150 -/

/-- Rule 150: `left xor centre xor right`. -/
def h150 (b c : Bool) : Bool := xor b c

theorem zr150_succ (L : Nat → Bool) (t k : Nat) :
    zr h150 L (t + 1) (k + 1) =
      xor (zr h150 L t (k + 2)) (xor (zr h150 L t (k + 1)) (zr h150 L t k)) := rfl

/-- **Two steps of rule 150 on the odd depths.** At the wall the cell at depth `1` two ticks later is
the cell at depth `3`; away from it, two ticks act by `x (k + 2) + x k + x (k - 2)`. -/
theorem two_step150 (L : Nat → Bool) (t : Nat) :
    zr h150 L (t + 2) 1 = zr h150 L t 3 ∧
      ∀ k, zr h150 L (t + 2) (k + 2) =
        xor (xor (zr h150 L t (k + 4)) (zr h150 L t (k + 2))) (zr h150 L t k) := by
  refine ⟨?_, fun k => ?_⟩
  · rw [zr150_succ, zr150_succ, zr150_succ, zr_wall, zr_wall]
    generalize zr h150 L t 3 = a
    generalize zr h150 L t 2 = b
    generalize zr h150 L t 1 = c
    cases a <;> cases b <;> cases c <;> rfl
  · rw [zr150_succ, zr150_succ, zr150_succ, zr150_succ]
    show xor (xor (zr h150 L t (k + 4)) (xor (zr h150 L t (k + 3)) (zr h150 L t (k + 2))))
      (xor (xor (zr h150 L t (k + 3)) (xor (zr h150 L t (k + 2)) (zr h150 L t (k + 1))))
        (zr h150 L (t + 1) (k + 1))) = _
    rw [zr150_succ]
    generalize zr h150 L t (k + 4) = a
    generalize zr h150 L t (k + 3) = b
    generalize zr h150 L t (k + 2) = c
    generalize zr h150 L t (k + 1) = d
    generalize zr h150 L t k = e
    cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> rfl

/-- **The odd depths of rule 150 are black.** If depth `1` is black at every even tick up to `T`,
every odd depth is black at every even tick with depth plus tick at most `T + 1`. -/
theorem odd150 {L : Nat → Bool} {T : Nat} (hblack : ∀ s, 2 * s ≤ T → zr h150 L (2 * s) 1 = true) :
    ∀ m s, 2 * m + 1 + 2 * s ≤ T + 1 → zr h150 L (2 * s) (2 * m + 1) = true := by
  have key : ∀ m, (∀ s, 2 * m + 1 + 2 * s ≤ T + 1 → zr h150 L (2 * s) (2 * m + 1) = true) ∧
      (∀ s, 2 * m + 3 + 2 * s ≤ T + 1 → zr h150 L (2 * s) (2 * m + 3) = true) := by
    intro m
    induction m with
    | zero =>
      refine ⟨fun s hs => hblack s (by omega), fun s hs => ?_⟩
      rw [← (two_step150 L (2 * s)).1, show 2 * s + 2 = 2 * (s + 1) by omega]
      exact hblack (s + 1) (by omega)
    | succ m ih =>
      refine ⟨ih.2, fun s hs => ?_⟩
      have e := (two_step150 L (2 * s)).2 (2 * m + 1)
      rw [show 2 * m + 1 + 4 = 2 * (m + 1) + 3 by omega, show 2 * m + 1 + 2 = 2 * m + 3 by omega,
        show 2 * s + 2 = 2 * (s + 1) by omega, ih.2 (s + 1) (by omega), ih.2 s (by omega),
        ih.1 s (by omega)] at e
      revert e
      generalize zr h150 L (2 * s) (2 * (m + 1) + 3) = a
      cases a <;> decide
  exact fun m => (key m).1

/-- **Rule 150's wall deadline.** A start of width at most `W` turns depth `1` white at some even
tick at most `2 ⌈W / 2⌉`. -/
theorem deadline150 {L : Nat → Bool} {W : Nat} (hW : ∀ k, W < k → L k = false) :
    ∃ s, 2 * s ≤ 2 * ((W + 1) / 2) ∧ zr h150 L (2 * s) 1 = false := by
  apply Classical.byContradiction
  intro hno
  have hblack : ∀ s, 2 * s ≤ 2 * ((W + 1) / 2) → zr h150 L (2 * s) 1 = true := by
    intro s hs
    cases hc : zr h150 L (2 * s) 1 with
    | true => rfl
    | false => exact absurd ⟨s, hs, hc⟩ hno
  have e := odd150 hblack ((W + 1) / 2) 0 (by omega)
  rw [show 2 * ((W + 1) / 2) + 1 = (2 * ((W + 1) / 2)) + 1 from rfl,
    show 2 * 0 = 0 from rfl, zr_zero, hW _ (by omega)] at e
  exact Bool.noConfusion e

/-- Every row with all odd depths black keeps all odd depths black at every even tick. -/
theorem fwd150 {M : Nat → Bool} (hM : ∀ m, M (2 * m + 1) = true) :
    ∀ s m, zr h150 M (2 * s) (2 * m + 1) = true := by
  intro s
  induction s with
  | zero => intro m; rw [show 2 * 0 = 0 from rfl, zr_zero]; exact hM m
  | succ s ih =>
    intro m
    cases m with
    | zero =>
      rw [show 2 * (s + 1) = 2 * s + 2 by omega, (two_step150 M (2 * s)).1]
      exact ih 1
    | succ m =>
      rw [show 2 * (s + 1) = 2 * s + 2 by omega, show 2 * (m + 1) + 1 = 2 * m + 1 + 2 by omega,
        (two_step150 M (2 * s)).2 (2 * m + 1), show 2 * m + 1 + 4 = 2 * (m + 2) + 1 by omega,
        show 2 * m + 1 + 2 = 2 * (m + 1) + 1 by omega, ih (m + 2), ih (m + 1), ih m]
      rfl

/-- **Rule 150's deadline is sharp.** Every start of width at most `W` with all odd depths black
keeps depth `1` black at every even tick below `2 ⌈W / 2⌉`. -/
theorem sharp150 {L : Nat → Bool} {W : Nat} (hodd : ∀ k, k % 2 = 1 → k ≤ W → L k = true) :
    ∀ s, 2 * s < 2 * ((W + 1) / 2) → zr h150 L (2 * s) 1 = true := by
  intro s hs
  let M : Nat → Bool := fun k => if k % 2 = 1 then true else L k
  have hM : ∀ m, M (2 * m + 1) = true := fun m => by
    show (if (2 * m + 1) % 2 = 1 then true else L (2 * m + 1)) = true
    rw [ite_eq_left (by omega)]
  have agree : ∀ i, 1 ≤ i → i ≤ 1 + 2 * s → L i = M i := by
    intro i hi1 hi2
    show L i = if i % 2 = 1 then true else L i
    by_cases hi : i % 2 = 1
    · rw [ite_eq_left hi]; exact hodd i hi (by omega)
    · rw [ite_eq_right hi]
  rw [zr_cone h150 (2 * s) 1 agree]
  exact fwd150 hM s 0

end Rule30WallDeadlines
end Ruliology.CellularAutomata
