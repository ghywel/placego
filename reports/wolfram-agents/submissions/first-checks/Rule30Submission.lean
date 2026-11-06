import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30ZeroBoundary

/-!
# The first composite check: a pair law, and two of every three checks are not near constant

Take a free word `f` with `n` bits, and let `Theta f` be the row that keeps column `-1` black at every
even step. The first check past the free range reads `check n l = Theta (word l) (2 n + 1)`. Write
`ones n` for the number of words of length `n` on which it is black.

Everything here is exact counting on the uniform free cube, with all even pins black.

* `two_tick`: two ticks of a row with a white wall, as one Boolean identity.
* `pair_count`: the check of a word differs from the check of its shift on exactly
  `2 ^ m + ones m` of the words of length `m + 2`. So the correlation of two consecutive checks is
  known exactly, in terms of the check two places back.
* `adjacent`, `distance_two`: with `gap n` the smaller of `ones n` and `2 ^ n - ones n`, the pair law
  and the elementary bounds on two overlapping sets give two linear inequalities between gaps.
* `two_of_three`: so among any three consecutive `n ≥ 2` at most one has `40 * gap n < 2 ^ n`.
* `first_check_count`: the rows of width at most `2 n` that are black at column `-1` at every even tick
  through `2 n` number exactly `2 ^ n - ones n`.
* `first_check_balanced`: so for at least two of any three consecutive `n ≥ 2`, the share of the
  `2 ^ n` rows that pass the first check past the free range lies in `[1/40, 39/40]`.

This bounds the first check only. From the second check on the fresh bits behind `pair_count` are
pinned, so these bounds do not multiply. Nothing here proves `Q01`, and Problems 1 to 3 stay open.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata Rule30ZeroBoundary

/-! ### Sums over the cube -/

/-- The free word of a bit list, white past its end. -/
def word (l : List Bool) (s : Nat) : Bool := l.getD s false

/-- The sum of `F` over all bit lists of length `n`. -/
def cubeSum : Nat → (List Bool → Nat) → Nat
  | 0, F => F []
  | n + 1, F => cubeSum n (fun l => F (false :: l)) + cubeSum n (fun l => F (true :: l))

theorem cubeSum_congr {n : Nat} {F G : List Bool → Nat} (h : ∀ l, l.length = n → F l = G l) :
    cubeSum n F = cubeSum n G := by
  induction n generalizing F G with
  | zero => exact h [] rfl
  | succ n ih =>
    show cubeSum n _ + cubeSum n _ = cubeSum n _ + cubeSum n _
    rw [ih (fun l hl => h (false :: l) (by simp [hl])), ih (fun l hl => h (true :: l) (by simp [hl]))]

theorem cubeSum_le {n : Nat} {F G : List Bool → Nat} (h : ∀ l, F l ≤ G l) :
    cubeSum n F ≤ cubeSum n G := by
  induction n generalizing F G with
  | zero => exact h []
  | succ n ih =>
    show cubeSum n _ + cubeSum n _ ≤ cubeSum n _ + cubeSum n _
    exact Nat.add_le_add (ih fun l => h _) (ih fun l => h _)

theorem cubeSum_add (n : Nat) (F G : List Bool → Nat) :
    cubeSum n (fun l => F l + G l) = cubeSum n F + cubeSum n G := by
  induction n generalizing F G with
  | zero => rfl
  | succ n ih =>
    show cubeSum n _ + cubeSum n _ = (cubeSum n _ + cubeSum n _) + (cubeSum n _ + cubeSum n _)
    rw [ih, ih]
    omega

theorem cubeSum_const (n c : Nat) : cubeSum n (fun _ => c) = 2 ^ n * c := by
  induction n with
  | zero => show c = 2 ^ 0 * c; omega
  | succ n ih =>
    show cubeSum n _ + cubeSum n _ = _
    rw [ih, Nat.pow_succ]
    generalize 2 ^ n = N
    rw [Nat.mul_comm N 2, Nat.mul_assoc]
    omega

theorem cubeSum_snoc (n : Nat) (F : List Bool → Nat) :
    cubeSum (n + 1) F = cubeSum n (fun l => F (l ++ [false]) + F (l ++ [true])) := by
  induction n generalizing F with
  | zero => rfl
  | succ n ih =>
    show cubeSum (n + 1) _ + cubeSum (n + 1) _ = cubeSum (n + 1) _
    rw [ih, ih]
    rfl

