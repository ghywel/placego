import Ruliology.CellularAutomata.Rule30Jen

namespace Ruliology.CellularAutomata.Rule30MovingWall63
open Rule30Jen

/-- A rule-30 evolution of the whole line. -/
def IsR30Z (G : Nat → Int → Bool) : Prop :=
  ∀ t x, G (t + 1) x = rule (G t (x - 1)) (G t x) (G t (x + 1))

/-- The ring orbit of `1010000`: row `τ` as a 7-bit number, bit `j` the cell at diagonal index `j`. -/
def orbRows : List Nat := [5, 27, 101, 58, 71, 88, 43, 84, 47, 80, 51, 92, 39, 120, 11, 53, 74, 117, 10, 54, 75, 116, 15, 49, 86, 41, 94, 33, 102, 57, 78, 113, 22, 106, 21, 107, 20, 108, 23, 105, 30, 98, 45, 82, 61, 66, 77, 114, 29, 99, 44, 85, 42, 87, 40, 89, 46, 83, 60, 69, 90, 37, 122]

/-- The closure: `(key, ψ)` with `key = (tq * 7 + dq) * 2 ^ 16 + strip`. -/
def closure : List (Nat × Int) := [
  (22390803, 0),
  (22916156, 2),
  (22980167, 4),
  (23558099, -3),
  (24125626, -10),
  (24765207, -17),
  (24786352, -15),
  (25318552, -13),
  (25351320, -13),
  (25931737, -20),
  (26452046, -18),
  (26980595, -16),
  (27498780, -14),
  (27586470, -12),
  (28057786, -10),
  (28697367, -17),
  (275888, -15),
  (808088, -13),
  (840856, -13),
  (962521, -20),
  (1482830, -18),
  (2011379, -16),
  (2529564, -14),
  (3076006, -12),
  (3547322, -10),
  (3728151, -17),
  (4208048, -15),
  (4740248, -13),
  (4773016, -13),
  (5353433, -20),
  (5873742, -18),
  (6402291, -16),
  (6461724, -14),
  (7008166, -12),
  (7479482, -10),
  (8119063, -17),
  (8598960, -15),
  (9131160, -13),
  (9163928, -13),
  (9285593, -20),
  (9805902, -18),
  (10334451, -16),
  (10852636, -14),
  (11399078, -12),
  (11870394, -10),
  (12051223, -17),
  (12531120, -15),
  (13063320, -13),
  (13096088, -13),
  (13676505, -20),
  (14196814, -18),
  (14266611, -16),
  (14784796, -14),
  (15331238, -12),
  (15802554, -10),
  (16442135, -17),
  (16922032, -15),
  (16995480, -13),
  (17028248, -13),
  (17608665, -20),
  (18128974, -18),
  (18657523, -16),
  (19175708, -14),
  (19722150, -12),
  (19734714, -10),
  (20374295, -17),
  (20854192, -15),
  (21386392, -13),
  (21419160, -13),
  (21999577, -20),
  (22061134, -18),
  (22589683, -16),
  (23107868, -14),
  (23654310, -12)]

def ringBit (τ j : Nat) : Bool := (orbRows.getD τ 0).testBit j

theorem ring_table : ∀ τ, τ < 63 → ∀ j, j < 7 →
    ringBit ((τ + 1) % 63) ((j + 1) % 7) = rule (ringBit τ ((j + 1) % 7)) (ringBit τ j) (ringBit τ ((j + 6) % 7)) := by
  decide

/-- The background at alignment `(0, 4)`: `E t x` is the ring orbit's row `(t + 4) mod 63` at diagonal index `(t - x) mod 7`. -/
def E (t : Nat) (x : Int) : Bool := ringBit ((t + 4) % 63) (((t : Int) - x) % 7).toNat

