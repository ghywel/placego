import Ruliology.CellularAutomata.Rule30Prize
/-!
# The alternating 90/150 hybrid with a white wall: the immortal rows

A row is `x : Nat → Bool`, with `x k` the cell at depth `k ≥ 1`; depth `0` is a white wall. The
hybrid `H` applies rule 150 (left, centre, right) at odd depths and rule 90 (left, right) at even
depths, with the wall white: over GF(2), `H x k = x (k + 1) + [k ≥ 2] x (k - 1) + [k odd] x k`
for `k ≥ 1` and `H x 0 = 0`. The column is `col x t = (H^t x) 1`. A row is immortal (`Immortal`)
when `col x (2 s)` is black for every `s`, and has width at most `W` (`WidthLE W x`) when
`x k = 0` for every `k > W`.

## Main results

* `immortal_iff_famRow`: a finite row with a white wall is immortal iff
  `x = e_1 + e_2 + Σ_{j ≥ 1} p_j (e_{4j-2} + e_{4j-1} + e_{4j+1} + e_{4j+2}) + Σ_{j ≥ 1} r_j e_{4j}`
  (the row `famRow p r` with `p 0 = 1`, `r 0 = 0`). `immortal_iff_bitFam` says the same cell by
  cell: `x 1 = 1`, and `x (4 j + 3) = x (4 j + 5)` and `x (4 j + 2) = x (4 j + 1) + x (4 j + 3)`
  for every `j`. `immortal_iff_bitFam_anyWall` drops the hypothesis on the wall cell, which `H`
  never reads.
* `immortal_real_iff`: the same in coefficients. Write the row as `X = Σ_j c_j A^j` with
  `A = S + S⁻¹` (the row `real n c`). Then `X` is immortal iff `X = (A + A^2) p(A^4) + r(A^4)`
  with `p(0) = 1` and `r(0) = 0` (`AFam c`). Every finite row has such coefficients
  (`real_surj`), and they are unique (`real_inj`).
* `immortal_width_six`: among the rows `rowOf n`, `n < 64` (depth `d` at bit `d - 1`: the rows of
  width at most `6` with a white wall), the immortal ones are `3, 11, 53, 61`; see also
  `immortal_three`, `immortal_eleven`, `immortal_fifty_three`, `immortal_sixty_one`.
  `not_immortal_width_one`: no row of width at most `1` is immortal, whatever its wall cell.
* `immortal_iff_param`, `paramRow_inj`, `paramRow_width`: for `W ≥ 2` the immortal rows of width
  at most `W` with a white wall are in bijection, through `paramRow`, with the Boolean sequences
  supported below `W / 2 - 1`, so there are `2 ^ (W / 2 - 1)` of them (the last step, counting
  those sequences, is not formalised). `immortal_count_le_twelve` checks the number itself for
  `2 ≤ W ≤ 12` by kernel evaluation over the rows `rowOf n`, `n < 2 ^ W` (through
  `immortalB_iff`).
* `col_not_eventually_periodic`: the column of a nonzero finite row with a white wall is not
  eventually periodic. `immortal_odd_word_not_eventually_periodic`: for an immortal finite row
  the odd-time column word is not eventually periodic.

## The proof

*The pair model.* Write a coefficient sequence as `X = A a(T) + b(T)` with `T = A^2` (`split`:
`a = decO c`, `b = decE c`). The hybrid acts as `P (a, b) = (a + b, T a)`; the depth-one cell is
`psi a`, where `psi q = q 0 + psi q_o` (`psi`, with fuel; `psi_mono`: on the monomial `T^m` it is
`1` exactly when `m + 1` is a power of `2`); and the decimation `D (a, b) = (a_o, a_e + b_o)`
satisfies `D (P (P x)) = P (D x)` (`D_P_P`). Hence (`psi_even_time`, `even_time_constant`) the
observation at time `2 s` is `fst (P^(2 s) x) 0` plus the observation of `D x` at time `s`; the
constant is `a 0` at `s = 0` and `a 0 + b 0` afterwards.

*The bridge.* In mirror coordinates index `k ≥ 1` holds the coefficient of `S^k + S^(-k)` and
index `0` the wall cell `S^0`. Multiplication by `A` is rule 90 with the wall cell read at depth
`1` (`M`). The extended hybrid is `HE = M + odd part`, and it agrees with `H` on rows with a white
wall (`HE_of_wall`). The realisation `real n c` is Horner's rule with `M`. It carries `HE` to
`L X = A X + X_odd` (`HE_real`, `iter_H_real`), and `L` is `P` after `split` (`split_Lc`).
Squaring commutes with it (`real_spread`: `A ↦ A^2` on coefficients is `S ↦ S^2` on rows), which
identifies the depth-one cell with `psi` of the odd part (`real_one`) and gives `col_real` and the
renormalisation `colE_even`.

*Injectivity.* The black cell nearest the wall reaches the column one depth per tick (`front`),
so a row whose column is white is white (`col_inj`). For an extended row `y` with a white extended
column, `HE y` has a white wall and a white column, so `HE y = 0`, and a finite row is recovered
from `HE y` from the top down (`colE_inj`).

*Classification.* With `c 0 = 0` the even column is `c 1` plus the extended column of `D X`. If
`c 1 = 1`, `D X` has a white column, so `D X = 0`, which is the family. If `c 1 = 0`, `D X` has an
all-black column, so `HE (D X) + D X` has a white column, `HE (D X) = D X`, and a finite fixed row
is white: a contradiction. Conversely the family has `D X = 0`.

*From coefficients to bits.* Squaring twice computes the realisation of the coefficient family:
`real (4 n + 2) (afam p r) = famRow (real n p) (real n r)` (`real_afam`). So the bit family is the
image of the coefficient family under `p ↦ real n p`, `r ↦ real n r`, a bijection of finite
sequences that keeps the value at `0`. The two families agree as sets but not term by term: the
row `e_{4j}` is `D_{4j}(A) = D_j(A^4)`, with `D_k` the Dickson polynomials, and this equals
`A^{4j}` only when `j` is a power of `2`; for example `A^12` is the row `e_4 + e_12`
(`real_A_pow_twelve`).

*Aperiodicity.* If the column repeats with period `q ≥ 1` from time `U`, the rows `H^U x` and
`H^(U + q) x` have equal columns, hence are equal (`col_inj`). The top cell of a finite row moves
away from the wall one depth per tick (`iter_H_top`), so `H^U x = 0` (`H_periodic_white`) and then
`x = 0` (`iter_H_kernel`). For an immortal row a periodic odd-time word makes the whole column
periodic, since every even time is black.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

/-! ## Rows, iteration and the hybrid -/

/-- A row of cells, or a coefficient sequence: a map from `Nat` to `Bool`. -/
abbrev Row := Nat → Bool

/-- The `n`-fold iterate of `f`, applying `f` first. -/
def iter {α : Type} (f : α → α) : Nat → α → α
  | 0, x => x
  | n + 1, x => iter f n (f x)

theorem iter_add {α : Type} (f : α → α) (a b : Nat) (x : α) :
    iter f (a + b) x = iter f b (iter f a x) := by
  induction a generalizing x with
  | zero => rw [Nat.zero_add]; rfl
  | succ a ih => rw [Nat.succ_add]; exact ih (f x)

/-- Cellwise exclusive or. -/
def xorS (u v : Row) : Row := fun j => xor (u j) (v j)

/-- The all-white row. -/
def blank : Row := fun _ => false

/-- `x` vanishes from index `n` on. -/
def Supp (n : Nat) (x : Row) : Prop := ∀ j, n ≤ j → x j = false

/-- A finite row of width at most `W`: every cell deeper than `W` is white. -/
def WidthLE (W : Nat) (x : Row) : Prop := ∀ k, W < k → x k = false

/-- The odd-index part. -/
def oddR (x : Row) : Row := fun k => if k % 2 = 1 then x k else false

/-- The even-index part. -/
def evenR (x : Row) : Row := fun k => if k % 2 = 1 then false else x k

/-- Shift down by one index. -/
def down (c : Row) : Row := fun j => c (j + 1)

/-- The alternating hybrid with a white wall at depth `0`: rule 150 at odd depths, rule 90 at
even depths. -/
def H (x : Row) (k : Nat) : Bool :=
  if k = 0 then false
  else xor (x (k + 1)) (xor (if 2 ≤ k then x (k - 1) else false) (if k % 2 = 1 then x k else false))

/-- The depth-one column. -/
def col (x : Row) (t : Nat) : Bool := iter H t x 1

/-- All even-time observations of the depth-one cell are black. -/
def Immortal (x : Row) : Prop := ∀ s, col x (2 * s) = true

/-! ## Boolean helpers -/

theorem xor_cancel_left (a b : Bool) : xor a (xor a b) = b := by cases a <;> cases b <;> rfl

theorem eq_of_xor_false {a b : Bool} (h : xor a b = false) : a = b := by
  cases a <;> cases b <;> first | rfl | exact absurd h (by decide)

theorem eq_false_of_true_xor {b : Bool} (h : xor true b = true) : b = false := by
  cases b <;> first | rfl | exact absurd h (by decide)

theorem eq_true_of_false_xor {b : Bool} (h : xor false b = true) : b = true := by
  cases b <;> first | rfl | exact absurd h (by decide)

theorem oddR_of_false {x : Row} {k : Nat} (h : x k = false) : oddR x k = false := by
  show (if k % 2 = 1 then x k else false) = false
  rw [h]; split <;> rfl

theorem oddR_odd (x : Row) (m : Nat) : oddR x (2 * m + 1) = x (2 * m + 1) :=
  ite_eq_left (show (2 * m + 1) % 2 = 1 by omega)

theorem oddR_even (x : Row) (m : Nat) : oddR x (2 * m) = false :=
  ite_eq_right (show ¬ (2 * m) % 2 = 1 by omega)

theorem oddR_one (x : Row) : oddR x 1 = x 1 := rfl

theorem supp_mono {n m : Nat} {x : Row} (hx : Supp n x) (h : n ≤ m) : Supp m x :=
  fun j hj => hx j (by omega)

theorem supp_xor {n : Nat} {u v : Row} (hu : Supp n u) (hv : Supp n v) : Supp n (xorS u v) := by
  intro j hj
  show xor (u j) (v j) = false
  rw [hu j hj, hv j hj]; rfl

theorem supp_oddR {n : Nat} {c : Row} (hc : Supp n c) : Supp n (oddR c) :=
  fun j hj => oddR_of_false (hc j hj)

/-! ## The hybrid at a wall -/

theorem H_wall (x : Row) : H x 0 = false := rfl

theorem H_one (x : Row) : H x 1 = xor (x 2) (x 1) := by
  show xor (x 2) (xor false (x 1)) = _
  rw [Bool.false_xor]

theorem H_add_two (x : Row) (k : Nat) :
    H x (k + 2) = xor (x (k + 3)) (xor (x (k + 1)) (oddR x (k + 2))) := by
  unfold H
  rw [ite_eq_right (show ¬ (k + 2 = 0) by omega), ite_eq_left (show 2 ≤ k + 2 by omega)]
  rfl

/-- Rule 90 on the symmetric line, in mirror coordinates: multiplication by `A = S + S⁻¹`, with
the wall cell (the coefficient of `S^0`) at index `0`. -/
def M (x : Row) : Nat → Bool
  | 0 => false
  | k + 1 => xor (x k) (x (k + 2))

/-- The extended hybrid: the same rule, with the wall cell `x 0` read at depth `1`. -/
def HE (x : Row) : Nat → Bool
  | 0 => false
  | k + 1 => xor (x k) (xor (x (k + 2)) (oddR x (k + 1)))

theorem HE_eq (x : Row) : HE x = xorS (M x) (oddR x) := by
  funext k
  cases k with
  | zero => rfl
  | succ k =>
    show xor (x k) (xor (x (k + 2)) (oddR x (k + 1))) = xor (xor (x k) (x (k + 2))) (oddR x (k + 1))
    rw [Bool.xor_assoc]

theorem HE_of_wall {x : Row} (hx : x 0 = false) : HE x = H x := by
  funext k
  match k with
  | 0 => rfl
  | 1 =>
    show xor (x 0) (xor (x 2) (oddR x 1)) = H x 1
    rw [H_one, hx, Bool.false_xor, oddR_one]
  | k + 2 =>
    show xor (x (k + 1)) (xor (x (k + 3)) (oddR x (k + 2))) = H x (k + 2)
    rw [H_add_two, Bool.xor_left_comm]