/-! ### The checks -/

/-- The first check past the free range of a word of length `n`. -/
def check (n : Nat) (l : List Bool) : Bool := Theta (word l) (2 * n + 1)

/-- The number of words of length `n` on which the check is black. -/
def ones (n : Nat) : Nat := cubeSum n (fun l => (check n l).toNat)

/-- The number of words of length `n + 1` on which the check differs from the check of the shift. -/
def flips (n : Nat) : Nat :=
  cubeSum (n + 1) (fun l => (xor (check (n + 1) l) (check n l.tail)).toNat)

/-- The smaller of the two sides of the check. -/
def gap (n : Nat) : Nat := min (ones n) (2 ^ n - ones n)

theorem ones_le (n : Nat) : ones n ≤ 2 ^ n := by
  have h : cubeSum n (fun l => (check n l).toNat) ≤ cubeSum n (fun _ => 1) :=
    cubeSum_le fun l => by cases check n l <;> decide
  rw [cubeSum_const] at h
  simpa [ones] using h

theorem shifted_sum (n : Nat) :
    cubeSum (n + 1) (fun l => (check n l.tail).toNat) = 2 * ones n := by
  show cubeSum n _ + cubeSum n _ = _
  simp only [List.tail_cons]
  unfold ones
  omega

/-- Two sets inside the cube, and their symmetric difference. -/
theorem overlap (n : Nat) :
    ones (n + 1) ≤ 2 * ones n + flips n ∧ 2 * ones n ≤ ones (n + 1) + flips n ∧
      flips n ≤ ones (n + 1) + 2 * ones n ∧
      flips n + (ones (n + 1) + 2 * ones n) ≤ 2 ^ (n + 1) * 2 := by
  have hs := shifted_sum n
  let X : List Bool → Nat := fun l => (check (n + 1) l).toNat
  let Y : List Bool → Nat := fun l => (check n l.tail).toNat
  let D : List Bool → Nat := fun l => (xor (check (n + 1) l) (check n l.tail)).toNat
  have hX : cubeSum (n + 1) X = ones (n + 1) := rfl
  have hY : cubeSum (n + 1) Y = 2 * ones n := hs
  have hD : cubeSum (n + 1) D = flips n := rfl
  have h1 : cubeSum (n + 1) X ≤ cubeSum (n + 1) (fun l => Y l + D l) :=
    cubeSum_le fun l => by
      show (check (n + 1) l).toNat ≤ (check n l.tail).toNat + (xor (check (n + 1) l) (check n l.tail)).toNat
      cases check (n + 1) l <;> cases check n l.tail <;> decide
  have h2 : cubeSum (n + 1) Y ≤ cubeSum (n + 1) (fun l => X l + D l) :=
    cubeSum_le fun l => by
      show (check n l.tail).toNat ≤ (check (n + 1) l).toNat + (xor (check (n + 1) l) (check n l.tail)).toNat
      cases check (n + 1) l <;> cases check n l.tail <;> decide
  have h3 : cubeSum (n + 1) D ≤ cubeSum (n + 1) (fun l => X l + Y l) :=
    cubeSum_le fun l => by
      show (xor (check (n + 1) l) (check n l.tail)).toNat ≤ (check (n + 1) l).toNat + (check n l.tail).toNat
      cases check (n + 1) l <;> cases check n l.tail <;> decide
  have h4 : cubeSum (n + 1) (fun l => D l + (X l + Y l)) ≤ cubeSum (n + 1) (fun _ => 2) :=
    cubeSum_le fun l => by
      show (xor (check (n + 1) l) (check n l.tail)).toNat + ((check (n + 1) l).toNat + (check n l.tail).toNat) ≤ 2
      cases check (n + 1) l <;> cases check n l.tail <;> decide
  rw [cubeSum_add] at h1 h2 h3
  rw [cubeSum_add, cubeSum_add, cubeSum_const] at h4
  omega

/-! ### Two ticks -/