theorem E_rule : IsR30Z E := by
  intro t x
  have h := ring_table ((t + 4) % 63) (Nat.mod_lt _ (by decide)) (((t : Int) - x) % 7).toNat (by omega)
  unfold E
  have e1 : (t + 1 + 4) % 63 = ((t + 4) % 63 + 1) % 63 := by omega
  have e2 : ((((t + 1 : Nat) : Int) - x) % 7).toNat = ((((t : Int) - x) % 7).toNat + 1) % 7 := by omega
  have e3 : (((t : Int) - (x - 1)) % 7).toNat = ((((t : Int) - x) % 7).toNat + 1) % 7 := by omega
  have e4 : (((t : Int) - (x + 1)) % 7).toNat = ((((t : Int) - x) % 7).toNat + 6) % 7 := by omega
  rw [e1, e2, e3, e4]; exact h

/-- The background at column `A + i`, from the phases `tq = t mod 63` and `dq = (t - A) mod 7`. -/
def refAt (tq dq : Nat) (i : Int) : Bool := ringBit ((tq + 4) % 63) (((dq : Int) - i) % 7).toNat

theorem refAt_spec {t tq dq : Nat} {A : Int} (htq : tq = t % 63) (hdq : dq = (((t : Int) - A) % 7).toNat) (i : Int) :
    refAt tq dq i = E t (A + i) := by
  unfold refAt E; subst htq; congr 1 <;> omega

/-- The first `n` values of `f` as bits. -/
def bitsOf (f : Nat → Bool) : Nat → Nat
  | 0 => 0
  | n + 1 => bitsOf f n ||| (if f n then 2 ^ n else 0)

def mask : Nat := 2 ^ 16 - 1

/-- The background's 16 cells right of the anchor, as a bit mask. -/
def refMask (tq dq : Nat) : Nat := bitsOf (fun i => refAt tq dq ((i : Int) + 1)) 16

/-- The window's 16 cells after one tick, from the anchor cell `eA`, the strip `m` and the input `b` beyond it. -/
def restOf (eA b : Bool) (m : Nat) : Nat :=
  (((m <<< 1) ||| (if eA then 1 else 0)) ^^^ (m ||| ((m >>> 1) ||| (if b then 2 ^ 15 else 0)))) &&& mask

/-- The anchor cell after one tick. -/
def n0Of (tq dq m : Nat) : Bool := rule (refAt tq dq (-1)) (refAt tq dq 0) (m.testBit 0)

/-- The anchor retreats when its own cell becomes a mismatch. -/
def retreats (tq dq m : Nat) : Bool := n0Of tq dq m != refAt ((tq + 1) % 63) ((dq + 1) % 7) 0

/-- One tick of the anchored window: the new phases, the new strip and whether the anchor retreats. -/
def step (tq dq m : Nat) (b : Bool) : Nat × Nat × Nat × Bool :=
  if retreats tq dq m then
    ((tq + 1) % 63, (dq + 2) % 7, ((restOf (refAt tq dq 0) b m <<< 1) ||| (if n0Of tq dq m then 1 else 0)) &&& mask, true)
  else ((tq + 1) % 63, (dq + 1) % 7, restOf (refAt tq dq 0) b m, false)

def keyOf (tq dq m : Nat) : Nat := (tq * 7 + dq) * 2 ^ 16 + m

def decode (k : Nat) : Nat × Nat × Nat := (k / 2 ^ 16 / 7, k / 2 ^ 16 % 7, k % 2 ^ 16)

