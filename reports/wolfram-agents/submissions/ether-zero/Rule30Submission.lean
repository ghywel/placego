import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30Ether

/-!
# Rule 30: the classic ether absorbs a black edge, so the edge's front speed is exactly zero

Insert one black cell, with white to its right, into the ether of `Rule30Ether` (spatial period 7, temporal period 4)
at any of its 28 alignments `(c0, c1)`, and evolve by rule 30 on the whole line (`G`). Then from a finite time on, the
ether is undisturbed at and left of a fixed column `xB`, and the disturbance never heals within the 13 cells to its
right (`edge_pinned`). The leftmost cell where `G` differs from the ether therefore stays in a fixed window for ever:
its speed is exactly zero, at every alignment.

* `trap_two_sided`: the ether-wall trap of `Rule30Ether` (`trap_invariant`, Lowry) on the whole line. The prescribed
  column is replaced by the induction hypothesis on the columns left of the B3 column.
* `G_left`: the light cone (columns `x < -t` are still the ether).
* `iter3_G`: a finite list simulation (`lin3` of `Rule30StripCertificates`) agrees with `G` on its range.
* `entry_c0_c1`: for each alignment, the kernel checks that by a stated time `t1 ≤ 222` the columns `-t1 .. xB` are the
  ether, `xB` is a B3 column, and the next 13 cells form one of the 109 wall states (`checkEntry`, by `decide`).
* `wall_ne_ref_all`: no wall state equals the ether's own 13 cells after a B3 (by `decide`), so the disturbance never
  heals.

Prior art: the ether and its wall trap are Lowry's (`Rule30Ether`), used there to exclude ether walls beside a periodic
center column. This module proves the trap on the whole line and shows that an inserted edge enters it at every
alignment. Scope: the lab frame of the ether; nothing here concerns the center column of the single-cell pattern.
-/

namespace Rule30Submission
open Ruliology.CellularAutomata
open Rule30Jen Rule30StripCertificates Rule30Ether

/-- A rule-30 evolution of the whole line. -/
def IsR30Z (G : Nat → Int → Bool) : Prop :=
  ∀ t x, G (t + 1) x = rule (G t (x - 1)) (G t x) (G t (x + 1))

/-- The ether at column `x` (an integer) with spatial offset `c`: the kit's ether column `(x + c) mod 7`. -/
def etherZ (c x : Int) (φ : Nat) : Bool := ether ((x + c) % 7).toNat φ

theorem etherZ_congr {c x y : Int} {φ ψ : Nat} (h : (x + c) % 7 = (y + c) % 7) (hφ : φ % 4 = ψ % 4) :
    etherZ c x φ = etherZ c y ψ := by
  unfold etherZ; rw [h]; exact ether_congr rfl hφ

theorem etherZ_eq_ether {c x : Int} {j : Nat} {φ ψ : Nat} (h : (x + c) % 7 = (j : Int) % 7) (hφ : φ % 4 = ψ % 4) :
    etherZ c x φ = ether j ψ := by
  unfold etherZ; exact ether_congr (by omega) hφ

/-- The ether is a rule-30 orbit of the whole line. -/
theorem etherZ_rule (c x : Int) (φ : Nat) :
    etherZ c x (φ + 1) = rule (etherZ c (x - 1) φ) (etherZ c x φ) (etherZ c (x + 1) φ) := by
  have h := ether_rule ((x + c) % 7).toNat φ
  have h1 : etherZ c (x - 1) φ = ether (((x + c) % 7).toNat + 6) φ := etherZ_eq_ether (by omega) rfl
  have h2 : etherZ c (x + 1) φ = ether (((x + c) % 7).toNat + 1) φ := etherZ_eq_ether (by omega) rfl
  rw [h1, h2]; exact h