/-- **Two ticks of a row with a white wall.** -/
theorem two_tick (L : Nat → Bool) (j : Nat) :
    zrow L 2 (j + 2) = xor (zrow L 0 (j + 4))
      ((zrow L 0 (j + 1) || zrow L 0 j) && !(xor (zrow L 0 (j + 3)) (zrow L 0 (j + 2)))) := by
  have h : zrow L 2 (j + 2) = xor (zrow L 1 (j + 3)) (zrow L 1 (j + 2) || zrow L 1 (j + 1)) :=
    zrow_succ L 1 (j + 1)
  have h1 : zrow L 1 (j + 1) = xor (zrow L 0 (j + 2)) (zrow L 0 (j + 1) || zrow L 0 j) :=
    zrow_succ L 0 j
  have h2 : zrow L 1 (j + 2) = xor (zrow L 0 (j + 3)) (zrow L 0 (j + 2) || zrow L 0 (j + 1)) :=
    zrow_succ L 0 (j + 1)
  have h3 : zrow L 1 (j + 3) = xor (zrow L 0 (j + 4)) (zrow L 0 (j + 3) || zrow L 0 (j + 2)) :=
    zrow_succ L 0 (j + 2)
  rw [h, h1, h2, h3]
  generalize zrow L 0 j = a
  generalize zrow L 0 (j + 1) = b
  generalize zrow L 0 (j + 2) = c
  generalize zrow L 0 (j + 3) = d
  generalize zrow L 0 (j + 4) = e
  revert a b c d e
  decide

/-- The check of a shifted word, against the check of the word. -/
theorem check_xor (m : Nat) (f : Nat → Bool) :
    Theta (fun s => f (s + 1)) (2 * m + 3) = xor (Theta f (2 * m + 5))
      ((Theta f (2 * m + 2) || Theta f (2 * m + 1)) &&
        !(xor (Theta f (2 * m + 4)) (Theta f (2 * m + 3)))) := by
  have h := two_tick (Theta f) (2 * m + 1)
  rw [two_step_shift f, zrow_zero_self (Theta_wall f)] at h
  exact h

/-! ### The pair law -/

theorem word_tail (l : List Bool) : word l.tail = fun s => word l (s + 1) := by
  funext s
  cases l with
  | nil => rfl
  | cons b l => rfl

theorem word_lt (p q : List Bool) {s : Nat} (hs : s < p.length) : word (p ++ q) s = word p s := by
  unfold word
  rw [List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD, List.getElem?_append_left hs]

theorem word_ge (p q : List Bool) (s : Nat) : word (p ++ q) (p.length + s) = word q s := by
  unfold word
  rw [List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD,
    List.getElem?_append_right (by omega), show p.length + s - p.length = s by omega]

theorem four_bools (c u v0 v1 w0 w1 : Bool) :
    ((u || c) && !(xor w0 v0)).toNat + ((u || c) && !(xor (!w0) v0)).toNat +
      ((((!u) || c) && !(xor w1 v1)).toNat + (((!u) || c) && !(xor (!w1) v1)).toNat) =
      1 + c.toNat := by
  revert c u v0 v1 w0 w1
  decide

theorem not_of_xor {a b : Bool} (h : xor a b = true) : b = !a := by
  revert h
  cases a <;> cases b <;> decide

