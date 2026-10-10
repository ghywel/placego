import Mathlib

/-!
# The shared part of entry 38's two-sided black-end proof (Local, 2026-10-10)

Rule 30, Theorem A, the strip of radius 6 (`inner`, `succSet`, `img`, `pre`, `word`, `full0`, `colConst`) and the
membership and window lemmas, from the parked BlackEnd38.lean (L525), without its six one-shot kernel checks (which
needed about 12 GB). gen_black_end38.py reads this file and writes BlackEnd38L.lean, the literal-stage proof (L553).
It compiles on its own in seconds and proves nothing about a particular q.
-/

set_option Elab.async false

namespace BlackEnd38

/-! ## Rule 30 and Theorem A (verbatim from TheoremA.lean, as in WhiteEnd.lean) -/

def step (x : ℤ → Bool) : ℤ → Bool := fun i => xor (x (i - 1)) (x i || x (i + 1))

def ev (x0 : ℤ → Bool) : ℕ → ℤ → Bool
  | 0 => x0
  | t + 1 => step (ev x0 t)

lemma edge (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (t : ℕ) :
    ev x0 t (e - t) = true ∧ ∀ j < e - t, ev x0 t j = false := by
  induction t with
  | zero => simpa using ⟨he, hl⟩
  | succ t ih =>
    obtain ⟨h1, h2⟩ := ih
    constructor
    · show xor (ev x0 t (e - ↑(t + 1) - 1)) (ev x0 t (e - ↑(t + 1)) || ev x0 t (e - ↑(t + 1) + 1)) = true
      have a1 : ev x0 t (e - ↑(t + 1) - 1) = false := h2 _ (by push_cast; omega)
      have a2 : ev x0 t (e - ↑(t + 1)) = false := h2 _ (by push_cast; omega)
      have a3 : e - ↑(t + 1) + 1 = e - ↑t := by push_cast; ring
      rw [a1, a2, a3, h1]; rfl
    · intro j hj
      show xor (ev x0 t (j - 1)) (ev x0 t j || ev x0 t (j + 1)) = false
      have b1 : ev x0 t (j - 1) = false := h2 _ (by push_cast at hj; omega)
      have b2 : ev x0 t j = false := h2 _ (by push_cast at hj; omega)
      have b3 : ev x0 t (j + 1) = false := h2 _ (by push_cast at hj; omega)
      rw [b1, b2, b3]; rfl

def Per (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) : Prop :=
  ∀ t : ℕ, a ≤ t → t + P ≤ b → ev x0 t k = ev x0 (t + P) k

lemma left (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 k P a b) (h1 : Per x0 (k + 1) P a b) :
    Per x0 (k - 1) P a (b - 1) := by
  intro t ht htb
  have inv : ∀ s : ℕ, ev x0 s (k - 1) = xor (ev x0 (s + 1) k) (ev x0 s k || ev x0 s (k + 1)) := by
    intro s
    show ev x0 s (k - 1) = xor (xor (ev x0 s (k - 1)) (ev x0 s k || ev x0 s (k + 1))) (ev x0 s k || ev x0 s (k + 1))
    cases ev x0 s (k - 1) <;> cases (ev x0 s k || ev x0 s (k + 1)) <;> rfl
  rw [inv t, inv (t + P)]
  have e1 : ev x0 (t + 1) k = ev x0 (t + 1 + P) k := h0 (t + 1) (by omega) (by omega)
  have e2 : ev x0 t k = ev x0 (t + P) k := h0 t ht (by omega)
  have e3 : ev x0 t (k + 1) = ev x0 (t + P) (k + 1) := h1 t ht (by omega)
  rw [e1, e2, e3, show t + 1 + P = t + P + 1 by ring]

lemma left_iter (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 k P a b) (h1 : Per x0 (k + 1) P a b) :
    ∀ j : ℕ, Per x0 (k - j) P a (b - j) ∧ Per x0 (k - j + 1) P a (b - j) := by
  intro j
  induction j with
  | zero => simpa using ⟨h0, h1⟩
  | succ j ih =>
    obtain ⟨g0, g1⟩ := ih
    have g := left x0 (k - j) P a (b - j) hP g0 (by simpa using g1)
    refine ⟨?_, ?_⟩
    · have : (k - ↑(j + 1)) = k - ↑j - 1 := by push_cast; ring
      rw [this, show b - (j + 1) = b - j - 1 by omega]; exact g
    · have e : (k - ↑(j + 1) + 1) = k - ↑j := by push_cast; ring
      rw [e, show b - (j + 1) = b - j - 1 by omega]
      intro t ht htb
      exact g0 t ht (by omega)

theorem theorem_A (x0 : ℤ → Bool) (c : ℤ) (L : ℕ) (hc : x0 (c - L) = true) (hl : ∀ j < c - L, x0 j = false)
    (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 c P a b) (h1 : Per x0 (c + 1) P a b) :
    b ≤ 2 * a + L + 2 * P - 1 := by
  by_contra hb
  push Not at hb
  set j : ℕ := a + P + L with hj
  have hper := (left_iter x0 c P a b hP h0 h1 j).1
  have E := edge x0 (c - L) hc hl
  have black : ev x0 (a + P) (c - j) = true := by
    have := (E (a + P)).1
    have e : c - ↑L - ↑(a + P) = c - ↑j := by rw [hj]; push_cast; ring
    rwa [e] at this
  have white : ev x0 a (c - j) = false := by
    have := (E a).2 (c - j) (by rw [hj]; push_cast; omega)
    exact this
  have := hper a le_rfl (by omega)
  rw [white, black] at this
  exact absurd this (by decide)

theorem no_two_periodic (x0 : ℤ → Bool) (c : ℤ) (L : ℕ) (hc : x0 (c - L) = true) (hl : ∀ j < c - L, x0 j = false)
    (P a : ℕ) (hP : 1 ≤ P)
    (h0 : ∀ t : ℕ, a ≤ t → ev x0 t c = ev x0 (t + P) c)
    (h1 : ∀ t : ℕ, a ≤ t → ev x0 t (c + 1) = ev x0 (t + P) (c + 1)) : False := by
  have := theorem_A x0 c L hc hl P a (2 * a + L + 2 * P) hP (fun t ht _ => h0 t ht) (fun t ht _ => h1 t ht)
  omega

/-- Evolution is a semigroup: evolving `ev x0 k` for `t` steps is evolving `x0` for `k + t`. -/
lemma ev_add (x0 : ℤ → Bool) (k t : ℕ) : ev (ev x0 k) t = ev x0 (k + t) := by
  induction t with
  | zero => rfl
  | succ t ih => show step (ev (ev x0 k) t) = step (ev x0 (k + t)); rw [ih]

/-! ## The strip of radius 6 -/

/-- Rule 30 on cells 1 .. 11 of a 13-cell row; the outer cells become 0. -/
def inner (r : ℕ) : ℕ := (((r <<< 1) ^^^ (r ||| (r >>> 1)))) &&& 4094

lemma inner_bits (r : ℕ) (_ : r < 8192) (j : ℕ) (hj : j < 13) : (inner r).testBit j =
    (if j = 0 ∨ j = 12 then false else xor (r.testBit (j - 1)) (r.testBit j || r.testBit (j + 1))) := by
  have h4094 : ∀ j < 13, (4094 : ℕ).testBit j = decide (j ≠ 0 ∧ j ≠ 12) := by decide
  unfold inner
  rw [Nat.testBit_and, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft, Nat.testBit_shiftRight,
    h4094 j hj]
  interval_cases j <;> simp [Nat.add_comm]

lemma inner_lt (r : ℕ) : inner r < 8192 := lt_of_le_of_lt Nat.and_le_right (by norm_num)

/-- The successors of row k with centre bit w, as a set. -/
def succSet (w k : ℕ) : ℕ :=
  if (inner k).testBit 6 == (w == 1) then
    (1 <<< inner k) ||| (1 <<< (inner k ||| 1)) ||| (1 <<< (inner k ||| 4096)) ||| (1 <<< (inner k ||| 4097))
  else 0

/-- The image of the set S (scanning every row; S stays one term throughout). -/
def imgAux (S w n : ℕ) : ℕ → ℕ :=
  Nat.rec (motive := fun _ => ℕ → ℕ) (fun acc => acc)
    (fun k ih acc => ih (if S.testBit k then acc ||| succSet w k else acc)) n

lemma imgAux_succ (S w n acc : ℕ) :
    imgAux S w (n + 1) acc = imgAux S w n (if S.testBit n then acc ||| succSet w n else acc) := rfl

def img (S w : ℕ) : ℕ := imgAux S w 8192 0

/-- The rows of S with a successor (centre w) in T. -/
def preAux (S T w n : ℕ) : ℕ → ℕ :=
  Nat.rec (motive := fun _ => ℕ → ℕ) (fun acc => acc)
    (fun k ih acc => ih (if S.testBit k && (succSet w k &&& T != 0) then acc ||| (1 <<< k) else acc)) n

lemma preAux_succ (S T w n acc : ℕ) : preAux S T w (n + 1) acc =
    preAux S T w n (if S.testBit n && (succSet w n &&& T != 0) then acc ||| (1 <<< n) else acc) := rfl

def pre (S T w : ℕ) : ℕ := preAux S T w 8192 0

/-- The column's bit at phase ph of the word 0 1^q. -/
def word (q ph : ℕ) : ℕ := if ph % (q + 1) = 0 then 0 else 1

/-- All rows with centre 0 (a scan of every row). -/
def zeroAux (n : ℕ) : ℕ → ℕ :=
  Nat.rec (motive := fun _ => ℕ → ℕ) (fun acc => acc)
    (fun k ih acc => ih (if k.testBit 6 then acc else acc ||| (1 <<< k))) n

lemma zeroAux_succ (n acc : ℕ) : zeroAux (n + 1) acc = zeroAux n (if n.testBit 6 then acc else acc ||| (1 <<< n)) :=
  rfl

def full0 : ℕ := zeroAux 8192 0

/-- Every member r < n of G has bit 5 equal to b (a scan of every row). -/
def allBit5 (G : ℕ) (b : Bool) (n : ℕ) : Bool :=
  Nat.rec (motive := fun _ => Bool) true (fun k ih => ih && (!(G.testBit k) || (k.testBit 5 == b))) n

/-- Cell c - 1 (bit 5) takes one value on G. -/
def colConst (G : ℕ) : Bool := allBit5 G false 8192 || allBit5 G true 8192

/-! ## Sets: membership -/

lemma testBit_one_shift (k : ℕ) : (1 <<< k).testBit k = true := by
  rw [Nat.one_shiftLeft]; exact Nat.testBit_two_pow_self

lemma acc_or (acc x y : ℕ) (h : acc.testBit y = true) : (acc ||| x).testBit y = true := by
  simp [Nat.testBit_or, h]

lemma imgAux_acc (S w : ℕ) : ∀ n acc y, acc.testBit y = true → (imgAux S w n acc).testBit y = true := by
  intro n
  induction n with
  | zero => intro acc y h; exact h
  | succ n ih =>
    intro acc y h
    rw [imgAux_succ]
    apply ih
    split_ifs
    · exact acc_or _ _ _ h
    · exact h

lemma imgAux_mem (S w : ℕ) : ∀ n acc s y, s < n → S.testBit s = true → (succSet w s).testBit y = true →
    (imgAux S w n acc).testBit y = true := by
  intro n
  induction n with
  | zero => intro acc s y hs; omega
  | succ n ih =>
    intro acc s y hs hS hy
    rw [imgAux_succ]
    rcases Nat.lt_succ_iff_lt_or_eq.mp hs with h | h
    · exact ih _ s y h hS hy
    · subst h
      apply imgAux_acc
      rw [if_pos hS]
      simp [Nat.testBit_or, hy]

lemma img_mem (S w s y : ℕ) (hs : s < 8192) (hS : S.testBit s = true) (hy : (succSet w s).testBit y = true) :
    (img S w).testBit y = true :=
  imgAux_mem S w 8192 0 s y hs hS hy

lemma preAux_acc (S T w : ℕ) : ∀ n acc y, acc.testBit y = true → (preAux S T w n acc).testBit y = true := by
  intro n
  induction n with
  | zero => intro acc y h; exact h
  | succ n ih =>
    intro acc y h
    rw [preAux_succ]
    apply ih
    split_ifs
    · exact acc_or _ _ _ h
    · exact h

lemma preAux_mem (S T w : ℕ) : ∀ n acc s y, s < n → S.testBit s = true → (succSet w s).testBit y = true →
    T.testBit y = true → (preAux S T w n acc).testBit s = true := by
  intro n
  induction n with
  | zero => intro acc s y hs; omega
  | succ n ih =>
    intro acc s y hs hS hy hT
    rw [preAux_succ]
    rcases Nat.lt_succ_iff_lt_or_eq.mp hs with h | h
    · exact ih _ s y h hS hy hT
    · subst h
      apply preAux_acc
      have hne : (succSet w s &&& T != 0) = true := by
        have : (succSet w s &&& T).testBit y = true := by simp [Nat.testBit_and, hy, hT]
        have h0 : succSet w s &&& T ≠ 0 := by
          intro h0; rw [h0, Nat.zero_testBit] at this; exact absurd this (by decide)
        simpa using h0
      rw [if_pos (by simp [hS, hne])]
      simp [Nat.testBit_or]

lemma pre_mem (S T w s y : ℕ) (hs : s < 8192) (hS : S.testBit s = true) (hy : (succSet w s).testBit y = true)
    (hT : T.testBit y = true) : (pre S T w).testBit s = true :=
  preAux_mem S T w 8192 0 s y hs hS hy hT

lemma zeroAux_acc : ∀ n acc y, acc.testBit y = true → (zeroAux n acc).testBit y = true := by
  intro n
  induction n with
  | zero => intro acc y h; exact h
  | succ n ih =>
    intro acc y h
    rw [zeroAux_succ]
    apply ih
    split_ifs
    · exact h
    · exact acc_or _ _ _ h

lemma zeroAux_mem : ∀ n acc r, r < n → r.testBit 6 = false → (zeroAux n acc).testBit r = true := by
  intro n
  induction n with
  | zero => intro acc r hr; omega
  | succ n ih =>
    intro acc r hr h6
    rw [zeroAux_succ]
    rcases Nat.lt_succ_iff_lt_or_eq.mp hr with h | h
    · exact ih _ r h h6
    · subst h
      apply zeroAux_acc
      rw [if_neg (by simp [h6])]
      simp [Nat.testBit_or]

lemma full0_mem (r : ℕ) (hr : r < 8192) (h6 : r.testBit 6 = false) : full0.testBit r = true :=
  zeroAux_mem 8192 0 r hr h6

lemma allBit5_spec (G : ℕ) (b : Bool) : ∀ n, allBit5 G b n = true → ∀ r < n, G.testBit r = true → r.testBit 5 = b := by
  intro n
  induction n with
  | zero => intro _ r hr; omega
  | succ n ih =>
    intro h r hr hG
    have h' : allBit5 G b n = true ∧ (!(G.testBit n) || (n.testBit 5 == b)) = true := by
      simpa [allBit5] using h
    rcases Nat.lt_succ_iff_lt_or_eq.mp hr with hlt | heq
    · exact ih h'.1 r hlt hG
    · subst heq
      have := h'.2
      simp [hG] at this
      exact this

/-! ## The actual strip -/

def enc (f : ℕ → Bool) : ℕ → ℕ
  | 0 => 0
  | k + 1 => Nat.bit (f 0) (enc (fun j => f (j + 1)) k)

lemma enc_lt (f : ℕ → Bool) (k : ℕ) : enc f k < 2 ^ k := by
  induction k generalizing f with
  | zero => simp [enc]
  | succ k ih =>
    have := ih (fun j => f (j + 1))
    simp only [enc]
    cases f 0 <;> simp [Nat.bit, pow_succ] <;> omega

lemma enc_testBit (f : ℕ → Bool) (k j : ℕ) : (enc f k).testBit j = (decide (j < k) && f j) := by
  induction k generalizing f j with
  | zero => simp [enc]
  | succ k ih =>
    rcases j with _ | j
    · simp [enc]
    · simp only [enc, Nat.testBit_bit_succ, ih]
      simp

def win (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) : ℕ := enc (fun j => ev x0 t (c - 6 + j)) 13

lemma win_lt (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) : win x0 c t < 8192 := enc_lt _ 13

lemma win_bit (x0 : ℤ → Bool) (c : ℤ) (t j : ℕ) (hj : j < 13) : (win x0 c t).testBit j = ev x0 t (c - 6 + j) := by
  simp [win, enc_testBit, hj]

lemma toNat_bit0 (b : Bool) : (b.toNat).testBit 0 = b := by cases b <;> rfl

lemma toNat_bit_pos (b : Bool) (j : ℕ) (hj : 1 ≤ j) : (b.toNat).testBit j = false := by
  cases b
  · simp
  · simp only [Bool.toNat_true]
    exact Nat.testBit_eq_false_of_lt (lt_of_lt_of_le (by norm_num) (Nat.pow_le_pow_right (by norm_num) hj))

lemma shl12_bit (b : Bool) (j : ℕ) : ((b.toNat) <<< 12).testBit j = (decide (j = 12) && b) := by
  rw [Nat.testBit_shiftLeft]
  by_cases h : j = 12
  · subst h; cases b <;> decide
  · by_cases h2 : 12 ≤ j
    · rw [toNat_bit_pos b (j - 12) (by omega)]; simp [h]
    · simp [h, h2]

/-- The next row is the inner update of this one, with the actual outer cells. -/
lemma win_step (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) :
    win x0 c (t + 1) = inner (win x0 c t) ||| (ev x0 (t + 1) (c - 6)).toNat ||| ((ev x0 (t + 1) (c + 6)).toNat <<< 12) := by
  apply Nat.eq_of_testBit_eq
  intro j
  by_cases hj : j < 13
  · rw [win_bit x0 c (t + 1) j hj]
    simp only [Nat.testBit_or, shl12_bit]
    rw [inner_bits _ (win_lt x0 c t) j hj]
    rcases (show j = 0 ∨ j = 12 ∨ (1 ≤ j ∧ j ≤ 11) by omega) with h | h | h
    · subst h
      rw [toNat_bit0]
      simp
    · subst h
      rw [toNat_bit_pos _ 12 (by norm_num), show c - 6 + ((12 : ℕ) : ℤ) = c + 6 by push_cast; ring]
      simp
    · rw [if_neg (by omega), toNat_bit_pos _ j h.1, show (decide (j = 12)) = false by simp; omega]
      simp only [Bool.or_false, Bool.false_and]
      rw [win_bit x0 c t (j - 1) (by omega), win_bit x0 c t j hj, win_bit x0 c t (j + 1) (by omega)]
      have hstep : ev x0 (t + 1) (c - 6 + (j : ℤ)) =
          xor (ev x0 t (c - 6 + (j : ℤ) - 1)) (ev x0 t (c - 6 + (j : ℤ)) || ev x0 t (c - 6 + (j : ℤ) + 1)) := rfl
      rw [hstep, show c - 6 + ((j - 1 : ℕ) : ℤ) = c - 6 + (j : ℤ) - 1 by push_cast [show 1 ≤ j by omega]; ring,
        show c - 6 + ((j + 1 : ℕ) : ℤ) = c - 6 + (j : ℤ) + 1 by push_cast; ring]
  · have h256 : 8192 ≤ 2 ^ j := by
      calc 8192 = 2 ^ 13 := by norm_num
        _ ≤ 2 ^ j := Nat.pow_le_pow_right (by norm_num) (by omega)
    have h1 : inner (win x0 c t) < 2 ^ 13 := by have := inner_lt (win x0 c t); norm_num; exact this
    have h2 : (ev x0 (t + 1) (c - 6)).toNat < 2 ^ 13 := lt_of_le_of_lt (Bool.toNat_le _) (by norm_num)
    have h3 : (ev x0 (t + 1) (c + 6)).toNat <<< 12 < 2 ^ 13 := by
      rw [Nat.shiftLeft_eq]
      have := Bool.toNat_le (ev x0 (t + 1) (c + 6))
      calc (ev x0 (t + 1) (c + 6)).toNat * 2 ^ 12 ≤ 1 * 2 ^ 12 := Nat.mul_le_mul_right _ this
        _ < 2 ^ 13 := by norm_num
    have hR := Nat.or_lt_two_pow (Nat.or_lt_two_pow h1 h2) h3
    rw [Nat.testBit_eq_false_of_lt (lt_of_lt_of_le (win_lt x0 c (t + 1)) h256),
      Nat.testBit_eq_false_of_lt (lt_of_lt_of_le hR (by norm_num at h256 ⊢; omega))]

/-- The column's next bit is the inner update's centre. -/
lemma centre_next (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) : (inner (win x0 c t)).testBit 6 = ev x0 (t + 1) c := by
  rw [inner_bits _ (win_lt x0 c t) 6 (by norm_num), if_neg (by omega), win_bit x0 c t 5 (by norm_num),
    win_bit x0 c t 6 (by norm_num), win_bit x0 c t 7 (by norm_num)]
  show _ = xor (ev x0 t (c - 1)) (ev x0 t c || ev x0 t (c + 1))
  rw [show c - 6 + ((5 : ℕ) : ℤ) = c - 1 by push_cast; ring, show c - 6 + ((6 : ℕ) : ℤ) = c by push_cast; ring,
    show c - 6 + ((7 : ℕ) : ℤ) = c + 1 by push_cast; ring]

lemma four_mem (a x : ℕ) (h : x = a ∨ x = (a ||| 1) ∨ x = (a ||| 4096) ∨ x = (a ||| 4097)) :
    ((1 <<< a) ||| (1 <<< (a ||| 1)) ||| (1 <<< (a ||| 4096)) ||| (1 <<< (a ||| 4097))).testBit x = true := by
  rcases h with h | h | h | h <;> subst h <;> simp [Nat.testBit_or]

/-- The actual next row is a successor of the actual row, under the column's actual next bit. -/
lemma succ_mem (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) :
    (succSet (ev x0 (t + 1) c).toNat (win x0 c t)).testBit (win x0 c (t + 1)) = true := by
  have hc := centre_next x0 c t
  unfold succSet
  rw [if_pos (by cases hb : ev x0 (t + 1) c <;> simp [hb, hc])]
  apply four_mem
  rw [win_step]
  have e1 : ∀ x : ℕ, x ||| 1 ||| 4096 = x ||| 4097 := fun x => by rw [Nat.or_assoc]; rfl
  cases ev x0 (t + 1) (c - 6) <;> cases ev x0 (t + 1) (c + 6) <;> simp [e1]

lemma colConst_spec (G : ℕ) (h : colConst G = true) (r s : ℕ) (hr : r < 8192) (hs : s < 8192)
    (hGr : G.testBit r = true) (hGs : G.testBit s = true) : r.testBit 5 = s.testBit 5 := by
  simp only [colConst, Bool.or_eq_true] at h
  rcases h with h | h
  · rw [allBit5_spec G false 8192 h r hr hGr, allBit5_spec G false 8192 h s hs hGs]
  · rw [allBit5_spec G true 8192 h r hr hGr, allBit5_spec G true 8192 h s hs hGs]

end BlackEnd38
