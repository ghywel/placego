module
public import Ruliology.CellularAutomata.Rule30Ether

/-!
Local, 2026-11-02 (L1320): the carrying read of Cloud's CL681 corollary, kernel-checked against the prize kit at main c42f6e5.

The kit's `trap_invariant` (Lowry, PR65) prescribes column `0` as an ether column for all time. CL681 needs the two-sided form:
on a rule-30 evolution of the whole line, if at time `t1` every column `x ≤ xB` carries the ether, column `xB` is a B3, and
the 13 cells right of `xB` form one of the 109 wall states, then this stays true for ever. Nothing is assumed about the cells
right of the strip. The proof is the kit's induction with the prescribed column replaced by the induction hypothesis on the
columns left of `xB`; it uses only the kit's `ether_rule`, `ether_congr` and `wall_facts` (the kernel fact `wallOK_true`).

Build: copy the kit's `lean/` package at the recorded commit, `lake build Ruliology.CellularAutomata.Rule30Ether`, then
`lake env lean EtherTwoSided.lean`.
-/
@[expose] public section
namespace Ruliology.CellularAutomata.EtherTwoSided
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

end Ruliology.CellularAutomata.EtherTwoSided