theorem iter_HE_of_wall {x : Row} (hx : x 0 = false) (t : Nat) : iter HE t x = iter H t x := by
  induction t generalizing x with
  | zero => rfl
  | succ t ih =>
    show iter HE t (HE x) = iter H t (H x)
    rw [HE_of_wall hx]
    exact ih (H_wall x)

/-! ## The pair model -/

/-- Multiplication by the variable: `T q 0 = false`, `T q (m + 1) = q m`. -/
def T (q : Row) : Nat → Bool
  | 0 => false
  | m + 1 => q m

/-- Odd decimation: `decO q m = q (2 m + 1)`. -/
def decO (q : Row) : Row := fun m => q (2 * m + 1)

/-- Even decimation: `decE q m = q (2 m)`. -/
def decE (q : Row) : Row := fun m => q (2 * m)

/-- The hybrid on pairs: `P (a, b) = (a + b, T a)`. -/
def P (x : Row × Row) : Row × Row := (xorS x.1 x.2, T x.1)

/-- The decimation `D (a, b) = (a_o, a_e + b_o)`. -/
def D (x : Row × Row) : Row × Row := (decO x.1, xorS (decE x.1) (decO x.2))

/-- The depth-one observation with fuel `n`: `psi (n + 1) q = q 0 + psi n q_o`. -/
def psi : Nat → Row → Bool
  | 0, _ => false
  | n + 1, q => xor (q 0) (psi n (decO q))

theorem D_P_P (x : Row × Row) : D (P (P x)) = P (D x) := by
  obtain ⟨a, b⟩ := x
  have h1 : decO (xorS (xorS a b) (T a)) = xorS (decO a) (xorS (decE a) (decO b)) := by
    funext m
    show xor (xor (a (2 * m + 1)) (b (2 * m + 1))) (a (2 * m)) =
      xor (a (2 * m + 1)) (xor (a (2 * m)) (b (2 * m + 1)))
    simp only [Bool.xor_left_comm, Bool.xor_comm]
  have h2 : xorS (decE (xorS (xorS a b) (T a))) (decO (T (xorS a b))) = T (decO a) := by
    funext m
    have hT : T a (2 * m) = T (decO a) m := by cases m <;> rfl
    show xor (xor (xor (a (2 * m)) (b (2 * m))) (T a (2 * m))) (xor (a (2 * m)) (b (2 * m))) =
      T (decO a) m
    rw [hT]
    simp only [Bool.xor_assoc, Bool.xor_left_comm, Bool.xor_comm, xor_cancel_left]
  show (decO (xorS (xorS a b) (T a)), xorS (decE (xorS (xorS a b) (T a))) (decO (T (xorS a b)))) =
    (xorS (decO a) (xorS (decE a) (decO b)), T (decO a))
  rw [h1, h2]

theorem D_iter_P (s : Nat) (x : Row × Row) : D (iter P (2 * s) x) = iter P s (D x) := by
  induction s generalizing x with
  | zero => rfl
  | succ s ih =>
    show D (iter P (2 * s) (P (P x))) = iter P s (P (D x))
    rw [ih, D_P_P]

theorem iter_P_succ_fst_zero (t : Nat) (x : Row × Row) :
    (iter P (t + 1) x).1 0 = xor (x.1 0) (x.2 0) := by
  induction t generalizing x with
  | zero => rfl
  | succ t ih =>
    show (iter P (t + 1) (P x)).1 0 = _
    rw [ih]
    show xor (xor (x.1 0) (x.2 0)) false = _
    rw [Bool.xor_false]

theorem psi_even_time (k s : Nat) (x : Row × Row) :
    psi (k + 1) (iter P (2 * s) x).1 =
      xor ((iter P (2 * s) x).1 0) (psi k (iter P s (D x)).1) := by
  show xor _ (psi k (D (iter P (2 * s) x)).1) = _
  rw [D_iter_P]

theorem even_time_constant (s : Nat) (x : Row × Row) :
    (iter P (2 * s) x).1 0 = if s = 0 then x.1 0 else xor (x.1 0) (x.2 0) := by
  cases s with
  | zero => rfl
  | succ s =>
    rw [ite_eq_right (show ¬ s + 1 = 0 by omega), show 2 * (s + 1) = 2 * s + 1 + 1 by omega,
      iter_P_succ_fst_zero]

theorem psi_of_zero {q : Row} (hq : ∀ j, q j = false) (n : Nat) : psi n q = false := by
  induction n generalizing q with
  | zero => rfl
  | succ n ih =>
    show xor (q 0) (psi n (decO q)) = false
    rw [hq 0, ih (q := decO q) (fun j => hq (2 * j + 1))]
    rfl

theorem psi_fuel (m : Nat) : ∀ q : Row, Supp m q → ∀ k, m ≤ k → psi k q = psi m q := by
  induction m with
  | zero =>
    intro q hq k _
    rw [psi_of_zero (fun j => hq j (Nat.zero_le j)) k]
    rfl
  | succ m ih =>
    intro q hq k hk
    obtain ⟨k, rfl⟩ : ∃ k', k = k' + 1 := ⟨k - 1, by omega⟩
    show xor (q 0) (psi k (decO q)) = xor (q 0) (psi m (decO q))
    rw [ih (decO q) (fun j hj => hq _ (by omega)) k (by omega)]

/-- The monomial `T^m`. -/
def mono (m : Nat) : Row := fun j => decide (j = m)

theorem psi_mono (n m : Nat) : psi n (mono m) = true ↔ ∃ r, r < n ∧ m + 1 = 2 ^ r := by
  induction n generalizing m with
  | zero =>
    constructor
    · intro h; cases h
    · rintro ⟨r, hr, _⟩; exact absurd hr (by omega)
  | succ n ih =>
    show xor (mono m 0) (psi n (decO (mono m))) = true ↔ _
    rcases Nat.lt_or_ge m 1 with hm | hm
    · obtain rfl : m = 0 := by omega
      rw [psi_of_zero (q := decO (mono 0)) (fun j => decide_eq_false (by omega)) n]
      exact ⟨fun _ => ⟨0, by omega, rfl⟩, fun _ => rfl⟩
    · have hm0 : mono m 0 = false := decide_eq_false (by omega)
      rw [hm0, Bool.false_xor]
      obtain ⟨i, hi | hi⟩ : ∃ i, m = 2 * i + 1 ∨ m = 2 * i + 2 := ⟨(m - 1) / 2, by omega⟩
      · subst hi
        have hd : decO (mono (2 * i + 1)) = mono i := by
          funext j
          show decide (2 * j + 1 = 2 * i + 1) = decide (j = i)
          rw [decide_eq_decide]; omega
        rw [hd, ih]
        constructor
        · rintro ⟨r, hr, he⟩
          refine ⟨r + 1, by omega, ?_⟩
          rw [Nat.pow_succ]; omega
        · rintro ⟨r, hr, he⟩
          cases r with
          | zero => exact absurd he (by simp)
          | succ r =>
            rw [Nat.pow_succ] at he
            exact ⟨r, by omega, by omega⟩
      · subst hi
        rw [psi_of_zero (q := decO (mono (2 * i + 2))) (fun j => decide_eq_false (by omega)) n]
        constructor
        · intro h; exact absurd h (by decide)
        · rintro ⟨r, _, he⟩
          cases r with
          | zero => exact absurd he (by simp)
          | succ r => rw [Nat.pow_succ] at he; omega

/-! ## The realisation: coefficients in the basis of powers of `A` -/

/-- Horner realisation with fuel `n`: the row, in mirror coordinates with the wall cell at index `0`,
of the polynomial `Σ_{j < n} c j A^j`. -/
def real : Nat → Row → Nat → Bool
  | 0, _, _ => false
  | _ + 1, c, 0 => c 0
  | n + 1, c, k + 1 => M (real n (down c)) (k + 1)

theorem M_xor (u v : Row) : M (xorS u v) = xorS (M u) (M v) := by
  funext k
  cases k with
  | zero => rfl
  | succ k =>
    show xor (xor (u k) (v k)) (xor (u (k + 2)) (v (k + 2))) =
      xor (xor (u k) (u (k + 2))) (xor (v k) (v (k + 2)))
    simp only [Bool.xor_assoc, Bool.xor_left_comm, Bool.xor_comm]

theorem real_xor (n : Nat) : ∀ c d : Row, real n (xorS c d) = xorS (real n c) (real n d) := by
  induction n with
  | zero => intro c d; funext k; rfl
  | succ n ih =>
    intro c d
    funext k
    cases k with
    | zero => rfl
    | succ k =>
      show M (real n (xorS (down c) (down d))) (k + 1) =
        xor (M (real n (down c)) (k + 1)) (M (real n (down d)) (k + 1))
      rw [ih, M_xor]
      rfl

theorem real_T (n : Nat) (c : Row) : real (n + 1) (T c) = M (real n c) := by
  funext k
  cases k with
  | zero => rfl
  | succ k => rfl

theorem real_supp (n : Nat) : ∀ c : Row, Supp n (real n c) := by
  induction n with
  | zero => intro c j _; rfl
  | succ n ih =>
    intro c j hj
    cases j with
    | zero => exact absurd hj (by omega)
    | succ j =>
      show xor (real n (down c) j) (real n (down c) (j + 2)) = false
      rw [ih (down c) j (by omega), ih (down c) (j + 2) (by omega)]
      rfl

theorem real_of_zero (n : Nat) : ∀ c : Row, (∀ j, c j = false) → ∀ k, real n c k = false := by
  induction n with
  | zero => intro c _ k; rfl
  | succ n ih =>
    intro c hc k
    cases k with
    | zero => exact hc 0
    | succ k =>
      show xor (real n (down c) k) (real n (down c) (k + 2)) = false
      rw [ih (down c) (fun j => hc (j + 1)) k, ih (down c) (fun j => hc (j + 1)) (k + 2)]
      rfl

theorem real_fuel (n : Nat) : ∀ c : Row, Supp n c → ∀ m, n ≤ m → real m c = real n c := by
  induction n with
  | zero =>
    intro c hc m _
    funext k
    rw [real_of_zero m c (fun j => hc j (Nat.zero_le j))]
    rfl
  | succ n ih =>
    intro c hc m hm
    obtain ⟨m, rfl⟩ : ∃ m', m = m' + 1 := ⟨m - 1, by omega⟩
    funext k
    cases k with
    | zero => rfl
    | succ k =>
      show M (real m (down c)) (k + 1) = M (real n (down c)) (k + 1)
      rw [ih (down c) (fun j hj => hc (j + 1) (by omega)) m (by omega)]

theorem down_oddR (c : Row) : down (oddR c) = evenR (down c) := by
  funext j
  show (if (j + 1) % 2 = 1 then c (j + 1) else false) = (if j % 2 = 1 then false else c (j + 1))
  by_cases h : j % 2 = 1
  · rw [ite_eq_right (show ¬ (j + 1) % 2 = 1 by omega), ite_eq_left h]
  · rw [ite_eq_left (show (j + 1) % 2 = 1 by omega), ite_eq_right h]

theorem down_evenR (c : Row) : down (evenR c) = oddR (down c) := by
  funext j
  show (if (j + 1) % 2 = 1 then false else c (j + 1)) = (if j % 2 = 1 then c (j + 1) else false)
  by_cases h : j % 2 = 1
  · rw [ite_eq_right (show ¬ (j + 1) % 2 = 1 by omega), ite_eq_left h]
  · rw [ite_eq_left (show (j + 1) % 2 = 1 by omega), ite_eq_right h]

theorem M_evenR (y : Row) : M (evenR y) = oddR (M y) := by
  funext k
  cases k with
  | zero => rfl
  | succ k =>
    show xor (evenR y k) (evenR y (k + 2)) =
      (if (k + 1) % 2 = 1 then xor (y k) (y (k + 2)) else false)
    unfold evenR
    by_cases h : k % 2 = 1
    · rw [ite_eq_left h, ite_eq_left (show (k + 2) % 2 = 1 by omega),
        ite_eq_right (show ¬ (k + 1) % 2 = 1 by omega)]
      rfl
    · rw [ite_eq_right h, ite_eq_right (show ¬ (k + 2) % 2 = 1 by omega),
        ite_eq_left (show (k + 1) % 2 = 1 by omega)]