/-- Columns `xB + 1, …, xB + m` of `G` at time `t`. -/
def rowZ (G : Nat → Int → Bool) (t : Nat) (xB : Int) (m : Nat) : List Bool := seg (fun i => G t (xB + (i : Int) + 1)) m

theorem rowZ_succ {G : Nat → Int → Bool} (hG : IsR30Z G) (t : Nat) (xB : Int) (b : Nat) :
    rowZ G (t + 1) xB b = lin3 (G t xB :: (rowZ G t xB b ++ [G t (xB + (b : Int) + 1)])) := by
  have e1 : rowZ G t xB b ++ [G t (xB + (b : Int) + 1)] = rowZ G t xB (b + 1) := by
    unfold rowZ; rw [seg_succ]
  have e2 : G t xB :: rowZ G t xB (b + 1) = seg (fun i => G t (xB + (i : Int))) (b + 2) := by
    show G t xB :: rowZ G t xB (b + 1) = G t (xB + ((0 : Nat) : Int)) :: seg (fun i => G t (xB + ((i + 1 : Nat) : Int))) (b + 1)
    rw [show xB + ((0 : Nat) : Int) = xB by omega]
    unfold rowZ
    congr 1
    exact seg_congr _ _ _ (fun i _ => by rw [show xB + ((i + 1 : Nat) : Int) = xB + (i : Int) + 1 by omega])
  rw [e1, e2, lin3_seg]
  unfold rowZ
  exact seg_congr _ _ _ (fun i _ => by
    rw [hG t (xB + (i : Int) + 1), show xB + (i : Int) + 1 - 1 = xB + (i : Int) by omega,
      show xB + ((i + 1 : Nat) : Int) = xB + (i : Int) + 1 by omega,
      show xB + ((i + 2 : Nat) : Int) = xB + (i : Int) + 1 + 1 by omega]
    rfl)

theorem rowZ_head (G : Nat → Int → Bool) (t : Nat) (xB : Int) (b : Nat) :
    (rowZ G t xB (b + 1)).headD false = G t (xB + 1) := by
  show G t (xB + ((0 : Nat) : Int) + 1) = G t (xB + 1)
  rw [show xB + ((0 : Nat) : Int) + 1 = xB + 1 by omega]