/-- The four completions of a prefix by two bits. -/
theorem four_sum (p : List Bool) :
    (xor (check (p.length + 2) (p ++ [false] ++ [false])) (check (p.length + 1) (p ++ [false] ++ [false]).tail)).toNat +
      (xor (check (p.length + 2) (p ++ [false] ++ [true])) (check (p.length + 1) (p ++ [false] ++ [true]).tail)).toNat +
      ((xor (check (p.length + 2) (p ++ [true] ++ [false])) (check (p.length + 1) (p ++ [true] ++ [false]).tail)).toNat +
       (xor (check (p.length + 2) (p ++ [true] ++ [true])) (check (p.length + 1) (p ++ [true] ++ [true]).tail)).toNat) =
      1 + (check p.length p).toNat := by
  have key : ∀ x y : Bool,
      xor (check (p.length + 2) (p ++ [x] ++ [y])) (check (p.length + 1) (p ++ [x] ++ [y]).tail) =
        ((Theta (word (p ++ [x] ++ [y])) (2 * p.length + 2) ||
            Theta (word (p ++ [x] ++ [y])) (2 * p.length + 1)) &&
          !(xor (Theta (word (p ++ [x] ++ [y])) (2 * p.length + 4))
            (Theta (word (p ++ [x] ++ [y])) (2 * p.length + 3)))) := by
    intro x y
    have h := check_xor p.length (word (p ++ [x] ++ [y]))
    show xor (Theta (word (p ++ [x] ++ [y])) (2 * p.length + 5))
      (Theta (word (p ++ [x] ++ [y]).tail) (2 * p.length + 3)) = _
    rw [word_tail, h]
    cases Theta (word (p ++ [x] ++ [y])) (2 * p.length + 5) <;> simp
  have agree : ∀ x y : Bool, ∀ s, s < p.length → word (p ++ [x] ++ [y]) s = word p s := by
    intro x y s hs
    rw [List.append_assoc]
    exact word_lt p _ hs
  have agree1 : ∀ x y y' : Bool, ∀ s, s ≤ p.length →
      word (p ++ [x] ++ [y]) s = word (p ++ [x] ++ [y']) s := by
    intro x y y' s hs
    have hl : (p ++ [x]).length = p.length + 1 := by simp
    rw [word_lt (p ++ [x]) [y] (by omega), word_lt (p ++ [x]) [y'] (by omega)]
  have atx : ∀ x y : Bool, word (p ++ [x] ++ [y]) p.length = x := by
    intro x y
    rw [List.append_assoc]
    exact word_ge p ([x] ++ [y]) 0
  have aty : ∀ x y : Bool, word (p ++ [x] ++ [y]) (p.length + 1) = y := by
    intro x y
    have h := word_ge (p ++ [x]) [y] 0
    have hl : (p ++ [x]).length = p.length + 1 := by simp
    rw [hl] at h
    exact h
  have b2 : ∀ x y : Bool, Theta (word (p ++ [x] ++ [y])) (2 * p.length + 1) = check p.length p := by
    intro x y
    exact tri_odd _ _ p.length (agree x y)
  have u0 : ∀ x y : Bool, Theta (word (p ++ [x] ++ [y])) (2 * p.length + 2) =
      Theta (word (p ++ [x] ++ [false])) (2 * p.length + 2) := by
    intro x y
    exact Theta_dep _ _ _ (fun s hs => agree1 x y false s (by omega))
  have v0 : ∀ x y : Bool, Theta (word (p ++ [x] ++ [y])) (2 * p.length + 3) =
      Theta (word (p ++ [x] ++ [false])) (2 * p.length + 3) := by
    intro x y
    exact Theta_dep _ _ _ (fun s hs => agree1 x y false s (by omega))
  have flipU : Theta (word (p ++ [true] ++ [false])) (2 * p.length + 2) =
      !Theta (word (p ++ [false] ++ [false])) (2 * p.length + 2) := by
    apply not_of_xor
    rw [tri_even _ _ p.length (fun s hs => by rw [agree _ _ s hs, agree _ _ s hs]), atx, atx]
    rfl
  have flipW : ∀ x : Bool, Theta (word (p ++ [x] ++ [true])) (2 * p.length + 4) =
      !Theta (word (p ++ [x] ++ [false])) (2 * p.length + 4) := by
    intro x
    apply not_of_xor
    rw [show 2 * p.length + 4 = 2 * (p.length + 1) + 2 by omega,
      tri_even _ _ (p.length + 1) (fun s hs => agree1 x false true s (by omega)), aty, aty]
    rfl
  rw [key, key, key, key, b2, b2, b2, b2, u0 false true, u0 true false, u0 true true, flipU,
    v0 false true, v0 true true, flipW false, flipW true]
  exact four_bools _ _ _ _ _ _

/-- **The pair law.** The check differs from the check of the shift on exactly `2 ^ m + ones m`
of the words of length `m + 2`. -/
theorem pair_count (m : Nat) : flips (m + 1) = 2 ^ m + ones m := by
  unfold flips
  rw [cubeSum_snoc, cubeSum_snoc]
  have h : cubeSum m (fun l =>
      (xor (check (m + 1 + 1) (l ++ [false] ++ [false])) (check (m + 1) (l ++ [false] ++ [false]).tail)).toNat +
      (xor (check (m + 1 + 1) (l ++ [false] ++ [true])) (check (m + 1) (l ++ [false] ++ [true]).tail)).toNat +
      ((xor (check (m + 1 + 1) (l ++ [true] ++ [false])) (check (m + 1) (l ++ [true] ++ [false]).tail)).toNat +
       (xor (check (m + 1 + 1) (l ++ [true] ++ [true])) (check (m + 1) (l ++ [true] ++ [true]).tail)).toNat)) =
      cubeSum m (fun l => 1 + (check m l).toNat) := by
    apply cubeSum_congr
    intro l hl
    subst hl
    exact four_sum l
  refine h.trans ?_
  rw [cubeSum_add, cubeSum_const, Nat.mul_one]
  rfl

/-! ### The inequalities -/

theorem pow_one_more (m : Nat) : 2 ^ (m + 1) = 2 * 2 ^ m := Nat.pow_succ'

theorem pow_two_more (m : Nat) : 2 ^ (m + 2) = 4 * 2 ^ m := by
  rw [pow_one_more (m + 1), pow_one_more m]; omega

theorem pow_three_more (m : Nat) : 2 ^ (m + 3) = 8 * 2 ^ m := by
  rw [pow_one_more (m + 2), pow_two_more m]; omega

theorem pow_four_more (m : Nat) : 2 ^ (m + 4) = 16 * 2 ^ m := by
  rw [pow_one_more (m + 3), pow_three_more m]; omega

/-- `overlap` with the pair law substituted, at indices `k + 1` and `k + 2`. -/
theorem overlap_pair (k : Nat) :
    ones (k + 2) ≤ 2 * ones (k + 1) + (2 ^ k + ones k) ∧
      2 * ones (k + 1) ≤ ones (k + 2) + (2 ^ k + ones k) ∧
      2 ^ k + ones k ≤ ones (k + 2) + 2 * ones (k + 1) ∧
      2 ^ k + ones k + (ones (k + 2) + 2 * ones (k + 1)) ≤ 8 * 2 ^ k := by
  have h := overlap (k + 1)
  rw [pair_count k, show 2 ^ (k + 1 + 1) * 2 = 8 * 2 ^ k by rw [pow_two_more k]; omega] at h
  exact h

theorem adjacent (m : Nat) : 2 ^ m + ones m ≤ gap (m + 2) + 2 * gap (m + 1) := by
  obtain ⟨a1, a2, a3, a4⟩ := overlap_pair m
  have b0 := ones_le m
  have b1 := ones_le (m + 1)
  have b2 := ones_le (m + 2)
  unfold gap
  rw [pow_one_more m] at b1 ⊢
  rw [pow_two_more m] at b2 ⊢
  generalize 2 ^ m = N at *
  omega

/-- **The distance-two inequality.** -/
theorem distance_two (m : Nat) : 2 ^ (m + 2) ≤ 4 * gap (m + 4) + 24 * gap (m + 2) := by
  obtain ⟨a1, a2, a3, a4⟩ : ones (m + 4) ≤ 2 * ones (m + 3) + (2 ^ (m + 2) + ones (m + 2)) ∧
      2 * ones (m + 3) ≤ ones (m + 4) + (2 ^ (m + 2) + ones (m + 2)) ∧
      2 ^ (m + 2) + ones (m + 2) ≤ ones (m + 4) + 2 * ones (m + 3) ∧
      2 ^ (m + 2) + ones (m + 2) + (ones (m + 4) + 2 * ones (m + 3)) ≤ 8 * 2 ^ (m + 2) :=
    overlap_pair (m + 2)
  obtain ⟨c1, c2, c3, c4⟩ : ones (m + 3) ≤ 2 * ones (m + 2) + (2 ^ (m + 1) + ones (m + 1)) ∧
      2 * ones (m + 2) ≤ ones (m + 3) + (2 ^ (m + 1) + ones (m + 1)) ∧
      2 ^ (m + 1) + ones (m + 1) ≤ ones (m + 3) + 2 * ones (m + 2) ∧
      2 ^ (m + 1) + ones (m + 1) + (ones (m + 3) + 2 * ones (m + 2)) ≤ 8 * 2 ^ (m + 1) :=
    overlap_pair (m + 1)
  obtain ⟨d1, d2, d3, d4⟩ := overlap_pair m
  have b0 := ones_le m
  have b1 := ones_le (m + 1)
  have b2 := ones_le (m + 2)
  have b3 := ones_le (m + 3)
  have b4 := ones_le (m + 4)
  unfold gap
  rw [pow_one_more m] at b1 c1 c2 c3 c4
  rw [pow_two_more m] at b2 a1 a2 a3 a4 ⊢
  rw [pow_three_more m] at b3
  rw [pow_four_more m] at b4 ⊢
  generalize 2 ^ m = N at *
  omega

/-- A check is *near constant* when its smaller side is under one fortieth. -/
def Bad (n : Nat) : Prop := 40 * gap n < 2 ^ n

/-- Two adjacent checks are not both near constant. -/
theorem not_both_bad_adjacent (m : Nat) : ¬ (Bad (m + 2) ∧ Bad (m + 3)) := by
  rintro ⟨h1, h2⟩
  have h : 2 ^ (m + 1) + ones (m + 1) ≤ gap (m + 3) + 2 * gap (m + 2) := adjacent (m + 1)
  unfold Bad at h1 h2
  rw [pow_one_more m] at h
  rw [pow_two_more m] at h1
  rw [pow_three_more m] at h2
  generalize 2 ^ m = N at *
  omega

/-- Two checks at distance two are not both near constant. -/
theorem not_both_bad_two (m : Nat) : ¬ (Bad (m + 2) ∧ Bad (m + 4)) := by
  rintro ⟨h1, h2⟩
  have h := distance_two m
  unfold Bad at h1 h2
  rw [pow_two_more m] at h h1
  rw [pow_four_more m] at h2
  generalize 2 ^ m = N at *
  omega

/-- **At most one of any three consecutive checks from `2` on is near constant.** -/
theorem two_of_three (m : Nat) :
    ¬ (Bad (m + 2) ∧ Bad (m + 3)) ∧ ¬ (Bad (m + 3) ∧ Bad (m + 4)) ∧ ¬ (Bad (m + 2) ∧ Bad (m + 4)) :=
  ⟨not_both_bad_adjacent m, not_both_bad_adjacent (m + 1), not_both_bad_two m⟩

/-! ### The survivor count -/

/-- The rows given by bit lists of length `n` beyond `l` whose last extension by a white cell passes
every even check. -/
def lastWhite : Nat → List Bool → Nat
  | 0, l => if ok (l ++ [false]) then 1 else 0
  | n + 1, l => lastWhite n (l ++ [false]) + lastWhite n (l ++ [true])

/-- The rows of width at most `2 n` black at column `-1` at every even tick through `2 n`. -/
def firstCheck (n : Nat) : Nat := lastWhite (2 * n) []

/-- The first `k` cells of a row, as a list. -/
def rowList (f : Nat → Bool) : Nat → List Bool
  | 0 => []
  | k + 1 => rowList f k ++ [Theta f (k + 1)]

theorem rowList_length (f : Nat → Bool) (k : Nat) : (rowList f k).length = k := by
  induction k with
  | zero => rfl
  | succ k ih => simp [rowList, ih]

theorem toRow_rowList (f : Nat → Bool) (k i : Nat) (hi : 1 ≤ i) (hk : i ≤ k) :
    toRow (rowList f k) i = Theta f i := by
  induction k with
  | zero => omega
  | succ k ih =>
    show toRow (rowList f k ++ [Theta f (k + 1)]) i = _
    by_cases h : i ≤ k
    · rw [toRow_snoc_le _ _ i (by rw [rowList_length]; exact h)]
      exact ih h
    · have e : i = (rowList f k).length + 1 := by rw [rowList_length]; omega
      rw [e, toRow_snoc_last, rowList_length]

theorem ok_rowList (f : Nat → Bool) (k : Nat) : ok (rowList f k) := by
  intro t ht he
  rw [rowList_length] at ht
  rw [zrow_light_cone (L' := Theta f) t 1 (fun i h1 h2 => toRow_rowList f k i h1 (by omega))]
  have := Theta_inX f (t / 2)
  rwa [show 2 * (t / 2) = t by omega] at this

theorem rowList_congr (f g : Nat → Bool) (k : Nat) (h : ∀ i, 1 ≤ i → i ≤ k → Theta f i = Theta g i) :
    rowList f k = rowList g k := by
  induction k with
  | zero => rfl
  | succ k ih =>
    show rowList f k ++ _ = rowList g k ++ _
    rw [ih (fun i h1 h2 => h i h1 (by omega)), h (k + 1) (by omega) (by omega)]

theorem lastWhite_of_not_ok {l : List Bool} (h : ¬ ok l) : ∀ n, lastWhite n l = 0 := by
  intro n
  induction n generalizing l with
  | zero =>
    show (if ok (l ++ [false]) then 1 else 0) = 0
    rw [ite_eq_right (fun hk => h (ok_of_snoc l false hk))]
  | succ n ih =>
    show lastWhite n _ + lastWhite n _ = 0
    rw [ih (fun hk => h (ok_of_snoc l false hk)), ih (fun hk => h (ok_of_snoc l true hk))]

/-- At an even length, exactly one of the two next cells keeps the row alive, and it is the row's own. -/
theorem wrong_cell_dead (f : Nat → Bool) (j : Nat) :
    ¬ ok (rowList f (2 * j) ++ [!Theta f (2 * j + 1)]) := by
  intro h
  have hl : (rowList f (2 * j)).length = 2 * j := rowList_length f (2 * j)
  have hb := ((ok_snoc _ _).mp h).2 (by rw [hl]; omega)
  have hg := ((ok_snoc (rowList f (2 * j)) (Theta f (2 * j + 1))).mp (ok_rowList f (2 * j + 1))).2
    (by rw [hl]; omega)
  have hp := snoc_pivot (rowList f (2 * j))
  cases hc : Theta f (2 * j + 1) with
  | false =>
    rw [hc] at hb hg
    have hb' : zrow (toRow (rowList f (2 * j) ++ [true])) (rowList f (2 * j)).length 1 = true := hb
    rw [hp, hg] at hb'
    exact absurd hb' (by decide)
  | true =>
    rw [hc] at hb hg
    have hb' : zrow (toRow (rowList f (2 * j) ++ [false])) (rowList f (2 * j)).length 1 = true := hb
    rw [hp, hb'] at hg
    exact absurd hg (by decide)

theorem rowList_cell (f : Nat → Bool) (j : Nat) :
    rowList f (2 * j) ++ [Theta f (2 * j + 1)] = rowList f (2 * j + 1) := rfl

theorem lastWhite_row (r : Nat) : ∀ p : List Bool,
    lastWhite (2 * r) (rowList (word p) (2 * p.length)) =
      cubeSum r (fun q => (!check (p.length + r) (p ++ q)).toNat) := by
  induction r with
  | zero =>
    intro p
    show (if ok (rowList (word p) (2 * p.length) ++ [false]) then 1 else 0) =
      (!check (p.length + 0) (p ++ [])).toNat
    have hc : check (p.length + 0) (p ++ []) = Theta (word p) (2 * p.length + 1) := by
      rw [List.append_nil]; rfl
    rw [hc]
    cases hb : Theta (word p) (2 * p.length + 1) with
    | false =>
      have h : ok (rowList (word p) (2 * p.length) ++ [false]) := by
        have := ok_rowList (word p) (2 * p.length + 1)
        rwa [← rowList_cell, hb] at this
      rw [ite_eq_left h]
      rfl
    | true =>
      have h := wrong_cell_dead (word p) p.length
      rw [hb] at h
      have h' : ¬ ok (rowList (word p) (2 * p.length) ++ [false]) := h
      rw [ite_eq_right h']
      rfl
  | succ r ih =>
    intro p
    have hstep : lastWhite (2 * (r + 1)) (rowList (word p) (2 * p.length)) =
        lastWhite (2 * r + 1) (rowList (word p) (2 * p.length) ++ [false]) +
          lastWhite (2 * r + 1) (rowList (word p) (2 * p.length) ++ [true]) := rfl
    have hext : ∀ x : Bool, rowList (word p) (2 * p.length + 1) =
        rowList (word (p ++ [x])) (2 * p.length + 1) := by
      intro x
      apply rowList_congr
      intro i _ hi
      exact Theta_dep _ _ _ (fun s hs => (word_lt p [x] (by omega)).symm)
    have hflip : Theta (word (p ++ [true])) (2 * p.length + 2) =
        !Theta (word (p ++ [false])) (2 * p.length + 2) := by
      apply not_of_xor
      rw [tri_even _ _ p.length (fun s hs => by rw [word_lt p _ hs, word_lt p _ hs])]
      have e : ∀ x : Bool, word (p ++ [x]) p.length = x := fun x => word_ge p [x] 0
      rw [e, e]
      rfl
    have hsucc : ∀ x : Bool, rowList (word (p ++ [x])) (2 * (p ++ [x]).length) =
        rowList (word p) (2 * p.length + 1) ++ [Theta (word (p ++ [x])) (2 * p.length + 2)] := by
      intro x
      have hl : 2 * (p ++ [x]).length = 2 * p.length + 1 + 1 := by simp; omega
      rw [hl, hext x]
      rfl
    have hih : ∀ x : Bool,
        lastWhite (2 * r) (rowList (word p) (2 * p.length + 1) ++ [Theta (word (p ++ [x])) (2 * p.length + 2)]) =
          cubeSum r (fun q => (!check (p.length + (r + 1)) (p ++ x :: q)).toNat) := by
      intro x
      rw [← hsucc x, ih (p ++ [x])]
      apply cubeSum_congr
      intro q _
      have hlen : (p ++ [x]).length + r = p.length + (r + 1) := by simp; omega
      rw [hlen, List.append_assoc]
      rfl
    have hright : lastWhite (2 * r + 1) (rowList (word p) (2 * p.length + 1)) =
        cubeSum (r + 1) (fun q => (!check (p.length + (r + 1)) (p ++ q)).toNat) := by
      show lastWhite (2 * r) (rowList (word p) (2 * p.length + 1) ++ [false]) +
          lastWhite (2 * r) (rowList (word p) (2 * p.length + 1) ++ [true]) =
        cubeSum r _ + cubeSum r _
      have h0 := hih false
      have h1 := hih true
      rw [hflip] at h1
      cases hb : Theta (word (p ++ [false])) (2 * p.length + 2) with
      | false =>
        rw [hb] at h0 h1
        have h1' : lastWhite (2 * r) (rowList (word p) (2 * p.length + 1) ++ [true]) = _ := h1
        rw [h0, h1']
      | true =>
        rw [hb] at h0 h1
        have h1' : lastWhite (2 * r) (rowList (word p) (2 * p.length + 1) ++ [false]) = _ := h1
        rw [h0, h1', Nat.add_comm]
    have hdead := wrong_cell_dead (word p) p.length
    cases hb : Theta (word p) (2 * p.length + 1) with
    | false =>
      rw [hb] at hdead
      have hd : ¬ ok (rowList (word p) (2 * p.length) ++ [true]) := hdead
      have e : rowList (word p) (2 * p.length + 1) = rowList (word p) (2 * p.length) ++ [false] := by
        rw [← rowList_cell, hb]
      rw [hstep, lastWhite_of_not_ok hd, Nat.add_zero]
      rw [e] at hright
      exact hright
    | true =>
      rw [hb] at hdead
      have hd : ¬ ok (rowList (word p) (2 * p.length) ++ [false]) := hdead
      have e : rowList (word p) (2 * p.length + 1) = rowList (word p) (2 * p.length) ++ [true] := by
        rw [← rowList_cell, hb]
      rw [hstep, lastWhite_of_not_ok hd, Nat.zero_add]
      rw [e] at hright
      exact hright

/-- **The first check, counted.** -/
theorem first_check_count (n : Nat) : firstCheck n + ones n = 2 ^ n := by
  have h := lastWhite_row n []
  have e : firstCheck n = cubeSum n (fun q => (!check n q).toNat) := by
    have h' : lastWhite (2 * n) (rowList (word []) (2 * ([] : List Bool).length)) =
        cubeSum n (fun q => (!check (([] : List Bool).length + n) ([] ++ q)).toNat) := h
    simp only [List.length_nil, Nat.mul_zero, Nat.zero_add, List.nil_append] at h'
    exact h'
  have s : cubeSum n (fun q => (!check n q).toNat + (check n q).toNat) = cubeSum n (fun _ => 1) :=
    cubeSum_congr fun l _ => by cases check n l <;> rfl
  rw [cubeSum_add, cubeSum_const] at s
  rw [e]
  unfold ones
  simpa using s

/-- **Balance.** A check that is not near constant passes between one fortieth and thirty-nine
fortieths of the rows. -/
theorem first_check_balanced {n : Nat} (h : ¬ Bad n) :
    2 ^ n ≤ 40 * firstCheck n ∧ 40 * firstCheck n ≤ 39 * 2 ^ n := by
  have hc := first_check_count n
  have hb := ones_le n
  unfold Bad gap at h
  generalize 2 ^ n = N at *
  omega

end Rule30Submission