theorem M_oddR (y : Row) : M (oddR y) = evenR (M y) := by
  funext k
  cases k with
  | zero => rfl
  | succ k =>
    show xor (oddR y k) (oddR y (k + 2)) =
      (if (k + 1) % 2 = 1 then false else xor (y k) (y (k + 2)))
    unfold oddR
    by_cases h : k % 2 = 1
    · rw [ite_eq_left h, ite_eq_left (show (k + 2) % 2 = 1 by omega),
        ite_eq_right (show ¬ (k + 1) % 2 = 1 by omega)]
    · rw [ite_eq_right h, ite_eq_right (show ¬ (k + 2) % 2 = 1 by omega),
        ite_eq_left (show (k + 1) % 2 = 1 by omega)]
      rfl

theorem real_parity (n : Nat) :
    ∀ c : Row, real n (oddR c) = oddR (real n c) ∧ real n (evenR c) = evenR (real n c) := by
  induction n with
  | zero =>
    intro c
    constructor
    · funext k; show false = (if k % 2 = 1 then false else false); split <;> rfl
    · funext k; show false = (if k % 2 = 1 then false else false); split <;> rfl
  | succ n ih =>
    intro c
    constructor
    · funext k
      cases k with
      | zero => rfl
      | succ k =>
        show M (real n (down (oddR c))) (k + 1) = oddR (M (real n (down c))) (k + 1)
        rw [down_oddR, (ih (down c)).2, M_evenR]
    · funext k
      cases k with
      | zero => rfl
      | succ k =>
        show M (real n (down (evenR c))) (k + 1) = evenR (M (real n (down c))) (k + 1)
        rw [down_evenR, (ih (down c)).1, M_oddR]

/-! ## Squaring: the Frobenius map -/

/-- Spread by two: `spread q (2 i) = q i`, odd indices white. On coefficient sequences it is the
substitution `A ↦ A^2`; on rows in mirror coordinates it is the substitution `S ↦ S^2`. -/
def spread (q : Row) : Row := fun j => if j % 2 = 0 then q (j / 2) else false

theorem spread_even (q : Row) (i : Nat) : spread q (2 * i) = q i := by
  unfold spread
  rw [ite_eq_left (show 2 * i % 2 = 0 by omega), show 2 * i / 2 = i by omega]

theorem spread_odd (q : Row) (i : Nat) : spread q (2 * i + 1) = false := by
  unfold spread
  rw [ite_eq_right (show ¬ (2 * i + 1) % 2 = 0 by omega)]

theorem spread_one (q : Row) : spread q 1 = false := rfl

theorem supp_spread {n : Nat} {q : Row} (hq : Supp n q) : Supp (2 * n) (spread q) := by
  intro j hj
  unfold spread
  split
  · exact hq _ (by omega)
  · rfl

theorem MM_add_two (z : Row) (k : Nat) : M (M z) (k + 2) = xor (z k) (z (k + 4)) := by
  show xor (xor (z k) (z (k + 2))) (xor (z (k + 2)) (z (k + 4))) = _
  simp only [Bool.xor_assoc, Bool.xor_left_comm, xor_cancel_left]

theorem M_M_spread (y : Row) : M (M (spread y)) = spread (M y) := by
  funext k
  match k with
  | 0 => rfl
  | 1 => rfl
  | k + 2 =>
    rw [MM_add_two]
    unfold spread
    by_cases h : k % 2 = 0
    · rw [ite_eq_left h, ite_eq_left (show (k + 4) % 2 = 0 by omega),
        ite_eq_left (show (k + 2) % 2 = 0 by omega), show (k + 4) / 2 = k / 2 + 2 by omega,
        show (k + 2) / 2 = k / 2 + 1 by omega]
      rfl
    · rw [ite_eq_right h, ite_eq_right (show ¬ (k + 4) % 2 = 0 by omega),
        ite_eq_right (show ¬ (k + 2) % 2 = 0 by omega)]
      rfl

theorem down_spread (c : Row) : down (spread c) = T (spread (down c)) := by
  funext j
  cases j with
  | zero => rfl
  | succ j =>
    show spread c (j + 2) = spread (down c) j
    unfold spread
    by_cases h : j % 2 = 0
    · rw [ite_eq_left (show (j + 2) % 2 = 0 by omega), ite_eq_left h,
        show (j + 2) / 2 = j / 2 + 1 by omega]
      rfl
    · rw [ite_eq_right (show ¬ (j + 2) % 2 = 0 by omega), ite_eq_right h]

/-- Squaring commutes with the realisation: `real (2 n) (spread c) = spread (real n c)`. -/
theorem real_spread (n : Nat) : ∀ c : Row, real (2 * n) (spread c) = spread (real n c) := by
  induction n with
  | zero =>
    intro c
    funext k
    show false = (if k % 2 = 0 then false else false)
    split <;> rfl
  | succ n ih =>
    intro c
    funext k
    cases k with
    | zero => rfl
    | succ k =>
      show M (real (2 * n + 1) (down (spread c))) (k + 1) = spread (real (n + 1) c) (k + 1)
      rw [down_spread, real_T, ih, M_M_spread]
      unfold spread
      by_cases h : (k + 1) % 2 = 0
      · rw [ite_eq_left h, ite_eq_left h]
        obtain ⟨j, hj⟩ : ∃ j, (k + 1) / 2 = j + 1 := ⟨(k + 1) / 2 - 1, by omega⟩
        rw [hj]
        rfl
      · rw [ite_eq_right h, ite_eq_right h]

/-! ## The bridge: the extended hybrid is the pair model -/

/-- The hybrid in coefficients: `L X = A X + X_odd`. -/
def Lc (c : Row) : Row := xorS (T c) (oddR c)

theorem supp_Lc {n : Nat} {c : Row} (hc : Supp n c) : Supp (n + 1) (Lc c) := by
  intro j hj
  obtain ⟨j, rfl⟩ : ∃ i, j = i + 1 := ⟨j - 1, by omega⟩
  show xor (c j) (oddR c (j + 1)) = false
  rw [hc j (by omega), supp_oddR hc (j + 1) (by omega)]
  rfl

theorem HE_real {n : Nat} {c : Row} (hc : Supp n c) : HE (real n c) = real (n + 1) (Lc c) := by
  rw [HE_eq, Lc, real_xor, real_T, ← (real_parity n c).1,
    real_fuel n (oddR c) (supp_oddR hc) (n + 1) (by omega)]

theorem supp_iter_Lc {n : Nat} {c : Row} (hc : Supp n c) (t : Nat) :
    Supp (n + t) (iter Lc t c) := by
  induction t generalizing n c with
  | zero => exact hc
  | succ t ih =>
    rw [show n + (t + 1) = n + 1 + t by omega]
    exact ih (supp_Lc hc)

theorem iter_HE_real {n : Nat} {c : Row} (hc : Supp n c) (t : Nat) :
    iter HE t (real n c) = real (n + t) (iter Lc t c) := by
  induction t generalizing n c with
  | zero => rfl
  | succ t ih =>
    show iter HE t (HE (real n c)) = real (n + (t + 1)) (iter Lc t (Lc c))
    rw [HE_real hc, ih (supp_Lc hc), show n + 1 + t = n + (t + 1) by omega]

/-- Split a coefficient sequence into its odd and even parts: `X = A a(T) + b(T)` with
`a = decO c`, `b = decE c`. -/
def split (c : Row) : Row × Row := (decO c, decE c)

/-- The inverse of `split`. -/
def join (x : Row × Row) : Row := fun j => if j % 2 = 1 then x.1 (j / 2) else x.2 (j / 2)

theorem split_Lc (c : Row) : split (Lc c) = P (split c) := by
  have h1 : decO (Lc c) = xorS (decO c) (decE c) := by
    funext m
    show xor (c (2 * m)) (oddR c (2 * m + 1)) = xor (c (2 * m + 1)) (c (2 * m))
    rw [oddR_odd, Bool.xor_comm]
  have h2 : decE (Lc c) = T (decO c) := by
    funext m
    show xor (T c (2 * m)) (oddR c (2 * m)) = T (decO c) m
    rw [oddR_even, Bool.xor_false]
    cases m <;> rfl
  show (decO (Lc c), decE (Lc c)) = (xorS (decO c) (decE c), T (decO c))
  rw [h1, h2]

theorem split_iter_Lc (t : Nat) (c : Row) : split (iter Lc t c) = iter P t (split c) := by
  induction t generalizing c with
  | zero => rfl
  | succ t ih =>
    show split (iter Lc t (Lc c)) = iter P t (P (split c))
    rw [ih, split_Lc]

theorem join_odd (x : Row × Row) (m : Nat) : join x (2 * m + 1) = x.1 m := by
  unfold join
  rw [ite_eq_left (show (2 * m + 1) % 2 = 1 by omega), show (2 * m + 1) / 2 = m by omega]

theorem join_even (x : Row × Row) (m : Nat) : join x (2 * m) = x.2 m := by
  unfold join
  rw [ite_eq_right (show ¬ (2 * m) % 2 = 1 by omega), show 2 * m / 2 = m by omega]

theorem split_join (x : Row × Row) : split (join x) = x := by
  obtain ⟨a, b⟩ := x
  show (decO (join (a, b)), decE (join (a, b))) = (a, b)
  have h1 : decO (join (a, b)) = a := funext fun m => join_odd (a, b) m
  have h2 : decE (join (a, b)) = b := funext fun m => join_even (a, b) m
  rw [h1, h2]

theorem supp_decO {n : Nat} {q : Row} (hq : Supp n q) : Supp n (decO q) :=
  fun j hj => hq _ (by omega)

theorem supp_decE {n : Nat} {q : Row} (hq : Supp n q) : Supp n (decE q) :=
  fun j hj => hq _ (by omega)

theorem decomp (c : Row) : c = xorS (spread (decE c)) (T (spread (decO c))) := by
  funext j
  obtain ⟨i, rfl | rfl⟩ : ∃ i, j = 2 * i ∨ j = 2 * i + 1 := ⟨j / 2, by omega⟩
  · show c (2 * i) = xor (spread (decE c) (2 * i)) (T (spread (decO c)) (2 * i))
    rw [spread_even]
    cases i with
    | zero =>
      show c (2 * 0) = xor (c (2 * 0)) false
      rw [Bool.xor_false]
    | succ i =>
      show c (2 * (i + 1)) = xor (c (2 * (i + 1))) (spread (decO c) (2 * i + 1))
      rw [spread_odd, Bool.xor_false]
  · show c (2 * i + 1) = xor (spread (decE c) (2 * i + 1)) (spread (decO c) (2 * i))
    rw [spread_odd, spread_even, Bool.false_xor]
    rfl

theorem real_one_step {n : Nat} {c : Row} (hc : Supp n c) :
    real (2 * n + 1) c 1 = xor (real n (decO c) 0) (real n (decO c) 1) := by
  have e : real (2 * n + 1) c 1 =
      real (2 * n + 1) (xorS (spread (decE c)) (T (spread (decO c)))) 1 :=
    congrArg (fun d => real (2 * n + 1) d 1) (decomp c)
  rw [e, real_xor, real_fuel (2 * n) _ (supp_spread (supp_decE hc)) (2 * n + 1) (by omega),
    real_spread, real_T, real_spread]
  show xor (spread (real n (decE c)) 1) (M (spread (real n (decO c))) 1) = _
  rw [spread_one, Bool.false_xor]
  rfl

theorem real_one_bound (N : Nat) :
    ∀ n, n ≤ N → ∀ c : Row, Supp n c → real n c 1 = psi n (decO c) := by
  induction N with
  | zero =>
    intro n hn c _
    obtain rfl : n = 0 := by omega
    rfl
  | succ N ih =>
    intro n hn c hc
    cases n with
    | zero => rfl
    | succ n =>
      have ha : Supp ((n + 1) / 2) (decO c) := fun j hj => hc _ (by omega)
      rw [← real_fuel (n + 1) c hc (2 * (n + 1) + 1) (by omega), real_one_step hc]
      show xor (decO c 0) (real (n + 1) (decO c) 1) = xor (decO c 0) (psi n (decO (decO c)))
      rw [real_fuel ((n + 1) / 2) (decO c) ha (n + 1) (by omega),
        ih ((n + 1) / 2) (by omega) (decO c) ha,
        psi_fuel ((n + 1) / 2) (decO (decO c)) (supp_decO ha) n (by omega)]

