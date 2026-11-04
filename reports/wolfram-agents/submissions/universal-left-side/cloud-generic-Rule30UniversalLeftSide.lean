module

public import Ruliology.CellularAutomata.Rule30LeftCoincidence
public import Ruliology.CellularAutomata.Rule30AgedLeftDiagonals

/-!
# One left side: every configuration with a leftmost black cell carries the universal strip below the first even fork

Rowland (*Local nested structure in rule 30*, 2006, §5) conjectured that rule 30 has "really only one left side": from
any row with a leftmost black cell, the eventual period of each left diagonal is independent of the row. He gave the
inductive argument in prose (unless the nearer parent diagonal is eventually white, the child is forced by its two parents;
at a white nearer parent with an odd number of blacks per period in the farther parent, the two continuations are
complements) and located the first possible failure at his column 53,209 (wheel 53,208 here), where the nearer parent is
eventually white and the farther parent has an even number of blacks per period. This module proves the induction in the
kit's reset framework, for every array obeying the left-diagonal recurrence with a black edge, hence for every
configuration with a leftmost black cell, with one common time shift.

Wall frame: `Ld x lo j t = evol x t (lo - t + j)` (`Rule30FiniteDiagonals`) is the `j`-th left diagonal of the configuration
`x` whose leftmost black cell is at `lo`; the family obeys `Rule30AgedLeftDiagonals.Recurrence`: wheel `0` keeps its value,
wheel `1` is the OR of wheels `0` and `1`, and wheel `j + 2` is reset by its nearer word `j + 1` and driven by its farther word
`j`: `a (j + 2) (t + 1) = a j t ⊕ (a (j + 1) t ∨ a (j + 2) t)`.