/-- One checked edge: the successor of entry `e` under input `b` is in `cl`, its potential is `e.2 + 9 * motion + 2`, and
its strip differs from the background's. -/
def okStep (cl : List (Nat × Int)) (e : Nat × Int) (b : Bool) : Bool :=
  match cl.lookup (keyOf (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).1
      (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.1
      (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.2.1) with
  | some ψ' => ψ' == e.2 + (if (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.2.2 then -9 else 0) + 2 &&
      (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.2.1 !=
        refMask (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).1 (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.1
  | none => false

/-- Every entry of `cl` steps into `cl` under both inputs. -/
def checkCl (cl : List (Nat × Int)) : Bool := cl.all (fun e => okStep cl e false && okStep cl e true)

theorem closure_ok : checkCl closure = true := by decide +kernel

/-- The start: phases `(48, 5)` and the strip of the inserted edge at time `300`, with potential `0`. -/
def startKey : Nat := 22390803

theorem start_ok : closure.lookup startKey = some 0 := by decide +kernel

theorem closure_bounds : closure.all (fun e => decide (-20 ≤ e.2) && decide (e.2 ≤ 4)) = true := by decide +kernel

/-! ### Soundness of one tick -/

theorem testBit_ite_pow (c : Bool) (k i : Nat) : (if c then 2 ^ k else 0 : Nat).testBit i = (c && decide (k = i)) := by
  cases c <;> simp [Nat.testBit_two_pow]

theorem testBit_ite_one (c : Bool) (i : Nat) : (if c then 1 else 0 : Nat).testBit i = (c && decide (0 = i)) := by
  have := testBit_ite_pow c 0 i; simpa using this

theorem testBit_mask (i : Nat) : mask.testBit i = decide (i < 16) := by
  unfold mask; exact Nat.testBit_two_pow_sub_one 16 i

theorem and_mask_lt (a : Nat) : a &&& mask < 2 ^ 16 :=
  Nat.lt_of_le_of_lt Nat.and_le_right (by unfold mask; decide)

theorem restOf_bit {eA b : Bool} {m : Nat} (hm : m < 2 ^ 16) {i : Nat} (hi : i < 16) :
    (restOf eA b m).testBit i =
      rule (if i = 0 then eA else m.testBit (i - 1)) (m.testBit i) (if i = 15 then b else m.testBit (i + 1)) := by
  unfold restOf
  rw [Nat.testBit_and, testBit_mask, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_or, Nat.testBit_or,
    Nat.testBit_shiftLeft, Nat.testBit_shiftRight, testBit_ite_one, testBit_ite_pow]
  have h24 : m.testBit 16 = false :=
    Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hm (Nat.pow_le_pow_right (by decide) (by omega)))
  by_cases h0 : i = 0
  · subst h0; simp [rule]
  · have hi0 : ¬ (0 = i) := fun h => h0 h.symm
    by_cases h23 : i = 15
    · subst h23; simp [rule, h24]
    · have hi23 : ¬ (15 = i) := fun h => h23 h.symm
      simp [rule, h0, h23, hi0, hi23, hi, show i ≥ 1 by omega, show 1 + i = i + 1 by omega]

/-- The invariant at time `t`: the background holds at and left of the anchor `A`, the phases are `t`'s and `A`'s, and the
strip `m` holds the 16 cells right of the anchor. -/
def Inv (G : Nat → Int → Bool) (t : Nat) (A : Int) (tq dq m : Nat) : Prop :=
  tq = t % 63 ∧ dq = (((t : Int) - A) % 7).toNat ∧ (∀ x, x ≤ A → G t x = E t x) ∧ m < 2 ^ 16 ∧
    ∀ i, i < 16 → m.testBit i = G t (A + 1 + i)

/-- **One tick is sound.** On a rule-30 evolution of the whole line, the invariant passes to the next tick with the anchor
moved by `step`'s retreat flag, whatever the cell beyond the window is. -/
theorem step_sound {G : Nat → Int → Bool} (hG : IsR30Z G) {t : Nat} {A : Int} {tq dq m : Nat}
    (h : Inv G t A tq dq m) :
    Inv G (t + 1) (if (step tq dq m (G t (A + 17))).2.2.2 then A - 1 else A)
      (step tq dq m (G t (A + 17))).1 (step tq dq m (G t (A + 17))).2.1 (step tq dq m (G t (A + 17))).2.2.1 := by
  obtain ⟨htq, hdq, hE, hm, hs⟩ := h
  have hrefA : refAt tq dq 0 = G t A := by
    rw [refAt_spec htq hdq, show A + 0 = A by omega]; exact (hE A (Int.le_refl A)).symm
  have hrefAm : refAt tq dq (-1) = G t (A - 1) := by
    rw [refAt_spec htq hdq, show A + -1 = A - 1 by omega]; exact (hE (A - 1) (by omega)).symm
  have hcell : ∀ i, i < 16 → (restOf (refAt tq dq 0) (G t (A + 17)) m).testBit i = G (t + 1) (A + 1 + i) := by
    intro i hi
    rw [restOf_bit hm hi, hG]
    have e1 : (if i = 0 then refAt tq dq 0 else m.testBit (i - 1)) = G t (A + 1 + (i : Int) - 1) := by
      by_cases h0 : i = 0
      · subst h0; simp only [↓reduceIte]; rw [hrefA]; congr 1; omega
      · simp only [h0, ↓reduceIte]; rw [hs (i - 1) (by omega)]; congr 1; omega
    have e2 : m.testBit i = G t (A + 1 + (i : Int)) := hs i hi
    have e3 : (if i = 15 then G t (A + 17) else m.testBit (i + 1)) = G t (A + 1 + (i : Int) + 1) := by
      by_cases h23 : i = 15
      · subst h23; simp only [↓reduceIte]; congr 1; omega
      · simp only [h23, ↓reduceIte]; rw [hs (i + 1) (by omega)]; congr 1; omega
    rw [e1, e2, e3]
  have hn0 : n0Of tq dq m = G (t + 1) A := by
    unfold n0Of
    rw [hrefAm, hrefA, hs 0 (by omega), hG, show A + 1 + ((0 : Nat) : Int) = A + 1 by omega]
  have hnext : refAt ((tq + 1) % 63) ((dq + 1) % 7) 0 = E (t + 1) A := by
    rw [refAt_spec (t := t + 1) (A := A) (by omega) (by omega)]; rw [show A + 0 = A by omega]
  have hleft : ∀ x, x ≤ A - 1 → G (t + 1) x = E (t + 1) x := by
    intro x hx
    rw [hG, E_rule, hE (x - 1) (by omega), hE x (by omega), hE (x + 1) (by omega)]
  unfold step
  by_cases hr : retreats tq dq m = true
  · simp only [hr, ite_true]
    refine ⟨by omega, by omega, fun x hx => hleft x hx, and_mask_lt _, ?_⟩
    intro i hi
    rw [Nat.testBit_and, testBit_mask, Nat.testBit_or, Nat.testBit_shiftLeft, testBit_ite_one]
    by_cases h0 : i = 0
    · subst h0; simp [hn0]
    · have hi0 : ¬ (0 = i) := fun h => h0 h.symm
      simp only [hi0, decide_false, Bool.and_false, Bool.or_false, show i ≥ 1 by omega, decide_true, Bool.true_and,
        show i < 16 from hi]
      rw [hcell (i - 1) (by omega), Bool.and_true]
      congr 1; omega
  · have hr' : retreats tq dq m = false := by simpa using hr
    simp only [hr', Bool.false_eq_true, ite_false]
    have hstay : G (t + 1) A = E (t + 1) A := by
      unfold retreats at hr'; rw [hn0, hnext] at hr'; simpa using hr'
    refine ⟨by omega, by omega, fun x hx => ?_, by unfold restOf; exact and_mask_lt _, fun i hi => hcell i hi⟩
    rcases Int.lt_or_eq_of_le hx with hlt | heq
    · exact hleft x (by omega)
    · rw [heq]; exact hstay

/-! ### The closure carries the invariant for ever -/

theorem lookup_mem : ∀ (l : List (Nat × Int)) (k : Nat) (v : Int), l.lookup k = some v → (k, v) ∈ l
  | [], _, _, h => by simp [List.lookup] at h
  | (k', v') :: l, k, v, h => by
    unfold List.lookup at h
    split at h
    · rename_i hk
      have hv : v' = v := by simpa using h
      have hkk : k = k' := by simpa using hk
      subst hv; subst hkk; exact List.mem_cons_self
    · exact List.mem_cons_of_mem _ (lookup_mem l k v h)

theorem decode_keyOf {tq dq m : Nat} (hdq : dq < 7) (hm : m < 2 ^ 16) : decode (keyOf tq dq m) = (tq, dq, m) := by
  unfold decode keyOf
  have h : (2 : Nat) ^ 16 = 65536 := rfl
  rw [h] at hm ⊢
  have e1 : ((tq * 7 + dq) * 65536 + m) / 65536 = tq * 7 + dq := by omega
  have e2 : ((tq * 7 + dq) * 65536 + m) % 65536 = m := by omega
  rw [e1, e2]
  have e3 : (tq * 7 + dq) / 7 = tq := by omega
  have e4 : (tq * 7 + dq) % 7 = dq := by omega
  rw [e3, e4]

theorem okStep_spec {cl : List (Nat × Int)} {e : Nat × Int} {b : Bool} (h : okStep cl e b = true) :
    ∃ ψ', cl.lookup (keyOf (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).1
        (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.1
        (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.2.1) = some ψ' ∧
      ψ' = e.2 + (if (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.2.2 then -9 else 0) + 2 ∧
      (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.2.1 ≠
        refMask (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).1
          (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.1 := by
  unfold okStep at h
  split at h
  · rename_i ψ' hl
    simp only [Bool.and_eq_true, beq_iff_eq, bne_iff_ne, ne_eq] at h
    exact ⟨ψ', hl, h.1, h.2⟩
  · exact absurd h (by simp)

theorem checkCl_spec {cl : List (Nat × Int)} (hok : checkCl cl = true) {k : Nat} {ψ : Int} (hk : cl.lookup k = some ψ)
    (b : Bool) : okStep cl (k, ψ) b = true := by
  unfold checkCl at hok
  have he := List.all_eq_true.1 hok (k, ψ) (lookup_mem _ _ _ hk)
  simp only [Bool.and_eq_true] at he
  cases b
  · exact he.1
  · exact he.2

theorem step_dq_lt (tq dq m : Nat) (b : Bool) : (step tq dq m b).2.1 < 7 := by
  unfold step; split
  · exact Nat.mod_lt _ (by decide)
  · exact Nat.mod_lt _ (by decide)

/-- **The anchored law, for any checked list.** From a state of `cl` with potential `ψ0` at time `t0` and anchor `A0`, for
every `n` the invariant holds at time `t0 + n` with some anchor `A`, the state is in `cl` with potential
`ψ0 + 9 (A - A0) + 2 n`, and its strip differs from the background's. -/
theorem anchored {cl : List (Nat × Int)} (hok : checkCl cl = true) {G : Nat → Int → Bool} (hG : IsR30Z G)
    {t0 : Nat} {A0 : Int} {tq0 dq0 m0 : Nat} {ψ0 : Int} (hinv : Inv G t0 A0 tq0 dq0 m0) (hdq0 : dq0 < 7)
    (hk : cl.lookup (keyOf tq0 dq0 m0) = some ψ0) (hne0 : m0 ≠ refMask tq0 dq0) :
    ∀ n : Nat, ∃ A : Int, ∃ tq dq m : Nat, ∃ ψ : Int, Inv G (t0 + n) A tq dq m ∧ dq < 7 ∧
      cl.lookup (keyOf tq dq m) = some ψ ∧ ψ = ψ0 + 9 * (A - A0) + 2 * (n : Int) ∧ m ≠ refMask tq dq := by
  intro n
  induction n with
  | zero =>
    exact ⟨A0, tq0, dq0, m0, ψ0, hinv, hdq0, hk, by omega, hne0⟩
  | succ n ih =>
    obtain ⟨A, tq, dq, m, ψ, hI, hdq, hl, hψ, -⟩ := ih
    have hdec : decode (keyOf tq dq m) = (tq, dq, m) := decode_keyOf hdq hI.2.2.2.1
    have hc := okStep_spec (checkCl_spec hok hl (G (t0 + n) (A + 17)))
    simp only [hdec] at hc
    obtain ⟨ψ', hl', hψ', hne⟩ := hc
    have hs := step_sound hG hI
    refine ⟨if (step tq dq m (G (t0 + n) (A + 17))).2.2.2 then A - 1 else A,
      (step tq dq m (G (t0 + n) (A + 17))).1, (step tq dq m (G (t0 + n) (A + 17))).2.1,
      (step tq dq m (G (t0 + n) (A + 17))).2.2.1, ψ', ?_, step_dq_lt _ _ _ _, hl', ?_, hne⟩
    · rw [show t0 + (n + 1) = t0 + n + 1 by omega]; exact hs
    · rw [hψ', hψ]
      cases (step tq dq m (G (t0 + n) (A + 17))).2.2.2 <;> simp <;> omega

/-! ### Bits of masks -/

theorem testBit_bitsOf (f : Nat → Bool) : ∀ n i, (bitsOf f n).testBit i = (decide (i < n) && f i)
  | 0, i => by simp [bitsOf]
  | n + 1, i => by
    unfold bitsOf
    rw [Nat.testBit_or, testBit_bitsOf f n i, testBit_ite_pow]
    by_cases h : i = n
    · subst h; simp
    · have h' : ¬ n = i := fun e => h e.symm
      by_cases hi : i < n
      · simp [hi, show i < n + 1 by omega, h']
      · simp [hi, show ¬ i < n + 1 by omega, h']

theorem bitsOf_lt (f : Nat → Bool) : ∀ n, bitsOf f n < 2 ^ n
  | 0 => by simp [bitsOf]
  | n + 1 => by
    unfold bitsOf
    have ih := bitsOf_lt f n
    have h1 : bitsOf f n < 2 ^ (n + 1) := Nat.lt_of_lt_of_le ih (Nat.pow_le_pow_right (by decide) (by omega))
    have h2 : (if f n then 2 ^ n else 0) < 2 ^ (n + 1) := by
      split
      · exact Nat.pow_lt_pow_right (by decide) (by omega)
      · exact Nat.two_pow_pos _
    exact Nat.or_lt_two_pow h1 h2

/-- A strip that differs from the background's mask holds a mismatch with the background inside the window. -/
theorem mismatch_of_ne {G : Nat → Int → Bool} {t : Nat} {A : Int} {tq dq m : Nat} (h : Inv G t A tq dq m)
    (hne : m ≠ refMask tq dq) : ∃ x, A < x ∧ x ≤ A + 16 ∧ G t x ≠ E t x := by
  obtain ⟨htq, hdq, -, hm, hs⟩ := h
  have : ∃ i, m.testBit i ≠ (refMask tq dq).testBit i := by
    apply Classical.byContradiction
    intro hc
    apply hne
    apply Nat.eq_of_testBit_eq
    intro i
    apply Classical.byContradiction
    intro hi
    exact hc ⟨i, hi⟩
  obtain ⟨i, hi⟩ := this
  have hi24 : i < 16 := by
    apply Classical.byContradiction
    intro hge
    have h1 : m.testBit i = false := Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hm (Nat.pow_le_pow_right (by decide) (by omega)))
    have h2 : (refMask tq dq).testBit i = false := by unfold refMask; rw [testBit_bitsOf]; simp [show ¬ i < 16 by omega]
    exact hi (by rw [h1, h2])
  refine ⟨A + 1 + i, by omega, by omega, ?_⟩
  rw [← hs i hi24]
  unfold refMask at hi
  rw [testBit_bitsOf, refAt_spec htq hdq] at hi
  simpa [hi24, show A + ((i : Int) + 1) = A + 1 + i by omega] using hi

/-! ### The inserted edge on the ring background -/

/-- The row at time `0`: the background left of `0`, a black cell at `0`, white to the right. -/
def initRow (x : Int) : Bool := if x < 0 then E 0 x else decide (x = 0)

/-- Its rule-30 evolution on the whole line. -/
def Gedge : Nat → Int → Bool
  | 0, x => initRow x
  | t + 1, x => rule (Gedge t (x - 1)) (Gedge t x) (Gedge t (x + 1))

theorem Gedge_isR30 : IsR30Z Gedge := fun _ _ => rfl

/-- Light cone: the columns `x < -t` are still the background. -/
theorem Gedge_left : ∀ t : Nat, ∀ x : Int, x + t < 0 → Gedge t x = E t x := by
  intro t
  induction t with
  | zero => intro x hx; show initRow x = _; unfold initRow; simp [show x < 0 by omega]
  | succ t ih =>
    intro x hx
    show rule (Gedge t (x - 1)) (Gedge t x) (Gedge t (x + 1)) = _
    rw [ih (x - 1) (by omega), ih x (by omega), ih (x + 1) (by omega), ← E_rule]

/-- Whole-row step on bit masks: bit `i` is column `lo + i`. -/
def stepN (a : Nat) : Nat := (a <<< 1) ^^^ (a ||| (a >>> 1))

theorem stepN_bit (a i : Nat) (hi : 1 ≤ i) :
    (stepN a).testBit i = rule (a.testBit (i - 1)) (a.testBit i) (a.testBit (i + 1)) := by
  unfold stepN
  rw [Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft, Nat.testBit_shiftRight]
  simp [show i ≥ 1 from hi, show 1 + i = i + 1 by omega, rule]

def lo : Int := -700

/-- The edge's row on `x = -700 .. 0`; white beyond. -/
def row0 : Nat := bitsOf (fun i => initRow (lo + i)) 701

def rowAt : Nat → Nat
  | 0 => row0
  | t + 1 => stepN (rowAt t)

theorem row0_spec : ∀ i, row0.testBit i = Gedge 0 (lo + i) := by
  intro i
  show _ = initRow (lo + i)
  unfold row0; rw [testBit_bitsOf]
  by_cases hi : i < 701
  · simp [hi]
  · simp only [hi, decide_false, Bool.false_and]
    unfold initRow lo
    simp [show ¬ (-700 + (i : Int) < 0) by omega, show ¬ (-700 + (i : Int) = 0) by omega]

theorem rowAt_spec : ∀ t i, t ≤ i → (rowAt t).testBit i = Gedge t (lo + i) := by
  intro t
  induction t with
  | zero => intro i _; exact row0_spec i
  | succ t ih =>
    intro i hi
    show (stepN (rowAt t)).testBit i = rule (Gedge t (lo + i - 1)) (Gedge t (lo + i)) (Gedge t (lo + i + 1))
    rw [stepN_bit _ _ (by omega), ih _ (by omega), ih _ (by omega), ih _ (by omega)]
    rw [show lo + ((i - 1 : Nat) : Int) = lo + (i : Int) - 1 by omega,
      show lo + ((i + 1 : Nat) : Int) = lo + (i : Int) + 1 by omega]

/-- The start check at `t = 300`: columns `-300 .. -55` are the background, and columns `-54 .. -39` are the strip of
`startKey`, which differs from the background's. -/
def entryOK : Bool :=
  let r := rowAt 300
  (List.range 246).all (fun j => r.testBit (400 + j) == E 300 (lo + ((400 + j : Nat) : Int))) &&
  (List.range 16).all (fun j => r.testBit (646 + j) == (startKey % 2 ^ 16).testBit j) &&
  (startKey % 2 ^ 16 != refMask 48 5) && (keyOf 48 5 (startKey % 2 ^ 16) == startKey)

theorem entry_ok : entryOK = true := by decide +kernel

theorem entry_inv : Inv Gedge 300 (-55) 48 5 (startKey % 2 ^ 16) ∧ startKey % 2 ^ 16 ≠ refMask 48 5 ∧
    keyOf 48 5 (startKey % 2 ^ 16) = startKey := by
  have h := entry_ok
  unfold entryOK at h
  simp only [Bool.and_eq_true, List.all_eq_true, List.mem_range, beq_iff_eq, bne_iff_ne, ne_eq] at h
  obtain ⟨⟨⟨hrow, hstrip⟩, hne⟩, hkey⟩ := h
  refine ⟨⟨by decide, by decide, fun x hx => ?_, Nat.mod_lt _ (by decide), fun i hi => ?_⟩, hne, hkey⟩
  · by_cases hlt : x + 300 < 0
    · exact Gedge_left 300 x (by omega)
    · have e := hrow (x + 300).toNat (by omega)
      rw [rowAt_spec 300 _ (by omega)] at e
      rw [show lo + ((400 + (x + 300).toNat : Nat) : Int) = x by unfold lo; omega] at e
      exact e
  · have e := hstrip i hi
    rw [rowAt_spec 300 _ (by omega)] at e
    have hx : lo + ((646 + i : Nat) : Int) = -55 + 1 + (i : Int) := by unfold lo; omega
    rw [hx] at e
    exact e.symm

/-- Radius-one locality: two rule-30 evolutions that agree at time `0` on `x ≤ c` agree at time `t` on `x ≤ c - t`. -/
theorem agree_cone {G H : Nat → Int → Bool} (hG : IsR30Z G) (hH : IsR30Z H) {c : Int}
    (h0 : ∀ x, x ≤ c → H 0 x = G 0 x) : ∀ t : Nat, ∀ x, x ≤ c - t → H t x = G t x := by
  intro t
  induction t with
  | zero => intro x hx; exact h0 x (by omega)
  | succ t ih =>
    intro x hx
    rw [hH, hG, ih (x - 1) (by omega), ih x (by omega), ih (x + 1) (by omega)]

/-- The law from the start invariant, for any rule-30 evolution of the whole line. -/
theorem law_from {H : Nat → Int → Bool} (hH : IsR30Z H) (hinv : Inv H 300 (-55) 48 5 (startKey % 2 ^ 16)) :
    ∀ t : Nat, 300 ≤ t → ∃ A : Int, (∀ x, x ≤ A → H t x = E t x) ∧
    (∃ x, A < x ∧ x ≤ A + 16 ∧ H t x ≠ E t x) ∧
    -20 ≤ 9 * (A + 55) + 2 * ((t : Int) - 300) ∧ 9 * (A + 55) + 2 * ((t : Int) - 300) ≤ 4 := by
  intro t ht
  obtain ⟨-, hne, hkey⟩ := entry_inv
  have hk : closure.lookup (keyOf 48 5 (startKey % 2 ^ 16)) = some 0 := by rw [hkey]; exact start_ok
  obtain ⟨A, tq, dq, m, ψ, hI, -, hl, hψ, hne'⟩ :=
    anchored closure_ok hH hinv (by decide) hk hne (t - 300)
  have hb := List.all_eq_true.1 closure_bounds _ (lookup_mem _ _ _ hl)
  simp only [Bool.and_eq_true, decide_eq_true_eq] at hb
  rw [show 300 + (t - 300) = t by omega] at hI
  refine ⟨A, hI.2.2.1, mismatch_of_ne hI hne', ?_, ?_⟩ <;> push_cast [show ((t - 300 : Nat) : Int) = (t : Int) - 300 by omega] at hψ <;> omega

/-- **The front law of the inserted edge on the ring background `1010000` (temporal period 63).** For every `t ≥ 300`
there is an anchor `A` with the background intact at and left of `A`, a mismatch within the 16 cells right of it, and
`-20 ≤ 9 (A + 55) + 2 (t - 300) ≤ 4`. So the leftmost difference moves left at exactly `2/9` cell per tick. -/
theorem edge_law : ∀ t : Nat, 300 ≤ t → ∃ A : Int, (∀ x, x ≤ A → Gedge t x = E t x) ∧
    (∃ x, A < x ∧ x ≤ A + 16 ∧ Gedge t x ≠ E t x) ∧
    -20 ≤ 9 * (A + 55) + 2 * ((t : Int) - 300) ∧ 9 * (A + 55) + 2 * ((t : Int) - 300) ≤ 4 :=
  law_from Gedge_isR30 entry_inv.1

/-- **Any right tail.** The same law holds for every rule-30 evolution of the whole line whose initial row agrees with the
inserted edge's at every `x ≤ 261`, whatever its cells beyond `261`: at `t = 300` the two agree on `x ≤ -39`, which holds
the whole start invariant, and the closure accepts every later input from the right. -/
theorem edge_law_tail {H : Nat → Int → Bool} (hH : IsR30Z H) (hag : ∀ x, x ≤ 261 → H 0 x = Gedge 0 x) :
    ∀ t : Nat, 300 ≤ t → ∃ A : Int, (∀ x, x ≤ A → H t x = E t x) ∧
    (∃ x, A < x ∧ x ≤ A + 16 ∧ H t x ≠ E t x) ∧
    -20 ≤ 9 * (A + 55) + 2 * ((t : Int) - 300) ∧ 9 * (A + 55) + 2 * ((t : Int) - 300) ≤ 4 := by
  have hc := agree_cone Gedge_isR30 hH hag 300
  obtain ⟨⟨htq, hdq, hE, hm, hs⟩, -, -⟩ := entry_inv
  refine law_from hH ⟨htq, hdq, fun x hx => ?_, hm, fun i hi => ?_⟩
  · rw [hc x (by omega)]; exact hE x hx
  · rw [hc _ (by omega)]; exact hs i hi

end Ruliology.CellularAutomata.Rule30MovingWall63