/-- The depth-one cell of the realisation is `psi` of the odd part. -/
theorem real_one {n : Nat} {c : Row} (hc : Supp n c) : real n c 1 = psi n (decO c) :=
  real_one_bound n n (Nat.le_refl n) c hc

/-- The depth-one column of the extended hybrid. -/
def colE (x : Row) (t : Nat) : Bool := iter HE t x 1

/-- The bridge: the column of the realisation of `c` is the pair-model observation. -/
theorem colE_real {n : Nat} {c : Row} (hc : Supp n c) (t K : Nat) (hK : n + t ≤ K) :
    colE (real n c) t = psi K (iter P t (split c)).1 := by
  show iter HE t (real n c) 1 = _
  rw [iter_HE_real hc, real_one (supp_iter_Lc hc t), ← split_iter_Lc]
  exact (psi_fuel (n + t) _ (supp_decO (supp_iter_Lc hc t)) K hK).symm

theorem supp_join_D {n : Nat} {c : Row} (hc : Supp n c) : Supp n (join (D (split c))) := by
  intro j hj
  show (if j % 2 = 1 then c (2 * (2 * (j / 2) + 1) + 1)
    else xor (c (2 * (2 * (j / 2)) + 1)) (c (2 * (2 * (j / 2) + 1)))) = false
  split
  · exact hc _ (by omega)
  · rw [hc _ (by omega), hc _ (by omega)]
    rfl

/-- Even-time renormalisation on physical coefficients (`c 0 = false`):
`c_{2s}(X) = a(0) + c_s(D X)`. -/
theorem colE_even {n : Nat} {c : Row} (hc : Supp n c) (h0 : c 0 = false) (s : Nat) :
    colE (real n c) (2 * s) = xor (c 1) (colE (real n (join (D (split c)))) s) := by
  rw [colE_real hc (2 * s) (n + 2 * s + 1) (by omega), psi_even_time,
    colE_real (supp_join_D hc) s (n + 2 * s) (by omega), split_join]
  congr 1
  cases s with
  | zero => rfl
  | succ s =>
    rw [show 2 * (s + 1) = 2 * s + 1 + 1 by omega, iter_P_succ_fst_zero]
    show xor (c 1) (c 0) = c 1
    rw [h0, Bool.xor_false]

/-! ## Injectivity of the column -/

/-- The black cell nearest the wall reaches the column after its depth less one ticks: if depths
`1, …, n` are white and depth `n + 1` is black, the column is black at time `n`. -/
theorem front (n : Nat) :
    ∀ x : Row, (∀ j, 1 ≤ j → j ≤ n → x j = false) → x (n + 1) = true → col x n = true := by
  induction n with
  | zero => intro x _ h; exact h
  | succ n ih =>
    intro x hz h1
    show col (H x) n = true
    apply ih
    · intro j hj1 hjn
      match j, hj1 with
      | 1, _ =>
        rw [H_one, hz 2 (by omega) (by omega), hz 1 (by omega) (by omega)]
        rfl
      | j + 2, _ =>
        rw [H_add_two, hz (j + 3) (by omega) (by omega), hz (j + 1) (by omega) (by omega),
          oddR_of_false (hz (j + 2) (by omega) (by omega))]
        rfl
    · cases n with
      | zero =>
        show H x 1 = true
        rw [H_one, h1, hz 1 (by omega) (by omega)]
        rfl
      | succ n =>
        show H x (n + 2) = true
        rw [H_add_two, h1, hz (n + 1) (by omega) (by omega),
          oddR_of_false (hz (n + 2) (by omega) (by omega))]
        rfl

/-- Triangular injectivity: a row whose column is white at every time is white at every depth
`k ≥ 1`. -/
theorem col_inj (x : Row) (hcol : ∀ t, col x t = false) : ∀ k, 1 ≤ k → x k = false := by
  have key : ∀ m, ∀ j, 1 ≤ j → j ≤ m → x j = false := by
    intro m
    induction m with
    | zero => intro j h1 h2; exact absurd h1 (by omega)
    | succ m ih =>
      intro j h1 h2
      rcases Nat.lt_or_ge j (m + 1) with h | h
      · exact ih j h1 (by omega)
      · obtain rfl : j = m + 1 := by omega
        cases hx : x (m + 1) with
        | false => rfl
        | true =>
          have e := front m x ih hx
          rw [hcol m] at e
          exact absurd e (by decide)
  intro k hk
  exact key k k hk (Nat.le_refl k)

/-- A finite row determined from the top down vanishes. -/
theorem zero_of_step {n : Nat} {y : Row} (hy : Supp n y)
    (step : ∀ k, y (k + 1) = false → y (k + 2) = false → y k = false) : ∀ k, y k = false := by
  have key : ∀ d k, n ≤ k + d → y k = false := by
    intro d
    induction d with
    | zero => intro k hk; exact hy k hk
    | succ d ih => intro k hk; exact step k (ih (k + 1) (by omega)) (ih (k + 2) (by omega))
  intro k
  exact key n k (by omega)

theorem HE_kernel {n : Nat} {y : Row} (hy : Supp n y) (h : ∀ k, HE y k = false) :
    ∀ k, y k = false := by
  apply zero_of_step hy
  intro k h1 h2
  have e : xor (y k) (xor (y (k + 2)) (oddR y (k + 1))) = false := h (k + 1)
  rw [h2, oddR_of_false h1, Bool.xor_false, Bool.xor_false] at e
  exact e

theorem HE_fix {n : Nat} {y : Row} (hy : Supp n y) (h : ∀ k, HE y k = y k) :
    ∀ k, y k = false := by
  apply zero_of_step hy
  intro k h1 h2
  have e : xor (y k) (xor (y (k + 2)) (oddR y (k + 1))) = y (k + 1) := h (k + 1)
  rw [h2, oddR_of_false h1, h1, Bool.xor_false, Bool.xor_false] at e
  exact e

theorem M_kernel {n : Nat} {y : Row} (hy : Supp n y) (h : ∀ k, M y (k + 1) = false) :
    ∀ k, y k = false := by
  apply zero_of_step hy
  intro k _ h2
  have e : xor (y k) (y (k + 2)) = false := h k
  rw [h2, Bool.xor_false] at e
  exact e

/-- Injectivity for extended rows: a finite extended row, wall cell included, whose extended
column is white at every time is white everywhere. -/
theorem colE_inj {n : Nat} {y : Row} (hy : Supp n y) (h : ∀ t, colE y t = false) :
    ∀ k, y k = false := by
  have hz : ∀ t, col (HE y) t = false := by
    intro t
    show iter H t (HE y) 1 = false
    rw [← iter_HE_of_wall (show HE y 0 = false from rfl)]
    exact h (t + 1)
  apply HE_kernel hy
  intro k
  cases k with
  | zero => rfl
  | succ k => exact col_inj (HE y) hz (k + 1) (by omega)

/-! ## Linearity -/

theorem oddR_xor (u v : Row) : oddR (xorS u v) = xorS (oddR u) (oddR v) := by
  funext k
  show (if k % 2 = 1 then xor (u k) (v k) else false) =
    xor (if k % 2 = 1 then u k else false) (if k % 2 = 1 then v k else false)
  split <;> rfl

theorem HE_xor (u v : Row) : HE (xorS u v) = xorS (HE u) (HE v) := by
  rw [HE_eq, HE_eq, HE_eq, M_xor, oddR_xor]
  funext k
  show xor (xor (M u k) (M v k)) (xor (oddR u k) (oddR v k)) =
    xor (xor (M u k) (oddR u k)) (xor (M v k) (oddR v k))
  simp only [Bool.xor_assoc, Bool.xor_left_comm]

theorem iter_HE_xor (t : Nat) :
    ∀ u v : Row, iter HE t (xorS u v) = xorS (iter HE t u) (iter HE t v) := by
  induction t with
  | zero => intro u v; rfl
  | succ t ih =>
    intro u v
    show iter HE t (HE (xorS u v)) = xorS (iter HE t (HE u)) (iter HE t (HE v))
    rw [HE_xor, ih]

theorem colE_xor (u v : Row) (t : Nat) : colE (xorS u v) t = xor (colE u t) (colE v t) := by
  show iter HE t (xorS u v) 1 = _
  rw [iter_HE_xor]
  rfl

theorem HE_blank : HE blank = blank := by
  funext k
  cases k with
  | zero => rfl
  | succ k =>
    show xor false (xor false (oddR blank (k + 1))) = false
    rw [oddR_of_false rfl]
    rfl

theorem colE_blank (t : Nat) : colE blank t = false := by
  have : ∀ t, iter HE t blank = blank := by
    intro t
    induction t with
    | zero => rfl
    | succ t ih => show iter HE t (HE blank) = blank; rw [HE_blank, ih]
  show iter HE t blank 1 = false
  rw [this]
  rfl

theorem supp_HE {n : Nat} {y : Row} (hy : Supp n y) : Supp (n + 1) (HE y) := by
  intro j hj
  obtain ⟨j, rfl⟩ : ∃ i, j = i + 1 := ⟨j - 1, by omega⟩
  show xor (y j) (xor (y (j + 2)) (oddR y (j + 1))) = false
  rw [hy j (by omega), hy (j + 2) (by omega), oddR_of_false (hy (j + 1) (by omega))]
  rfl

/-! ## Coefficients of finite rows -/

/-- The realisation is injective on finite coefficient sequences. -/
theorem real_inj (n : Nat) :
    ∀ c : Row, Supp n c → (∀ k, real n c k = false) → ∀ j, c j = false := by
  induction n with
  | zero => intro c hc _ j; exact hc j (Nat.zero_le j)
  | succ n ih =>
    intro c hc h j
    have hd : ∀ k, real n (down c) k = false :=
      M_kernel (real_supp n (down c)) (fun k => h (k + 1))
    have hd' := ih (down c) (fun j hj => hc (j + 1) (by omega)) hd
    cases j with
    | zero => exact h 0
    | succ j => exact hd' j

/-- One black cell at index `n`, of colour `b`. -/
def single (n : Nat) (b : Bool) : Row := fun k => decide (k = n) && b