A **strip** `C : Nat → Nat → Bool` (wheel, time) is admissible through `J` when `C 0 = C 1 = 1`, each `C (j + 2)` obeys the
recurrence driven by `C j` and `C (j + 1)`, and at each wheel `m + 1 ≤ J` either the nearer word `C m` has blacks arbitrarily
late or there is an `L` that is a period of every word through `m` and an antiperiod of `C (m + 1)`. Rowland's condition, a
white nearer word with odd parity of the farther word over `L`, gives the antiperiod (`antiperiod_of_odd_parity`, from the
kit's `white_shift`). The universal strip of the single black cell is admissible through `53207`: its white words are wheels
2, 7, 28, 399 with farther weights 1, 1, 3, 3 over the common periods 1, 2, 4, 8, and the first even case is wheel 53,207 with
weight 6 over period 16, the fork at 53,208. That is a finite check of the data, in a companion certificate.

* `universal_of_strip`: for every array `a` with the recurrence and `a 0 0 = true`, and every strip admissible through `J`,
  there is one shift `s` with `a j (t + s) = C j t` for all `j ≤ J` and all large `t`. The induction: at a nearer word with
  blacks arbitrarily late, the row's child and the strip's word are two solutions of one recurrence with the same parents
  and agree from the first black on (`Rule30LeftCoincidence.solutions_agree`); otherwise the nearer word is eventually white,
  both children integrate the farther word, their difference is constant, and if it is `1` the antiperiod turns the
  complement into the word shifted by `L`, which the `L`-periodic lower strip does not see.
* `one_left_side`: the same for the left diagonals `Ld x lo` of every configuration white left of `lo` with `x lo = true`.
* `same_left_side`: any two such configurations have the same left side through `J`, up to a time shift.
* `seed_left_side`: the single black cell's diagonals `D j` are eventually the strip's words: the seed is one such array, so
  the theorem certifies its own strip without evolving it.

Nothing here concerns the center column or the Prize problems; beyond the first even fork the strip branches (Rowland's
further columns 58,288 and 72,577), and that is outside the statement. Proposed in the contributors' record by Claude
(Anthropic) after Rowland's argument, with the interface fixed by Claude (Anthropic, Local); the reset lemmas are the kit's
and `Rule30LeftCoincidence`'s.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30UniversalLeftSide

set_option autoImplicit false

open Rule30Jen Rule30Realization Rule30Diagonals Rule30LeftReset Rule30LeftCoincidence Rule30FiniteDiagonals Rule30AgedLeftDiagonals

/-- Wheel `0` of a recurrence array with a black start is black at every time. -/
theorem zero_eq {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) : ∀ t, a 0 t = true
  | 0 => ha0
  | t + 1 => by rw [ha.1 t, zero_eq ha ha0 t]

/-- Wheel `1` is black from time `1` on. -/
theorem one_eq {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) (t : Nat) : a 1 (t + 1) = true := by
  rw [ha.2.1 t, zero_eq ha ha0 t]
  rfl

/-- A white nearer word with odd parity of the farther word over `L` makes the child `L`-antiperiodic (Rowland's
doubling condition, through the kit's `white_shift`). -/
theorem antiperiod_of_odd_parity {x a b : Nat → Bool} {L : Nat}
    (hx : ∀ t, x (t + 1) = xor (a t) (b t || x t)) (hb : ∀ t, b t = false) (hpar : ∀ t, par a t L = true) :
    ∀ t, x (t + L) = !x t := by
  intro t
  have h := white_shift (s := 0) (L := L) hx (fun u _ => hb u) t (Nat.zero_le t)
  rw [hpar t] at h
  rw [h]
  cases x t <;> rfl

/-- The induction: wheels `0 … n` of the array are the strip's words at one common shift, from one time on. -/
theorem aligned {a C : Nat → Nat → Bool} {J : Nat} (ha : Recurrence a) (ha0 : a 0 0 = true)
    (h0 : ∀ t, C 0 t = true) (h1 : ∀ t, C 1 t = true)
    (hC : ∀ j t, j + 2 ≤ J → C (j + 2) (t + 1) = xor (C j t) (C (j + 1) t || C (j + 2) t))
    (hstep : ∀ m, m + 1 ≤ J → (∀ T, ∃ t, T ≤ t ∧ C m t = true) ∨
      ∃ L, (∀ j, j ≤ m → ∀ t, C j (t + L) = C j t) ∧ ∀ t, C (m + 1) (t + L) = !C (m + 1) t) :
    ∀ n, n ≤ J → ∃ s T, ∀ j, j ≤ n → ∀ t, T ≤ t → a j (t + s) = C j t
  | 0, _ => ⟨0, 0, fun j hj t _ => by
      have hj0 : j = 0 := by omega
      subst hj0
      rw [zero_eq ha ha0, h0]⟩
  | 1, _ => ⟨0, 1, fun j hj t ht => by
      rcases Nat.lt_or_ge j 1 with hlt | hge
      · have hj0 : j = 0 := by omega
        subst hj0
        rw [zero_eq ha ha0, h0]
      · have hj1 : j = 1 := by omega
        subst hj1
        obtain ⟨u, rfl⟩ : ∃ u, t = u + 1 := ⟨t - 1, by omega⟩
        rw [one_eq ha ha0 u, h1]⟩
  | n + 2, hn => by
    obtain ⟨s, T, ih⟩ := aligned ha ha0 h0 h1 hC hstep (n + 1) (by omega)
    -- the array's child, shifted, from `T` on: the same recurrence as the strip's word, with the strip's parents
    have hy : ∀ t, T ≤ t → a (n + 2) (t + 1 + s) = xor (C n t) (C (n + 1) t || a (n + 2) (t + s)) := by
      intro t ht
      rw [show t + 1 + s = (t + s) + 1 by omega, ha.2.2 n (t + s), ih n (by omega) t ht, ih (n + 1) (by omega) t ht]
    have hz : ∀ t, C (n + 2) (t + 1) = xor (C n t) (C (n + 1) t || C (n + 2) t) := fun t => hC n t hn
    by_cases hb : ∀ T', ∃ t, T' ≤ t ∧ C (n + 1) t = true
    · -- a black of the nearer word at or after `T`: both children are forced from there
      obtain ⟨t0, ht0, hblack⟩ := hb T
      have hy' : ∀ u, a (n + 2) (T + (u + 1) + s) =
          xor (C n (T + u)) (C (n + 1) (T + u) || a (n + 2) (T + u + s)) := by
        intro u
        rw [show T + (u + 1) + s = T + u + 1 + s by omega]
        exact hy (T + u) (by omega)
      have hz' : ∀ u, C (n + 2) (T + (u + 1)) = xor (C n (T + u)) (C (n + 1) (T + u) || C (n + 2) (T + u)) := by
        intro u
        rw [show T + (u + 1) = T + u + 1 by omega]
        exact hz (T + u)
      have hs0 : C (n + 1) (T + (t0 - T)) = true := by
        rw [show T + (t0 - T) = t0 by omega]
        exact hblack
      have agree := solutions_agree (x := fun u => a (n + 2) (T + u + s)) (a := fun u => C n (T + u))
        (b := fun u => C (n + 1) (T + u)) (x' := fun u => C (n + 2) (T + u)) hy' hz' (s0 := t0 - T) hs0
      refine ⟨s, t0 + 1, fun j hj t ht => ?_⟩
      rcases Nat.lt_or_ge j (n + 2) with hlt | hge
      · exact ih j (by omega) t (by omega)
      · have hj2 : j = n + 2 := by omega
        subst hj2
        have h : a (n + 2) (T + (t - T) + s) = C (n + 2) (T + (t - T)) := agree (t - T) (by omega)
        rw [show T + (t - T) = t by omega] at h
        exact h
    · -- the nearer word is eventually white: both children integrate the farther word
      have hwhite : ∃ T1, ∀ t, T1 ≤ t → C (n + 1) t = false := by
        apply Classical.byContradiction
        intro hcon
        apply hb
        intro T'
        apply Classical.byContradiction
        intro hno
        apply hcon
        refine ⟨T', fun t ht => ?_⟩
        apply Classical.byContradiction
        intro hne
        apply hno
        refine ⟨t, ht, ?_⟩
        cases hc : C (n + 1) t
        · exact absurd hc hne
        · rfl
      obtain ⟨T1, hT1⟩ := hwhite
      obtain ⟨L, hL, hanti⟩ : ∃ L, (∀ j, j ≤ n + 1 → ∀ t, C j (t + L) = C j t) ∧
          ∀ t, C (n + 2) (t + L) = !C (n + 2) t := by
        rcases hstep (n + 1) hn with hlate | hdata
        · exact absurd hlate hb
        · exact hdata
      -- from `T2 = T + T1` on, both children are integrators of `C n`
      have hyB : ∀ t, T + T1 ≤ t → a (n + 2) (t + 1 + s) = xor (C n t) (a (n + 2) (t + s)) := by
        intro t ht
        rw [hy t (by omega), hT1 t (by omega)]
        rfl
      have hzB : ∀ t, T + T1 ≤ t → C (n + 2) (t + 1) = xor (C n t) (C (n + 2) t) := by
        intro t ht
        rw [hz t, hT1 t (by omega)]
        rfl
      have hdiff : ∀ t, T + T1 ≤ t → xor (a (n + 2) (t + s)) (C (n + 2) t) =
          xor (a (n + 2) (T + T1 + s)) (C (n + 2) (T + T1)) := by
        intro t ht
        induction t with
        | zero =>
          have hT : T + T1 = 0 := by omega
          rw [hT]
        | succ t iht =>
          rcases Nat.lt_or_ge t (T + T1) with hlt | hge
          · have hT : T + T1 = t + 1 := by omega
            rw [hT]
          · rw [hyB t hge, hzB t hge, ← iht hge]
            cases C n t <;> cases a (n + 2) (t + s) <;> cases C (n + 2) t <;> rfl
      by_cases h0' : a (n + 2) (T + T1 + s) = C (n + 2) (T + T1)
      · -- the same solution: the shift stays
        refine ⟨s, T + T1, fun j hj t ht => ?_⟩
        rcases Nat.lt_or_ge j (n + 2) with hlt | hge
        · exact ih j (by omega) t (by omega)
        · have hj2 : j = n + 2 := by omega
          subst hj2
          have h := hdiff t ht
          rw [h0'] at h
          revert h
          cases a (n + 2) (t + s) <;> cases C (n + 2) t <;> cases C (n + 2) (T + T1) <;> decide
      · -- the complement: the antiperiod makes it the word shifted by `L`
        have hneg : ∀ t, T + T1 ≤ t → a (n + 2) (t + s) = !C (n + 2) t := by
          intro t ht
          have h := hdiff t ht
          revert h h0'
          cases a (n + 2) (T + T1 + s) <;> cases C (n + 2) (T + T1) <;> cases a (n + 2) (t + s) <;>
            cases C (n + 2) t <;> decide
        refine ⟨s + L, T + T1, fun j hj t ht => ?_⟩
        rcases Nat.lt_or_ge j (n + 2) with hlt | hge
        · rw [show t + (s + L) = (t + L) + s by omega, ih j (by omega) (t + L) (by omega), hL j (by omega) t]
        · have hj2 : j = n + 2 := by omega
          subst hj2
          rw [show t + (s + L) = (t + L) + s by omega, hneg (t + L) (by omega), hanti t]
          cases C (n + 2) t <;> rfl

/-- **One left side, for every array with the recurrence and a black edge.** For every strip admissible through `J`, one
shift aligns every wheel through `J` with the strip, each from some time on. -/
theorem universal_of_strip {a C : Nat → Nat → Bool} {J : Nat} (ha : Recurrence a) (ha0 : a 0 0 = true)
    (h0 : ∀ t, C 0 t = true) (h1 : ∀ t, C 1 t = true)
    (hC : ∀ j t, j + 2 ≤ J → C (j + 2) (t + 1) = xor (C j t) (C (j + 1) t || C (j + 2) t))
    (hstep : ∀ m, m + 1 ≤ J → (∀ T, ∃ t, T ≤ t ∧ C m t = true) ∨
      ∃ L, (∀ j, j ≤ m → ∀ t, C j (t + L) = C j t) ∧ ∀ t, C (m + 1) (t + L) = !C (m + 1) t) :
    ∃ s, ∀ j, j ≤ J → ∃ T, ∀ t, T ≤ t → a j (t + s) = C j t := by
  obtain ⟨s, T, h⟩ := aligned ha ha0 h0 h1 hC hstep J (Nat.le_refl J)
  exact ⟨s, fun j hj => ⟨T, h j hj⟩⟩

/-- **One left side, for every configuration with a leftmost black cell.** -/
theorem one_left_side {C : Nat → Nat → Bool} {J : Nat}
    {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false) (hlo : x lo = true)
    (h0 : ∀ t, C 0 t = true) (h1 : ∀ t, C 1 t = true)
    (hC : ∀ j t, j + 2 ≤ J → C (j + 2) (t + 1) = xor (C j t) (C (j + 1) t || C (j + 2) t))
    (hstep : ∀ m, m + 1 ≤ J → (∀ T, ∃ t, T ≤ t ∧ C m t = true) ∨
      ∃ L, (∀ j, j ≤ m → ∀ t, C j (t + L) = C j t) ∧ ∀ t, C (m + 1) (t + L) = !C (m + 1) t) :
    ∃ s, ∀ j, j ≤ J → ∃ T, ∀ t, T ≤ t → Ld x lo j (t + s) = C j t := by
  have ha0 : Ld x lo 0 0 = true := by
    show evol x 0 (lo - ((0 : Nat) : Int) + ((0 : Nat) : Int)) = true
    rw [show lo - ((0 : Nat) : Int) + ((0 : Nat) : Int) = lo by omega]
    exact hlo
  exact universal_of_strip (Ld_recurrence hleft) ha0 h0 h1 hC hstep

/-- Any two configurations with a leftmost black cell have the same left side through `J`, up to a time shift. -/
theorem same_left_side {C : Nat → Nat → Bool} {J : Nat}
    {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false) (hlo : x lo = true)
    {y : Int → Bool} {lo' : Int} (hleft' : ∀ p, p < lo' → y p = false) (hlo' : y lo' = true)
    (h0 : ∀ t, C 0 t = true) (h1 : ∀ t, C 1 t = true)
    (hC : ∀ j t, j + 2 ≤ J → C (j + 2) (t + 1) = xor (C j t) (C (j + 1) t || C (j + 2) t))
    (hstep : ∀ m, m + 1 ≤ J → (∀ T, ∃ t, T ≤ t ∧ C m t = true) ∨
      ∃ L, (∀ j, j ≤ m → ∀ t, C j (t + L) = C j t) ∧ ∀ t, C (m + 1) (t + L) = !C (m + 1) t) :
    ∃ s s', ∀ j, j ≤ J → ∃ T, ∀ t, T ≤ t → Ld x lo j (t + s) = Ld y lo' j (t + s') := by
  obtain ⟨s, h⟩ := one_left_side hleft hlo h0 h1 hC hstep
  obtain ⟨s', h'⟩ := one_left_side hleft' hlo' h0 h1 hC hstep
  refine ⟨s, s', fun j hj => ?_⟩
  obtain ⟨T, hT⟩ := h j hj
  obtain ⟨T', hT'⟩ := h' j hj
  exact ⟨T + T', fun t ht => by rw [hT t (by omega), hT' t (by omega)]⟩

/-- The single black cell's diagonals obey the recurrence with a black edge. -/
theorem D_recurrence : Recurrence D :=
  ⟨fun t => by rw [D_zero, D_zero],
    fun t => by rw [D_one, D_zero]; rfl,
    fun i t => D_step i t⟩

/-- The single black cell's left diagonals are eventually the strip's words: the seed is one such array, so the theorem
certifies its own strip without evolving it. -/
theorem seed_left_side {C : Nat → Nat → Bool} {J : Nat}
    (h0 : ∀ t, C 0 t = true) (h1 : ∀ t, C 1 t = true)
    (hC : ∀ j t, j + 2 ≤ J → C (j + 2) (t + 1) = xor (C j t) (C (j + 1) t || C (j + 2) t))
    (hstep : ∀ m, m + 1 ≤ J → (∀ T, ∃ t, T ≤ t ∧ C m t = true) ∨
      ∃ L, (∀ j, j ≤ m → ∀ t, C j (t + L) = C j t) ∧ ∀ t, C (m + 1) (t + L) = !C (m + 1) t) :
    ∃ s, ∀ j, j ≤ J → ∃ T, ∀ t, T ≤ t → D j (t + s) = C j t :=
  universal_of_strip D_recurrence (D_zero 0) h0 h1 hC hstep

end Ruliology.CellularAutomata.Rule30UniversalLeftSide