/-- **The two-sided ether-wall trap.** On a rule-30 evolution of the whole line, if at time `t1` every column `x ≤ xB` is the
ether (offset `c`, phase `t1 + s`), column `xB` is a B3, and columns `xB + 1 .. xB + 13` form a wall state, then this holds at
every later time, whatever the cells right of the strip do. -/
theorem trap_two_sided {G : Nat → Int → Bool} (hG : IsR30Z G) (c xB : Int) (s t1 : Nat)
    (hk : (xB + c) % 7 = 2)
    (hE : ∀ x, x ≤ xB → G t1 x = etherZ c x (t1 + s))
    (hW : ((t1 + s) % 4, rowZ G t1 xB 13) ∈ wallStates) :
    ∀ n, (∀ x, x ≤ xB → G (t1 + n) x = etherZ c x (t1 + n + s)) ∧
      ((t1 + n + s) % 4, rowZ G (t1 + n) xB 13) ∈ wallStates := by
  intro n
  induction n with
  | zero => exact ⟨fun x hx => by simpa using hE x hx, by simpa using hW⟩
  | succ n ih =>
    obtain ⟨hE', hW'⟩ := ih
    have hph : t1 + n + 1 + s = (t1 + n + s) + 1 := by omega
    have htt : t1 + (n + 1) = (t1 + n) + 1 := by omega
    -- column `xB` is the B3 column: its value is `ether 2` at the phase
    have hck : G (t1 + n) xB = ether 2 ((t1 + n + s) % 4) := by
      rw [hE' xB (Int.le_refl xB)]; exact etherZ_eq_ether (by omega) (by omega)
    refine ⟨fun x hx => ?_, ?_⟩
    · rw [htt, hG, hph, etherZ_rule c x (t1 + n + s), hE' (x - 1) (by omega), hE' x hx]
      rcases Int.lt_or_eq_of_le hx with hlt | heq
      · rw [hE' (x + 1) (by omega)]
      · -- `x = xB`, the B3: its right neighbour is the wall's head
        subst heq
        cases hb : etherZ c x (t1 + n + s) with
        | true => simp [rule]
        | false =>
          have hw2 : ether 2 ((t1 + n + s) % 4) = false := by
            rw [← hb]; exact (etherZ_eq_ether (by omega) (by omega)).symm
          have hhead := (wall_facts hW').1 hw2
          rw [rowZ_head] at hhead
          rw [hhead]
          congr 1
          exact (etherZ_eq_ether (by omega) (by omega)).symm
    · rw [htt, rowZ_succ hG, hph, hck]
      have e := (wall_facts hW').2 (G (t1 + n) (xB + ((13 : Nat) : Int) + 1))
      rwa [show ((t1 + n + s) % 4 + 1) % 4 = (t1 + n + s + 1) % 4 by omega] at e

/-- Hence the leftmost mismatch with the ether is bounded below: no column `x ≤ xB` ever differs from the ether again. -/
theorem news_bounded {G : Nat → Int → Bool} (hG : IsR30Z G) (c xB : Int) (s t1 : Nat)
    (hk : (xB + c) % 7 = 2)
    (hE : ∀ x, x ≤ xB → G t1 x = etherZ c x (t1 + s))
    (hW : ((t1 + s) % 4, rowZ G t1 xB 13) ∈ wallStates) :
    ∀ t, t1 ≤ t → ∀ x, x ≤ xB → G t x = etherZ c x (t + s) := by
  intro t ht x hx
  have h := (trap_two_sided hG c xB s t1 hk hE hW (t - t1)).1 x hx
  rwa [show t1 + (t - t1) = t by omega] at h


/-! ### The inserted edge -/

/-- The row at time `0`: the ether (offset `c0`, phase `c1`) left of `0`, a black cell at `0`, white to the right. -/
def initRow (c0 c1 : Nat) (x : Int) : Bool :=
  if x < 0 then etherZ c0 x c1 else if x = 0 then true else false

/-- Its rule-30 evolution on the whole line. -/
def G (c0 c1 : Nat) : Nat → Int → Bool
  | 0, x => initRow c0 c1 x
  | t + 1, x => rule (G c0 c1 t (x - 1)) (G c0 c1 t x) (G c0 c1 t (x + 1))

theorem G_isR30 (c0 c1 : Nat) : IsR30Z (G c0 c1) := fun _ _ => rfl

/-- Light cone: the columns `x < -t` are still the ether. -/
theorem G_left (c0 c1 : Nat) : ∀ t : Nat, ∀ x : Int, x + t < 0 → G c0 c1 t x = etherZ c0 x (t + c1) := by
  intro t
  induction t with
  | zero =>
    intro x hx
    show initRow c0 c1 x = _
    unfold initRow; simp [show x < 0 by omega]
  | succ t ih =>
    intro x hx
    show rule (G c0 c1 t (x - 1)) (G c0 c1 t x) (G c0 c1 t (x + 1)) = _
    rw [ih (x - 1) (by omega), ih x (by omega), ih (x + 1) (by omega),
      show t + 1 + c1 = (t + c1) + 1 by omega, etherZ_rule]

/-! ### A finite simulation, bridged to `G` -/

def iter3 : Nat → List Bool → List Bool
  | 0, l => l
  | k + 1, l => iter3 k (lin3 l)

theorem lin3_G (c0 c1 t : Nat) (lo : Int) (m : Nat) :
    lin3 (seg (fun i => G c0 c1 t (lo + (i : Int))) (m + 2)) = seg (fun i => G c0 c1 (t + 1) (lo + 1 + (i : Int))) m := by
  rw [lin3_seg]
  apply seg_congr
  intro i _
  show xor _ _ = rule (G c0 c1 t (lo + 1 + (i : Int) - 1)) (G c0 c1 t (lo + 1 + (i : Int))) (G c0 c1 t (lo + 1 + (i : Int) + 1))
  rw [show lo + 1 + (i : Int) - 1 = lo + (i : Int) by omega, show lo + ((i + 1 : Nat) : Int) = lo + 1 + (i : Int) by omega,
    show lo + ((i + 2 : Nat) : Int) = lo + 1 + (i : Int) + 1 by omega]
  rfl

theorem iter3_G (c0 c1 : Nat) : ∀ (k t : Nat) (lo : Int) (n : Nat),
    iter3 k (seg (fun i => G c0 c1 t (lo + (i : Int))) (n + 2 * k)) = seg (fun i => G c0 c1 (t + k) (lo + k + (i : Int))) n := by
  intro k
  induction k with
  | zero => intro t lo n; simp [iter3]
  | succ k ih =>
    intro t lo n
    show iter3 k (lin3 _) = _
    rw [show n + 2 * (k + 1) = (n + 2 * k) + 2 by omega, lin3_G, ih (t + 1) (lo + 1) n]
    rw [show t + 1 + k = t + (k + 1) by omega, show lo + 1 + (k : Int) = lo + ((k + 1 : Nat) : Int) by omega]

/-! ### The finite entry check -/

/-- The entry check for one alignment: simulate from `lo = -2 t1` to time `t1`; the columns `-t1 .. xB` must be the
ether, column `xB` a B3, and the 13 cells after it a wall state at the phase. -/
def checkEntry (c0 c1 t1 : Nat) (xB : Int) : Bool :=
  let lo : Int := -((2 * t1 : Nat) : Int)
  let n : Nat := (xB + 13 + (t1 : Int) - lo + 1).toNat
  let L := iter3 t1 (seg (fun i => initRow c0 c1 (lo + (i : Int))) n)
  decide (0 ≤ xB + (t1 : Int) + 1) && decide ((xB + (c0 : Int)) % 7 = 2) &&
  (List.range (xB + (t1 : Int) + 1).toNat).all (fun i => L.getD i false == etherZ c0 (-(t1 : Int) + (i : Int)) (t1 + c1)) &&
  wallStates.contains ((t1 + c1) % 4, (L.drop (xB + (t1 : Int) + 1).toNat).take 13)


theorem seg_getD' : ∀ (n : Nat) (f : Nat → Bool) (i : Nat), i < n → (seg f n).getD i false = f i
  | 0, _, _, h => absurd h (Nat.not_lt_zero _)
  | n + 1, f, 0, _ => rfl
  | n + 1, f, i + 1, h => by
    show (seg (fun j => f (j + 1)) n).getD i false = f (i + 1)
    exact seg_getD' n (fun j => f (j + 1)) i (by omega)

theorem seg_drop_take : ∀ (k m n : Nat) (f : Nat → Bool), k + m ≤ n → ((seg f n).drop k).take m = seg (fun i => f (k + i)) m
  | 0, m, n, f, h => by
    simp only [List.drop_zero, Nat.zero_add]
    induction m generalizing n f with
    | zero => rfl
    | succ m ih =>
      obtain ⟨n', rfl⟩ : ∃ n', n = n' + 1 := ⟨n - 1, by omega⟩
      show f 0 :: (seg (fun i => f (i + 1)) n').take m = f 0 :: seg (fun i => f (i + 1)) m
      rw [ih n' (fun i => f (i + 1)) (by omega)]
  | k + 1, m, n, f, h => by
    obtain ⟨n', rfl⟩ : ∃ n', n = n' + 1 := ⟨n - 1, by omega⟩
    show ((seg (fun i => f (i + 1)) n').drop k).take m = _
    rw [seg_drop_take k m n' (fun i => f (i + 1)) (by omega)]
    exact seg_congr _ _ _ (fun i _ => by rw [show k + i + 1 = k + 1 + i by omega])

/-- A passing check gives the trap's hypotheses at time `t1`. -/
theorem entry_spec {c0 c1 t1 : Nat} {xB : Int} (h : checkEntry c0 c1 t1 xB = true) :
    (xB + (c0 : Int)) % 7 = 2 ∧ (∀ x, x ≤ xB → G c0 c1 t1 x = etherZ c0 x (t1 + c1)) ∧
      ((t1 + c1) % 4, rowZ (G c0 c1) t1 xB 13) ∈ wallStates := by
  unfold checkEntry at h
  simp only [Bool.and_eq_true, decide_eq_true_eq] at h
  obtain ⟨⟨⟨h0, hk⟩, hall⟩, hw⟩ := h
  have hn : (xB + 13 + (t1 : Int) - -((2 * t1 : Nat) : Int) + 1).toNat = (xB + (t1 : Int) + 14).toNat + 2 * t1 := by omega
  rw [hn] at hall hw
  have hL : iter3 t1 (seg (fun i => initRow c0 c1 (-((2 * t1 : Nat) : Int) + (i : Int))) ((xB + (t1 : Int) + 14).toNat + 2 * t1))
      = seg (fun i => G c0 c1 t1 (-(t1 : Int) + (i : Int))) (xB + (t1 : Int) + 14).toNat := by
    have := iter3_G c0 c1 t1 0 (-((2 * t1 : Nat) : Int)) (xB + (t1 : Int) + 14).toNat
    rw [Nat.zero_add] at this
    rw [show (fun i : Nat => initRow c0 c1 (-((2 * t1 : Nat) : Int) + (i : Int))) =
        (fun i : Nat => G c0 c1 0 (-((2 * t1 : Nat) : Int) + (i : Int))) from rfl, this]
    exact seg_congr _ _ _ (fun i _ => by rw [show -((2 * t1 : Nat) : Int) + (t1 : Int) + (i : Int) = -(t1 : Int) + (i : Int) by omega])
  rw [hL] at hall hw
  refine ⟨hk, fun x hx => ?_, ?_⟩
  · by_cases hlt : x + (t1 : Int) < 0
    · exact G_left c0 c1 t1 x hlt
    · have hi : (x + (t1 : Int)).toNat < (xB + (t1 : Int) + 1).toNat := by omega
      have e := List.all_eq_true.1 hall _ (List.mem_range.2 hi)
      rw [beq_iff_eq, seg_getD' _ _ _ (by omega)] at e
      rw [show -(t1 : Int) + (((x + (t1 : Int)).toNat : Nat) : Int) = x by omega] at e
      exact e
  · rw [seg_drop_take _ _ _ _ (by omega)] at hw
    have e : seg (fun i => G c0 c1 t1 (-(t1 : Int) + (((xB + (t1 : Int) + 1).toNat + i : Nat) : Int))) 13 = rowZ (G c0 c1) t1 xB 13 := by
      unfold rowZ
      exact seg_congr _ _ _ (fun i _ => by rw [show -(t1 : Int) + (((xB + (t1 : Int) + 1).toNat + i : Nat) : Int) = xB + (i : Int) + 1 by omega])
    rw [e] at hw
    exact List.contains_iff_mem.1 hw

/-! ### The upper bound: a wall state is never the ether's own strip -/

/-- The ether's 13 cells right of a B3 column at phase `φ` (ether columns 3 .. 15). -/
def refStrip (φ : Nat) : List Bool := seg (fun i => ether (3 + i) φ) 13

theorem wall_ne_ref_all : wallStates.all (fun e => e.2 != refStrip e.1) = true := by decide

theorem seg_ne_witness : ∀ (n : Nat) (f g : Nat → Bool), seg f n ≠ seg g n → ∃ i, i < n ∧ f i ≠ g i := by
  intro n f g h
  apply Classical.byContradiction
  intro hc
  exact h (seg_congr n f g (fun i hi => Classical.byContradiction (fun hne => hc ⟨i, hi, hne⟩)))

/-! ### The theorem -/

/-- **From a passing check, the front is pinned for ever.** For every `t ≥ t1` the ether is intact at and left of `xB`,
and some cell among `xB + 1 .. xB + 13` differs from it. -/
theorem pinned_of_check {c0 c1 t1 : Nat} {xB : Int} (h : checkEntry c0 c1 t1 xB = true) :
    ∀ t, t1 ≤ t → (∀ x, x ≤ xB → G c0 c1 t x = etherZ c0 x (t + c1)) ∧
      ∃ x, xB < x ∧ x ≤ xB + 13 ∧ G c0 c1 t x ≠ etherZ c0 x (t + c1) := by
  obtain ⟨hk, hE, hW⟩ := entry_spec h
  have inv := trap_two_sided (G_isR30 c0 c1) (c0 : Int) xB c1 t1 hk hE hW
  intro t ht
  obtain ⟨hE', hW'⟩ := inv (t - t1)
  rw [show t1 + (t - t1) = t by omega] at hE' hW'
  refine ⟨hE', ?_⟩
  have hne : rowZ (G c0 c1) t xB 13 ≠ refStrip ((t + c1) % 4) := by
    have := List.all_eq_true.1 wall_ne_ref_all _ hW'
    simpa using this
  unfold rowZ refStrip at hne
  obtain ⟨i, hi, hfi⟩ := seg_ne_witness 13 _ _ hne
  refine ⟨xB + (i : Int) + 1, by omega, by omega, fun hc => hfi ?_⟩
  rw [hc]
  exact etherZ_eq_ether (by omega) (by omega)

set_option maxRecDepth 100000 in
theorem entry_0_0 : checkEntry 0 0 81 (-19) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_0_1 : checkEntry 0 1 13 (-5) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_0_2 : checkEntry 0 2 10 2 = true := by decide
set_option maxRecDepth 100000 in
theorem entry_0_3 : checkEntry 0 3 186 (-26) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_1_0 : checkEntry 1 0 185 (-27) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_1_1 : checkEntry 1 1 17 (-6) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_1_2 : checkEntry 1 2 9 1 = true := by decide
set_option maxRecDepth 100000 in
theorem entry_1_3 : checkEntry 1 3 9 1 = true := by decide
set_option maxRecDepth 100000 in
theorem entry_2_0 : checkEntry 2 0 8 0 = true := by decide
set_option maxRecDepth 100000 in
theorem entry_2_1 : checkEntry 2 1 17 (-7) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_2_2 : checkEntry 2 2 16 (-7) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_2_3 : checkEntry 2 3 8 0 = true := by decide
set_option maxRecDepth 100000 in
theorem entry_3_0 : checkEntry 3 0 7 (-1) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_3_1 : checkEntry 3 1 7 (-1) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_3_2 : checkEntry 3 2 16 (-8) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_3_3 : checkEntry 3 3 7 (-1) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_4_0 : checkEntry 4 0 6 (-2) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_4_1 : checkEntry 4 1 148 (-23) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_4_2 : checkEntry 4 2 6 (-2) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_4_3 : checkEntry 4 3 222 (-37) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_5_0 : checkEntry 5 0 221 (-38) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_5_1 : checkEntry 5 1 148 (-24) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_5_2 : checkEntry 5 2 5 (-3) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_5_3 : checkEntry 5 3 5 (-3) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_6_0 : checkEntry 6 0 4 (-4) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_6_1 : checkEntry 6 1 25 (-11) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_6_2 : checkEntry 6 2 4 (-4) = true := by decide
set_option maxRecDepth 100000 in
theorem entry_6_3 : checkEntry 6 3 82 (-18) = true := by decide

/-- **The classic ether absorbs a black edge: its front speed is exactly zero.** For every alignment `(c0, c1)` of the
kit's ether, the leftmost cell where the inserted edge's evolution differs from the ether stays, from a finite time on,
inside a fixed window of 13 cells: the ether at and left of `xB` is never disturbed, and the disturbance never heals. -/
theorem edge_pinned (c0 c1 : Nat) (h0 : c0 < 7) (h1 : c1 < 4) : ∃ xB : Int, ∃ t1 : Nat, ∀ t, t1 ≤ t →
    (∀ x, x ≤ xB → G c0 c1 t x = etherZ c0 x (t + c1)) ∧ ∃ x, xB < x ∧ x ≤ xB + 13 ∧ G c0 c1 t x ≠ etherZ c0 x (t + c1) :=
  match c0, c1, h0, h1 with
  | 0, 0, _, _ => ⟨(-19), 81, pinned_of_check entry_0_0⟩
  | 0, 1, _, _ => ⟨(-5), 13, pinned_of_check entry_0_1⟩
  | 0, 2, _, _ => ⟨2, 10, pinned_of_check entry_0_2⟩
  | 0, 3, _, _ => ⟨(-26), 186, pinned_of_check entry_0_3⟩
  | 1, 0, _, _ => ⟨(-27), 185, pinned_of_check entry_1_0⟩
  | 1, 1, _, _ => ⟨(-6), 17, pinned_of_check entry_1_1⟩
  | 1, 2, _, _ => ⟨1, 9, pinned_of_check entry_1_2⟩
  | 1, 3, _, _ => ⟨1, 9, pinned_of_check entry_1_3⟩
  | 2, 0, _, _ => ⟨0, 8, pinned_of_check entry_2_0⟩
  | 2, 1, _, _ => ⟨(-7), 17, pinned_of_check entry_2_1⟩
  | 2, 2, _, _ => ⟨(-7), 16, pinned_of_check entry_2_2⟩
  | 2, 3, _, _ => ⟨0, 8, pinned_of_check entry_2_3⟩
  | 3, 0, _, _ => ⟨(-1), 7, pinned_of_check entry_3_0⟩
  | 3, 1, _, _ => ⟨(-1), 7, pinned_of_check entry_3_1⟩
  | 3, 2, _, _ => ⟨(-8), 16, pinned_of_check entry_3_2⟩
  | 3, 3, _, _ => ⟨(-1), 7, pinned_of_check entry_3_3⟩
  | 4, 0, _, _ => ⟨(-2), 6, pinned_of_check entry_4_0⟩
  | 4, 1, _, _ => ⟨(-23), 148, pinned_of_check entry_4_1⟩
  | 4, 2, _, _ => ⟨(-2), 6, pinned_of_check entry_4_2⟩
  | 4, 3, _, _ => ⟨(-37), 222, pinned_of_check entry_4_3⟩
  | 5, 0, _, _ => ⟨(-38), 221, pinned_of_check entry_5_0⟩
  | 5, 1, _, _ => ⟨(-24), 148, pinned_of_check entry_5_1⟩
  | 5, 2, _, _ => ⟨(-3), 5, pinned_of_check entry_5_2⟩
  | 5, 3, _, _ => ⟨(-3), 5, pinned_of_check entry_5_3⟩
  | 6, 0, _, _ => ⟨(-4), 4, pinned_of_check entry_6_0⟩
  | 6, 1, _, _ => ⟨(-11), 25, pinned_of_check entry_6_1⟩
  | 6, 2, _, _ => ⟨(-4), 4, pinned_of_check entry_6_2⟩
  | 6, 3, _, _ => ⟨(-18), 82, pinned_of_check entry_6_3⟩
  | c0 + 7, _, h, _ => absurd h (by omega)
  | _, c1 + 4, _, h => absurd h (by omega)

end Rule30Submission