theorem M_surj (n : Nat) :
    ∀ z : Row, z 0 = false → Supp (n + 1) z → ∃ y, Supp n y ∧ M y = z := by
  induction n with
  | zero =>
    intro z h0 hz
    refine ⟨blank, fun j _ => rfl, ?_⟩
    funext k
    cases k with
    | zero => exact h0.symm
    | succ k => exact (hz (k + 1) (by omega)).symm
  | succ n ih =>
    intro z h0 hz
    have h0' : xorS z (M (single n (z (n + 1)))) 0 = false := by
      show xor (z 0) false = false
      rw [h0]
      rfl
    have hz' : Supp (n + 1) (xorS z (M (single n (z (n + 1))))) := by
      intro j hj
      obtain ⟨j, rfl⟩ : ∃ i, j = i + 1 := ⟨j - 1, by omega⟩
      show xor (z (j + 1)) (xor (decide (j = n) && z (n + 1)) (decide (j + 2 = n) && z (n + 1))) =
        false
      rw [show decide (j + 2 = n) = false from decide_eq_false (by omega)]
      by_cases hjn : j = n
      · subst hjn
        rw [show decide (j = j) = true from decide_eq_true rfl]
        simp
      · rw [hz (j + 1) (by omega), show decide (j = n) = false from decide_eq_false hjn]
        rfl
    obtain ⟨y', hy', hM⟩ := ih _ h0' hz'
    refine ⟨xorS y' (single n (z (n + 1))), ?_, ?_⟩
    · intro j hj
      show xor (y' j) (decide (j = n) && z (n + 1)) = false
      rw [hy' j (by omega), show decide (j = n) = false from decide_eq_false (by omega)]
      rfl
    · rw [M_xor, hM]
      funext k
      show xor (xor (z k) (M (single n (z (n + 1))) k)) (M (single n (z (n + 1))) k) = z k
      rw [Bool.xor_assoc, Bool.xor_self, Bool.xor_false]

/-- Every finite row is a realisation: the change of basis to powers of `A` is onto. -/
theorem real_surj (n : Nat) : ∀ x : Row, Supp n x → ∃ c, Supp n c ∧ real n c = x := by
  induction n with
  | zero =>
    intro x hx
    refine ⟨blank, fun j _ => rfl, ?_⟩
    funext k
    exact (hx k (Nat.zero_le k)).symm
  | succ n ih =>
    intro x hx
    obtain ⟨y, hy, hMy⟩ := M_surj n (fun k => if k = 0 then false else x k) rfl
      (fun j hj => by
        show (if j = 0 then false else x j) = false
        rw [ite_eq_right (show ¬ j = 0 by omega)]
        exact hx j hj)
    obtain ⟨c', hc', hreal⟩ := ih y hy
    refine ⟨fun j => if j = 0 then x 0 else c' (j - 1), ?_, ?_⟩
    · intro j hj
      show (if j = 0 then x 0 else c' (j - 1)) = false
      rw [ite_eq_right (show ¬ j = 0 by omega)]
      exact hc' _ (by omega)
    · funext k
      cases k with
      | zero => rfl
      | succ k =>
        have hd : down (fun j => if j = 0 then x 0 else c' (j - 1)) = c' := by
          funext j
          show (if j + 1 = 0 then x 0 else c' (j + 1 - 1)) = c' j
          rw [ite_eq_right (show ¬ j + 1 = 0 by omega), Nat.add_sub_cancel]
        show M (real n (down (fun j => if j = 0 then x 0 else c' (j - 1)))) (k + 1) = x (k + 1)
        rw [hd, hreal, hMy]
        show (if k + 1 = 0 then false else x (k + 1)) = x (k + 1)
        rw [ite_eq_right (show ¬ k + 1 = 0 by omega)]

/-! ## Classification in coefficients -/

/-- The family `X = (A + A^2) p(A^4) + r(A^4)` with `p(0) = 1`, in coefficients (the condition
`r(0) = 0` is the hypothesis `c 0 = false`): `c 1 = 1`, `c (4 m + 3) = 0` and
`c (4 m + 1) = c (4 m + 2)`. -/
def AFam (c : Row) : Prop :=
  c 1 = true ∧ ∀ m, c (4 * m + 3) = false ∧ c (4 * m + 1) = c (4 * m + 2)

/-- **Classification in coefficients.** A finite physical row with coefficient sequence `c`
(that is, the row `real n c`) is immortal iff `c` lies in the family. -/
theorem immortal_real_iff {n : Nat} {c : Row} (hc : Supp n c) (h0 : c 0 = false) :
    Immortal (real n c) ↔ AFam c := by
  have hx0 : real n c 0 = false := by
    cases n with
    | zero => rfl
    | succ n => exact h0
  have hev : ∀ s, col (real n c) (2 * s) = xor (c 1) (colE (real n (join (D (split c)))) s) := by
    intro s
    show iter H (2 * s) (real n c) 1 = _
    rw [← iter_HE_of_wall hx0]
    exact colE_even hc h0 s
  have hy : Supp n (real n (join (D (split c)))) := real_supp n _
  constructor
  · intro himm
    cases h1 : c 1 with
    | true =>
      have hz : ∀ s, colE (real n (join (D (split c)))) s = false := by
        intro s
        have e := himm s
        rw [hev, h1] at e
        exact eq_false_of_true_xor e
      have hj := real_inj n _ (supp_join_D hc) (colE_inj hy hz)
      refine ⟨h1, fun m => ⟨?_, ?_⟩⟩
      · have e := hj (2 * m + 1)
        rw [join_odd] at e
        rw [show 4 * m + 3 = 2 * (2 * m + 1) + 1 by omega]
        exact e
      · have e := hj (2 * m)
        rw [join_even] at e
        rw [show 4 * m + 1 = 2 * (2 * m) + 1 by omega, show 4 * m + 2 = 2 * (2 * m + 1) by omega]
        exact eq_of_xor_false e
    | false =>
      exfalso
      generalize real n (join (D (split c))) = y at hev hy
      have hone : ∀ s, colE y s = true := by
        intro s
        have e := himm s
        rw [hev, h1] at e
        exact eq_true_of_false_xor e
      have hz : ∀ s, colE (xorS (HE y) y) s = false := by
        intro s
        rw [colE_xor]
        show xor (colE y (s + 1)) (colE y s) = false
        rw [hone, hone]
        rfl
      have hfix := colE_inj (supp_xor (supp_HE hy) (supp_mono hy (by omega))) hz
      have hy0 := HE_fix hy (fun k => eq_of_xor_false (hfix k))
      have e := hone 0
      rw [show colE y 0 = y 1 from rfl, hy0 1] at e
      exact absurd e (by decide)
  · rintro ⟨h1, hm⟩ s
    have hz : real n (join (D (split c))) = blank := by
      funext k
      apply real_of_zero
      intro j
      obtain ⟨i, rfl | rfl⟩ : ∃ i, j = 2 * i ∨ j = 2 * i + 1 := ⟨j / 2, by omega⟩
      · rw [join_even]
        show xor (c (2 * (2 * i) + 1)) (c (2 * (2 * i + 1))) = false
        rw [show 2 * (2 * i) + 1 = 4 * i + 1 by omega, show 2 * (2 * i + 1) = 4 * i + 2 by omega,
          (hm i).2, Bool.xor_self]
      · rw [join_odd]
        show c (2 * (2 * i + 1) + 1) = false
        rw [show 2 * (2 * i + 1) + 1 = 4 * i + 3 by omega]
        exact (hm i).1
    rw [hev, hz, colE_blank, h1]
    rfl

/-- The bridge for the physical hybrid: on a physical coefficient sequence (`c 0 = false`) the
column of `H` is the pair-model observation `psi ∘ fst ∘ P^t`, for any fuel `K ≥ n + t`. -/
theorem col_real {n : Nat} {c : Row} (hc : Supp n c) (h0 : c 0 = false) (t K : Nat)
    (hK : n + t ≤ K) : col (real n c) t = psi K (iter P t (split c)).1 := by
  have hx0 : real n c 0 = false := by
    cases n with
    | zero => rfl
    | succ n => exact h0
  show iter H t (real n c) 1 = _
  rw [← iter_HE_of_wall hx0]
  exact colE_real hc t K hK

/-- The dynamics bridge for the physical hybrid: `H^t` of a realisation is the realisation of
`L^t`. -/
theorem iter_H_real {n : Nat} {c : Row} (hc : Supp n c) (h0 : c 0 = false) (t : Nat) :
    iter H t (real n c) = real (n + t) (iter Lc t c) := by
  have hx0 : real n c 0 = false := by
    cases n with
    | zero => rfl
    | succ n => exact h0
  rw [← iter_HE_of_wall hx0, iter_HE_real hc]

/-! ## The bit family -/

/-- The bit family. `famRow p r` is the exclusive-or sum of `e_1 + e_2` (for `p 0`),
`p j (e_{4j-2} + e_{4j-1} + e_{4j+1} + e_{4j+2})` for `j ≥ 1` and `r j e_{4j}`, evaluated cell by
cell: depth `4 i` is `r i`, depth `4 i + 1` is `p i`, depth `4 i + 2` is `p i + p (i + 1)` and
depth `4 i + 3` is `p (i + 1)`. -/
def famRow (p r : Row) (k : Nat) : Bool :=
  if k % 4 = 0 then r (k / 4)
  else if k % 4 = 1 then p (k / 4)
  else if k % 4 = 2 then xor (p (k / 4)) (p (k / 4 + 1))
  else p (k / 4 + 1)

theorem famRow_zero_mod (p r : Row) (i : Nat) : famRow p r (4 * i) = r i := by
  unfold famRow
  rw [ite_eq_left (show 4 * i % 4 = 0 by omega), show 4 * i / 4 = i by omega]

theorem famRow_one_mod (p r : Row) (i : Nat) : famRow p r (4 * i + 1) = p i := by
  unfold famRow
  rw [ite_eq_right (show ¬ (4 * i + 1) % 4 = 0 by omega),
    ite_eq_left (show (4 * i + 1) % 4 = 1 by omega), show (4 * i + 1) / 4 = i by omega]

theorem famRow_two_mod (p r : Row) (i : Nat) :
    famRow p r (4 * i + 2) = xor (p i) (p (i + 1)) := by
  unfold famRow
  rw [ite_eq_right (show ¬ (4 * i + 2) % 4 = 0 by omega),
    ite_eq_right (show ¬ (4 * i + 2) % 4 = 1 by omega),
    ite_eq_left (show (4 * i + 2) % 4 = 2 by omega), show (4 * i + 2) / 4 = i by omega]

theorem famRow_three_mod (p r : Row) (i : Nat) : famRow p r (4 * i + 3) = p (i + 1) := by
  unfold famRow
  rw [ite_eq_right (show ¬ (4 * i + 3) % 4 = 0 by omega),
    ite_eq_right (show ¬ (4 * i + 3) % 4 = 1 by omega),
    ite_eq_right (show ¬ (4 * i + 3) % 4 = 2 by omega), show (4 * i + 3) / 4 = i by omega]

/-- Coefficients of `(A + A^2) p(A^4) + r(A^4)`. -/
def afam (p r : Row) (j : Nat) : Bool :=
  if j % 4 = 0 then r (j / 4) else if j % 4 = 3 then false else p (j / 4)

theorem afam_zero_mod (p r : Row) (i : Nat) : afam p r (4 * i) = r i := by
  unfold afam
  rw [ite_eq_left (show 4 * i % 4 = 0 by omega), show 4 * i / 4 = i by omega]

theorem afam_one_mod (p r : Row) (i : Nat) : afam p r (4 * i + 1) = p i := by
  unfold afam
  rw [ite_eq_right (show ¬ (4 * i + 1) % 4 = 0 by omega),
    ite_eq_right (show ¬ (4 * i + 1) % 4 = 3 by omega), show (4 * i + 1) / 4 = i by omega]

theorem afam_two_mod (p r : Row) (i : Nat) : afam p r (4 * i + 2) = p i := by
  unfold afam
  rw [ite_eq_right (show ¬ (4 * i + 2) % 4 = 0 by omega),
    ite_eq_right (show ¬ (4 * i + 2) % 4 = 3 by omega), show (4 * i + 2) / 4 = i by omega]

theorem afam_three_mod (p r : Row) (i : Nat) : afam p r (4 * i + 3) = false := by
  unfold afam
  rw [ite_eq_right (show ¬ (4 * i + 3) % 4 = 0 by omega),
    ite_eq_left (show (4 * i + 3) % 4 = 3 by omega)]

theorem cases_four (k : Nat) : ∃ i, k = 4 * i ∨ k = 4 * i + 1 ∨ k = 4 * i + 2 ∨ k = 4 * i + 3 :=
  ⟨k / 4, by omega⟩

theorem ss_zero (q : Row) (i : Nat) : spread (spread q) (4 * i) = q i := by
  rw [show 4 * i = 2 * (2 * i) by omega, spread_even, spread_even]

theorem ss_one (q : Row) (i : Nat) : spread (spread q) (4 * i + 1) = false := by
  rw [show 4 * i + 1 = 2 * (2 * i) + 1 by omega, spread_odd]

theorem ss_two (q : Row) (i : Nat) : spread (spread q) (4 * i + 2) = false := by
  rw [show 4 * i + 2 = 2 * (2 * i + 1) by omega, spread_even, spread_odd]

theorem ss_three (q : Row) (i : Nat) : spread (spread q) (4 * i + 3) = false := by
  rw [show 4 * i + 3 = 2 * (2 * i + 1) + 1 by omega, spread_odd]

theorem T_ss_four (q : Row) (i : Nat) : T (spread (spread q)) (4 * i) = false := by
  cases i with
  | zero => rfl
  | succ i =>
    rw [show 4 * (i + 1) = 4 * i + 3 + 1 by omega]
    exact ss_three q i

theorem TT_ss_four (q : Row) (i : Nat) : T (T (spread (spread q))) (4 * i) = false := by
  cases i with
  | zero => rfl
  | succ i =>
    rw [show 4 * (i + 1) = 4 * i + 2 + 1 + 1 by omega]
    exact ss_two q i

theorem afam_eq (p r : Row) :
    afam p r = xorS (xorS (T (spread (spread p))) (T (T (spread (spread p))))) (spread (spread r)) := by
  funext j
  obtain ⟨i, rfl | rfl | rfl | rfl⟩ := cases_four j
  · show afam p r (4 * i) = xor (xor (T (spread (spread p)) (4 * i))
      (T (T (spread (spread p))) (4 * i))) (spread (spread r) (4 * i))
    rw [afam_zero_mod, T_ss_four, TT_ss_four, ss_zero, Bool.xor_false, Bool.false_xor]
  · show afam p r (4 * i + 1) = xor (xor (spread (spread p) (4 * i))
      (T (spread (spread p)) (4 * i))) (spread (spread r) (4 * i + 1))
    rw [afam_one_mod, T_ss_four, ss_zero, ss_one, Bool.xor_false, Bool.xor_false]
  · show afam p r (4 * i + 2) = xor (xor (spread (spread p) (4 * i + 1))
      (spread (spread p) (4 * i))) (spread (spread r) (4 * i + 2))
    rw [afam_two_mod, ss_one, ss_zero, ss_two, Bool.xor_false, Bool.false_xor]
  · show afam p r (4 * i + 3) = xor (xor (spread (spread p) (4 * i + 2))
      (spread (spread p) (4 * i + 1))) (spread (spread r) (4 * i + 3))
    rw [afam_three_mod, ss_two, ss_one, ss_three]
    rfl

theorem M_ss_four (q : Row) (i : Nat) : M (spread (spread q)) (4 * i) = false := by
  cases i with
  | zero => rfl
  | succ i =>
    rw [show 4 * (i + 1) = 4 * i + 3 + 1 by omega]
    show xor (spread (spread q) (4 * i + 3)) (spread (spread q) (4 * i + 3 + 2)) = false
    rw [ss_three, show 4 * i + 3 + 2 = 4 * (i + 1) + 1 by omega, ss_one]
    rfl

theorem MM_ss_four (q : Row) (i : Nat) : M (M (spread (spread q))) (4 * i) = false := by
  cases i with
  | zero => rfl
  | succ i =>
    rw [show 4 * (i + 1) = 4 * i + 2 + 2 by omega, MM_add_two, ss_two,
      show 4 * i + 2 + 4 = 4 * (i + 1) + 2 by omega, ss_two]
    rfl

theorem MM_ss_one (q : Row) (i : Nat) : M (M (spread (spread q))) (4 * i + 1) = false := by
  cases i with
  | zero => rfl
  | succ i =>
    rw [show 4 * (i + 1) + 1 = 4 * i + 3 + 2 by omega, MM_add_two, ss_three,
      show 4 * i + 3 + 4 = 4 * (i + 1) + 3 by omega, ss_three]
    rfl

theorem famRow_eq (u v : Row) :
    famRow u v =
      xorS (xorS (M (spread (spread u))) (M (M (spread (spread u))))) (spread (spread v)) := by
  funext k
  obtain ⟨i, rfl | rfl | rfl | rfl⟩ := cases_four k
  · show famRow u v (4 * i) = xor (xor (M (spread (spread u)) (4 * i))
      (M (M (spread (spread u))) (4 * i))) (spread (spread v) (4 * i))
    rw [famRow_zero_mod, M_ss_four, MM_ss_four, ss_zero, Bool.xor_false, Bool.false_xor]
  · show famRow u v (4 * i + 1) = xor (xor (xor (spread (spread u) (4 * i))
      (spread (spread u) (4 * i + 2))) (M (M (spread (spread u))) (4 * i + 1)))
      (spread (spread v) (4 * i + 1))
    rw [famRow_one_mod, MM_ss_one, ss_zero, ss_two, ss_one, Bool.xor_false, Bool.xor_false,
      Bool.xor_false]
  · have e : M (M (spread (spread u))) (4 * i + 2) = xor (u i) (u (i + 1)) := by
      rw [MM_add_two, ss_zero, show 4 * i + 4 = 4 * (i + 1) by omega, ss_zero]
    show famRow u v (4 * i + 2) = xor (xor (xor (spread (spread u) (4 * i + 1))
      (spread (spread u) (4 * i + 3))) (M (M (spread (spread u))) (4 * i + 2)))
      (spread (spread v) (4 * i + 2))
    rw [famRow_two_mod, e, ss_one, ss_three, ss_two, Bool.xor_false, Bool.xor_false,
      Bool.false_xor]
  · have e1 : M (M (spread (spread u))) (4 * i + 3) = false := by
      rw [show 4 * i + 3 = 4 * i + 1 + 2 by omega, MM_add_two, ss_one,
        show 4 * i + 1 + 4 = 4 * (i + 1) + 1 by omega, ss_one]
      rfl
    have e2 : M (spread (spread u)) (4 * i + 3) = u (i + 1) := by
      show xor (spread (spread u) (4 * i + 2)) (spread (spread u) (4 * i + 2 + 2)) = u (i + 1)
      rw [ss_two, show 4 * i + 2 + 2 = 4 * (i + 1) by omega, ss_zero, Bool.false_xor]
    show famRow u v (4 * i + 3) = xor (xor (M (spread (spread u)) (4 * i + 3))
      (M (M (spread (spread u))) (4 * i + 3))) (spread (spread v) (4 * i + 3))
    rw [famRow_three_mod, e1, e2, ss_three, Bool.xor_false, Bool.xor_false]

theorem supp_afam {n : Nat} {p r : Row} (hp : Supp n p) (hr : Supp n r) :
    Supp (4 * n) (afam p r) := by
  intro j hj
  unfold afam
  split
  · exact hr _ (by omega)
  · split
    · rfl
    · exact hp _ (by omega)

/-- The realisation of the coefficient family is the bit family:
`real (4 n + 2) (afam p r) = famRow (real n p) (real n r)`. -/
theorem real_afam {n : Nat} {p r : Row} (hp : Supp n p) (hr : Supp n r) :
    real (4 * n + 2) (afam p r) = famRow (real n p) (real n r) := by
  have hsp : Supp (4 * n) (spread (spread p)) := by
    have h := supp_spread (supp_spread hp)
    rwa [show 2 * (2 * n) = 4 * n by omega] at h
  have hsr : Supp (4 * n) (spread (spread r)) := by
    have h := supp_spread (supp_spread hr)
    rwa [show 2 * (2 * n) = 4 * n by omega] at h
  have hss : ∀ q : Row, real (4 * n) (spread (spread q)) = spread (spread (real n q)) := by
    intro q
    rw [show 4 * n = 2 * (2 * n) by omega, real_spread, real_spread]
  have h1 : real (4 * n + 2) (T (spread (spread p))) = M (spread (spread (real n p))) := by
    rw [show 4 * n + 2 = 4 * n + 1 + 1 by omega, real_T,
      real_fuel (4 * n) _ hsp (4 * n + 1) (by omega), hss]
  have h2 : real (4 * n + 2) (T (T (spread (spread p)))) = M (M (spread (spread (real n p)))) := by
    rw [show 4 * n + 2 = 4 * n + 1 + 1 by omega, real_T, real_T, hss]
  have h3 : real (4 * n + 2) (spread (spread r)) = spread (spread (real n r)) := by
    rw [real_fuel (4 * n) _ hsr (4 * n + 2) (by omega), hss]
  rw [afam_eq, real_xor, real_xor, h1, h2, h3, famRow_eq]

/-- The power `A^12` is the row `e_4 + e_12`, not `e_12`. -/
theorem real_A_pow_twelve : ∀ k, k < 14 → real 13 (mono 12) k = decide (k = 4 ∨ k = 12) := by
  decide

theorem afam_of_AFam {c : Row} (h : AFam c) :
    c = afam (fun i => c (4 * i + 1)) (fun i => c (4 * i)) := by
  funext j
  obtain ⟨i, rfl | rfl | rfl | rfl⟩ := cases_four j
  · rw [afam_zero_mod]
  · rw [afam_one_mod]
  · rw [afam_two_mod]
    exact ((h.2 i).2).symm
  · rw [afam_three_mod]
    exact (h.2 i).1

theorem supp_of_width {W : Nat} {x : Row} (hx : WidthLE W x) : Supp (W + 1) x :=
  fun k hk => hx k hk

/-- **Classification.** A finite row with a white wall is immortal iff it lies in the bit
family: `x = e_1 + e_2 + Σ_{j ≥ 1} p_j (e_{4j-2} + e_{4j-1} + e_{4j+1} + e_{4j+2}) +
Σ_{j ≥ 1} r_j e_{4j}`. -/
theorem immortal_iff_famRow {W : Nat} {x : Row} (hx : WidthLE W x) (h0 : x 0 = false) :
    Immortal x ↔ ∃ p r : Row, p 0 = true ∧ r 0 = false ∧ x = famRow p r := by
  obtain ⟨c, hc, rfl⟩ := real_surj (W + 1) x (supp_of_width hx)
  have hc0 : c 0 = false := h0
  constructor
  · intro himm
    have hA := (immortal_real_iff hc hc0).1 himm
    have hp : Supp (W + 1) (fun i => c (4 * i + 1)) := fun j hj => hc _ (by omega)
    have hr : Supp (W + 1) (fun i => c (4 * i)) := fun j hj => hc _ (by omega)
    refine ⟨real (W + 1) (fun i => c (4 * i + 1)), real (W + 1) (fun i => c (4 * i)), hA.1, hc0, ?_⟩
    rw [← real_afam hp hr, ← afam_of_AFam hA]
    exact (real_fuel (W + 1) c hc _ (by omega)).symm
  · rintro ⟨p', r', hp1, hr0, hfam⟩
    have hsp : Supp (W + 1) p' := by
      intro j hj
      have e := congrFun hfam (4 * j + 1)
      rw [famRow_one_mod] at e
      rw [← e]
      exact real_supp (W + 1) c _ (by omega)
    have hsr : Supp (W + 1) r' := by
      intro j hj
      have e := congrFun hfam (4 * j)
      rw [famRow_zero_mod] at e
      rw [← e]
      exact real_supp (W + 1) c _ (by omega)
    obtain ⟨p, hp, hpp⟩ := real_surj (W + 1) p' hsp
    obtain ⟨r, hr, hrr⟩ := real_surj (W + 1) r' hsr
    have hrow : real (W + 1) c = real (4 * (W + 1) + 2) (afam p r) := by
      rw [real_afam hp hr, hpp, hrr, hfam]
    have hp0 : p 0 = true := (congrFun hpp 0).trans hp1
    have hr0' : r 0 = false := (congrFun hrr 0).trans hr0
    have hA : AFam (afam p r) := by
      refine ⟨(afam_one_mod p r 0).trans hp0, fun m => ⟨afam_three_mod p r m, ?_⟩⟩
      rw [afam_one_mod, afam_two_mod]
    rw [hrow]
    exact (immortal_real_iff (supp_mono (supp_afam hp hr) (by omega))
      ((afam_zero_mod p r 0).trans hr0')).2 hA

/-- The bit family, cell by cell: depth `1` is black and, for every `j`,
`x (4 j + 3) = x (4 j + 5)` and `x (4 j + 2) = x (4 j + 1) + x (4 j + 3)`. -/
def BitFam (x : Row) : Prop :=
  x 1 = true ∧ ∀ j, x (4 * j + 3) = x (4 * j + 5) ∧ x (4 * j + 2) = xor (x (4 * j + 1)) (x (4 * j + 3))

theorem famRow_iff_bitFam (x : Row) :
    (∃ p r : Row, p 0 = true ∧ r 0 = false ∧ x = famRow p r) ↔ x 0 = false ∧ BitFam x := by
  constructor
  · rintro ⟨p, r, hp, hr, rfl⟩
    refine ⟨(famRow_zero_mod p r 0).trans hr, (famRow_one_mod p r 0).trans hp, fun j => ⟨?_, ?_⟩⟩
    · rw [famRow_three_mod, show 4 * j + 5 = 4 * (j + 1) + 1 by omega, famRow_one_mod]
    · rw [famRow_two_mod, famRow_one_mod, famRow_three_mod]
  · rintro ⟨h0, h1, hj⟩
    refine ⟨fun i => x (4 * i + 1), fun i => x (4 * i), h1, h0, ?_⟩
    funext k
    obtain ⟨i, rfl | rfl | rfl | rfl⟩ := cases_four k
    · rw [famRow_zero_mod]
    · rw [famRow_one_mod]
    · rw [famRow_two_mod, (hj i).2, (hj i).1, show 4 * (i + 1) + 1 = 4 * i + 5 by omega]
    · rw [famRow_three_mod, (hj i).1, show 4 * (i + 1) + 1 = 4 * i + 5 by omega]

/-- **Classification, cell by cell.** -/
theorem immortal_iff_bitFam {W : Nat} {x : Row} (hx : WidthLE W x) (h0 : x 0 = false) :
    Immortal x ↔ BitFam x := by
  rw [immortal_iff_famRow hx h0, famRow_iff_bitFam]
  exact ⟨fun h => h.2, fun h => ⟨h0, h⟩⟩

/-- Whiten the wall cell. -/
def clearWall (x : Row) : Row := fun k => if k = 0 then false else x k

theorem H_clearWall (x : Row) : H (clearWall x) = H x := by
  funext k
  match k with
  | 0 => rfl
  | 1 =>
    rw [H_one, H_one]
    rfl
  | k + 2 =>
    have e : ∀ i, clearWall x (i + 1) = x (i + 1) := fun i => ite_eq_right (by omega)
    rw [H_add_two, H_add_two]
    show xor (clearWall x (k + 2 + 1)) (xor (clearWall x (k + 1))
      (if (k + 2) % 2 = 1 then clearWall x (k + 1 + 1) else false)) = _
    rw [e, e, e]
    rfl

/-- **Classification for any wall cell.** `H` never reads depth `0`, so the cell-by-cell
classification holds for every finite row. -/
theorem immortal_iff_bitFam_anyWall {W : Nat} {x : Row} (hx : WidthLE W x) :
    Immortal x ↔ BitFam x := by
  have hcol : ∀ t, col (clearWall x) t = col x t := by
    intro t
    cases t with
    | zero => rfl
    | succ t =>
      show iter H t (H (clearWall x)) 1 = iter H t (H x) 1
      rw [H_clearWall]
  have hw : WidthLE W (clearWall x) := by
    intro k hk
    show (if k = 0 then false else x k) = false
    split
    · rfl
    · exact hx k hk
  have hI : Immortal x ↔ Immortal (clearWall x) :=
    ⟨fun h s => (hcol (2 * s)).trans (h s), fun h s => (hcol (2 * s)).symm.trans (h s)⟩
  rw [hI, immortal_iff_bitFam hw rfl]
  have e : ∀ i, clearWall x (i + 1) = x (i + 1) := fun i => ite_eq_right (by omega)
  unfold BitFam
  rw [show clearWall x 1 = x 1 from e 0]
  constructor
  · rintro ⟨h1, hj⟩
    refine ⟨h1, fun j => ?_⟩
    have := hj j
    rw [show 4 * j + 3 = (4 * j + 2) + 1 by omega, show 4 * j + 5 = (4 * j + 4) + 1 by omega,
      show 4 * j + 2 = (4 * j + 1) + 1 by omega, show 4 * j + 1 = (4 * j) + 1 by omega,
      e, e, e, e] at this
    exact this
  · rintro ⟨h1, hj⟩
    refine ⟨h1, fun j => ?_⟩
    rw [show 4 * j + 3 = (4 * j + 2) + 1 by omega, show 4 * j + 5 = (4 * j + 4) + 1 by omega,
      show 4 * j + 2 = (4 * j + 1) + 1 by omega, show 4 * j + 1 = (4 * j) + 1 by omega,
      e, e, e, e]
    exact hj j

/-! ## Concrete rows -/

/-- The bit family with the conditions checked for `j < N` only. -/
abbrev BitFamUpTo (N : Nat) (x : Row) : Prop :=
  x 1 = true ∧ ∀ j, j < N →
    x (4 * j + 3) = x (4 * j + 5) ∧ x (4 * j + 2) = xor (x (4 * j + 1)) (x (4 * j + 3))

theorem bitFam_iff_upTo {W : Nat} {x : Row} (hx : WidthLE W x) :
    BitFam x ↔ BitFamUpTo (W / 4 + 1) x := by
  constructor
  · rintro ⟨h1, hj⟩
    exact ⟨h1, fun j _ => hj j⟩
  · rintro ⟨h1, hj⟩
    refine ⟨h1, fun j => ?_⟩
    rcases Nat.lt_or_ge j (W / 4 + 1) with h | h
    · exact hj j h
    · rw [hx (4 * j + 3) (by omega), hx (4 * j + 5) (by omega), hx (4 * j + 2) (by omega),
        hx (4 * j + 1) (by omega)]
      exact ⟨rfl, rfl⟩

/-- The row with depth `d ≥ 1` black exactly when bit `d - 1` of `n` is set (depth `0` white). -/
def rowOf (n : Nat) : Row := fun k => decide (1 ≤ k) && n.testBit (k - 1)

theorem rowOf_width {W n : Nat} (hn : n < 2 ^ W) : WidthLE W (rowOf n) := by
  intro k hk
  show (decide (1 ≤ k) && n.testBit (k - 1)) = false
  rw [Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hn (Nat.pow_le_pow_right (by omega) (by omega))),
    Bool.and_false]

theorem immortal_rowOf_iff {W n : Nat} (hn : n < 2 ^ W) :
    Immortal (rowOf n) ↔ BitFamUpTo (W / 4 + 1) (rowOf n) := by
  rw [immortal_iff_bitFam (rowOf_width hn) rfl, bitFam_iff_upTo (rowOf_width hn)]

theorem immortal_three : Immortal (rowOf 3) :=
  (immortal_rowOf_iff (W := 2) (by decide)).2 (by decide)

theorem immortal_eleven : Immortal (rowOf 11) :=
  (immortal_rowOf_iff (W := 4) (by decide)).2 (by decide)

theorem immortal_fifty_three : Immortal (rowOf 53) :=
  (immortal_rowOf_iff (W := 6) (by decide)).2 (by decide)

theorem immortal_sixty_one : Immortal (rowOf 61) :=
  (immortal_rowOf_iff (W := 6) (by decide)).2 (by decide)

/-- The immortal rows of width at most `6` with a white wall are exactly `rowOf 3`, `rowOf 11`,
`rowOf 53` and `rowOf 61`. -/
theorem immortal_width_six (n : Nat) (hn : n < 64) :
    Immortal (rowOf n) ↔ n = 3 ∨ n = 11 ∨ n = 53 ∨ n = 61 := by
  rw [immortal_rowOf_iff (W := 6) hn]
  revert n
  decide

theorem H_two (x : Row) : H x 2 = xor (x 3) (xor (x 1) (oddR x 2)) := H_add_two x 0

/-- No row of width at most `1` is immortal, whatever its wall cell: the column is white at
time `2`. -/
theorem not_immortal_width_one {x : Row} (hx : WidthLE 1 x) : ¬ Immortal x := by
  intro himm
  have e : H (H x) 1 = true := himm 1
  rw [H_one, H_one, H_two, hx 2 (by omega), hx 3 (by omega), oddR_of_false (hx 2 (by omega))] at e
  generalize x 1 = b at e
  cases b <;> exact absurd e (by decide)

/-! ## Aperiodicity -/

theorem H_xor (u v : Row) : H (xorS u v) = xorS (H u) (H v) := by
  funext k
  match k with
  | 0 => rfl
  | 1 =>
    show H (xorS u v) 1 = xor (H u 1) (H v 1)
    rw [H_one, H_one, H_one]
    show xor (xor (u 2) (v 2)) (xor (u 1) (v 1)) = xor (xor (u 2) (u 1)) (xor (v 2) (v 1))
    simp only [Bool.xor_assoc, Bool.xor_left_comm, Bool.xor_comm]
  | k + 2 =>
    show H (xorS u v) (k + 2) = xor (H u (k + 2)) (H v (k + 2))
    rw [H_add_two, H_add_two, H_add_two, oddR_xor]
    show xor (xor (u (k + 3)) (v (k + 3))) (xor (xor (u (k + 1)) (v (k + 1)))
        (xor (oddR u (k + 2)) (oddR v (k + 2)))) =
      xor (xor (u (k + 3)) (xor (u (k + 1)) (oddR u (k + 2))))
        (xor (v (k + 3)) (xor (v (k + 1)) (oddR v (k + 2))))
    simp only [Bool.xor_assoc, Bool.xor_left_comm]

theorem iter_H_xor (t : Nat) :
    ∀ u v : Row, iter H t (xorS u v) = xorS (iter H t u) (iter H t v) := by
  induction t with
  | zero => intro u v; rfl
  | succ t ih =>
    intro u v
    show iter H t (H (xorS u v)) = xorS (iter H t (H u)) (iter H t (H v))
    rw [H_xor, ih]

theorem col_xor (u v : Row) (t : Nat) : col (xorS u v) t = xor (col u t) (col v t) := by
  show iter H t (xorS u v) 1 = _
  rw [iter_H_xor]
  rfl

theorem iter_H_wall {x : Row} (hx : x 0 = false) (t : Nat) : iter H t x 0 = false := by
  induction t generalizing x with
  | zero => exact hx
  | succ t ih => exact ih (H_wall x)

theorem supp_H {n : Nat} {x : Row} (hx : Supp n x) : Supp (n + 1) (H x) := by
  intro j hj
  match j, hj with
  | 1, hj =>
    rw [H_one, hx 2 (by omega), hx 1 (by omega)]
    rfl
  | j + 2, hj =>
    rw [H_add_two, hx (j + 3) (by omega), hx (j + 1) (by omega),
      oddR_of_false (hx (j + 2) (by omega))]
    rfl

theorem supp_iter_H {n : Nat} {x : Row} (hx : Supp n x) (t : Nat) : Supp (n + t) (iter H t x) := by
  induction t generalizing n x with
  | zero => exact hx
  | succ t ih =>
    rw [show n + (t + 1) = n + 1 + t by omega]
    exact ih (supp_H hx)

theorem H_top {k : Nat} {y : Row} (hy : Supp (k + 1) y) (hk : 1 ≤ k) : H y (k + 1) = y k := by
  obtain ⟨k, rfl⟩ : ∃ i, k = i + 1 := ⟨k - 1, by omega⟩
  rw [H_add_two, hy (k + 3) (by omega), oddR_of_false (hy (k + 2) (by omega)), Bool.xor_false,
    Bool.false_xor]

/-- The top cell moves one step away from the wall per tick. -/
theorem iter_H_top (q : Nat) :
    ∀ {k : Nat} {y : Row}, Supp (k + 1) y → 1 ≤ k → iter H q y (k + q) = y k := by
  induction q with
  | zero => intro k y _ _; rfl
  | succ q ih =>
    intro k y hy hk
    show iter H q (H y) (k + (q + 1)) = y k
    rw [show k + (q + 1) = k + 1 + q by omega, ih (supp_H hy) (by omega), H_top hy hk]

/-- A finite row with a white wall that returns under `H^q`, `q ≥ 1`, is white. -/
theorem H_periodic_white {n q : Nat} {y : Row} (hy : Supp n y) (h0 : y 0 = false) (hq : 1 ≤ q)
    (hper : iter H q y = y) : ∀ k, y k = false := by
  have step : ∀ m, 1 ≤ m → Supp (m + 1) y → Supp m y := by
    intro m hm hs j hj
    rcases Nat.lt_or_ge j (m + 1) with h | h
    · obtain rfl : j = m := by omega
      have e := iter_H_top q hs hm
      rw [hper] at e
      rw [← e]
      exact hs _ (by omega)
    · exact hs j h
  have down1 : ∀ d, Supp (1 + d) y → Supp 1 y := by
    intro d
    induction d with
    | zero => exact id
    | succ d ih => intro hs; exact ih (step (1 + d) (by omega) hs)
  have h1 := down1 n (supp_mono hy (by omega))
  intro k
  cases k with
  | zero => exact h0
  | succ k => exact h1 (k + 1) (by omega)

theorem col_of_white {y : Row} (hy : ∀ k, y k = false) (t : Nat) : col y t = false := by
  have hH : ∀ {z : Row}, (∀ k, z k = false) → ∀ k, H z k = false := by
    intro z hz k
    match k with
    | 0 => rfl
    | 1 => rw [H_one, hz 2, hz 1]; rfl
    | k + 2 => rw [H_add_two, hz (k + 3), hz (k + 1), oddR_of_false (hz (k + 2))]; rfl
  have key : ∀ t, ∀ z : Row, (∀ k, z k = false) → iter H t z 1 = false := by
    intro t
    induction t with
    | zero => intro z hz; exact hz 1
    | succ t ih => intro z hz; exact ih (H z) (hH hz)
  exact key t y hy

/-- If the column of a finite row with a white wall repeats with period `q ≥ 1` from time `U`
on, it is white from time `U` on. -/
theorem col_periodic_white {n U q : Nat} {x : Row} (hx : Supp n x) (h0 : x 0 = false)
    (hq : 1 ≤ q) (hper : ∀ u, U ≤ u → col x (u + q) = col x u) :
    ∀ u, U ≤ u → col x u = false := by
  have hcol : ∀ t, col (iter H U x) t = col x (U + t) := by
    intro t
    show iter H t (iter H U x) 1 = iter H (U + t) x 1
    rw [iter_add]
  have hcolq : ∀ t, col (iter H q (iter H U x)) t = col (iter H U x) t := by
    intro t
    show iter H t (iter H q (iter H U x)) 1 = col (iter H U x) t
    rw [← iter_add]
    show col (iter H U x) (q + t) = col (iter H U x) t
    rw [hcol, hcol, show U + (q + t) = U + t + q by omega, hper (U + t) (by omega)]
  have hw : ∀ t, col (xorS (iter H U x) (iter H q (iter H U x))) t = false := by
    intro t
    rw [col_xor, hcolq, Bool.xor_self]
  have hy0 : iter H U x 0 = false := iter_H_wall h0 U
  have hyq0 : iter H q (iter H U x) 0 = false := iter_H_wall hy0 q
  have heq : iter H q (iter H U x) = iter H U x := by
    funext k
    cases k with
    | zero => rw [hy0, hyq0]
    | succ k => exact (eq_of_xor_false (col_inj _ hw (k + 1) (by omega))).symm
  have hwhite := H_periodic_white (supp_iter_H hx U) hy0 hq heq
  intro u hu
  obtain ⟨t, rfl⟩ : ∃ t, u = U + t := ⟨u - U, by omega⟩
  rw [← hcol]
  exact col_of_white hwhite t

theorem H_kernel {n : Nat} {y : Row} (hy : Supp n y) (h0 : y 0 = false)
    (h : ∀ k, H y k = false) : ∀ k, y k = false := by
  apply zero_of_step hy
  intro k h1 h2
  cases k with
  | zero => exact h0
  | succ k =>
    have e := h (k + 2)
    rw [H_add_two, h2, oddR_of_false h1, Bool.xor_false, Bool.false_xor] at e
    exact e

theorem iter_H_kernel (U : Nat) :
    ∀ {n : Nat} {x : Row}, Supp n x → x 0 = false → (∀ k, iter H U x k = false) →
      ∀ k, x k = false := by
  induction U with
  | zero => intro n x _ _ h; exact h
  | succ U ih =>
    intro n x hx h0 h
    exact H_kernel hx h0 (ih (supp_H hx) (H_wall x) h)

/-- **Aperiodicity.** The depth-one column of a nonzero finite row with a white wall is not
eventually periodic. -/
theorem col_not_eventually_periodic {W : Nat} {x : Row} (hx : WidthLE W x) (h0 : x 0 = false)
    (hne : ∃ k, x k = true) : ¬ ∃ U q, 1 ≤ q ∧ ∀ u, U ≤ u → col x (u + q) = col x u := by
  rintro ⟨U, q, hq, hper⟩
  have hw := col_periodic_white (supp_of_width hx) h0 hq hper
  have hy : ∀ t, col (iter H U x) t = false := by
    intro t
    show iter H t (iter H U x) 1 = false
    rw [← iter_add]
    exact hw (U + t) (by omega)
  have hy0 : ∀ k, iter H U x k = false := by
    intro k
    cases k with
    | zero => exact iter_H_wall h0 U
    | succ k => exact col_inj _ hy (k + 1) (by omega)
  obtain ⟨k, hk⟩ := hne
  rw [iter_H_kernel U (supp_of_width hx) h0 hy0 k] at hk
  exact absurd hk (by decide)

/-- **Aperiodicity of immortal rows.** For an immortal finite row with a white wall, the odd-time
column word is not eventually periodic. -/
theorem immortal_odd_word_not_eventually_periodic {W : Nat} {x : Row} (hx : WidthLE W x)
    (h0 : x 0 = false) (himm : Immortal x) :
    ¬ ∃ N p, 1 ≤ p ∧ ∀ t, N ≤ t → col x (2 * (t + p) + 1) = col x (2 * t + 1) := by
  rintro ⟨N, p, hp, hper⟩
  have hfull : ∀ u, 2 * N ≤ u → col x (u + 2 * p) = col x u := by
    intro u hu
    obtain ⟨t, rfl | rfl⟩ : ∃ t, u = 2 * t ∨ u = 2 * t + 1 := ⟨u / 2, by omega⟩
    · rw [show 2 * t + 2 * p = 2 * (t + p) by omega, himm, himm]
    · rw [show 2 * t + 1 + 2 * p = 2 * (t + p) + 1 by omega]
      exact hper t (by omega)
  have e := col_periodic_white (supp_of_width hx) h0 (show 1 ≤ 2 * p by omega) hfull (2 * N)
    (Nat.le_refl _)
  rw [himm N] at e
  exact absurd e (by decide)

/-! ## Counting -/

/-- A decision procedure for the immortality of `rowOf n` at width `W` (see `immortalB_iff`). -/
def immortalB (W n : Nat) : Bool := decide (BitFamUpTo (W / 4 + 1) (rowOf n))

theorem immortalB_iff {W n : Nat} (hn : n < 2 ^ W) : immortalB W n = true ↔ Immortal (rowOf n) := by
  rw [immortal_rowOf_iff hn]
  exact ⟨of_decide_eq_true, decide_eq_true⟩

/-- For `2 ≤ W ≤ 12`, exactly `2 ^ (W / 2 - 1)` of the rows `rowOf n` with `n < 2 ^ W` are
immortal (with `immortalB_iff`). -/
theorem immortal_count_le_twelve :
    ∀ W, W < 13 → 2 ≤ W → ((List.range (2 ^ W)).filter (immortalB W)).length = 2 ^ (W / 2 - 1) := by
  decide +kernel

/-- For `W ≤ 1`, none of the rows `rowOf n` with `n < 2 ^ W` is immortal. -/
theorem immortal_count_le_one :
    ∀ W, W < 2 → ((List.range (2 ^ W)).filter (immortalB W)).length = 0 := by
  decide +kernel

/-! ## The family as an affine space -/

/-- The bit family by its free parameters, interleaved by depth: `v (2 j - 2) = r j` (depth
`4 j`) and `v (2 j - 1) = p j` (depths `4 j - 2`, `4 j - 1`, `4 j + 1`, `4 j + 2`) for `j ≥ 1`. -/
def paramRow (v : Row) : Row :=
  famRow (fun j => if j = 0 then true else v (2 * j - 1))
    (fun j => if j = 0 then false else v (2 * j - 2))

theorem paramRow_even (v : Row) (j : Nat) : paramRow v (4 * (j + 1)) = v (2 * j) := by
  unfold paramRow
  rw [famRow_zero_mod]
  show (if j + 1 = 0 then false else v (2 * (j + 1) - 2)) = v (2 * j)
  rw [ite_eq_right (show ¬ j + 1 = 0 by omega), show 2 * (j + 1) - 2 = 2 * j by omega]

theorem paramRow_odd (v : Row) (j : Nat) : paramRow v (4 * (j + 1) + 1) = v (2 * j + 1) := by
  unfold paramRow
  rw [famRow_one_mod]
  show (if j + 1 = 0 then true else v (2 * (j + 1) - 1)) = v (2 * j + 1)
  rw [ite_eq_right (show ¬ j + 1 = 0 by omega), show 2 * (j + 1) - 1 = 2 * j + 1 by omega]

/-- Distinct parameters give distinct rows. -/
theorem paramRow_inj {v v' : Row} (h : paramRow v = paramRow v') : v = v' := by
  funext i
  obtain ⟨j, rfl | rfl⟩ : ∃ j, i = 2 * j ∨ i = 2 * j + 1 := ⟨i / 2, by omega⟩
  · have e1 := paramRow_even v j
    have e2 := paramRow_even v' j
    rw [h] at e1
    exact e1.symm.trans e2
  · have e1 := paramRow_odd v j
    have e2 := paramRow_odd v' j
    rw [h] at e1
    exact e1.symm.trans e2

/-- Parameters supported below `W / 2 - 1` give rows of width at most `W`. -/
theorem paramRow_width {W : Nat} {v : Row} (hW : 2 ≤ W) (hv : Supp (W / 2 - 1) v) :
    WidthLE W (paramRow v) := by
  intro k hk
  unfold paramRow
  obtain ⟨i, rfl | rfl | rfl | rfl⟩ := cases_four k
  · rw [famRow_zero_mod]
    show (if i = 0 then false else v (2 * i - 2)) = false
    split
    · rfl
    · exact hv _ (by omega)
  · rw [famRow_one_mod]
    show (if i = 0 then true else v (2 * i - 1)) = false
    split
    · exact absurd hk (by omega)
    · exact hv _ (by omega)
  · rw [famRow_two_mod]
    show xor (if i = 0 then true else v (2 * i - 1)) (if i + 1 = 0 then true else v (2 * (i + 1) - 1))
      = false
    rw [ite_eq_right (show ¬ i + 1 = 0 by omega), hv (2 * (i + 1) - 1) (by omega)]
    split
    · exact absurd hk (by omega)
    · rw [hv _ (by omega)]
      rfl
  · rw [famRow_three_mod]
    show (if i + 1 = 0 then true else v (2 * (i + 1) - 1)) = false
    rw [ite_eq_right (show ¬ i + 1 = 0 by omega)]
    exact hv _ (by omega)

/-- **The count.** For `W ≥ 2`, the immortal rows of width at most `W` with a white wall are
exactly the rows `paramRow v` with `v` supported below `W / 2 - 1`; with `paramRow_inj` and
`paramRow_width` this is a bijection with the `2 ^ (W / 2 - 1)` Boolean words of length
`W / 2 - 1`. -/
theorem immortal_iff_param {W : Nat} {x : Row} (hW : 2 ≤ W) (hx : WidthLE W x)
    (h0 : x 0 = false) : Immortal x ↔ ∃ v, Supp (W / 2 - 1) v ∧ x = paramRow v := by
  rw [immortal_iff_famRow hx h0]
  constructor
  · rintro ⟨p, r, hp, hr, rfl⟩
    refine ⟨fun i => if i % 2 = 0 then r (i / 2 + 1) else p ((i + 1) / 2), ?_, ?_⟩
    · intro i hi
      show (if i % 2 = 0 then r (i / 2 + 1) else p ((i + 1) / 2)) = false
      split
      · have e := hx (4 * (i / 2 + 1)) (by omega)
        rw [famRow_zero_mod] at e
        exact e
      · have e3 := hx (4 * ((i + 1) / 2) + 3) (by omega)
        rw [famRow_three_mod] at e3
        have e2 := hx (4 * ((i + 1) / 2) + 2) (by omega)
        rw [famRow_two_mod, e3, Bool.xor_false] at e2
        exact e2
    · unfold paramRow
      congr 1
      · funext j
        cases j with
        | zero => exact hp
        | succ j =>
          show p (j + 1) = (if j + 1 = 0 then true else
            (if (2 * (j + 1) - 1) % 2 = 0 then r ((2 * (j + 1) - 1) / 2 + 1)
              else p ((2 * (j + 1) - 1 + 1) / 2)))
          rw [ite_eq_right (show ¬ j + 1 = 0 by omega),
            ite_eq_right (show ¬ (2 * (j + 1) - 1) % 2 = 0 by omega),
            show (2 * (j + 1) - 1 + 1) / 2 = j + 1 by omega]
      · funext j
        cases j with
        | zero => exact hr
        | succ j =>
          show r (j + 1) = (if j + 1 = 0 then false else
            (if (2 * (j + 1) - 2) % 2 = 0 then r ((2 * (j + 1) - 2) / 2 + 1)
              else p ((2 * (j + 1) - 2 + 1) / 2)))
          rw [ite_eq_right (show ¬ j + 1 = 0 by omega),
            ite_eq_left (show (2 * (j + 1) - 2) % 2 = 0 by omega),
            show (2 * (j + 1) - 2) / 2 + 1 = j + 1 by omega]
  · rintro ⟨v, _, rfl⟩
    exact ⟨_, _, rfl, rfl, rfl⟩

end Rule30Submission
